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

class TestAuthAPIs(BaseTestCase):
    """
    Contains methods to test the signup and login API endpoints
    """

    def test_signup_not_in_json(self):
        """Tests to check if signup request data is in json format"""
        response = self.client.post('api/v1/auth/signup', 
        data=json.dumps(dict(
            username="Rita",
            password="hedwig",
            email="rita@gmail.com", 
            admin="False"
        )),
        content_type='HTML')
        self.assertEqual(response.status_code, 400)
    
    def test_add_a_user(self):
        """Tests if a user can successfully be added"""
        response = self.client.post('api/v1/auth/signup', 
        data=json.dumps(dict(
            username="Rita",
            password="hedwig",
            email="rita@gmail.com", 
            admin="False"
        )),
        content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_cannot_add_user_without_name(self):
        """Tests that a user cannot be added without a name"""
        response = self.client.post('api/v1/auth/signup', 
        data=json.dumps(dict(
            username="",
            password="hedwig",
            email="rita@gmail.com",
            admin="False"
        )),
        content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_cannot_add_user_with_invalid_name(self):
        """Tests to ensure username contains only letters"""
        response = self.client.post('api/v1/auth/signup', 
        data=json.dumps(dict(
            username="12345",
            password="hedwig",
            email="rita@gmail.com",
            admin="False"
        )),
        content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_cannot_add_user_without_email(self):
        """Tests that a user cannot be added without an email"""
        response = self.client.post('api/v1/auth/signup', 
        data=json.dumps(dict(
            username="Rita",
            password="hedwig",
            email="",
            admin="False"
        )),
        content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_cannot_add_user_with_invalid_email(self):
        """Tests that user email is of the correct foramt"""
        response = self.client.post('api/v1/auth/signup', 
        data=json.dumps(dict(
            username="Rita",
            password="hedwig",
            email="@123.com@gmail",
            admin="False"
        )),
        content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_cannot_add_user_with_invalid_password(self):
        """Tests that password input is of the proper length before being accepted"""
        response = self.client.post('api/v1/auth/signup', 
        data=json.dumps(dict(
            username="Rita",
            password="worlddomination",
            email="rita@gmail.com",
            admin="False"
        )),
        content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_cannot_add_user_without_password(self):
        """Tests that there is a password provided before signup"""
        response = self.client.post('api/v1/auth/signup', 
        data=json.dumps(dict(
            username="12345",
            password="",
            email="rita@gmail.com",
            admin="False"
        )),
        content_type='application/json')
        self.assertEqual(response.status_code, 400)


    def test_cannot_add_user_with_missing_parameter(self):
        """Tests to ensure all parameters have been filled in"""
        response = self.client.post('api/v1/auth/signup', 
        data=json.dumps(dict(
            password="hedwig",
            email="rita@gmail.com",
            admin="False"
        )),
        content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_user_login_not_in_json(self):
        """Test that login data is in json format"""
        response = self.client.post('api/v1/auth/login', 
        data=json.dumps(dict(
            password="hedwig",
            username="Rita"
            )
        ),
        content_type='HTML')
        self.assertEqual(response.status_code, 400)

    def test_can_login_user(self):
        """Test if a user can successfully be logged in"""
        self.client.post('api/v1/auth/signup', 
        data=json.dumps(dict(
            username="Rita",
            password="hedwig",
            email="rita@gmail.com", 
            admin="False"
        )),
        content_type='application/json')

        response =  self.client.post('api/v1/auth/login', 
        data=json.dumps(dict(
            username="Rita", 
            password="hedwig"
            )
        ),
        content_type='application/json')
        self.assertEqual(response.status_code, 200)


    def test_invalid_user_login(self):
        """Tests for non signed up user logging in"""
        response = self.client.post('api/v1/auth/login', 
        data=json.dumps(dict(
            password="we",
            username="Rita"
            )
        ),
        content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_invalid_password_login(self):
        """Tests to ensure that password matches username"""
        self.client.post('api/v1/auth/signup', 
        data=json.dumps(dict(
            username="Rita",
            password="hedwig",
            email="rita@gmail.com", 
            admin="False"
        )),
        content_type='application/json')
        response = self.client.post('api/v1/auth/login', 
        data=json.dumps(dict(
            password="we",
            username="Rita"
            )
        ),
        content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_invalid_username_login(self):
        """Tests if usename matches password"""
        self.client.post('api/v1/auth/signup', 
        data=json.dumps(dict(
            username="Rita",
            password="hedwig",
            email="rita@gmail.com", 
            admin="False"
        )),
        content_type='application/json')
        response = self.client.post('api/v1/auth/login', 
        data=json.dumps(dict(
            password="hedwig",
            username="Hellen"
            )
        ),
        content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_missing_parameter_user_login(self):
        """Tests to ensure both fields are filled in before login"""
        response = self.client.post('api/v1/auth/login', 
        data=json.dumps(dict(
            username="Rita"
            )
        ),
        content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def tearDown(self):
        test_db.delete_all_tables()

