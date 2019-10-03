from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HUnitConnectTownHall_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HUnitConnectTownHall_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HUnitConnectTownHall_CompleteLHS, self).__init__(name='HUnitConnectTownHall_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HUnitConnectTownHall_CompleteLHS')
		self["equations"] = []
		# Set the node attributes

		# match class Country(13.0.m.0Country) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__Country"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'13.0.m.0Country')

		# match class City(13.0.m.1City) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__City"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'13.0.m.1City')

		# apply class Community(13.0.a.0Community) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__Community"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'13.0.a.0Community')

		# apply class TownHall(13.0.a.1TownHall) node
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return True"""
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__TownHall"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'13.0.a.1TownHall')

		# match association Country--cities-->Citynode
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return attr_value == "cities" """
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__directLink_S"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'13.0.m.0Countryassoc413.0.m.1City')

		# apply association Community--townHalls-->TownHallnode
		self.add_node()
		self.vs[5]["MT_pre__attr1"] = """return attr_value == "townHalls" """
		self.vs[5]["MT_label__"] = """6"""
		self.vs[5]["mm__"] = """MT_pre__directLink_T"""
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'13.0.a.0Communityassoc513.0.a.1TownHall')

		# trace association Community--trace-->Countrynode
		self.add_node()
		self.vs[6]["MT_label__"] = """7"""
		self.vs[6]["mm__"] = """MT_pre__trace_link"""
		self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'13.0.a.0Communityassoc613.0.m.0Country')

		# trace association TownHall--trace-->Citynode
		self.add_node()
		self.vs[7]["MT_label__"] = """8"""
		self.vs[7]["mm__"] = """MT_pre__trace_link"""
		self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'13.0.a.1TownHallassoc713.0.m.1City')


		# Add the edges
		self.add_edges([
			(0,4), # match class Country(13.0.m.0Country) -> association cities
			(4,1), # association City -> match class City(13.0.m.1City)
			(2,5), # apply class Community(13.0.a.0Community) -> association townHalls
			(5,3), # association TownHall -> apply class TownHall(13.0.a.1TownHall)
			(2,6), # apply class Community(13.0.m.0Country) -> backward_association 
			(6,0), # backward_associationCountry -> match_class Country(13.0.m.0Country)
			(3,7), # apply class TownHall(13.0.m.1City) -> backward_association 
			(7,1), # backward_associationCity -> match_class City(13.0.m.1City)
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
		return attr_value == "cities"
		# define evaluation methods for each apply association.

	def eval_attr16(self, attr_value, this):
		return attr_value == "townHalls"

	def constraint(self, PreNode, graph):
		return True

