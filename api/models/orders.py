"""Orders module"""
class Orders:
    """Orders class defining methods and variables"""
    def __init__(self, order_id, menu_id, user_id, location, status):
        self.order_id = order_id
        self.menu_id = menu_id
        self.location = location 
        self.status = status