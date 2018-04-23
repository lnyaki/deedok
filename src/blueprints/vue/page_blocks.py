from flask import render_template

def vue_test(data):
	#return render_template('vue/vue_tests.html',context=data)
	return "Test dans vue!"

def vue_app1(data):
	return render_template('vue/app1.html', context=data)

def vue_form(data):
	return render_template('vue/test_form.html',context=data)
	