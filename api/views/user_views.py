import datetime
import re

from flasgger import swag_from
from flask import Blueprint, jsonify, make_response, request
from flask_jwt_extended import get_jwt_identity, jwt_required

from api import app
from api.models.menu import Menu, get_food_by_id
from api.models.orders import Orders

user_bp = Blueprint('user_bp', __name__)

def validate_user_string(string):
    response = ''
    if not string:
        response = None
    elif not isinstance(string, str) or not re.search(r'^[a-zA-Z]+$', string):
        response = None
    else:
        response = string
    return response
    
@user_bp.route('/orders', methods=['GET'])
@swag_from("..docs/get_user_orders.yml")
@jwt_required
def get_user_orders():
    """Get a particular user's orders"""
    logged_in = get_jwt_identity()
    user_id = logged_in['user_id']
    if user_id:
        my_orders = Orders.get_user_orders(user_id)
        if len(my_orders)==0:
            return jsonify({'message': 'You have no order history!'}), 404
        return jsonify({'message':'Your order history has been returned', 'Orders':my_orders}), 200
    return jsonify({'message':'Log in to get your order history'}), 401

@user_bp.route('/orders', methods=['POST'])
@swag_from("..docs/add_order.yml")
@jwt_required
def add_one_user_order():
    """Place an order by user"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'message': 'Data should be in JSON!'}), 400 
        logged_in = get_jwt_identity()
        user_id = logged_in['user_id']
        user_location = data['location']
        date = datetime.datetime.utcnow()
        order_status = 'New'
        food_id = data['food_id']
        if not food_id:
            return jsonify({'message': 'Fill in the menu_id'}), 400
        elif not user_location:
            return jsonify({'message': 'Fill in the location'}), 400
        # elif not re.search(r'^[0-9]+$', food_id):
        #     return jsonify({'message': 'Food id must be an integer'}), 400
        menu_id = get_food_by_id(food_id)
        if menu_id is None:
            return jsonify({'message':'Food is not on the menu'}), 404
        location = validate_user_string(user_location)
        if location is None:
            return jsonify({'message':'Invalid location'}), 400
        my_order = Orders(location=location, date=date, status=order_status, menu_id=menu_id, user_id=user_id)
        my_order.add_an_order(location, date, order_status, menu_id, user_id)
        return jsonify({'message':'Created one food order'}), 201
    except KeyError:    
        return jsonify({'message': 'Missing parameter: fill in location and food_id'}), 400
