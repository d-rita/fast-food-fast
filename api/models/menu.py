"""Menu module"""
class Menu:
    """Menu class to define Menu methods and variables"""
    menu={}
    def __init__(self, menu_id, food_name, food_price):
        self.menu_id = menu_id
        self.food_name = food_name
        self.food_price = food_price

    def add_food_item(self):
        if self.food_name not in self.menu:
            self.menu['food_name'] = self.food_name
            self.menu['food_price'] = self.food_price