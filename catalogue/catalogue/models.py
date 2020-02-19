from catalogue  import db, login_manager
from flask_login import UserMixin
#from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))


class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(100), unique=True, nullable=False)
	password = db.Column(db.String(60), nullable=False)


	def __repr__(self):
		return f"User('{self.username}', '{self.email}')"




conditions = db.Table('conditions', 
		db.Column('condition_id', db.Integer, db.ForeignKey('condition.id'), primary_key=True), 
		db.Column('asset_id', db.String(10), db.ForeignKey('asset.serial_number'), primary_key=True)
)


class Asset(db.Model):
	serial_number = db.Column(db.String(10), primary_key=True)
	asset_category = db.Column(db.String(20), nullable=False)
	model_name = db.Column(db.String(20), nullable=False)
	series_name = db.Column(db.String(20))
	asset_color = db.Column(db.String(50), nullable=False)
	memory = db.Column(db.String(50))
	processor = db.Column(db.String(50))
	location = db.Column(db.String(50), nullable=False)
	status = db.Column(db.String(10), nullable=False)
	delivery_date = db.Column(db.String(30), nullable=False)
	condition = db.relationship("Condition", secondary=conditions, lazy='subquery', backref=db.backref('assets', lazy=True))
	assigned_id = db.Column(db.Integer, db.ForeignKey('assigned_to.id'))
	
	def __repr__(self):
		return f"Asset('{self.serial_number}', '{self.catalogue}', '{self.model_name}', '{self.asset_color}', '{self.memory}', '{self.processor}', '{self.location}', '{self.department}', '{self.assigned_to}', '{self.status}', '{self.delivery_date}', '{self.assigned_date}', '{self.condition}')"



class Assigned_to(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(20), nullable=False)
	last_name = db.Column(db.String(20), nullable=False)
	department = db.Column(db.String(20), nullable=False)
	assigned_date = db.Column(db.String(30), nullable=False)
	asset = db.relationship('Asset', backref='asset', lazy=True)


	def __repr__(self):
		return f"Assigned_to('{self.first_name}', '{self.last_name}', '{self.department}', '{self.assigned_date}')"


class Condition(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	description = db.Column(db.String(200), nullable=False)
	condition_status = db.Column(db.String(100))
	reporting_date = db.Column(db.String(50))
	resolving_date = db.Column(db.String(50))


	def __repr__(self):
		return f"Condition('{self.description}', '{self.condition_status}', '{self.reporting_date}', '{self.resolving_date}')"

