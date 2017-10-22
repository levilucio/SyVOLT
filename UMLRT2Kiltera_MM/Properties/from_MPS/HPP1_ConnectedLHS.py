from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HPP1_ConnectedLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HPP1_ConnectedLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HPP1_ConnectedLHS, self).__init__(name='HPP1_ConnectedLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HPP1_ConnectedLHS')
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


		# match association Transition--type-->SIBLING0node
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return attr_value == "type" """
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__directLink_S"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.30.m.1Transitionassoc40.30.m.0SIBLING0')

		# match association Transition--triggers-->Triggernode
		self.add_node()
		self.vs[5]["MT_pre__attr1"] = """return attr_value == "triggers" """
		self.vs[5]["MT_label__"] = """6"""
		self.vs[5]["mm__"] = """MT_pre__directLink_S"""
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.30.m.1Transitionassoc50.30.m.2Trigger')

		# match association Trigger--signal-->Signalnode
		self.add_node()
		self.vs[6]["MT_pre__attr1"] = """return attr_value == "signal" """
		self.vs[6]["MT_label__"] = """7"""
		self.vs[6]["mm__"] = """MT_pre__directLink_S"""
		self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.30.m.2Triggerassoc60.30.m.3Signal')

		# Add the edges
		self.add_edges([
			(1,4), # match class Transition(0.30.m.1Transition) -> association type
			(4,0), # association SIBLING0 -> match class SIBLING0(0.30.m.0SIBLING0)
			(1,5), # match class Transition(0.30.m.1Transition) -> association triggers
			(5,2), # association Trigger -> match class Trigger(0.30.m.2Trigger)
			(2,6), # match class Trigger(0.30.m.2Trigger) -> association signal
			(6,3), # association Signal -> match class Signal(0.30.m.3Signal)
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

	# define evaluation methods for each match association.

	def eval_attr15(self, attr_value, this):
		return attr_value == "type"
	def eval_attr16(self, attr_value, this):
		return attr_value == "triggers"
	def eval_attr17(self, attr_value, this):
		return attr_value == "signal"

	def constraint(self, PreNode, graph):
		return True

