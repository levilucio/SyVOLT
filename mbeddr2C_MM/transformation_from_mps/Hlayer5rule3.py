from core.himesis import Himesis
import uuid

class Hlayer5rule3(Himesis):
	def __init__(self):
		"""
		Creates the himesis graph representing the DSLTrans rule layer5rule3.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(Hlayer5rule3, self).__init__(name='Hlayer5rule3', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """layer5rule3"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule3')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """layer5rule3"""

		# match class TestCase(layer5rule3class0TestCase) node
		self.add_node()
		self.vs[3]["mm__"] = """TestCase"""
		self.vs[3]["attr1"] = """+"""

		# match class StatementList(layer5rule3class1StatementList) node
		self.add_node()
		self.vs[4]["mm__"] = """StatementList"""
		self.vs[4]["attr1"] = """+"""

		# match class InitializeConfiguration(layer5rule3class2InitializeConfiguration) node
		self.add_node()
		self.vs[5]["mm__"] = """InitializeConfiguration"""
		self.vs[5]["attr1"] = """+"""

		# match class InstanceConfiguration(layer5rule3class3InstanceConfiguration) node
		self.add_node()
		self.vs[6]["mm__"] = """InstanceConfiguration"""
		self.vs[6]["attr1"] = """+"""

		# apply class StatementList(layer5rule3class4StatementList) node
		self.add_node()
		self.vs[7]["mm__"] = """StatementList"""
		self.vs[7]["attr1"] = """1"""

		# apply class ExpressionStatement(layer5rule3class5ExpressionStatement) node
		self.add_node()
		self.vs[8]["mm__"] = """ExpressionStatement"""
		self.vs[8]["attr1"] = """1"""

		# apply class FunctionCall(layer5rule3class6FunctionCall) node
		self.add_node()
		self.vs[9]["mm__"] = """FunctionCall"""
		self.vs[9]["attr1"] = """1"""

		# apply class FunctionPrototype(layer5rule3class7FunctionPrototype) node
		self.add_node()
		self.vs[10]["mm__"] = """FunctionPrototype"""
		self.vs[10]["attr1"] = """1"""

		# match association TestCase--body-->StatementList node 
		self.add_node()
		self.vs[11]["attr1"] = """body"""
		self.vs[11]["mm__"] = """directLink_S"""

		# match association StatementList--statements-->InitializeConfiguration node 
		self.add_node()
		self.vs[12]["attr1"] = """statements"""
		self.vs[12]["mm__"] = """directLink_S"""

		# match association InitializeConfiguration--config-->InstanceConfiguration node 
		self.add_node()
		self.vs[13]["attr1"] = """config"""
		self.vs[13]["mm__"] = """directLink_S"""

		# apply association StatementList--statements-->ExpressionStatement node 
		self.add_node()
		self.vs[14]["attr1"] = """statements"""
		self.vs[14]["mm__"] = """directLink_T"""

		# apply association ExpressionStatement--expr-->FunctionCall node 
		self.add_node()
		self.vs[15]["attr1"] = """expr"""
		self.vs[15]["mm__"] = """directLink_T"""

		# apply association FunctionCall--function-->FunctionPrototype node 
		self.add_node()
		self.vs[16]["attr1"] = """function"""
		self.vs[16]["mm__"] = """directLink_T"""

		# backward association StatementList-->TestCasenode 
		self.add_node()
		self.vs[17]["mm__"] = """backward_link"""

		# backward association FunctionPrototype-->InstanceConfigurationnode 
		self.add_node()
		self.vs[18]["mm__"] = """backward_link"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class TestCase(layer5rule3class0TestCase)
			(0,4), # matchmodel -> match_class StatementList(layer5rule3class1StatementList)
			(0,5), # matchmodel -> match_class InitializeConfiguration(layer5rule3class2InitializeConfiguration)
			(0,6), # matchmodel -> match_class InstanceConfiguration(layer5rule3class3InstanceConfiguration)
			(1,7), # applymodel -> apply_classStatementList(layer5rule3class4StatementList)
			(1,8), # applymodel -> apply_classExpressionStatement(layer5rule3class5ExpressionStatement)
			(1,9), # applymodel -> apply_classFunctionCall(layer5rule3class6FunctionCall)
			(1,10), # applymodel -> apply_classFunctionPrototype(layer5rule3class7FunctionPrototype)
			(3,11), # match classTestCase(layer5rule3class0TestCase) -> association body
			(11,4), # associationbody -> match_classTestCase(layer5rule3class1StatementList)
			(4,12), # match classStatementList(layer5rule3class1StatementList) -> association statements
			(12,5), # associationstatements -> match_classStatementList(layer5rule3class2InitializeConfiguration)
			(5,13), # match classInitializeConfiguration(layer5rule3class2InitializeConfiguration) -> association config
			(13,6), # associationconfig -> match_classInitializeConfiguration(layer5rule3class3InstanceConfiguration)
			(7,14), # apply class StatementList(layer5rule3class4StatementList) -> association statements
			(14,8), # associationstatements -> apply_classExpressionStatement(layer5rule3class5ExpressionStatement)
			(8,15), # apply class ExpressionStatement(layer5rule3class5ExpressionStatement) -> association expr
			(15,9), # associationexpr -> apply_classFunctionCall(layer5rule3class6FunctionCall)
			(9,16), # apply class FunctionCall(layer5rule3class6FunctionCall) -> association function
			(16,10), # associationfunction -> apply_classFunctionPrototype(layer5rule3class7FunctionPrototype)
			(7,17), # apply class StatementList(layer5rule3class0TestCase) -> backward_association 
			(17,3), # backward_associationTestCase -> match_class TestCase(layer5rule3class0TestCase)
			(10,18), # apply class FunctionPrototype(layer5rule3class3InstanceConfiguration) -> backward_association 
			(18,6), # backward_associationInstanceConfiguration -> match_class InstanceConfiguration(layer5rule3class3InstanceConfiguration)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = []
