from 	flask 	import render_template
from 	page 	import Page
from 	blueprints.gsearch.graph_dao 	import Graph_Dao
import 	blueprints.vue.page_blocks 		as blocks

def index():
	page 		= Page('Vue.js tests!')
	graph 		= Graph_Dao()
	data 		= {}

	page.addScript("dbQueries.js","gsearch")

	page.addBlockCenter(blocks.vue_test(data))
	
	return page.render()