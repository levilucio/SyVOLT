from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HAssignmentInstance2_ConnectedLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HAssignmentInstance2_ConnectedLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HAssignmentInstance2_ConnectedLHS, self).__init__(name='HAssignmentInstance2_ConnectedLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HAssignmentInstance2_ConnectedLHS')
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


		# match association InstanceConfiguration--contents-->ComponentInstancenode
		self.add_node()
		self.vs[11]["MT_pre__attr1"] = """return attr_value == "contents" """
		self.vs[11]["MT_label__"] = """12"""
		self.vs[11]["mm__"] = """MT_pre__directLink_S"""
		self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.3InstanceConfigurationassoc110.3.m.2ComponentInstance')

		# match association ImplementationModule--contents-->Functionnode
		self.add_node()
		self.vs[12]["MT_pre__attr1"] = """return attr_value == "contents" """
		self.vs[12]["MT_label__"] = """13"""
		self.vs[12]["mm__"] = """MT_pre__directLink_S"""
		self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.0ImplementationModuleassoc120.3.m.1Function')

		# match association ImplementationModule--contents-->InstanceConfigurationnode
		self.add_node()
		self.vs[13]["MT_pre__attr1"] = """return attr_value == "contents" """
		self.vs[13]["MT_label__"] = """14"""
		self.vs[13]["mm__"] = """MT_pre__directLink_S"""
		self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.0ImplementationModuleassoc130.3.m.3InstanceConfiguration')

		# match association ImplementationModule--contents-->TestCasenode
		self.add_node()
		self.vs[14]["MT_pre__attr1"] = """return attr_value == "contents" """
		self.vs[14]["MT_label__"] = """15"""
		self.vs[14]["mm__"] = """MT_pre__directLink_S"""
		self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.0ImplementationModuleassoc140.3.m.4TestCase')

		# match association TestCase--body-->StatementListnode
		self.add_node()
		self.vs[15]["MT_pre__attr1"] = """return attr_value == "body" """
		self.vs[15]["MT_label__"] = """16"""
		self.vs[15]["mm__"] = """MT_pre__directLink_S"""
		self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.4TestCaseassoc150.3.m.5StatementList')

		# match association StatementList--statements-->InitializeConfigurationnode
		self.add_node()
		self.vs[16]["MT_pre__attr1"] = """return attr_value == "statements" """
		self.vs[16]["MT_label__"] = """17"""
		self.vs[16]["mm__"] = """MT_pre__directLink_S"""
		self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.5StatementListassoc160.3.m.6InitializeConfiguration')

		# match association InitializeConfiguration--config-->InstanceConfigurationnode
		self.add_node()
		self.vs[17]["MT_pre__attr1"] = """return attr_value == "config" """
		self.vs[17]["MT_label__"] = """18"""
		self.vs[17]["mm__"] = """MT_pre__directLink_S"""
		self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.6InitializeConfigurationassoc170.3.m.3InstanceConfiguration')

		# match association Function--body-->StatementListnode
		self.add_node()
		self.vs[18]["MT_pre__attr1"] = """return attr_value == "body" """
		self.vs[18]["MT_label__"] = """19"""
		self.vs[18]["mm__"] = """MT_pre__directLink_S"""
		self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.1Functionassoc180.3.m.7StatementList')

		# match association StatementList--statements-->ReturnStatementnode
		self.add_node()
		self.vs[19]["MT_pre__attr1"] = """return attr_value == "statements" """
		self.vs[19]["MT_label__"] = """20"""
		self.vs[19]["mm__"] = """MT_pre__directLink_S"""
		self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.7StatementListassoc190.3.m.10ReturnStatement')

		# match association ReturnStatement--expression-->ExecuteTestExpressionnode
		self.add_node()
		self.vs[20]["MT_pre__attr1"] = """return attr_value == "expression" """
		self.vs[20]["MT_label__"] = """21"""
		self.vs[20]["mm__"] = """MT_pre__directLink_S"""
		self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.10ReturnStatementassoc200.3.m.8ExecuteTestExpression')

		# match association ExecuteTestExpression--tests-->TestCaseRefnode
		self.add_node()
		self.vs[21]["MT_pre__attr1"] = """return attr_value == "tests" """
		self.vs[21]["MT_label__"] = """22"""
		self.vs[21]["mm__"] = """MT_pre__directLink_S"""
		self.vs[21]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.8ExecuteTestExpressionassoc210.3.m.9TestCaseRef')

		# match association TestCaseRef--testcase-->TestCasenode
		self.add_node()
		self.vs[22]["MT_pre__attr1"] = """return attr_value == "testcase" """
		self.vs[22]["MT_label__"] = """23"""
		self.vs[22]["mm__"] = """MT_pre__directLink_S"""
		self.vs[22]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.9TestCaseRefassoc220.3.m.4TestCase')

		# Add the edges
		self.add_edges([
			(3,11), # match class InstanceConfiguration(0.3.m.3InstanceConfiguration) -> association contents
			(11,2), # association ComponentInstance -> match class ComponentInstance(0.3.m.2ComponentInstance)
			(0,12), # match class ImplementationModule(0.3.m.0ImplementationModule) -> association contents
			(12,1), # association Function -> match class Function(0.3.m.1Function)
			(0,13), # match class ImplementationModule(0.3.m.0ImplementationModule) -> association contents
			(13,3), # association InstanceConfiguration -> match class InstanceConfiguration(0.3.m.3InstanceConfiguration)
			(0,14), # match class ImplementationModule(0.3.m.0ImplementationModule) -> association contents
			(14,4), # association TestCase -> match class TestCase(0.3.m.4TestCase)
			(4,15), # match class TestCase(0.3.m.4TestCase) -> association body
			(15,5), # association StatementList -> match class StatementList(0.3.m.5StatementList)
			(5,16), # match class StatementList(0.3.m.5StatementList) -> association statements
			(16,6), # association InitializeConfiguration -> match class InitializeConfiguration(0.3.m.6InitializeConfiguration)
			(6,17), # match class InitializeConfiguration(0.3.m.6InitializeConfiguration) -> association config
			(17,3), # association InstanceConfiguration -> match class InstanceConfiguration(0.3.m.3InstanceConfiguration)
			(1,18), # match class Function(0.3.m.1Function) -> association body
			(18,7), # association StatementList -> match class StatementList(0.3.m.7StatementList)
			(7,19), # match class StatementList(0.3.m.7StatementList) -> association statements
			(19,10), # association ReturnStatement -> match class ReturnStatement(0.3.m.10ReturnStatement)
			(10,20), # match class ReturnStatement(0.3.m.10ReturnStatement) -> association expression
			(20,8), # association ExecuteTestExpression -> match class ExecuteTestExpression(0.3.m.8ExecuteTestExpression)
			(8,21), # match class ExecuteTestExpression(0.3.m.8ExecuteTestExpression) -> association tests
			(21,9), # association TestCaseRef -> match class TestCaseRef(0.3.m.9TestCaseRef)
			(9,22), # match class TestCaseRef(0.3.m.9TestCaseRef) -> association testcase
			(22,4), # association TestCase -> match class TestCase(0.3.m.4TestCase)
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

	# define evaluation methods for each match association.

	def eval_attr112(self, attr_value, this):
		return attr_value == "contents"
	def eval_attr113(self, attr_value, this):
		return attr_value == "contents"
	def eval_attr114(self, attr_value, this):
		return attr_value == "contents"
	def eval_attr115(self, attr_value, this):
		return attr_value == "contents"
	def eval_attr116(self, attr_value, this):
		return attr_value == "body"
	def eval_attr117(self, attr_value, this):
		return attr_value == "statements"
	def eval_attr118(self, attr_value, this):
		return attr_value == "config"
	def eval_attr119(self, attr_value, this):
		return attr_value == "body"
	def eval_attr120(self, attr_value, this):
		return attr_value == "statements"
	def eval_attr121(self, attr_value, this):
		return attr_value == "expression"
	def eval_attr122(self, attr_value, this):
		return attr_value == "tests"
	def eval_attr123(self, attr_value, this):
		return attr_value == "testcase"

	def constraint(self, PreNode, graph):
		return True

