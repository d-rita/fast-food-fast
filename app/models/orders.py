from app.models import food
orders = []
class Orders(object):
    def __init__(self, location,name, price, payment, date):
       # self.orderId=orderId
        self.location=location
        self.name=name
        self.price=price
        self.payment=payment
        #self.quantity=quantity
        self.date=date
        #self.food={}

    def add_order(self):
        pass

    def delete_order(self):
        pass

    def update_order(self):
        pass

