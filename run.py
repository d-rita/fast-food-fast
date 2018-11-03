from api import app
from api.views import order_views, user_views, menu_views
from api.models.db import DatabaseConnection
from config import DevelopmentConfig

app.config.from_object(DevelopmentConfig)

db_conn = DatabaseConnection()
db_conn.create_all_tables()

if __name__=='__main__':
    app.run()
