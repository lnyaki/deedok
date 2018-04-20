from 	flask 	import render_template
from 	page 	import Page
from 	blueprints.gsearch.graph_dao 	import Graph_Dao
import 	blueprints.vue.page_blocks 		as blocks

def index():
	page 		= Page('Vue.js tests!')
	graph 		= Graph_Dao()

	page.addScript("dbQueries.js","gsearch")

	page.addBlockCenter(blocks.vue_test())
	
	return page.render()