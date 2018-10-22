from flask import json

from tests.base_test import BaseTestCase


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
            admin=True
        )),
        content_type='HTML')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Data should be in JSON format', response.data)
    
    def test_add_a_user(self):
        """Tests if a user can successfully be added"""
        response = self.client.post('api/v1/auth/signup', 
        data=json.dumps(dict(
            username='Diana',
            password='hogwarts',
            email='diana@gmail.com', 
            admin=False,
        )),
        content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'New user added', response.data)

    def test_cannot_add_user_without_name(self):
        """Tests that a user cannot be added without a name"""
        response = self.client.post('api/v1/auth/signup', 
        data=json.dumps(dict(
            username="",
            password="hedwig",
            email="rita@gmail.com",
            admin=True
        )),
        content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'field cannot be blank', response.data)

    def test_cannot_add_user_with_invalid_name(self):
        """Tests to ensure username contains only letters"""
        response = self.client.post('api/v1/auth/signup', 
        data=json.dumps(dict(
            username="12345",
            password="hedwig",
            email="rita@gmail.com",
            admin=True
        )),
        content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Username can only contain letters', response.data)

    def test_cannot_add_user_without_email(self):
        """Tests that a user cannot be added without an email"""
        response = self.client.post('api/v1/auth/signup', 
        data=json.dumps(dict(
            username="Rita",
            password="hedwig",
            email="",
            admin=True
        )),
        content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'field cannot be blank', response.data)

    def test_cannot_add_user_with_invalid_email(self):
        """Tests that user email is of the correct format"""
        response = self.client.post('api/v1/auth/signup', 
        data=json.dumps(dict(
            username="Rita",
            password="hedwig",
            email="@123.com@gmail",
            admin=True
        )),
        content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Invalid email format', response.data)

    def test_cannot_add_user_with_invalid_password(self):
        """Tests that password input is of the proper length before being accepted"""
        response = self.client.post('api/v1/auth/signup', 
        data=json.dumps(dict(
            username="Rita",
            password="worlddomination",
            email="rita@gmail.com",
            admin=True
        )),
        content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Password should be between 6-9 characters', response.data)
        
    def test_cannot_add_user_without_password(self):
        """Tests that there is a password provided before signup"""
        response = self.client.post('api/v1/auth/signup', 
        data=json.dumps(dict(
            username="12345",
            password="",
            email="rita@gmail.com",
            admin=True
        )),
        content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'field cannot be blank', response.data)


    def test_cannot_add_user_with_missing_parameter(self):
        """Tests to ensure all parameters have been filled in"""
        response = self.client.post('api/v1/auth/signup', 
        data=json.dumps(dict(
            password="hedwig",
            email="rita@gmail.com",
            admin=True
        )),
        content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Missing key parameter: username, email, password', response.data)

    def test_cannot_add_same_user_twice(self):
        """Tests to ensure same user cannot be signed up more than once"""
        self.client.post('api/v1/auth/signup', 
        data=json.dumps(dict(
            username="Diana",
            password='hogwarts',
            email='diana@gmail.com',
            admin=False
        )),
        content_type='application/json')
        response = self.client.post('api/v1/auth/signup', 
        data=json.dumps(dict(
            username='Diana',
            password='hogwarts',
            email='diana@gmail.com',
            admin=False
        )),
        content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'User already exists!', response.data)
        #login tests

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
        self.assertIn(b'Data should be in JSON format', response.data)

    def test_can_login_user(self):
        """Test if a user can successfully be logged in"""
        self.client.post('api/v1/auth/signup', 
        data=json.dumps(dict(
            username="Rita",
            password="hedwig",
            email="rita@gmail.com", 
            admin=True
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
        self.assertIn(b'Successfully logged in', response.data)


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
        self.assertIn(b'User must sign up before logging in', response.data)

    def test_empty_password_login(self):
        """Tests to ensure that user does not login with empty password"""
        self.client.post('api/v1/auth/signup', 
        data=json.dumps(dict(
            username="Rita",
            password="hedwig",
            email="rita@gmail.com", 
            admin=True
        )),
        content_type='application/json')
        response = self.client.post('api/v1/auth/login', 
        data=json.dumps(dict(
            password="",
            username="Rita"
            )
        ),
        content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Please enter your password', response.data)

    def test_wrong_password_login(self):
        """Tests to ensure that password matches username"""
        self.client.post('api/v1/auth/signup', 
        data=json.dumps(dict(
            username="Rita",
            password="hedwig",
            email="rita@gmail.com", 
            admin=True
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
        self.assertIn(b'User must sign up before logging in', response.data)

    def test_empty_username_login(self):
        """Tests to ensure that user does not login with empty username"""
        self.client.post('api/v1/auth/signup', 
        data=json.dumps(dict(
            username="Rita",
            password="hedwig",
            email="rita@gmail.com", 
            admin=True
        )),
        content_type='application/json')
        response = self.client.post('api/v1/auth/login', 
        data=json.dumps(dict(
            password="hedwig",
            username=""
            )
        ),
        content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Please enter your username', response.data)

    def test_invalid_username_login(self):
        """Tests if usename matches password"""
        self.client.post('api/v1/auth/signup', 
        data=json.dumps(dict(
            username="Rita",
            password="hedwig",
            email="rita@gmail.com", 
            admin=True
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
        self.assertIn(b'User must sign up before logging in', response.data)

    def test_missing_parameter_user_login(self):
        """Tests to ensure both fields are filled in before login"""
        response = self.client.post('api/v1/auth/login', 
        data=json.dumps(dict(
            username="Rita"
            )
        ),
        content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Missing key parameter: username, password', response.data)
