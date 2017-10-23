from core.himesis import Himesis
import uuid

class Hlayer5rule1(Himesis):
	def __init__(self):
		"""
		Creates the himesis graph representing the DSLTrans rule layer5rule1.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(Hlayer5rule1, self).__init__(name='Hlayer5rule1', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """layer5rule1"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """layer5rule1"""

		# match class ComponentInstance(layer5rule1class0ComponentInstance) node
		self.add_node()
		self.vs[3]["mm__"] = """ComponentInstance"""
		self.vs[3]["attr1"] = """+"""

		# match class AtomicComponent(layer5rule1class1AtomicComponent) node
		self.add_node()
		self.vs[4]["mm__"] = """AtomicComponent"""
		self.vs[4]["attr1"] = """+"""

		# match class RequiredPort(layer5rule1class2RequiredPort) node
		self.add_node()
		self.vs[5]["mm__"] = """RequiredPort"""
		self.vs[5]["attr1"] = """+"""

		# match class InstanceConfiguration(layer5rule1class3InstanceConfiguration) node
		self.add_node()
		self.vs[6]["mm__"] = """InstanceConfiguration"""
		self.vs[6]["attr1"] = """+"""

		# match class AssemblyConnector(layer5rule1class4AssemblyConnector) node
		self.add_node()
		self.vs[7]["mm__"] = """AssemblyConnector"""
		self.vs[7]["attr1"] = """+"""

		# match class InstancePortRef(layer5rule1class5InstancePortRef) node
		self.add_node()
		self.vs[8]["mm__"] = """InstancePortRef"""
		self.vs[8]["attr1"] = """+"""

		# match class InstancePortRef(layer5rule1class6InstancePortRef) node
		self.add_node()
		self.vs[9]["mm__"] = """InstancePortRef"""
		self.vs[9]["attr1"] = """+"""

		# match class ComponentInstance(layer5rule1class7ComponentInstance) node
		self.add_node()
		self.vs[10]["mm__"] = """ComponentInstance"""
		self.vs[10]["attr1"] = """+"""

		# match class AtomicComponent(layer5rule1class8AtomicComponent) node
		self.add_node()
		self.vs[11]["mm__"] = """AtomicComponent"""
		self.vs[11]["attr1"] = """+"""

		# match class ProvidedPort(layer5rule1class9ProvidedPort) node
		self.add_node()
		self.vs[12]["mm__"] = """ProvidedPort"""
		self.vs[12]["attr1"] = """+"""

		# match class ClientServerInterface(layer5rule1class10ClientServerInterface) node
		self.add_node()
		self.vs[13]["mm__"] = """ClientServerInterface"""
		self.vs[13]["attr1"] = """+"""

		# apply class StatementList(layer5rule1class11StatementList) node
		self.add_node()
		self.vs[14]["mm__"] = """StatementList"""
		self.vs[14]["attr1"] = """1"""

		# apply class GlobalVariableDeclaration(layer5rule1class12GlobalVariableDeclaration) node
		self.add_node()
		self.vs[15]["mm__"] = """GlobalVariableDeclaration"""
		self.vs[15]["attr1"] = """1"""

		# apply class ExpressionStatement(layer5rule1class13ExpressionStatement) node
		self.add_node()
		self.vs[16]["mm__"] = """ExpressionStatement"""
		self.vs[16]["attr1"] = """1"""

		# apply class AssignmentExpr(layer5rule1class14AssignmentExpr) node
		self.add_node()
		self.vs[17]["mm__"] = """AssignmentExpr"""
		self.vs[17]["attr1"] = """1"""

		# apply class GenericDotExpression(layer5rule1class15GenericDotExpression) node
		self.add_node()
		self.vs[18]["mm__"] = """GenericDotExpression"""
		self.vs[18]["attr1"] = """1"""

		# apply class ReferenceExpr(layer5rule1class16ReferenceExpr) node
		self.add_node()
		self.vs[19]["mm__"] = """ReferenceExpr"""
		self.vs[19]["attr1"] = """1"""

		# apply class GlobalVarRef(layer5rule1class17GlobalVarRef) node
		self.add_node()
		self.vs[20]["mm__"] = """GlobalVarRef"""
		self.vs[20]["attr1"] = """1"""

		# apply class GenericMemberRef(layer5rule1class18GenericMemberRef) node
		self.add_node()
		self.vs[21]["mm__"] = """GenericMemberRef"""
		self.vs[21]["attr1"] = """1"""

		# apply class Member(layer5rule1class19Member) node
		self.add_node()
		self.vs[22]["mm__"] = """Member"""
		self.vs[22]["attr1"] = """1"""

		# apply class GlobalVariableDeclaration(layer5rule1class20GlobalVariableDeclaration) node
		self.add_node()
		self.vs[23]["mm__"] = """GlobalVariableDeclaration"""
		self.vs[23]["attr1"] = """1"""

		# apply class GlobalVarRef(layer5rule1class21GlobalVarRef) node
		self.add_node()
		self.vs[24]["mm__"] = """GlobalVarRef"""
		self.vs[24]["attr1"] = """1"""

		# apply class ExpressionStatement(layer5rule1class22ExpressionStatement) node
		self.add_node()
		self.vs[25]["mm__"] = """ExpressionStatement"""
		self.vs[25]["attr1"] = """1"""

		# apply class AssignmentExpr(layer5rule1class23AssignmentExpr) node
		self.add_node()
		self.vs[26]["mm__"] = """AssignmentExpr"""
		self.vs[26]["attr1"] = """1"""

		# apply class GenericDotExpression(layer5rule1class24GenericDotExpression) node
		self.add_node()
		self.vs[27]["mm__"] = """GenericDotExpression"""
		self.vs[27]["attr1"] = """1"""

		# apply class GlobalVarRef(layer5rule1class25GlobalVarRef) node
		self.add_node()
		self.vs[28]["mm__"] = """GlobalVarRef"""
		self.vs[28]["attr1"] = """1"""

		# apply class GenericMemberRef(layer5rule1class26GenericMemberRef) node
		self.add_node()
		self.vs[29]["mm__"] = """GenericMemberRef"""
		self.vs[29]["attr1"] = """1"""

		# apply class Member(layer5rule1class27Member) node
		self.add_node()
		self.vs[30]["mm__"] = """Member"""
		self.vs[30]["attr1"] = """1"""

		# apply class ReferenceExpr(layer5rule1class28ReferenceExpr) node
		self.add_node()
		self.vs[31]["mm__"] = """ReferenceExpr"""
		self.vs[31]["attr1"] = """1"""

		# apply class GlobalVarRef(layer5rule1class29GlobalVarRef) node
		self.add_node()
		self.vs[32]["mm__"] = """GlobalVarRef"""
		self.vs[32]["attr1"] = """1"""

		# apply class GlobalVariableDeclaration(layer5rule1class30GlobalVariableDeclaration) node
		self.add_node()
		self.vs[33]["mm__"] = """GlobalVariableDeclaration"""
		self.vs[33]["attr1"] = """1"""

		# match association ComponentInstance--component-->AtomicComponent node 
		self.add_node()
		self.vs[34]["attr1"] = """component"""
		self.vs[34]["mm__"] = """directLink_S"""

		# match association AtomicComponent--contents-->RequiredPort node 
		self.add_node()
		self.vs[35]["attr1"] = """contents"""
		self.vs[35]["mm__"] = """directLink_S"""

		# match association InstanceConfiguration--contents-->ComponentInstance node 
		self.add_node()
		self.vs[36]["attr1"] = """contents"""
		self.vs[36]["mm__"] = """directLink_S"""

		# match association InstanceConfiguration--contents-->AssemblyConnector node 
		self.add_node()
		self.vs[37]["attr1"] = """contents"""
		self.vs[37]["mm__"] = """directLink_S"""

		# match association AssemblyConnector--source-->InstancePortRef node 
		self.add_node()
		self.vs[38]["attr1"] = """source"""
		self.vs[38]["mm__"] = """directLink_S"""

		# match association InstancePortRef--instance-->ComponentInstance node 
		self.add_node()
		self.vs[39]["attr1"] = """instance"""
		self.vs[39]["mm__"] = """directLink_S"""

		# match association InstancePortRef--port-->RequiredPort node 
		self.add_node()
		self.vs[40]["attr1"] = """port"""
		self.vs[40]["mm__"] = """directLink_S"""

		# match association InstanceConfiguration--contents-->ComponentInstance node 
		self.add_node()
		self.vs[41]["attr1"] = """contents"""
		self.vs[41]["mm__"] = """directLink_S"""

		# match association InstancePortRef--instance-->ComponentInstance node 
		self.add_node()
		self.vs[42]["attr1"] = """instance"""
		self.vs[42]["mm__"] = """directLink_S"""

		# match association AssemblyConnector--target-->InstancePortRef node 
		self.add_node()
		self.vs[43]["attr1"] = """target"""
		self.vs[43]["mm__"] = """directLink_S"""

		# match association ComponentInstance--component-->AtomicComponent node 
		self.add_node()
		self.vs[44]["attr1"] = """component"""
		self.vs[44]["mm__"] = """directLink_S"""

		# match association AtomicComponent--contents-->ProvidedPort node 
		self.add_node()
		self.vs[45]["attr1"] = """contents"""
		self.vs[45]["mm__"] = """directLink_S"""

		# match association ProvidedPort--intf-->ClientServerInterface node 
		self.add_node()
		self.vs[46]["attr1"] = """intf"""
		self.vs[46]["mm__"] = """directLink_S"""

		# match association RequiredPort--intf-->ClientServerInterface node 
		self.add_node()
		self.vs[47]["attr1"] = """intf"""
		self.vs[47]["mm__"] = """directLink_S"""

		# apply association StatementList--statements-->ExpressionStatement node 
		self.add_node()
		self.vs[48]["attr1"] = """statements"""
		self.vs[48]["mm__"] = """directLink_T"""

		# apply association ExpressionStatement--expr-->AssignmentExpr node 
		self.add_node()
		self.vs[49]["attr1"] = """expr"""
		self.vs[49]["mm__"] = """directLink_T"""

		# apply association AssignmentExpr--left-->GenericDotExpression node 
		self.add_node()
		self.vs[50]["attr1"] = """left"""
		self.vs[50]["mm__"] = """directLink_T"""

		# apply association AssignmentExpr--right-->ReferenceExpr node 
		self.add_node()
		self.vs[51]["attr1"] = """right"""
		self.vs[51]["mm__"] = """directLink_T"""

		# apply association GenericDotExpression--expression-->GlobalVarRef node 
		self.add_node()
		self.vs[52]["attr1"] = """expression"""
		self.vs[52]["mm__"] = """directLink_T"""

		# apply association GenericDotExpression--target-->GenericMemberRef node 
		self.add_node()
		self.vs[53]["attr1"] = """target"""
		self.vs[53]["mm__"] = """directLink_T"""

		# apply association GlobalVarRef--var-->GlobalVariableDeclaration node 
		self.add_node()
		self.vs[54]["attr1"] = """var"""
		self.vs[54]["mm__"] = """directLink_T"""

		# apply association GenericMemberRef--member-->Member node 
		self.add_node()
		self.vs[55]["attr1"] = """member"""
		self.vs[55]["mm__"] = """directLink_T"""

		# apply association ReferenceExpr--expression-->GlobalVarRef node 
		self.add_node()
		self.vs[56]["attr1"] = """expression"""
		self.vs[56]["mm__"] = """directLink_T"""

		# apply association GlobalVarRef--var-->GlobalVariableDeclaration node 
		self.add_node()
		self.vs[57]["attr1"] = """var"""
		self.vs[57]["mm__"] = """directLink_T"""

		# apply association StatementList--statements-->ExpressionStatement node 
		self.add_node()
		self.vs[58]["attr1"] = """statements"""
		self.vs[58]["mm__"] = """directLink_T"""

		# apply association ExpressionStatement--expr-->AssignmentExpr node 
		self.add_node()
		self.vs[59]["attr1"] = """expr"""
		self.vs[59]["mm__"] = """directLink_T"""

		# apply association AssignmentExpr--left-->GenericDotExpression node 
		self.add_node()
		self.vs[60]["attr1"] = """left"""
		self.vs[60]["mm__"] = """directLink_T"""

		# apply association GenericDotExpression--expression-->GlobalVarRef node 
		self.add_node()
		self.vs[61]["attr1"] = """expression"""
		self.vs[61]["mm__"] = """directLink_T"""

		# apply association GlobalVarRef--var-->GlobalVariableDeclaration node 
		self.add_node()
		self.vs[62]["attr1"] = """var"""
		self.vs[62]["mm__"] = """directLink_T"""

		# apply association GenericDotExpression--target-->GenericMemberRef node 
		self.add_node()
		self.vs[63]["attr1"] = """target"""
		self.vs[63]["mm__"] = """directLink_T"""

		# apply association GenericMemberRef--member-->Member node 
		self.add_node()
		self.vs[64]["attr1"] = """member"""
		self.vs[64]["mm__"] = """directLink_T"""

		# apply association AssignmentExpr--right-->ReferenceExpr node 
		self.add_node()
		self.vs[65]["attr1"] = """right"""
		self.vs[65]["mm__"] = """directLink_T"""

		# apply association ReferenceExpr--expression-->GlobalVarRef node 
		self.add_node()
		self.vs[66]["attr1"] = """expression"""
		self.vs[66]["mm__"] = """directLink_T"""

		# apply association GlobalVarRef--var-->GlobalVariableDeclaration node 
		self.add_node()
		self.vs[67]["attr1"] = """var"""
		self.vs[67]["mm__"] = """directLink_T"""

		# backward association StatementList-->ComponentInstancenode 
		self.add_node()
		self.vs[68]["mm__"] = """backward_link"""

		# backward association GlobalVariableDeclaration-->ComponentInstancenode 
		self.add_node()
		self.vs[69]["mm__"] = """backward_link"""

		# backward association Member-->RequiredPortnode 
		self.add_node()
		self.vs[70]["mm__"] = """backward_link"""

		# backward association GlobalVariableDeclaration-->ComponentInstancenode 
		self.add_node()
		self.vs[71]["mm__"] = """backward_link"""

		# backward association Member-->RequiredPortnode 
		self.add_node()
		self.vs[72]["mm__"] = """backward_link"""

		# backward association GlobalVariableDeclaration-->ProvidedPortnode 
		self.add_node()
		self.vs[73]["mm__"] = """backward_link"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class ComponentInstance(layer5rule1class0ComponentInstance)
			(0,4), # matchmodel -> match_class AtomicComponent(layer5rule1class1AtomicComponent)
			(0,5), # matchmodel -> match_class RequiredPort(layer5rule1class2RequiredPort)
			(0,6), # matchmodel -> match_class InstanceConfiguration(layer5rule1class3InstanceConfiguration)
			(0,7), # matchmodel -> match_class AssemblyConnector(layer5rule1class4AssemblyConnector)
			(0,8), # matchmodel -> match_class InstancePortRef(layer5rule1class5InstancePortRef)
			(0,9), # matchmodel -> match_class InstancePortRef(layer5rule1class6InstancePortRef)
			(0,10), # matchmodel -> match_class ComponentInstance(layer5rule1class7ComponentInstance)
			(0,11), # matchmodel -> match_class AtomicComponent(layer5rule1class8AtomicComponent)
			(0,12), # matchmodel -> match_class ProvidedPort(layer5rule1class9ProvidedPort)
			(0,13), # matchmodel -> match_class ClientServerInterface(layer5rule1class10ClientServerInterface)
			(1,14), # applymodel -> apply_classStatementList(layer5rule1class11StatementList)
			(1,15), # applymodel -> apply_classGlobalVariableDeclaration(layer5rule1class12GlobalVariableDeclaration)
			(1,16), # applymodel -> apply_classExpressionStatement(layer5rule1class13ExpressionStatement)
			(1,17), # applymodel -> apply_classAssignmentExpr(layer5rule1class14AssignmentExpr)
			(1,18), # applymodel -> apply_classGenericDotExpression(layer5rule1class15GenericDotExpression)
			(1,19), # applymodel -> apply_classReferenceExpr(layer5rule1class16ReferenceExpr)
			(1,20), # applymodel -> apply_classGlobalVarRef(layer5rule1class17GlobalVarRef)
			(1,21), # applymodel -> apply_classGenericMemberRef(layer5rule1class18GenericMemberRef)
			(1,22), # applymodel -> apply_classMember(layer5rule1class19Member)
			(1,23), # applymodel -> apply_classGlobalVariableDeclaration(layer5rule1class20GlobalVariableDeclaration)
			(1,24), # applymodel -> apply_classGlobalVarRef(layer5rule1class21GlobalVarRef)
			(1,25), # applymodel -> apply_classExpressionStatement(layer5rule1class22ExpressionStatement)
			(1,26), # applymodel -> apply_classAssignmentExpr(layer5rule1class23AssignmentExpr)
			(1,27), # applymodel -> apply_classGenericDotExpression(layer5rule1class24GenericDotExpression)
			(1,28), # applymodel -> apply_classGlobalVarRef(layer5rule1class25GlobalVarRef)
			(1,29), # applymodel -> apply_classGenericMemberRef(layer5rule1class26GenericMemberRef)
			(1,30), # applymodel -> apply_classMember(layer5rule1class27Member)
			(1,31), # applymodel -> apply_classReferenceExpr(layer5rule1class28ReferenceExpr)
			(1,32), # applymodel -> apply_classGlobalVarRef(layer5rule1class29GlobalVarRef)
			(1,33), # applymodel -> apply_classGlobalVariableDeclaration(layer5rule1class30GlobalVariableDeclaration)
			(3,34), # match classComponentInstance(layer5rule1class0ComponentInstance) -> association component
			(34,4), # associationcomponent -> match_classComponentInstance(layer5rule1class1AtomicComponent)
			(4,35), # match classAtomicComponent(layer5rule1class1AtomicComponent) -> association contents
			(35,5), # associationcontents -> match_classAtomicComponent(layer5rule1class2RequiredPort)
			(6,36), # match classInstanceConfiguration(layer5rule1class3InstanceConfiguration) -> association contents
			(36,3), # associationcontents -> match_classInstanceConfiguration(layer5rule1class0ComponentInstance)
			(6,37), # match classInstanceConfiguration(layer5rule1class3InstanceConfiguration) -> association contents
			(37,7), # associationcontents -> match_classInstanceConfiguration(layer5rule1class4AssemblyConnector)
			(7,38), # match classAssemblyConnector(layer5rule1class4AssemblyConnector) -> association source
			(38,8), # associationsource -> match_classAssemblyConnector(layer5rule1class5InstancePortRef)
			(8,39), # match classInstancePortRef(layer5rule1class5InstancePortRef) -> association instance
			(39,3), # associationinstance -> match_classInstancePortRef(layer5rule1class0ComponentInstance)
			(8,40), # match classInstancePortRef(layer5rule1class5InstancePortRef) -> association port
			(40,5), # associationport -> match_classInstancePortRef(layer5rule1class2RequiredPort)
			(6,41), # match classInstanceConfiguration(layer5rule1class3InstanceConfiguration) -> association contents
			(41,10), # associationcontents -> match_classInstanceConfiguration(layer5rule1class7ComponentInstance)
			(9,42), # match classInstancePortRef(layer5rule1class6InstancePortRef) -> association instance
			(42,10), # associationinstance -> match_classInstancePortRef(layer5rule1class7ComponentInstance)
			(7,43), # match classAssemblyConnector(layer5rule1class4AssemblyConnector) -> association target
			(43,9), # associationtarget -> match_classAssemblyConnector(layer5rule1class6InstancePortRef)
			(10,44), # match classComponentInstance(layer5rule1class7ComponentInstance) -> association component
			(44,11), # associationcomponent -> match_classComponentInstance(layer5rule1class8AtomicComponent)
			(11,45), # match classAtomicComponent(layer5rule1class8AtomicComponent) -> association contents
			(45,12), # associationcontents -> match_classAtomicComponent(layer5rule1class9ProvidedPort)
			(12,46), # match classProvidedPort(layer5rule1class9ProvidedPort) -> association intf
			(46,13), # associationintf -> match_classProvidedPort(layer5rule1class10ClientServerInterface)
			(5,47), # match classRequiredPort(layer5rule1class2RequiredPort) -> association intf
			(47,13), # associationintf -> match_classRequiredPort(layer5rule1class10ClientServerInterface)
			(14,48), # apply class StatementList(layer5rule1class11StatementList) -> association statements
			(48,16), # associationstatements -> apply_classExpressionStatement(layer5rule1class13ExpressionStatement)
			(16,49), # apply class ExpressionStatement(layer5rule1class13ExpressionStatement) -> association expr
			(49,17), # associationexpr -> apply_classAssignmentExpr(layer5rule1class14AssignmentExpr)
			(17,50), # apply class AssignmentExpr(layer5rule1class14AssignmentExpr) -> association left
			(50,18), # associationleft -> apply_classGenericDotExpression(layer5rule1class15GenericDotExpression)
			(17,51), # apply class AssignmentExpr(layer5rule1class14AssignmentExpr) -> association right
			(51,19), # associationright -> apply_classReferenceExpr(layer5rule1class16ReferenceExpr)
			(18,52), # apply class GenericDotExpression(layer5rule1class15GenericDotExpression) -> association expression
			(52,20), # associationexpression -> apply_classGlobalVarRef(layer5rule1class17GlobalVarRef)
			(18,53), # apply class GenericDotExpression(layer5rule1class15GenericDotExpression) -> association target
			(53,21), # associationtarget -> apply_classGenericMemberRef(layer5rule1class18GenericMemberRef)
			(20,54), # apply class GlobalVarRef(layer5rule1class17GlobalVarRef) -> association var
			(54,15), # associationvar -> apply_classGlobalVariableDeclaration(layer5rule1class12GlobalVariableDeclaration)
			(21,55), # apply class GenericMemberRef(layer5rule1class18GenericMemberRef) -> association member
			(55,22), # associationmember -> apply_classMember(layer5rule1class19Member)
			(19,56), # apply class ReferenceExpr(layer5rule1class16ReferenceExpr) -> association expression
			(56,24), # associationexpression -> apply_classGlobalVarRef(layer5rule1class21GlobalVarRef)
			(24,57), # apply class GlobalVarRef(layer5rule1class21GlobalVarRef) -> association var
			(57,23), # associationvar -> apply_classGlobalVariableDeclaration(layer5rule1class20GlobalVariableDeclaration)
			(14,58), # apply class StatementList(layer5rule1class11StatementList) -> association statements
			(58,25), # associationstatements -> apply_classExpressionStatement(layer5rule1class22ExpressionStatement)
			(25,59), # apply class ExpressionStatement(layer5rule1class22ExpressionStatement) -> association expr
			(59,26), # associationexpr -> apply_classAssignmentExpr(layer5rule1class23AssignmentExpr)
			(26,60), # apply class AssignmentExpr(layer5rule1class23AssignmentExpr) -> association left
			(60,27), # associationleft -> apply_classGenericDotExpression(layer5rule1class24GenericDotExpression)
			(27,61), # apply class GenericDotExpression(layer5rule1class24GenericDotExpression) -> association expression
			(61,28), # associationexpression -> apply_classGlobalVarRef(layer5rule1class25GlobalVarRef)
			(28,62), # apply class GlobalVarRef(layer5rule1class25GlobalVarRef) -> association var
			(62,15), # associationvar -> apply_classGlobalVariableDeclaration(layer5rule1class12GlobalVariableDeclaration)
			(27,63), # apply class GenericDotExpression(layer5rule1class24GenericDotExpression) -> association target
			(63,29), # associationtarget -> apply_classGenericMemberRef(layer5rule1class26GenericMemberRef)
			(29,64), # apply class GenericMemberRef(layer5rule1class26GenericMemberRef) -> association member
			(64,30), # associationmember -> apply_classMember(layer5rule1class27Member)
			(26,65), # apply class AssignmentExpr(layer5rule1class23AssignmentExpr) -> association right
			(65,31), # associationright -> apply_classReferenceExpr(layer5rule1class28ReferenceExpr)
			(31,66), # apply class ReferenceExpr(layer5rule1class28ReferenceExpr) -> association expression
			(66,32), # associationexpression -> apply_classGlobalVarRef(layer5rule1class29GlobalVarRef)
			(32,67), # apply class GlobalVarRef(layer5rule1class29GlobalVarRef) -> association var
			(67,33), # associationvar -> apply_classGlobalVariableDeclaration(layer5rule1class30GlobalVariableDeclaration)
			(14,68), # apply class StatementList(layer5rule1class0ComponentInstance) -> backward_association 
			(68,3), # backward_associationComponentInstance -> match_class ComponentInstance(layer5rule1class0ComponentInstance)
			(15,69), # apply class GlobalVariableDeclaration(layer5rule1class0ComponentInstance) -> backward_association 
			(69,3), # backward_associationComponentInstance -> match_class ComponentInstance(layer5rule1class0ComponentInstance)
			(22,70), # apply class Member(layer5rule1class2RequiredPort) -> backward_association 
			(70,5), # backward_associationRequiredPort -> match_class RequiredPort(layer5rule1class2RequiredPort)
			(23,71), # apply class GlobalVariableDeclaration(layer5rule1class7ComponentInstance) -> backward_association 
			(71,10), # backward_associationComponentInstance -> match_class ComponentInstance(layer5rule1class7ComponentInstance)
			(30,72), # apply class Member(layer5rule1class2RequiredPort) -> backward_association 
			(72,5), # backward_associationRequiredPort -> match_class RequiredPort(layer5rule1class2RequiredPort)
			(33,73), # apply class GlobalVariableDeclaration(layer5rule1class9ProvidedPort) -> backward_association 
			(73,12), # backward_associationProvidedPort -> match_class ProvidedPort(layer5rule1class9ProvidedPort)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = []
