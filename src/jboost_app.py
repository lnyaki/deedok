from flask import Flask
import jboost_controller as jbc 
from routes import my_test, routes

# ------ Blueprints imports ------- #
from blueprints.testBP.testBP_app 	import blueprint_test 
from blueprints.gsearch.app 		import gsearch

app = Flask(__name__)


# ------ BLUEPRINTS -------- #
app.register_blueprint(blueprint_test)
app.register_blueprint(gsearch)

routes(app)


if __name__ == "__main__":
    app.run(debug=True)
