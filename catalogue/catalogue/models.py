from catalogue  import db, login_manager
from flask_login import UserMixin
#from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))


class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(20), unique=True, nullable=False)
	password = db.Column(db.String(60), nullable=False)


	def __repr__(self):
		return f"User('{self.username}', '{self.email}')"




class Laptop(db.Model):
	serial_number = db.Column(db.String(10), primary_key=True)
	model_name = db.Column(db.String(20), nullable=False)
	series_name = db.Column(db.String(20), nullable=False)
	asset_color = db.Column(db.String(50), nullable=False)
	memory = db.Column(db.String(50), nullable=False)
	processor = db.Column(db.String(50), nullable=False)
	location = db.Column(db.String(50), nullable=False)
	department = db.Column(db.String(50))
	assigned_to = db.Column(db.String(50), unique=True, nullable=True)
	status = db.Column(db.String(10), nullable=False)
	delivery_date = db.Column(db.String(30), nullable=False)
	assigned_date = db.Column(db.String(30))
	condition = db.Column(db.Text, nullable=False)
	
	def __repr__(self):
		return f"Laptop('{self.serial_number}', '{self.model_name}', '{self.asset_color}', '{self.memory}', '{self.processor}', '{self.location}', '{self.department}', '{self.assigned_to}', '{self.status}', '{self.delivery_date}', '{self.assigned_date}', '{self.condition}')"


class Monitor(db.Model):
	serial_number = db.Column(db.String(10), primary_key=True)
	model_name = db.Column(db.String(20), nullable=False)
	asset_color = db.Column(db.String(50), nullable=False)
	screen_size = db.Column(db.String(10), nullable=False)
	location = db.Column(db.String(50), nullable=False)
	department = db.Column(db.String(50), nullable=True)
	assigned_to = db.Column(db.String(50), unique=True, nullable=True)
	status = db.Column(db.String(50), nullable=False)
	delivery_date = db.Column(db.String(30), nullable=False)
	assigned_date = db.Column(db.String(30), nullable=True)
	condition = db.Column(db.Text, nullable=False)
	
	def __repr__(self):
		return f"Monitor('{self.serial_number}', '{self.model_name}', '{self.asset_color}', '{self.screen_size}', '{self.location}', '{self.department}', '{self.assigned_to}', '{self.status}', '{self.delivery_date}', '{self.assigned_date}', '{self.condition}')"


class CPU(db.Model):
	serial_number = db.Column(db.String(10), primary_key=True)
	model_name = db.Column(db.String(20), nullable=False)
	series_name = db.Column(db.String(20), nullable=False)
	asset_color = db.Column(db.String(50), nullable=False)
	memory = db.Column(db.String(50), nullable=False)
	processor = db.Column(db.String(50), nullable=False)
	location = db.Column(db.String(50), nullable=False)
	department = db.Column(db.String(50), nullable=True)
	assigned_to = db.Column(db.String(50), unique=True, nullable=True)
	status = db.Column(db.String(50), nullable=False)
	delivery_date = db.Column(db.String(30), nullable=False)
	assigned_date = db.Column(db.String(30), nullable=True)
	condition = db.Column(db.Text, nullable=False)
	
	def __repr__(self):
		return f"CPU('{self.serial_number}', '{self.model_name}', '{self.series_name}', '{self.asset_color}', '{self.memory}', '{self.processor}', '{self.location}', '{self.department}', '{self.assigned_to}', '{self.status}', '{self.delivery_date}', '{self.assigned_date}', '{self.condition}')"


class Phone(db.Model):
	serial_number = db.Column(db.String(10), primary_key=True)
	model_name = db.Column(db.String(20), nullable=False)
	asset_color = db.Column(db.String(50), nullable=False)
	location = db.Column(db.String(50), nullable=False)
	department = db.Column(db.String(50), nullable=True)
	assigned_to = db.Column(db.String(50), unique=True, nullable=True)
	status = db.Column(db.String(50), nullable=False)
	delivery_date = db.Column(db.String(30), nullable=False)
	assigned_date = db.Column(db.String(30), nullable=True)
	condition = db.Column(db.Text, nullable=False)
	
	def __repr__(self):
		return f"Phone('{self.serial_number}', '{self.model_name}', '{self.asset_color}', {self.location}', '{self.department}', '{self.assigned_to}', '{self.status}', '{self.delivery_date}', '{self.assigned_date}', '{self.condition}')"