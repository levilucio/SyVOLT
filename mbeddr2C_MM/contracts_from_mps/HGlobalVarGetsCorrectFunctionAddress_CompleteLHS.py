from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HGlobalVarGetsCorrectFunctionAddress_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HGlobalVarGetsCorrectFunctionAddress_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HGlobalVarGetsCorrectFunctionAddress_CompleteLHS, self).__init__(name='HGlobalVarGetsCorrectFunctionAddress_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HGlobalVarGetsCorrectFunctionAddress_CompleteLHS')
		self["equations"] = []
		# Set the node attributes

		# match class ComponentInstance(0.2.m.0ComponentInstance) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__ComponentInstance"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.m.0ComponentInstance')

		# match class Operation(0.2.m.1Operation) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__Operation"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.m.1Operation')

		# match class OperationTrigger(0.2.m.2OperationTrigger) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__OperationTrigger"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.m.2OperationTrigger')

		# match class Executable(0.2.m.3Executable) node
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return True"""
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__Executable"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.m.3Executable')

		# match class ProvidedPort(0.2.m.4ProvidedPort) node
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return True"""
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__ProvidedPort"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.m.4ProvidedPort')

		# match class InstanceConfiguration(0.2.m.5InstanceConfiguration) node
		self.add_node()
		self.vs[5]["MT_pre__attr1"] = """return True"""
		self.vs[5]["MT_label__"] = """6"""
		self.vs[5]["mm__"] = """MT_pre__InstanceConfiguration"""
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.m.5InstanceConfiguration')

		# match class ClientServerInterface(0.2.m.6ClientServerInterface) node
		self.add_node()
		self.vs[6]["MT_pre__attr1"] = """return True"""
		self.vs[6]["MT_label__"] = """7"""
		self.vs[6]["mm__"] = """MT_pre__ClientServerInterface"""
		self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.m.6ClientServerInterface')

		# match class AtomicComponent(0.2.m.7AtomicComponent) node
		self.add_node()
		self.vs[7]["MT_pre__attr1"] = """return True"""
		self.vs[7]["MT_label__"] = """8"""
		self.vs[7]["mm__"] = """MT_pre__AtomicComponent"""
		self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.m.7AtomicComponent')

		# apply class StatementList(0.2.a.0StatementList) node
		self.add_node()
		self.vs[8]["MT_pre__attr1"] = """return True"""
		self.vs[8]["MT_label__"] = """9"""
		self.vs[8]["mm__"] = """MT_pre__StatementList"""
		self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.a.0StatementList')

		# apply class FunctionCall(0.2.a.1FunctionCall) node
		self.add_node()
		self.vs[9]["MT_pre__attr1"] = """return True"""
		self.vs[9]["MT_label__"] = """10"""
		self.vs[9]["mm__"] = """MT_pre__FunctionCall"""
		self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.a.1FunctionCall')

		# apply class GenericMemberRef(0.2.a.2GenericMemberRef) node
		self.add_node()
		self.vs[10]["MT_pre__attr1"] = """return True"""
		self.vs[10]["MT_label__"] = """11"""
		self.vs[10]["mm__"] = """MT_pre__GenericMemberRef"""
		self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.a.2GenericMemberRef')

		# apply class AssignmentExpr(0.2.a.3AssignmentExpr) node
		self.add_node()
		self.vs[11]["MT_pre__attr1"] = """return True"""
		self.vs[11]["MT_label__"] = """12"""
		self.vs[11]["mm__"] = """MT_pre__AssignmentExpr"""
		self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.a.3AssignmentExpr')

		# apply class ExpressionStatement(0.2.a.4ExpressionStatement) node
		self.add_node()
		self.vs[12]["MT_pre__attr1"] = """return True"""
		self.vs[12]["MT_label__"] = """13"""
		self.vs[12]["mm__"] = """MT_pre__ExpressionStatement"""
		self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.a.4ExpressionStatement')

		# apply class StatementList(0.2.a.5StatementList) node
		self.add_node()
		self.vs[13]["MT_pre__attr1"] = """return True"""
		self.vs[13]["MT_label__"] = """14"""
		self.vs[13]["mm__"] = """MT_pre__StatementList"""
		self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.a.5StatementList')

		# apply class FunctionPrototype(0.2.a.6FunctionPrototype) node
		self.add_node()
		self.vs[14]["MT_pre__attr1"] = """return True"""
		self.vs[14]["MT_label__"] = """15"""
		self.vs[14]["mm__"] = """MT_pre__FunctionPrototype"""
		self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.a.6FunctionPrototype')

		# apply class ExpressionStatement(0.2.a.7ExpressionStatement) node
		self.add_node()
		self.vs[15]["MT_pre__attr1"] = """return True"""
		self.vs[15]["MT_label__"] = """16"""
		self.vs[15]["mm__"] = """MT_pre__ExpressionStatement"""
		self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.a.7ExpressionStatement')

		# apply class Function(0.2.a.8Function) node
		self.add_node()
		self.vs[16]["MT_pre__attr1"] = """return True"""
		self.vs[16]["MT_label__"] = """17"""
		self.vs[16]["mm__"] = """MT_pre__Function"""
		self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.a.8Function')

		# apply class FunctionRefExpr(0.2.a.9FunctionRefExpr) node
		self.add_node()
		self.vs[17]["MT_pre__attr1"] = """return True"""
		self.vs[17]["MT_label__"] = """18"""
		self.vs[17]["mm__"] = """MT_pre__FunctionRefExpr"""
		self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.a.9FunctionRefExpr')

		# apply class GlobalVarRef(0.2.a.10GlobalVarRef) node
		self.add_node()
		self.vs[18]["MT_pre__attr1"] = """return True"""
		self.vs[18]["MT_label__"] = """19"""
		self.vs[18]["mm__"] = """MT_pre__GlobalVarRef"""
		self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.a.10GlobalVarRef')

		# apply class ReferenceExpr(0.2.a.11ReferenceExpression) node
		self.add_node()
		self.vs[19]["MT_pre__attr1"] = """return True"""
		self.vs[19]["MT_label__"] = """20"""
		self.vs[19]["mm__"] = """MT_pre__ReferenceExpr"""
		self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.a.11ReferenceExpression')

		# apply class GenericDotExpression(0.2.a.12GenericDotExpression) node
		self.add_node()
		self.vs[20]["MT_pre__attr1"] = """return True"""
		self.vs[20]["MT_label__"] = """21"""
		self.vs[20]["mm__"] = """MT_pre__GenericDotExpression"""
		self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.a.12GenericDotExpression')

		# apply class Function(0.2.a.13Function) node
		self.add_node()
		self.vs[21]["MT_pre__attr1"] = """return True"""
		self.vs[21]["MT_label__"] = """22"""
		self.vs[21]["mm__"] = """MT_pre__Function"""
		self.vs[21]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.a.13Function')

		# apply class FunctionPrototype(0.2.a.14FunctionPrototype) node
		self.add_node()
		self.vs[22]["MT_pre__attr1"] = """return True"""
		self.vs[22]["MT_label__"] = """23"""
		self.vs[22]["mm__"] = """MT_pre__FunctionPrototype"""
		self.vs[22]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.a.14FunctionPrototype')

		# apply class GlobalVariableDeclaration(0.2.a.15GlobalVariableDeclaration) node
		self.add_node()
		self.vs[23]["MT_pre__attr1"] = """return True"""
		self.vs[23]["MT_label__"] = """24"""
		self.vs[23]["mm__"] = """MT_pre__GlobalVariableDeclaration"""
		self.vs[23]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.a.15GlobalVariableDeclaration')

		# apply class StructDeclaration(0.2.a.16StructDeclaration) node
		self.add_node()
		self.vs[24]["MT_pre__attr1"] = """return True"""
		self.vs[24]["MT_label__"] = """25"""
		self.vs[24]["mm__"] = """MT_pre__StructDeclaration"""
		self.vs[24]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.a.16StructDeclaration')

		# apply class CFunctionPointerStructMember(0.2.a.17CFunctionPointerStructMember) node
		self.add_node()
		self.vs[25]["MT_pre__attr1"] = """return True"""
		self.vs[25]["MT_label__"] = """26"""
		self.vs[25]["mm__"] = """MT_pre__CFunctionPointerStructMember"""
		self.vs[25]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.a.17CFunctionPointerStructMember')

		# match association InstanceConfiguration--contents-->ComponentInstancenode
		self.add_node()
		self.vs[26]["MT_pre__attr1"] = """return attr_value == "contents" """
		self.vs[26]["MT_label__"] = """27"""
		self.vs[26]["mm__"] = """MT_pre__directLink_S"""
		self.vs[26]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.m.5InstanceConfigurationassoc260.2.m.0ComponentInstance')

		# match association AtomicComponent--contents-->ProvidedPortnode
		self.add_node()
		self.vs[27]["MT_pre__attr1"] = """return attr_value == "contents" """
		self.vs[27]["MT_label__"] = """28"""
		self.vs[27]["mm__"] = """MT_pre__directLink_S"""
		self.vs[27]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.m.7AtomicComponentassoc270.2.m.4ProvidedPort')

		# match association ComponentInstance--component-->AtomicComponentnode
		self.add_node()
		self.vs[28]["MT_pre__attr1"] = """return attr_value == "component" """
		self.vs[28]["MT_label__"] = """29"""
		self.vs[28]["mm__"] = """MT_pre__directLink_S"""
		self.vs[28]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.m.0ComponentInstanceassoc280.2.m.7AtomicComponent')

		# match association AtomicComponent--contents-->Executablenode
		self.add_node()
		self.vs[29]["MT_pre__attr1"] = """return attr_value == "contents" """
		self.vs[29]["MT_label__"] = """30"""
		self.vs[29]["mm__"] = """MT_pre__directLink_S"""
		self.vs[29]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.m.7AtomicComponentassoc290.2.m.3Executable')

		# match association Executable--trigger-->OperationTriggernode
		self.add_node()
		self.vs[30]["MT_pre__attr1"] = """return attr_value == "trigger" """
		self.vs[30]["MT_label__"] = """31"""
		self.vs[30]["mm__"] = """MT_pre__directLink_S"""
		self.vs[30]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.m.3Executableassoc300.2.m.2OperationTrigger')

		# match association OperationTrigger--calledOperation-->Operationnode
		self.add_node()
		self.vs[31]["MT_pre__attr1"] = """return attr_value == "calledOperation" """
		self.vs[31]["MT_label__"] = """32"""
		self.vs[31]["mm__"] = """MT_pre__directLink_S"""
		self.vs[31]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.m.2OperationTriggerassoc310.2.m.1Operation')

		# match association ProvidedPort--intf-->ClientServerInterfacenode
		self.add_node()
		self.vs[32]["MT_pre__attr1"] = """return attr_value == "intf" """
		self.vs[32]["MT_label__"] = """33"""
		self.vs[32]["mm__"] = """MT_pre__directLink_S"""
		self.vs[32]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.m.4ProvidedPortassoc320.2.m.6ClientServerInterface')

		# match association ClientServerInterface--contents-->Operationnode
		self.add_node()
		self.vs[33]["MT_pre__attr1"] = """return attr_value == "contents" """
		self.vs[33]["MT_label__"] = """34"""
		self.vs[33]["mm__"] = """MT_pre__directLink_S"""
		self.vs[33]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.m.6ClientServerInterfaceassoc330.2.m.1Operation')

		# match association OperationTrigger--providedPort-->ProvidedPortnode
		self.add_node()
		self.vs[34]["MT_pre__attr1"] = """return attr_value == "providedPort" """
		self.vs[34]["MT_label__"] = """35"""
		self.vs[34]["mm__"] = """MT_pre__directLink_S"""
		self.vs[34]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.m.2OperationTriggerassoc340.2.m.4ProvidedPort')

		# apply association FunctionCall--function-->FunctionPrototypenode
		self.add_node()
		self.vs[35]["MT_pre__attr1"] = """return attr_value == "function" """
		self.vs[35]["MT_label__"] = """36"""
		self.vs[35]["mm__"] = """MT_pre__directLink_T"""
		self.vs[35]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.a.1FunctionCallassoc350.2.a.6FunctionPrototype')

		# apply association Function--body-->StatementListnode
		self.add_node()
		self.vs[36]["MT_pre__attr1"] = """return attr_value == "body" """
		self.vs[36]["MT_label__"] = """37"""
		self.vs[36]["mm__"] = """MT_pre__directLink_T"""
		self.vs[36]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.a.8Functionassoc360.2.a.5StatementList')

		# apply association StatementList--statements-->ExpressionStatementnode
		self.add_node()
		self.vs[37]["MT_pre__attr1"] = """return attr_value == "statements" """
		self.vs[37]["MT_label__"] = """38"""
		self.vs[37]["mm__"] = """MT_pre__directLink_T"""
		self.vs[37]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.a.5StatementListassoc370.2.a.7ExpressionStatement')

		# apply association ExpressionStatement--expr-->FunctionCallnode
		self.add_node()
		self.vs[38]["MT_pre__attr1"] = """return attr_value == "expr" """
		self.vs[38]["MT_label__"] = """39"""
		self.vs[38]["mm__"] = """MT_pre__directLink_T"""
		self.vs[38]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.a.7ExpressionStatementassoc380.2.a.1FunctionCall')

		# apply association Function--body-->StatementListnode
		self.add_node()
		self.vs[39]["MT_pre__attr1"] = """return attr_value == "body" """
		self.vs[39]["MT_label__"] = """40"""
		self.vs[39]["mm__"] = """MT_pre__directLink_T"""
		self.vs[39]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.a.13Functionassoc390.2.a.0StatementList')

		# apply association StatementList--statements-->ExpressionStatementnode
		self.add_node()
		self.vs[40]["MT_pre__attr1"] = """return attr_value == "statements" """
		self.vs[40]["MT_label__"] = """41"""
		self.vs[40]["mm__"] = """MT_pre__directLink_T"""
		self.vs[40]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.a.0StatementListassoc400.2.a.4ExpressionStatement')

		# apply association ExpressionStatement--expr-->AssignmentExprnode
		self.add_node()
		self.vs[41]["MT_pre__attr1"] = """return attr_value == "expr" """
		self.vs[41]["MT_label__"] = """42"""
		self.vs[41]["mm__"] = """MT_pre__directLink_T"""
		self.vs[41]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.a.4ExpressionStatementassoc410.2.a.3AssignmentExpr')

		# apply association AssignmentExpr--left-->GenericDotExpressionnode
		self.add_node()
		self.vs[42]["MT_pre__attr1"] = """return attr_value == "left" """
		self.vs[42]["MT_label__"] = """43"""
		self.vs[42]["mm__"] = """MT_pre__directLink_T"""
		self.vs[42]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.a.3AssignmentExprassoc420.2.a.12GenericDotExpression')

		# apply association AssignmentExpr--right-->ReferenceExpressionnode
		self.add_node()
		self.vs[43]["MT_pre__attr1"] = """return attr_value == "right" """
		self.vs[43]["MT_label__"] = """44"""
		self.vs[43]["mm__"] = """MT_pre__directLink_T"""
		self.vs[43]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.a.3AssignmentExprassoc430.2.a.11ReferenceExpression')

		# apply association GenericDotExpression--expression-->GlobalVarRefnode
		self.add_node()
		self.vs[44]["MT_pre__attr1"] = """return attr_value == "expression" """
		self.vs[44]["MT_label__"] = """45"""
		self.vs[44]["mm__"] = """MT_pre__directLink_T"""
		self.vs[44]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.a.12GenericDotExpressionassoc440.2.a.10GlobalVarRef')

		# apply association GenericDotExpression--target-->GenericMemberRefnode
		self.add_node()
		self.vs[45]["MT_pre__attr1"] = """return attr_value == "target" """
		self.vs[45]["MT_label__"] = """46"""
		self.vs[45]["mm__"] = """MT_pre__directLink_T"""
		self.vs[45]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.a.12GenericDotExpressionassoc450.2.a.2GenericMemberRef')

		# apply association ReferenceExpression--expression-->FunctionRefExprnode
		self.add_node()
		self.vs[46]["MT_pre__attr1"] = """return attr_value == "expression" """
		self.vs[46]["MT_label__"] = """47"""
		self.vs[46]["mm__"] = """MT_pre__directLink_T"""
		self.vs[46]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.a.11ReferenceExpressionassoc460.2.a.9FunctionRefExpr')

		# apply association FunctionRefExpr--function-->FunctionPrototypenode
		self.add_node()
		self.vs[47]["MT_pre__attr1"] = """return attr_value == "function" """
		self.vs[47]["MT_label__"] = """48"""
		self.vs[47]["mm__"] = """MT_pre__directLink_T"""
		self.vs[47]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.a.9FunctionRefExprassoc470.2.a.14FunctionPrototype')

		# apply association StructDeclaration--members-->CFunctionPointerStructMembernode
		self.add_node()
		self.vs[48]["MT_pre__attr1"] = """return attr_value == "members" """
		self.vs[48]["MT_label__"] = """49"""
		self.vs[48]["mm__"] = """MT_pre__directLink_T"""
		self.vs[48]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.a.16StructDeclarationassoc480.2.a.17CFunctionPointerStructMember')

		# apply association GenericMemberRef--member-->CFunctionPointerStructMembernode
		self.add_node()
		self.vs[49]["MT_pre__attr1"] = """return attr_value == "member" """
		self.vs[49]["MT_label__"] = """50"""
		self.vs[49]["mm__"] = """MT_pre__directLink_T"""
		self.vs[49]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.a.2GenericMemberRefassoc490.2.a.17CFunctionPointerStructMember')

		# apply association GlobalVarRef--var-->GlobalVariableDeclarationnode
		self.add_node()
		self.vs[50]["MT_pre__attr1"] = """return attr_value == "var" """
		self.vs[50]["MT_label__"] = """51"""
		self.vs[50]["mm__"] = """MT_pre__directLink_T"""
		self.vs[50]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.a.10GlobalVarRefassoc500.2.a.15GlobalVariableDeclaration')

		# trace association Function--trace-->InstanceConfigurationnode
		self.add_node()
		self.vs[51]["MT_label__"] = """52"""
		self.vs[51]["mm__"] = """MT_pre__trace_link"""
		self.vs[51]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.a.8Functionassoc510.2.m.5InstanceConfiguration')

		# trace association FunctionPrototype--trace-->ComponentInstancenode
		self.add_node()
		self.vs[52]["MT_label__"] = """53"""
		self.vs[52]["mm__"] = """MT_pre__trace_link"""
		self.vs[52]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.a.6FunctionPrototypeassoc520.2.m.0ComponentInstance')

		# trace association Function--trace-->ComponentInstancenode
		self.add_node()
		self.vs[53]["MT_label__"] = """54"""
		self.vs[53]["mm__"] = """MT_pre__trace_link"""
		self.vs[53]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.a.13Functionassoc530.2.m.0ComponentInstance')

		# trace association FunctionPrototype--trace-->Executablenode
		self.add_node()
		self.vs[54]["MT_label__"] = """55"""
		self.vs[54]["mm__"] = """MT_pre__trace_link"""
		self.vs[54]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.a.14FunctionPrototypeassoc540.2.m.3Executable')

		# trace association GlobalVariableDeclaration--trace-->ComponentInstancenode
		self.add_node()
		self.vs[55]["MT_label__"] = """56"""
		self.vs[55]["mm__"] = """MT_pre__trace_link"""
		self.vs[55]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.a.15GlobalVariableDeclarationassoc550.2.m.0ComponentInstance')

		# trace association StructDeclaration--trace-->ClientServerInterfacenode
		self.add_node()
		self.vs[56]["MT_label__"] = """57"""
		self.vs[56]["mm__"] = """MT_pre__trace_link"""
		self.vs[56]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.a.16StructDeclarationassoc560.2.m.6ClientServerInterface')

		# trace association CFunctionPointerStructMember--trace-->Operationnode
		self.add_node()
		self.vs[57]["MT_label__"] = """58"""
		self.vs[57]["mm__"] = """MT_pre__trace_link"""
		self.vs[57]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.a.17CFunctionPointerStructMemberassoc570.2.m.1Operation')

		self['equations'].append(((14,'name'),('concat',(('wildcard'),('constant','__wire')))))
		self['equations'].append(((16,'name'),('concat',(('wildcard'),('constant','__init')))))
		self['equations'].append(((21,'name'),('concat',(('wildcard'),('constant','__wire')))))
		self['equations'].append(((22,'name'),('concat',(('wildcard'),(3,'name')))))
		self['equations'].append(((23,'name'),('concat',(('wildcard'),('constant','__ops')))))
		self['equations'].append(((24,'name'),('concat',(('wildcard'),('constant','__idata')))))
		self['equations'].append(((25,'name'),(1,'name')))

		# Add the edges
		self.add_edges([
			(5,26), # match class InstanceConfiguration(0.2.m.5InstanceConfiguration) -> association contents
			(26,0), # association ComponentInstance -> match class ComponentInstance(0.2.m.0ComponentInstance)
			(7,27), # match class AtomicComponent(0.2.m.7AtomicComponent) -> association contents
			(27,4), # association ProvidedPort -> match class ProvidedPort(0.2.m.4ProvidedPort)
			(0,28), # match class ComponentInstance(0.2.m.0ComponentInstance) -> association component
			(28,7), # association AtomicComponent -> match class AtomicComponent(0.2.m.7AtomicComponent)
			(7,29), # match class AtomicComponent(0.2.m.7AtomicComponent) -> association contents
			(29,3), # association Executable -> match class Executable(0.2.m.3Executable)
			(3,30), # match class Executable(0.2.m.3Executable) -> association trigger
			(30,2), # association OperationTrigger -> match class OperationTrigger(0.2.m.2OperationTrigger)
			(2,31), # match class OperationTrigger(0.2.m.2OperationTrigger) -> association calledOperation
			(31,1), # association Operation -> match class Operation(0.2.m.1Operation)
			(4,32), # match class ProvidedPort(0.2.m.4ProvidedPort) -> association intf
			(32,6), # association ClientServerInterface -> match class ClientServerInterface(0.2.m.6ClientServerInterface)
			(6,33), # match class ClientServerInterface(0.2.m.6ClientServerInterface) -> association contents
			(33,1), # association Operation -> match class Operation(0.2.m.1Operation)
			(2,34), # match class OperationTrigger(0.2.m.2OperationTrigger) -> association providedPort
			(34,4), # association ProvidedPort -> match class ProvidedPort(0.2.m.4ProvidedPort)
			(9,35), # apply class FunctionCall(0.2.a.1FunctionCall) -> association function
			(35,14), # association FunctionPrototype -> apply class FunctionPrototype(0.2.a.6FunctionPrototype)
			(16,36), # apply class Function(0.2.a.8Function) -> association body
			(36,13), # association StatementList -> apply class StatementList(0.2.a.5StatementList)
			(13,37), # apply class StatementList(0.2.a.5StatementList) -> association statements
			(37,15), # association ExpressionStatement -> apply class ExpressionStatement(0.2.a.7ExpressionStatement)
			(15,38), # apply class ExpressionStatement(0.2.a.7ExpressionStatement) -> association expr
			(38,9), # association FunctionCall -> apply class FunctionCall(0.2.a.1FunctionCall)
			(21,39), # apply class Function(0.2.a.13Function) -> association body
			(39,8), # association StatementList -> apply class StatementList(0.2.a.0StatementList)
			(8,40), # apply class StatementList(0.2.a.0StatementList) -> association statements
			(40,12), # association ExpressionStatement -> apply class ExpressionStatement(0.2.a.4ExpressionStatement)
			(12,41), # apply class ExpressionStatement(0.2.a.4ExpressionStatement) -> association expr
			(41,11), # association AssignmentExpr -> apply class AssignmentExpr(0.2.a.3AssignmentExpr)
			(11,42), # apply class AssignmentExpr(0.2.a.3AssignmentExpr) -> association left
			(42,20), # association GenericDotExpression -> apply class GenericDotExpression(0.2.a.12GenericDotExpression)
			(11,43), # apply class AssignmentExpr(0.2.a.3AssignmentExpr) -> association right
			(43,19), # association ReferenceExpression -> apply class ReferenceExpression(0.2.a.11ReferenceExpression)
			(20,44), # apply class GenericDotExpression(0.2.a.12GenericDotExpression) -> association expression
			(44,18), # association GlobalVarRef -> apply class GlobalVarRef(0.2.a.10GlobalVarRef)
			(20,45), # apply class GenericDotExpression(0.2.a.12GenericDotExpression) -> association target
			(45,10), # association GenericMemberRef -> apply class GenericMemberRef(0.2.a.2GenericMemberRef)
			(19,46), # apply class ReferenceExpression(0.2.a.11ReferenceExpression) -> association expression
			(46,17), # association FunctionRefExpr -> apply class FunctionRefExpr(0.2.a.9FunctionRefExpr)
			(17,47), # apply class FunctionRefExpr(0.2.a.9FunctionRefExpr) -> association function
			(47,22), # association FunctionPrototype -> apply class FunctionPrototype(0.2.a.14FunctionPrototype)
			(24,48), # apply class StructDeclaration(0.2.a.16StructDeclaration) -> association members
			(48,25), # association CFunctionPointerStructMember -> apply class CFunctionPointerStructMember(0.2.a.17CFunctionPointerStructMember)
			(10,49), # apply class GenericMemberRef(0.2.a.2GenericMemberRef) -> association member
			(49,25), # association CFunctionPointerStructMember -> apply class CFunctionPointerStructMember(0.2.a.17CFunctionPointerStructMember)
			(18,50), # apply class GlobalVarRef(0.2.a.10GlobalVarRef) -> association var
			(50,23), # association GlobalVariableDeclaration -> apply class GlobalVariableDeclaration(0.2.a.15GlobalVariableDeclaration)
			(16,51), # apply class Function(0.2.m.5InstanceConfiguration) -> backward_association 
			(51,5), # backward_associationInstanceConfiguration -> match_class InstanceConfiguration(0.2.m.5InstanceConfiguration)
			(14,52), # apply class FunctionPrototype(0.2.m.0ComponentInstance) -> backward_association 
			(52,0), # backward_associationComponentInstance -> match_class ComponentInstance(0.2.m.0ComponentInstance)
			(21,53), # apply class Function(0.2.m.0ComponentInstance) -> backward_association 
			(53,0), # backward_associationComponentInstance -> match_class ComponentInstance(0.2.m.0ComponentInstance)
			(22,54), # apply class FunctionPrototype(0.2.m.3Executable) -> backward_association 
			(54,3), # backward_associationExecutable -> match_class Executable(0.2.m.3Executable)
			(23,55), # apply class GlobalVariableDeclaration(0.2.m.0ComponentInstance) -> backward_association 
			(55,0), # backward_associationComponentInstance -> match_class ComponentInstance(0.2.m.0ComponentInstance)
			(24,56), # apply class StructDeclaration(0.2.m.6ClientServerInterface) -> backward_association 
			(56,6), # backward_associationClientServerInterface -> match_class ClientServerInterface(0.2.m.6ClientServerInterface)
			(25,57), # apply class CFunctionPointerStructMember(0.2.m.1Operation) -> backward_association 
			(57,1), # backward_associationOperation -> match_class Operation(0.2.m.1Operation)
		])


	# define evaluation methods for each match class.

	def eval_attr11(self, attr_value, this):
		return True

	def eval_attr12(self, attr_value, this):
		return True

	def eval_attr13(self, attr_value, this):
		return True

	def eval_attr14(self, attr_value, this):
		return True

	def eval_attr15(self, attr_value, this):
		return True

	def eval_attr16(self, attr_value, this):
		return True

	def eval_attr17(self, attr_value, this):
		return True

	def eval_attr18(self, attr_value, this):
		return True

	# define evaluation methods for each apply class.

	def eval_attr19(self, attr_value, this):
		return True

	def eval_attr110(self, attr_value, this):
		return True

	def eval_attr111(self, attr_value, this):
		return True

	def eval_attr112(self, attr_value, this):
		return True

	def eval_attr113(self, attr_value, this):
		return True

	def eval_attr114(self, attr_value, this):
		return True

	def eval_attr115(self, attr_value, this):
		return True

	def eval_attr116(self, attr_value, this):
		return True

	def eval_attr117(self, attr_value, this):
		return True

	def eval_attr118(self, attr_value, this):
		return True

	def eval_attr119(self, attr_value, this):
		return True

	def eval_attr120(self, attr_value, this):
		return True

	def eval_attr121(self, attr_value, this):
		return True

	def eval_attr122(self, attr_value, this):
		return True

	def eval_attr123(self, attr_value, this):
		return True

	def eval_attr124(self, attr_value, this):
		return True

	def eval_attr125(self, attr_value, this):
		return True

	def eval_attr126(self, attr_value, this):
		return True

		# define evaluation methods for each match association.

	def eval_attr127(self, attr_value, this):
		return attr_value == "contents"
	def eval_attr128(self, attr_value, this):
		return attr_value == "contents"
	def eval_attr129(self, attr_value, this):
		return attr_value == "component"
	def eval_attr130(self, attr_value, this):
		return attr_value == "contents"
	def eval_attr131(self, attr_value, this):
		return attr_value == "trigger"
	def eval_attr132(self, attr_value, this):
		return attr_value == "calledOperation"
	def eval_attr133(self, attr_value, this):
		return attr_value == "intf"
	def eval_attr134(self, attr_value, this):
		return attr_value == "contents"
	def eval_attr135(self, attr_value, this):
		return attr_value == "providedPort"
		# define evaluation methods for each apply association.

	def eval_attr136(self, attr_value, this):
		return attr_value == "function"
	def eval_attr137(self, attr_value, this):
		return attr_value == "body"
	def eval_attr138(self, attr_value, this):
		return attr_value == "statements"
	def eval_attr139(self, attr_value, this):
		return attr_value == "expr"
	def eval_attr140(self, attr_value, this):
		return attr_value == "body"
	def eval_attr141(self, attr_value, this):
		return attr_value == "statements"
	def eval_attr142(self, attr_value, this):
		return attr_value == "expr"
	def eval_attr143(self, attr_value, this):
		return attr_value == "left"
	def eval_attr144(self, attr_value, this):
		return attr_value == "right"
	def eval_attr145(self, attr_value, this):
		return attr_value == "expression"
	def eval_attr146(self, attr_value, this):
		return attr_value == "target"
	def eval_attr147(self, attr_value, this):
		return attr_value == "expression"
	def eval_attr148(self, attr_value, this):
		return attr_value == "function"
	def eval_attr149(self, attr_value, this):
		return attr_value == "members"
	def eval_attr150(self, attr_value, this):
		return attr_value == "member"
	def eval_attr151(self, attr_value, this):
		return attr_value == "var"

	def constraint(self, PreNode, graph):
		return True

