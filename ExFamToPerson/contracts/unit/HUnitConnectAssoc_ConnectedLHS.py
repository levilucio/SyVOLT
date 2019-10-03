from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HUnitConnectAssoc_ConnectedLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HUnitConnectAssoc_ConnectedLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HUnitConnectAssoc_ConnectedLHS, self).__init__(name='HUnitConnectAssoc_ConnectedLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HUnitConnectAssoc_ConnectedLHS')
		self["equations"] = []
		# Set the node attributes

		# match class Country(13.0.m.0Country) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__Country"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'13.0.m.0Country')

		# match class Company(14.0.m.2Company) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__Company"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'14.0.m.2Company')

		# match class City(13.0.m.1City) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__City"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'13.0.m.1City')


		# match association Country--cities-->Citynode
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return attr_value == "cities" """
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__directLink_S"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'13.0.m.0Countryassoc313.0.m.1City')

		# match association Country--companies-->Companynode
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return attr_value == "companies" """
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__directLink_S"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'13.0.m.0Countryassoc414.0.m.2Company')

		# match association City--companies-->Companynode
		self.add_node()
		self.vs[5]["MT_pre__attr1"] = """return attr_value == "companies" """
		self.vs[5]["MT_label__"] = """6"""
		self.vs[5]["mm__"] = """MT_pre__directLink_S"""
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'13.0.m.1Cityassoc514.0.m.2Company')

		# match association Company--isIn-->Citynode
		self.add_node()
		self.vs[6]["MT_pre__attr1"] = """return attr_value == "isIn" """
		self.vs[6]["MT_label__"] = """7"""
		self.vs[6]["mm__"] = """MT_pre__directLink_S"""
		self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'14.0.m.2Companyassoc613.0.m.1City')

		# Add the edges
		self.add_edges([
			(0,3), # match class Country(13.0.m.0Country) -> association cities
			(3,2), # association City -> match class City(13.0.m.1City)
			(0,4), # match class Country(13.0.m.0Country) -> association companies
			(4,1), # association Company -> match class Company(14.0.m.2Company)
			(2,5), # match class City(13.0.m.1City) -> association companies
			(5,1), # association Company -> match class Company(14.0.m.2Company)
			(1,6), # match class Company(14.0.m.2Company) -> association isIn
			(6,2), # association City -> match class City(13.0.m.1City)
		])


	# define evaluation methods for each match class.

	def eval_attr11(self, attr_value, this):
		return True

	def eval_attr12(self, attr_value, this):
		return True

	def eval_attr13(self, attr_value, this):
		return True

	# define evaluation methods for each match association.

	def eval_attr14(self, attr_value, this):
		return attr_value == "cities"
	def eval_attr15(self, attr_value, this):
		return attr_value == "companies"
	def eval_attr16(self, attr_value, this):
		return attr_value == "companies"
	def eval_attr17(self, attr_value, this):
		return attr_value == "isIn"

	def constraint(self, PreNode, graph):
		return True

