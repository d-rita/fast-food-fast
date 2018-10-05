from flask import Blueprint, jsonify, make_response, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from api.models.orders import Orders 
from api import app

order_bp = Blueprint('order_bp', __name__)

@order_bp.route('/orders', methods=['GET'])
@jwt_required
def get_orders():
    """Get all orders"""
    logged_in_admin = get_jwt_identity()
    if logged_in_admin['admin'] == True:
        all_orders = Orders.get_all_orders()
        if len(all_orders) == 0:
            return jsonify({'message': 'There are no orders'}), 404
        return jsonify({'message': 'All orders are returned!', 'Orders': all_orders}), 200
    return jsonify({'message':'Only an admin can access all orders'}), 401

@order_bp.route('/orders/<int:order_id>', methods=['GET'])
@jwt_required
def get_an_order(order_id):
    logged_in_admin = get_jwt_identity()
    if logged_in_admin['admin'] == True:
        an_order = Orders.get_an_order(order_id)
        if an_order is None:
            return jsonify({'message':'Order does not exist'}), 200
        return jsonify({'Order':an_order }), 200
    return jsonify({'message':'Only an admin can access all orders'}), 401
    

@order_bp.route('/orders/<int:order_id>', methods=['PUT'])
@jwt_required
def update_order_status(order_id):
    logged_in_admin = get_jwt_identity()
    if logged_in_admin['admin'] == True:
        try:
            data = request.get_json()
            if not data:
                return jsonify({'message': 'Data should be in JSON format!'}), 400
            status = data['order_status']
            result = Orders.update_status(order_id, status)
            return jsonify({'updated_order': result})
        except KeyError:
            return jsonify({'message': 'Fill in missing parameter: order_status'})
    return jsonify({'message':'Only an admin can access all orders'}), 401
