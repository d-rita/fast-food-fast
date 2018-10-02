from flask import make_response, jsonify, Blueprint, request

from api import app

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/orders', methods=['GET'])
def get_user_orders():
    return jsonify({'message': 'Orders from a particular user returned!'})

@user_bp.route('/orders', methods=['POST'])
def add_one_user_order():
    return jsonify({'message': 'Create one food order'})

