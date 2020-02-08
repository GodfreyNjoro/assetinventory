from flask import render_template, url_for, flash, redirect, request, Blueprint
from catalogue import app, db
from catalogue.main.forms import LaptopForm, MonitorForm
from catalogue.models import Laptop, Monitor
from flask_login import login_required

main = Blueprint('main', __name__)


#@main.route('/main-page')
#@login_required
#def main_page():
#	return render_template('main_page.html')

@main.route('/main-page', methods=['GET', 'POST'])
@login_required
def main_page():
	

	return render_template('main_page.html', title='Main Page')