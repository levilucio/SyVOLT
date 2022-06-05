from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HPP4_ConnectedLHS(HimesisPreConditionPatternLHS):
	def __init__(self, *args, **kwargs):
		"""
		Creates the himesis graph representing the AToM3 model HPP4_ConnectedLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HPP4_ConnectedLHS, self).__init__(name='HPP4_ConnectedLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HPP4_ConnectedLHS')
		self["equations"] = []
		# Set the node attributes

		# match class State(0.33.m.0State) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__State"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.33.m.0State')

		# match class ExitPoint(0.33.m.1ExitPoint) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__ExitPoint"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.33.m.1ExitPoint')

		# match class Transition(0.33.m.2Transition) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__Transition"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.33.m.2Transition')

		# match class OUT2(0.33.m.3OUT2) node
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return True"""
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__OUT2"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.33.m.3OUT2')


		# match association ExitPoint--outgoingTransitions-->Transitionnode
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return attr_value == "outgoingTransitions" """
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__directLink_S"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.33.m.1ExitPointassoc40.33.m.2Transition')

		# match association Transition--type-->OUT2node
		self.add_node()
		self.vs[5]["MT_pre__attr1"] = """return attr_value == "type" """
		self.vs[5]["MT_label__"] = """6"""
		self.vs[5]["mm__"] = """MT_pre__directLink_S"""
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.33.m.2Transitionassoc50.33.m.3OUT2')

		# match association State--exitPoints-->ExitPointnode
		self.add_node()
		self.vs[6]["MT_pre__attr1"] = """return attr_value == "exitPoints" """
		self.vs[6]["MT_label__"] = """7"""
		self.vs[6]["mm__"] = """MT_pre__directLink_S"""
		self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.33.m.0Stateassoc60.33.m.1ExitPoint')

		# Add the edges
		self.add_edges([
			(1,4), # match class ExitPoint(0.33.m.1ExitPoint) -> association outgoingTransitions
			(4,2), # association Transition -> match class Transition(0.33.m.2Transition)
			(2,5), # match class Transition(0.33.m.2Transition) -> association type
			(5,3), # association OUT2 -> match class OUT2(0.33.m.3OUT2)
			(0,6), # match class State(0.33.m.0State) -> association exitPoints
			(6,1), # association ExitPoint -> match class ExitPoint(0.33.m.1ExitPoint)
		])


	# define evaluation methods for each match class.

	def eval_attr11(self, attr_value, this):
		return True

	def eval_attr12(self, attr_value, this):
		return True

	def eval_attr13(self, attr_value, this):
		return True

	def eval_attr14(self, attr_value, this):
		return True

	# define evaluation methods for each match association.

	def eval_attr15(self, attr_value, this):
		return attr_value == "outgoingTransitions"
	def eval_attr16(self, attr_value, this):
		return attr_value == "type"
	def eval_attr17(self, attr_value, this):
		return attr_value == "exitPoints"

	def constraint(self, PreNode, graph):
		return True

