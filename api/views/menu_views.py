from flask import jsonify, make_response, request, Blueprint
from api.models.menu import Menu
from flask_jwt_extended import jwt_required, get_jwt_identity
import re

from api import app
from api.models.db import DatabaseConnection

menu_bp = Blueprint('menu_bp', __name__)

@menu_bp.route('/menu', methods=['GET'])
@jwt_required
def get_menu():
    user = get_jwt_identity()
    my_menu = Menu.get_menu()   
    return make_response(jsonify({'message':'Menu successfully returned', 'Menu': my_menu}), 200)

@menu_bp.route('/menu', methods=['POST'])
@jwt_required
def add_menu_option():  
    logged_in_admin = get_jwt_identity()
    if logged_in_admin['admin'] == True:
        try:
            data = request.get_json()
            if not data:
                return jsonify({'message': 'Data should be in json format!'}), 400
            food_name = data['name']
            food_price = data['price']
            if not food_name:
                return jsonify({'message':'Fill in food name'}), 400
            elif not food_price:
                return jsonify({'message':'Fill in food price'}), 400
            elif not isinstance(food_name, str) or not re.search(r'^[a-zA-Z]+$', food_name):
                return jsonify({'message': 'Please enter letters only'}), 400
            elif not isinstance(food_price, int):
                return jsonify({'message': 'Please enter numbers only'}), 400
            food = Menu(f_name=food_name, f_price=food_price)
            food.add_food_item(food_name, food_price)
            return jsonify({'message': 'Food successfully added!'}), 201
        except KeyError:
            return jsonify({'message':'Fill in all parameters: name and price'}), 400
    return jsonify({'message':'Only admins allowed'}), 401
    