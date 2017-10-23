from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HAssignmentInstance2_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HAssignmentInstance2_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HAssignmentInstance2_CompleteLHS, self).__init__(name='HAssignmentInstance2_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HAssignmentInstance2_CompleteLHS')
		self["equations"] = []
		# Set the node attributes

		# match class ImplementationModule(0.3.m.0ImplementationModule) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__ImplementationModule"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.0ImplementationModule')

		# match class Function(0.3.m.1Function) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__Function"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.1Function')

		# match class ComponentInstance(0.3.m.2ComponentInstance) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__ComponentInstance"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.2ComponentInstance')

		# match class InstanceConfiguration(0.3.m.3InstanceConfiguration) node
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return True"""
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__InstanceConfiguration"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.3InstanceConfiguration')

		# match class TestCase(0.3.m.4TestCase) node
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return True"""
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__TestCase"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.4TestCase')

		# match class StatementList(0.3.m.5StatementList) node
		self.add_node()
		self.vs[5]["MT_pre__attr1"] = """return True"""
		self.vs[5]["MT_label__"] = """6"""
		self.vs[5]["mm__"] = """MT_pre__StatementList"""
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.5StatementList')

		# match class InitializeConfiguration(0.3.m.6InitializeConfiguration) node
		self.add_node()
		self.vs[6]["MT_pre__attr1"] = """return True"""
		self.vs[6]["MT_label__"] = """7"""
		self.vs[6]["mm__"] = """MT_pre__InitializeConfiguration"""
		self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.6InitializeConfiguration')

		# match class StatementList(0.3.m.7StatementList) node
		self.add_node()
		self.vs[7]["MT_pre__attr1"] = """return True"""
		self.vs[7]["MT_label__"] = """8"""
		self.vs[7]["mm__"] = """MT_pre__StatementList"""
		self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.7StatementList')

		# match class ExecuteTestExpression(0.3.m.8ExecuteTestExpression) node
		self.add_node()
		self.vs[8]["MT_pre__attr1"] = """return True"""
		self.vs[8]["MT_label__"] = """9"""
		self.vs[8]["mm__"] = """MT_pre__ExecuteTestExpression"""
		self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.8ExecuteTestExpression')

		# match class TestCaseRef(0.3.m.9TestCaseRef) node
		self.add_node()
		self.vs[9]["MT_pre__attr1"] = """return True"""
		self.vs[9]["MT_label__"] = """10"""
		self.vs[9]["mm__"] = """MT_pre__TestCaseRef"""
		self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.9TestCaseRef')

		# match class ReturnStatement(0.3.m.10ReturnStatement) node
		self.add_node()
		self.vs[10]["MT_pre__attr1"] = """return True"""
		self.vs[10]["MT_label__"] = """11"""
		self.vs[10]["mm__"] = """MT_pre__ReturnStatement"""
		self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.10ReturnStatement')

		# apply class Function(0.3.a.0Function) node
		self.add_node()
		self.vs[11]["MT_pre__attr1"] = """return True"""
		self.vs[11]["MT_label__"] = """12"""
		self.vs[11]["mm__"] = """MT_pre__Function"""
		self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.0Function')

		# apply class FunctionPrototype(0.3.a.1FunctionPrototype) node
		self.add_node()
		self.vs[12]["MT_pre__attr1"] = """return True"""
		self.vs[12]["MT_label__"] = """13"""
		self.vs[12]["mm__"] = """MT_pre__FunctionPrototype"""
		self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.1FunctionPrototype')

		# apply class ImplementationModule(0.3.a.2ImplementationModule) node
		self.add_node()
		self.vs[13]["MT_pre__attr1"] = """return True"""
		self.vs[13]["MT_label__"] = """14"""
		self.vs[13]["mm__"] = """MT_pre__ImplementationModule"""
		self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.2ImplementationModule')

		# apply class FunctionPrototype(0.3.a.3FunctionPrototype) node
		self.add_node()
		self.vs[14]["MT_pre__attr1"] = """return True"""
		self.vs[14]["MT_label__"] = """15"""
		self.vs[14]["mm__"] = """MT_pre__FunctionPrototype"""
		self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.3FunctionPrototype')

		# apply class FunctionPrototype(0.3.a.4FunctionPrototype) node
		self.add_node()
		self.vs[15]["MT_pre__attr1"] = """return True"""
		self.vs[15]["MT_label__"] = """16"""
		self.vs[15]["mm__"] = """MT_pre__FunctionPrototype"""
		self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.4FunctionPrototype')

		# apply class StatementList(0.3.a.5StatementList) node
		self.add_node()
		self.vs[16]["MT_pre__attr1"] = """return True"""
		self.vs[16]["MT_label__"] = """17"""
		self.vs[16]["mm__"] = """MT_pre__StatementList"""
		self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.5StatementList')

		# apply class Function(0.3.a.6Function) node
		self.add_node()
		self.vs[17]["MT_pre__attr1"] = """return True"""
		self.vs[17]["MT_label__"] = """18"""
		self.vs[17]["mm__"] = """MT_pre__Function"""
		self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.6Function')

		# apply class ExpressionStatement(0.3.a.7ExpressionStatement) node
		self.add_node()
		self.vs[18]["MT_pre__attr1"] = """return True"""
		self.vs[18]["MT_label__"] = """19"""
		self.vs[18]["mm__"] = """MT_pre__ExpressionStatement"""
		self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.7ExpressionStatement')

		# apply class FunctionCall(0.3.a.8FunctionCall) node
		self.add_node()
		self.vs[19]["MT_pre__attr1"] = """return True"""
		self.vs[19]["MT_label__"] = """20"""
		self.vs[19]["mm__"] = """MT_pre__FunctionCall"""
		self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.8FunctionCall')

		# apply class FunctionCall(0.3.a.9FunctionCall) node
		self.add_node()
		self.vs[20]["MT_pre__attr1"] = """return True"""
		self.vs[20]["MT_label__"] = """21"""
		self.vs[20]["mm__"] = """MT_pre__FunctionCall"""
		self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.9FunctionCall')

		# apply class ExpressionStatement(0.3.a.10ExpressionStatement) node
		self.add_node()
		self.vs[21]["MT_pre__attr1"] = """return True"""
		self.vs[21]["MT_label__"] = """22"""
		self.vs[21]["mm__"] = """MT_pre__ExpressionStatement"""
		self.vs[21]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.10ExpressionStatement')

		# apply class StatementList(0.3.a.11StatementList) node
		self.add_node()
		self.vs[22]["MT_pre__attr1"] = """return True"""
		self.vs[22]["MT_label__"] = """23"""
		self.vs[22]["mm__"] = """MT_pre__StatementList"""
		self.vs[22]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.11StatementList')

		# apply class Function(0.3.a.12Function) node
		self.add_node()
		self.vs[23]["MT_pre__attr1"] = """return True"""
		self.vs[23]["MT_label__"] = """24"""
		self.vs[23]["mm__"] = """MT_pre__Function"""
		self.vs[23]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.12Function')

		# apply class Function(0.3.a.13Function) node
		self.add_node()
		self.vs[24]["MT_pre__attr1"] = """return True"""
		self.vs[24]["MT_label__"] = """25"""
		self.vs[24]["mm__"] = """MT_pre__Function"""
		self.vs[24]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.13Function')

		# apply class ExpressionStatement(0.3.a.14ExpressionStatement) node
		self.add_node()
		self.vs[25]["MT_pre__attr1"] = """return True"""
		self.vs[25]["MT_label__"] = """26"""
		self.vs[25]["mm__"] = """MT_pre__ExpressionStatement"""
		self.vs[25]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.14ExpressionStatement')

		# apply class StatementList(0.3.a.15StatementList) node
		self.add_node()
		self.vs[26]["MT_pre__attr1"] = """return True"""
		self.vs[26]["MT_label__"] = """27"""
		self.vs[26]["mm__"] = """MT_pre__StatementList"""
		self.vs[26]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.15StatementList')

		# apply class Function(0.3.a.16Function) node
		self.add_node()
		self.vs[27]["MT_pre__attr1"] = """return True"""
		self.vs[27]["MT_label__"] = """28"""
		self.vs[27]["mm__"] = """MT_pre__Function"""
		self.vs[27]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.16Function')

		# apply class FunctionCall(0.3.a.17FunctionCall) node
		self.add_node()
		self.vs[28]["MT_pre__attr1"] = """return True"""
		self.vs[28]["MT_label__"] = """29"""
		self.vs[28]["mm__"] = """MT_pre__FunctionCall"""
		self.vs[28]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.17FunctionCall')

		# apply class StatementList(0.3.a.18StatementList) node
		self.add_node()
		self.vs[29]["MT_pre__attr1"] = """return True"""
		self.vs[29]["MT_label__"] = """30"""
		self.vs[29]["mm__"] = """MT_pre__StatementList"""
		self.vs[29]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.18StatementList')

		# apply class ExpressionStatement(0.3.a.19ExpressionStatement) node
		self.add_node()
		self.vs[30]["MT_pre__attr1"] = """return True"""
		self.vs[30]["MT_label__"] = """31"""
		self.vs[30]["mm__"] = """MT_pre__ExpressionStatement"""
		self.vs[30]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.19ExpressionStatement')

		# apply class FunctionCall(0.3.a.20FunctionCall) node
		self.add_node()
		self.vs[31]["MT_pre__attr1"] = """return True"""
		self.vs[31]["MT_label__"] = """32"""
		self.vs[31]["mm__"] = """MT_pre__FunctionCall"""
		self.vs[31]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.20FunctionCall')

		# apply class FunctionPrototype(0.3.a.21FunctionPrototype) node
		self.add_node()
		self.vs[32]["MT_pre__attr1"] = """return True"""
		self.vs[32]["MT_label__"] = """33"""
		self.vs[32]["mm__"] = """MT_pre__FunctionPrototype"""
		self.vs[32]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.21FunctionPrototype')

		# match association InstanceConfiguration--contents-->ComponentInstancenode
		self.add_node()
		self.vs[33]["MT_pre__attr1"] = """return attr_value == "contents" """
		self.vs[33]["MT_label__"] = """34"""
		self.vs[33]["mm__"] = """MT_pre__directLink_S"""
		self.vs[33]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.3InstanceConfigurationassoc330.3.m.2ComponentInstance')

		# match association ImplementationModule--contents-->Functionnode
		self.add_node()
		self.vs[34]["MT_pre__attr1"] = """return attr_value == "contents" """
		self.vs[34]["MT_label__"] = """35"""
		self.vs[34]["mm__"] = """MT_pre__directLink_S"""
		self.vs[34]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.0ImplementationModuleassoc340.3.m.1Function')

		# match association ImplementationModule--contents-->InstanceConfigurationnode
		self.add_node()
		self.vs[35]["MT_pre__attr1"] = """return attr_value == "contents" """
		self.vs[35]["MT_label__"] = """36"""
		self.vs[35]["mm__"] = """MT_pre__directLink_S"""
		self.vs[35]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.0ImplementationModuleassoc350.3.m.3InstanceConfiguration')

		# match association ImplementationModule--contents-->TestCasenode
		self.add_node()
		self.vs[36]["MT_pre__attr1"] = """return attr_value == "contents" """
		self.vs[36]["MT_label__"] = """37"""
		self.vs[36]["mm__"] = """MT_pre__directLink_S"""
		self.vs[36]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.0ImplementationModuleassoc360.3.m.4TestCase')

		# match association TestCase--body-->StatementListnode
		self.add_node()
		self.vs[37]["MT_pre__attr1"] = """return attr_value == "body" """
		self.vs[37]["MT_label__"] = """38"""
		self.vs[37]["mm__"] = """MT_pre__directLink_S"""
		self.vs[37]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.4TestCaseassoc370.3.m.5StatementList')

		# match association StatementList--statements-->InitializeConfigurationnode
		self.add_node()
		self.vs[38]["MT_pre__attr1"] = """return attr_value == "statements" """
		self.vs[38]["MT_label__"] = """39"""
		self.vs[38]["mm__"] = """MT_pre__directLink_S"""
		self.vs[38]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.5StatementListassoc380.3.m.6InitializeConfiguration')

		# match association InitializeConfiguration--config-->InstanceConfigurationnode
		self.add_node()
		self.vs[39]["MT_pre__attr1"] = """return attr_value == "config" """
		self.vs[39]["MT_label__"] = """40"""
		self.vs[39]["mm__"] = """MT_pre__directLink_S"""
		self.vs[39]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.6InitializeConfigurationassoc390.3.m.3InstanceConfiguration')

		# match association Function--body-->StatementListnode
		self.add_node()
		self.vs[40]["MT_pre__attr1"] = """return attr_value == "body" """
		self.vs[40]["MT_label__"] = """41"""
		self.vs[40]["mm__"] = """MT_pre__directLink_S"""
		self.vs[40]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.1Functionassoc400.3.m.7StatementList')

		# match association StatementList--statements-->ReturnStatementnode
		self.add_node()
		self.vs[41]["MT_pre__attr1"] = """return attr_value == "statements" """
		self.vs[41]["MT_label__"] = """42"""
		self.vs[41]["mm__"] = """MT_pre__directLink_S"""
		self.vs[41]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.7StatementListassoc410.3.m.10ReturnStatement')

		# match association ReturnStatement--expression-->ExecuteTestExpressionnode
		self.add_node()
		self.vs[42]["MT_pre__attr1"] = """return attr_value == "expression" """
		self.vs[42]["MT_label__"] = """43"""
		self.vs[42]["mm__"] = """MT_pre__directLink_S"""
		self.vs[42]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.10ReturnStatementassoc420.3.m.8ExecuteTestExpression')

		# match association ExecuteTestExpression--tests-->TestCaseRefnode
		self.add_node()
		self.vs[43]["MT_pre__attr1"] = """return attr_value == "tests" """
		self.vs[43]["MT_label__"] = """44"""
		self.vs[43]["mm__"] = """MT_pre__directLink_S"""
		self.vs[43]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.8ExecuteTestExpressionassoc430.3.m.9TestCaseRef')

		# match association TestCaseRef--testcase-->TestCasenode
		self.add_node()
		self.vs[44]["MT_pre__attr1"] = """return attr_value == "testcase" """
		self.vs[44]["MT_label__"] = """45"""
		self.vs[44]["mm__"] = """MT_pre__directLink_S"""
		self.vs[44]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.9TestCaseRefassoc440.3.m.4TestCase')

		# apply association ImplementationModule--contents-->Functionnode
		self.add_node()
		self.vs[45]["MT_pre__attr1"] = """return attr_value == "contents" """
		self.vs[45]["MT_label__"] = """46"""
		self.vs[45]["mm__"] = """MT_pre__directLink_T"""
		self.vs[45]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.2ImplementationModuleassoc450.3.a.0Function')

		# apply association ImplementationModule--contents-->FunctionPrototypenode
		self.add_node()
		self.vs[46]["MT_pre__attr1"] = """return attr_value == "contents" """
		self.vs[46]["MT_label__"] = """47"""
		self.vs[46]["mm__"] = """MT_pre__directLink_T"""
		self.vs[46]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.2ImplementationModuleassoc460.3.a.1FunctionPrototype')

		# apply association ImplementationModule--contents-->FunctionPrototypenode
		self.add_node()
		self.vs[47]["MT_pre__attr1"] = """return attr_value == "contents" """
		self.vs[47]["MT_label__"] = """48"""
		self.vs[47]["mm__"] = """MT_pre__directLink_T"""
		self.vs[47]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.2ImplementationModuleassoc470.3.a.3FunctionPrototype')

		# apply association StatementList--statements-->ExpressionStatementnode
		self.add_node()
		self.vs[48]["MT_pre__attr1"] = """return attr_value == "statements" """
		self.vs[48]["MT_label__"] = """49"""
		self.vs[48]["mm__"] = """MT_pre__directLink_T"""
		self.vs[48]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.5StatementListassoc480.3.a.7ExpressionStatement')

		# apply association ImplementationModule--contents-->FunctionPrototypenode
		self.add_node()
		self.vs[49]["MT_pre__attr1"] = """return attr_value == "contents" """
		self.vs[49]["MT_label__"] = """50"""
		self.vs[49]["mm__"] = """MT_pre__directLink_T"""
		self.vs[49]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.2ImplementationModuleassoc490.3.a.4FunctionPrototype')

		# apply association Function--body-->StatementListnode
		self.add_node()
		self.vs[50]["MT_pre__attr1"] = """return attr_value == "body" """
		self.vs[50]["MT_label__"] = """51"""
		self.vs[50]["mm__"] = """MT_pre__directLink_T"""
		self.vs[50]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.0Functionassoc500.3.a.5StatementList')

		# apply association ImplementationModule--contents-->Functionnode
		self.add_node()
		self.vs[51]["MT_pre__attr1"] = """return attr_value == "contents" """
		self.vs[51]["MT_label__"] = """52"""
		self.vs[51]["mm__"] = """MT_pre__directLink_T"""
		self.vs[51]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.2ImplementationModuleassoc510.3.a.6Function')

		# apply association ExpressionStatement--expr-->FunctionCallnode
		self.add_node()
		self.vs[52]["MT_pre__attr1"] = """return attr_value == "expr" """
		self.vs[52]["MT_label__"] = """53"""
		self.vs[52]["mm__"] = """MT_pre__directLink_T"""
		self.vs[52]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.7ExpressionStatementassoc520.3.a.8FunctionCall')

		# apply association FunctionCall--function-->FunctionPrototypenode
		self.add_node()
		self.vs[53]["MT_pre__attr1"] = """return attr_value == "function" """
		self.vs[53]["MT_label__"] = """54"""
		self.vs[53]["mm__"] = """MT_pre__directLink_T"""
		self.vs[53]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.8FunctionCallassoc530.3.a.4FunctionPrototype')

		# apply association ImplementationModule--contents-->Functionnode
		self.add_node()
		self.vs[54]["MT_pre__attr1"] = """return attr_value == "contents" """
		self.vs[54]["MT_label__"] = """55"""
		self.vs[54]["mm__"] = """MT_pre__directLink_T"""
		self.vs[54]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.2ImplementationModuleassoc540.3.a.12Function')

		# apply association Function--body-->StatementListnode
		self.add_node()
		self.vs[55]["MT_pre__attr1"] = """return attr_value == "body" """
		self.vs[55]["MT_label__"] = """56"""
		self.vs[55]["mm__"] = """MT_pre__directLink_T"""
		self.vs[55]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.12Functionassoc550.3.a.11StatementList')

		# apply association StatementList--statements-->ExpressionStatementnode
		self.add_node()
		self.vs[56]["MT_pre__attr1"] = """return attr_value == "statements" """
		self.vs[56]["MT_label__"] = """57"""
		self.vs[56]["mm__"] = """MT_pre__directLink_T"""
		self.vs[56]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.11StatementListassoc560.3.a.10ExpressionStatement')

		# apply association ExpressionStatement--expr-->FunctionCallnode
		self.add_node()
		self.vs[57]["MT_pre__attr1"] = """return attr_value == "expr" """
		self.vs[57]["MT_label__"] = """58"""
		self.vs[57]["mm__"] = """MT_pre__directLink_T"""
		self.vs[57]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.10ExpressionStatementassoc570.3.a.9FunctionCall')

		# apply association FunctionCall--function-->FunctionPrototypenode
		self.add_node()
		self.vs[58]["MT_pre__attr1"] = """return attr_value == "function" """
		self.vs[58]["MT_label__"] = """59"""
		self.vs[58]["mm__"] = """MT_pre__directLink_T"""
		self.vs[58]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.9FunctionCallassoc580.3.a.1FunctionPrototype')

		# apply association ImplementationModule--contents-->Functionnode
		self.add_node()
		self.vs[59]["MT_pre__attr1"] = """return attr_value == "contents" """
		self.vs[59]["MT_label__"] = """60"""
		self.vs[59]["mm__"] = """MT_pre__directLink_T"""
		self.vs[59]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.2ImplementationModuleassoc590.3.a.13Function')

		# apply association ImplementationModule--contents-->Functionnode
		self.add_node()
		self.vs[60]["MT_pre__attr1"] = """return attr_value == "contents" """
		self.vs[60]["MT_label__"] = """61"""
		self.vs[60]["mm__"] = """MT_pre__directLink_T"""
		self.vs[60]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.2ImplementationModuleassoc600.3.a.16Function')

		# apply association FunctionCall--function-->FunctionPrototypenode
		self.add_node()
		self.vs[61]["MT_pre__attr1"] = """return attr_value == "function" """
		self.vs[61]["MT_label__"] = """62"""
		self.vs[61]["mm__"] = """MT_pre__directLink_T"""
		self.vs[61]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.17FunctionCallassoc610.3.a.3FunctionPrototype')

		# apply association Function--body-->StatementListnode
		self.add_node()
		self.vs[62]["MT_pre__attr1"] = """return attr_value == "body" """
		self.vs[62]["MT_label__"] = """63"""
		self.vs[62]["mm__"] = """MT_pre__directLink_T"""
		self.vs[62]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.13Functionassoc620.3.a.18StatementList')

		# apply association Function--body-->StatementListnode
		self.add_node()
		self.vs[63]["MT_pre__attr1"] = """return attr_value == "body" """
		self.vs[63]["MT_label__"] = """64"""
		self.vs[63]["mm__"] = """MT_pre__directLink_T"""
		self.vs[63]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.16Functionassoc630.3.a.15StatementList')

		# apply association StatementList--statements-->ExpressionStatementnode
		self.add_node()
		self.vs[64]["MT_pre__attr1"] = """return attr_value == "statements" """
		self.vs[64]["MT_label__"] = """65"""
		self.vs[64]["mm__"] = """MT_pre__directLink_T"""
		self.vs[64]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.15StatementListassoc640.3.a.14ExpressionStatement')

		# apply association ExpressionStatement--expr-->FunctionCallnode
		self.add_node()
		self.vs[65]["MT_pre__attr1"] = """return attr_value == "expr" """
		self.vs[65]["MT_label__"] = """66"""
		self.vs[65]["mm__"] = """MT_pre__directLink_T"""
		self.vs[65]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.14ExpressionStatementassoc650.3.a.17FunctionCall')

		# apply association StatementList--statements-->ExpressionStatementnode
		self.add_node()
		self.vs[66]["MT_pre__attr1"] = """return attr_value == "statements" """
		self.vs[66]["MT_label__"] = """67"""
		self.vs[66]["mm__"] = """MT_pre__directLink_T"""
		self.vs[66]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.18StatementListassoc660.3.a.19ExpressionStatement')

		# apply association ExpressionStatement--expr-->FunctionCallnode
		self.add_node()
		self.vs[67]["MT_pre__attr1"] = """return attr_value == "expr" """
		self.vs[67]["MT_label__"] = """68"""
		self.vs[67]["mm__"] = """MT_pre__directLink_T"""
		self.vs[67]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.19ExpressionStatementassoc670.3.a.20FunctionCall')

		# apply association ImplementationModule--contents-->FunctionPrototypenode
		self.add_node()
		self.vs[68]["MT_pre__attr1"] = """return attr_value == "contents" """
		self.vs[68]["MT_label__"] = """69"""
		self.vs[68]["mm__"] = """MT_pre__directLink_T"""
		self.vs[68]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.2ImplementationModuleassoc680.3.a.21FunctionPrototype')

		# apply association FunctionCall--function-->FunctionPrototypenode
		self.add_node()
		self.vs[69]["MT_pre__attr1"] = """return attr_value == "function" """
		self.vs[69]["MT_label__"] = """70"""
		self.vs[69]["mm__"] = """MT_pre__directLink_T"""
		self.vs[69]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.20FunctionCallassoc690.3.a.21FunctionPrototype')

		# trace association FunctionPrototype--trace-->InstanceConfigurationnode
		self.add_node()
		self.vs[70]["MT_label__"] = """71"""
		self.vs[70]["mm__"] = """MT_pre__trace_link"""
		self.vs[70]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.1FunctionPrototypeassoc700.3.m.3InstanceConfiguration')

		# trace association Function--trace-->InstanceConfigurationnode
		self.add_node()
		self.vs[71]["MT_label__"] = """72"""
		self.vs[71]["mm__"] = """MT_pre__trace_link"""
		self.vs[71]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.0Functionassoc710.3.m.3InstanceConfiguration')

		# trace association ImplementationModule--trace-->ImplementationModulenode
		self.add_node()
		self.vs[72]["MT_label__"] = """73"""
		self.vs[72]["mm__"] = """MT_pre__trace_link"""
		self.vs[72]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.2ImplementationModuleassoc720.3.m.0ImplementationModule')

		# trace association FunctionPrototype--trace-->ComponentInstancenode
		self.add_node()
		self.vs[73]["MT_label__"] = """74"""
		self.vs[73]["mm__"] = """MT_pre__trace_link"""
		self.vs[73]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.4FunctionPrototypeassoc730.3.m.2ComponentInstance')

		# trace association FunctionPrototype--trace-->Functionnode
		self.add_node()
		self.vs[74]["MT_label__"] = """75"""
		self.vs[74]["mm__"] = """MT_pre__trace_link"""
		self.vs[74]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.3FunctionPrototypeassoc740.3.m.1Function')

		# trace association Function--trace-->ComponentInstancenode
		self.add_node()
		self.vs[75]["MT_label__"] = """76"""
		self.vs[75]["mm__"] = """MT_pre__trace_link"""
		self.vs[75]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.6Functionassoc750.3.m.2ComponentInstance')

		# trace association Function--trace-->TestCasenode
		self.add_node()
		self.vs[76]["MT_label__"] = """77"""
		self.vs[76]["mm__"] = """MT_pre__trace_link"""
		self.vs[76]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.12Functionassoc760.3.m.4TestCase')

		# trace association FunctionCall--trace-->InitializeConfigurationnode
		self.add_node()
		self.vs[77]["MT_label__"] = """78"""
		self.vs[77]["mm__"] = """MT_pre__trace_link"""
		self.vs[77]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.9FunctionCallassoc770.3.m.6InitializeConfiguration')

		# trace association Function--trace-->Functionnode
		self.add_node()
		self.vs[78]["MT_label__"] = """79"""
		self.vs[78]["mm__"] = """MT_pre__trace_link"""
		self.vs[78]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.13Functionassoc780.3.m.1Function')

		# trace association Function--trace-->Functionnode
		self.add_node()
		self.vs[79]["MT_label__"] = """80"""
		self.vs[79]["mm__"] = """MT_pre__trace_link"""
		self.vs[79]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.16Functionassoc790.3.m.1Function')

		# trace association FunctionCall--trace-->TestCaseRefnode
		self.add_node()
		self.vs[80]["MT_label__"] = """81"""
		self.vs[80]["mm__"] = """MT_pre__trace_link"""
		self.vs[80]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.20FunctionCallassoc800.3.m.9TestCaseRef')

		# trace association FunctionPrototype--trace-->TestCasenode
		self.add_node()
		self.vs[81]["MT_label__"] = """82"""
		self.vs[81]["mm__"] = """MT_pre__trace_link"""
		self.vs[81]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.a.21FunctionPrototypeassoc810.3.m.4TestCase')

		self['equations'].append(((11,'name'),('concat',(('wildcard'),('constant','__init')))))
		self['equations'].append(((12,'name'),('concat',(('wildcard'),('constant','__init')))))
		self['equations'].append(((14,'name'),('concat',(('wildcard'),('constant','_blockexpr_main_2')))))
		self['equations'].append(((15,'name'),('concat',(('wildcard'),('constant','__wire')))))
		self['equations'].append(((17,'name'),('concat',(('wildcard'),('constant','__wire')))))
		self['equations'].append(((24,'name'),('concat',(('wildcard'),('constant','_blockexpr_main_2')))))
		self['equations'].append(((27,'name'),('constant','main')))

		# Add the edges
		self.add_edges([
			(3,33), # match class InstanceConfiguration(0.3.m.3InstanceConfiguration) -> association contents
			(33,2), # association ComponentInstance -> match class ComponentInstance(0.3.m.2ComponentInstance)
			(0,34), # match class ImplementationModule(0.3.m.0ImplementationModule) -> association contents
			(34,1), # association Function -> match class Function(0.3.m.1Function)
			(0,35), # match class ImplementationModule(0.3.m.0ImplementationModule) -> association contents
			(35,3), # association InstanceConfiguration -> match class InstanceConfiguration(0.3.m.3InstanceConfiguration)
			(0,36), # match class ImplementationModule(0.3.m.0ImplementationModule) -> association contents
			(36,4), # association TestCase -> match class TestCase(0.3.m.4TestCase)
			(4,37), # match class TestCase(0.3.m.4TestCase) -> association body
			(37,5), # association StatementList -> match class StatementList(0.3.m.5StatementList)
			(5,38), # match class StatementList(0.3.m.5StatementList) -> association statements
			(38,6), # association InitializeConfiguration -> match class InitializeConfiguration(0.3.m.6InitializeConfiguration)
			(6,39), # match class InitializeConfiguration(0.3.m.6InitializeConfiguration) -> association config
			(39,3), # association InstanceConfiguration -> match class InstanceConfiguration(0.3.m.3InstanceConfiguration)
			(1,40), # match class Function(0.3.m.1Function) -> association body
			(40,7), # association StatementList -> match class StatementList(0.3.m.7StatementList)
			(7,41), # match class StatementList(0.3.m.7StatementList) -> association statements
			(41,10), # association ReturnStatement -> match class ReturnStatement(0.3.m.10ReturnStatement)
			(10,42), # match class ReturnStatement(0.3.m.10ReturnStatement) -> association expression
			(42,8), # association ExecuteTestExpression -> match class ExecuteTestExpression(0.3.m.8ExecuteTestExpression)
			(8,43), # match class ExecuteTestExpression(0.3.m.8ExecuteTestExpression) -> association tests
			(43,9), # association TestCaseRef -> match class TestCaseRef(0.3.m.9TestCaseRef)
			(9,44), # match class TestCaseRef(0.3.m.9TestCaseRef) -> association testcase
			(44,4), # association TestCase -> match class TestCase(0.3.m.4TestCase)
			(13,45), # apply class ImplementationModule(0.3.a.2ImplementationModule) -> association contents
			(45,11), # association Function -> apply class Function(0.3.a.0Function)
			(13,46), # apply class ImplementationModule(0.3.a.2ImplementationModule) -> association contents
			(46,12), # association FunctionPrototype -> apply class FunctionPrototype(0.3.a.1FunctionPrototype)
			(13,47), # apply class ImplementationModule(0.3.a.2ImplementationModule) -> association contents
			(47,14), # association FunctionPrototype -> apply class FunctionPrototype(0.3.a.3FunctionPrototype)
			(16,48), # apply class StatementList(0.3.a.5StatementList) -> association statements
			(48,18), # association ExpressionStatement -> apply class ExpressionStatement(0.3.a.7ExpressionStatement)
			(13,49), # apply class ImplementationModule(0.3.a.2ImplementationModule) -> association contents
			(49,15), # association FunctionPrototype -> apply class FunctionPrototype(0.3.a.4FunctionPrototype)
			(11,50), # apply class Function(0.3.a.0Function) -> association body
			(50,16), # association StatementList -> apply class StatementList(0.3.a.5StatementList)
			(13,51), # apply class ImplementationModule(0.3.a.2ImplementationModule) -> association contents
			(51,17), # association Function -> apply class Function(0.3.a.6Function)
			(18,52), # apply class ExpressionStatement(0.3.a.7ExpressionStatement) -> association expr
			(52,19), # association FunctionCall -> apply class FunctionCall(0.3.a.8FunctionCall)
			(19,53), # apply class FunctionCall(0.3.a.8FunctionCall) -> association function
			(53,15), # association FunctionPrototype -> apply class FunctionPrototype(0.3.a.4FunctionPrototype)
			(13,54), # apply class ImplementationModule(0.3.a.2ImplementationModule) -> association contents
			(54,23), # association Function -> apply class Function(0.3.a.12Function)
			(23,55), # apply class Function(0.3.a.12Function) -> association body
			(55,22), # association StatementList -> apply class StatementList(0.3.a.11StatementList)
			(22,56), # apply class StatementList(0.3.a.11StatementList) -> association statements
			(56,21), # association ExpressionStatement -> apply class ExpressionStatement(0.3.a.10ExpressionStatement)
			(21,57), # apply class ExpressionStatement(0.3.a.10ExpressionStatement) -> association expr
			(57,20), # association FunctionCall -> apply class FunctionCall(0.3.a.9FunctionCall)
			(20,58), # apply class FunctionCall(0.3.a.9FunctionCall) -> association function
			(58,12), # association FunctionPrototype -> apply class FunctionPrototype(0.3.a.1FunctionPrototype)
			(13,59), # apply class ImplementationModule(0.3.a.2ImplementationModule) -> association contents
			(59,24), # association Function -> apply class Function(0.3.a.13Function)
			(13,60), # apply class ImplementationModule(0.3.a.2ImplementationModule) -> association contents
			(60,27), # association Function -> apply class Function(0.3.a.16Function)
			(28,61), # apply class FunctionCall(0.3.a.17FunctionCall) -> association function
			(61,14), # association FunctionPrototype -> apply class FunctionPrototype(0.3.a.3FunctionPrototype)
			(24,62), # apply class Function(0.3.a.13Function) -> association body
			(62,29), # association StatementList -> apply class StatementList(0.3.a.18StatementList)
			(27,63), # apply class Function(0.3.a.16Function) -> association body
			(63,26), # association StatementList -> apply class StatementList(0.3.a.15StatementList)
			(26,64), # apply class StatementList(0.3.a.15StatementList) -> association statements
			(64,25), # association ExpressionStatement -> apply class ExpressionStatement(0.3.a.14ExpressionStatement)
			(25,65), # apply class ExpressionStatement(0.3.a.14ExpressionStatement) -> association expr
			(65,28), # association FunctionCall -> apply class FunctionCall(0.3.a.17FunctionCall)
			(29,66), # apply class StatementList(0.3.a.18StatementList) -> association statements
			(66,30), # association ExpressionStatement -> apply class ExpressionStatement(0.3.a.19ExpressionStatement)
			(30,67), # apply class ExpressionStatement(0.3.a.19ExpressionStatement) -> association expr
			(67,31), # association FunctionCall -> apply class FunctionCall(0.3.a.20FunctionCall)
			(13,68), # apply class ImplementationModule(0.3.a.2ImplementationModule) -> association contents
			(68,32), # association FunctionPrototype -> apply class FunctionPrototype(0.3.a.21FunctionPrototype)
			(31,69), # apply class FunctionCall(0.3.a.20FunctionCall) -> association function
			(69,32), # association FunctionPrototype -> apply class FunctionPrototype(0.3.a.21FunctionPrototype)
			(12,70), # apply class FunctionPrototype(0.3.m.3InstanceConfiguration) -> backward_association 
			(70,3), # backward_associationInstanceConfiguration -> match_class InstanceConfiguration(0.3.m.3InstanceConfiguration)
			(11,71), # apply class Function(0.3.m.3InstanceConfiguration) -> backward_association 
			(71,3), # backward_associationInstanceConfiguration -> match_class InstanceConfiguration(0.3.m.3InstanceConfiguration)
			(13,72), # apply class ImplementationModule(0.3.m.0ImplementationModule) -> backward_association 
			(72,0), # backward_associationImplementationModule -> match_class ImplementationModule(0.3.m.0ImplementationModule)
			(15,73), # apply class FunctionPrototype(0.3.m.2ComponentInstance) -> backward_association 
			(73,2), # backward_associationComponentInstance -> match_class ComponentInstance(0.3.m.2ComponentInstance)
			(14,74), # apply class FunctionPrototype(0.3.m.1Function) -> backward_association 
			(74,1), # backward_associationFunction -> match_class Function(0.3.m.1Function)
			(17,75), # apply class Function(0.3.m.2ComponentInstance) -> backward_association 
			(75,2), # backward_associationComponentInstance -> match_class ComponentInstance(0.3.m.2ComponentInstance)
			(23,76), # apply class Function(0.3.m.4TestCase) -> backward_association 
			(76,4), # backward_associationTestCase -> match_class TestCase(0.3.m.4TestCase)
			(20,77), # apply class FunctionCall(0.3.m.6InitializeConfiguration) -> backward_association 
			(77,6), # backward_associationInitializeConfiguration -> match_class InitializeConfiguration(0.3.m.6InitializeConfiguration)
			(24,78), # apply class Function(0.3.m.1Function) -> backward_association 
			(78,1), # backward_associationFunction -> match_class Function(0.3.m.1Function)
			(27,79), # apply class Function(0.3.m.1Function) -> backward_association 
			(79,1), # backward_associationFunction -> match_class Function(0.3.m.1Function)
			(31,80), # apply class FunctionCall(0.3.m.9TestCaseRef) -> backward_association 
			(80,9), # backward_associationTestCaseRef -> match_class TestCaseRef(0.3.m.9TestCaseRef)
			(32,81), # apply class FunctionPrototype(0.3.m.4TestCase) -> backward_association 
			(81,4), # backward_associationTestCase -> match_class TestCase(0.3.m.4TestCase)
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

	def eval_attr110(self, attr_value, this):
		return True

	def eval_attr111(self, attr_value, this):
		return True

	# define evaluation methods for each apply class.

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

	def eval_attr127(self, attr_value, this):
		return True

	def eval_attr128(self, attr_value, this):
		return True

	def eval_attr129(self, attr_value, this):
		return True

	def eval_attr130(self, attr_value, this):
		return True

	def eval_attr131(self, attr_value, this):
		return True

	def eval_attr132(self, attr_value, this):
		return True

	def eval_attr133(self, attr_value, this):
		return True

		# define evaluation methods for each match association.

	def eval_attr134(self, attr_value, this):
		return attr_value == "contents"
	def eval_attr135(self, attr_value, this):
		return attr_value == "contents"
	def eval_attr136(self, attr_value, this):
		return attr_value == "contents"
	def eval_attr137(self, attr_value, this):
		return attr_value == "contents"
	def eval_attr138(self, attr_value, this):
		return attr_value == "body"
	def eval_attr139(self, attr_value, this):
		return attr_value == "statements"
	def eval_attr140(self, attr_value, this):
		return attr_value == "config"
	def eval_attr141(self, attr_value, this):
		return attr_value == "body"
	def eval_attr142(self, attr_value, this):
		return attr_value == "statements"
	def eval_attr143(self, attr_value, this):
		return attr_value == "expression"
	def eval_attr144(self, attr_value, this):
		return attr_value == "tests"
	def eval_attr145(self, attr_value, this):
		return attr_value == "testcase"
		# define evaluation methods for each apply association.

	def eval_attr146(self, attr_value, this):
		return attr_value == "contents"
	def eval_attr147(self, attr_value, this):
		return attr_value == "contents"
	def eval_attr148(self, attr_value, this):
		return attr_value == "contents"
	def eval_attr149(self, attr_value, this):
		return attr_value == "statements"
	def eval_attr150(self, attr_value, this):
		return attr_value == "contents"
	def eval_attr151(self, attr_value, this):
		return attr_value == "body"
	def eval_attr152(self, attr_value, this):
		return attr_value == "contents"
	def eval_attr153(self, attr_value, this):
		return attr_value == "expr"
	def eval_attr154(self, attr_value, this):
		return attr_value == "function"
	def eval_attr155(self, attr_value, this):
		return attr_value == "contents"
	def eval_attr156(self, attr_value, this):
		return attr_value == "body"
	def eval_attr157(self, attr_value, this):
		return attr_value == "statements"
	def eval_attr158(self, attr_value, this):
		return attr_value == "expr"
	def eval_attr159(self, attr_value, this):
		return attr_value == "function"
	def eval_attr160(self, attr_value, this):
		return attr_value == "contents"
	def eval_attr161(self, attr_value, this):
		return attr_value == "contents"
	def eval_attr162(self, attr_value, this):
		return attr_value == "function"
	def eval_attr163(self, attr_value, this):
		return attr_value == "body"
	def eval_attr164(self, attr_value, this):
		return attr_value == "body"
	def eval_attr165(self, attr_value, this):
		return attr_value == "statements"
	def eval_attr166(self, attr_value, this):
		return attr_value == "expr"
	def eval_attr167(self, attr_value, this):
		return attr_value == "statements"
	def eval_attr168(self, attr_value, this):
		return attr_value == "expr"
	def eval_attr169(self, attr_value, this):
		return attr_value == "contents"
	def eval_attr170(self, attr_value, this):
		return attr_value == "function"

	def constraint(self, PreNode, graph):
		return True

