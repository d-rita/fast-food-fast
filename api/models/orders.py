"""Orders module"""
import psycopg2
from api.models.db import DatabaseConnection
class Orders:
    """Orders class defining methods and variables"""
    def __init__(self, order_id, location, date, status, menu_id, user_id):
        self.order_id = order_id
        self.location = location 
        self.date = date
        self.status = status
        self.menu_id = menu_id
        self.user_id  = user_id

    def add_an_order(self):
        query = '''INSERT INTO orders (order_id, place, today, order_status, menu_id, user_id)
        VALUES ('{}', '{}', '{}', '{}', '{}', '{}')'''.format(
            self.order_id,
            self.location,
            self.date,
            self.status,
            self.menu_id,
            self.user_id
        )
        my_db = DatabaseConnection()
        my_db.cur.execute(query)

