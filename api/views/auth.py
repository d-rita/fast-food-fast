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
        if not user_name or not user_email or not user_password:
            return jsonify({"message": "field cannot be blank"}), 400                              
        elif not re.search(r'^[a-zA-Z]+$', user_name):
            return jsonify({'message': 'Username can only contain letters'}), 400                           
        elif not re.search(r'[^@#]+@[^@#]+\.[^@#]+', user_email):
            return jsonify({'message':'Invalid email format'}), 400           
        elif len(user_password) < 6 or len(user_password) > 9:
            return jsonify({'message':'Password should be between 6-9 characters'}), 400
        user=Users(username=user_name, email=user_email, password=user_password)
        user.add_user(user_name, user_email, user_password)
        return jsonify({'message':'New user added'}), 201
    except KeyError:
        return jsonify({'message':'Missing key parameter'}), 400

@auth_bp.route('/login', methods=['POST'])
def login():
    try: 
        data = request.get_json()
        if not data:
            return jsonify({'message': 'Data should be in JSON format!'}), 400
        username = data['username']
        password = data['password']
        logged_in = Users.check_user_credentials(username, password)
        if logged_in is not None:
            return jsonify({'Successfully logged in': logged_in})
        return jsonify({'message':'Invalid password or username'}), 400  
    except KeyError:
        return jsonify({'message': 'Missing key parameter'}), 400
