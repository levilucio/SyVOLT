from core.himesis import Himesis
import uuid

class HConnectOutputsOfExitPoint2BProcDefTransition2QInst(Himesis):
	def __init__(self, *args, **kwargs):
		"""
		Creates the himesis graph representing the DSLTrans rule ConnectOutputsOfExitPoint2BProcDefTransition2QInst.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HConnectOutputsOfExitPoint2BProcDefTransition2QInst, self).__init__(name='HConnectOutputsOfExitPoint2BProcDefTransition2QInst', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """ConnectOutputsOfExitPoint2BProcDefTransition2QInst"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConnectOutputsOfExitPoint2BProcDefTransition2QInst')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """ConnectOutputsOfExitPoint2BProcDefTransition2QInst"""

		# match class ExitPoint(7.1.m.0ExitPoint) node
		self.add_node()
		self.vs[3]["mm__"] = """ExitPoint"""
		self.vs[3]["attr1"] = """+"""

		# match class Transition(7.1.m.1Transition) node
		self.add_node()
		self.vs[4]["mm__"] = """Transition"""
		self.vs[4]["attr1"] = """1"""

		# apply class Par(7.1.a.0Par) node
		self.add_node()
		self.vs[5]["mm__"] = """Par"""
		self.vs[5]["attr1"] = """1"""

		# apply class Inst(7.1.a.1Inst) node
		self.add_node()
		self.vs[6]["mm__"] = """Inst"""
		self.vs[6]["attr1"] = """1"""

		# match association ExitPoint--outgoingTransitions-->Transition node 
		self.add_node()
		self.vs[7]["attr1"] = """outgoingTransitions"""
		self.vs[7]["mm__"] = """directLink_S"""

		# apply association Par--p-->Inst node 
		self.add_node()
		self.vs[8]["attr1"] = """p"""
		self.vs[8]["mm__"] = """directLink_T"""

		# backward association Par-->ExitPointnode 
		self.add_node()
		self.vs[9]["mm__"] = """backward_link"""

		# backward association Inst-->Transitionnode 
		self.add_node()
		self.vs[10]["mm__"] = """backward_link"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class ExitPoint(7.1.m.0ExitPoint)
			(0,4), # matchmodel -> match_class Transition(7.1.m.1Transition)
			(1,5), # applymodel -> apply_classPar(7.1.a.0Par)
			(1,6), # applymodel -> apply_classInst(7.1.a.1Inst)
			(3,7), # match classExitPoint(7.1.m.0ExitPoint) -> association outgoingTransitions
			(7,4), # associationoutgoingTransitions -> match_classExitPoint(7.1.m.1Transition)
			(5,8), # apply class Par(7.1.a.0Par) -> association p
			(8,6), # associationp -> apply_classInst(7.1.a.1Inst)
			(5,9), # apply class Par(7.1.m.0ExitPoint) -> backward_association 
			(9,3), # backward_associationExitPoint -> match_class ExitPoint(7.1.m.0ExitPoint)
			(6,10), # apply class Inst(7.1.m.1Transition) -> backward_association 
			(10,4), # backward_associationTransition -> match_class Transition(7.1.m.1Transition)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = []
