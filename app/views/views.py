import datetime
import re

from flask import jsonify, make_response, request

from app import app
from app.models.orders import generate_orderId, orders

for_today=datetime.datetime.now().date()

#GET ALL ORDERS
@app.route('/api/v1/orders', methods=['GET'])
def get_all_orders():
    if orders:
        return make_response(jsonify({'orders': orders}), 200)
    else:
        return make_response(jsonify({'message':'No orders'}), 404)

#FETCH A PARTICULAR ORDER
@app.route('/api/v1/orders/<int:orderId>', methods=['GET'])
def get_an_order(orderId):
    for order in orders:
        if order['orderId'] == orderId:
            return make_response(jsonify(order), 200)
    return make_response(jsonify({'message': 'Order not found'}), 404)

#CREATE A NEW ORDER
@app.route('/api/v1/orders', methods=['POST'])
def add_order():
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
    updated_order=[]
    for order in orders:
        if order['orderId']==orderId:
            order['status']='Complete'
            updated_order.append(order)
            return make_response(jsonify({'updated_order':updated_order,'message':'Order status updated'}), 200)
    return make_response(jsonify({'message':'Order does not exist'}), 404)
