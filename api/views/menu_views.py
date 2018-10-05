from flask import jsonify, make_response, request, Blueprint
from api.models.menu import Menu
from flask_jwt_extended import jwt_required, get_jwt_identity

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
    user = get_jwt_identity()
    data = request.get_json()
    if not data:
        return jsonify({'message': 'Data should be in json format!'}), 400
    food_name = data['name']
    food_price = data['price']
    food = Menu(f_name=food_name, f_price=food_price)
    food.add_food_item(food_name, food_price)
    return jsonify({'message': 'Order successfully added!'}), 201
    