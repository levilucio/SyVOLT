from core.himesis import Himesis
import uuid

class Hlayer4rule3(Himesis):
	def __init__(self):
		"""
		Creates the himesis graph representing the DSLTrans rule layer4rule3.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(Hlayer4rule3, self).__init__(name='Hlayer4rule3', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """layer4rule3"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule3')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """layer4rule3"""

		# match class ImplementationModule(layer4rule3class0ImplementationModule) node
		self.add_node()
		self.vs[3]["mm__"] = """ImplementationModule"""
		self.vs[3]["attr1"] = """+"""

		# match class Function(layer4rule3class1Function) node
		self.add_node()
		self.vs[4]["mm__"] = """Function"""
		self.vs[4]["attr1"] = """+"""

		# match class Int32Type(layer4rule3class2Int32Type) node
		self.add_node()
		self.vs[5]["mm__"] = """Int32Type"""
		self.vs[5]["attr1"] = """+"""

		# apply class ImplementationModule(layer4rule3class3ImplementationModule) node
		self.add_node()
		self.vs[6]["mm__"] = """ImplementationModule"""
		self.vs[6]["attr1"] = """1"""

		# apply class Function(layer4rule3class4Function) node
		self.add_node()
		self.vs[7]["mm__"] = """Function"""
		self.vs[7]["attr1"] = """1"""

		# apply class VoidType(layer4rule3class5VoidType) node
		self.add_node()
		self.vs[8]["mm__"] = """VoidType"""
		self.vs[8]["attr1"] = """1"""

		# apply class StatementList(layer4rule3class6StatementList) node
		self.add_node()
		self.vs[9]["mm__"] = """StatementList"""
		self.vs[9]["attr1"] = """1"""

		# apply class Function(layer4rule3class7Function) node
		self.add_node()
		self.vs[10]["mm__"] = """Function"""
		self.vs[10]["attr1"] = """1"""

		# apply class StatementList(layer4rule3class8StatementList) node
		self.add_node()
		self.vs[11]["mm__"] = """StatementList"""
		self.vs[11]["attr1"] = """1"""

		# apply class Int32Type(layer4rule3class9Int32Type) node
		self.add_node()
		self.vs[12]["mm__"] = """Int32Type"""
		self.vs[12]["attr1"] = """1"""

		# apply class ExpressionStatement(layer4rule3class10ExpressionStatement) node
		self.add_node()
		self.vs[13]["mm__"] = """ExpressionStatement"""
		self.vs[13]["attr1"] = """1"""

		# apply class FunctionCall(layer4rule3class11FunctionCall) node
		self.add_node()
		self.vs[14]["mm__"] = """FunctionCall"""
		self.vs[14]["attr1"] = """1"""

		# apply class FunctionPrototype(layer4rule3class12FunctionPrototype) node
		self.add_node()
		self.vs[15]["mm__"] = """FunctionPrototype"""
		self.vs[15]["attr1"] = """1"""

		# match association ImplementationModule--contents-->Function node 
		self.add_node()
		self.vs[16]["attr1"] = """contents"""
		self.vs[16]["mm__"] = """directLink_S"""

		# match association Function--type-->Int32Type node 
		self.add_node()
		self.vs[17]["attr1"] = """type"""
		self.vs[17]["mm__"] = """directLink_S"""

		# apply association ImplementationModule--contents-->Function node 
		self.add_node()
		self.vs[18]["attr1"] = """contents"""
		self.vs[18]["mm__"] = """directLink_T"""

		# apply association Function--type-->VoidType node 
		self.add_node()
		self.vs[19]["attr1"] = """type"""
		self.vs[19]["mm__"] = """directLink_T"""

		# apply association Function--body-->StatementList node 
		self.add_node()
		self.vs[20]["attr1"] = """body"""
		self.vs[20]["mm__"] = """directLink_T"""

		# apply association ImplementationModule--contents-->Function node 
		self.add_node()
		self.vs[21]["attr1"] = """contents"""
		self.vs[21]["mm__"] = """directLink_T"""

		# apply association Function--type-->Int32Type node 
		self.add_node()
		self.vs[22]["attr1"] = """type"""
		self.vs[22]["mm__"] = """directLink_T"""

		# apply association Function--body-->StatementList node 
		self.add_node()
		self.vs[23]["attr1"] = """body"""
		self.vs[23]["mm__"] = """directLink_T"""

		# apply association StatementList--statements-->ExpressionStatement node 
		self.add_node()
		self.vs[24]["attr1"] = """statements"""
		self.vs[24]["mm__"] = """directLink_T"""

		# apply association ExpressionStatement--expr-->FunctionCall node 
		self.add_node()
		self.vs[25]["attr1"] = """expr"""
		self.vs[25]["mm__"] = """directLink_T"""

		# apply association FunctionCall--function-->FunctionPrototype node 
		self.add_node()
		self.vs[26]["attr1"] = """function"""
		self.vs[26]["mm__"] = """directLink_T"""

		# backward association ImplementationModule-->ImplementationModulenode 
		self.add_node()
		self.vs[27]["mm__"] = """backward_link"""

		# backward association FunctionPrototype-->Functionnode 
		self.add_node()
		self.vs[28]["mm__"] = """backward_link"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class ImplementationModule(layer4rule3class0ImplementationModule)
			(0,4), # matchmodel -> match_class Function(layer4rule3class1Function)
			(0,5), # matchmodel -> match_class Int32Type(layer4rule3class2Int32Type)
			(1,6), # applymodel -> apply_classImplementationModule(layer4rule3class3ImplementationModule)
			(1,7), # applymodel -> apply_classFunction(layer4rule3class4Function)
			(1,8), # applymodel -> apply_classVoidType(layer4rule3class5VoidType)
			(1,9), # applymodel -> apply_classStatementList(layer4rule3class6StatementList)
			(1,10), # applymodel -> apply_classFunction(layer4rule3class7Function)
			(1,11), # applymodel -> apply_classStatementList(layer4rule3class8StatementList)
			(1,12), # applymodel -> apply_classInt32Type(layer4rule3class9Int32Type)
			(1,13), # applymodel -> apply_classExpressionStatement(layer4rule3class10ExpressionStatement)
			(1,14), # applymodel -> apply_classFunctionCall(layer4rule3class11FunctionCall)
			(1,15), # applymodel -> apply_classFunctionPrototype(layer4rule3class12FunctionPrototype)
			(3,16), # match classImplementationModule(layer4rule3class0ImplementationModule) -> association contents
			(16,4), # associationcontents -> match_classImplementationModule(layer4rule3class1Function)
			(4,17), # match classFunction(layer4rule3class1Function) -> association type
			(17,5), # associationtype -> match_classFunction(layer4rule3class2Int32Type)
			(6,18), # apply class ImplementationModule(layer4rule3class3ImplementationModule) -> association contents
			(18,7), # associationcontents -> apply_classFunction(layer4rule3class4Function)
			(7,19), # apply class Function(layer4rule3class4Function) -> association type
			(19,8), # associationtype -> apply_classVoidType(layer4rule3class5VoidType)
			(7,20), # apply class Function(layer4rule3class4Function) -> association body
			(20,9), # associationbody -> apply_classStatementList(layer4rule3class6StatementList)
			(6,21), # apply class ImplementationModule(layer4rule3class3ImplementationModule) -> association contents
			(21,10), # associationcontents -> apply_classFunction(layer4rule3class7Function)
			(10,22), # apply class Function(layer4rule3class7Function) -> association type
			(22,12), # associationtype -> apply_classInt32Type(layer4rule3class9Int32Type)
			(10,23), # apply class Function(layer4rule3class7Function) -> association body
			(23,11), # associationbody -> apply_classStatementList(layer4rule3class8StatementList)
			(11,24), # apply class StatementList(layer4rule3class8StatementList) -> association statements
			(24,13), # associationstatements -> apply_classExpressionStatement(layer4rule3class10ExpressionStatement)
			(13,25), # apply class ExpressionStatement(layer4rule3class10ExpressionStatement) -> association expr
			(25,14), # associationexpr -> apply_classFunctionCall(layer4rule3class11FunctionCall)
			(14,26), # apply class FunctionCall(layer4rule3class11FunctionCall) -> association function
			(26,15), # associationfunction -> apply_classFunctionPrototype(layer4rule3class12FunctionPrototype)
			(6,27), # apply class ImplementationModule(layer4rule3class0ImplementationModule) -> backward_association 
			(27,3), # backward_associationImplementationModule -> match_class ImplementationModule(layer4rule3class0ImplementationModule)
			(15,28), # apply class FunctionPrototype(layer4rule3class1Function) -> backward_association 
			(28,4), # backward_associationFunction -> match_class Function(layer4rule3class1Function)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = [((7,'name'),('concat',((3,'name'),('constant','_blockexpr_main_2')))),((10,'name'),('constant','main')),]
