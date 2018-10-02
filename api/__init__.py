from flask import Flask

app = Flask(__name__)

from api.views.order_views import order_bp
app.register_blueprint(order_bp, url_prefix='/api/v1')

from api.views.menu_views import menu_bp
app.register_blueprint(menu_bp, url_prefix='/api/v1')

from api.views.user_views import user_bp
app.register_blueprint(user_bp, url_prefix='/api/v1/users')

@app.route('/home')
def home():
    return 'This is the home page'