from flask import jsonify, make_response, request, Blueprint
from api.models.menu import Menu

from api import app
from api.models.db import DatabaseConnection

menu_bp = Blueprint('menu_bp', __name__)

@menu_bp.route('/menu', methods=['GET'])
def get_menu():
    my_menu = Menu.get_menu()
    #print('#############',my_menu)
    return jsonify({'message':'Menu successfully returned', 'Menu': my_menu}), 200

@menu_bp.route('/menu', methods=['POST'])
def add_menu_option():  
    data = request.get_json()
    if not data:
        return jsonify({'message': 'Data should be in json format!'}), 400
    food_name = data['name']
    food_price = data['price']
    food = Menu(f_name=food_name, f_price=food_price)
    food.add_food_item(food_name, food_price)
    return jsonify({'message': 'Order successfully added!'}), 200
    