from flask import render_template, url_for, flash, redirect, request, Blueprint
from catalogue import app, db
from catalogue.main.forms import LaptopForm, MonitorForm
from catalogue.models import Laptop
from flask_login import login_required

main = Blueprint('main', __name__)


#@main.route('/main-page')
#@login_required
#def main_page():
#	return render_template('main_page.html')

@main.route('/main-page', methods=['GET', 'POST'])
@login_required
def main_page():
	form = LaptopForm()
	if form.validate_on_submit():
		laptop = Laptop(serial_number=form.serial_number.data, model_name=form.model_name.data, series_name=form.series_name.data, asset_color=form.asset_color.data,
			            memory=form.memory.data, processor=form.processor.data, location=form.location.data, department=form.department.data, assigned_to=form.assigned_to.data,
			            status=form.status.data, delivery_date=form.delivery_date.data, assigned_date=form.assigned_date.data, condition=form.condition.data)

		db.session.add(laptop)
		db.session.commit()
		flash('Laptop saved!', 'success')
		return redirect(url_for('main.main_page1'))


	return render_template('child_main.html', title='Main Page', form=form)

#@main.route('/main-page1', methods=['GET', 'POST'])
#@login_required
#def main_page1():
#	form = MonitorForm()
#	if form.validate_on_submit():
#		monitor = Monitor(serial_number=form.serial_number.data, model_name=form.model_name.data, asset_color=form.asset_color.data, screen_size=form.screen_size.data, location=form.location.data,
#						 department=form.department.data, assigned_to=form.assigned_to.data, status=form.status.data, delivery_date=form.delivery_date.data, 
#						 assigned_date=form.assigned_date.data, condition=form.condition.data)

#		db.session.add(monitor)
#		db.session.commit()
#		flash('Monitor saved!', 'success')
#		return redirect(url_for('main.main_page1'))

#	return render_template('child_main.html', title='Main Page', form=form)