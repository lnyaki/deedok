from flask import Flask
import jboost_controller as jbc 
from routes import routes

# ------ Blueprints imports ------- #
#from blueprints.testBP.testBP_app 	import blueprint_test 
from blueprints.gsearch.app 		import gsearch
from blueprints.vue.app 			import vue

app = Flask(__name__)


# ------ BLUEPRINTS -------- #
#app.register_blueprint(blueprint_test)
app.register_blueprint(gsearch)
app.register_blueprint(vue)

routes(app)


if __name__ == "__main__":
    app.run(debug=True)
