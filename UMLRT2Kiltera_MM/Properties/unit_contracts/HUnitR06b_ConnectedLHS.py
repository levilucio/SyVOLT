from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HUnitR06b_ConnectedLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HUnitR06b_ConnectedLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HUnitR06b_ConnectedLHS, self).__init__(name='HUnitR06b_ConnectedLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HUnitR06b_ConnectedLHS')
		self["equations"] = []
		# Set the node attributes

		# match class Transition(6.1.m.0Transition) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__Transition"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.1.m.0Transition')

		# match class OUT2(6.1.m.1OUT2) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__OUT2"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.1.m.1OUT2')

		# match class StateMachine(6.1.m.2StateMachine) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__StateMachine"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.1.m.2StateMachine')

		# match class Vertex(6.1.m.3Vertex) node
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return True"""
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__Vertex"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.1.m.3Vertex')


		# match association Transition--type-->OUT2node
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return attr_value == "type" """
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__directLink_S"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.1.m.0Transitionassoc46.1.m.1OUT2')

		# match association Transition--owningStateMachine-->StateMachinenode
		self.add_node()
		self.vs[5]["MT_pre__attr1"] = """return attr_value == "owningStateMachine" """
		self.vs[5]["MT_label__"] = """6"""
		self.vs[5]["mm__"] = """MT_pre__directLink_S"""
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.1.m.0Transitionassoc56.1.m.2StateMachine')

		# match association StateMachine--exitPoints-->Vertexnode
		self.add_node()
		self.vs[6]["MT_pre__attr1"] = """return attr_value == "exitPoints" """
		self.vs[6]["MT_label__"] = """7"""
		self.vs[6]["mm__"] = """MT_pre__directLink_S"""
		self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.1.m.2StateMachineassoc66.1.m.3Vertex')

		# match association Transition--dest-->Vertexnode
		self.add_node()
		self.vs[7]["MT_pre__attr1"] = """return attr_value == "dest" """
		self.vs[7]["MT_label__"] = """8"""
		self.vs[7]["mm__"] = """MT_pre__directLink_S"""
		self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.1.m.0Transitionassoc76.1.m.3Vertex')

		# Add the edges
		self.add_edges([
			(0,4), # match class Transition(6.1.m.0Transition) -> association type
			(4,1), # association OUT2 -> match class OUT2(6.1.m.1OUT2)
			(0,5), # match class Transition(6.1.m.0Transition) -> association owningStateMachine
			(5,2), # association StateMachine -> match class StateMachine(6.1.m.2StateMachine)
			(2,6), # match class StateMachine(6.1.m.2StateMachine) -> association exitPoints
			(6,3), # association Vertex -> match class Vertex(6.1.m.3Vertex)
			(0,7), # match class Transition(6.1.m.0Transition) -> association dest
			(7,3), # association Vertex -> match class Vertex(6.1.m.3Vertex)
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
		return attr_value == "type"
	def eval_attr16(self, attr_value, this):
		return attr_value == "owningStateMachine"
	def eval_attr17(self, attr_value, this):
		return attr_value == "exitPoints"
	def eval_attr18(self, attr_value, this):
		return attr_value == "dest"

	def constraint(self, PreNode, graph):
		return True

