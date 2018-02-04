import pandas as pd
from py2neo import Graph, authenticate, Node
import sys

def delete_all_nodes():
	pass

def load_categories(filename):
	df = pd.read_csv(filename)
	graph = get_graph_connection()

	print(df)

	node_type = "CATEGORY"
	node_list = {}

	print("-------------------")
	print("MERGE (n:{type} {{name : '@ROOT'}})".format(type=node_type))
	print("-------------------")
	#create root node
	graph.run("MERGE (n:{type} {{name : '@ROOT'}})".format(type=node_type))

	transaction = graph.begin()
	#create unlinked category nodes
	for index, row in df.iterrows():
		name 			= row[0].strip()
		parentCategory 	= row[1].strip()

		query = "MERGE (n:{type} {{name : '{name}'}})".format(type=node_type,name=name)

		

		transaction.run(query)

	transaction.commit()

	transaction = graph.begin()

	for index, row in df.iterrows():
		name 			= row[0].strip()
		parentCategory 	= row[1].strip()


		query = 		"MATCH (n:CATEGORY {{name : '{name}'}}) \n".format(name=parentCategory)
		query = query + "MATCH (m:CATEGORY {{name : '{name}'}}) \n".format(name=name)
		query = query + "MERGE(n)-[:HAS_SUBCAT]->(m)"

		transaction.run(query)

	transaction.commit()


def get_graph_connection():
	PORT 		= 9000
	BOLT_PORT 	= 9001
	PASSWORD 	= "ad3eedda5d0118116ec22394419131b8"
	USERNAME 	= "neo4j"
	HOST 		= "localhost"

	# Stack overflow		
	authenticate("localhost:9000", USERNAME, PASSWORD)
	
	return Graph(host=HOST,http_port=9000,bolt_port=9001,bolt=False)

if __name__ == '__main__':
	filename = sys.argv[1]

	load_categories(filename)