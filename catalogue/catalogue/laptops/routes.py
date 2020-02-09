from flask import render_template, url_for, flash, redirect, request, Blueprint
from catalogue import app, db
from catalogue.laptops.forms import LaptopForm
from catalogue.models import Laptop
from flask_login import login_required

laptops = Blueprint('laptops', __name__)


#@main.route('/main-page')
#@login_required
#def main_page():
#	return render_template('main_page.html')

@laptops.route('/laptop', methods=['GET', 'POST'])
@login_required
def laptop():
	form = LaptopForm()
	if form.validate_on_submit():
		laptop = Laptop(serial_number=form.serial_number.data, model_name=form.model_name.data, series_name=form.series_name.data, asset_color=form.asset_color.data,
			            memory=form.memory.data, processor=form.processor.data, location=form.location.data, department=form.department.data, assigned_to=form.assigned_to.data,
			            status=form.status.data, delivery_date=form.delivery_date.data, assigned_date=form.assigned_date.data, condition=form.condition.data)

		db.session.add(laptop)
		db.session.commit()
		flash('Laptop saved!', 'success')
		return redirect(url_for('main.main_page'))

	return render_template('laptop.html', title='Laptop', form=form)


class laptop_count():
	total = db.session.query(Laptop).count()