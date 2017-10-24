from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HAssignmentInstance_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HAssignmentInstance_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HAssignmentInstance_CompleteLHS, self).__init__(name='HAssignmentInstance_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HAssignmentInstance_CompleteLHS')
		self["equations"] = []
		# Set the node attributes

		# match class AssemblyConnector(0.1.m.0AssemblyConnector) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__AssemblyConnector"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.1.m.0AssemblyConnector')

		# match class InstancePortRef(0.1.m.1InstancePortRef) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__InstancePortRef"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.1.m.1InstancePortRef')

		# match class ComponentInstance(0.1.m.2ComponentInstance) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__ComponentInstance"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.1.m.2ComponentInstance')

		# match class RequiredPort(0.1.m.3RequiredPort) node
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return True"""
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__RequiredPort"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.1.m.3RequiredPort')

		# match class AtomicComponent(0.1.m.4AtomicComponent) node
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return True"""
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__AtomicComponent"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.1.m.4AtomicComponent')

		# match class InstancePortRef(0.1.m.5InstancePortRef) node
		self.add_node()
		self.vs[5]["MT_pre__attr1"] = """return True"""
		self.vs[5]["MT_label__"] = """6"""
		self.vs[5]["mm__"] = """MT_pre__InstancePortRef"""
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.1.m.5InstancePortRef')

		# match class ComponentInstance(0.1.m.6ComponentInstance) node
		self.add_node()
		self.vs[6]["MT_pre__attr1"] = """return True"""
		self.vs[6]["MT_label__"] = """7"""
		self.vs[6]["mm__"] = """MT_pre__ComponentInstance"""
		self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.1.m.6ComponentInstance')

		# match class ProvidedPort(0.1.m.7ProvidedPort) node
		self.add_node()
		self.vs[7]["MT_pre__attr1"] = """return True"""
		self.vs[7]["MT_label__"] = """8"""
		self.vs[7]["mm__"] = """MT_pre__ProvidedPort"""
		self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.1.m.7ProvidedPort')

		# match class AtomicComponent(0.1.m.8AtomicComponent) node
		self.add_node()
		self.vs[8]["MT_pre__attr1"] = """return True"""
		self.vs[8]["MT_label__"] = """9"""
		self.vs[8]["mm__"] = """MT_pre__AtomicComponent"""
		self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.1.m.8AtomicComponent')

		# apply class GenericDotExpression(0.1.a.0GenericDotExpression) node
		self.add_node()
		self.vs[9]["MT_pre__attr1"] = """return True"""
		self.vs[9]["MT_label__"] = """10"""
		self.vs[9]["mm__"] = """MT_pre__GenericDotExpression"""
		self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.1.a.0GenericDotExpression')

		# apply class GlobalVarRef(0.1.a.1GlobalVarRef) node
		self.add_node()
		self.vs[10]["MT_pre__attr1"] = """return True"""
		self.vs[10]["MT_label__"] = """11"""
		self.vs[10]["mm__"] = """MT_pre__GlobalVarRef"""
		self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.1.a.1GlobalVarRef')

		# apply class GlobalVariableDeclaration(0.1.a.2GlobalVariableDeclaration) node
		self.add_node()
		self.vs[11]["MT_pre__attr1"] = """return True"""
		self.vs[11]["MT_label__"] = """12"""
		self.vs[11]["mm__"] = """MT_pre__GlobalVariableDeclaration"""
		self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.1.a.2GlobalVariableDeclaration')

		# apply class ReferenceExpr(0.1.a.3ReferenceExpr) node
		self.add_node()
		self.vs[12]["MT_pre__attr1"] = """return True"""
		self.vs[12]["MT_label__"] = """13"""
		self.vs[12]["mm__"] = """MT_pre__ReferenceExpr"""
		self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.1.a.3ReferenceExpr')

		# apply class GenericMemberRef(0.1.a.4GenericMemberRef) node
		self.add_node()
		self.vs[13]["MT_pre__attr1"] = """return True"""
		self.vs[13]["MT_label__"] = """14"""
		self.vs[13]["mm__"] = """MT_pre__GenericMemberRef"""
		self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.1.a.4GenericMemberRef')

		# apply class GlobalVariableDeclaration(0.1.a.5GlobalVariableDeclaration) node
		self.add_node()
		self.vs[14]["MT_pre__attr1"] = """return True"""
		self.vs[14]["MT_label__"] = """15"""
		self.vs[14]["mm__"] = """MT_pre__GlobalVariableDeclaration"""
		self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.1.a.5GlobalVariableDeclaration')

		# apply class GlobalVarRef(0.1.a.6GlobalVarRef) node
		self.add_node()
		self.vs[15]["MT_pre__attr1"] = """return True"""
		self.vs[15]["MT_label__"] = """16"""
		self.vs[15]["mm__"] = """MT_pre__GlobalVarRef"""
		self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.1.a.6GlobalVarRef')

		# apply class AssignmentExpr(0.1.a.7AssignmentExpr) node
		self.add_node()
		self.vs[16]["MT_pre__attr1"] = """return True"""
		self.vs[16]["MT_label__"] = """17"""
		self.vs[16]["mm__"] = """MT_pre__AssignmentExpr"""
		self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.1.a.7AssignmentExpr')

		# apply class StructDeclaration(0.1.a.8StructDeclaration) node
		self.add_node()
		self.vs[17]["MT_pre__attr1"] = """return True"""
		self.vs[17]["MT_label__"] = """18"""
		self.vs[17]["mm__"] = """MT_pre__StructDeclaration"""
		self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.1.a.8StructDeclaration')

		# apply class Member(0.1.a.9Member) node
		self.add_node()
		self.vs[18]["MT_pre__attr1"] = """return True"""
		self.vs[18]["MT_label__"] = """19"""
		self.vs[18]["mm__"] = """MT_pre__Member"""
		self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.1.a.9Member')

		# apply class TypeDefType(0.1.a.10TypeDefType) node
		self.add_node()
		self.vs[19]["MT_pre__attr1"] = """return True"""
		self.vs[19]["MT_label__"] = """20"""
		self.vs[19]["mm__"] = """MT_pre__TypeDefType"""
		self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.1.a.10TypeDefType')

		# apply class TypeDef(0.1.a.11TypeDef) node
		self.add_node()
		self.vs[20]["MT_pre__attr1"] = """return True"""
		self.vs[20]["MT_label__"] = """21"""
		self.vs[20]["mm__"] = """MT_pre__TypeDef"""
		self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.1.a.11TypeDef')

		# apply class StructType(0.1.a.12StructType) node
		self.add_node()
		self.vs[21]["MT_pre__attr1"] = """return True"""
		self.vs[21]["MT_label__"] = """22"""
		self.vs[21]["mm__"] = """MT_pre__StructType"""
		self.vs[21]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.1.a.12StructType')

		# match association AssemblyConnector--source-->InstancePortRefnode
		self.add_node()
		self.vs[22]["MT_pre__attr1"] = """return attr_value == "source" """
		self.vs[22]["MT_label__"] = """23"""
		self.vs[22]["mm__"] = """MT_pre__directLink_S"""
		self.vs[22]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.1.m.0AssemblyConnectorassoc220.1.m.1InstancePortRef')

		# match association InstancePortRef--instance-->ComponentInstancenode
		self.add_node()
		self.vs[23]["MT_pre__attr1"] = """return attr_value == "instance" """
		self.vs[23]["MT_label__"] = """24"""
		self.vs[23]["mm__"] = """MT_pre__directLink_S"""
		self.vs[23]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.1.m.1InstancePortRefassoc230.1.m.2ComponentInstance')

		# match association InstancePortRef--port-->RequiredPortnode
		self.add_node()
		self.vs[24]["MT_pre__attr1"] = """return attr_value == "port" """
		self.vs[24]["MT_label__"] = """25"""
		self.vs[24]["mm__"] = """MT_pre__directLink_S"""
		self.vs[24]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.1.m.1InstancePortRefassoc240.1.m.3RequiredPort')

		# match association ComponentInstance--component-->AtomicComponentnode
		self.add_node()
		self.vs[25]["MT_pre__attr1"] = """return attr_value == "component" """
		self.vs[25]["MT_label__"] = """26"""
		self.vs[25]["mm__"] = """MT_pre__directLink_S"""
		self.vs[25]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.1.m.2ComponentInstanceassoc250.1.m.4AtomicComponent')

		# match association AtomicComponent--contents-->RequiredPortnode
		self.add_node()
		self.vs[26]["MT_pre__attr1"] = """return attr_value == "contents" """
		self.vs[26]["MT_label__"] = """27"""
		self.vs[26]["mm__"] = """MT_pre__directLink_S"""
		self.vs[26]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.1.m.4AtomicComponentassoc260.1.m.3RequiredPort')

		# match association AssemblyConnector--target-->InstancePortRefnode
		self.add_node()
		self.vs[27]["MT_pre__attr1"] = """return attr_value == "target" """
		self.vs[27]["MT_label__"] = """28"""
		self.vs[27]["mm__"] = """MT_pre__directLink_S"""
		self.vs[27]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.1.m.0AssemblyConnectorassoc270.1.m.5InstancePortRef')

		# match association InstancePortRef--instance-->ComponentInstancenode
		self.add_node()
		self.vs[28]["MT_pre__attr1"] = """return attr_value == "instance" """
		self.vs[28]["MT_label__"] = """29"""
		self.vs[28]["mm__"] = """MT_pre__directLink_S"""
		self.vs[28]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.1.m.5InstancePortRefassoc280.1.m.6ComponentInstance')

		# match association InstancePortRef--port-->ProvidedPortnode
		self.add_node()
		self.vs[29]["MT_pre__attr1"] = """return attr_value == "port" """
		self.vs[29]["MT_label__"] = """30"""
		self.vs[29]["mm__"] = """MT_pre__directLink_S"""
		self.vs[29]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.1.m.5InstancePortRefassoc290.1.m.7ProvidedPort')

		# match association ComponentInstance--component-->AtomicComponentnode
		self.add_node()
		self.vs[30]["MT_pre__attr1"] = """return attr_value == "component" """
		self.vs[30]["MT_label__"] = """31"""
		self.vs[30]["mm__"] = """MT_pre__directLink_S"""
		self.vs[30]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.1.m.6ComponentInstanceassoc300.1.m.8AtomicComponent')

		# match association AtomicComponent--contents-->ProvidedPortnode
		self.add_node()
		self.vs[31]["MT_pre__attr1"] = """return attr_value == "contents" """
		self.vs[31]["MT_label__"] = """32"""
		self.vs[31]["mm__"] = """MT_pre__directLink_S"""
		self.vs[31]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.1.m.8AtomicComponentassoc310.1.m.7ProvidedPort')

		# apply association AssignmentExpr--left-->GenericDotExpressionnode
		self.add_node()
		self.vs[32]["MT_pre__attr1"] = """return attr_value == "left" """
		self.vs[32]["MT_label__"] = """33"""
		self.vs[32]["mm__"] = """MT_pre__directLink_T"""
		self.vs[32]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.1.a.7AssignmentExprassoc320.1.a.0GenericDotExpression')

		# apply association AssignmentExpr--right-->ReferenceExprnode
		self.add_node()
		self.vs[33]["MT_pre__attr1"] = """return attr_value == "right" """
		self.vs[33]["MT_label__"] = """34"""
		self.vs[33]["mm__"] = """MT_pre__directLink_T"""
		self.vs[33]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.1.a.7AssignmentExprassoc330.1.a.3ReferenceExpr')

		# apply association GenericDotExpression--expression-->GlobalVarRefnode
		self.add_node()
		self.vs[34]["MT_pre__attr1"] = """return attr_value == "expression" """
		self.vs[34]["MT_label__"] = """35"""
		self.vs[34]["mm__"] = """MT_pre__directLink_T"""
		self.vs[34]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.1.a.0GenericDotExpressionassoc340.1.a.6GlobalVarRef')

		# apply association GenericDotExpression--target-->GenericMemberRefnode
		self.add_node()
		self.vs[35]["MT_pre__attr1"] = """return attr_value == "target" """
		self.vs[35]["MT_label__"] = """36"""
		self.vs[35]["mm__"] = """MT_pre__directLink_T"""
		self.vs[35]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.1.a.0GenericDotExpressionassoc350.1.a.4GenericMemberRef')

		# apply association ReferenceExpr--expression-->GlobalVarRefnode
		self.add_node()
		self.vs[36]["MT_pre__attr1"] = """return attr_value == "expression" """
		self.vs[36]["MT_label__"] = """37"""
		self.vs[36]["mm__"] = """MT_pre__directLink_T"""
		self.vs[36]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.1.a.3ReferenceExprassoc360.1.a.1GlobalVarRef')

		# apply association GlobalVarRef--var-->GlobalVariableDeclarationnode
		self.add_node()
		self.vs[37]["MT_pre__attr1"] = """return attr_value == "var" """
		self.vs[37]["MT_label__"] = """38"""
		self.vs[37]["mm__"] = """MT_pre__directLink_T"""
		self.vs[37]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.1.a.6GlobalVarRefassoc370.1.a.2GlobalVariableDeclaration')

		# apply association GenericMemberRef--member-->Membernode
		self.add_node()
		self.vs[38]["MT_pre__attr1"] = """return attr_value == "member" """
		self.vs[38]["MT_label__"] = """39"""
		self.vs[38]["mm__"] = """MT_pre__directLink_T"""
		self.vs[38]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.1.a.4GenericMemberRefassoc380.1.a.9Member')

		# apply association StructDeclaration--members-->Membernode
		self.add_node()
		self.vs[39]["MT_pre__attr1"] = """return attr_value == "members" """
		self.vs[39]["MT_label__"] = """40"""
		self.vs[39]["mm__"] = """MT_pre__directLink_T"""
		self.vs[39]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.1.a.8StructDeclarationassoc390.1.a.9Member')

		# apply association GlobalVarRef--var-->GlobalVariableDeclarationnode
		self.add_node()
		self.vs[40]["MT_pre__attr1"] = """return attr_value == "var" """
		self.vs[40]["MT_label__"] = """41"""
		self.vs[40]["mm__"] = """MT_pre__directLink_T"""
		self.vs[40]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.1.a.1GlobalVarRefassoc400.1.a.5GlobalVariableDeclaration')

		# apply association GlobalVariableDeclaration--type-->TypeDefTypenode
		self.add_node()
		self.vs[41]["MT_pre__attr1"] = """return attr_value == "type" """
		self.vs[41]["MT_label__"] = """42"""
		self.vs[41]["mm__"] = """MT_pre__directLink_T"""
		self.vs[41]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.1.a.2GlobalVariableDeclarationassoc410.1.a.10TypeDefType')

		# apply association TypeDefType--typeDef-->TypeDefnode
		self.add_node()
		self.vs[42]["MT_pre__attr1"] = """return attr_value == "typeDef" """
		self.vs[42]["MT_label__"] = """43"""
		self.vs[42]["mm__"] = """MT_pre__directLink_T"""
		self.vs[42]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.1.a.10TypeDefTypeassoc420.1.a.11TypeDef')

		# apply association TypeDef--original-->StructTypenode
		self.add_node()
		self.vs[43]["MT_pre__attr1"] = """return attr_value == "original" """
		self.vs[43]["MT_label__"] = """44"""
		self.vs[43]["mm__"] = """MT_pre__directLink_T"""
		self.vs[43]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.1.a.11TypeDefassoc430.1.a.12StructType')

		# apply association StructType--struct-->StructDeclarationnode
		self.add_node()
		self.vs[44]["MT_pre__attr1"] = """return attr_value == "struct" """
		self.vs[44]["MT_label__"] = """45"""
		self.vs[44]["mm__"] = """MT_pre__directLink_T"""
		self.vs[44]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.1.a.12StructTypeassoc440.1.a.8StructDeclaration')

		# trace association GlobalVariableDeclaration--trace-->ComponentInstancenode
		self.add_node()
		self.vs[45]["MT_label__"] = """46"""
		self.vs[45]["mm__"] = """MT_pre__trace_link"""
		self.vs[45]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.1.a.2GlobalVariableDeclarationassoc450.1.m.2ComponentInstance')

		# trace association StructDeclaration--trace-->AtomicComponentnode
		self.add_node()
		self.vs[46]["MT_label__"] = """47"""
		self.vs[46]["mm__"] = """MT_pre__trace_link"""
		self.vs[46]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.1.a.8StructDeclarationassoc460.1.m.4AtomicComponent')

		# trace association GlobalVariableDeclaration--trace-->ComponentInstancenode
		self.add_node()
		self.vs[47]["MT_label__"] = """48"""
		self.vs[47]["mm__"] = """MT_pre__trace_link"""
		self.vs[47]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.1.a.5GlobalVariableDeclarationassoc470.1.m.6ComponentInstance')

		# trace association Member--trace-->RequiredPortnode
		self.add_node()
		self.vs[48]["MT_label__"] = """49"""
		self.vs[48]["mm__"] = """MT_pre__trace_link"""
		self.vs[48]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.1.a.9Memberassoc480.1.m.3RequiredPort')

		self['equations'].append(((11,'name'),('concat',(('wildcard'),('constant','__instance')))))
		self['equations'].append(((14,'name'),('concat',(('wildcard'),('constant','__ops')))))
		self['equations'].append(((17,'name'),('concat',(('wildcard'),('constant','__cdata')))))
		self['equations'].append(((18,'name'),('concat',(('wildcard'),('constant','__ops')))))

		# Add the edges
		self.add_edges([
			(0,22), # match class AssemblyConnector(0.1.m.0AssemblyConnector) -> association source
			(22,1), # association InstancePortRef -> match class InstancePortRef(0.1.m.1InstancePortRef)
			(1,23), # match class InstancePortRef(0.1.m.1InstancePortRef) -> association instance
			(23,2), # association ComponentInstance -> match class ComponentInstance(0.1.m.2ComponentInstance)
			(1,24), # match class InstancePortRef(0.1.m.1InstancePortRef) -> association port
			(24,3), # association RequiredPort -> match class RequiredPort(0.1.m.3RequiredPort)
			(2,25), # match class ComponentInstance(0.1.m.2ComponentInstance) -> association component
			(25,4), # association AtomicComponent -> match class AtomicComponent(0.1.m.4AtomicComponent)
			(4,26), # match class AtomicComponent(0.1.m.4AtomicComponent) -> association contents
			(26,3), # association RequiredPort -> match class RequiredPort(0.1.m.3RequiredPort)
			(0,27), # match class AssemblyConnector(0.1.m.0AssemblyConnector) -> association target
			(27,5), # association InstancePortRef -> match class InstancePortRef(0.1.m.5InstancePortRef)
			(5,28), # match class InstancePortRef(0.1.m.5InstancePortRef) -> association instance
			(28,6), # association ComponentInstance -> match class ComponentInstance(0.1.m.6ComponentInstance)
			(5,29), # match class InstancePortRef(0.1.m.5InstancePortRef) -> association port
			(29,7), # association ProvidedPort -> match class ProvidedPort(0.1.m.7ProvidedPort)
			(6,30), # match class ComponentInstance(0.1.m.6ComponentInstance) -> association component
			(30,8), # association AtomicComponent -> match class AtomicComponent(0.1.m.8AtomicComponent)
			(8,31), # match class AtomicComponent(0.1.m.8AtomicComponent) -> association contents
			(31,7), # association ProvidedPort -> match class ProvidedPort(0.1.m.7ProvidedPort)
			(16,32), # apply class AssignmentExpr(0.1.a.7AssignmentExpr) -> association left
			(32,9), # association GenericDotExpression -> apply class GenericDotExpression(0.1.a.0GenericDotExpression)
			(16,33), # apply class AssignmentExpr(0.1.a.7AssignmentExpr) -> association right
			(33,12), # association ReferenceExpr -> apply class ReferenceExpr(0.1.a.3ReferenceExpr)
			(9,34), # apply class GenericDotExpression(0.1.a.0GenericDotExpression) -> association expression
			(34,15), # association GlobalVarRef -> apply class GlobalVarRef(0.1.a.6GlobalVarRef)
			(9,35), # apply class GenericDotExpression(0.1.a.0GenericDotExpression) -> association target
			(35,13), # association GenericMemberRef -> apply class GenericMemberRef(0.1.a.4GenericMemberRef)
			(12,36), # apply class ReferenceExpr(0.1.a.3ReferenceExpr) -> association expression
			(36,10), # association GlobalVarRef -> apply class GlobalVarRef(0.1.a.1GlobalVarRef)
			(15,37), # apply class GlobalVarRef(0.1.a.6GlobalVarRef) -> association var
			(37,11), # association GlobalVariableDeclaration -> apply class GlobalVariableDeclaration(0.1.a.2GlobalVariableDeclaration)
			(13,38), # apply class GenericMemberRef(0.1.a.4GenericMemberRef) -> association member
			(38,18), # association Member -> apply class Member(0.1.a.9Member)
			(17,39), # apply class StructDeclaration(0.1.a.8StructDeclaration) -> association members
			(39,18), # association Member -> apply class Member(0.1.a.9Member)
			(10,40), # apply class GlobalVarRef(0.1.a.1GlobalVarRef) -> association var
			(40,14), # association GlobalVariableDeclaration -> apply class GlobalVariableDeclaration(0.1.a.5GlobalVariableDeclaration)
			(11,41), # apply class GlobalVariableDeclaration(0.1.a.2GlobalVariableDeclaration) -> association type
			(41,19), # association TypeDefType -> apply class TypeDefType(0.1.a.10TypeDefType)
			(19,42), # apply class TypeDefType(0.1.a.10TypeDefType) -> association typeDef
			(42,20), # association TypeDef -> apply class TypeDef(0.1.a.11TypeDef)
			(20,43), # apply class TypeDef(0.1.a.11TypeDef) -> association original
			(43,21), # association StructType -> apply class StructType(0.1.a.12StructType)
			(21,44), # apply class StructType(0.1.a.12StructType) -> association struct
			(44,17), # association StructDeclaration -> apply class StructDeclaration(0.1.a.8StructDeclaration)
			(11,45), # apply class GlobalVariableDeclaration(0.1.m.2ComponentInstance) -> backward_association 
			(45,2), # backward_associationComponentInstance -> match_class ComponentInstance(0.1.m.2ComponentInstance)
			(17,46), # apply class StructDeclaration(0.1.m.4AtomicComponent) -> backward_association 
			(46,4), # backward_associationAtomicComponent -> match_class AtomicComponent(0.1.m.4AtomicComponent)
			(14,47), # apply class GlobalVariableDeclaration(0.1.m.6ComponentInstance) -> backward_association 
			(47,6), # backward_associationComponentInstance -> match_class ComponentInstance(0.1.m.6ComponentInstance)
			(18,48), # apply class Member(0.1.m.3RequiredPort) -> backward_association 
			(48,3), # backward_associationRequiredPort -> match_class RequiredPort(0.1.m.3RequiredPort)
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

	def eval_attr19(self, attr_value, this):
		return True

	# define evaluation methods for each apply class.

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

		# define evaluation methods for each match association.

	def eval_attr123(self, attr_value, this):
		return attr_value == "source"
	def eval_attr124(self, attr_value, this):
		return attr_value == "instance"
	def eval_attr125(self, attr_value, this):
		return attr_value == "port"
	def eval_attr126(self, attr_value, this):
		return attr_value == "component"
	def eval_attr127(self, attr_value, this):
		return attr_value == "contents"
	def eval_attr128(self, attr_value, this):
		return attr_value == "target"
	def eval_attr129(self, attr_value, this):
		return attr_value == "instance"
	def eval_attr130(self, attr_value, this):
		return attr_value == "port"
	def eval_attr131(self, attr_value, this):
		return attr_value == "component"
	def eval_attr132(self, attr_value, this):
		return attr_value == "contents"
		# define evaluation methods for each apply association.

	def eval_attr133(self, attr_value, this):
		return attr_value == "left"
	def eval_attr134(self, attr_value, this):
		return attr_value == "right"
	def eval_attr135(self, attr_value, this):
		return attr_value == "expression"
	def eval_attr136(self, attr_value, this):
		return attr_value == "target"
	def eval_attr137(self, attr_value, this):
		return attr_value == "expression"
	def eval_attr138(self, attr_value, this):
		return attr_value == "var"
	def eval_attr139(self, attr_value, this):
		return attr_value == "member"
	def eval_attr140(self, attr_value, this):
		return attr_value == "members"
	def eval_attr141(self, attr_value, this):
		return attr_value == "var"
	def eval_attr142(self, attr_value, this):
		return attr_value == "type"
	def eval_attr143(self, attr_value, this):
		return attr_value == "typeDef"
	def eval_attr144(self, attr_value, this):
		return attr_value == "original"
	def eval_attr145(self, attr_value, this):
		return attr_value == "struct"

	def constraint(self, PreNode, graph):
		return True

