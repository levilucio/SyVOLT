from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HUnitR07c_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HUnitR07c_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HUnitR07c_CompleteLHS, self).__init__(name='HUnitR07c_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HUnitR07c_CompleteLHS')
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

		# apply class ListenBranch(7.2.a.0ListenBranch) node
		self.add_node()
		self.vs[7]["MT_pre__attr1"] = """return True"""
		self.vs[7]["MT_label__"] = """8"""
		self.vs[7]["mm__"] = """MT_pre__ListenBranch"""
		self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.2.a.0ListenBranch')

		# apply class Seq(7.2.a.1Seq) node
		self.add_node()
		self.vs[8]["MT_pre__attr1"] = """return True"""
		self.vs[8]["MT_label__"] = """9"""
		self.vs[8]["mm__"] = """MT_pre__Seq"""
		self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.2.a.1Seq')

		# apply class Trigger(7.2.a.2Trigger) node
		self.add_node()
		self.vs[9]["MT_pre__attr1"] = """return True"""
		self.vs[9]["MT_label__"] = """10"""
		self.vs[9]["mm__"] = """MT_pre__Trigger"""
		self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.2.a.2Trigger')

		# apply class Listen(7.2.a.3Listen) node
		self.add_node()
		self.vs[10]["MT_pre__attr1"] = """return True"""
		self.vs[10]["MT_label__"] = """11"""
		self.vs[10]["mm__"] = """MT_pre__Listen"""
		self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.2.a.3Listen')

		# apply class ListenBranch(7.2.a.4ListenBranch) node
		self.add_node()
		self.vs[11]["MT_pre__attr1"] = """return True"""
		self.vs[11]["MT_label__"] = """12"""
		self.vs[11]["mm__"] = """MT_pre__ListenBranch"""
		self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.2.a.4ListenBranch')

		# apply class Inst(7.2.a.5Inst) node
		self.add_node()
		self.vs[12]["MT_pre__attr1"] = """return True"""
		self.vs[12]["MT_label__"] = """13"""
		self.vs[12]["mm__"] = """MT_pre__Inst"""
		self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.2.a.5Inst')

		# apply class Listen(7.2.a.6Listen) node
		self.add_node()
		self.vs[13]["MT_pre__attr1"] = """return True"""
		self.vs[13]["MT_label__"] = """14"""
		self.vs[13]["mm__"] = """MT_pre__Listen"""
		self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.2.a.6Listen')

		# match association Transition--src-->Vertexnode
		self.add_node()
		self.vs[14]["MT_pre__attr1"] = """return attr_value == "src" """
		self.vs[14]["MT_label__"] = """15"""
		self.vs[14]["mm__"] = """MT_pre__directLink_S"""
		self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.2.m.0Transitionassoc147.2.m.1Vertex')

		# match association Vertex--owningStateMachine-->StateMachinenode
		self.add_node()
		self.vs[15]["MT_pre__attr1"] = """return attr_value == "owningStateMachine" """
		self.vs[15]["MT_label__"] = """16"""
		self.vs[15]["mm__"] = """MT_pre__directLink_S"""
		self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.2.m.1Vertexassoc157.2.m.2StateMachine')

		# match association StateMachine--states-->Statenode
		self.add_node()
		self.vs[16]["MT_pre__attr1"] = """return attr_value == "states" """
		self.vs[16]["MT_label__"] = """17"""
		self.vs[16]["mm__"] = """MT_pre__directLink_S"""
		self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.2.m.2StateMachineassoc167.2.m.3State')

		# match association Transition--triggers-->Triggernode
		self.add_node()
		self.vs[17]["MT_pre__attr1"] = """return attr_value == "triggers" """
		self.vs[17]["MT_label__"] = """18"""
		self.vs[17]["mm__"] = """MT_pre__directLink_S"""
		self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.2.m.0Transitionassoc177.2.m.4Trigger')

		# match association Trigger--signal-->Signalnode
		self.add_node()
		self.vs[18]["MT_pre__attr1"] = """return attr_value == "signal" """
		self.vs[18]["MT_label__"] = """19"""
		self.vs[18]["mm__"] = """MT_pre__directLink_S"""
		self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.2.m.4Triggerassoc187.2.m.5Signal')

		# match association State--transitions-->Transitionnode
		self.add_node()
		self.vs[19]["MT_pre__attr1"] = """return attr_value == "transitions" """
		self.vs[19]["MT_label__"] = """20"""
		self.vs[19]["mm__"] = """MT_pre__directLink_S"""
		self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.2.m.6Stateassoc197.2.m.0Transition')

		# apply association ListenBranch--p-->Seqnode
		self.add_node()
		self.vs[20]["MT_pre__attr1"] = """return attr_value == "p" """
		self.vs[20]["MT_label__"] = """21"""
		self.vs[20]["mm__"] = """MT_pre__directLink_T"""
		self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.2.a.0ListenBranchassoc207.2.a.1Seq')

		# apply association Seq--p-->Triggernode
		self.add_node()
		self.vs[21]["MT_pre__attr1"] = """return attr_value == "p" """
		self.vs[21]["MT_label__"] = """22"""
		self.vs[21]["mm__"] = """MT_pre__directLink_T"""
		self.vs[21]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.2.a.1Seqassoc217.2.a.2Trigger')

		# apply association Seq--p-->Listennode
		self.add_node()
		self.vs[22]["MT_pre__attr1"] = """return attr_value == "p" """
		self.vs[22]["MT_label__"] = """23"""
		self.vs[22]["mm__"] = """MT_pre__directLink_T"""
		self.vs[22]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.2.a.1Seqassoc227.2.a.3Listen')

		# apply association Listen--branches-->ListenBranchnode
		self.add_node()
		self.vs[23]["MT_pre__attr1"] = """return attr_value == "branches" """
		self.vs[23]["MT_label__"] = """24"""
		self.vs[23]["mm__"] = """MT_pre__directLink_T"""
		self.vs[23]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.2.a.3Listenassoc237.2.a.4ListenBranch')

		# apply association ListenBranch--p-->Instnode
		self.add_node()
		self.vs[24]["MT_pre__attr1"] = """return attr_value == "p" """
		self.vs[24]["MT_label__"] = """25"""
		self.vs[24]["mm__"] = """MT_pre__directLink_T"""
		self.vs[24]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.2.a.4ListenBranchassoc247.2.a.5Inst')

		# apply association Listen--branches-->ListenBranchnode
		self.add_node()
		self.vs[25]["MT_pre__attr1"] = """return attr_value == "branches" """
		self.vs[25]["MT_label__"] = """26"""
		self.vs[25]["mm__"] = """MT_pre__directLink_T"""
		self.vs[25]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.2.a.6Listenassoc257.2.a.0ListenBranch')

		# trace association Inst--trace-->Transitionnode
		self.add_node()
		self.vs[26]["MT_label__"] = """27"""
		self.vs[26]["mm__"] = """MT_pre__trace_link"""
		self.vs[26]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.2.a.5Instassoc267.2.m.0Transition')

		# trace association Listen--trace-->Statenode
		self.add_node()
		self.vs[27]["MT_label__"] = """28"""
		self.vs[27]["mm__"] = """MT_pre__trace_link"""
		self.vs[27]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.2.a.6Listenassoc277.2.m.6State')

		self['equations'].append(((7,'channel'),(5,'name')))
		self['equations'].append(((9,'channel'),('constant','exit_in')))
		self['equations'].append(((11,'channel'),('constant','exack_in')))

		# Add the edges
		self.add_edges([
			(0,14), # match class Transition(7.2.m.0Transition) -> association src
			(14,1), # association Vertex -> match class Vertex(7.2.m.1Vertex)
			(1,15), # match class Vertex(7.2.m.1Vertex) -> association owningStateMachine
			(15,2), # association StateMachine -> match class StateMachine(7.2.m.2StateMachine)
			(2,16), # match class StateMachine(7.2.m.2StateMachine) -> association states
			(16,3), # association State -> match class State(7.2.m.3State)
			(0,17), # match class Transition(7.2.m.0Transition) -> association triggers
			(17,4), # association Trigger -> match class Trigger(7.2.m.4Trigger)
			(4,18), # match class Trigger(7.2.m.4Trigger) -> association signal
			(18,5), # association Signal -> match class Signal(7.2.m.5Signal)
			(6,19), # match class State(7.2.m.6State) -> association transitions
			(19,0), # association Transition -> match class Transition(7.2.m.0Transition)
			(7,20), # apply class ListenBranch(7.2.a.0ListenBranch) -> association p
			(20,8), # association Seq -> apply class Seq(7.2.a.1Seq)
			(8,21), # apply class Seq(7.2.a.1Seq) -> association p
			(21,9), # association Trigger -> apply class Trigger(7.2.a.2Trigger)
			(8,22), # apply class Seq(7.2.a.1Seq) -> association p
			(22,10), # association Listen -> apply class Listen(7.2.a.3Listen)
			(10,23), # apply class Listen(7.2.a.3Listen) -> association branches
			(23,11), # association ListenBranch -> apply class ListenBranch(7.2.a.4ListenBranch)
			(11,24), # apply class ListenBranch(7.2.a.4ListenBranch) -> association p
			(24,12), # association Inst -> apply class Inst(7.2.a.5Inst)
			(13,25), # apply class Listen(7.2.a.6Listen) -> association branches
			(25,7), # association ListenBranch -> apply class ListenBranch(7.2.a.0ListenBranch)
			(12,26), # apply class Inst(7.2.m.0Transition) -> backward_association 
			(26,0), # backward_associationTransition -> match_class Transition(7.2.m.0Transition)
			(13,27), # apply class Listen(7.2.m.6State) -> backward_association 
			(27,6), # backward_associationState -> match_class State(7.2.m.6State)
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

	# define evaluation methods for each apply class.

	def eval_attr18(self, attr_value, this):
		return True

	def eval_attr19(self, attr_value, this):
		return True

	def eval_attr110(self, attr_value, this):
		return True

	def eval_attr111(self, attr_value, this):
		return True

	def eval_attr112(self, attr_value, this):
		return True

	def eval_attr113(self, attr_value, this):
		return True

	def eval_attr114(self, attr_value, this):
		return True

		# define evaluation methods for each match association.

	def eval_attr115(self, attr_value, this):
		return attr_value == "src"
	def eval_attr116(self, attr_value, this):
		return attr_value == "owningStateMachine"
	def eval_attr117(self, attr_value, this):
		return attr_value == "states"
	def eval_attr118(self, attr_value, this):
		return attr_value == "triggers"
	def eval_attr119(self, attr_value, this):
		return attr_value == "signal"
	def eval_attr120(self, attr_value, this):
		return attr_value == "transitions"
		# define evaluation methods for each apply association.

	def eval_attr121(self, attr_value, this):
		return attr_value == "p"
	def eval_attr122(self, attr_value, this):
		return attr_value == "p"
	def eval_attr123(self, attr_value, this):
		return attr_value == "p"
	def eval_attr124(self, attr_value, this):
		return attr_value == "branches"
	def eval_attr125(self, attr_value, this):
		return attr_value == "p"
	def eval_attr126(self, attr_value, this):
		return attr_value == "branches"

	def constraint(self, PreNode, graph):
		return True

