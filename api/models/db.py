"""Database module"""
import psycopg2
from api import app

conn = psycopg2.connect(dbname="d44f6hfmbs0tfq", user="ghzwbjivzerzbt", password="367fe74a9db0cf5d24a6c567c1712de7b7dfe3e1b099c0d426c544703fd2ae0c", host="ec2-50-17-225-140.compute-1.amazonaws.com")
cur = conn.cursor()

class DatabaseConnection:
    """This class sets up a database connection and creates tables """
    
    def __init__(self):
        """initialises database connections"""
        self.conn = conn
        self.cur = cur
        self.conn.autocommit = True

    def create_all_tables(self): 
        try: 
            self.cur.execute('''CREATE TABLE IF NOT EXISTS users(user_id SERIAL PRIMARY KEY,username VARCHAR(100),email VARCHAR(50),user_password VARCHAR(50),admin BOOLEAN NOT NULL)''')
            self.cur.execute('''CREATE TABLE IF NOT EXISTS menus(menu_id SERIAL PRIMARY KEY,food_name VARCHAR(50),food_price INTEGER)''')
            self.cur.execute('''CREATE TABLE IF NOT EXISTS orders(order_id SERIAL PRIMARY KEY,place VARCHAR(50),today TIMESTAMP NOT NULL,order_status VARCHAR(25),menu_id INTEGER NOT NULL REFERENCES menus (menu_id) ON UPDATE CASCADE ON DELETE CASCADE,user_id INTEGER NOT NULL REFERENCES users (user_id) ON UPDATE CASCADE ON DELETE CASCADE)''')
            self.conn.commit()
        except(psycopg2.DatabaseError):
            self.conn.rollback()

    def delete_all_tables(self):
        self.cur.execute('''DROP TABLE IF EXISTS orders CASCADE''')
        self.cur.execute('''DROP TABLE IF EXISTS users CASCADE''') 
        self.cur.execute('''DROP TABLE IF EXISTS menus CASCADE''')
        
   