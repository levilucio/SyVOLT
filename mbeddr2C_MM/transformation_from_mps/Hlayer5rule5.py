from core.himesis import Himesis
import uuid

class Hlayer5rule5(Himesis):
	def __init__(self):
		"""
		Creates the himesis graph representing the DSLTrans rule layer5rule5.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(Hlayer5rule5, self).__init__(name='Hlayer5rule5', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """layer5rule5"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule5')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """layer5rule5"""

		# match class StatementList(layer5rule5class0StatementList) node
		self.add_node()
		self.vs[3]["mm__"] = """StatementList"""
		self.vs[3]["attr1"] = """+"""

		# match class ReturnStatement(layer5rule5class1ReturnStatement) node
		self.add_node()
		self.vs[4]["mm__"] = """ReturnStatement"""
		self.vs[4]["attr1"] = """+"""

		# match class ExecuteTestExpression(layer5rule5class2ExecuteTestExpression) node
		self.add_node()
		self.vs[5]["mm__"] = """ExecuteTestExpression"""
		self.vs[5]["attr1"] = """+"""

		# match class Function(layer5rule5class3Function) node
		self.add_node()
		self.vs[6]["mm__"] = """Function"""
		self.vs[6]["attr1"] = """+"""

		# match class TestCaseRef(layer5rule5class4TestCaseRef) node
		self.add_node()
		self.vs[7]["mm__"] = """TestCaseRef"""
		self.vs[7]["attr1"] = """+"""

		# match class TestCase(layer5rule5class5TestCase) node
		self.add_node()
		self.vs[8]["mm__"] = """TestCase"""
		self.vs[8]["attr1"] = """+"""

		# apply class StatementList(layer5rule5class6StatementList) node
		self.add_node()
		self.vs[9]["mm__"] = """StatementList"""
		self.vs[9]["attr1"] = """1"""

		# apply class ExpressionStatement(layer5rule5class7ExpressionStatement) node
		self.add_node()
		self.vs[10]["mm__"] = """ExpressionStatement"""
		self.vs[10]["attr1"] = """1"""

		# apply class FunctionCall(layer5rule5class8FunctionCall) node
		self.add_node()
		self.vs[11]["mm__"] = """FunctionCall"""
		self.vs[11]["attr1"] = """1"""

		# apply class FunctionPrototype(layer5rule5class9FunctionPrototype) node
		self.add_node()
		self.vs[12]["mm__"] = """FunctionPrototype"""
		self.vs[12]["attr1"] = """1"""

		# match association Function--body-->StatementList node 
		self.add_node()
		self.vs[13]["attr1"] = """body"""
		self.vs[13]["mm__"] = """directLink_S"""

		# match association StatementList--statements-->ReturnStatement node 
		self.add_node()
		self.vs[14]["attr1"] = """statements"""
		self.vs[14]["mm__"] = """directLink_S"""

		# match association ReturnStatement--expression-->ExecuteTestExpression node 
		self.add_node()
		self.vs[15]["attr1"] = """expression"""
		self.vs[15]["mm__"] = """directLink_S"""

		# match association ExecuteTestExpression--tests-->TestCaseRef node 
		self.add_node()
		self.vs[16]["attr1"] = """tests"""
		self.vs[16]["mm__"] = """directLink_S"""

		# match association TestCaseRef--testcase-->TestCase node 
		self.add_node()
		self.vs[17]["attr1"] = """testcase"""
		self.vs[17]["mm__"] = """directLink_S"""

		# apply association StatementList--statements-->ExpressionStatement node 
		self.add_node()
		self.vs[18]["attr1"] = """statements"""
		self.vs[18]["mm__"] = """directLink_T"""

		# apply association ExpressionStatement--expr-->FunctionCall node 
		self.add_node()
		self.vs[19]["attr1"] = """expr"""
		self.vs[19]["mm__"] = """directLink_T"""

		# apply association FunctionCall--function-->FunctionPrototype node 
		self.add_node()
		self.vs[20]["attr1"] = """function"""
		self.vs[20]["mm__"] = """directLink_T"""

		# backward association StatementList-->Functionnode 
		self.add_node()
		self.vs[21]["mm__"] = """backward_link"""

		# backward association FunctionPrototype-->TestCasenode 
		self.add_node()
		self.vs[22]["mm__"] = """backward_link"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class StatementList(layer5rule5class0StatementList)
			(0,4), # matchmodel -> match_class ReturnStatement(layer5rule5class1ReturnStatement)
			(0,5), # matchmodel -> match_class ExecuteTestExpression(layer5rule5class2ExecuteTestExpression)
			(0,6), # matchmodel -> match_class Function(layer5rule5class3Function)
			(0,7), # matchmodel -> match_class TestCaseRef(layer5rule5class4TestCaseRef)
			(0,8), # matchmodel -> match_class TestCase(layer5rule5class5TestCase)
			(1,9), # applymodel -> apply_classStatementList(layer5rule5class6StatementList)
			(1,10), # applymodel -> apply_classExpressionStatement(layer5rule5class7ExpressionStatement)
			(1,11), # applymodel -> apply_classFunctionCall(layer5rule5class8FunctionCall)
			(1,12), # applymodel -> apply_classFunctionPrototype(layer5rule5class9FunctionPrototype)
			(6,13), # match classFunction(layer5rule5class3Function) -> association body
			(13,3), # associationbody -> match_classFunction(layer5rule5class0StatementList)
			(3,14), # match classStatementList(layer5rule5class0StatementList) -> association statements
			(14,4), # associationstatements -> match_classStatementList(layer5rule5class1ReturnStatement)
			(4,15), # match classReturnStatement(layer5rule5class1ReturnStatement) -> association expression
			(15,5), # associationexpression -> match_classReturnStatement(layer5rule5class2ExecuteTestExpression)
			(5,16), # match classExecuteTestExpression(layer5rule5class2ExecuteTestExpression) -> association tests
			(16,7), # associationtests -> match_classExecuteTestExpression(layer5rule5class4TestCaseRef)
			(7,17), # match classTestCaseRef(layer5rule5class4TestCaseRef) -> association testcase
			(17,8), # associationtestcase -> match_classTestCaseRef(layer5rule5class5TestCase)
			(9,18), # apply class StatementList(layer5rule5class6StatementList) -> association statements
			(18,10), # associationstatements -> apply_classExpressionStatement(layer5rule5class7ExpressionStatement)
			(10,19), # apply class ExpressionStatement(layer5rule5class7ExpressionStatement) -> association expr
			(19,11), # associationexpr -> apply_classFunctionCall(layer5rule5class8FunctionCall)
			(11,20), # apply class FunctionCall(layer5rule5class8FunctionCall) -> association function
			(20,12), # associationfunction -> apply_classFunctionPrototype(layer5rule5class9FunctionPrototype)
			(9,21), # apply class StatementList(layer5rule5class3Function) -> backward_association 
			(21,6), # backward_associationFunction -> match_class Function(layer5rule5class3Function)
			(12,22), # apply class FunctionPrototype(layer5rule5class5TestCase) -> backward_association 
			(22,8), # backward_associationTestCase -> match_class TestCase(layer5rule5class5TestCase)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = []
