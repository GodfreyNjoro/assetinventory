from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from catalogue.models import User





class RegistrationForm(FlaskForm):
	username = StringField('Username', render_kw={"placeholder": "Username"}, validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField('Email', render_kw={"placeholder": "Email"}, validators=[DataRequired(), Email()])
	password= PasswordField('Password', render_kw={"placeholder": "Password"}, validators=[DataRequired()])
	confirm_password= PasswordField('Confirm Password', render_kw={"placeholder": "Confirm Password"}, validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign Up')

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('That username is taken. Please choose another username')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('That email is taken. Please choose a different one')


class LoginForm(FlaskForm):
	username = StringField('Username', render_kw={"placeholder": "Username"}, validators=[DataRequired(), Length(min=2, max=20)])
	password= PasswordField('Password', render_kw={"placeholder": "Password"}, validators=[DataRequired()])
	remember = BooleanField('Remember Me ')
	submit = SubmitField('Login')

