"""Orders module"""
from api.db import DatabaseConnection
class Orders:
    """Orders class defining methods and variables"""
    def __init__(self, order_id, menu_id, user_id, location, status):
        self.order_id = order_id
        self.menu_id = menu_id
        self.location = location 
        self.status = status

    # def get_all_orders(self):
    #     get_all = "SELECT * orders WHERE user_id =={}"

       

    
    

    # def update_order_status(self):
    # pass
