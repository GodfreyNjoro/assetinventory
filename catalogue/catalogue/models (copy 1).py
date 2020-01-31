from catalogue  import db, login_manager
from flask_login import UserMixin
from datetime import datetime

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

issues = db.Table('issues', db.Column('issue_id', db.Integer, db.ForeignKey('issue.id'), primary_key=True), 
							db.Column('computer_id', db.String(10), db.ForeignKey('computer.serial_number'), primary_key=True)
)

class Computer(db.Model):
	serial_number = db.Column(db.String(10), primary_key=True)
	computer_color = db.Column(db.String(50), unique=True, nullable=False)
	memory = db.Column(db.String(50), nullable=False)
	processor = db.Column(db.String(50), nullable=False)
	delivery_date = db.Column(db.DateTime, nullable=False)
	company_id = db.Column(db.Integer, db.ForeignKey('company.id'))
	staff = db.relationship('Staff', backref='computer', lazy=True)
	issues = db.relationship('Issue', secondary=issues, lazy='subquery', backref=db.backref('computer', lazy=True))
	#user = db.relationship('User', backref='username', lazy=True)

	def __repr__(self):
		return f"Computer('{self.serial_number}', '{self.computer_color}', '{self.memory}', '{self.processor}', '{self.delivery_date}'"

class Staff(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	staff_name = db.Column(db.String(50), unique=True, nullable=False)
	ownership_date = db.Column(db.DateTime, nullable=True)
	comp_id = db.Column(db.Integer, db.ForeignKey('computer.serial_number'))

	def __repr__(self):
		return f"Staff('{self.staff_name}', '{self.ownership_date}'"

class Issue(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	description = db.Column(db.String(200), nullable=False)
	issue_date = db.Column(db.DateTime, nullable=False, default=datetime)
	#comp_id = db.Column(db.Integer, db.ForeignKey('computer.serial_number'))

	def __repr__(self):
		return f"Issue('{self.description}', '{self.issue_date}'"


class Company(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	company_name = db.Column(db.String(15), unique=True, nullable=False)
	computers = db.relationship('Computer', backref='company')

	def __repr__(self):
		return f"Company('{self.company_name}')"

