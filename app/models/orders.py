orders = []

ID=0
def generate_orderId(orders):# pragma: no cover
    """Function to generate orderId"""
    global ID
    if len(orders)==0:
        ID = len(orders)+1
    else:
        ID = ID+1
    return ID

class Orders(object):
    """Orders module to define order attributes"""
    def __init__(self, orderId,location,name, price, date, status):
        """Initializes order attributes"""
        self.orderId=orderId
        self.location=location
        self.name=name
        self.price=price
        self.date=date
        self.status=status
