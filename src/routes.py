from flask import Flask, render_template
import jboost_controller as jbc

def my_test() :
	return "dans test"

def routes(app):
	@app.route("/testroute")
	def troute():
		return "hello, ça marche a fond yeah!"	

	@app.route("/")
	def hello():
    		context = { 'content': "contenu"+my_test(), 'scripts': "scripts",'title':"Hello test"}
    		return render_template("base.html", context=context)

	@app.route("/test")
	def test():
    		return render_template("test.html", context={'content' : "zarbi", 'side' : "toto"})

	@app.route("/controller")
	def controller():
    		return jbc.homepage()

