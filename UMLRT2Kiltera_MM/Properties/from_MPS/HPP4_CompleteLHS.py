from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HPP4_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self, *args, **kwargs):
		"""
		Creates the himesis graph representing the AToM3 model HPP4_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HPP4_CompleteLHS, self).__init__(name='HPP4_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HPP4_CompleteLHS')
		self["equations"] = []
		# Set the node attributes

		# match class State(0.33.m.0State) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__State"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.33.m.0State')

		# match class ExitPoint(0.33.m.1ExitPoint) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__ExitPoint"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.33.m.1ExitPoint')

		# match class Transition(0.33.m.2Transition) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__Transition"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.33.m.2Transition')

		# match class OUT2(0.33.m.3OUT2) node
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return True"""
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__OUT2"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.33.m.3OUT2')

		# apply class Par(0.33.a.0Par) node
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return True"""
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__Par"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.33.a.0Par')

		# apply class Inst(0.33.a.1Inst) node
		self.add_node()
		self.vs[5]["MT_pre__attr1"] = """return True"""
		self.vs[5]["MT_label__"] = """6"""
		self.vs[5]["mm__"] = """MT_pre__Inst"""
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.33.a.1Inst')

		# apply class Name(0.33.a.2Name) node
		self.add_node()
		self.vs[6]["MT_pre__attr1"] = """return True"""
		self.vs[6]["MT_label__"] = """7"""
		self.vs[6]["mm__"] = """MT_pre__Name"""
		self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.33.a.2Name')

		# apply class Trigger(0.33.a.3Trigger) node
		self.add_node()
		self.vs[7]["MT_pre__attr1"] = """return True"""
		self.vs[7]["MT_label__"] = """8"""
		self.vs[7]["mm__"] = """MT_pre__Trigger"""
		self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.33.a.3Trigger')

		# match association ExitPoint--outgoingTransitions-->Transitionnode
		self.add_node()
		self.vs[8]["MT_pre__attr1"] = """return attr_value == "outgoingTransitions" """
		self.vs[8]["MT_label__"] = """9"""
		self.vs[8]["mm__"] = """MT_pre__directLink_S"""
		self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.33.m.1ExitPointassoc80.33.m.2Transition')

		# match association Transition--type-->OUT2node
		self.add_node()
		self.vs[9]["MT_pre__attr1"] = """return attr_value == "type" """
		self.vs[9]["MT_label__"] = """10"""
		self.vs[9]["mm__"] = """MT_pre__directLink_S"""
		self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.33.m.2Transitionassoc90.33.m.3OUT2')

		# match association State--exitPoints-->ExitPointnode
		self.add_node()
		self.vs[10]["MT_pre__attr1"] = """return attr_value == "exitPoints" """
		self.vs[10]["MT_label__"] = """11"""
		self.vs[10]["mm__"] = """MT_pre__directLink_S"""
		self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.33.m.0Stateassoc100.33.m.1ExitPoint')

		# apply association Par--p-->Instnode
		self.add_node()
		self.vs[11]["MT_pre__attr1"] = """return attr_value == "p" """
		self.vs[11]["MT_label__"] = """12"""
		self.vs[11]["mm__"] = """MT_pre__directLink_T"""
		self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.33.a.0Parassoc110.33.a.1Inst')

		# apply association Inst--channelNames-->Namenode
		self.add_node()
		self.vs[12]["MT_pre__attr1"] = """return attr_value == "channelNames" """
		self.vs[12]["MT_label__"] = """13"""
		self.vs[12]["mm__"] = """MT_pre__directLink_T"""
		self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.33.a.1Instassoc120.33.a.2Name')

		# apply association Par--p-->Triggernode
		self.add_node()
		self.vs[13]["MT_pre__attr1"] = """return attr_value == "p" """
		self.vs[13]["MT_label__"] = """14"""
		self.vs[13]["mm__"] = """MT_pre__directLink_T"""
		self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.33.a.0Parassoc130.33.a.3Trigger')

		# trace association Par--trace-->ExitPointnode
		self.add_node()
		self.vs[14]["MT_label__"] = """15"""
		self.vs[14]["mm__"] = """MT_pre__trace_link"""
		self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.33.a.0Parassoc140.33.m.1ExitPoint')

		# trace association Trigger--trace-->ExitPointnode
		self.add_node()
		self.vs[15]["MT_label__"] = """16"""
		self.vs[15]["mm__"] = """MT_pre__trace_link"""
		self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.33.a.3Triggerassoc150.33.m.1ExitPoint')

		# trace association Inst--trace-->Transitionnode
		self.add_node()
		self.vs[16]["MT_label__"] = """17"""
		self.vs[16]["mm__"] = """MT_pre__trace_link"""
		self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.33.a.1Instassoc160.33.m.2Transition')

		# trace association Name--trace-->Transitionnode
		self.add_node()
		self.vs[17]["MT_label__"] = """18"""
		self.vs[17]["mm__"] = """MT_pre__trace_link"""
		self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.33.a.2Nameassoc170.33.m.2Transition')

		self['equations'].append(((7,'channel'),('constant','sh_in')))

		# Add the edges
		self.add_edges([
			(1,8), # match class ExitPoint(0.33.m.1ExitPoint) -> association outgoingTransitions
			(8,2), # association Transition -> match class Transition(0.33.m.2Transition)
			(2,9), # match class Transition(0.33.m.2Transition) -> association type
			(9,3), # association OUT2 -> match class OUT2(0.33.m.3OUT2)
			(0,10), # match class State(0.33.m.0State) -> association exitPoints
			(10,1), # association ExitPoint -> match class ExitPoint(0.33.m.1ExitPoint)
			(4,11), # apply class Par(0.33.a.0Par) -> association p
			(11,5), # association Inst -> apply class Inst(0.33.a.1Inst)
			(5,12), # apply class Inst(0.33.a.1Inst) -> association channelNames
			(12,6), # association Name -> apply class Name(0.33.a.2Name)
			(4,13), # apply class Par(0.33.a.0Par) -> association p
			(13,7), # association Trigger -> apply class Trigger(0.33.a.3Trigger)
			(4,14), # apply class Par(0.33.m.1ExitPoint) -> backward_association 
			(14,1), # backward_associationExitPoint -> match_class ExitPoint(0.33.m.1ExitPoint)
			(7,15), # apply class Trigger(0.33.m.1ExitPoint) -> backward_association 
			(15,1), # backward_associationExitPoint -> match_class ExitPoint(0.33.m.1ExitPoint)
			(5,16), # apply class Inst(0.33.m.2Transition) -> backward_association 
			(16,2), # backward_associationTransition -> match_class Transition(0.33.m.2Transition)
			(6,17), # apply class Name(0.33.m.2Transition) -> backward_association 
			(17,2), # backward_associationTransition -> match_class Transition(0.33.m.2Transition)
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

	def eval_attr18(self, attr_value, this):
		return True

		# define evaluation methods for each match association.

	def eval_attr19(self, attr_value, this):
		return attr_value == "outgoingTransitions"
	def eval_attr110(self, attr_value, this):
		return attr_value == "type"
	def eval_attr111(self, attr_value, this):
		return attr_value == "exitPoints"
		# define evaluation methods for each apply association.

	def eval_attr112(self, attr_value, this):
		return attr_value == "p"
	def eval_attr113(self, attr_value, this):
		return attr_value == "channelNames"
	def eval_attr114(self, attr_value, this):
		return attr_value == "p"

	def constraint(self, PreNode, graph):
		return True

