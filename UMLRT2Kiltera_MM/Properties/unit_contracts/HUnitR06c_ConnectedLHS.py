from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HUnitR06c_ConnectedLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HUnitR06c_ConnectedLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HUnitR06c_ConnectedLHS, self).__init__(name='HUnitR06c_ConnectedLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HUnitR06c_ConnectedLHS')
		self["equations"] = []
		# Set the node attributes

		# match class State(6.2.m.0State) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__State"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.2.m.0State')

		# match class Transition(6.2.m.1Transition) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__Transition"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.2.m.1Transition')

		# match class IN1(6.2.m.2IN1) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__IN1"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.2.m.2IN1')

		# match class EntryPoint(6.2.m.3EntryPoint) node
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return True"""
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__EntryPoint"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.2.m.3EntryPoint')

		# match class StateMachine(6.2.m.4StateMachine) node
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return True"""
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__StateMachine"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.2.m.4StateMachine')


		# match association State--transitions-->Transitionnode
		self.add_node()
		self.vs[5]["MT_pre__attr1"] = """return attr_value == "transitions" """
		self.vs[5]["MT_label__"] = """6"""
		self.vs[5]["mm__"] = """MT_pre__directLink_S"""
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.2.m.0Stateassoc56.2.m.1Transition')

		# match association Transition--type-->IN1node
		self.add_node()
		self.vs[6]["MT_pre__attr1"] = """return attr_value == "type" """
		self.vs[6]["MT_label__"] = """7"""
		self.vs[6]["mm__"] = """MT_pre__directLink_S"""
		self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.2.m.1Transitionassoc66.2.m.2IN1')

		# match association Transition--dest-->EntryPointnode
		self.add_node()
		self.vs[7]["MT_pre__attr1"] = """return attr_value == "dest" """
		self.vs[7]["MT_label__"] = """8"""
		self.vs[7]["mm__"] = """MT_pre__directLink_S"""
		self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.2.m.1Transitionassoc76.2.m.3EntryPoint')

		# match association EntryPoint--owningStateMachine-->StateMachinenode
		self.add_node()
		self.vs[8]["MT_pre__attr1"] = """return attr_value == "owningStateMachine" """
		self.vs[8]["MT_label__"] = """9"""
		self.vs[8]["mm__"] = """MT_pre__directLink_S"""
		self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.2.m.3EntryPointassoc86.2.m.4StateMachine')

		# Add the edges
		self.add_edges([
			(0,5), # match class State(6.2.m.0State) -> association transitions
			(5,1), # association Transition -> match class Transition(6.2.m.1Transition)
			(1,6), # match class Transition(6.2.m.1Transition) -> association type
			(6,2), # association IN1 -> match class IN1(6.2.m.2IN1)
			(1,7), # match class Transition(6.2.m.1Transition) -> association dest
			(7,3), # association EntryPoint -> match class EntryPoint(6.2.m.3EntryPoint)
			(3,8), # match class EntryPoint(6.2.m.3EntryPoint) -> association owningStateMachine
			(8,4), # association StateMachine -> match class StateMachine(6.2.m.4StateMachine)
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

	# define evaluation methods for each match association.

	def eval_attr16(self, attr_value, this):
		return attr_value == "transitions"
	def eval_attr17(self, attr_value, this):
		return attr_value == "type"
	def eval_attr18(self, attr_value, this):
		return attr_value == "dest"
	def eval_attr19(self, attr_value, this):
		return attr_value == "owningStateMachine"

	def constraint(self, PreNode, graph):
		return True

