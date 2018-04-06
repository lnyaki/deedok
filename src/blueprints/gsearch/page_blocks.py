from flask import render_template

def categoriesButtonList(categories):
	return render_template('gsearch/categoriesButtonList.html',context={'categories':categories,'divClass':' '})

def movieList(movies):
	return render_template('gsearch/moviesList.html',context={'movies':movies,'divClass':'test'})

def testForm():
	return render_template('gsearch/gsearch_test_form.html',context={})

def button(value,buttonClass='',id='button'):
	return render_template('gsearch/button.html',context={'content':value,'buttonClass':buttonClass,'id':id})

def test_paragraph(data):
	return render_template('gsearch/test_paragraph.html',context=data)

def vue_test(data):
	return render_template('gsearch/vue_tests.html',context=data)