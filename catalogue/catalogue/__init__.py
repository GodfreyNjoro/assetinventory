from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

from config import config


bcrypt = Bcrypt()
db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bcrypt.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'users.login'
    login_manager.login_message_category = 'info'

    # from catalogue.users.routes import users
    # from catalogue.assets.routes import assets
    # from catalogue.main.routes import main

    from account import account as account_blueprint
    from asset import asset as asset_blueprint
    from dashboard import dashboard as dashboard_blueprint

    app.register_blueprint(account_blueprint)
    app.register_blueprint(asset_blueprint)
    app.register_blueprint(dashboard_blueprint)

    return app