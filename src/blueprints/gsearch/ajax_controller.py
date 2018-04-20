from blueprints.gsearch.graph_dao 	import Graph_Dao
from flask 							import jsonify
import json
from pprint 						import pprint

def getCategories(categories):
	#cats = categories

	graph 	= Graph_Dao()
	cats 	= graph.getCategories()

	pprint("GetCategories, ajax_controller")
	pprint(cats)

	return json.dumps(cats)

	#return json.dumps("Data received Yeah!")