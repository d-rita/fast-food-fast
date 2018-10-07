"""Module to test Orders model and views"""
from tests.base_test import BaseTestCase


from api.views import menu_views

class TestMenus(BaseTestCase):
    def test_get_menu(self):
        self.add_menu(1, 'Pizza', 12000)
        resp = self.get_menus()
        self.assertEqual(resp.status_code, 200)

    def test_add_menu_option(self):
        self.add_menu(1, 'Pizza', 12000)
        resp = self.get_menus()
        self.assertEqual(resp.status_code, 201)

    def test_cannot_get_non_existing_menu(self):
        resp = self.get_menus()
        self.assertEqual(resp.status_code, 404)

    def test_get_orders_not_admin(self):
        resp = self.get_orders()
        self.assertEqual(resp.status_code, 401)

    def test_get_existing_order(self):
        self.add_order('Bunga', '12/03/2018', 'New', 1, 2)
        resp = self.get_an_order(1)
        self.assertEqual(resp.status_code, 200)

    def test_get_nonexisting_order(self):
        resp = self.get_orders()
        self.assertEqual(resp.status_code, 404)
    
    def test_add_an_order(self):
        resp = self.add_order('Bunga', '12/03/2018', 'New', 1, 2)
        self.assertEqual(resp.status_code, 201)

 
        
