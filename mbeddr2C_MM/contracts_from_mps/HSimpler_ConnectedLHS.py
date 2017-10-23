from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HSimpler_ConnectedLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HSimpler_ConnectedLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HSimpler_ConnectedLHS, self).__init__(name='HSimpler_ConnectedLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HSimpler_ConnectedLHS')
		self["equations"] = []
		# Set the node attributes

		# match class ImplementationModule(0.4.m.0ImplementationModule) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__ImplementationModule"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.4.m.0ImplementationModule')

		# match class Function(0.4.m.1Function) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__Function"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.4.m.1Function')

		# match class ComponentInstance(0.4.m.2ComponentInstance) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__ComponentInstance"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.4.m.2ComponentInstance')

		# match class InstanceConfiguration(0.4.m.3InstanceConfiguration) node
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return True"""
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__InstanceConfiguration"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.4.m.3InstanceConfiguration')

		# match class TestCase(0.4.m.4TestCase) node
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return True"""
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__TestCase"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.4.m.4TestCase')

		# match class StatementList(0.4.m.5StatementList) node
		self.add_node()
		self.vs[5]["MT_pre__attr1"] = """return True"""
		self.vs[5]["MT_label__"] = """6"""
		self.vs[5]["mm__"] = """MT_pre__StatementList"""
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.4.m.5StatementList')

		# match class InitializeConfiguration(0.4.m.6InitializeConfiguration) node
		self.add_node()
		self.vs[6]["MT_pre__attr1"] = """return True"""
		self.vs[6]["MT_label__"] = """7"""
		self.vs[6]["mm__"] = """MT_pre__InitializeConfiguration"""
		self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.4.m.6InitializeConfiguration')


		# match association InstanceConfiguration--contents-->ComponentInstancenode
		self.add_node()
		self.vs[7]["MT_pre__attr1"] = """return attr_value == "contents" """
		self.vs[7]["MT_label__"] = """8"""
		self.vs[7]["mm__"] = """MT_pre__directLink_S"""
		self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.4.m.3InstanceConfigurationassoc70.4.m.2ComponentInstance')

		# match association ImplementationModule--contents-->Functionnode
		self.add_node()
		self.vs[8]["MT_pre__attr1"] = """return attr_value == "contents" """
		self.vs[8]["MT_label__"] = """9"""
		self.vs[8]["mm__"] = """MT_pre__directLink_S"""
		self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.4.m.0ImplementationModuleassoc80.4.m.1Function')

		# match association ImplementationModule--contents-->InstanceConfigurationnode
		self.add_node()
		self.vs[9]["MT_pre__attr1"] = """return attr_value == "contents" """
		self.vs[9]["MT_label__"] = """10"""
		self.vs[9]["mm__"] = """MT_pre__directLink_S"""
		self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.4.m.0ImplementationModuleassoc90.4.m.3InstanceConfiguration')

		# match association ImplementationModule--contents-->TestCasenode
		self.add_node()
		self.vs[10]["MT_pre__attr1"] = """return attr_value == "contents" """
		self.vs[10]["MT_label__"] = """11"""
		self.vs[10]["mm__"] = """MT_pre__directLink_S"""
		self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.4.m.0ImplementationModuleassoc100.4.m.4TestCase')

		# match association TestCase--body-->StatementListnode
		self.add_node()
		self.vs[11]["MT_pre__attr1"] = """return attr_value == "body" """
		self.vs[11]["MT_label__"] = """12"""
		self.vs[11]["mm__"] = """MT_pre__directLink_S"""
		self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.4.m.4TestCaseassoc110.4.m.5StatementList')

		# match association StatementList--statements-->InitializeConfigurationnode
		self.add_node()
		self.vs[12]["MT_pre__attr1"] = """return attr_value == "statements" """
		self.vs[12]["MT_label__"] = """13"""
		self.vs[12]["mm__"] = """MT_pre__directLink_S"""
		self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.4.m.5StatementListassoc120.4.m.6InitializeConfiguration')

		# match association InitializeConfiguration--config-->InstanceConfigurationnode
		self.add_node()
		self.vs[13]["MT_pre__attr1"] = """return attr_value == "config" """
		self.vs[13]["MT_label__"] = """14"""
		self.vs[13]["mm__"] = """MT_pre__directLink_S"""
		self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.4.m.6InitializeConfigurationassoc130.4.m.3InstanceConfiguration')

		# Add the edges
		self.add_edges([
			(3,7), # match class InstanceConfiguration(0.4.m.3InstanceConfiguration) -> association contents
			(7,2), # association ComponentInstance -> match class ComponentInstance(0.4.m.2ComponentInstance)
			(0,8), # match class ImplementationModule(0.4.m.0ImplementationModule) -> association contents
			(8,1), # association Function -> match class Function(0.4.m.1Function)
			(0,9), # match class ImplementationModule(0.4.m.0ImplementationModule) -> association contents
			(9,3), # association InstanceConfiguration -> match class InstanceConfiguration(0.4.m.3InstanceConfiguration)
			(0,10), # match class ImplementationModule(0.4.m.0ImplementationModule) -> association contents
			(10,4), # association TestCase -> match class TestCase(0.4.m.4TestCase)
			(4,11), # match class TestCase(0.4.m.4TestCase) -> association body
			(11,5), # association StatementList -> match class StatementList(0.4.m.5StatementList)
			(5,12), # match class StatementList(0.4.m.5StatementList) -> association statements
			(12,6), # association InitializeConfiguration -> match class InitializeConfiguration(0.4.m.6InitializeConfiguration)
			(6,13), # match class InitializeConfiguration(0.4.m.6InitializeConfiguration) -> association config
			(13,3), # association InstanceConfiguration -> match class InstanceConfiguration(0.4.m.3InstanceConfiguration)
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

	# define evaluation methods for each match association.

	def eval_attr18(self, attr_value, this):
		return attr_value == "contents"
	def eval_attr19(self, attr_value, this):
		return attr_value == "contents"
	def eval_attr110(self, attr_value, this):
		return attr_value == "contents"
	def eval_attr111(self, attr_value, this):
		return attr_value == "contents"
	def eval_attr112(self, attr_value, this):
		return attr_value == "body"
	def eval_attr113(self, attr_value, this):
		return attr_value == "statements"
	def eval_attr114(self, attr_value, this):
		return attr_value == "config"

	def constraint(self, PreNode, graph):
		return True

