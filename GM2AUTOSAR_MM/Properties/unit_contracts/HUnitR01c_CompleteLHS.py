from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HUnitR01c_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HUnitR01c_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HUnitR01c_CompleteLHS, self).__init__(name='HUnitR01c_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HUnitR01c_CompleteLHS')
		self["equations"] = []
		# Set the node attributes

		# match class Module(1.2.m.0Module) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__Module"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'1.2.m.0Module')

		# match class Partition(1.2.m.1Partition) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__Partition"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'1.2.m.1Partition')

		# match class PhysicalNode(1.2.m.2PhysicalNode) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__PhysicalNode"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'1.2.m.2PhysicalNode')

		# apply class SwCompToEcuMapping_component(1.2.a.0SwCompToEcuMapping_component) node
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return True"""
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__SwCompToEcuMapping_component"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'1.2.a.0SwCompToEcuMapping_component')

		# apply class ComponentPrototype(1.2.a.1ComponentPrototype) node
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return True"""
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__ComponentPrototype"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'1.2.a.1ComponentPrototype')

		# match association PhysicalNode--partition-->Partitionnode
		self.add_node()
		self.vs[5]["MT_pre__attr1"] = """return attr_value == "partition" """
		self.vs[5]["MT_label__"] = """6"""
		self.vs[5]["mm__"] = """MT_pre__directLink_S"""
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'1.2.m.2PhysicalNodeassoc51.2.m.1Partition')

		# match association Partition--module-->Modulenode
		self.add_node()
		self.vs[6]["MT_pre__attr1"] = """return attr_value == "module" """
		self.vs[6]["MT_label__"] = """7"""
		self.vs[6]["mm__"] = """MT_pre__directLink_S"""
		self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'1.2.m.1Partitionassoc61.2.m.0Module')

		# apply association SwCompToEcuMapping_component--componentPrototype-->ComponentPrototypenode
		self.add_node()
		self.vs[7]["MT_pre__attr1"] = """return attr_value == "componentPrototype" """
		self.vs[7]["MT_label__"] = """8"""
		self.vs[7]["mm__"] = """MT_pre__directLink_T"""
		self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'1.2.a.0SwCompToEcuMapping_componentassoc71.2.a.1ComponentPrototype')

		self['equations'].append(((4,'shortName'),(0,'name')))

		# Add the edges
		self.add_edges([
			(2,5), # match class PhysicalNode(1.2.m.2PhysicalNode) -> association partition
			(5,1), # association Partition -> match class Partition(1.2.m.1Partition)
			(1,6), # match class Partition(1.2.m.1Partition) -> association module
			(6,0), # association Module -> match class Module(1.2.m.0Module)
			(3,7), # apply class SwCompToEcuMapping_component(1.2.a.0SwCompToEcuMapping_component) -> association componentPrototype
			(7,4), # association ComponentPrototype -> apply class ComponentPrototype(1.2.a.1ComponentPrototype)
		])


	# define evaluation methods for each match class.

	def eval_attr11(self, attr_value, this):
		return True

	def eval_attr12(self, attr_value, this):
		return True

	def eval_attr13(self, attr_value, this):
		return True

	# define evaluation methods for each apply class.

	def eval_attr14(self, attr_value, this):
		return True

	def eval_attr15(self, attr_value, this):
		return True

		# define evaluation methods for each match association.

	def eval_attr16(self, attr_value, this):
		return attr_value == "partition"
	def eval_attr17(self, attr_value, this):
		return attr_value == "module"
		# define evaluation methods for each apply association.

	def eval_attr18(self, attr_value, this):
		return attr_value == "componentPrototype"

	def constraint(self, PreNode, graph):
		return True

