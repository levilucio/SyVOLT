from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HUnitR07d_ConnectedLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HUnitR07d_ConnectedLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HUnitR07d_ConnectedLHS, self).__init__(name='HUnitR07d_ConnectedLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HUnitR07d_ConnectedLHS')
		self["equations"] = []
		# Set the node attributes

		# match class Transition(7.3.m.0Transition) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__Transition"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.3.m.0Transition')

		# match class IN1(7.3.m.1IN1) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__IN1"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.3.m.1IN1')

		# match class State(7.3.m.2State) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__State"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.3.m.2State')

		# match class Vertex(7.3.m.3Vertex) node
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return True"""
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__Vertex"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.3.m.3Vertex')


		# match association State--transitions-->Transitionnode
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return attr_value == "transitions" """
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__directLink_S"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.3.m.2Stateassoc47.3.m.0Transition')

		# match association Transition--type-->IN1node
		self.add_node()
		self.vs[5]["MT_pre__attr1"] = """return attr_value == "type" """
		self.vs[5]["MT_label__"] = """6"""
		self.vs[5]["mm__"] = """MT_pre__directLink_S"""
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.3.m.0Transitionassoc57.3.m.1IN1')

		# match association Transition--src-->Vertexnode
		self.add_node()
		self.vs[6]["MT_pre__attr1"] = """return attr_value == "src" """
		self.vs[6]["MT_label__"] = """7"""
		self.vs[6]["mm__"] = """MT_pre__directLink_S"""
		self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.3.m.0Transitionassoc67.3.m.3Vertex')

		# Add the edges
		self.add_edges([
			(2,4), # match class State(7.3.m.2State) -> association transitions
			(4,0), # association Transition -> match class Transition(7.3.m.0Transition)
			(0,5), # match class Transition(7.3.m.0Transition) -> association type
			(5,1), # association IN1 -> match class IN1(7.3.m.1IN1)
			(0,6), # match class Transition(7.3.m.0Transition) -> association src
			(6,3), # association Vertex -> match class Vertex(7.3.m.3Vertex)
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
		return attr_value == "transitions"
	def eval_attr16(self, attr_value, this):
		return attr_value == "type"
	def eval_attr17(self, attr_value, this):
		return attr_value == "src"

	def constraint(self, PreNode, graph):
		return True

