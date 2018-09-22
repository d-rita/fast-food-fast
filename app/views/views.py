from flask import Flask, jsonify, request, json, make_response
from app import app
from app.models.orders import orders
from flask import make_response


#GET ALL ORDERS
@app.route('/api/v1/orders', methods=['GET'])
def get_all_orders():
    return jsonify({'orders': orders})

#FETCH A PARTICULAR ORDER
@app.route('/api/v1/orders/<int:orderId>', methods=['GET'])
def get_an_order(orderId):
        food_order=[order for order in orders if order['orderId']==orderId]
        return jsonify({'order': food_order[0]})

#CREATE A NEW ORDER
@app.route('/api/v1/orders', methods=['POST'])
def add_order():
    order={
        'name': request.json['name'], 
        'price': request.json['price'],
        'location': request.json['location'],
        'payment':'cash on delivery',
        'date': request.json['date']
    }
    orders.append(order)
    return make_response(jsonify({'message': "Order added successfully"}), 201)
    
#Update status of order
@app.route('/orders/<int:orderId>', methods=['PUT'])
def update_order_status(orderId):
    pass