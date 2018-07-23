from flask import render_template, render_template_string

def homepage():
	return render_template("base.html", context={'content' : "<div>coucou</div>"})


def test(username, id, args):
	print("---- ARGS -----")
	print(args)
	print(args.get('id'))
	print(args.get('username'))
	return "jboost controller test "+ username + " " + str(id)	
