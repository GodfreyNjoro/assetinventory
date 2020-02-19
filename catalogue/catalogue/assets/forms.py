from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
#from wtforms.fields.html5 import DateTimeLocalField
from wtforms.validators import DataRequired, Length
from catalogue.models import Asset




class AssetForm(FlaskForm):
	serial_number = StringField('Serial Number', render_kw={"placeholder": "Serial Number"}, validators=[DataRequired(), Length(min=2, max=10)])
	asset_category = StringField('Asset Category', render_kw={"placeholder": "Asset Category"}, validators=[DataRequired()])
	model_name = StringField('Model Name', render_kw={"placeholder": "Model Name"}, validators=[DataRequired(), Length(min=2, max=20)])
	series_name = StringField('Series Name', render_kw={"placeholder": "Series Name"})
	asset_color = StringField('Asset Color', render_kw={"placeholder": "Asset Color"}, validators=[DataRequired(), Length(min=2, max=50)])
	memory = StringField('Memory', render_kw={"placeholder": "Memory"})
	processor = StringField('Processor', render_kw={"placeholder": "Processor"})
	location = StringField('location', render_kw={"placeholder": "location"}, validators=[DataRequired(), Length(min=2, max=50)])
	status = StringField('Status', render_kw={"placeholder": "Status"}, validators=[DataRequired(), Length(min=2, max=50)])
	delivery_date = StringField('Delivery Date', render_kw={"placeholder": "dd/mm/yyyy"}, validators=[DataRequired()])
	submit = SubmitField('Save')