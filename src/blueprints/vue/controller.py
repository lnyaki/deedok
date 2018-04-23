from 	flask 	import render_template
from 	page 	import Page
from 	blueprints.gsearch.graph_dao 	import Graph_Dao
import 	blueprints.vue.page_blocks 		as blocks

def index():
	page 		= Page('Vue.js tests!')
	graph 		= Graph_Dao()
	data 		= {'page' : page}

	page.addScript("dbQueries.js","gsearch")

	page.addBlockCenter(blocks.vue_test({'page': page, 'id': page.next_id()}))
	page.addBlockCenter(blocks.vue_app1({'page': page, 'id': page.next_id()}))

	page.addBlockRight(blocks.vue_form({'page': page, 'id': page.next_id()}))
	
	return page.render()