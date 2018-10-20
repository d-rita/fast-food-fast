"""Menu module"""
from api.models.db import DatabaseConnection
from flask import jsonify

def get_food_by_id(menu_id):
    query = '''SELECT menu_id FROM menus WHERE menu_id = {}'''.format(menu_id)
    my_db = DatabaseConnection()
    my_db.cur.execute(query)
    fd_count = my_db.cur.rowcount
    fds_id = my_db.cur.fetchone()
    if fd_count > 0:
        fd={}
        fd['id']=fds_id[0]
        return fd['id']
    return None

class Menu:
    """Menu class to define Menu methods and variables"""
    def __init__(self, f_name, f_price):
        self.f_name = f_name
        self.f_price = f_price

    def add_food_item(self, f_name, f_price):
        query = '''INSERT INTO menus (food_name, food_price)
        VALUES ('{}', '{}') RETURNING menu_id'''.format(
            self.f_name,
            self.f_price
            )
        my_db = DatabaseConnection()
        my_db.cur.execute(query)

    @classmethod
    def get_menu(cls):
        query = '''SELECT * FROM menus'''
        my_db = DatabaseConnection()
        my_db.cur.execute(query)
        foods = my_db.cur.fetchall()
        foods_count = my_db.cur.rowcount
        if foods_count > 0:
            menu_list=[]
            for food in foods:
                fd = {}
                fd['menu_id'] = food[0]
                fd['food_name'] = food[1]
                fd['food_price'] = food[2]
                menu_list.append(fd)
            return menu_list
        return None

    @classmethod
    def check_if_food_is_new(cls, name, price):
        query = '''SELECT * FROM menus WHERE food_name = %s AND food_price = %s'''
        my_db = DatabaseConnection()
        my_db.cur.execute(query, (name, price))
        user_count = my_db.cur.rowcount
        if user_count > 0:
            return False
        return True     