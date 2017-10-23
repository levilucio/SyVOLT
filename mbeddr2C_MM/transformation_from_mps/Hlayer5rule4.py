from core.himesis import Himesis
import uuid

class Hlayer5rule4(Himesis):
	def __init__(self):
		"""
		Creates the himesis graph representing the DSLTrans rule layer5rule4.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(Hlayer5rule4, self).__init__(name='Hlayer5rule4', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """layer5rule4"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule4')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """layer5rule4"""

		# match class TestCase(layer5rule4class0TestCase) node
		self.add_node()
		self.vs[3]["mm__"] = """TestCase"""
		self.vs[3]["attr1"] = """+"""

		# match class StatementList(layer5rule4class1StatementList) node
		self.add_node()
		self.vs[4]["mm__"] = """StatementList"""
		self.vs[4]["attr1"] = """+"""

		# match class ExpressionStatement(layer5rule4class2ExpressionStatement) node
		self.add_node()
		self.vs[5]["mm__"] = """ExpressionStatement"""
		self.vs[5]["attr1"] = """+"""

		# match class PortAdapterOpCallExpr(layer5rule4class3PortAdapterOpCallExpr) node
		self.add_node()
		self.vs[6]["mm__"] = """PortAdapterOpCallExpr"""
		self.vs[6]["attr1"] = """+"""

		# match class PortAdapterRefExpr(layer5rule4class4PortAdapterRefExpr) node
		self.add_node()
		self.vs[7]["mm__"] = """PortAdapterRefExpr"""
		self.vs[7]["attr1"] = """+"""

		# match class PortAdapter(layer5rule4class5PortAdapter) node
		self.add_node()
		self.vs[8]["mm__"] = """PortAdapter"""
		self.vs[8]["attr1"] = """+"""

		# match class Operation(layer5rule4class6Operation) node
		self.add_node()
		self.vs[9]["mm__"] = """Operation"""
		self.vs[9]["attr1"] = """+"""

		# match class AdapterInstancePortRef(layer5rule4class7AdapterInstancePortRef) node
		self.add_node()
		self.vs[10]["mm__"] = """AdapterInstancePortRef"""
		self.vs[10]["attr1"] = """+"""

		# match class ComponentInstance(layer5rule4class8ComponentInstance) node
		self.add_node()
		self.vs[11]["mm__"] = """ComponentInstance"""
		self.vs[11]["attr1"] = """+"""

		# match class ProvidedPort(layer5rule4class9ProvidedPort) node
		self.add_node()
		self.vs[12]["mm__"] = """ProvidedPort"""
		self.vs[12]["attr1"] = """+"""

		# match class ClientServerInterface(layer5rule4class10ClientServerInterface) node
		self.add_node()
		self.vs[13]["mm__"] = """ClientServerInterface"""
		self.vs[13]["attr1"] = """+"""

		# apply class StatementList(layer5rule4class11StatementList) node
		self.add_node()
		self.vs[14]["mm__"] = """StatementList"""
		self.vs[14]["attr1"] = """1"""

		# apply class ExpressionStatement(layer5rule4class12ExpressionStatement) node
		self.add_node()
		self.vs[15]["mm__"] = """ExpressionStatement"""
		self.vs[15]["attr1"] = """1"""

		# apply class FunctionCall(layer5rule4class13FunctionCall) node
		self.add_node()
		self.vs[16]["mm__"] = """FunctionCall"""
		self.vs[16]["attr1"] = """1"""

		# apply class FunctionPrototype(layer5rule4class14FunctionPrototype) node
		self.add_node()
		self.vs[17]["mm__"] = """FunctionPrototype"""
		self.vs[17]["attr1"] = """1"""

		# apply class ReferenceExpr(layer5rule4class15ReferenceExpr) node
		self.add_node()
		self.vs[18]["mm__"] = """ReferenceExpr"""
		self.vs[18]["attr1"] = """1"""

		# apply class GlobalVarRef(layer5rule4class16GlobalVarRef) node
		self.add_node()
		self.vs[19]["mm__"] = """GlobalVarRef"""
		self.vs[19]["attr1"] = """1"""

		# apply class GlobalVariableDeclaration(layer5rule4class17GlobalVariableDeclaration) node
		self.add_node()
		self.vs[20]["mm__"] = """GlobalVariableDeclaration"""
		self.vs[20]["attr1"] = """1"""

		# match association TestCase--body-->StatementList node 
		self.add_node()
		self.vs[21]["attr1"] = """body"""
		self.vs[21]["mm__"] = """directLink_S"""

		# match association StatementList--statements-->ExpressionStatement node 
		self.add_node()
		self.vs[22]["attr1"] = """statements"""
		self.vs[22]["mm__"] = """directLink_S"""

		# match association ExpressionStatement--expr-->PortAdapterOpCallExpr node 
		self.add_node()
		self.vs[23]["attr1"] = """expr"""
		self.vs[23]["mm__"] = """directLink_S"""

		# match association PortAdapterOpCallExpr--expression-->PortAdapterRefExpr node 
		self.add_node()
		self.vs[24]["attr1"] = """expression"""
		self.vs[24]["mm__"] = """directLink_S"""

		# match association PortAdapterRefExpr--portAdater-->PortAdapter node 
		self.add_node()
		self.vs[25]["attr1"] = """portAdater"""
		self.vs[25]["mm__"] = """directLink_S"""

		# match association PortAdapterOpCallExpr--operation-->Operation node 
		self.add_node()
		self.vs[26]["attr1"] = """operation"""
		self.vs[26]["mm__"] = """directLink_S"""

		# match association PortAdapter--portRef-->AdapterInstancePortRef node 
		self.add_node()
		self.vs[27]["attr1"] = """portRef"""
		self.vs[27]["mm__"] = """directLink_S"""

		# match association AdapterInstancePortRef--instance-->ComponentInstance node 
		self.add_node()
		self.vs[28]["attr1"] = """instance"""
		self.vs[28]["mm__"] = """directLink_S"""

		# match association AdapterInstancePortRef--port-->ProvidedPort node 
		self.add_node()
		self.vs[29]["attr1"] = """port"""
		self.vs[29]["mm__"] = """directLink_S"""

		# match association ProvidedPort--intf-->ClientServerInterface node 
		self.add_node()
		self.vs[30]["attr1"] = """intf"""
		self.vs[30]["mm__"] = """directLink_S"""

		# match association ClientServerInterface--contents-->Operation node 
		self.add_node()
		self.vs[31]["attr1"] = """contents"""
		self.vs[31]["mm__"] = """directLink_S"""

		# apply association StatementList--statements-->ExpressionStatement node 
		self.add_node()
		self.vs[32]["attr1"] = """statements"""
		self.vs[32]["mm__"] = """directLink_T"""

		# apply association ExpressionStatement--expr-->FunctionCall node 
		self.add_node()
		self.vs[33]["attr1"] = """expr"""
		self.vs[33]["mm__"] = """directLink_T"""

		# apply association FunctionCall--function-->FunctionPrototype node 
		self.add_node()
		self.vs[34]["attr1"] = """function"""
		self.vs[34]["mm__"] = """directLink_T"""

		# apply association FunctionCall--actuals-->ReferenceExpr node 
		self.add_node()
		self.vs[35]["attr1"] = """actuals"""
		self.vs[35]["mm__"] = """directLink_T"""

		# apply association ReferenceExpr--expression-->GlobalVarRef node 
		self.add_node()
		self.vs[36]["attr1"] = """expression"""
		self.vs[36]["mm__"] = """directLink_T"""

		# apply association GlobalVarRef--var-->GlobalVariableDeclaration node 
		self.add_node()
		self.vs[37]["attr1"] = """var"""
		self.vs[37]["mm__"] = """directLink_T"""

		# backward association StatementList-->TestCasenode 
		self.add_node()
		self.vs[38]["mm__"] = """backward_link"""

		# backward association FunctionPrototype-->ProvidedPortnode 
		self.add_node()
		self.vs[39]["mm__"] = """backward_link"""

		# backward association GlobalVariableDeclaration-->ComponentInstancenode 
		self.add_node()
		self.vs[40]["mm__"] = """backward_link"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class TestCase(layer5rule4class0TestCase)
			(0,4), # matchmodel -> match_class StatementList(layer5rule4class1StatementList)
			(0,5), # matchmodel -> match_class ExpressionStatement(layer5rule4class2ExpressionStatement)
			(0,6), # matchmodel -> match_class PortAdapterOpCallExpr(layer5rule4class3PortAdapterOpCallExpr)
			(0,7), # matchmodel -> match_class PortAdapterRefExpr(layer5rule4class4PortAdapterRefExpr)
			(0,8), # matchmodel -> match_class PortAdapter(layer5rule4class5PortAdapter)
			(0,9), # matchmodel -> match_class Operation(layer5rule4class6Operation)
			(0,10), # matchmodel -> match_class AdapterInstancePortRef(layer5rule4class7AdapterInstancePortRef)
			(0,11), # matchmodel -> match_class ComponentInstance(layer5rule4class8ComponentInstance)
			(0,12), # matchmodel -> match_class ProvidedPort(layer5rule4class9ProvidedPort)
			(0,13), # matchmodel -> match_class ClientServerInterface(layer5rule4class10ClientServerInterface)
			(1,14), # applymodel -> apply_classStatementList(layer5rule4class11StatementList)
			(1,15), # applymodel -> apply_classExpressionStatement(layer5rule4class12ExpressionStatement)
			(1,16), # applymodel -> apply_classFunctionCall(layer5rule4class13FunctionCall)
			(1,17), # applymodel -> apply_classFunctionPrototype(layer5rule4class14FunctionPrototype)
			(1,18), # applymodel -> apply_classReferenceExpr(layer5rule4class15ReferenceExpr)
			(1,19), # applymodel -> apply_classGlobalVarRef(layer5rule4class16GlobalVarRef)
			(1,20), # applymodel -> apply_classGlobalVariableDeclaration(layer5rule4class17GlobalVariableDeclaration)
			(3,21), # match classTestCase(layer5rule4class0TestCase) -> association body
			(21,4), # associationbody -> match_classTestCase(layer5rule4class1StatementList)
			(4,22), # match classStatementList(layer5rule4class1StatementList) -> association statements
			(22,5), # associationstatements -> match_classStatementList(layer5rule4class2ExpressionStatement)
			(5,23), # match classExpressionStatement(layer5rule4class2ExpressionStatement) -> association expr
			(23,6), # associationexpr -> match_classExpressionStatement(layer5rule4class3PortAdapterOpCallExpr)
			(6,24), # match classPortAdapterOpCallExpr(layer5rule4class3PortAdapterOpCallExpr) -> association expression
			(24,7), # associationexpression -> match_classPortAdapterOpCallExpr(layer5rule4class4PortAdapterRefExpr)
			(7,25), # match classPortAdapterRefExpr(layer5rule4class4PortAdapterRefExpr) -> association portAdater
			(25,8), # associationportAdater -> match_classPortAdapterRefExpr(layer5rule4class5PortAdapter)
			(6,26), # match classPortAdapterOpCallExpr(layer5rule4class3PortAdapterOpCallExpr) -> association operation
			(26,9), # associationoperation -> match_classPortAdapterOpCallExpr(layer5rule4class6Operation)
			(8,27), # match classPortAdapter(layer5rule4class5PortAdapter) -> association portRef
			(27,10), # associationportRef -> match_classPortAdapter(layer5rule4class7AdapterInstancePortRef)
			(10,28), # match classAdapterInstancePortRef(layer5rule4class7AdapterInstancePortRef) -> association instance
			(28,11), # associationinstance -> match_classAdapterInstancePortRef(layer5rule4class8ComponentInstance)
			(10,29), # match classAdapterInstancePortRef(layer5rule4class7AdapterInstancePortRef) -> association port
			(29,12), # associationport -> match_classAdapterInstancePortRef(layer5rule4class9ProvidedPort)
			(12,30), # match classProvidedPort(layer5rule4class9ProvidedPort) -> association intf
			(30,13), # associationintf -> match_classProvidedPort(layer5rule4class10ClientServerInterface)
			(13,31), # match classClientServerInterface(layer5rule4class10ClientServerInterface) -> association contents
			(31,9), # associationcontents -> match_classClientServerInterface(layer5rule4class6Operation)
			(14,32), # apply class StatementList(layer5rule4class11StatementList) -> association statements
			(32,15), # associationstatements -> apply_classExpressionStatement(layer5rule4class12ExpressionStatement)
			(15,33), # apply class ExpressionStatement(layer5rule4class12ExpressionStatement) -> association expr
			(33,16), # associationexpr -> apply_classFunctionCall(layer5rule4class13FunctionCall)
			(16,34), # apply class FunctionCall(layer5rule4class13FunctionCall) -> association function
			(34,17), # associationfunction -> apply_classFunctionPrototype(layer5rule4class14FunctionPrototype)
			(16,35), # apply class FunctionCall(layer5rule4class13FunctionCall) -> association actuals
			(35,18), # associationactuals -> apply_classReferenceExpr(layer5rule4class15ReferenceExpr)
			(18,36), # apply class ReferenceExpr(layer5rule4class15ReferenceExpr) -> association expression
			(36,19), # associationexpression -> apply_classGlobalVarRef(layer5rule4class16GlobalVarRef)
			(19,37), # apply class GlobalVarRef(layer5rule4class16GlobalVarRef) -> association var
			(37,20), # associationvar -> apply_classGlobalVariableDeclaration(layer5rule4class17GlobalVariableDeclaration)
			(14,38), # apply class StatementList(layer5rule4class0TestCase) -> backward_association 
			(38,3), # backward_associationTestCase -> match_class TestCase(layer5rule4class0TestCase)
			(17,39), # apply class FunctionPrototype(layer5rule4class9ProvidedPort) -> backward_association 
			(39,12), # backward_associationProvidedPort -> match_class ProvidedPort(layer5rule4class9ProvidedPort)
			(20,40), # apply class GlobalVariableDeclaration(layer5rule4class8ComponentInstance) -> backward_association 
			(40,11), # backward_associationComponentInstance -> match_class ComponentInstance(layer5rule4class8ComponentInstance)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = []
