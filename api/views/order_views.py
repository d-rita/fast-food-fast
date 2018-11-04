from flasgger import swag_from
from flask import Blueprint, jsonify, make_response, request
from flask_jwt_extended import get_jwt_identity, jwt_required

from api import app
from api.models.orders import Orders
from api.models.users import Users

order_bp = Blueprint('order_bp', __name__)

@order_bp.route('/orders', methods=['GET'])
@swag_from("..docs/get_orders.yml")
@jwt_required
def get_orders():
    """Get all orders"""
    logged_in = get_jwt_identity()
    admin = Users.check_if_admin(logged_in['user_id'])
    if admin[0] == True:
        all_orders = Orders.get_all_orders()
        if len(all_orders) == 0:
            return jsonify({'message': 'There are no orders'}), 404
        return jsonify({'message': 'All orders are returned!', 'Orders': all_orders}), 200
    return jsonify({'message':'Only an admin can access all orders'}), 401

@order_bp.route('/orders/<int:order_id>', methods=['GET'])
@swag_from("..docs/get_an_order.yml")
@jwt_required
def get_an_order(order_id):
    logged_in_admin = get_jwt_identity()
    if logged_in_admin['admin'] == True:
        an_order = Orders.get_an_order(order_id)
        if an_order is None:
            return jsonify({'message':'Order does not exist'}), 404
        return jsonify({'message': 'One order has been returned','Order':an_order }), 200
    return jsonify({'message':'Only an admin can access all orders'}), 401
    

@order_bp.route('/orders/<int:order_id>', methods=['PUT'])
@swag_from("..docs/update_order.yml")
@jwt_required
def update_order_status(order_id):
    logged_in = get_jwt_identity()
    admin = Users.check_if_admin(logged_in['user_id'])
    if admin[0] == True:
        data = request.get_json()
        if not data:
            return jsonify({'message': 'Data should be in JSON format!'}), 400
        status = data['order_status']
        result = Orders.update_status(order_id, status)
        return jsonify({'message':'Order status updated','updated_order': result}), 200
    return jsonify({'message':'Only an admin can access all orders'}), 401
