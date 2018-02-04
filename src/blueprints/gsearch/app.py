#app for gsearch
from flask 	import Blueprint 
from .routes 	import routes

gsearch = Blueprint('gsearch', __name__, static_folder='static',template_folder='templates',url_prefix='/gsearch')

routes(gsearch)

