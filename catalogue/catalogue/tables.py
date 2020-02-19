from flask_table import Table, Col
from catalogue.models import Asset


class AssetResults(Table):
	serial_number = Col('Serial Number')
	asset_category = Col('Asset Category')
	model_name = Col('Model Name')
	series_name = Col('Series Name')
	asset_color = Col('Asset Color')
	memory = Col('Memory')
	processor = Col('Processor')
	location = Col('Location')
	status = Col('Status')
	delivery_date = Col('Delivery Date')
	condition = Col('Condition')