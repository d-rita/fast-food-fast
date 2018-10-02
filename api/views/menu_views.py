from flask import jsonify, make_response, request, Blueprint

from api import app

menu_bp = Blueprint('menu_bp', __name__)

@menu_bp.route('/menu', methods=['GET'])
def get_menu():
    return jsonify({'message': 'Here is the menu'})

@menu_bp.route('/menu', methods=['POST'])
def add_menu_option():
    return jsonify({'message': 'One food item added!'})