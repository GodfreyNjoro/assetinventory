from flask import render_template, url_for, flash, redirect, request, Blueprint
from catalogue import app, db
from catalogue.ipphone.forms import PhoneForm
from catalogue.models import Phone
from flask_login import login_required

ipphone = Blueprint('ipphone', __name__)


@ipphone.route('/phone', methods=['GET', 'POST'])
@login_required
def phone():
	form = PhoneForm()
	if form.validate_on_submit():
		phone = Phone(serial_number=form.serial_number.data, model_name=form.model_name.data, asset_color=form.asset_color.data, location=form.location.data,
						 department=form.department.data, assigned_to=form.assigned_to.data, status=form.status.data, delivery_date=form.delivery_date.data, 
						 assigned_date=form.assigned_date.data, condition=form.condition.data)

		db.session.add(phone)
		db.session.commit()
		flash('Phone saved!', 'success')
		return redirect(url_for('main.main_page'))

	return render_template('ipphone.html', title=Phone, form=form)