"""BaseTest module"""
import unittest
import  json
import psycopg2
from api import app
from api.models.db import DatabaseConnection
from config import TestingConfig


class BaseTestCase(unittest.TestCase):
    """Parent class with initial setup of test client and test database"""
    #conn = psycopg2.connect(database="testdb", user="postgres", password="diana", host="localhost")
    #test_db = DatabaseConnection()
    def create_test_app(self):
        app.config.from_object(TestingConfig)

    def setUp(self):
        self.client = app.test_client(self)
        #self.test_db.create_all_tables()
        
    #def tearDown(self):
        #self.test_db.delete_all_tables()

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

    def add_order(self, order_id, location, date, status, food_id, user_id):
        """Defines from post method in JSON format"""
        return self.client.post('/api/v1/users/orders',
            data=json.dumps(dict(
                order_id=order_id,
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


