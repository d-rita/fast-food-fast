"""BaseTest module"""
import unittest
import  json
import psycopg2
from api import app

from api.views import user_views, order_views, auth, menu_views


class BaseTestCase(unittest.TestCase):
    """Parent class with initial setup of test client and test database"""

    def setUp(self):
        self.client = app.test_client(self)

    def add_menu(self, menuid, name, price ):
        """Defines from post method in JSON format"""
        return self.client.post('/api/v1/menus',
            data=json.dumps(dict(
                menuid=menuid,
                name=name,
                price=price
            )
        ),
        content_type='application/json')

    def add_order(self, location, date, status, food_id, user_id):
        """Defines from post method in JSON format"""
        return self.client.post('/api/v1/users/orders',
            data=json.dumps(dict(
                # order_id=order_id,
                location=location,
                date=date,
                status=status,
                food_id=food_id,
                user_id=user_id
            )
        ),
        content_type='application/json')

    def get_menus(self):
        """Return all menu options"""
        return self.client.get('/api/v1/menus')

    def get_orders(self):
        return self.client.get('/api/v1/orders')
    
    def get_an_order(self, order_id):
        return self.client.get('/api/v1/orders/1')

class TestAuthViews(BaseTestCase):
    
    def test_add_a_user(self):
        response = self.client.post('api/v1/auth/signup', 
        data=json.dumps(dict(
            username="Rita",
            password="hedwig",
            email="rita@gmail.com"
        )),
        content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_cannot_add_user_without_name(self):
        response = self.client.post('api/v1/auth/signup', 
        data=json.dumps(dict(
            username="",
            password="hedwig",
            email="rita@gmail.com"
        )),
        content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_cannot_add_user_with_non_letter_name(self):
        response = self.client.post('api/v1/auth/signup', 
        data=json.dumps(dict(
            username="12345",
            password="hedwig",
            email="rita@gmail.com"
        )),
        content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_cannot_add_user_with_invalid_email(self):
        response = self.client.post('api/v1/auth/signup', 
        data=json.dumps(dict(
            username="Rita",
            password="hedwig",
            email="@123.com@gmail"
        )),
        content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_cannot_add_user_with_invalid_password(self):
        response = self.client.post('api/v1/auth/signup', 
        data=json.dumps(dict(
            username="Rita",
            password="worlddomination",
            email="rita@gmail.com"
        )),
        content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_cannot_add_user_with_missing_parameter(self):
        response = self.client.post('api/v1/auth/signup', 
        data=json.dumps(dict(
            password="hedwig",
            email="rita@gmail.com"
        )),
        content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_invalid_user_login(self):
        response = self.client.post('api/v1/auth/login', 
        data=json.dumps(dict(
            password="we",
            username="Rita"
            )
        ),
        content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_missing_parameter_user_login(self):
        response = self.client.post('api/v1/auth/login', 
        data=json.dumps(dict(
            username="Rita"
            )
        ),
        content_type='application/json')
        self.assertEqual(response.status_code, 400)

