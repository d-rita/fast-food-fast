#from app.models import food
#from random import randint
orders = [] 

id = 0 
def generate_orderId(orders): # pragma: no cover
    global id
    if len(orders)==0:
        id = len(orders)+1
    else:
        id = id+1
    return id 

class Orders(object):
    def __init__(self, orderId,location,name, price, payment,quantity, date):
        self.orderId=orderId
        self.location=location
        self.name=name
        self.price=price
        self.payment=payment
        self.quantity=quantity
        self.date=date
        #self.accepted = False
        #self.rejected = False
        #self.completed = False
