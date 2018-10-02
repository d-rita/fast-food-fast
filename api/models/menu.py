"""Menu module"""
from api.models.db import DatabaseConnection


class Menu:
    """Menu class to define Menu methods and variables"""
    def __init__(self, f_name, f_price):
        self.f_name = f_name
        self.f_price = f_price

    def add_food_item(self, f_name, f_price):
        query = '''INSERT INTO menus (food_name, food_price)
        VALUES ('{}', '{}')'''.format(
            self.f_name,
            self.f_price
            )
        my_db = DatabaseConnection()
        my_db.cur.execute(query)

    @classmethod
    def get_menu(cls):
        menu_list=[]
        query = '''SELECT * FROM menus'''
        my_db = DatabaseConnection()
        my_db.cur.execute(query)
        foods = my_db.cur.fetchall()
        if foods:
            for food in foods:
                menu_list.append(Menu.my_menu(food))
                return menu_list



    @staticmethod
    def my_menu(food):
        return {
            "food_name":food[0],
            "food_price":food[1]
        }


        