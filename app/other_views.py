from flask import Flask, jsonify, request, json, abort, make_response

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

foods=[
    {
        'foodId':'F1',
        'name':'Cheese Burger',
        'price':12000
    }, 
    {
        'foodId':'F2',
        'name':'Chicken Pizza', 
        'price':12000
    }
]

users=[
    {
        'userId':'A1',
        'name': 'Mary Nakato',
        'email':'mary256@gmail.com', 
        'password': 'qwertya5d',
    },
    {
        'userId':'A2',
        'name': 'Patrick Nkurunziza',
        'email':'zizapat@hotmail.com', 
        'password': 'pa55w0rD', 
    }
]

@app.errorhandler(404)
def resource_not_found(error):
    return make_response(jsonify({'error': 'Oops! Cannot Be Found'}), 404)

@app.route('/orders', methods=['GET'])
def get_all_orders():
    return jsonify({'orders': orders})

@app.route('/orders/<int:orderId>', methods=['GET'])
def get_order(orderId):
        food_order=[order for order in orders if order['orderId']==orderId]
        return jsonify({'order': food_order[0]})

@app.route('/foods', methods=['GET'])
def get_all_foods():
    return jsonify({'foods': foods})

@app.route('/foods/<string:foodId>', methods=['GET'])
def get_food(foodId):
    food=[food for food in foods if food['foodId']==foodId]
    return jsonify({'food': food[0]})

@app.route('/users', methods=['GET'])
def get_all_users():
    return jsonify({'users':users})

@app.route('/users/<string:userId>', methods=['GET'])
def get_user(userId):
    user=[user for user in users if user['userId']==userId]
    return jsonify({'user': user[0]})


@app.route('/orders', methods=['POST'])
def add_order():
    order={}
   # order['name']=request.json['name']
   # order['price']=request.json]['price']
   # order['location']=request.json['location']
    order['payment']='Cash on Delivery'
   # order['date']=request.json['date']
   # order={
        #'orderId':orders[-1]['orderId']+1,
     #   'name': request.json['name'], 
     #   'price': request.json['price'],
     #   'location': request.json['location'],
      #  'payment':'cash on delivery',
      #  'date': request.json['date']
    #}
    orders.append(order)
    return jsonify({'orders': orders})



    



if __name__=='__main__':
    app.run(debug=True)