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
    return make_response(jsonify({'message': 'Order not found'}), 404)

#CREATE A NEW ORDER
@app.route('/api/v1/orders', methods=['POST'])
def add_order():
    name= request.json['name']
    price= request.json['price']
    location= request.json['location']
    payment='cash on delivery'
    quantity=request.json['quantity']
    date= request.json['date']
    status=request.json['status']
    order = {
        'orderId':generate_orderId(orders),
        'location':location,
        'name':name,
        'price':price,
        'payment':payment,
        'quantity':quantity,
        'date':date, 
        'status':status
    }
    Orders('orderId', location= location, name = name, price =price, payment = payment, quantity=quantity, date = date, status=status )
    orders.append(order)
    return make_response(jsonify({'message': "Order sent successfully"}), 201)
    
#Update status of order
@app.route('/api/v1/orders/<int:orderId>', methods=['PUT'])
def update_order_status(orderId):
    updated_order=[]
    for order in orders:
        if order['orderId']==orderId:
            order['status']=request.json['status']
            updated_order.append(order)
            return make_response(jsonify({'message':'Order status updated'}), 200)
    return make_response(jsonify({'message':'Order does not exist'}), 404)