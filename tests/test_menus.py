import json 
from tests.base_test import BaseTestCase
from api.models.db import DatabaseConnection

test_db = DatabaseConnection()


class TestMenusAPIs(BaseTestCase):
    """This class contains tests for the menus API endpoints"""

    def test_add_food_not_json_data(self):
        """Tests that food can be added by admin"""
        resp1 = self.client.post('/api/v1/menu',
            headers=dict(Authorization='Bearer ' + self.login_admin()),
            data=json.dumps(dict(
                name='Burger',
                price=12000
            )
        ),
        content_type='HTML')
        self.assertEqual(resp1.status_code, 400)
        self.assertIn(b'Data should be in json format!', resp1.data)

    def test_add_food_non_admin(self):
        """Tests that food cannot be added by non admin"""
        resp1 = self.client.post('/api/v1/menu',
            headers=dict(Authorization='Bearer ' + self.login_user()),
            data=json.dumps(dict(
                name='Burger',
                price=12000
            )
        ),
        content_type='application/json')
        self.assertEqual(resp1.status_code, 401)
        self.assertIn(b'Only admins allowed', resp1.data)

    def test_add_food(self):
        """Tests that food can be added by admin"""
        resp1 = self.client.post('/api/v1/menu',
            headers=dict(Authorization='Bearer ' + self.login_admin()),
            data=json.dumps(dict(
                name='Burger',
                price=12000
            )
        ),
        content_type='application/json')
        self.assertEqual(resp1.status_code, 201)
        self.assertIn(b'Food successfully added!', resp1.data)

    def test_cannot_add_food_twice(self):
        """Tests that food cannot be added more than once by admin"""
        self.client.post('/api/v1/menu',
            headers=dict(Authorization='Bearer ' + self.login_admin()),
            data=json.dumps(dict(
                name='Burger',
                price=12000
            )
        ),
        content_type='application/json')
        resp1 = self.client.post('/api/v1/menu',
            headers=dict(Authorization='Bearer ' + self.login_admin()),
            data=json.dumps(dict(
                name='Burger',
                price=12000
            )
        ),
        content_type='application/json')
        self.assertEqual(resp1.status_code, 400)
        self.assertIn(b'Food already exists on the menu', resp1.data)

    def test_cannot_add_food_empty_name(self):
        """Tests that food cannot be added without name"""
        resp1 = self.client.post('/api/v1/menu',
            headers=dict(Authorization='Bearer ' + self.login_admin()),
            data=json.dumps(dict(
                name='',
                price=12000
            )
        ),
        content_type='application/json')
        self.assertEqual(resp1.status_code, 400)
        self.assertIn(b'Fill in food name', resp1.data)

    def test_cannot_add_food_invalid_name(self):
        """Tests that food cannot be added with invalid food name"""
        resp1 = self.client.post('/api/v1/menu',
            headers=dict(Authorization='Bearer ' + self.login_admin()),
            data=json.dumps(dict(
                name=12345,
                price=12000
            )
        ),
        content_type='application/json')
        self.assertEqual(resp1.status_code, 400)
        self.assertIn(b'Please enter letters only', resp1.data)

    def test_cannot_add_food_invalid_prcie(self):
        """Tests that food cannot be added with invalid food price"""
        resp1 = self.client.post('/api/v1/menu',
            headers=dict(Authorization='Bearer ' + self.login_admin()),
            data=json.dumps(dict(
                name='Burger',
                price='twelve'
            )
        ),
        content_type='application/json')
        self.assertEqual(resp1.status_code, 400)
        self.assertIn(b'Please enter numbers only', resp1.data)

    def test_cannot_add_food_empty_price(self):
        """Tests that food cannot be added without price"""
        resp1 = self.client.post('/api/v1/menu',
            headers=dict(Authorization='Bearer ' + self.login_admin()),
            data=json.dumps(dict(
                name='Burger',
                price=''
            )
        ),
        content_type='application/json')
        self.assertEqual(resp1.status_code, 400)
        self.assertIn(b'Fill in food price', resp1.data)

    def test_cannot_add_food_missing_parameter(self):
        """Tests that food cannot be added with missing parameter"""
        resp1 = self.client.post('/api/v1/menu',
            headers=dict(Authorization='Bearer ' + self.login_admin()),
            data=json.dumps(dict(
                name='Burger'
            )
        ),
        content_type='application/json')
        self.assertEqual(resp1.status_code, 400)
        self.assertIn(b'Fill in all parameters: name and price', resp1.data)

    def test_return_menu(self):
        self.client.post('/api/v1/menu',
            headers=dict(Authorization='Bearer ' + self.login_admin()),
            data=json.dumps(dict(
                name='Burger',
                price=12000
            )
        ),
        content_type='application/json')
        self.client.post('/api/v1/menu',
            headers=dict(Authorization='Bearer ' + self.login_admin()),
            data=json.dumps(dict(
                name='Braai',
                price=20000
            )
        ),
        content_type='application/json')
        resp1 = self.client.get('api/v1/menu', 
        headers=dict(Authorization='Bearer ' + self.login_user()), 
        content_type='application/json')
        self.assertEqual(resp1.status_code, 200)
        self.assertIn(b'Menu successfully returned', resp1.data)