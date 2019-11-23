from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HUnitR07c_ConnectedLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HUnitR07c_ConnectedLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HUnitR07c_ConnectedLHS, self).__init__(name='HUnitR07c_ConnectedLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HUnitR07c_ConnectedLHS')
		self["equations"] = []
		# Set the node attributes

		# match class Transition(7.2.m.0Transition) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__Transition"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.2.m.0Transition')

		# match class Vertex(7.2.m.1Vertex) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__Vertex"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.2.m.1Vertex')

		# match class StateMachine(7.2.m.2StateMachine) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__StateMachine"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.2.m.2StateMachine')

		# match class State(7.2.m.3State) node
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return True"""
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__State"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.2.m.3State')

		# match class Trigger(7.2.m.4Trigger) node
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return True"""
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__Trigger"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.2.m.4Trigger')

		# match class Signal(7.2.m.5Signal) node
		self.add_node()
		self.vs[5]["MT_pre__attr1"] = """return True"""
		self.vs[5]["MT_label__"] = """6"""
		self.vs[5]["mm__"] = """MT_pre__Signal"""
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.2.m.5Signal')

		# match class State(7.2.m.6State) node
		self.add_node()
		self.vs[6]["MT_pre__attr1"] = """return True"""
		self.vs[6]["MT_label__"] = """7"""
		self.vs[6]["mm__"] = """MT_pre__State"""
		self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.2.m.6State')


		# match association Transition--src-->Vertexnode
		self.add_node()
		self.vs[7]["MT_pre__attr1"] = """return attr_value == "src" """
		self.vs[7]["MT_label__"] = """8"""
		self.vs[7]["mm__"] = """MT_pre__directLink_S"""
		self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.2.m.0Transitionassoc77.2.m.1Vertex')

		# match association Vertex--owningStateMachine-->StateMachinenode
		self.add_node()
		self.vs[8]["MT_pre__attr1"] = """return attr_value == "owningStateMachine" """
		self.vs[8]["MT_label__"] = """9"""
		self.vs[8]["mm__"] = """MT_pre__directLink_S"""
		self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.2.m.1Vertexassoc87.2.m.2StateMachine')

		# match association StateMachine--states-->Statenode
		self.add_node()
		self.vs[9]["MT_pre__attr1"] = """return attr_value == "states" """
		self.vs[9]["MT_label__"] = """10"""
		self.vs[9]["mm__"] = """MT_pre__directLink_S"""
		self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.2.m.2StateMachineassoc97.2.m.3State')

		# match association Transition--triggers-->Triggernode
		self.add_node()
		self.vs[10]["MT_pre__attr1"] = """return attr_value == "triggers" """
		self.vs[10]["MT_label__"] = """11"""
		self.vs[10]["mm__"] = """MT_pre__directLink_S"""
		self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.2.m.0Transitionassoc107.2.m.4Trigger')

		# match association Trigger--signal-->Signalnode
		self.add_node()
		self.vs[11]["MT_pre__attr1"] = """return attr_value == "signal" """
		self.vs[11]["MT_label__"] = """12"""
		self.vs[11]["mm__"] = """MT_pre__directLink_S"""
		self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.2.m.4Triggerassoc117.2.m.5Signal')

		# match association State--transitions-->Transitionnode
		self.add_node()
		self.vs[12]["MT_pre__attr1"] = """return attr_value == "transitions" """
		self.vs[12]["MT_label__"] = """13"""
		self.vs[12]["mm__"] = """MT_pre__directLink_S"""
		self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.2.m.6Stateassoc127.2.m.0Transition')

		# Add the edges
		self.add_edges([
			(0,7), # match class Transition(7.2.m.0Transition) -> association src
			(7,1), # association Vertex -> match class Vertex(7.2.m.1Vertex)
			(1,8), # match class Vertex(7.2.m.1Vertex) -> association owningStateMachine
			(8,2), # association StateMachine -> match class StateMachine(7.2.m.2StateMachine)
			(2,9), # match class StateMachine(7.2.m.2StateMachine) -> association states
			(9,3), # association State -> match class State(7.2.m.3State)
			(0,10), # match class Transition(7.2.m.0Transition) -> association triggers
			(10,4), # association Trigger -> match class Trigger(7.2.m.4Trigger)
			(4,11), # match class Trigger(7.2.m.4Trigger) -> association signal
			(11,5), # association Signal -> match class Signal(7.2.m.5Signal)
			(6,12), # match class State(7.2.m.6State) -> association transitions
			(12,0), # association Transition -> match class Transition(7.2.m.0Transition)
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

	def eval_attr15(self, attr_value, this):
		return True

	def eval_attr16(self, attr_value, this):
		return True

	def eval_attr17(self, attr_value, this):
		return True

	# define evaluation methods for each match association.

	def eval_attr18(self, attr_value, this):
		return attr_value == "src"
	def eval_attr19(self, attr_value, this):
		return attr_value == "owningStateMachine"
	def eval_attr110(self, attr_value, this):
		return attr_value == "states"
	def eval_attr111(self, attr_value, this):
		return attr_value == "triggers"
	def eval_attr112(self, attr_value, this):
		return attr_value == "signal"
	def eval_attr113(self, attr_value, this):
		return attr_value == "transitions"

	def constraint(self, PreNode, graph):
		return True

