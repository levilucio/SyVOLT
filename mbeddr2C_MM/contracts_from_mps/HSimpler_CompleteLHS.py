from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HSimpler_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HSimpler_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HSimpler_CompleteLHS, self).__init__(name='HSimpler_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HSimpler_CompleteLHS')
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

		# apply class Function(0.4.a.0Function) node
		self.add_node()
		self.vs[7]["MT_pre__attr1"] = """return True"""
		self.vs[7]["MT_label__"] = """8"""
		self.vs[7]["mm__"] = """MT_pre__Function"""
		self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.4.a.0Function')

		# apply class FunctionPrototype(0.4.a.1FunctionPrototype) node
		self.add_node()
		self.vs[8]["MT_pre__attr1"] = """return True"""
		self.vs[8]["MT_label__"] = """9"""
		self.vs[8]["mm__"] = """MT_pre__FunctionPrototype"""
		self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.4.a.1FunctionPrototype')

		# apply class ImplementationModule(0.4.a.2ImplementationModule) node
		self.add_node()
		self.vs[9]["MT_pre__attr1"] = """return True"""
		self.vs[9]["MT_label__"] = """10"""
		self.vs[9]["mm__"] = """MT_pre__ImplementationModule"""
		self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.4.a.2ImplementationModule')

		# apply class FunctionPrototype(0.4.a.3FunctionPrototype) node
		self.add_node()
		self.vs[10]["MT_pre__attr1"] = """return True"""
		self.vs[10]["MT_label__"] = """11"""
		self.vs[10]["mm__"] = """MT_pre__FunctionPrototype"""
		self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.4.a.3FunctionPrototype')

		# apply class FunctionPrototype(0.4.a.4FunctionPrototype) node
		self.add_node()
		self.vs[11]["MT_pre__attr1"] = """return True"""
		self.vs[11]["MT_label__"] = """12"""
		self.vs[11]["mm__"] = """MT_pre__FunctionPrototype"""
		self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.4.a.4FunctionPrototype')

		# apply class StatementList(0.4.a.5StatementList) node
		self.add_node()
		self.vs[12]["MT_pre__attr1"] = """return True"""
		self.vs[12]["MT_label__"] = """13"""
		self.vs[12]["mm__"] = """MT_pre__StatementList"""
		self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.4.a.5StatementList')

		# apply class Function(0.4.a.6Function) node
		self.add_node()
		self.vs[13]["MT_pre__attr1"] = """return True"""
		self.vs[13]["MT_label__"] = """14"""
		self.vs[13]["mm__"] = """MT_pre__Function"""
		self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.4.a.6Function')

		# apply class FunctionCall(0.4.a.7FunctionCall) node
		self.add_node()
		self.vs[14]["MT_pre__attr1"] = """return True"""
		self.vs[14]["MT_label__"] = """15"""
		self.vs[14]["mm__"] = """MT_pre__FunctionCall"""
		self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.4.a.7FunctionCall')

		# match association InstanceConfiguration--contents-->ComponentInstancenode
		self.add_node()
		self.vs[15]["MT_pre__attr1"] = """return attr_value == "contents" """
		self.vs[15]["MT_label__"] = """16"""
		self.vs[15]["mm__"] = """MT_pre__directLink_S"""
		self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.4.m.3InstanceConfigurationassoc150.4.m.2ComponentInstance')

		# match association ImplementationModule--contents-->Functionnode
		self.add_node()
		self.vs[16]["MT_pre__attr1"] = """return attr_value == "contents" """
		self.vs[16]["MT_label__"] = """17"""
		self.vs[16]["mm__"] = """MT_pre__directLink_S"""
		self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.4.m.0ImplementationModuleassoc160.4.m.1Function')

		# match association ImplementationModule--contents-->InstanceConfigurationnode
		self.add_node()
		self.vs[17]["MT_pre__attr1"] = """return attr_value == "contents" """
		self.vs[17]["MT_label__"] = """18"""
		self.vs[17]["mm__"] = """MT_pre__directLink_S"""
		self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.4.m.0ImplementationModuleassoc170.4.m.3InstanceConfiguration')

		# match association ImplementationModule--contents-->TestCasenode
		self.add_node()
		self.vs[18]["MT_pre__attr1"] = """return attr_value == "contents" """
		self.vs[18]["MT_label__"] = """19"""
		self.vs[18]["mm__"] = """MT_pre__directLink_S"""
		self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.4.m.0ImplementationModuleassoc180.4.m.4TestCase')

		# match association TestCase--body-->StatementListnode
		self.add_node()
		self.vs[19]["MT_pre__attr1"] = """return attr_value == "body" """
		self.vs[19]["MT_label__"] = """20"""
		self.vs[19]["mm__"] = """MT_pre__directLink_S"""
		self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.4.m.4TestCaseassoc190.4.m.5StatementList')

		# match association StatementList--statements-->InitializeConfigurationnode
		self.add_node()
		self.vs[20]["MT_pre__attr1"] = """return attr_value == "statements" """
		self.vs[20]["MT_label__"] = """21"""
		self.vs[20]["mm__"] = """MT_pre__directLink_S"""
		self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.4.m.5StatementListassoc200.4.m.6InitializeConfiguration')

		# match association InitializeConfiguration--config-->InstanceConfigurationnode
		self.add_node()
		self.vs[21]["MT_pre__attr1"] = """return attr_value == "config" """
		self.vs[21]["MT_label__"] = """22"""
		self.vs[21]["mm__"] = """MT_pre__directLink_S"""
		self.vs[21]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.4.m.6InitializeConfigurationassoc210.4.m.3InstanceConfiguration')

		# apply association ImplementationModule--contents-->Functionnode
		self.add_node()
		self.vs[22]["MT_pre__attr1"] = """return attr_value == "contents" """
		self.vs[22]["MT_label__"] = """23"""
		self.vs[22]["mm__"] = """MT_pre__directLink_T"""
		self.vs[22]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.4.a.2ImplementationModuleassoc220.4.a.0Function')

		# apply association ImplementationModule--contents-->FunctionPrototypenode
		self.add_node()
		self.vs[23]["MT_pre__attr1"] = """return attr_value == "contents" """
		self.vs[23]["MT_label__"] = """24"""
		self.vs[23]["mm__"] = """MT_pre__directLink_T"""
		self.vs[23]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.4.a.2ImplementationModuleassoc230.4.a.1FunctionPrototype')

		# apply association ImplementationModule--contents-->FunctionPrototypenode
		self.add_node()
		self.vs[24]["MT_pre__attr1"] = """return attr_value == "contents" """
		self.vs[24]["MT_label__"] = """25"""
		self.vs[24]["mm__"] = """MT_pre__directLink_T"""
		self.vs[24]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.4.a.2ImplementationModuleassoc240.4.a.3FunctionPrototype')

		# apply association ImplementationModule--contents-->FunctionPrototypenode
		self.add_node()
		self.vs[25]["MT_pre__attr1"] = """return attr_value == "contents" """
		self.vs[25]["MT_label__"] = """26"""
		self.vs[25]["mm__"] = """MT_pre__directLink_T"""
		self.vs[25]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.4.a.2ImplementationModuleassoc250.4.a.4FunctionPrototype')

		# apply association Function--body-->StatementListnode
		self.add_node()
		self.vs[26]["MT_pre__attr1"] = """return attr_value == "body" """
		self.vs[26]["MT_label__"] = """27"""
		self.vs[26]["mm__"] = """MT_pre__directLink_T"""
		self.vs[26]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.4.a.0Functionassoc260.4.a.5StatementList')

		# apply association ImplementationModule--contents-->Functionnode
		self.add_node()
		self.vs[27]["MT_pre__attr1"] = """return attr_value == "contents" """
		self.vs[27]["MT_label__"] = """28"""
		self.vs[27]["mm__"] = """MT_pre__directLink_T"""
		self.vs[27]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.4.a.2ImplementationModuleassoc270.4.a.6Function')

		# apply association FunctionCall--function-->FunctionPrototypenode
		self.add_node()
		self.vs[28]["MT_pre__attr1"] = """return attr_value == "function" """
		self.vs[28]["MT_label__"] = """29"""
		self.vs[28]["mm__"] = """MT_pre__directLink_T"""
		self.vs[28]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.4.a.7FunctionCallassoc280.4.a.1FunctionPrototype')

		# trace association FunctionPrototype--trace-->InstanceConfigurationnode
		self.add_node()
		self.vs[29]["MT_label__"] = """30"""
		self.vs[29]["mm__"] = """MT_pre__trace_link"""
		self.vs[29]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.4.a.1FunctionPrototypeassoc290.4.m.3InstanceConfiguration')

		# trace association Function--trace-->InstanceConfigurationnode
		self.add_node()
		self.vs[30]["MT_label__"] = """31"""
		self.vs[30]["mm__"] = """MT_pre__trace_link"""
		self.vs[30]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.4.a.0Functionassoc300.4.m.3InstanceConfiguration')

		# trace association ImplementationModule--trace-->ImplementationModulenode
		self.add_node()
		self.vs[31]["MT_label__"] = """32"""
		self.vs[31]["mm__"] = """MT_pre__trace_link"""
		self.vs[31]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.4.a.2ImplementationModuleassoc310.4.m.0ImplementationModule')

		# trace association FunctionPrototype--trace-->ComponentInstancenode
		self.add_node()
		self.vs[32]["MT_label__"] = """33"""
		self.vs[32]["mm__"] = """MT_pre__trace_link"""
		self.vs[32]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.4.a.4FunctionPrototypeassoc320.4.m.2ComponentInstance')

		# trace association FunctionPrototype--trace-->Functionnode
		self.add_node()
		self.vs[33]["MT_label__"] = """34"""
		self.vs[33]["mm__"] = """MT_pre__trace_link"""
		self.vs[33]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.4.a.3FunctionPrototypeassoc330.4.m.1Function')

		# trace association Function--trace-->ComponentInstancenode
		self.add_node()
		self.vs[34]["MT_label__"] = """35"""
		self.vs[34]["mm__"] = """MT_pre__trace_link"""
		self.vs[34]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.4.a.6Functionassoc340.4.m.2ComponentInstance')

		# trace association FunctionCall--trace-->InitializeConfigurationnode
		self.add_node()
		self.vs[35]["MT_label__"] = """36"""
		self.vs[35]["mm__"] = """MT_pre__trace_link"""
		self.vs[35]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.4.a.7FunctionCallassoc350.4.m.6InitializeConfiguration')

		self['equations'].append(((7,'name'),('concat',(('wildcard'),('constant','__init')))))
		self['equations'].append(((8,'name'),('concat',(('wildcard'),('constant','__init')))))
		self['equations'].append(((10,'name'),('concat',(('wildcard'),('constant','_blockexpr_main_2')))))
		self['equations'].append(((11,'name'),('concat',(('wildcard'),('constant','__wire')))))
		self['equations'].append(((13,'name'),('concat',(('wildcard'),('constant','__wire')))))

		# Add the edges
		self.add_edges([
			(3,15), # match class InstanceConfiguration(0.4.m.3InstanceConfiguration) -> association contents
			(15,2), # association ComponentInstance -> match class ComponentInstance(0.4.m.2ComponentInstance)
			(0,16), # match class ImplementationModule(0.4.m.0ImplementationModule) -> association contents
			(16,1), # association Function -> match class Function(0.4.m.1Function)
			(0,17), # match class ImplementationModule(0.4.m.0ImplementationModule) -> association contents
			(17,3), # association InstanceConfiguration -> match class InstanceConfiguration(0.4.m.3InstanceConfiguration)
			(0,18), # match class ImplementationModule(0.4.m.0ImplementationModule) -> association contents
			(18,4), # association TestCase -> match class TestCase(0.4.m.4TestCase)
			(4,19), # match class TestCase(0.4.m.4TestCase) -> association body
			(19,5), # association StatementList -> match class StatementList(0.4.m.5StatementList)
			(5,20), # match class StatementList(0.4.m.5StatementList) -> association statements
			(20,6), # association InitializeConfiguration -> match class InitializeConfiguration(0.4.m.6InitializeConfiguration)
			(6,21), # match class InitializeConfiguration(0.4.m.6InitializeConfiguration) -> association config
			(21,3), # association InstanceConfiguration -> match class InstanceConfiguration(0.4.m.3InstanceConfiguration)
			(9,22), # apply class ImplementationModule(0.4.a.2ImplementationModule) -> association contents
			(22,7), # association Function -> apply class Function(0.4.a.0Function)
			(9,23), # apply class ImplementationModule(0.4.a.2ImplementationModule) -> association contents
			(23,8), # association FunctionPrototype -> apply class FunctionPrototype(0.4.a.1FunctionPrototype)
			(9,24), # apply class ImplementationModule(0.4.a.2ImplementationModule) -> association contents
			(24,10), # association FunctionPrototype -> apply class FunctionPrototype(0.4.a.3FunctionPrototype)
			(9,25), # apply class ImplementationModule(0.4.a.2ImplementationModule) -> association contents
			(25,11), # association FunctionPrototype -> apply class FunctionPrototype(0.4.a.4FunctionPrototype)
			(7,26), # apply class Function(0.4.a.0Function) -> association body
			(26,12), # association StatementList -> apply class StatementList(0.4.a.5StatementList)
			(9,27), # apply class ImplementationModule(0.4.a.2ImplementationModule) -> association contents
			(27,13), # association Function -> apply class Function(0.4.a.6Function)
			(14,28), # apply class FunctionCall(0.4.a.7FunctionCall) -> association function
			(28,8), # association FunctionPrototype -> apply class FunctionPrototype(0.4.a.1FunctionPrototype)
			(8,29), # apply class FunctionPrototype(0.4.m.3InstanceConfiguration) -> backward_association 
			(29,3), # backward_associationInstanceConfiguration -> match_class InstanceConfiguration(0.4.m.3InstanceConfiguration)
			(7,30), # apply class Function(0.4.m.3InstanceConfiguration) -> backward_association 
			(30,3), # backward_associationInstanceConfiguration -> match_class InstanceConfiguration(0.4.m.3InstanceConfiguration)
			(9,31), # apply class ImplementationModule(0.4.m.0ImplementationModule) -> backward_association 
			(31,0), # backward_associationImplementationModule -> match_class ImplementationModule(0.4.m.0ImplementationModule)
			(11,32), # apply class FunctionPrototype(0.4.m.2ComponentInstance) -> backward_association 
			(32,2), # backward_associationComponentInstance -> match_class ComponentInstance(0.4.m.2ComponentInstance)
			(10,33), # apply class FunctionPrototype(0.4.m.1Function) -> backward_association 
			(33,1), # backward_associationFunction -> match_class Function(0.4.m.1Function)
			(13,34), # apply class Function(0.4.m.2ComponentInstance) -> backward_association 
			(34,2), # backward_associationComponentInstance -> match_class ComponentInstance(0.4.m.2ComponentInstance)
			(14,35), # apply class FunctionCall(0.4.m.6InitializeConfiguration) -> backward_association 
			(35,6), # backward_associationInitializeConfiguration -> match_class InitializeConfiguration(0.4.m.6InitializeConfiguration)
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

	# define evaluation methods for each apply class.

	def eval_attr18(self, attr_value, this):
		return True

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

		# define evaluation methods for each match association.

	def eval_attr116(self, attr_value, this):
		return attr_value == "contents"
	def eval_attr117(self, attr_value, this):
		return attr_value == "contents"
	def eval_attr118(self, attr_value, this):
		return attr_value == "contents"
	def eval_attr119(self, attr_value, this):
		return attr_value == "contents"
	def eval_attr120(self, attr_value, this):
		return attr_value == "body"
	def eval_attr121(self, attr_value, this):
		return attr_value == "statements"
	def eval_attr122(self, attr_value, this):
		return attr_value == "config"
		# define evaluation methods for each apply association.

	def eval_attr123(self, attr_value, this):
		return attr_value == "contents"
	def eval_attr124(self, attr_value, this):
		return attr_value == "contents"
	def eval_attr125(self, attr_value, this):
		return attr_value == "contents"
	def eval_attr126(self, attr_value, this):
		return attr_value == "contents"
	def eval_attr127(self, attr_value, this):
		return attr_value == "body"
	def eval_attr128(self, attr_value, this):
		return attr_value == "contents"
	def eval_attr129(self, attr_value, this):
		return attr_value == "function"

	def constraint(self, PreNode, graph):
		return True

