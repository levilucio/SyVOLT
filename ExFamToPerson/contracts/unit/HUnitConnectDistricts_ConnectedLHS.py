from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HUnitConnectDistricts_ConnectedLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HUnitConnectDistricts_ConnectedLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HUnitConnectDistricts_ConnectedLHS, self).__init__(name='HUnitConnectDistricts_ConnectedLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HUnitConnectDistricts_ConnectedLHS')
		self["equations"] = []
		# Set the node attributes

		# match class City(16.0.m.0City) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__City"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'16.0.m.0City')

		# match class Neighborhood(16.0.m.1Neighborhood) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__Neighborhood"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'16.0.m.1Neighborhood')


		# match association City--neighborhoods-->Neighborhoodnode
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return attr_value == "neighborhoods" """
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__directLink_S"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'16.0.m.0Cityassoc216.0.m.1Neighborhood')

		# Add the edges
		self.add_edges([
			(0,2), # match class City(16.0.m.0City) -> association neighborhoods
			(2,1), # association Neighborhood -> match class Neighborhood(16.0.m.1Neighborhood)
		])


	# define evaluation methods for each match class.

	def eval_attr11(self, attr_value, this):
		return True

	def eval_attr12(self, attr_value, this):
		return True

	# define evaluation methods for each match association.

	def eval_attr13(self, attr_value, this):
		return attr_value == "neighborhoods"

	def constraint(self, PreNode, graph):
		return True

