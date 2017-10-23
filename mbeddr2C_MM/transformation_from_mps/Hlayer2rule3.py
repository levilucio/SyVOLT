from core.himesis import Himesis
import uuid

class Hlayer2rule3(Himesis):
	def __init__(self):
		"""
		Creates the himesis graph representing the DSLTrans rule layer2rule3.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(Hlayer2rule3, self).__init__(name='Hlayer2rule3', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """layer2rule3"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer2rule3')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """layer2rule3"""

		# match class Operation(layer2rule3class0Operation) node
		self.add_node()
		self.vs[3]["mm__"] = """Operation"""
		self.vs[3]["attr1"] = """+"""

		# apply class FunctionPrototype(layer2rule3class1FunctionPrototype) node
		self.add_node()
		self.vs[4]["mm__"] = """FunctionPrototype"""
		self.vs[4]["attr1"] = """1"""

		# apply class Argument(layer2rule3class2Argument) node
		self.add_node()
		self.vs[5]["mm__"] = """Argument"""
		self.vs[5]["attr1"] = """1"""

		# apply class VoidType(layer2rule3class3VoidType) node
		self.add_node()
		self.vs[6]["mm__"] = """VoidType"""
		self.vs[6]["attr1"] = """1"""

		# apply class PointerType(layer2rule3class4PointerType) node
		self.add_node()
		self.vs[7]["mm__"] = """PointerType"""
		self.vs[7]["attr1"] = """1"""

		# apply association FunctionPrototype--arguments-->Argument node 
		self.add_node()
		self.vs[8]["attr1"] = """arguments"""
		self.vs[8]["mm__"] = """directLink_T"""

		# apply association Argument--type-->PointerType node 
		self.add_node()
		self.vs[9]["attr1"] = """type"""
		self.vs[9]["mm__"] = """directLink_T"""

		# apply association PointerType--baseType-->VoidType node 
		self.add_node()
		self.vs[10]["attr1"] = """baseType"""
		self.vs[10]["mm__"] = """directLink_T"""

		# backward association FunctionPrototype-->Operationnode 
		self.add_node()
		self.vs[11]["mm__"] = """backward_link"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class Operation(layer2rule3class0Operation)
			(1,4), # applymodel -> apply_classFunctionPrototype(layer2rule3class1FunctionPrototype)
			(1,5), # applymodel -> apply_classArgument(layer2rule3class2Argument)
			(1,6), # applymodel -> apply_classVoidType(layer2rule3class3VoidType)
			(1,7), # applymodel -> apply_classPointerType(layer2rule3class4PointerType)
			(4,8), # apply class FunctionPrototype(layer2rule3class1FunctionPrototype) -> association arguments
			(8,5), # associationarguments -> apply_classArgument(layer2rule3class2Argument)
			(5,9), # apply class Argument(layer2rule3class2Argument) -> association type
			(9,7), # associationtype -> apply_classPointerType(layer2rule3class4PointerType)
			(7,10), # apply class PointerType(layer2rule3class4PointerType) -> association baseType
			(10,6), # associationbaseType -> apply_classVoidType(layer2rule3class3VoidType)
			(4,11), # apply class FunctionPrototype(layer2rule3class0Operation) -> backward_association 
			(11,3), # backward_associationOperation -> match_class Operation(layer2rule3class0Operation)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = [((5,'name'),('constant','___id')),]
