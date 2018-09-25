import datetime
import re

from flask import jsonify, make_response, request

from app import app
from app.models.orders import generate_orderId, orders

for_today=datetime.datetime.now().date()

#GET ALL ORDERS
@app.route('/api/v1/orders', methods=['GET'])
def get_all_orders():
    """
    This function maps to '/api/v1/orders' for GET method
    Retrieves all orders

    Returns:
    200 if orders list exists and JSON format of all orders
    404 if there is no orders list
    """
    if orders:
        return make_response(jsonify({'orders': orders}), 200)
    else:
        return make_response(jsonify({'message':'No orders'}), 404)

#FETCH A PARTICULAR ORDER
@app.route('/api/v1/orders/<int:orderId>', methods=['GET'])
def get_an_order(orderId):
    """
    This function maps to '/api/v1/orders/<int:orderId> for GET method'
    Retrieves an order matching the orderId in url

    Args:
    int orderId

    Returns:
    200 if orderId matches existing order
    404 if orderId finds no match
    """
    for order in orders:
        if order['orderId'] == orderId:
            return make_response(jsonify(order), 200)
    return make_response(jsonify({'message': 'Order not found'}), 404)

#CREATE A NEW ORDER
@app.route('/api/v1/orders', methods=['POST'])
def add_order():
    """
    This function maps to '/api/v1/orders/ for POST method'
    Create an order

    Returns:
    201 for successful creation of order
    400 for a bad request: empty fields and wrong data type
    """
    input_data=request.json
    order = {
        'orderId':generate_orderId(orders),
        'location':input_data['location'],
        'name':input_data['name'],
        'price':input_data['price'],
        'date':for_today,
        'status':'Pending'
    }
    name=order['name']
    location=order['location']
    price=order['price']
    if not name:
        return make_response(jsonify('Please enter name'), 400)
    elif not isinstance(name, str):
        return make_response(jsonify('Please enter letters only'), 400)
    elif not re.search(r'^[a-zA-Z]+$', name):
        return make_response(jsonify('Please enter letters only'), 400)
    if not price:
        return make_response(jsonify('Please enter price'), 400)
    elif not isinstance(price, int):
        return make_response(jsonify('Please enter digits only'), 400)
    if not location:
        return make_response(jsonify('Please enter location'), 400)
    elif not isinstance(location, str):
        return make_response(jsonify('Please enter letters only'), 400)
    elif not re.search(r'^[a-zA-Z]+$', location):
        return make_response(jsonify('Please enter letters only'), 400)
    else:
        orders.append(order)
        return make_response(jsonify({'added_order': order, 'message': "Order sent successfully"}), 201)

#Update status of order
@app.route('/api/v1/orders/<int:orderId>', methods=['PUT'])
def update_order_status(orderId):
    """
    This function maps to '/api/v1/orders/<int:orderId>' for PUT method
    It updates the order status of order matching the given orderId.

    Args:
    int orderId

    Returns:
    201 if update has been made
    404 if order does not exist
    """
    updated_order=[]
    for order in orders:
        if order['orderId']==orderId:
            order['status']='Complete'
            updated_order.append(order)
            return make_response(jsonify({'updated_order':updated_order,'message':'Order status updated'}), 201)
    return make_response(jsonify({'message':'Order does not exist'}), 404)
