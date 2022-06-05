from core.himesis import Himesis
import uuid

class HMapHeirarchyOfStates2HeirarchyOfProcs(Himesis):
	def __init__(self, *args, **kwargs):
		"""
		Creates the himesis graph representing the DSLTrans rule MapHeirarchyOfStates2HeirarchyOfProcs.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HMapHeirarchyOfStates2HeirarchyOfProcs, self).__init__(name='HMapHeirarchyOfStates2HeirarchyOfProcs', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """MapHeirarchyOfStates2HeirarchyOfProcs"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'MapHeirarchyOfStates2HeirarchyOfProcs')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """MapHeirarchyOfStates2HeirarchyOfProcs"""

		# match class State(3.1.m.0State) node
		self.add_node()
		self.vs[3]["mm__"] = """State"""
		self.vs[3]["attr1"] = """+"""

		# match class State(3.1.m.1State) node
		self.add_node()
		self.vs[4]["mm__"] = """State"""
		self.vs[4]["attr1"] = """+"""

		# apply class LocalDef(3.1.a.0LocalDef) node
		self.add_node()
		self.vs[5]["mm__"] = """LocalDef"""
		self.vs[5]["attr1"] = """1"""

		# apply class ProcDef(3.1.a.1ProcDef) node
		self.add_node()
		self.vs[6]["mm__"] = """ProcDef"""
		self.vs[6]["attr1"] = """1"""

		# match association State--states-->State node 
		self.add_node()
		self.vs[7]["attr1"] = """states"""
		self.vs[7]["mm__"] = """directLink_S"""

		# apply association LocalDef--def-->ProcDef node 
		self.add_node()
		self.vs[8]["attr1"] = """def"""
		self.vs[8]["mm__"] = """directLink_T"""

		# backward association LocalDef-->Statenode 
		self.add_node()
		self.vs[9]["mm__"] = """backward_link"""

		# backward association ProcDef-->Statenode 
		self.add_node()
		self.vs[10]["mm__"] = """backward_link"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class State(3.1.m.0State)
			(0,4), # matchmodel -> match_class State(3.1.m.1State)
			(1,5), # applymodel -> apply_classLocalDef(3.1.a.0LocalDef)
			(1,6), # applymodel -> apply_classProcDef(3.1.a.1ProcDef)
			(3,7), # match classState(3.1.m.0State) -> association states
			(7,4), # associationstates -> match_classState(3.1.m.1State)
			(5,8), # apply class LocalDef(3.1.a.0LocalDef) -> association def
			(8,6), # associationdef -> apply_classProcDef(3.1.a.1ProcDef)
			(5,9), # apply class LocalDef(3.1.m.0State) -> backward_association 
			(9,3), # backward_associationState -> match_class State(3.1.m.0State)
			(6,10), # apply class ProcDef(3.1.m.1State) -> backward_association 
			(10,4), # backward_associationState -> match_class State(3.1.m.1State)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = []
