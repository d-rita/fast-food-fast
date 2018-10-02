import psycopg2

class DatabaseConnection:
    """class holding database queries"""
    def __init__(self):
        """initialises database connections"""
        self.conn = psycopg2.connect(database="fastfoodfast", user="postgres", password="diana", host="localhost", port="5432")
        self.cur = self.conn.cursor()
        self.autocommit = True

    def create_all_tables(self):
        """create the tables for database"""
        create_users_table = "CREATE TABLE IF NOT EXISTS users\
        (user_id SERIAL PRIMARY KEY, username TEXT, email VARCHAR(50), user_password VARCHAR(50), admin BOOLEAN NOT NULL DEFAULT 'False')"
        self.cur.execute(create_users_table)
        #print('Users table successfully created')

        create_menus_table = "CREATE TABLE IF NOT EXISTS menus\
        (menu_id SERIAL PRIMARY KEY, food_name VARCHAR(50), food_price INTEGER)"
        self.cur.execute(create_menus_table)
        #print('Menus table successfully created')

        create_orders_table = "CREATE TABLE IF NOT EXISTS orders\
        (order_id SERIAL PRIMARY KEY, place VARCHAR(50), order_status VARCHAR(25), menu_id INTEGER NOT NULL, \
        FOREIGN KEY (menu_id) REFERENCES menus (menu_id) ON UPDATE CASCADE ON DELETE CASCADE, \
        user_id INTEGER NOT NULL, \
        FOREIGN KEY (user_id) REFERENCES users (user_id) ON UPDATE CASCADE ON DELETE CASCADE, \
        today TIMESTAMP NOT NULL)"
        self.cur.execute(create_orders_table)
        #print('Orders table successfully created')

