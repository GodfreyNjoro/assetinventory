from flask import render_template, url_for, flash, redirect, request, Blueprint
from catalogue import  db
from .forms import AssetForm
from catalogue.models import Asset
from flask_login import login_required
from . import asset



@asset.route('/asset', methods=['GET'])
@login_required
def get_all_assets():
	"""
	Get all assets
	"""
	return render_template('inventory.assets_list.html', title='Asset')


@asset.route('/assets/<int:id>', methods=['GET'])
@login_required
def get_asset():
	"""
	Get a specific asset
	"""
	pass

@asset.route('/asset', methods=['POST'])
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

