import re

from flask import Blueprint, jsonify, make_response, request
from flask_jwt_extended import create_access_token, jwt_required

from api import app
from api.models.db import DatabaseConnection
from api.models.users import Users

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/signup', methods=['POST'])
def sign_up():
    try: 
        data = request.get_json()
        if not data:
            return jsonify({'message':'Data should be in JSON format'}), 400
        user_name = data['username']
        user_email = data['email']
        user_password = data['password']
        admin = data['admin']
        if not user_name or not user_email or not user_password:
            return jsonify({"message": "field cannot be blank"}), 400                           
        elif not re.search(r'^[a-zA-Z]+$', user_name) or not isinstance(user_name, str):
            return jsonify({'message': 'Username can only contain letters'}), 400                           
        elif not re.search(r'[^@#]+@[^@#]+\.[^@#]+', user_email):
            return jsonify({'message':'Invalid email format'}), 400           
        elif len(user_password) < 6 or len(user_password) > 9:
            return jsonify({'message':'Password should be between 6-9 characters'}), 400
        elif not isinstance(admin, bool):
            return jsonify({'message': 'Use False or True to specify admin role'})
        new_user = Users.check_if_user_is_new(user_name, user_email)
        if new_user == True:
            user=Users(username=user_name, email=user_email, password=user_password, admin=admin)
            user.add_user(user_name, user_email, user_password, admin)
            return jsonify({'message':'New user added'}), 201
        return jsonify({'message': 'User already exists!'}), 400
    except KeyError:
        return jsonify({'message':'Missing key parameter: username, email, password, admin'}), 400

@auth_bp.route('/login', methods=['POST'])
def login():
    try: 
        data = request.get_json()
        if not data:
            return jsonify({'message': 'Data should be in JSON format!'}), 400
        username = data['username']
        password = data['password']
        user_token = Users.check_user_credentials(username, password)
        if user_token is not None:
            return jsonify({'message':'Successfully logged in', 'token': user_token}), 200
        return jsonify({'message':'User must sign up before logging in'}), 400  
    except KeyError:
        return jsonify({'message': 'Missing key parameter: username, password, admin'}), 400
