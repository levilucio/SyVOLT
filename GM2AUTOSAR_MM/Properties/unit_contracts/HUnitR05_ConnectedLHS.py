from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HUnitR05_ConnectedLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HUnitR05_ConnectedLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HUnitR05_ConnectedLHS, self).__init__(name='HUnitR05_ConnectedLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HUnitR05_ConnectedLHS')
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


		# match association Partition--module-->Modulenode
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return attr_value == "module" """
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__directLink_S"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'5.0.m.0Partitionassoc25.0.m.1Module')

		# Add the edges
		self.add_edges([
			(0,2), # match class Partition(5.0.m.0Partition) -> association module
			(2,1), # association Module -> match class Module(5.0.m.1Module)
		])


	# define evaluation methods for each match class.

	def eval_attr11(self, attr_value, this):
		return True

	def eval_attr12(self, attr_value, this):
		return True

	# define evaluation methods for each match association.

	def eval_attr13(self, attr_value, this):
		return attr_value == "module"

	def constraint(self, PreNode, graph):
		return True

