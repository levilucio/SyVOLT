from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HUnitR06_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HUnitR06_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HUnitR06_CompleteLHS, self).__init__(name='HUnitR06_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HUnitR06_CompleteLHS')
		self["equations"] = []
		# Set the node attributes

		# match class PhysicalNode(6.0.m.0PhysicalNode) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__PhysicalNode"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.0.m.0PhysicalNode')

		# match class Partition(6.0.m.1Partition) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__Partition"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.0.m.1Partition')

		# apply class SwcToEcuMapping(6.0.a.0SwcToEcuMapping) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__SwcToEcuMapping"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.0.a.0SwcToEcuMapping')

		# apply class EcuInstance(6.0.a.1EcuInstance) node
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return True"""
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__EcuInstance"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.0.a.1EcuInstance')

		# match association PhysicalNode--partition-->Partitionnode
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return attr_value == "partition" """
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__directLink_S"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.0.m.0PhysicalNodeassoc46.0.m.1Partition')

		# apply association SwcToEcuMapping--ecuInstance-->EcuInstancenode
		self.add_node()
		self.vs[5]["MT_pre__attr1"] = """return attr_value == "ecuInstance" """
		self.vs[5]["MT_label__"] = """6"""
		self.vs[5]["mm__"] = """MT_pre__directLink_T"""
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.0.a.0SwcToEcuMappingassoc56.0.a.1EcuInstance')

		# trace association EcuInstance--trace-->PhysicalNodenode
		self.add_node()
		self.vs[6]["MT_label__"] = """7"""
		self.vs[6]["mm__"] = """MT_pre__trace_link"""
		self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.0.a.1EcuInstanceassoc66.0.m.0PhysicalNode')

		# trace association SwcToEcuMapping--trace-->Partitionnode
		self.add_node()
		self.vs[7]["MT_label__"] = """8"""
		self.vs[7]["mm__"] = """MT_pre__trace_link"""
		self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.0.a.0SwcToEcuMappingassoc76.0.m.1Partition')


		# Add the edges
		self.add_edges([
			(0,4), # match class PhysicalNode(6.0.m.0PhysicalNode) -> association partition
			(4,1), # association Partition -> match class Partition(6.0.m.1Partition)
			(2,5), # apply class SwcToEcuMapping(6.0.a.0SwcToEcuMapping) -> association ecuInstance
			(5,3), # association EcuInstance -> apply class EcuInstance(6.0.a.1EcuInstance)
			(3,6), # apply class EcuInstance(6.0.m.0PhysicalNode) -> backward_association 
			(6,0), # backward_associationPhysicalNode -> match_class PhysicalNode(6.0.m.0PhysicalNode)
			(2,7), # apply class SwcToEcuMapping(6.0.m.1Partition) -> backward_association 
			(7,1), # backward_associationPartition -> match_class Partition(6.0.m.1Partition)
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
		return attr_value == "ecuInstance"

	def constraint(self, PreNode, graph):
		return True

