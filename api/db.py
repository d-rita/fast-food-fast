import psycopg2

conn = psycopg2.connect(dbname="fastfooddb", user="postgres", password="diana", host="localhost")
print('Database successfully connected')
cur = conn.cursor()

class DatabaseConnection:
    """class holding database queries"""
    def __init__(self):
        """initialises database connections"""
        self.conn = conn
        self.cur = cur
        self.autocommit = True

    def create_all_tables(self):
        """create the tables for database"""
        commands = (
            '''CREATE TABLE IF NOT EXISTS users(
                user_id SERIAL PRIMARY KEY,
                username VARCHAR(100),
                email VARCHAR(50),
                user_password VARCHAR(50),
                admin BOOLEAN NOT NULL DEFAULT FALSE
                 )''',

            '''CREATE TABLE IF NOT EXISTS menus(
                menu_id SERIAL PRIMARY KEY,
                food_name VARCHAR(50),
                food_price INTEGER)''',

            '''CREATE TABLE IF NOT EXISTS orders(
                order_id SERIAL PRIMARY KEY,
                place VARCHAR(50),
                order_status VARCHAR(25),
                menu_id INTEGER NOT NULL, 
                FOREIGN KEY (menu_id) REFERENCES menus (menu_id) ON UPDATE CASCADE ON DELETE CASCADE,
                user_id INTEGER NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users (user_id) ON UPDATE CASCADE ON DELETE CASCADE,
                today TIMESTAMP NOT NULL)'''
        )

        for command in commands:
            self.cur.execute(command)

