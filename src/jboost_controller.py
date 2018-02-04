from flask import render_template, render_template_string

def homepage():
	return render_template("base.html", context={'content' : "<div>coucou</div>"})


def test():
	return "jboost controller test "	
