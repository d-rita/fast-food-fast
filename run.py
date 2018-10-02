from api import app
from api.views import order_views, user_views, menu_views
from api.database_conn import DatabaseConnection

db_conn = DatabaseConnection()
db_conn.create_all_tables()

if __name__=='__main__':
    app.run(debug=True)
