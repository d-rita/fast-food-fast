from flask import Blueprint, jsonify, make_response, request

from api import app

order_bp = Blueprint('order_bp', __name__)

@order_bp.route('/orders', methods=['GET'])
def get_orders():
    return jsonify({'message': 'All orders are returned!'})

@order_bp.route('/orders/<int:order_id>', methods=['GET'])
def get_an_order(order_id):
    return jsonify({'message': 'One order returned!'})

@order_bp.route('/orders/<int:order_id>', methods=['PUT'])
def update_order_status(order_id):
    return jsonify({'message': 'Order status updated.'})
