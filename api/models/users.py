"""Users module"""
import re

from flask import jsonify
from flask_jwt_extended import create_access_token

from api import app
from api.models.db import DatabaseConnection


class Users:
    """Users class defining users methods and variables"""
    def __init__(self, username, email, password, admin):
        self.username = username
        self.email = email
        self.password = password
        self.admin = admin

    def add_user(self, username, email, password, admin):
        query = '''INSERT INTO users (username, email, user_password, admin)
        VALUES ('{}', '{}', '{}', '{}') RETURNING user_id'''.format(
            self.username,
            self.email,
            self.password,
            self.admin
        )
        my_db = DatabaseConnection()
        my_db.cur.execute(query)

    @classmethod
    def check_user_credentials(cls, username, password):
        query = '''SELECT * FROM users WHERE username = %s AND user_password = %s'''
        my_db = DatabaseConnection()
        my_db.cur.execute(query, (username, password))
        user_count = my_db.cur.rowcount
        existing_user = my_db.cur.fetchone()
        if user_count > 0:
            user = dict(user_id=existing_user[0], username=existing_user[1], email=existing_user[2], password=existing_user[3], admin=existing_user[4])
            token = create_access_token(identity=user)
            return token
        return None

    @classmethod
    def check_if_admin(cls, userid):
        query = '''SELECT admin FROM users WHERE user_id = {}'''.format(userid)
        my_db = DatabaseConnection()
        my_db.cur.execute(query)
        result = my_db.cur.fetchone()
        return result

    @classmethod
    def check_if_user_is_new(cls, username, email):
        query = '''SELECT * FROM users WHERE username = %s AND email = %s'''
        my_db = DatabaseConnection()
        my_db.cur.execute(query, (username, email))
        user_count = my_db.cur.rowcount
        if user_count > 0:
            return False
        return True

    @classmethod
    def check_logged_in_as(cls, username, password):
        query = '''SELECT admin FROM users WHERE username = %s AND user_password = %s'''
        my_db = DatabaseConnection()
        my_db.cur.execute(query, (username, password))
        result = my_db.cur.fetchone()
        return result
