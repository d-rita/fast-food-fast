from flask import make_response, jsonify, Blueprint, request
import psycopg2
from api.models.db import DatabaseConnection

from api import app
from api.models.orders import Orders
from api.models.menu import Menu
import datetime

user_bp = Blueprint('user_bp', __name__)

def get_food_by_id(menu_id):
    try: 
        my_db = DatabaseConnection()
        my_db.cur.execute('''SELECT menu_id FROM menus WHERE menu_id = {}'''.format(menu_id))
        fds_id = my_db.cur.fetchone()
        fd={}
        fd['id']=fds_id[0]
        return fd['id']
    except:
        return jsonify({'message': 'Food does not exist'}), 400

@user_bp.route('/<int:user_id>/orders', methods=['GET'])####work on this
def get_user_orders(user_id):
    """Get a particular user's orders"""
    my_orders = Orders.get_user_orders(user_id)
    if len(my_orders)==0:
        return jsonify({'message': 'You have no order history!'}), 404
    return jsonify({'message':'This is your order history', 'Your orders':my_orders}), 200

@user_bp.route('/orders', methods=['POST'])#Validate user ids
def add_one_user_order():
    """Place an order by user"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'message': 'Data should be in JSON!'}), 400
        location = data['location']
        date = datetime.datetime.utcnow()
        order_status = 'New'
        menu_id = get_food_by_id(data['food_id'])
        user_id = data['user_id']
        my_order = Orders(location=location, date=date, status=order_status, menu_id=menu_id, user_id=user_id)
        my_order.add_an_order(location, date, order_status, menu_id, user_id)
        return jsonify({'message': 'Created one food order'})
    except:
        return jsonify({'message': 'Error'}), 500