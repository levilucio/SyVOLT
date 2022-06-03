from core.himesis import Himesis
import uuid

class HConnectOPState2CProcDefTransition2InstotherInTransitions(Himesis):
	def __init__(self, *args, **kwargs):
		"""
		Creates the himesis graph representing the DSLTrans rule ConnectOPState2CProcDefTransition2InstotherInTransitions.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HConnectOPState2CProcDefTransition2InstotherInTransitions, self).__init__(name='HConnectOPState2CProcDefTransition2InstotherInTransitions', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """ConnectOPState2CProcDefTransition2InstotherInTransitions"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConnectOPState2CProcDefTransition2InstotherInTransitions')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """ConnectOPState2CProcDefTransition2InstotherInTransitions"""

		# match class Transition(7.3.m.0Transition) node
		self.add_node()
		self.vs[3]["mm__"] = """Transition"""
		self.vs[3]["attr1"] = """+"""

		# match class IN1(7.3.m.1IN1) node
		self.add_node()
		self.vs[4]["mm__"] = """IN1"""
		self.vs[4]["attr1"] = """+"""

		# match class State(7.3.m.2State) node
		self.add_node()
		self.vs[5]["mm__"] = """State"""
		self.vs[5]["attr1"] = """+"""

		# match class Vertex(7.3.m.3Vertex) node
		self.add_node()
		self.vs[6]["mm__"] = """Vertex"""
		self.vs[6]["attr1"] = """+"""

		# apply class ConditionSet(7.3.a.0ConditionSet) node
		self.add_node()
		self.vs[7]["mm__"] = """ConditionSet"""
		self.vs[7]["attr1"] = """1"""

		# apply class ConditionBranch(7.3.a.1ConditionBranch) node
		self.add_node()
		self.vs[8]["mm__"] = """ConditionBranch"""
		self.vs[8]["attr1"] = """1"""

		# apply class Expr(7.3.a.2Expr) node
		self.add_node()
		self.vs[9]["mm__"] = """Expr"""
		self.vs[9]["attr1"] = """1"""

		# apply class Inst(7.3.a.3Inst) node
		self.add_node()
		self.vs[10]["mm__"] = """Inst"""
		self.vs[10]["attr1"] = """1"""

		# match association State--transitions-->Transition node 
		self.add_node()
		self.vs[11]["attr1"] = """transitions"""
		self.vs[11]["mm__"] = """directLink_S"""

		# match association Transition--type-->IN1 node 
		self.add_node()
		self.vs[12]["attr1"] = """type"""
		self.vs[12]["mm__"] = """directLink_S"""

		# match association Transition--src-->Vertex node 
		self.add_node()
		self.vs[13]["attr1"] = """src"""
		self.vs[13]["mm__"] = """directLink_S"""

		# apply association ConditionSet--branches-->ConditionBranch node 
		self.add_node()
		self.vs[14]["attr1"] = """branches"""
		self.vs[14]["mm__"] = """directLink_T"""

		# apply association ConditionBranch--if-->Expr node 
		self.add_node()
		self.vs[15]["attr1"] = """if"""
		self.vs[15]["mm__"] = """directLink_T"""

		# apply association ConditionBranch--then-->Inst node 
		self.add_node()
		self.vs[16]["attr1"] = """then"""
		self.vs[16]["mm__"] = """directLink_T"""

		# backward association ConditionSet-->Statenode 
		self.add_node()
		self.vs[17]["mm__"] = """backward_link"""

		# backward association Inst-->Transitionnode 
		self.add_node()
		self.vs[18]["mm__"] = """backward_link"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class Transition(7.3.m.0Transition)
			(0,4), # matchmodel -> match_class IN1(7.3.m.1IN1)
			(0,5), # matchmodel -> match_class State(7.3.m.2State)
			(0,6), # matchmodel -> match_class Vertex(7.3.m.3Vertex)
			(1,7), # applymodel -> apply_classConditionSet(7.3.a.0ConditionSet)
			(1,8), # applymodel -> apply_classConditionBranch(7.3.a.1ConditionBranch)
			(1,9), # applymodel -> apply_classExpr(7.3.a.2Expr)
			(1,10), # applymodel -> apply_classInst(7.3.a.3Inst)
			(5,11), # match classState(7.3.m.2State) -> association transitions
			(11,3), # associationtransitions -> match_classState(7.3.m.0Transition)
			(3,12), # match classTransition(7.3.m.0Transition) -> association type
			(12,4), # associationtype -> match_classTransition(7.3.m.1IN1)
			(3,13), # match classTransition(7.3.m.0Transition) -> association src
			(13,6), # associationsrc -> match_classTransition(7.3.m.3Vertex)
			(7,14), # apply class ConditionSet(7.3.a.0ConditionSet) -> association branches
			(14,8), # associationbranches -> apply_classConditionBranch(7.3.a.1ConditionBranch)
			(8,15), # apply class ConditionBranch(7.3.a.1ConditionBranch) -> association if
			(15,9), # associationif -> apply_classExpr(7.3.a.2Expr)
			(8,16), # apply class ConditionBranch(7.3.a.1ConditionBranch) -> association then
			(16,10), # associationthen -> apply_classInst(7.3.a.3Inst)
			(7,17), # apply class ConditionSet(7.3.m.2State) -> backward_association 
			(17,5), # backward_associationState -> match_class State(7.3.m.2State)
			(10,18), # apply class Inst(7.3.m.0Transition) -> backward_association 
			(18,3), # backward_associationTransition -> match_class Transition(7.3.m.0Transition)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = [((9,'literal'),('concat',(('constant','enp=A'),('concat',((6,'name'),('constant','A')))))),]
