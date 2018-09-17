from flask import Flask, jsonify, request, json, make_response

app = Flask(__name__)

orders = [
    {
    'orderId':1,
    'name':'Veggie Burger',
    'price': 12000,
    'location':'Bunga',
    'payment':'cash on delivery',
    'date':'12/05/2016'
    }, 
    {
    'orderId':2,
    'name':'Ham Burger',
    'price': 12000,
    'location':'Kibuye',
     'payment':'card',
     'date':'12/07/2018'
     }
]

#GET ALL ORDERS
@app.route('/orders', methods=['GET'])
def get_all_orders():
    return jsonify({'orders': orders})

#FETCH A PARTICULAR ORDER
@app.route('/orders/<int:orderId>', methods=['GET'])
def get_an_order(orderId):
        food_order=[order for order in orders if order['orderId']==orderId]
        return jsonify({'order': food_order[0]})

#CREATE A NEW ORDER
@app.route('/orders', methods=['POST'])
def add_order():
    order={
        'name': request.json['name'], 
        'price': request.json['price'],
        'location': request.json['location'],
        'payment':'cash on delivery',
        'date': request.json['date']
    }
    orders.append(order)
    return jsonify({'orders': orders})
    
#Update status of order
@app.route('/orders/<int:orderId>', methods=['PUT'])
def update_order_status(orderId):
    food_order=[order for order in orders if order['orderId']==orderId]
    food_order[0]['name']=request.json['name']
    food_order[0]['price']=request.json['price']
    
    return jsonify({'order': food_order[0]})



if __name__=='__main__':
    app.run(debug=True)