from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HUnitR07b_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HUnitR07b_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HUnitR07b_CompleteLHS, self).__init__(name='HUnitR07b_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HUnitR07b_CompleteLHS')
		self["equations"] = []
		# Set the node attributes

		# match class ExitPoint(7.1.m.0ExitPoint) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__ExitPoint"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.1.m.0ExitPoint')

		# match class Transition(7.1.m.1Transition) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__Transition"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.1.m.1Transition')

		# apply class Par(7.1.a.0Par) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__Par"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.1.a.0Par')

		# apply class Inst(7.1.a.1Inst) node
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return True"""
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__Inst"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.1.a.1Inst')

		# match association ExitPoint--outgoingTransitions-->Transitionnode
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return attr_value == "outgoingTransitions" """
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__directLink_S"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.1.m.0ExitPointassoc47.1.m.1Transition')

		# apply association Par--p-->Instnode
		self.add_node()
		self.vs[5]["MT_pre__attr1"] = """return attr_value == "p" """
		self.vs[5]["MT_label__"] = """6"""
		self.vs[5]["mm__"] = """MT_pre__directLink_T"""
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.1.a.0Parassoc57.1.a.1Inst')

		# trace association Par--trace-->ExitPointnode
		self.add_node()
		self.vs[6]["MT_label__"] = """7"""
		self.vs[6]["mm__"] = """MT_pre__trace_link"""
		self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.1.a.0Parassoc67.1.m.0ExitPoint')

		# trace association Inst--trace-->Transitionnode
		self.add_node()
		self.vs[7]["MT_label__"] = """8"""
		self.vs[7]["mm__"] = """MT_pre__trace_link"""
		self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.1.a.1Instassoc77.1.m.1Transition')


		# Add the edges
		self.add_edges([
			(0,4), # match class ExitPoint(7.1.m.0ExitPoint) -> association outgoingTransitions
			(4,1), # association Transition -> match class Transition(7.1.m.1Transition)
			(2,5), # apply class Par(7.1.a.0Par) -> association p
			(5,3), # association Inst -> apply class Inst(7.1.a.1Inst)
			(2,6), # apply class Par(7.1.m.0ExitPoint) -> backward_association 
			(6,0), # backward_associationExitPoint -> match_class ExitPoint(7.1.m.0ExitPoint)
			(3,7), # apply class Inst(7.1.m.1Transition) -> backward_association 
			(7,1), # backward_associationTransition -> match_class Transition(7.1.m.1Transition)
		])


	# define evaluation methods for each match class.

	def eval_attr11(self, attr_value, this):
		return True

	def eval_attr12(self, attr_value, this):
		return True

	# define evaluation methods for each apply class.

	def eval_attr13(self, attr_value, this):
		return True

	def eval_attr14(self, attr_value, this):
		return True

		# define evaluation methods for each match association.

	def eval_attr15(self, attr_value, this):
		return attr_value == "outgoingTransitions"
		# define evaluation methods for each apply association.

	def eval_attr16(self, attr_value, this):
		return attr_value == "p"

	def constraint(self, PreNode, graph):
		return True

