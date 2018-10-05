from flask import Flask
from flask_jwt_extended import JWTManager


app = Flask(__name__)
jwt = JWTManager(app)
app.config['SECRET_KEY'] = 'welcometomyworld'

from api.views.order_views import order_bp
app.register_blueprint(order_bp, url_prefix='/api/v1')

from api.views.menu_views import menu_bp
app.register_blueprint(menu_bp, url_prefix='/api/v1')

from api.views.user_views import user_bp
app.register_blueprint(user_bp, url_prefix='/api/v1/users')

from api.views.auth import auth_bp
app.register_blueprint(auth_bp, url_prefix='/api/v1/auth' )

@app.route('/home')
def home():
    return 'This is the home page'