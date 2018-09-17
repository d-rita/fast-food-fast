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

@app.route('/orders', methods=['GET'])
def get_all_orders():
    return jsonify({'orders': orders})


if __name__=='__main__':
    app.run(debug=True)