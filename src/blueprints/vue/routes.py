from flask import Flask, request
from . import controller 

from blueprints.gsearch import ajax_controller as ajx
from blueprints.vue import controller as vue_controller

def routes(app):

	@app.route('/',methods=['GET'])
	def index():
		data = {}
		return vue_controller.index()

	@app.route('/test', methods=['GET'])
	def test():
		return "Toto? Test"
