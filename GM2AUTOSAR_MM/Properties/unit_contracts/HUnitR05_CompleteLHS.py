from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HUnitR05_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HUnitR05_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HUnitR05_CompleteLHS, self).__init__(name='HUnitR05_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HUnitR05_CompleteLHS')
		self["equations"] = []
		# Set the node attributes

		# match class Partition(5.0.m.0Partition) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__Partition"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'5.0.m.0Partition')

		# match class Module(5.0.m.1Module) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__Module"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'5.0.m.1Module')

		# apply class SwcToEcuMapping(5.0.a.0SwcToEcuMapping) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__SwcToEcuMapping"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'5.0.a.0SwcToEcuMapping')

		# apply class SwCompToEcuMapping_component(5.0.a.1SwCompToEcuMapping_component) node
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return True"""
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__SwCompToEcuMapping_component"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'5.0.a.1SwCompToEcuMapping_component')

		# match association Partition--module-->Modulenode
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return attr_value == "module" """
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__directLink_S"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'5.0.m.0Partitionassoc45.0.m.1Module')

		# apply association SwcToEcuMapping--component-->SwCompToEcuMapping_componentnode
		self.add_node()
		self.vs[5]["MT_pre__attr1"] = """return attr_value == "component" """
		self.vs[5]["MT_label__"] = """6"""
		self.vs[5]["mm__"] = """MT_pre__directLink_T"""
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'5.0.a.0SwcToEcuMappingassoc55.0.a.1SwCompToEcuMapping_component')

		# trace association SwcToEcuMapping--trace-->Partitionnode
		self.add_node()
		self.vs[6]["MT_label__"] = """7"""
		self.vs[6]["mm__"] = """MT_pre__trace_link"""
		self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'5.0.a.0SwcToEcuMappingassoc65.0.m.0Partition')

		# trace association SwCompToEcuMapping_component--trace-->Modulenode
		self.add_node()
		self.vs[7]["MT_label__"] = """8"""
		self.vs[7]["mm__"] = """MT_pre__trace_link"""
		self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'5.0.a.1SwCompToEcuMapping_componentassoc75.0.m.1Module')


		# Add the edges
		self.add_edges([
			(0,4), # match class Partition(5.0.m.0Partition) -> association module
			(4,1), # association Module -> match class Module(5.0.m.1Module)
			(2,5), # apply class SwcToEcuMapping(5.0.a.0SwcToEcuMapping) -> association component
			(5,3), # association SwCompToEcuMapping_component -> apply class SwCompToEcuMapping_component(5.0.a.1SwCompToEcuMapping_component)
			(2,6), # apply class SwcToEcuMapping(5.0.m.0Partition) -> backward_association 
			(6,0), # backward_associationPartition -> match_class Partition(5.0.m.0Partition)
			(3,7), # apply class SwCompToEcuMapping_component(5.0.m.1Module) -> backward_association 
			(7,1), # backward_associationModule -> match_class Module(5.0.m.1Module)
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

		# define evaluation methods for each match association.

	def eval_attr15(self, attr_value, this):
		return attr_value == "module"
		# define evaluation methods for each apply association.

	def eval_attr16(self, attr_value, this):
		return attr_value == "component"

	def constraint(self, PreNode, graph):
		return True

