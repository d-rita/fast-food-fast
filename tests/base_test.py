"""BaseTest module"""
import unittest
import psycopg2
from api import app
from api.models.db import DatabaseConnection
from config import TestingConfig

class BaseTestCase(unittest.TestCase):
    """Parent class with initial setup of test client and test database"""
    conn = psycopg2.connect(database="testdb", user="postgres", password="diana", host="localhost")
    test_db = DatabaseConnection()

    def setUp(self):
        #self.app = config(TestingConfig)
        self.client = app.test_client(self)
        self.test_db.create_all_tables()

    def tearDown(self):
        self.test_db.delete_all_tables()

