from flask import render_template, url_for, flash, redirect, request, Blueprint
from catalogue import  db
from .forms import AssetForm
from catalogue.models import Asset
from flask_login import login_required
from . import asset

#@main.route('/main-page')
#@login_required
#def main_page():
#	return render_template('main_page.html')

@asset.route('/asset', methods=['GET', 'POST'])
@login_required
def asset():
	form = AssetForm()
	if form.validate_on_submit():
		asset = Asset(serial_number=form.serial_number.data, asset_category=form.asset_category.data, model_name=form.model_name.data, series_name=form.series_name.data, asset_color=form.asset_color.data,
			            memory=form.memory.data, processor=form.processor.data, location=form.location.data, status=form.status.data, delivery_date=form.delivery_date.data)

		db.session.add(asset)
		db.session.commit()
		flash('Asset saved!', 'success')
		return redirect(url_for('main.main_page'))

	return render_template('asset.html', title='Asset', form=form)

