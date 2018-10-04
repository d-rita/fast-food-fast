"""Module to test Orders model and views"""
from tests.base_test import BaseTestCase
import psycopg2
from api.models.db import DatabaseConnection
from api.views import menu_views

class TestMenus(BaseTestCase):
    def test_get_menu(self):
        self.add_menu(1, 'Pizza', 12000)
        resp = self.get_menus()
        self.assertEqual(resp.status_code, 200)

    def test_add_menu_option(self):
        resp = self.add_menu(1, 'Pizza', 12000)
        self.assertEqual(resp.status_code, 201)

    def test_cannot_get_non_existing_menu(self):
        resp = self.get_menus()
        self.assertEqual(resp.status_code, 404)

 
        
