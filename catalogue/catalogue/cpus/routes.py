from flask import render_template, url_for, flash, redirect, request, Blueprint
from catalogue import app, db
from catalogue.cpus.forms import CPUForm
from catalogue.models import CPU
from flask_login import login_required

cpus = Blueprint('cpus', __name__)


@cpus.route('/cpu', methods=['GET', 'POST'])
@login_required
def cpu():
	form = CPUForm()
	if form.validate_on_submit():
		cpu = CPU(serial_number=form.serial_number.data, model_name=form.model_name.data, series_name=form.series_name.data, asset_color=form.asset_color.data,
			            memory=form.memory.data, processor=form.processor.data, location=form.location.data, department=form.department.data, assigned_to=form.assigned_to.data,
			            status=form.status.data, delivery_date=form.delivery_date.data, assigned_date=form.assigned_date.data, condition=form.condition.data)

		db.session.add(cpu)
		db.session.commit()
		flash('CPU saved!', 'success')
		return redirect(url_for('main.main_page'))

	return render_template('cpu.html', title='CPU', form=form)