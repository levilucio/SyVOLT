from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HUnitR04b_IsolatedLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HUnitR04b_IsolatedLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HUnitR04b_IsolatedLHS, self).__init__(name='HUnitR04b_IsolatedLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HUnitR04b_IsolatedLHS')
		self["equations"] = []
		# Set the node attributes

		# match class PhysicalNode(4.1.m.0PhysicalNode) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__PhysicalNode"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'4.1.m.0PhysicalNode')

		# match class Partition(4.1.m.1Partition) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__Partition"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'4.1.m.1Partition')

		# match class Module(4.1.m.2Module) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__Module"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'4.1.m.2Module')

		# match class Scheduler(4.1.m.3Scheduler) node
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return True"""
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__Scheduler"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'4.1.m.3Scheduler')

		# match class Service(4.1.m.4Service) node
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return True"""
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__Service"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'4.1.m.4Service')

	# define evaluation methods for each apply class.

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


	def constraint(self, PreNode, graph):
		return True

