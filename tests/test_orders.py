"""Module to test Orders model and views"""
from tests.base_test import BaseTestCase
import json

class TestOrdersAPIs(BaseTestCase):
    
   #get all orders
    def test_get_all_orders_not_admin(self):
        """Test that non admin cannot get all orders """
        response1 = self.client.get('/api/v1/orders',
        headers=dict(Authorization='Bearer '+ self.login_user()),
        content_type='application/json')
        self.assertEqual(response1.status_code, 401)
        self.assertIn(b'Only an admin can access all orders', response1.data)


    def test_get_non_existing_orders(self):
        """Tests that an admin cannot retrieve empty orders list"""
        response1 = self.client.get('/api/v1/orders',
        headers=dict(Authorization='Bearer '+ self.login_admin()),
        content_type='application/json')
        self.assertEqual(response1.status_code, 404)
        self.assertIn(b'There are no orders', response1.data)

    def test_get_non_existing_order_not_admin(self):
        """Tests that non admin cannot retrieve a particular order"""
        response1 = self.client.get('/api/v1/orders/1',
        headers=dict(Authorization='Bearer '+ self.login_user()),
        content_type='application/json')
        self.assertEqual(response1.status_code, 401)
        self.assertIn(b'Only an admin can access all orders', response1.data)


    def test_get_non_existing_order(self):
        """Test that admin cannot retrieve non existent order"""
        response1 = self.client.get('/api/v1/orders/1',
        headers=dict(Authorization='Bearer '+ self.login_admin()),
        content_type='application/json')
        self.assertEqual(response1.status_code, 404)
        self.assertIn(b'Order does not exist', response1.data)

    def test_get_existing_orders(self):
        """Test to retrieve all orders by admin"""
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
        self.client.post('/api/v1/users/orders',
        headers=dict(Authorization='Bearer '+ self.login_user()),
        data=json.dumps(dict(
                location='Kamwokya',
                food_id=1
        )),
        content_type='application/json')
        response = self.client.get('/api/v1/orders',
        headers=dict(Authorization='Bearer '+ self.login_admin()),
        content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'All orders are returned!', response.data)

    def test_get_specific_order(self):
        """Test to retrieve a specific order by admin"""
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
        response = self.client.get('/api/v1/orders/1',
        headers=dict(Authorization='Bearer '+ self.login_admin()),
        content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'One order has been returned', response.data)

    def test_update_order_status(self):
        """Test to update order status by admin"""
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
        response = self.client.put('/api/v1/orders/1',
        headers=dict(Authorization='Bearer '+ self.login_admin()),
        data=json.dumps(dict(
            order_status='Processing'
        )),
        content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Order status updated', response.data)

    def test_update_order_status_non_admin(self):
        """Test to update order status by non  admin"""
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
        response = self.client.put('/api/v1/orders/1',
        headers=dict(Authorization='Bearer '+ self.login_user()),
        data=json.dumps(dict(
            order_status='Processing'
        )),
        content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertIn(b'Only an admin can access all orders', response.data)