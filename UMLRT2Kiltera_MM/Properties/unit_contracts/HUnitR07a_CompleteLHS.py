from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HUnitR07a_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HUnitR07a_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HUnitR07a_CompleteLHS, self).__init__(name='HUnitR07a_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HUnitR07a_CompleteLHS')
		self["equations"] = []
		# Set the node attributes

		# match class State(7.0.m.0State) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__State"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.0.m.0State')

		# match class Transition(7.0.m.1Transition) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__Transition"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.0.m.1Transition')

		# match class Trigger(7.0.m.2Trigger) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__Trigger"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.0.m.2Trigger')

		# match class Signal(7.0.m.3Signal) node
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return True"""
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__Signal"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.0.m.3Signal')

		# apply class Listen(7.0.a.0Listen) node
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return True"""
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__Listen"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.0.a.0Listen')

		# apply class ListenBranch(7.0.a.1ListenBranch) node
		self.add_node()
		self.vs[5]["MT_pre__attr1"] = """return True"""
		self.vs[5]["MT_label__"] = """6"""
		self.vs[5]["mm__"] = """MT_pre__ListenBranch"""
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.0.a.1ListenBranch')

		# apply class Inst(7.0.a.2Inst) node
		self.add_node()
		self.vs[6]["MT_pre__attr1"] = """return True"""
		self.vs[6]["MT_label__"] = """7"""
		self.vs[6]["mm__"] = """MT_pre__Inst"""
		self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.0.a.2Inst')

		# match association State--transitions-->Transitionnode
		self.add_node()
		self.vs[7]["MT_pre__attr1"] = """return attr_value == "transitions" """
		self.vs[7]["MT_label__"] = """8"""
		self.vs[7]["mm__"] = """MT_pre__directLink_S"""
		self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.0.m.0Stateassoc77.0.m.1Transition')

		# match association Transition--triggers-->Triggernode
		self.add_node()
		self.vs[8]["MT_pre__attr1"] = """return attr_value == "triggers" """
		self.vs[8]["MT_label__"] = """9"""
		self.vs[8]["mm__"] = """MT_pre__directLink_S"""
		self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.0.m.1Transitionassoc87.0.m.2Trigger')

		# match association Trigger--signal-->Signalnode
		self.add_node()
		self.vs[9]["MT_pre__attr1"] = """return attr_value == "signal" """
		self.vs[9]["MT_label__"] = """10"""
		self.vs[9]["mm__"] = """MT_pre__directLink_S"""
		self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.0.m.2Triggerassoc97.0.m.3Signal')

		# apply association Listen--branches-->ListenBranchnode
		self.add_node()
		self.vs[10]["MT_pre__attr1"] = """return attr_value == "branches" """
		self.vs[10]["MT_label__"] = """11"""
		self.vs[10]["mm__"] = """MT_pre__directLink_T"""
		self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.0.a.0Listenassoc107.0.a.1ListenBranch')

		# apply association ListenBranch--p-->Instnode
		self.add_node()
		self.vs[11]["MT_pre__attr1"] = """return attr_value == "p" """
		self.vs[11]["MT_label__"] = """12"""
		self.vs[11]["mm__"] = """MT_pre__directLink_T"""
		self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.0.a.1ListenBranchassoc117.0.a.2Inst')

		# trace association Listen--trace-->Statenode
		self.add_node()
		self.vs[12]["MT_label__"] = """13"""
		self.vs[12]["mm__"] = """MT_pre__trace_link"""
		self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.0.a.0Listenassoc127.0.m.0State')

		# trace association Inst--trace-->Transitionnode
		self.add_node()
		self.vs[13]["MT_label__"] = """14"""
		self.vs[13]["mm__"] = """MT_pre__trace_link"""
		self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.0.a.2Instassoc137.0.m.1Transition')

		self['equations'].append(((5,'channel'),(3,'name')))

		# Add the edges
		self.add_edges([
			(0,7), # match class State(7.0.m.0State) -> association transitions
			(7,1), # association Transition -> match class Transition(7.0.m.1Transition)
			(1,8), # match class Transition(7.0.m.1Transition) -> association triggers
			(8,2), # association Trigger -> match class Trigger(7.0.m.2Trigger)
			(2,9), # match class Trigger(7.0.m.2Trigger) -> association signal
			(9,3), # association Signal -> match class Signal(7.0.m.3Signal)
			(4,10), # apply class Listen(7.0.a.0Listen) -> association branches
			(10,5), # association ListenBranch -> apply class ListenBranch(7.0.a.1ListenBranch)
			(5,11), # apply class ListenBranch(7.0.a.1ListenBranch) -> association p
			(11,6), # association Inst -> apply class Inst(7.0.a.2Inst)
			(4,12), # apply class Listen(7.0.m.0State) -> backward_association 
			(12,0), # backward_associationState -> match_class State(7.0.m.0State)
			(6,13), # apply class Inst(7.0.m.1Transition) -> backward_association 
			(13,1), # backward_associationTransition -> match_class Transition(7.0.m.1Transition)
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

	# define evaluation methods for each apply class.

	def eval_attr15(self, attr_value, this):
		return True

	def eval_attr16(self, attr_value, this):
		return True

	def eval_attr17(self, attr_value, this):
		return True

		# define evaluation methods for each match association.

	def eval_attr18(self, attr_value, this):
		return attr_value == "transitions"
	def eval_attr19(self, attr_value, this):
		return attr_value == "triggers"
	def eval_attr110(self, attr_value, this):
		return attr_value == "signal"
		# define evaluation methods for each apply association.

	def eval_attr111(self, attr_value, this):
		return attr_value == "branches"
	def eval_attr112(self, attr_value, this):
		return attr_value == "p"

	def constraint(self, PreNode, graph):
		return True

