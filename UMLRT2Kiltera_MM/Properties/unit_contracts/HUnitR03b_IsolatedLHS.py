from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HUnitR03b_IsolatedLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HUnitR03b_IsolatedLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HUnitR03b_IsolatedLHS, self).__init__(name='HUnitR03b_IsolatedLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HUnitR03b_IsolatedLHS')
		self["equations"] = []
		# Set the node attributes

		# match class State(3.1.m.0State) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__State"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'3.1.m.0State')

		# match class State(3.1.m.1State) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__State"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'3.1.m.1State')

	# define evaluation methods for each apply class.

	def eval_attr11(self, attr_value, this):
		return True

	def eval_attr12(self, attr_value, this):
		return True


	def constraint(self, PreNode, graph):
		return True

