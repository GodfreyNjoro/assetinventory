from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from catalogue.config import Config


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

from catalogue.users.routes import users
from catalogue.assets.routes import assets
from catalogue.main.routes import main

app.register_blueprint(users)
app.register_blueprint(assets)
app.register_blueprint(main)