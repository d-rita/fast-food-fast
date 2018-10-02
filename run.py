from api import app
from api.views import order_views, user_views, menu_views
from api.db import DatabaseConnection


if __name__=='__main__':
    db_conn = DatabaseConnection()
    db_conn.create_all_tables()
    app.run(debug=True)
