from core.himesis import Himesis
import uuid

class Hlayer3rule0(Himesis):
	def __init__(self):
		"""
		Creates the himesis graph representing the DSLTrans rule layer3rule0.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(Hlayer3rule0, self).__init__(name='Hlayer3rule0', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """layer3rule0"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule0')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """layer3rule0"""

		# match class ImplementationModule(layer3rule0class0ImplementationModule) node
		self.add_node()
		self.vs[3]["mm__"] = """ImplementationModule"""
		self.vs[3]["attr1"] = """+"""

		# match class Function(layer3rule0class1Function) node
		self.add_node()
		self.vs[4]["mm__"] = """Function"""
		self.vs[4]["attr1"] = """+"""

		# match class Int32Type(layer3rule0class2Int32Type) node
		self.add_node()
		self.vs[5]["mm__"] = """Int32Type"""
		self.vs[5]["attr1"] = """+"""

		# apply class ImplementationModule(layer3rule0class3ImplementationModule) node
		self.add_node()
		self.vs[6]["mm__"] = """ImplementationModule"""
		self.vs[6]["attr1"] = """1"""

		# apply class FunctionPrototype(layer3rule0class4FunctionPrototype) node
		self.add_node()
		self.vs[7]["mm__"] = """FunctionPrototype"""
		self.vs[7]["attr1"] = """1"""

		# apply class VoidType(layer3rule0class5VoidType) node
		self.add_node()
		self.vs[8]["mm__"] = """VoidType"""
		self.vs[8]["attr1"] = """1"""

		# match association ImplementationModule--contents-->Function node 
		self.add_node()
		self.vs[9]["attr1"] = """contents"""
		self.vs[9]["mm__"] = """directLink_S"""

		# match association Function--type-->Int32Type node 
		self.add_node()
		self.vs[10]["attr1"] = """type"""
		self.vs[10]["mm__"] = """directLink_S"""

		# apply association ImplementationModule--contents-->FunctionPrototype node 
		self.add_node()
		self.vs[11]["attr1"] = """contents"""
		self.vs[11]["mm__"] = """directLink_T"""

		# apply association FunctionPrototype--type-->VoidType node 
		self.add_node()
		self.vs[12]["attr1"] = """type"""
		self.vs[12]["mm__"] = """directLink_T"""

		# backward association ImplementationModule-->ImplementationModulenode 
		self.add_node()
		self.vs[13]["mm__"] = """backward_link"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class ImplementationModule(layer3rule0class0ImplementationModule)
			(0,4), # matchmodel -> match_class Function(layer3rule0class1Function)
			(0,5), # matchmodel -> match_class Int32Type(layer3rule0class2Int32Type)
			(1,6), # applymodel -> apply_classImplementationModule(layer3rule0class3ImplementationModule)
			(1,7), # applymodel -> apply_classFunctionPrototype(layer3rule0class4FunctionPrototype)
			(1,8), # applymodel -> apply_classVoidType(layer3rule0class5VoidType)
			(3,9), # match classImplementationModule(layer3rule0class0ImplementationModule) -> association contents
			(9,4), # associationcontents -> match_classImplementationModule(layer3rule0class1Function)
			(4,10), # match classFunction(layer3rule0class1Function) -> association type
			(10,5), # associationtype -> match_classFunction(layer3rule0class2Int32Type)
			(6,11), # apply class ImplementationModule(layer3rule0class3ImplementationModule) -> association contents
			(11,7), # associationcontents -> apply_classFunctionPrototype(layer3rule0class4FunctionPrototype)
			(7,12), # apply class FunctionPrototype(layer3rule0class4FunctionPrototype) -> association type
			(12,8), # associationtype -> apply_classVoidType(layer3rule0class5VoidType)
			(6,13), # apply class ImplementationModule(layer3rule0class0ImplementationModule) -> backward_association 
			(13,3), # backward_associationImplementationModule -> match_class ImplementationModule(layer3rule0class0ImplementationModule)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = [((7,'name'),('concat',((3,'name'),('constant','_blockexpr_main_2')))),]
