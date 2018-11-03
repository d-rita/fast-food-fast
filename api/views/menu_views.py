import re

from flasgger import swag_from
from flask import Blueprint, jsonify, make_response, request
from flask_jwt_extended import get_jwt_identity, jwt_required

from api import app
from api.models.db import DatabaseConnection
from api.models.menu import Menu

menu_bp = Blueprint('menu_bp', __name__)

@menu_bp.route('/menu', methods=['GET'])
@swag_from("..docs/get_menu.yml")
def get_menu():
    my_menu = Menu.get_menu()  
    if my_menu == None:
        return make_response(jsonify({'message': 'There is no menu'}), 404) 
    return make_response(jsonify({'message':'Menu successfully returned', 'Menu': my_menu}), 200)

@menu_bp.route('/menu', methods=['POST'])
@swag_from("../docs/add_food.yml")
@jwt_required
def add_menu_option():  
    logged_in_admin = get_jwt_identity()
    if logged_in_admin['admin'] == True:
        data = request.get_json()
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
        new_food = Menu.check_if_food_is_new(food_name, food_price)
        if new_food == True:
            food = Menu(f_name=food_name, f_price=food_price)
            food.add_food_item(food_name, food_price)
            return jsonify({'message': 'Food successfully added!'}), 201
        return jsonify({'message': 'Food already exists on the menu'}), 400
    return jsonify({'message':'Only admins allowed'}), 401
