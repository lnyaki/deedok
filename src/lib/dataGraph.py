
class DataGraph():
	_graph 	= None
	_cursor	= None

	def __init__(self, dbPathData):
		self._graph = self.initialize(dbPathData)
		pass

	def initialize(self,dbPathData):
		pass