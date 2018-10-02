import psycopg2

class DatabaseConnection:
    
    def __init__(self):
        """initialises database connections"""
        self.conn = psycopg2.connect(dbname="fastfooddb", user="postgres", password="diana", host="localhost")
        #self.conn.rollback()
        self.cur = self.conn.cursor()
        #self.autocommit = True

    def create_all_tables(self): 
        try: 
            self.cur.execute('''CREATE TABLE IF NOT EXISTS users(user_id SERIAL PRIMARY KEY,username VARCHAR(100),email VARCHAR(50),user_password VARCHAR(50),admin BOOLEAN NOT NULL DEFAULT FALSE)''')
            self.cur.execute('''CREATE TABLE IF NOT EXISTS menus(menu_id SERIAL PRIMARY KEY,food_name VARCHAR(50),food_price INTEGER)''')
            self.cur.execute('''CREATE TABLE IF NOT EXISTS orders(order_id SERIAL PRIMARY KEY,place VARCHAR(50),today TIMESTAMP NOT NULL,order_status VARCHAR(25),menu_id INTEGER NOT NULL REFERENCES menus (menu_id) ON UPDATE CASCADE ON DELETE CASCADE,user_id INTEGER NOT NULL REFERENCES users (user_id) ON UPDATE CASCADE ON DELETE CASCADE)''')
            self.conn.commit()
        except(psycopg2.DatabaseError):
            self.conn.rollback()

