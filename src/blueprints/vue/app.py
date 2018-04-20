#app for vue
from flask 	import Blueprint 
from .routes	import routes

vue = Blueprint('vue', __name__, static_folder='static',template_folder='templates',url_prefix='/vue')

routes(vue)

