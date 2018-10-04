from flask import Blueprint, jsonify, make_response, request
from api.models.orders import Orders 
from api import app

order_bp = Blueprint('order_bp', __name__)

@order_bp.route('/orders', methods=['GET'])
def get_orders():
    """Get all orders"""
    all_orders = Orders.get_all_orders()
    if len(all_orders) == 0:
        return jsonify({'message': 'There are no orders'}), 404
    return jsonify({'message': 'All orders are returned!', 'Orders': all_orders}), 200

@order_bp.route('/orders/<int:order_id>', methods=['GET'])
def get_an_order(order_id):
    an_order = Orders.get_an_order(order_id)
    if an_order is None:
        return jsonify({'message':'Order does not exist'}), 200
    return jsonify({'Order':an_order }), 200

@order_bp.route('/orders/<int:order_id>', methods=['PUT'])
def update_order_status(order_id):
    data = request.get_json()
    if not data:
        return jsonify({'message': 'Data should be in JSON format!'}), 400
    status = data['order_status']
    result = Orders.update_status(order_id, status)
    return jsonify({'updated_order': result})
