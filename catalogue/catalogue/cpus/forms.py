from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
#from wtforms.fields.html5 import DateTimeLocalField
from wtforms.validators import DataRequired, Length
from catalogue.models import CPU


class CPUForm(FlaskForm):
	serial_number = StringField('Serial Number', render_kw={"placeholder": "Serial Number"}, validators=[DataRequired(), Length(min=2, max=10)])
	model_name = StringField('Model Name', render_kw={"placeholder": "Model Name"}, validators=[DataRequired(), Length(min=2, max=20)])
	series_name = StringField('Series Name', render_kw={"placeholder": "Series Name"}, validators=[DataRequired(), Length(min=2, max=20)])
	asset_color = StringField('Asset Color', render_kw={"placeholder": "Asset Color"}, validators=[DataRequired(), Length(min=2, max=50)])
	memory = StringField('Memory', render_kw={"placeholder": "Memory"}, validators=[DataRequired(), Length(min=2, max=20)])
	processor = StringField('Processor', render_kw={"placeholder": "Processor"}, validators=[DataRequired(), Length(min=2, max=50)])
	location = StringField('location', render_kw={"placeholder": "location"}, validators=[DataRequired(), Length(min=2, max=50)])
	department = StringField('Department', render_kw={"placeholder": "Department"})
	assigned_to = StringField('Assigned To', render_kw={"placeholder": "Assigned To"})
	status = StringField('Status', render_kw={"placeholder": "Status"}, validators=[DataRequired(), Length(min=2, max=50)])
	delivery_date = StringField('Delivery Date', render_kw={"placeholder": "dd/mm/yyyy"}, validators=[DataRequired()])
	assigned_date = StringField('Assigned Date', render_kw={"placeholder": "dd/mm/yyyy"})
	condition = TextAreaField('Condition', render_kw={"placeholder": "Condition"}, validators=[DataRequired()])
	submit = SubmitField('Save')