from flask import Flask, request
from . import controller 

from blueprints.gsearch import ajax_controller as ajx
from blueprints.vue import controller as vue_controller
import jboost_controller as jbc

def routes(app):
	@app.route('/',methods=['GET'])
	def shokw():
        	return "hello"

	@app.route('/test', methods=['GET'])
	def test():
		return "Toto? Test"
