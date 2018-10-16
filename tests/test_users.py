from tests.base_test import BaseTestCase
import json

class TestUsersAPIs(BaseTestCase):


    def test_retrieve_empty_user_order_history(self):
        """Test to retrieve a particular user's empty order history """
        response = self.client.get('api/v1/users/orders', 
        headers=dict(Authorization='Bearer '+ self.login_user()),
        content_type='application/json')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'You have no order history', response.data)

    def test_user_add_order(self):
        """Test that user can place an order"""
        self.client.post('/api/v1/menu',
            headers=dict(Authorization='Bearer ' + self.login_admin()),
            data=json.dumps(dict(
                name='Burger',
                price=12000
            )
        ),
        content_type='application/json')
        response1 = self.client.post('/api/v1/users/orders',
        headers=dict(Authorization='Bearer '+ self.login_user()),
        data=json.dumps(dict(
                location='Bunga',
                food_id=1
        )),
        content_type='application/json')
        self.assertEqual(response1.status_code, 201)
        self.assertIn(b'Created one food order', response1.data)

    def test_user_cannot_add_order_with_unknown_food(self):
        """Test that user cannot place an order for food that does not exist"""
        response1 = self.client.post('/api/v1/users/orders',
        headers=dict(Authorization='Bearer '+ self.login_user()),
        data=json.dumps(dict(
                location='Bunga',
                food_id=101
        )),
        content_type='application/json')
        self.assertEqual(response1.status_code, 404)
        self.assertIn(b'Food is not on the menu', response1.data)

    def test_user_cannot_add_order_without_food(self):
        """Test that user cannot place an order without food"""
        self.client.post('/api/v1/menu',
            headers=dict(Authorization='Bearer ' + self.login_admin()),
            data=json.dumps(dict(
                name='Burger',
                price=12000
            )
        ),
        content_type='application/json')
        response1 = self.client.post('/api/v1/users/orders',
        headers=dict(Authorization='Bearer '+ self.login_user()),
        data=json.dumps(dict(
                location='Bunga',
                food_id=''
        )),
        content_type='application/json')
        self.assertEqual(response1.status_code, 400)
        self.assertIn(b'Fill in the menu_id', response1.data)

    def test_user_cannot_add_order_with_invalid_food_id(self):
        """Test that user cannot place an order without food"""
        self.client.post('/api/v1/menu',
            headers=dict(Authorization='Bearer ' + self.login_admin()),
            data=json.dumps(dict(
                name='Burger',
                price=12000
            )
        ),
        content_type='application/json')
        response1 = self.client.post('/api/v1/users/orders',
        headers=dict(Authorization='Bearer '+ self.login_user()),
        data=json.dumps(dict(
                location='Bunga',
                food_id='two'
        )),
        content_type='application/json')
        self.assertEqual(response1.status_code, 400)
        self.assertIn(b'Id must be an integer', response1.data)

    def test_user_cannot_add_order_with_empty_location(self):
        """Test that user cannot place an order without location"""
        self.client.post('/api/v1/menu',
            headers=dict(Authorization='Bearer ' + self.login_admin()),
            data=json.dumps(dict(
                name='Burger',
                price=12000
            )
        ),
        content_type='application/json')
        response1 = self.client.post('/api/v1/users/orders',
        headers=dict(Authorization='Bearer '+ self.login_user()),
        data=json.dumps(dict(
                location='',
                food_id='two'
        )),
        content_type='application/json')
        self.assertEqual(response1.status_code, 400)
        self.assertIn(b'Fill in the location', response1.data)

    
    def test_user_cannot_add_order_with_invalid_location(self):
        """Test that user cannot place an order with location of non string type"""
        self.client.post('/api/v1/menu',
            headers=dict(Authorization='Bearer ' + self.login_admin()),
            data=json.dumps(dict(
                name='Burger',
                price=12000
            )
        ),
        content_type='application/json')
        response1 = self.client.post('/api/v1/users/orders',
        headers=dict(Authorization='Bearer '+ self.login_user()),
        data=json.dumps(dict(
                location=2345,
                food_id=1        )),
        content_type='application/json')
        self.assertEqual(response1.status_code, 400)
        self.assertIn(b'Invalid location', response1.data)

    def test_user_cannot_add_order_with_missing_parameter(self):
        """Test that user cannot place an order with missing parameter"""
        self.client.post('/api/v1/menu',
            headers=dict(Authorization='Bearer ' + self.login_admin()),
            data=json.dumps(dict(
                name='Burger',
                price=12000
            )
        ),
        content_type='application/json')
        response1 = self.client.post('/api/v1/users/orders',
        headers=dict(Authorization='Bearer '+ self.login_user()),
        data=json.dumps(dict(
                food_id=1        )),
        content_type='application/json')
        self.assertEqual(response1.status_code, 400)
        self.assertIn(b'Missing parameter: fill in location and food_id', response1.data)

    def test_retrieve_user_order_history(self):
        """Test to retrieve a particular user's order history """
        self.client.post('/api/v1/menu',
            headers=dict(Authorization='Bearer ' + self.login_admin()),
            data=json.dumps(dict(
                name='Burger',
                price=12000
            )
        ),
        content_type='application/json')
        self.client.post('/api/v1/users/orders',
        headers=dict(Authorization='Bearer '+ self.login_user()),
        data=json.dumps(dict(
                location='Bunga',
                food_id=1
        )),
        content_type='application/json')
        response = self.client.get('api/v1/users/orders', 
        headers=dict(Authorization='Bearer '+ self.login_user()),
        content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Your order history has been returned', response.data)