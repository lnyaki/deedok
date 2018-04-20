from flask import Flask, request
from . import controller 
import jboost_controller as jbc

def routes(app):
	@app.route('/',methods=['GET'])
	def shokw():
        	return controller.index()

	@app.route('/vue',methods=['GET'])
	def vue():
		return controller.vue()

	@app.route('/test',methods=['GET'])
	def test():
		return jbc.test()

	@app.route('/experiment',methods=['GET'])
	def experiment():
		return controller.experiment() 

	@app.route('/testgraph',methods=['GET'])
	def testGraph():
		return controller.testGraph() 

	@app.route('/ajax/categories',methods=['POST'])
	def ajaxCategories():
		return ajx.getCategories(request.json)
