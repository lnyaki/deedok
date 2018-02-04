
class DataGraphNode():
	_parents 	= None
	_relations	= None
	_properties = None

	def __init__(self, propertiesDictionary=None):
		self._properties = propertiesDictionary

	def addRelation(self, relationData, NodeData):
		pass

	def getChildren(self):
		pass
