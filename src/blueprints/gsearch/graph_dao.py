from py2neo import Graph, authenticate
from blueprints.gsearch.graph_db import Graph_DB

class Graph_Dao():
	_graph = None

	def __init__(self):
		self._graph = Graph_DB().getInstance()

	def query(self,query):
		return self._graph.data(query)

	def getCategoryPath(self):
		return self.query("match p = (:SYSTEM)-[*]-(m) where not((m)-->()) return p")

	def deleteAllNodes(self):
		self._graph.delete_all()

	def createIndex(self,labels,properties):
		return self.query("CREATE INDEX ON : {labels}({properties})".format(labels=labels,properties=properties))
		

	def getCategories(self):
		#return self.query("match (n) where n.name STARTS WITH 'To' return n")
		return self.query("MATCH (n:CATEGORY) return n.name as name LIMIT 10")
		#return self.query("match(s:SYSTEM{name: 'categories'})-[r:BASE_CATEGORY]->(n:CATEGORY) return s,r,n")

	def getMovies(self):
		return self.query("match(n:Movie) return n order by n.title limit 100")

	def test_movies(self):
		data = self.query("match(n:Person) return n.name")