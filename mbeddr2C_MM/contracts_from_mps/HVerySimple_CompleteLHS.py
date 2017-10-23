from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HVerySimple_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HVerySimple_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HVerySimple_CompleteLHS, self).__init__(name='HVerySimple_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HVerySimple_CompleteLHS')
		self["equations"] = []
		# Set the node attributes

		# match class ComponentInstance(0.5.m.0ComponentInstance) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__ComponentInstance"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.5.m.0ComponentInstance')

		# match class InstanceConfiguration(0.5.m.1InstanceConfiguration) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__InstanceConfiguration"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.5.m.1InstanceConfiguration')

		# apply class Function(0.5.a.0Function) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__Function"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.5.a.0Function')

		# apply class FunctionPrototype(0.5.a.1FunctionPrototype) node
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return True"""
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__FunctionPrototype"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.5.a.1FunctionPrototype')

		# apply class FunctionPrototype(0.5.a.2FunctionPrototype) node
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return True"""
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__FunctionPrototype"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.5.a.2FunctionPrototype')

		# match association InstanceConfiguration--contents-->ComponentInstancenode
		self.add_node()
		self.vs[5]["MT_pre__attr1"] = """return attr_value == "contents" """
		self.vs[5]["MT_label__"] = """6"""
		self.vs[5]["mm__"] = """MT_pre__directLink_S"""
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.5.m.1InstanceConfigurationassoc50.5.m.0ComponentInstance')

		# trace association FunctionPrototype--trace-->InstanceConfigurationnode
		self.add_node()
		self.vs[6]["MT_label__"] = """7"""
		self.vs[6]["mm__"] = """MT_pre__trace_link"""
		self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.5.a.1FunctionPrototypeassoc60.5.m.1InstanceConfiguration')

		# trace association Function--trace-->InstanceConfigurationnode
		self.add_node()
		self.vs[7]["MT_label__"] = """8"""
		self.vs[7]["mm__"] = """MT_pre__trace_link"""
		self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.5.a.0Functionassoc70.5.m.1InstanceConfiguration')

		# trace association FunctionPrototype--trace-->ComponentInstancenode
		self.add_node()
		self.vs[8]["MT_label__"] = """9"""
		self.vs[8]["mm__"] = """MT_pre__trace_link"""
		self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.5.a.2FunctionPrototypeassoc80.5.m.0ComponentInstance')

		self['equations'].append(((2,'name'),('concat',(('wildcard'),('constant','__init')))))
		self['equations'].append(((3,'name'),('concat',(('wildcard'),('constant','__init')))))
		self['equations'].append(((4,'name'),('concat',(('wildcard'),('constant','__wire')))))

		# Add the edges
		self.add_edges([
			(1,5), # match class InstanceConfiguration(0.5.m.1InstanceConfiguration) -> association contents
			(5,0), # association ComponentInstance -> match class ComponentInstance(0.5.m.0ComponentInstance)
			(3,6), # apply class FunctionPrototype(0.5.m.1InstanceConfiguration) -> backward_association 
			(6,1), # backward_associationInstanceConfiguration -> match_class InstanceConfiguration(0.5.m.1InstanceConfiguration)
			(2,7), # apply class Function(0.5.m.1InstanceConfiguration) -> backward_association 
			(7,1), # backward_associationInstanceConfiguration -> match_class InstanceConfiguration(0.5.m.1InstanceConfiguration)
			(4,8), # apply class FunctionPrototype(0.5.m.0ComponentInstance) -> backward_association 
			(8,0), # backward_associationComponentInstance -> match_class ComponentInstance(0.5.m.0ComponentInstance)
		])


	# define evaluation methods for each match class.

	def eval_attr11(self, attr_value, this):
		return True

	def eval_attr12(self, attr_value, this):
		return True

	# define evaluation methods for each apply class.

	def eval_attr13(self, attr_value, this):
		return True

	def eval_attr14(self, attr_value, this):
		return True

	def eval_attr15(self, attr_value, this):
		return True

		# define evaluation methods for each match association.

	def eval_attr16(self, attr_value, this):
		return attr_value == "contents"
		# define evaluation methods for each apply association.


	def constraint(self, PreNode, graph):
		return True

