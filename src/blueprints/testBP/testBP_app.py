from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

blueprint_test = Blueprint('simple_page', __name__, template_folder='templates',url_prefix='/testBP')

@blueprint_test.route('/test', defaults={'page': 'index'})
#@simple_page.route('/<page>')
def show(page):
	try:
		return "hello Blueprint ==> "+__name__
		#return render_template('pages/%s.html' % page)

	except TemplateNotFound:
		abort(404)
