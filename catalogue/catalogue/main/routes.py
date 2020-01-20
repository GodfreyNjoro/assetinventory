from flask import render_template, Blueprint
from flask_login import login_required

main = Blueprint('main', __name__)


@main.route('/main-page')
@login_required
def main_page():
	return render_template('main_page.html')