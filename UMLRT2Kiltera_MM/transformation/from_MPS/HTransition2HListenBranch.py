from core.himesis import Himesis
import uuid

class HTransition2HListenBranch(Himesis):
	def __init__(self, *args, **kwargs):
		"""
		Creates the himesis graph representing the DSLTrans rule Transition2HListenBranch.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HTransition2HListenBranch, self).__init__(name='HTransition2HListenBranch', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """Transition2HListenBranch"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Transition2HListenBranch')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """Transition2HListenBranch"""

		# match class Transition(7.2.m.0Transition) node
		self.add_node()
		self.vs[3]["mm__"] = """Transition"""
		self.vs[3]["attr1"] = """+"""

		# match class Vertex(7.2.m.1Vertex) node
		self.add_node()
		self.vs[4]["mm__"] = """Vertex"""
		self.vs[4]["attr1"] = """+"""

		# match class StateMachine(7.2.m.2StateMachine) node
		self.add_node()
		self.vs[5]["mm__"] = """StateMachine"""
		self.vs[5]["attr1"] = """+"""

		# match class State(7.2.m.3State) node
		self.add_node()
		self.vs[6]["mm__"] = """State"""
		self.vs[6]["attr1"] = """1"""

		# match class Trigger(7.2.m.4Trigger) node
		self.add_node()
		self.vs[7]["mm__"] = """Trigger"""
		self.vs[7]["attr1"] = """1"""

		# match class Signal(7.2.m.5Signal) node
		self.add_node()
		self.vs[8]["mm__"] = """Signal"""
		self.vs[8]["attr1"] = """1"""

		# match class State(7.2.m.6State) node
		self.add_node()
		self.vs[9]["mm__"] = """State"""
		self.vs[9]["attr1"] = """+"""

		# apply class ListenBranch(7.2.a.0ListenBranch) node
		self.add_node()
		self.vs[10]["mm__"] = """ListenBranch"""
		self.vs[10]["attr1"] = """1"""

		# apply class Seq(7.2.a.1Seq) node
		self.add_node()
		self.vs[11]["mm__"] = """Seq"""
		self.vs[11]["attr1"] = """1"""

		# apply class Trigger(7.2.a.2Trigger) node
		self.add_node()
		self.vs[12]["mm__"] = """Trigger"""
		self.vs[12]["attr1"] = """1"""

		# apply class Listen(7.2.a.3Listen) node
		self.add_node()
		self.vs[13]["mm__"] = """Listen"""
		self.vs[13]["attr1"] = """1"""

		# apply class ListenBranch(7.2.a.4ListenBranch) node
		self.add_node()
		self.vs[14]["mm__"] = """ListenBranch"""
		self.vs[14]["attr1"] = """1"""

		# apply class Inst(7.2.a.5Inst) node
		self.add_node()
		self.vs[15]["mm__"] = """Inst"""
		self.vs[15]["attr1"] = """1"""

		# apply class Listen(7.2.a.6Listen) node
		self.add_node()
		self.vs[16]["mm__"] = """Listen"""
		self.vs[16]["attr1"] = """1"""

		# match association Transition--src-->Vertex node 
		self.add_node()
		self.vs[17]["attr1"] = """src"""
		self.vs[17]["mm__"] = """directLink_S"""

		# match association Vertex--owningStateMachine-->StateMachine node 
		self.add_node()
		self.vs[18]["attr1"] = """owningStateMachine"""
		self.vs[18]["mm__"] = """directLink_S"""

		# match association StateMachine--states-->State node 
		self.add_node()
		self.vs[19]["attr1"] = """states"""
		self.vs[19]["mm__"] = """directLink_S"""

		# match association Transition--triggers-->Trigger node 
		self.add_node()
		self.vs[20]["attr1"] = """triggers"""
		self.vs[20]["mm__"] = """directLink_S"""

		# match association Trigger--signal-->Signal node 
		self.add_node()
		self.vs[21]["attr1"] = """signal"""
		self.vs[21]["mm__"] = """directLink_S"""

		# match association State--transitions-->Transition node 
		self.add_node()
		self.vs[22]["attr1"] = """transitions"""
		self.vs[22]["mm__"] = """directLink_S"""

		# apply association ListenBranch--p-->Seq node 
		self.add_node()
		self.vs[23]["attr1"] = """p"""
		self.vs[23]["mm__"] = """directLink_T"""

		# apply association Seq--p-->Trigger node 
		self.add_node()
		self.vs[24]["attr1"] = """p"""
		self.vs[24]["mm__"] = """directLink_T"""

		# apply association Seq--p-->Listen node 
		self.add_node()
		self.vs[25]["attr1"] = """p"""
		self.vs[25]["mm__"] = """directLink_T"""

		# apply association Listen--branches-->ListenBranch node 
		self.add_node()
		self.vs[26]["attr1"] = """branches"""
		self.vs[26]["mm__"] = """directLink_T"""

		# apply association ListenBranch--p-->Inst node 
		self.add_node()
		self.vs[27]["attr1"] = """p"""
		self.vs[27]["mm__"] = """directLink_T"""

		# apply association Listen--branches-->ListenBranch node 
		self.add_node()
		self.vs[28]["attr1"] = """branches"""
		self.vs[28]["mm__"] = """directLink_T"""

		# backward association Inst-->Transitionnode 
		self.add_node()
		self.vs[29]["mm__"] = """backward_link"""

		# backward association Listen-->Statenode 
		self.add_node()
		self.vs[30]["mm__"] = """backward_link"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class Transition(7.2.m.0Transition)
			(0,4), # matchmodel -> match_class Vertex(7.2.m.1Vertex)
			(0,5), # matchmodel -> match_class StateMachine(7.2.m.2StateMachine)
			(0,6), # matchmodel -> match_class State(7.2.m.3State)
			(0,7), # matchmodel -> match_class Trigger(7.2.m.4Trigger)
			(0,8), # matchmodel -> match_class Signal(7.2.m.5Signal)
			(0,9), # matchmodel -> match_class State(7.2.m.6State)
			(1,10), # applymodel -> apply_classListenBranch(7.2.a.0ListenBranch)
			(1,11), # applymodel -> apply_classSeq(7.2.a.1Seq)
			(1,12), # applymodel -> apply_classTrigger(7.2.a.2Trigger)
			(1,13), # applymodel -> apply_classListen(7.2.a.3Listen)
			(1,14), # applymodel -> apply_classListenBranch(7.2.a.4ListenBranch)
			(1,15), # applymodel -> apply_classInst(7.2.a.5Inst)
			(1,16), # applymodel -> apply_classListen(7.2.a.6Listen)
			(3,17), # match classTransition(7.2.m.0Transition) -> association src
			(17,4), # associationsrc -> match_classTransition(7.2.m.1Vertex)
			(4,18), # match classVertex(7.2.m.1Vertex) -> association owningStateMachine
			(18,5), # associationowningStateMachine -> match_classVertex(7.2.m.2StateMachine)
			(5,19), # match classStateMachine(7.2.m.2StateMachine) -> association states
			(19,6), # associationstates -> match_classStateMachine(7.2.m.3State)
			(3,20), # match classTransition(7.2.m.0Transition) -> association triggers
			(20,7), # associationtriggers -> match_classTransition(7.2.m.4Trigger)
			(7,21), # match classTrigger(7.2.m.4Trigger) -> association signal
			(21,8), # associationsignal -> match_classTrigger(7.2.m.5Signal)
			(9,22), # match classState(7.2.m.6State) -> association transitions
			(22,3), # associationtransitions -> match_classState(7.2.m.0Transition)
			(10,23), # apply class ListenBranch(7.2.a.0ListenBranch) -> association p
			(23,11), # associationp -> apply_classSeq(7.2.a.1Seq)
			(11,24), # apply class Seq(7.2.a.1Seq) -> association p
			(24,12), # associationp -> apply_classTrigger(7.2.a.2Trigger)
			(11,25), # apply class Seq(7.2.a.1Seq) -> association p
			(25,13), # associationp -> apply_classListen(7.2.a.3Listen)
			(13,26), # apply class Listen(7.2.a.3Listen) -> association branches
			(26,14), # associationbranches -> apply_classListenBranch(7.2.a.4ListenBranch)
			(14,27), # apply class ListenBranch(7.2.a.4ListenBranch) -> association p
			(27,15), # associationp -> apply_classInst(7.2.a.5Inst)
			(16,28), # apply class Listen(7.2.a.6Listen) -> association branches
			(28,10), # associationbranches -> apply_classListenBranch(7.2.a.0ListenBranch)
			(15,29), # apply class Inst(7.2.m.0Transition) -> backward_association 
			(29,3), # backward_associationTransition -> match_class Transition(7.2.m.0Transition)
			(16,30), # apply class Listen(7.2.m.6State) -> backward_association 
			(30,9), # backward_associationState -> match_class State(7.2.m.6State)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = [((10,'channel'),(8,'name')),((12,'channel'),('constant','exit_in')),((14,'channel'),('constant','exack_in')),]
