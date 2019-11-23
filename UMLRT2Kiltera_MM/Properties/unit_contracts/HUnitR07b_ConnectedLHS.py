from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HUnitR07b_ConnectedLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HUnitR07b_ConnectedLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HUnitR07b_ConnectedLHS, self).__init__(name='HUnitR07b_ConnectedLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HUnitR07b_ConnectedLHS')
		self["equations"] = []
		# Set the node attributes

		# match class ExitPoint(7.1.m.0ExitPoint) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__ExitPoint"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.1.m.0ExitPoint')

		# match class Transition(7.1.m.1Transition) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__Transition"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.1.m.1Transition')


		# match association ExitPoint--outgoingTransitions-->Transitionnode
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return attr_value == "outgoingTransitions" """
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__directLink_S"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.1.m.0ExitPointassoc27.1.m.1Transition')

		# Add the edges
		self.add_edges([
			(0,2), # match class ExitPoint(7.1.m.0ExitPoint) -> association outgoingTransitions
			(2,1), # association Transition -> match class Transition(7.1.m.1Transition)
		])


	# define evaluation methods for each match class.

	def eval_attr11(self, attr_value, this):
		return True

	def eval_attr12(self, attr_value, this):
		return True

	# define evaluation methods for each match association.

	def eval_attr13(self, attr_value, this):
		return attr_value == "outgoingTransitions"

	def constraint(self, PreNode, graph):
		return True

