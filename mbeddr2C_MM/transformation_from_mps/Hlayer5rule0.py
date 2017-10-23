from core.himesis import Himesis
import uuid

class Hlayer5rule0(Himesis):
	def __init__(self):
		"""
		Creates the himesis graph representing the DSLTrans rule layer5rule0.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(Hlayer5rule0, self).__init__(name='Hlayer5rule0', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """layer5rule0"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """layer5rule0"""

		# match class ComponentInstance(layer5rule0class0ComponentInstance) node
		self.add_node()
		self.vs[3]["mm__"] = """ComponentInstance"""
		self.vs[3]["attr1"] = """+"""

		# match class AtomicComponent(layer5rule0class1AtomicComponent) node
		self.add_node()
		self.vs[4]["mm__"] = """AtomicComponent"""
		self.vs[4]["attr1"] = """+"""

		# match class ProvidedPort(layer5rule0class2ProvidedPort) node
		self.add_node()
		self.vs[5]["mm__"] = """ProvidedPort"""
		self.vs[5]["attr1"] = """+"""

		# match class ClientServerInterface(layer5rule0class3ClientServerInterface) node
		self.add_node()
		self.vs[6]["mm__"] = """ClientServerInterface"""
		self.vs[6]["attr1"] = """+"""

		# match class Operation(layer5rule0class4Operation) node
		self.add_node()
		self.vs[7]["mm__"] = """Operation"""
		self.vs[7]["attr1"] = """+"""

		# apply class StatementList(layer5rule0class5StatementList) node
		self.add_node()
		self.vs[8]["mm__"] = """StatementList"""
		self.vs[8]["attr1"] = """1"""

		# apply class GlobalVariableDeclaration(layer5rule0class6GlobalVariableDeclaration) node
		self.add_node()
		self.vs[9]["mm__"] = """GlobalVariableDeclaration"""
		self.vs[9]["attr1"] = """1"""

		# apply class ExpressionStatement(layer5rule0class7ExpressionStatement) node
		self.add_node()
		self.vs[10]["mm__"] = """ExpressionStatement"""
		self.vs[10]["attr1"] = """1"""

		# apply class AssignmentExpr(layer5rule0class8AssignmentExpr) node
		self.add_node()
		self.vs[11]["mm__"] = """AssignmentExpr"""
		self.vs[11]["attr1"] = """1"""

		# apply class GenericDotExpression(layer5rule0class9GenericDotExpression) node
		self.add_node()
		self.vs[12]["mm__"] = """GenericDotExpression"""
		self.vs[12]["attr1"] = """1"""

		# apply class ReferenceExpr(layer5rule0class10ReferenceExpr) node
		self.add_node()
		self.vs[13]["mm__"] = """ReferenceExpr"""
		self.vs[13]["attr1"] = """1"""

		# apply class GlobalVarRef(layer5rule0class11GlobalVarRef) node
		self.add_node()
		self.vs[14]["mm__"] = """GlobalVarRef"""
		self.vs[14]["attr1"] = """1"""

		# apply class GenericMemberRef(layer5rule0class12GenericMemberRef) node
		self.add_node()
		self.vs[15]["mm__"] = """GenericMemberRef"""
		self.vs[15]["attr1"] = """1"""

		# apply class CFunctionPointerStructMember(layer5rule0class13CFunctionPointerStructMember) node
		self.add_node()
		self.vs[16]["mm__"] = """CFunctionPointerStructMember"""
		self.vs[16]["attr1"] = """1"""

		# apply class FunctionPrototype(layer5rule0class14FunctionPrototype) node
		self.add_node()
		self.vs[17]["mm__"] = """FunctionPrototype"""
		self.vs[17]["attr1"] = """1"""

		# apply class FunctionRefExpr(layer5rule0class15FunctionRefExpr) node
		self.add_node()
		self.vs[18]["mm__"] = """FunctionRefExpr"""
		self.vs[18]["attr1"] = """1"""

		# match association ComponentInstance--component-->AtomicComponent node 
		self.add_node()
		self.vs[19]["attr1"] = """component"""
		self.vs[19]["mm__"] = """directLink_S"""

		# match association AtomicComponent--contents-->ProvidedPort node 
		self.add_node()
		self.vs[20]["attr1"] = """contents"""
		self.vs[20]["mm__"] = """directLink_S"""

		# match association ProvidedPort--intf-->ClientServerInterface node 
		self.add_node()
		self.vs[21]["attr1"] = """intf"""
		self.vs[21]["mm__"] = """directLink_S"""

		# match association ClientServerInterface--contents-->Operation node 
		self.add_node()
		self.vs[22]["attr1"] = """contents"""
		self.vs[22]["mm__"] = """directLink_S"""

		# apply association StatementList--statements-->ExpressionStatement node 
		self.add_node()
		self.vs[23]["attr1"] = """statements"""
		self.vs[23]["mm__"] = """directLink_T"""

		# apply association ExpressionStatement--expr-->AssignmentExpr node 
		self.add_node()
		self.vs[24]["attr1"] = """expr"""
		self.vs[24]["mm__"] = """directLink_T"""

		# apply association AssignmentExpr--left-->GenericDotExpression node 
		self.add_node()
		self.vs[25]["attr1"] = """left"""
		self.vs[25]["mm__"] = """directLink_T"""

		# apply association AssignmentExpr--right-->ReferenceExpr node 
		self.add_node()
		self.vs[26]["attr1"] = """right"""
		self.vs[26]["mm__"] = """directLink_T"""

		# apply association GenericDotExpression--expression-->GlobalVarRef node 
		self.add_node()
		self.vs[27]["attr1"] = """expression"""
		self.vs[27]["mm__"] = """directLink_T"""

		# apply association GenericDotExpression--target-->GenericMemberRef node 
		self.add_node()
		self.vs[28]["attr1"] = """target"""
		self.vs[28]["mm__"] = """directLink_T"""

		# apply association GlobalVarRef--var-->GlobalVariableDeclaration node 
		self.add_node()
		self.vs[29]["attr1"] = """var"""
		self.vs[29]["mm__"] = """directLink_T"""

		# apply association GenericMemberRef--member-->CFunctionPointerStructMember node 
		self.add_node()
		self.vs[30]["attr1"] = """member"""
		self.vs[30]["mm__"] = """directLink_T"""

		# apply association ReferenceExpr--expression-->FunctionRefExpr node 
		self.add_node()
		self.vs[31]["attr1"] = """expression"""
		self.vs[31]["mm__"] = """directLink_T"""

		# apply association FunctionRefExpr--function-->FunctionPrototype node 
		self.add_node()
		self.vs[32]["attr1"] = """function"""
		self.vs[32]["mm__"] = """directLink_T"""

		# backward association StatementList-->ComponentInstancenode 
		self.add_node()
		self.vs[33]["mm__"] = """backward_link"""

		# backward association GlobalVariableDeclaration-->ProvidedPortnode 
		self.add_node()
		self.vs[34]["mm__"] = """backward_link"""

		# backward association CFunctionPointerStructMember-->Operationnode 
		self.add_node()
		self.vs[35]["mm__"] = """backward_link"""

		# backward association FunctionPrototype-->ProvidedPortnode 
		self.add_node()
		self.vs[36]["mm__"] = """backward_link"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class ComponentInstance(layer5rule0class0ComponentInstance)
			(0,4), # matchmodel -> match_class AtomicComponent(layer5rule0class1AtomicComponent)
			(0,5), # matchmodel -> match_class ProvidedPort(layer5rule0class2ProvidedPort)
			(0,6), # matchmodel -> match_class ClientServerInterface(layer5rule0class3ClientServerInterface)
			(0,7), # matchmodel -> match_class Operation(layer5rule0class4Operation)
			(1,8), # applymodel -> apply_classStatementList(layer5rule0class5StatementList)
			(1,9), # applymodel -> apply_classGlobalVariableDeclaration(layer5rule0class6GlobalVariableDeclaration)
			(1,10), # applymodel -> apply_classExpressionStatement(layer5rule0class7ExpressionStatement)
			(1,11), # applymodel -> apply_classAssignmentExpr(layer5rule0class8AssignmentExpr)
			(1,12), # applymodel -> apply_classGenericDotExpression(layer5rule0class9GenericDotExpression)
			(1,13), # applymodel -> apply_classReferenceExpr(layer5rule0class10ReferenceExpr)
			(1,14), # applymodel -> apply_classGlobalVarRef(layer5rule0class11GlobalVarRef)
			(1,15), # applymodel -> apply_classGenericMemberRef(layer5rule0class12GenericMemberRef)
			(1,16), # applymodel -> apply_classCFunctionPointerStructMember(layer5rule0class13CFunctionPointerStructMember)
			(1,17), # applymodel -> apply_classFunctionPrototype(layer5rule0class14FunctionPrototype)
			(1,18), # applymodel -> apply_classFunctionRefExpr(layer5rule0class15FunctionRefExpr)
			(3,19), # match classComponentInstance(layer5rule0class0ComponentInstance) -> association component
			(19,4), # associationcomponent -> match_classComponentInstance(layer5rule0class1AtomicComponent)
			(4,20), # match classAtomicComponent(layer5rule0class1AtomicComponent) -> association contents
			(20,5), # associationcontents -> match_classAtomicComponent(layer5rule0class2ProvidedPort)
			(5,21), # match classProvidedPort(layer5rule0class2ProvidedPort) -> association intf
			(21,6), # associationintf -> match_classProvidedPort(layer5rule0class3ClientServerInterface)
			(6,22), # match classClientServerInterface(layer5rule0class3ClientServerInterface) -> association contents
			(22,7), # associationcontents -> match_classClientServerInterface(layer5rule0class4Operation)
			(8,23), # apply class StatementList(layer5rule0class5StatementList) -> association statements
			(23,10), # associationstatements -> apply_classExpressionStatement(layer5rule0class7ExpressionStatement)
			(10,24), # apply class ExpressionStatement(layer5rule0class7ExpressionStatement) -> association expr
			(24,11), # associationexpr -> apply_classAssignmentExpr(layer5rule0class8AssignmentExpr)
			(11,25), # apply class AssignmentExpr(layer5rule0class8AssignmentExpr) -> association left
			(25,12), # associationleft -> apply_classGenericDotExpression(layer5rule0class9GenericDotExpression)
			(11,26), # apply class AssignmentExpr(layer5rule0class8AssignmentExpr) -> association right
			(26,13), # associationright -> apply_classReferenceExpr(layer5rule0class10ReferenceExpr)
			(12,27), # apply class GenericDotExpression(layer5rule0class9GenericDotExpression) -> association expression
			(27,14), # associationexpression -> apply_classGlobalVarRef(layer5rule0class11GlobalVarRef)
			(12,28), # apply class GenericDotExpression(layer5rule0class9GenericDotExpression) -> association target
			(28,15), # associationtarget -> apply_classGenericMemberRef(layer5rule0class12GenericMemberRef)
			(14,29), # apply class GlobalVarRef(layer5rule0class11GlobalVarRef) -> association var
			(29,9), # associationvar -> apply_classGlobalVariableDeclaration(layer5rule0class6GlobalVariableDeclaration)
			(15,30), # apply class GenericMemberRef(layer5rule0class12GenericMemberRef) -> association member
			(30,16), # associationmember -> apply_classCFunctionPointerStructMember(layer5rule0class13CFunctionPointerStructMember)
			(13,31), # apply class ReferenceExpr(layer5rule0class10ReferenceExpr) -> association expression
			(31,18), # associationexpression -> apply_classFunctionRefExpr(layer5rule0class15FunctionRefExpr)
			(18,32), # apply class FunctionRefExpr(layer5rule0class15FunctionRefExpr) -> association function
			(32,17), # associationfunction -> apply_classFunctionPrototype(layer5rule0class14FunctionPrototype)
			(8,33), # apply class StatementList(layer5rule0class0ComponentInstance) -> backward_association 
			(33,3), # backward_associationComponentInstance -> match_class ComponentInstance(layer5rule0class0ComponentInstance)
			(9,34), # apply class GlobalVariableDeclaration(layer5rule0class2ProvidedPort) -> backward_association 
			(34,5), # backward_associationProvidedPort -> match_class ProvidedPort(layer5rule0class2ProvidedPort)
			(16,35), # apply class CFunctionPointerStructMember(layer5rule0class4Operation) -> backward_association 
			(35,7), # backward_associationOperation -> match_class Operation(layer5rule0class4Operation)
			(17,36), # apply class FunctionPrototype(layer5rule0class2ProvidedPort) -> backward_association 
			(36,5), # backward_associationProvidedPort -> match_class ProvidedPort(layer5rule0class2ProvidedPort)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = []
