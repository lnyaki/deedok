from flask import render_template
from page import Page
from py2neo import Path, Walkable
from blueprints.gsearch.graph_dao import Graph_Dao
import blueprints.gsearch.page_blocks as blocks

def index():
	page 		= Page('GSearch!')
	graph 		= Graph_Dao()

	categories = graph.getCategories()
	print(categories)
	page.addScript("dbQueries.js","gsearch")
	page.addScript("ajax.js")
	page.addScript("testAjax.js","gsearch")
	#page.addScript("angular.min.js")

	page.addBlockCenter(blocks.testForm())
	page.addBlockCenter(blocks.test_paragraph({'name':"Super Name!", 'id': page.next_id()}))


	page.addBlockLeft(blocks.categoriesButtonList(categories))
	page.addBlockLeft(blocks.test_paragraph({'name':"Super Name, le 2e!", 'id': page.next_id()}))

	page.addBlockRight(blocks.button("Delete graph","btn-danger","buttonID"))
	page.addBlockRight(blocks.button("Create GSearch graph","btn-primary","gsearchButton"))
	page.addBlockRight(blocks.test_paragraph({'name':"Super Name, le 3e!", 'id': page.next_id()}))
	

	return page.render()

def experiment():
	page 			= Page("Experiment page")
	graph 			= Graph_Dao()
	#categories 		= graph.getCategories()
	movies = graph.getMovies()
	categories = ["cat1","cat2","cat3","cat1","cat2","cat3",
					"cat1","cat2","cat3","cat1","cat2","cat3","cat1","cat2","cat3"]
	categoryList 	= blocks.categoriesButtonList(categories)
	movieList 		= blocks.movieList(movies)
	page.addBlockRight(categoryList)
	page.addBlockCenter(movieList)
	return page.render()

def testGraph():
	graph = Graph_Dao()
	result = graph.getCategoryPath()

	page = Page("Hello?")
	page.addBlockCenter("<div>Testing graph stuff</div>")
	page.addBlockCenter("<div><p> {data}</p><div>".format(data=result))
	walkable = Walkable(result)
	path = Path(walkable)

	return page.render()
