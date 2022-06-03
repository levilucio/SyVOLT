from core.himesis import Himesis
import uuid

class HBasicStateNoOutgoing2ProcDef(Himesis):
	def __init__(self, *args, **kwargs):
		"""
		Creates the himesis graph representing the DSLTrans rule BasicStateNoOutgoing2ProcDef.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HBasicStateNoOutgoing2ProcDef, self).__init__(name='HBasicStateNoOutgoing2ProcDef', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """BasicStateNoOutgoing2ProcDef"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'BasicStateNoOutgoing2ProcDef')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """BasicStateNoOutgoing2ProcDef"""

		# match class State(4.0.m.0State) node
		self.add_node()
		self.vs[3]["mm__"] = """State"""
		self.vs[3]["attr1"] = """+"""

		# apply class ProcDef(4.0.a.0ProcDef) node
		self.add_node()
		self.vs[4]["mm__"] = """ProcDef"""
		self.vs[4]["attr1"] = """1"""

		# apply class Null(4.0.a.1Null) node
		self.add_node()
		self.vs[5]["mm__"] = """Null"""
		self.vs[5]["attr1"] = """1"""

		# apply association ProcDef--p-->Null node 
		self.add_node()
		self.vs[6]["attr1"] = """p"""
		self.vs[6]["mm__"] = """directLink_T"""

		# backward association ProcDef-->Statenode 
		self.add_node()
		self.vs[7]["mm__"] = """backward_link"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class State(4.0.m.0State)
			(1,4), # applymodel -> apply_classProcDef(4.0.a.0ProcDef)
			(1,5), # applymodel -> apply_classNull(4.0.a.1Null)
			(4,6), # apply class ProcDef(4.0.a.0ProcDef) -> association p
			(6,5), # associationp -> apply_classNull(4.0.a.1Null)
			(4,7), # apply class ProcDef(4.0.m.0State) -> backward_association 
			(7,3), # backward_associationState -> match_class State(4.0.m.0State)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = []
