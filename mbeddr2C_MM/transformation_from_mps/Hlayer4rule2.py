from core.himesis import Himesis
import uuid

class Hlayer4rule2(Himesis):
	def __init__(self):
		"""
		Creates the himesis graph representing the DSLTrans rule layer4rule2.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(Hlayer4rule2, self).__init__(name='Hlayer4rule2', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """layer4rule2"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule2')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """layer4rule2"""

		# match class ImplementationModule(layer4rule2class0ImplementationModule) node
		self.add_node()
		self.vs[3]["mm__"] = """ImplementationModule"""
		self.vs[3]["attr1"] = """+"""

		# match class TestCase(layer4rule2class1TestCase) node
		self.add_node()
		self.vs[4]["mm__"] = """TestCase"""
		self.vs[4]["attr1"] = """+"""

		# apply class ImplementationModule(layer4rule2class2ImplementationModule) node
		self.add_node()
		self.vs[5]["mm__"] = """ImplementationModule"""
		self.vs[5]["attr1"] = """1"""

		# apply class Function(layer4rule2class3Function) node
		self.add_node()
		self.vs[6]["mm__"] = """Function"""
		self.vs[6]["attr1"] = """1"""

		# apply class VoidType(layer4rule2class4VoidType) node
		self.add_node()
		self.vs[7]["mm__"] = """VoidType"""
		self.vs[7]["attr1"] = """1"""

		# apply class StatementList(layer4rule2class5StatementList) node
		self.add_node()
		self.vs[8]["mm__"] = """StatementList"""
		self.vs[8]["attr1"] = """1"""

		# match association ImplementationModule--contents-->TestCase node 
		self.add_node()
		self.vs[9]["attr1"] = """contents"""
		self.vs[9]["mm__"] = """directLink_S"""

		# apply association ImplementationModule--contents-->Function node 
		self.add_node()
		self.vs[10]["attr1"] = """contents"""
		self.vs[10]["mm__"] = """directLink_T"""

		# apply association Function--type-->VoidType node 
		self.add_node()
		self.vs[11]["attr1"] = """type"""
		self.vs[11]["mm__"] = """directLink_T"""

		# apply association Function--body-->StatementList node 
		self.add_node()
		self.vs[12]["attr1"] = """body"""
		self.vs[12]["mm__"] = """directLink_T"""

		# backward association ImplementationModule-->ImplementationModulenode 
		self.add_node()
		self.vs[13]["mm__"] = """backward_link"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class ImplementationModule(layer4rule2class0ImplementationModule)
			(0,4), # matchmodel -> match_class TestCase(layer4rule2class1TestCase)
			(1,5), # applymodel -> apply_classImplementationModule(layer4rule2class2ImplementationModule)
			(1,6), # applymodel -> apply_classFunction(layer4rule2class3Function)
			(1,7), # applymodel -> apply_classVoidType(layer4rule2class4VoidType)
			(1,8), # applymodel -> apply_classStatementList(layer4rule2class5StatementList)
			(3,9), # match classImplementationModule(layer4rule2class0ImplementationModule) -> association contents
			(9,4), # associationcontents -> match_classImplementationModule(layer4rule2class1TestCase)
			(5,10), # apply class ImplementationModule(layer4rule2class2ImplementationModule) -> association contents
			(10,6), # associationcontents -> apply_classFunction(layer4rule2class3Function)
			(6,11), # apply class Function(layer4rule2class3Function) -> association type
			(11,7), # associationtype -> apply_classVoidType(layer4rule2class4VoidType)
			(6,12), # apply class Function(layer4rule2class3Function) -> association body
			(12,8), # associationbody -> apply_classStatementList(layer4rule2class5StatementList)
			(5,13), # apply class ImplementationModule(layer4rule2class0ImplementationModule) -> backward_association 
			(13,3), # backward_associationImplementationModule -> match_class ImplementationModule(layer4rule2class0ImplementationModule)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = [((6,'name'),('concat',((3,'name'),('concat',(('constant','_'),(4,'name')))))),]
