"""Orders module"""
import psycopg2
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
    def update_status(cls, order_id, order_status):
        valid_status = ['Complete', 'Processing', 'Cancelled']
        query='''UPDATE orders SET order_status={} WHERE order_id = {}'''.format(valid_status, order_id)
