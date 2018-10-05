import datetime

from flask import Blueprint, jsonify, make_response, request
from flask_jwt_extended import get_jwt_identity, jwt_required

from api import app
from api.models.menu import Menu, get_food_by_id
from api.models.orders import Orders

user_bp = Blueprint('user_bp', __name__)


@user_bp.route('/orders', methods=['GET'])
@jwt_required
def get_user_orders():
    """Get a particular user's orders"""
    logged_in = get_jwt_identity()
    user_id = logged_in['user_id']
    if user_id:
        my_orders = Orders.get_user_orders(user_id)
        if len(my_orders)==0:
            return jsonify({'message': 'You have no order history!'}), 404
        return jsonify({'message':'This is your order history', 'Your orders':my_orders}), 200
    return jsonify({'message':'Log in to get your orders'}), 401

@user_bp.route('/orders', methods=['POST'])
@jwt_required
def add_one_user_order():
    """Place an order by user"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'message': 'Data should be in JSON!'}), 400
        logged_in = get_jwt_identity()
        user_id = data['user_id']
        location = data['location']
        date = datetime.datetime.utcnow()
        order_status = 'New'
        menu_id = get_food_by_id(data['food_id'])
        if user_id == logged_in['user_id']:
            if menu_id is None:
                return jsonify({'message':'Food is not on the menu'}), 404
            my_order = Orders(location=location, date=date, status=order_status, menu_id=menu_id, user_id=user_id)
            my_order.add_an_order(location, date, order_status, menu_id, user_id)
            return jsonify({'message':'Created one food order'})
        return jsonify({'message':'User must first log in!'}), 401
    except KeyError:
        return jsonify({'message': 'Missing parameter: fill in user_id, location and menu_id'})
