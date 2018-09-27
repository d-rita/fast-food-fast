"""This is the orders module"""
ORDERS = []

ID = 0

def generate_orderid(orders):# pragma: no cover
    """Function to generate orderId"""
    global ID
    if len(orders) == 0:
        ID = len(orders)+1
    else:
        ID = ID+1
    return ID

class Orders(object):
    """Orders module to define order attributes"""
    def __init__(self, orderid, location, name, price, date, status):
        """Initializes order attributes"""
        self.orderid = orderid
        self.location = location
        self.name = name
        self.price = price
        self.date = date
        self.status = status
