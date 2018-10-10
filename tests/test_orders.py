"""Module to test Orders model and views"""
from tests.base_test import BaseTestCase
import json


#from api.views import menu_views

class TestOrders(BaseTestCase):


   #get all orders
    def test_get_all_orders_not_admin(self):
        self.signup_user('Diana', 'meclient', 'diana@gmail.com', False)
        response1 = self.login_user('Diana', 'meclient')
        self.token = json.loads(response1.data.decode())["token"]
        response2 = self.client.get('/api/v1/orders',
        headers=dict(Authorization='Bearer ' + self.token),
        content_type='application/json')
        self.assertEqual(response2.status_code, 401)

    def test_get_non_existing_orders(self):
        self.signup_user('Rita', 'hedwig', 'rita@gmail.com', True)
        response1 = self.login_user('Rita', 'hedwig')
        data = json.loads(response1.data.decode())
        self.token = data.get('token')
        response2 = self.client.get('/api/v1/orders',
        headers=({'token': self.token}),
        content_type='application/json')
        self.assertEqual(response2.status_code, 404)

    def test_get_existing_orders(self):
        self.signup_user('Rita', 'hedwig', 'rita@gmail.com', True)
        response1 = self.login_user('Rita', 'hedwig')
        data = json.loads(response1.data.decode())
        self.token = data.get('token')
        self.add_order(self.token, 1, 'Bunga', '12/03/2018', 'New', 1, 1)
        self.add_order(self.token, 2, 'Bunamwaya', '12/10/2018', 'New', 1, 1)
        response2 = self.client.get('/api/v1/orders',
        headers=({'token': self.token}),
        content_type='application/json')
        self.assertEqual(response2.status_code, 404)


    #add an order
    def test_add_an_order_not_logged_in(self):
        resp = self.add_order(1, 'Bunga', '12/03/2018', 'New', 1, 2)
        self.assertEqual(resp.status_code, 401)

    #get an order



