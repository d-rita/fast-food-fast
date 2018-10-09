"""Module to test Orders model and views"""
from tests.base_test import BaseTestCase


from api.views import menu_views

class TestMenus(BaseTestCase):

    def test_get_orders_not_admin(self):
        resp = self.get_orders()
        self.assertEqual(resp.status_code, 401)

    
    def test_add_an_order_not_logged_in(self):
        resp = self.add_order(1, 'Bunga', '12/03/2018', 'New', 1, 2)
        self.assertEqual(resp.status_code, 401)

 
        
