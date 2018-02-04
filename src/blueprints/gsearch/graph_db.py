from py2neo import Graph, authenticate

class Graph_DB():

	graph = None

	def __init__(self):
		pass		



	def getInstance(self):
		if (self.graph is None):
		
			PORT 		= 9000
			BOLT_PORT 	= 9001
			PASSWORD 	= "ad3eedda5d0118116ec22394419131b8"
			USERNAME 	= "neo4j"
			HOST 		= "localhost"
			DBPATH 		= "/db/data"
		
			authenticate("{host}:{port}".format(host=HOST,port=PORT), USERNAME, PASSWORD)
			self.graph = Graph(host=HOST,http_port=9000,bolt_port=9001,bolt=False)

			print("Graph --------")
			print(self.graph.data("match (n) where n.name STARTS WITH 'To' return n"))


		return self.graph

