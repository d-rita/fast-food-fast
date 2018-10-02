import jwt
import re
from api import app
from flask import  request, make_response, jsonify
from api.models.users import Users, USERS

@app.route('/api/v1/auth/signup', methods=['GET'])
def sign_up():
    data = request.get_json
    user = {
        'username': data['username'],
        'email': data['email'],
        'password' : data['password']
    }
    username = user['username']
    email = user['email']
    password = user['password']
    if not username or not email or not password:
        return jsonify({"message": "field cannot be blank"}), 400                              
    elif not re.search(r'^[a-zA-Z]+$', username):
        return jsonify({'message': 'Username can only contain letters'}), 400                           
    elif not re.search(r'[^@]+@[^@]+\.[^@]+', email):
        return jsonify({'message':'Invalid email format'}), 400           
    elif len(password) < 6 or len(password) > 9:
        return jsonify({'message':'Password should be between 6-9 characters'}), 400
    USERS.append(user)
    return jsonify({'message': 'User successfully logged in'})

@app.route('/api/v1/auth/login', methods=['POST'])
def login():
    pass
