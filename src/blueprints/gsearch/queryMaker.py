

def selectCategories(categoryList):
	pass

def selectItems():
	pass

def buildQuery(label, propertyName, eltList):
	'''
	Human query : give me <what> from <where>.
	Ex: give me the <total number> of <goals>(b) scored by <romelu lukaku>(a) during <season 2012-2013> (b)
	
	==> In cypher, this is translated in a query that has 3 parts.
	- Part 1 : get the context 				"match(xxx)-[yy]->(zz) with zz"
	- Part 2 : reach desired information 	"match (zz)-[r]->(a)"
	- Part 3 : return info 					"return zz.type, a.name, a.size"
	'''
	#1) Return the main context on which the actual query wil be applied
	#getQueryContext()

	#2) Select the various elements from which a value will be returned
	# getSelectedNodes()

	#3) Return the data from the selected elements
	# getReturnData()

	response = selectNodes(label,propertyName, eltList)
	response = response + selectAttributes('','')

	return response

def getQueryContext(contextData):
	'''
	contextData is an object that contains details on how to build the query
	ex:{label:'OBJECT',variable:'lukaku', first_name:'romelu', last_name:'lukaku'}
	==> match(lukaku:OBJECT)-[:FIRST_NAME]->(:ITEM{value:"romelu"})
		match(lukaku)-[:LAST_NAME]->({name:"lukaku"})
		with lukaku

	ex 2: [{type:'relation',
			base_node:{label:'OBJECT', variable:'lukaku', properties:{}},
			relation:{direction:'to_target/to_base_node',name:'FIRST_NAME',properties:{}, variable:''},
			target_node:{label:'ITEM',variable:'target', properties:{name:'romelu'}},
			target_relation:
				{type:'partial_relation',
				direction:'to_base_node', 
				relation:{direction:'to_base_node', name:'xx', properties:{}}}
			},
			{}]
	'''

def selectNodes(label, propertyName,elementList):
	matchQuery = ""
	selectName = "n"


	for elt in elementList:
		matchQuery = matchQuery + "MATCH (:{label} {{{property}:'{value}'}})-[]-({selectName}:OBJECT)\n".format(label=label,property=propertyName,value=elt,selectName=selectName)

	matchQuery = matchQuery + "WITH {selectName}\n".format(selectName="n")
	return matchQuery

def selectAttributes(selectedElements, attributes):
	return ""

def getArchetypes(categoryName):
	query = "MATCH (n:CATEGORY{{name:'{category}'}})-[:ATTRIBUTE]->(item:ITEM) return item.name as property, item.access as access".format(category=categoryName)
	return query


if __name__ == '__main__':
	label = "CATEGORY"
	propertyName = "name"
	eltList = ['first name','last name']

	response = buildQuery(label,propertyName,eltList)
	print(response)

	#	Ex: give me the <total number> of <goals>(b) scored by <romelu lukaku>(a) during <season 2012-2013> (b)
	base_node = {'label': 'OBJECT', 'variable':'lukaku'}
	target_node1 = {label:'ITEM', 'variable': 'target1', 'properties':{'name':'romelu'}}
	target_node2 = {label:'ITEM', 'variable': 'target2', 'properties':{'name':'lukaku'}}
	relation1 = {'type': 'relation', 'base_node': base_node, 'target_node':target_node1, 'relation': {'name':'first_name','direction':'to_target'}}
	relation2 = {'type': 'relation', 'base_node': base_node, 'target_node':target_node2, 'relation': {'name':'first_name','direction':'to_target'}}
	data = {}
	contextData = {}
	response = getQueryContext(contextData)
	print(response)

	print('Archetypes')
	archetypes = getArchetypes('character')
	print(archetypes)