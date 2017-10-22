from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HPP1_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HPP1_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HPP1_CompleteLHS, self).__init__(name='HPP1_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HPP1_CompleteLHS')
		self["equations"] = []
		# Set the node attributes

		# match class SIBLING0(0.30.m.0SIBLING0) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__SIBLING0"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.30.m.0SIBLING0')

		# match class Transition(0.30.m.1Transition) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__Transition"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.30.m.1Transition')

		# match class Trigger(0.30.m.2Trigger) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__Trigger"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.30.m.2Trigger')

		# match class Signal(0.30.m.3Signal) node
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return True"""
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__Signal"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.30.m.3Signal')

		# apply class ListenBranch(0.30.a.0ListenBranch) node
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return True"""
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__ListenBranch"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.30.a.0ListenBranch')

		# apply class Inst(0.30.a.1Inst) node
		self.add_node()
		self.vs[5]["MT_pre__attr1"] = """return True"""
		self.vs[5]["MT_label__"] = """6"""
		self.vs[5]["mm__"] = """MT_pre__Inst"""
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.30.a.1Inst')

		# apply class Name(0.30.a.2Name) node
		self.add_node()
		self.vs[6]["MT_pre__attr1"] = """return True"""
		self.vs[6]["MT_label__"] = """7"""
		self.vs[6]["mm__"] = """MT_pre__Name"""
		self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.30.a.2Name')

		# apply class Name(0.30.a.3Name) node
		self.add_node()
		self.vs[7]["MT_pre__attr1"] = """return True"""
		self.vs[7]["MT_label__"] = """8"""
		self.vs[7]["mm__"] = """MT_pre__Name"""
		self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.30.a.3Name')

		# apply class Name(0.30.a.4Name) node
		self.add_node()
		self.vs[8]["MT_pre__attr1"] = """return True"""
		self.vs[8]["MT_label__"] = """9"""
		self.vs[8]["mm__"] = """MT_pre__Name"""
		self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.30.a.4Name')

		# apply class Name(0.30.a.5Name) node
		self.add_node()
		self.vs[9]["MT_pre__attr1"] = """return True"""
		self.vs[9]["MT_label__"] = """10"""
		self.vs[9]["mm__"] = """MT_pre__Name"""
		self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.30.a.5Name')

		# match association Transition--type-->SIBLING0node
		self.add_node()
		self.vs[10]["MT_pre__attr1"] = """return attr_value == "type" """
		self.vs[10]["MT_label__"] = """11"""
		self.vs[10]["mm__"] = """MT_pre__directLink_S"""
		self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.30.m.1Transitionassoc100.30.m.0SIBLING0')

		# match association Transition--triggers-->Triggernode
		self.add_node()
		self.vs[11]["MT_pre__attr1"] = """return attr_value == "triggers" """
		self.vs[11]["MT_label__"] = """12"""
		self.vs[11]["mm__"] = """MT_pre__directLink_S"""
		self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.30.m.1Transitionassoc110.30.m.2Trigger')

		# match association Trigger--signal-->Signalnode
		self.add_node()
		self.vs[12]["MT_pre__attr1"] = """return attr_value == "signal" """
		self.vs[12]["MT_label__"] = """13"""
		self.vs[12]["mm__"] = """MT_pre__directLink_S"""
		self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.30.m.2Triggerassoc120.30.m.3Signal')

		# apply association ListenBranch--p-->Instnode
		self.add_node()
		self.vs[13]["MT_pre__attr1"] = """return attr_value == "p" """
		self.vs[13]["MT_label__"] = """14"""
		self.vs[13]["mm__"] = """MT_pre__directLink_T"""
		self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.30.a.0ListenBranchassoc130.30.a.1Inst')

		# apply association Inst--channelNames-->Namenode
		self.add_node()
		self.vs[14]["MT_pre__attr1"] = """return attr_value == "channelNames" """
		self.vs[14]["MT_label__"] = """15"""
		self.vs[14]["mm__"] = """MT_pre__directLink_T"""
		self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.30.a.1Instassoc140.30.a.2Name')

		# apply association Inst--channelNames-->Namenode
		self.add_node()
		self.vs[15]["MT_pre__attr1"] = """return attr_value == "channelNames" """
		self.vs[15]["MT_label__"] = """16"""
		self.vs[15]["mm__"] = """MT_pre__directLink_T"""
		self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.30.a.1Instassoc150.30.a.3Name')

		# apply association Inst--channelNames-->Namenode
		self.add_node()
		self.vs[16]["MT_pre__attr1"] = """return attr_value == "channelNames" """
		self.vs[16]["MT_label__"] = """17"""
		self.vs[16]["mm__"] = """MT_pre__directLink_T"""
		self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.30.a.1Instassoc160.30.a.5Name')

		# apply association Inst--channelNames-->Namenode
		self.add_node()
		self.vs[17]["MT_pre__attr1"] = """return attr_value == "channelNames" """
		self.vs[17]["MT_label__"] = """18"""
		self.vs[17]["mm__"] = """MT_pre__directLink_T"""
		self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.30.a.1Instassoc170.30.a.4Name')

		# trace association Inst--trace-->Transitionnode
		self.add_node()
		self.vs[18]["MT_label__"] = """19"""
		self.vs[18]["mm__"] = """MT_pre__trace_link"""
		self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.30.a.1Instassoc180.30.m.1Transition')


		# Add the edges
		self.add_edges([
			(1,10), # match class Transition(0.30.m.1Transition) -> association type
			(10,0), # association SIBLING0 -> match class SIBLING0(0.30.m.0SIBLING0)
			(1,11), # match class Transition(0.30.m.1Transition) -> association triggers
			(11,2), # association Trigger -> match class Trigger(0.30.m.2Trigger)
			(2,12), # match class Trigger(0.30.m.2Trigger) -> association signal
			(12,3), # association Signal -> match class Signal(0.30.m.3Signal)
			(4,13), # apply class ListenBranch(0.30.a.0ListenBranch) -> association p
			(13,5), # association Inst -> apply class Inst(0.30.a.1Inst)
			(5,14), # apply class Inst(0.30.a.1Inst) -> association channelNames
			(14,6), # association Name -> apply class Name(0.30.a.2Name)
			(5,15), # apply class Inst(0.30.a.1Inst) -> association channelNames
			(15,7), # association Name -> apply class Name(0.30.a.3Name)
			(5,16), # apply class Inst(0.30.a.1Inst) -> association channelNames
			(16,9), # association Name -> apply class Name(0.30.a.5Name)
			(5,17), # apply class Inst(0.30.a.1Inst) -> association channelNames
			(17,8), # association Name -> apply class Name(0.30.a.4Name)
			(5,18), # apply class Inst(0.30.m.1Transition) -> backward_association 
			(18,1), # backward_associationTransition -> match_class Transition(0.30.m.1Transition)
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

		# define evaluation methods for each match association.

	def eval_attr111(self, attr_value, this):
		return attr_value == "type"
	def eval_attr112(self, attr_value, this):
		return attr_value == "triggers"
	def eval_attr113(self, attr_value, this):
		return attr_value == "signal"
		# define evaluation methods for each apply association.

	def eval_attr114(self, attr_value, this):
		return attr_value == "p"
	def eval_attr115(self, attr_value, this):
		return attr_value == "channelNames"
	def eval_attr116(self, attr_value, this):
		return attr_value == "channelNames"
	def eval_attr117(self, attr_value, this):
		return attr_value == "channelNames"
	def eval_attr118(self, attr_value, this):
		return attr_value == "channelNames"

	def constraint(self, PreNode, graph):
		return True

