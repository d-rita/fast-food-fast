orders = [] 

Id = 0 
def generate_orderId(orders):# pragma: no cover
    """Function to generate orderId""" 
    global Id
    if len(orders)==0:
        Id = len(orders)+1
    else:
        Id = Id+1
    return Id 

class Orders(object):
    """Orders module to define an instance of an order"""
    def __init__(self, orderId,location,name, price, payment,quantity, date, status):
        self.orderId=orderId
        self.location=location
        self.name=name
        self.price=price
        self.payment=payment
        self.quantity=quantity
        self.date=date
        self.status=status
