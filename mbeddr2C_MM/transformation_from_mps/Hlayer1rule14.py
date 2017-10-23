from core.himesis import Himesis
import uuid

class Hlayer1rule14(Himesis):
	def __init__(self):
		"""
		Creates the himesis graph representing the DSLTrans rule layer1rule14.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(Hlayer1rule14, self).__init__(name='Hlayer1rule14', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """layer1rule14"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule14')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """layer1rule14"""

		# match class Operation(layer1rule14class0Operation) node
		self.add_node()
		self.vs[3]["mm__"] = """Operation"""
		self.vs[3]["attr1"] = """+"""

		# match class StringType(layer1rule14class1StringType) node
		self.add_node()
		self.vs[4]["mm__"] = """StringType"""
		self.vs[4]["attr1"] = """+"""

		# apply class FunctionPrototype(layer1rule14class2FunctionPrototype) node
		self.add_node()
		self.vs[5]["mm__"] = """FunctionPrototype"""
		self.vs[5]["attr1"] = """1"""

		# apply class StringType(layer1rule14class3StringType) node
		self.add_node()
		self.vs[6]["mm__"] = """StringType"""
		self.vs[6]["attr1"] = """1"""

		# match association Operation--type-->StringType node 
		self.add_node()
		self.vs[7]["attr1"] = """type"""
		self.vs[7]["mm__"] = """directLink_S"""

		# apply association FunctionPrototype--type-->StringType node 
		self.add_node()
		self.vs[8]["attr1"] = """type"""
		self.vs[8]["mm__"] = """directLink_T"""

		# backward association FunctionPrototype-->Operationnode 
		self.add_node()
		self.vs[9]["mm__"] = """backward_link"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class Operation(layer1rule14class0Operation)
			(0,4), # matchmodel -> match_class StringType(layer1rule14class1StringType)
			(1,5), # applymodel -> apply_classFunctionPrototype(layer1rule14class2FunctionPrototype)
			(1,6), # applymodel -> apply_classStringType(layer1rule14class3StringType)
			(3,7), # match classOperation(layer1rule14class0Operation) -> association type
			(7,4), # associationtype -> match_classOperation(layer1rule14class1StringType)
			(5,8), # apply class FunctionPrototype(layer1rule14class2FunctionPrototype) -> association type
			(8,6), # associationtype -> apply_classStringType(layer1rule14class3StringType)
			(5,9), # apply class FunctionPrototype(layer1rule14class0Operation) -> backward_association 
			(9,3), # backward_associationOperation -> match_class Operation(layer1rule14class0Operation)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = []
