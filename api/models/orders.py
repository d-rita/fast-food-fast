"""Orders module"""
from flask import jsonify

from api.models.db import DatabaseConnection
from api.models.menu import Menu

class Orders:
    """Orders class defining methods and variables"""
    def __init__(self, location, date, status, menu_id, user_id):
        self.location = location 
        self.date = date
        self.status = status
        self.menu_id = menu_id
        self.user_id  = user_id

    def add_an_order(self, location, date, status, menu_id, user_id):
        query = '''INSERT INTO orders (place, today, order_status, menu_id, user_id)
        VALUES ('{}', '{}', '{}', '{}', '{}') RETURNING order_id'''.format(
            self.location,
            self.date,
            self.status,
            self.menu_id,
            self.user_id
        )
        my_db = DatabaseConnection()
        my_db.cur.execute(query)

    @classmethod
    def get_all_orders(cls):
        """Get a particular user's orders"""
        query = '''SELECT * FROM orders'''
        my_db = DatabaseConnection()
        my_db.cur.execute(query)
        orders = my_db.cur.fetchall()
        order_list = []
        for order in orders:
            ords={}
            ords['order_id'] = order[0]
            ords['location'] = order[1]
            ords['date'] = order[2]
            ords['status'] = order[3]
            ords['menu_id'] = order[4]
            ords['user_id'] = order[5]
            order_list.append(ords)
        return order_list

    @classmethod
    def get_user_orders(cls, user_id):
        """Get a particular user's orders"""
        query = '''SELECT * FROM orders WHERE user_id = {}'''.format(user_id)
        my_db = DatabaseConnection()
        my_db.cur.execute(query)
        orders = my_db.cur.fetchall()
        order_list = []
        for order in orders:
            ords={}
            ords['order_id'] = order[0]
            ords['location'] = order[1]
            ords['date'] = order[2]
            ords['status'] = order[3]
            ords['menu_id'] = order[4]
            ords['user_id'] = order[5]
            order_list.append(ords)
        return order_list
   
    @classmethod
    def update_status(cls, order_id, ord_status):
        valid_order = cls.get_an_order(order_id)
        if valid_order is None:
            return ('Cannot update non-existing order')
        else:
            valid_status = ['Complete', 'Processing', 'Cancelled']
            orders_list=[]
            if ord_status not in valid_status:
                return ('Invalid status')
            else:
                query='''UPDATE orders SET order_status = %s WHERE order_id = %s RETURNING order_id, place, today, order_status, menu_id, user_id'''
                my_db = DatabaseConnection()
                my_db.cur.execute(query, (ord_status, order_id))
                updated = my_db.cur.fetchone()
                u_ord = {}
                u_ord['order_id'] = updated[0]
                u_ord['location'] = updated[1]
                u_ord['date'] = updated[2]
                u_ord['status'] = updated[3]
                u_ord['menu_id'] = updated[4]
                u_ord['user_id'] = updated[5]
                orders_list.append(u_ord)
            return orders_list

    @classmethod
    def get_an_order(cls, order_id):
        query = '''SELECT * FROM orders WHERE order_id = {}'''.format(order_id)
        my_db = DatabaseConnection()
        my_db.cur.execute(query)
        order = my_db.cur.fetchone()
        if order:
            ords={}
            ords['order_id'] = order[0]
            ords['location'] = order[1]
            ords['date'] = order[2]
            ords['status'] = order[3]
            ords['menu_id'] = order[4]
            ords['user_id'] = order[5]
            return ords
        return None
