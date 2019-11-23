from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HUnitR05a_ConnectedLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HUnitR05a_ConnectedLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HUnitR05a_ConnectedLHS, self).__init__(name='HUnitR05a_ConnectedLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HUnitR05a_ConnectedLHS')
		self["equations"] = []
		# Set the node attributes

		# match class State(5.0.m.0State) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__State"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'5.0.m.0State')

		# match class ExitPoint(5.0.m.1ExitPoint) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__ExitPoint"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'5.0.m.1ExitPoint')


		# match association State--exitPoints-->ExitPointnode
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return attr_value == "exitPoints" """
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__directLink_S"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'5.0.m.0Stateassoc25.0.m.1ExitPoint')

		# Add the edges
		self.add_edges([
			(0,2), # match class State(5.0.m.0State) -> association exitPoints
			(2,1), # association ExitPoint -> match class ExitPoint(5.0.m.1ExitPoint)
		])


	# define evaluation methods for each match class.

	def eval_attr11(self, attr_value, this):
		return True

	def eval_attr12(self, attr_value, this):
		return True

	# define evaluation methods for each match association.

	def eval_attr13(self, attr_value, this):
		return attr_value == "exitPoints"

	def constraint(self, PreNode, graph):
		return True

