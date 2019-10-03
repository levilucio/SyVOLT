from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HUnitConnectDistricts_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HUnitConnectDistricts_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HUnitConnectDistricts_CompleteLHS, self).__init__(name='HUnitConnectDistricts_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HUnitConnectDistricts_CompleteLHS')
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

		# apply class TownHall(16.0.a.0TownHall) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__TownHall"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'16.0.a.0TownHall')

		# apply class District(16.0.a.1District) node
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return True"""
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__District"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'16.0.a.1District')

		# match association City--neighborhoods-->Neighborhoodnode
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return attr_value == "neighborhoods" """
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__directLink_S"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'16.0.m.0Cityassoc416.0.m.1Neighborhood')

		# apply association TownHall--districts-->Districtnode
		self.add_node()
		self.vs[5]["MT_pre__attr1"] = """return attr_value == "districts" """
		self.vs[5]["MT_label__"] = """6"""
		self.vs[5]["mm__"] = """MT_pre__directLink_T"""
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'16.0.a.0TownHallassoc516.0.a.1District')

		# trace association TownHall--trace-->Citynode
		self.add_node()
		self.vs[6]["MT_label__"] = """7"""
		self.vs[6]["mm__"] = """MT_pre__trace_link"""
		self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'16.0.a.0TownHallassoc616.0.m.0City')

		# trace association District--trace-->Neighborhoodnode
		self.add_node()
		self.vs[7]["MT_label__"] = """8"""
		self.vs[7]["mm__"] = """MT_pre__trace_link"""
		self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'16.0.a.1Districtassoc716.0.m.1Neighborhood')


		# Add the edges
		self.add_edges([
			(0,4), # match class City(16.0.m.0City) -> association neighborhoods
			(4,1), # association Neighborhood -> match class Neighborhood(16.0.m.1Neighborhood)
			(2,5), # apply class TownHall(16.0.a.0TownHall) -> association districts
			(5,3), # association District -> apply class District(16.0.a.1District)
			(2,6), # apply class TownHall(16.0.m.0City) -> backward_association 
			(6,0), # backward_associationCity -> match_class City(16.0.m.0City)
			(3,7), # apply class District(16.0.m.1Neighborhood) -> backward_association 
			(7,1), # backward_associationNeighborhood -> match_class Neighborhood(16.0.m.1Neighborhood)
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
		return attr_value == "neighborhoods"
		# define evaluation methods for each apply association.

	def eval_attr16(self, attr_value, this):
		return attr_value == "districts"

	def constraint(self, PreNode, graph):
		return True

