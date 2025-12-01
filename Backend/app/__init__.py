from flask import Flask
from flask_cors import CORS

from UserApi import register_user_blueprint
from adminApi import register_admin_blueprint
from routes.health import health_bp
from .config import configure_app
from .extensions import api, jwt, mail


def create_app():
    app = Flask(__name__)
    app.register_blueprint(health_bp)
    configure_app(app)
    CORS(app, resources={r"/*": {"origins": ["https://desi-delivery.vercel.app"]}}, supports_credentials=True)
    api.__init__app(app)
    jwt.__init__app(app)
    mail.__init__app(app)
    register_user_blueprint(app)
    register_admin_blueprint(app)
    return app
