from py2neo import Graph, authenticate

PORT 		= 9000
BOLT_PORT 	= 9001
PASSWORD 	= "ad3eedda5d0118116ec22394419131b8"
USERNAME 	= "neo4j"
HOST 		= "localhost"
DBPATH 		= "/db/data"

# Stack overflow		
authenticate("localhost:9000", USERNAME, PASSWORD)
graph = Graph(host=HOST,http_port=9000,bolt_port=9001,bolt=False)


#authenticate("{host}:{port}".format(host=HOST,port=PORT),USERNAME,PASSWORD)
#graph = Graph("bolt://{host}:{port}/db/data".format(host=HOST,port=PORT),bolt_port=BOLT_PORT)
			#self.graph = Graph("bolt://{user}:{password}@{host}:{port}{dbpath}".format(user=USERNAME,
			#	password=PASSWORD, host=HOST,port=BOLT_PORT,dbpath=DBPATH,bolt=True))
print("Graph --------")
print(graph.data("match (n) where n.name STARTS WITH 'To' return n"))