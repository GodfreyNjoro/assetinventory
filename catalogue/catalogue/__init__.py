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
from catalogue.laptops.routes import laptops
from catalogue.monitors.routes import monitors
from catalogue.cpus.routes import cpus 
from catalogue.ipphone.routes import ipphone
from catalogue.main.routes import main

app.register_blueprint(users)
app.register_blueprint(laptops)
app.register_blueprint(monitors)
app.register_blueprint(cpus)
app.register_blueprint(ipphone)
app.register_blueprint(main)