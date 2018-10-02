"""Database module"""
import psycopg2

class DatabaseConnection:
    """This class sets up a database connection and creates tables """
    
    def __init__(self):
        """initialises database connections"""
        self.conn = psycopg2.connect(dbname="fastfooddb", user="postgres", password="diana", host="localhost")
        #self.conn.rollback()
        self.cur = self.conn.cursor()
        self.conn.autocommit = True

    def create_all_tables(self): 
        try: 
            self.cur.execute('''CREATE TABLE IF NOT EXISTS users(user_id SERIAL PRIMARY KEY,username VARCHAR(100),email VARCHAR(50),user_password VARCHAR(50),admin BOOLEAN NOT NULL DEFAULT FALSE)''')
            self.cur.execute('''CREATE TABLE IF NOT EXISTS menus(menu_id SERIAL PRIMARY KEY,food_name VARCHAR(50),food_price INTEGER)''')
            self.cur.execute('''CREATE TABLE IF NOT EXISTS orders(order_id SERIAL PRIMARY KEY,place VARCHAR(50),today TIMESTAMP NOT NULL,order_status VARCHAR(25),menu_id INTEGER NOT NULL REFERENCES menus (menu_id) ON UPDATE CASCADE ON DELETE CASCADE,user_id INTEGER NOT NULL REFERENCES users (user_id) ON UPDATE CASCADE ON DELETE CASCADE)''')
            self.conn.commit()
        except(psycopg2.DatabaseError):
            self.conn.rollback()
    
    # def add_food_query(self, query):
    #     """Executes query to add food item"""
    #     return self.cur.execute(query)

    # def get_menu_query(self, query):
    #     """Executes query to retrieve menu"""
    #     return self.cur.execute(query)

    # def place_order_query(self, query):
    #     """Executes query to place order"""
    #     return self.cur.execute(query)

    # def get_all_query(self, query):
    #     """Executes query to get all orders"""
    #     return self.cur.execute(query)
        
    # def orders_history_query(self, query):
    #     """Executes query to get a user's order history"""
    #     return self.cur.execute(query)
        
    # def order_status_query(self, query):
    #     """Executes query to update order status"""
    #     return self.cur.execute(query)
    
    # def sign_up_query(self, query):
    #     """Executes query to sign up a new user"""
    #     return self.cur.execute(query)
        
    # def log_in_query(self, query):
    #     """Executes query to log in a user"""
    #     return self.cur.execute(query)
        
    # def get_order_query(self, query):
    #     """Executes query to get one specific order"""
    #     return self.cur.execute(query)
        