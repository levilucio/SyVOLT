from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HPP3_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self, *args, **kwargs):
		"""
		Creates the himesis graph representing the AToM3 model HPP3_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HPP3_CompleteLHS, self).__init__(name='HPP3_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HPP3_CompleteLHS')
		self["equations"] = []
		# Set the node attributes

		# match class State(0.32.m.0State) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__State"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.32.m.0State')

		# match class ExitPoint(0.32.m.1ExitPoint) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__ExitPoint"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.32.m.1ExitPoint')

		# match class Transition(0.32.m.2Transition) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__Transition"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.32.m.2Transition')

		# match class SIBLING0(0.32.m.3SIBLING0) node
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return True"""
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__SIBLING0"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.32.m.3SIBLING0')

		# apply class Par(0.32.a.0Par) node
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return True"""
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__Par"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.32.a.0Par')

		# apply class Inst(0.32.a.1Inst) node
		self.add_node()
		self.vs[5]["MT_pre__attr1"] = """return True"""
		self.vs[5]["MT_label__"] = """6"""
		self.vs[5]["mm__"] = """MT_pre__Inst"""
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.32.a.1Inst')

		# apply class Name(0.32.a.2Name) node
		self.add_node()
		self.vs[6]["MT_pre__attr1"] = """return True"""
		self.vs[6]["MT_label__"] = """7"""
		self.vs[6]["mm__"] = """MT_pre__Name"""
		self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.32.a.2Name')

		# apply class Name(0.32.a.3Name) node
		self.add_node()
		self.vs[7]["MT_pre__attr1"] = """return True"""
		self.vs[7]["MT_label__"] = """8"""
		self.vs[7]["mm__"] = """MT_pre__Name"""
		self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.32.a.3Name')

		# apply class Name(0.32.a.4Name) node
		self.add_node()
		self.vs[8]["MT_pre__attr1"] = """return True"""
		self.vs[8]["MT_label__"] = """9"""
		self.vs[8]["mm__"] = """MT_pre__Name"""
		self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.32.a.4Name')

		# apply class Name(0.32.a.5Name) node
		self.add_node()
		self.vs[9]["MT_pre__attr1"] = """return True"""
		self.vs[9]["MT_label__"] = """10"""
		self.vs[9]["mm__"] = """MT_pre__Name"""
		self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.32.a.5Name')

		# apply class Trigger(0.32.a.6Trigger) node
		self.add_node()
		self.vs[10]["MT_pre__attr1"] = """return True"""
		self.vs[10]["MT_label__"] = """11"""
		self.vs[10]["mm__"] = """MT_pre__Trigger"""
		self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.32.a.6Trigger')

		# match association ExitPoint--outgoingTransitions-->Transitionnode
		self.add_node()
		self.vs[11]["MT_pre__attr1"] = """return attr_value == "outgoingTransitions" """
		self.vs[11]["MT_label__"] = """12"""
		self.vs[11]["mm__"] = """MT_pre__directLink_S"""
		self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.32.m.1ExitPointassoc110.32.m.2Transition')

		# match association Transition--type-->SIBLING0node
		self.add_node()
		self.vs[12]["MT_pre__attr1"] = """return attr_value == "type" """
		self.vs[12]["MT_label__"] = """13"""
		self.vs[12]["mm__"] = """MT_pre__directLink_S"""
		self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.32.m.2Transitionassoc120.32.m.3SIBLING0')

		# match association State--exitPoints-->ExitPointnode
		self.add_node()
		self.vs[13]["MT_pre__attr1"] = """return attr_value == "exitPoints" """
		self.vs[13]["MT_label__"] = """14"""
		self.vs[13]["mm__"] = """MT_pre__directLink_S"""
		self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.32.m.0Stateassoc130.32.m.1ExitPoint')

		# apply association Par--p-->Instnode
		self.add_node()
		self.vs[14]["MT_pre__attr1"] = """return attr_value == "p" """
		self.vs[14]["MT_label__"] = """15"""
		self.vs[14]["mm__"] = """MT_pre__directLink_T"""
		self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.32.a.0Parassoc140.32.a.1Inst')

		# apply association Inst--channelNames-->Namenode
		self.add_node()
		self.vs[15]["MT_pre__attr1"] = """return attr_value == "channelNames" """
		self.vs[15]["MT_label__"] = """16"""
		self.vs[15]["mm__"] = """MT_pre__directLink_T"""
		self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.32.a.1Instassoc150.32.a.2Name')

		# apply association Inst--channelNames-->Namenode
		self.add_node()
		self.vs[16]["MT_pre__attr1"] = """return attr_value == "channelNames" """
		self.vs[16]["MT_label__"] = """17"""
		self.vs[16]["mm__"] = """MT_pre__directLink_T"""
		self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.32.a.1Instassoc160.32.a.3Name')

		# apply association Inst--channelNames-->Namenode
		self.add_node()
		self.vs[17]["MT_pre__attr1"] = """return attr_value == "channelNames" """
		self.vs[17]["MT_label__"] = """18"""
		self.vs[17]["mm__"] = """MT_pre__directLink_T"""
		self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.32.a.1Instassoc170.32.a.5Name')

		# apply association Inst--channelNames-->Namenode
		self.add_node()
		self.vs[18]["MT_pre__attr1"] = """return attr_value == "channelNames" """
		self.vs[18]["MT_label__"] = """19"""
		self.vs[18]["mm__"] = """MT_pre__directLink_T"""
		self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.32.a.1Instassoc180.32.a.4Name')

		# apply association Par--p-->Triggernode
		self.add_node()
		self.vs[19]["MT_pre__attr1"] = """return attr_value == "p" """
		self.vs[19]["MT_label__"] = """20"""
		self.vs[19]["mm__"] = """MT_pre__directLink_T"""
		self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.32.a.0Parassoc190.32.a.6Trigger')

		# trace association Par--trace-->ExitPointnode
		self.add_node()
		self.vs[20]["MT_label__"] = """21"""
		self.vs[20]["mm__"] = """MT_pre__trace_link"""
		self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.32.a.0Parassoc200.32.m.1ExitPoint')

		# trace association Trigger--trace-->ExitPointnode
		self.add_node()
		self.vs[21]["MT_label__"] = """22"""
		self.vs[21]["mm__"] = """MT_pre__trace_link"""
		self.vs[21]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.32.a.6Triggerassoc210.32.m.1ExitPoint')

		# trace association Inst--trace-->Transitionnode
		self.add_node()
		self.vs[22]["MT_label__"] = """23"""
		self.vs[22]["mm__"] = """MT_pre__trace_link"""
		self.vs[22]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.32.a.1Instassoc220.32.m.2Transition')

		# trace association Name--trace-->Transitionnode
		self.add_node()
		self.vs[23]["MT_label__"] = """24"""
		self.vs[23]["mm__"] = """MT_pre__trace_link"""
		self.vs[23]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.32.a.2Nameassoc230.32.m.2Transition')

		# trace association Name--trace-->Transitionnode
		self.add_node()
		self.vs[24]["MT_label__"] = """25"""
		self.vs[24]["mm__"] = """MT_pre__trace_link"""
		self.vs[24]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.32.a.3Nameassoc240.32.m.2Transition')

		# trace association Name--trace-->Transitionnode
		self.add_node()
		self.vs[25]["MT_label__"] = """26"""
		self.vs[25]["mm__"] = """MT_pre__trace_link"""
		self.vs[25]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.32.a.4Nameassoc250.32.m.2Transition')

		# trace association Name--trace-->Transitionnode
		self.add_node()
		self.vs[26]["MT_label__"] = """27"""
		self.vs[26]["mm__"] = """MT_pre__trace_link"""
		self.vs[26]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.32.a.5Nameassoc260.32.m.2Transition')

		self['equations'].append(((10,'channel'),('constant','sh_in')))

		# Add the edges
		self.add_edges([
			(1,11), # match class ExitPoint(0.32.m.1ExitPoint) -> association outgoingTransitions
			(11,2), # association Transition -> match class Transition(0.32.m.2Transition)
			(2,12), # match class Transition(0.32.m.2Transition) -> association type
			(12,3), # association SIBLING0 -> match class SIBLING0(0.32.m.3SIBLING0)
			(0,13), # match class State(0.32.m.0State) -> association exitPoints
			(13,1), # association ExitPoint -> match class ExitPoint(0.32.m.1ExitPoint)
			(4,14), # apply class Par(0.32.a.0Par) -> association p
			(14,5), # association Inst -> apply class Inst(0.32.a.1Inst)
			(5,15), # apply class Inst(0.32.a.1Inst) -> association channelNames
			(15,6), # association Name -> apply class Name(0.32.a.2Name)
			(5,16), # apply class Inst(0.32.a.1Inst) -> association channelNames
			(16,7), # association Name -> apply class Name(0.32.a.3Name)
			(5,17), # apply class Inst(0.32.a.1Inst) -> association channelNames
			(17,9), # association Name -> apply class Name(0.32.a.5Name)
			(5,18), # apply class Inst(0.32.a.1Inst) -> association channelNames
			(18,8), # association Name -> apply class Name(0.32.a.4Name)
			(4,19), # apply class Par(0.32.a.0Par) -> association p
			(19,10), # association Trigger -> apply class Trigger(0.32.a.6Trigger)
			(4,20), # apply class Par(0.32.m.1ExitPoint) -> backward_association 
			(20,1), # backward_associationExitPoint -> match_class ExitPoint(0.32.m.1ExitPoint)
			(10,21), # apply class Trigger(0.32.m.1ExitPoint) -> backward_association 
			(21,1), # backward_associationExitPoint -> match_class ExitPoint(0.32.m.1ExitPoint)
			(5,22), # apply class Inst(0.32.m.2Transition) -> backward_association 
			(22,2), # backward_associationTransition -> match_class Transition(0.32.m.2Transition)
			(6,23), # apply class Name(0.32.m.2Transition) -> backward_association 
			(23,2), # backward_associationTransition -> match_class Transition(0.32.m.2Transition)
			(7,24), # apply class Name(0.32.m.2Transition) -> backward_association 
			(24,2), # backward_associationTransition -> match_class Transition(0.32.m.2Transition)
			(8,25), # apply class Name(0.32.m.2Transition) -> backward_association 
			(25,2), # backward_associationTransition -> match_class Transition(0.32.m.2Transition)
			(9,26), # apply class Name(0.32.m.2Transition) -> backward_association 
			(26,2), # backward_associationTransition -> match_class Transition(0.32.m.2Transition)
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

	def eval_attr19(self, attr_value, this):
		return True

	def eval_attr110(self, attr_value, this):
		return True

	def eval_attr111(self, attr_value, this):
		return True

		# define evaluation methods for each match association.

	def eval_attr112(self, attr_value, this):
		return attr_value == "outgoingTransitions"
	def eval_attr113(self, attr_value, this):
		return attr_value == "type"
	def eval_attr114(self, attr_value, this):
		return attr_value == "exitPoints"
		# define evaluation methods for each apply association.

	def eval_attr115(self, attr_value, this):
		return attr_value == "p"
	def eval_attr116(self, attr_value, this):
		return attr_value == "channelNames"
	def eval_attr117(self, attr_value, this):
		return attr_value == "channelNames"
	def eval_attr118(self, attr_value, this):
		return attr_value == "channelNames"
	def eval_attr119(self, attr_value, this):
		return attr_value == "channelNames"
	def eval_attr120(self, attr_value, this):
		return attr_value == "p"

	def constraint(self, PreNode, graph):
		return True

