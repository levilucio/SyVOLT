from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HUnitR02_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HUnitR02_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HUnitR02_CompleteLHS, self).__init__(name='HUnitR02_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HUnitR02_CompleteLHS')
		self["equations"] = []
		# Set the node attributes

		# match class PhysicalNode(2.0.m.0PhysicalNode) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__PhysicalNode"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'2.0.m.0PhysicalNode')

		# match class Partition(2.0.m.1Partition) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__Partition"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'2.0.m.1Partition')

		# apply class SystemMapping(2.0.a.0SystemMapping) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__SystemMapping"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'2.0.a.0SystemMapping')

		# apply class SwcToEcuMapping(2.0.a.1SwcToEcuMapping) node
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return True"""
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__SwcToEcuMapping"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'2.0.a.1SwcToEcuMapping')

		# match association PhysicalNode--partition-->Partitionnode
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return attr_value == "partition" """
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__directLink_S"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'2.0.m.0PhysicalNodeassoc42.0.m.1Partition')

		# apply association SystemMapping--swMapping-->SwcToEcuMappingnode
		self.add_node()
		self.vs[5]["MT_pre__attr1"] = """return attr_value == "swMapping" """
		self.vs[5]["MT_label__"] = """6"""
		self.vs[5]["mm__"] = """MT_pre__directLink_T"""
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'2.0.a.0SystemMappingassoc52.0.a.1SwcToEcuMapping')

		# trace association SystemMapping--trace-->PhysicalNodenode
		self.add_node()
		self.vs[6]["MT_label__"] = """7"""
		self.vs[6]["mm__"] = """MT_pre__trace_link"""
		self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'2.0.a.0SystemMappingassoc62.0.m.0PhysicalNode')

		# trace association SwcToEcuMapping--trace-->Partitionnode
		self.add_node()
		self.vs[7]["MT_label__"] = """8"""
		self.vs[7]["mm__"] = """MT_pre__trace_link"""
		self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'2.0.a.1SwcToEcuMappingassoc72.0.m.1Partition')


		# Add the edges
		self.add_edges([
			(0,4), # match class PhysicalNode(2.0.m.0PhysicalNode) -> association partition
			(4,1), # association Partition -> match class Partition(2.0.m.1Partition)
			(2,5), # apply class SystemMapping(2.0.a.0SystemMapping) -> association swMapping
			(5,3), # association SwcToEcuMapping -> apply class SwcToEcuMapping(2.0.a.1SwcToEcuMapping)
			(2,6), # apply class SystemMapping(2.0.m.0PhysicalNode) -> backward_association 
			(6,0), # backward_associationPhysicalNode -> match_class PhysicalNode(2.0.m.0PhysicalNode)
			(3,7), # apply class SwcToEcuMapping(2.0.m.1Partition) -> backward_association 
			(7,1), # backward_associationPartition -> match_class Partition(2.0.m.1Partition)
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
		return attr_value == "partition"
		# define evaluation methods for each apply association.

	def eval_attr16(self, attr_value, this):
		return attr_value == "swMapping"

	def constraint(self, PreNode, graph):
		return True

