from flask import Flask, jsonify, request, json, make_response
from app import app
from app.models.orders import orders, Orders, generate_orderId



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
    return make_response(jsonify({'message': 'Order not found'}), 400)

#CREATE A NEW ORDER
@app.route('/api/v1/orders', methods=['POST'])
def add_order():
    name= request.json['name']
    price= request.json['price']
    location= request.json['location']
    payment='cash on delivery'
    date= request.json['date']
    order = {
        'orderId':generate_orderId(orders),
        'location':location,
        'name':name,
        'price':price,
        'payment':payment,
        'date':date
    }
    Orders('orderId', location= location, name = name, price =price, payment = payment, date = date )
    orders.append(order)
    return make_response(jsonify({'message': "Order sent successfully"}), 201)
    
#Update status of order
@app.route('/orders/<int:orderId>', methods=['PUT'])
def update_order_status(orderId):
    pass