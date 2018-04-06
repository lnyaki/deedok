from blueprints.gsearch.graph_dao 	import Graph_Dao
from flask 							import jsonify
from pprint 						import pprint

def getCategories(categories):
	cats = categories
	pprint("GetCategories, ajax_controller")
	pprint(cats)

	return jsonify("Data received Yeah!")
