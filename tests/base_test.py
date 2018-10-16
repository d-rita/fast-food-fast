"""BaseTest module"""
import unittest
import  json
import os

from api import app
from api.models.db import DatabaseConnection

test_db = DatabaseConnection()


class BaseTestCase(unittest.TestCase):
    """Parent class with initial setup of test client and test database"""

    def setUp(self):
        self.client = app.test_client(self)
        test_db.create_all_tables()

    def signup_user(self):
        return self.client.post('api/v1/auth/signup', 
        data=json.dumps(dict(
            username='Diana',
            password='hogwarts',
            email='diana@gmail.com', 
            admin=False
        )),
        content_type='application/json')

    def login_user(self):
        self.client.post('api/v1/auth/signup', 
        data=json.dumps(dict(
            username='Diana',
            password='hogwarts',
            email='diana@gmail.com', 
            admin=False
        )),
        content_type='application/json')
        response = self.client.post('api/v1/auth/login', 
        data=json.dumps(dict(
            username='Diana', 
            password='hogwarts'
            )
        ),
        content_type='application/json')
        token = json.loads(response.data.decode())["token"]
        return token


    def login_admin(self):
        self.client.post('api/v1/auth/signup', 
        data=json.dumps(dict(
            username='Rita',
            password='hedwig',
            email='rita@gmail.com', 
            admin=True
        )),
        content_type='application/json')
        response = self.client.post('api/v1/auth/login', 
        data=json.dumps(dict(
            username='Rita', 
            password='hedwig'
            )
        ),
        content_type='application/json')
        token = json.loads(response.data.decode())["token"]
        return token

    def tearDown(self):
        test_db.delete_all_tables()

