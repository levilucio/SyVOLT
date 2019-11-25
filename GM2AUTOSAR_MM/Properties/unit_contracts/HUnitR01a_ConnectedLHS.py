from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HUnitR01a_ConnectedLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HUnitR01a_ConnectedLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HUnitR01a_ConnectedLHS, self).__init__(name='HUnitR01a_ConnectedLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HUnitR01a_ConnectedLHS')
		self["equations"] = []
		# Set the node attributes

		# match class PhysicalNode(1.0.m.0PhysicalNode) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__PhysicalNode"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'1.0.m.0PhysicalNode')

		# match class Partition(1.0.m.1Partition) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__Partition"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'1.0.m.1Partition')

		# match class Module(1.0.m.2Module) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__Module"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'1.0.m.2Module')


		# match association PhysicalNode--partition-->Partitionnode
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return attr_value == "partition" """
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__directLink_S"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'1.0.m.0PhysicalNodeassoc31.0.m.1Partition')

		# match association Partition--module-->Modulenode
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return attr_value == "module" """
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__directLink_S"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'1.0.m.1Partitionassoc41.0.m.2Module')

		# Add the edges
		self.add_edges([
			(0,3), # match class PhysicalNode(1.0.m.0PhysicalNode) -> association partition
			(3,1), # association Partition -> match class Partition(1.0.m.1Partition)
			(1,4), # match class Partition(1.0.m.1Partition) -> association module
			(4,2), # association Module -> match class Module(1.0.m.2Module)
		])


	# define evaluation methods for each match class.

	def eval_attr11(self, attr_value, this):
		return True

	def eval_attr12(self, attr_value, this):
		return True

	def eval_attr13(self, attr_value, this):
		return True

	# define evaluation methods for each match association.

	def eval_attr14(self, attr_value, this):
		return attr_value == "partition"
	def eval_attr15(self, attr_value, this):
		return attr_value == "module"

	def constraint(self, PreNode, graph):
		return True

