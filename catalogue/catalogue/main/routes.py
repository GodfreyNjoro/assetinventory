from flask import render_template, url_for, flash, redirect, request, Blueprint
from catalogue import app, db
#from catalogue.main.forms import LaptopForm, MonitorForm
from catalogue.models import Asset
from catalogue.tables import AssetResults
from flask_login import login_required

main = Blueprint('main', __name__)


#@main.route('/main-page')
#@login_required
#def main_page():
#	return render_template('main_page.html')

@main.route('/main-page', methods=['GET', 'POST'])
@login_required
def main_page():
	asset_num = Asset.query.paginate()
	assets = Asset.query.all()
	laptop = Asset.query.filter_by(asset_category='Laptop').paginate()
	monitor = Asset.query.filter_by(asset_category='Monitor').paginate()
	cpu = Asset.query.filter_by(asset_category='CPU').paginate()
	phone = Asset.query.filter_by(asset_category='Phone').paginate()
	table = AssetResults(assets)
	return render_template('main_page.html', title='Main Page', asset_num=asset_num, assets=assets, table=table, laptop=laptop, monitor=monitor, cpu=cpu, phone=phone)

