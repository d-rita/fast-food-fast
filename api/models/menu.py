"""Menu module"""
from api.models.db import DatabaseConnection


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
        try: 
            query = '''SELECT * FROM menus'''
            my_db = DatabaseConnection()
            my_db.cur.execute(query)
            foods = my_db.cur.fetchall()
            my_db.conn.commit()
            #print('##########',foods)
            menu_list=[]
            for food in foods:
                fd = {}
                fd['menu_id'] = food[0]
                fd['food_name'] = food[1]
                fd['food_price'] = food[2]
                menu_list.append(fd)
                #print('================', menu_list)
            return menu_list
        except KeyError as e:
            print(e)




    @staticmethod
    def my_menu(food):
        return {
            "food_name":food[0],
            "food_price":food[1]
        }


        