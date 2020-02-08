from flask import render_template, url_for, flash, redirect, request, Blueprint
from catalogue import app, db
from catalogue.monitors.forms import MonitorForm
from catalogue.models import Monitor
from flask_login import login_required

monitors = Blueprint('monitors', __name__)


@monitors.route('/monitor', methods=['GET', 'POST'])
@login_required
def monitor():
	form = MonitorForm()
	if form.validate_on_submit():
		monitor = Monitor(serial_number=form.serial_number.data, model_name=form.model_name.data, asset_color=form.asset_color.data, screen_size=form.screen_size.data, location=form.location.data,
						 department=form.department.data, assigned_to=form.assigned_to.data, status=form.status.data, delivery_date=form.delivery_date.data, 
						 assigned_date=form.assigned_date.data, condition=form.condition.data)

		db.session.add(monitor)
		db.session.commit()
		flash('Monitor saved!', 'success')
		return redirect(url_for('main.main_page'))

	return render_template('monitor.html', title=Monitor, form=form)