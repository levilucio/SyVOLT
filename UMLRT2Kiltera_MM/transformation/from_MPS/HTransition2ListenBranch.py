from core.himesis import Himesis
import uuid

class HTransition2ListenBranch(Himesis):
	def __init__(self, *args, **kwargs):
		"""
		Creates the himesis graph representing the DSLTrans rule Transition2ListenBranch.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HTransition2ListenBranch, self).__init__(name='HTransition2ListenBranch', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """Transition2ListenBranch"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Transition2ListenBranch')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """Transition2ListenBranch"""

		# match class State(7.0.m.0State) node
		self.add_node()
		self.vs[3]["mm__"] = """State"""
		self.vs[3]["attr1"] = """+"""

		# match class Transition(7.0.m.1Transition) node
		self.add_node()
		self.vs[4]["mm__"] = """Transition"""
		self.vs[4]["attr1"] = """+"""

		# match class Trigger(7.0.m.2Trigger) node
		self.add_node()
		self.vs[5]["mm__"] = """Trigger"""
		self.vs[5]["attr1"] = """1"""

		# match class Signal(7.0.m.3Signal) node
		self.add_node()
		self.vs[6]["mm__"] = """Signal"""
		self.vs[6]["attr1"] = """1"""

		# apply class Listen(7.0.a.0Listen) node
		self.add_node()
		self.vs[7]["mm__"] = """Listen"""
		self.vs[7]["attr1"] = """1"""

		# apply class ListenBranch(7.0.a.1ListenBranch) node
		self.add_node()
		self.vs[8]["mm__"] = """ListenBranch"""
		self.vs[8]["attr1"] = """1"""

		# apply class Inst(7.0.a.2Inst) node
		self.add_node()
		self.vs[9]["mm__"] = """Inst"""
		self.vs[9]["attr1"] = """1"""

		# match association State--transitions-->Transition node 
		self.add_node()
		self.vs[10]["attr1"] = """transitions"""
		self.vs[10]["mm__"] = """directLink_S"""

		# match association Transition--triggers-->Trigger node 
		self.add_node()
		self.vs[11]["attr1"] = """triggers"""
		self.vs[11]["mm__"] = """directLink_S"""

		# match association Trigger--signal-->Signal node 
		self.add_node()
		self.vs[12]["attr1"] = """signal"""
		self.vs[12]["mm__"] = """directLink_S"""

		# apply association Listen--branches-->ListenBranch node 
		self.add_node()
		self.vs[13]["attr1"] = """branches"""
		self.vs[13]["mm__"] = """directLink_T"""

		# apply association ListenBranch--p-->Inst node 
		self.add_node()
		self.vs[14]["attr1"] = """p"""
		self.vs[14]["mm__"] = """directLink_T"""

		# backward association Listen-->Statenode 
		self.add_node()
		self.vs[15]["mm__"] = """backward_link"""

		# backward association Inst-->Transitionnode 
		self.add_node()
		self.vs[16]["mm__"] = """backward_link"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class State(7.0.m.0State)
			(0,4), # matchmodel -> match_class Transition(7.0.m.1Transition)
			(0,5), # matchmodel -> match_class Trigger(7.0.m.2Trigger)
			(0,6), # matchmodel -> match_class Signal(7.0.m.3Signal)
			(1,7), # applymodel -> apply_classListen(7.0.a.0Listen)
			(1,8), # applymodel -> apply_classListenBranch(7.0.a.1ListenBranch)
			(1,9), # applymodel -> apply_classInst(7.0.a.2Inst)
			(3,10), # match classState(7.0.m.0State) -> association transitions
			(10,4), # associationtransitions -> match_classState(7.0.m.1Transition)
			(4,11), # match classTransition(7.0.m.1Transition) -> association triggers
			(11,5), # associationtriggers -> match_classTransition(7.0.m.2Trigger)
			(5,12), # match classTrigger(7.0.m.2Trigger) -> association signal
			(12,6), # associationsignal -> match_classTrigger(7.0.m.3Signal)
			(7,13), # apply class Listen(7.0.a.0Listen) -> association branches
			(13,8), # associationbranches -> apply_classListenBranch(7.0.a.1ListenBranch)
			(8,14), # apply class ListenBranch(7.0.a.1ListenBranch) -> association p
			(14,9), # associationp -> apply_classInst(7.0.a.2Inst)
			(7,15), # apply class Listen(7.0.m.0State) -> backward_association 
			(15,3), # backward_associationState -> match_class State(7.0.m.0State)
			(9,16), # apply class Inst(7.0.m.1Transition) -> backward_association 
			(16,4), # backward_associationTransition -> match_class Transition(7.0.m.1Transition)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = [((8,'channel'),(6,'name')),]
