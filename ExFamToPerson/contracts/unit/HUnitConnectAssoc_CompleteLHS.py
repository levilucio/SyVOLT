from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HUnitConnectAssoc_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HUnitConnectAssoc_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HUnitConnectAssoc_CompleteLHS, self).__init__(name='HUnitConnectAssoc_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HUnitConnectAssoc_CompleteLHS')
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

		# apply class Community(14.0.a.0Community) node
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return True"""
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__Community"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'14.0.a.0Community')

		# apply class Association(14.0.a.1Association) node
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return True"""
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__Association"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'14.0.a.1Association')

		# match association Country--cities-->Citynode
		self.add_node()
		self.vs[5]["MT_pre__attr1"] = """return attr_value == "cities" """
		self.vs[5]["MT_label__"] = """6"""
		self.vs[5]["mm__"] = """MT_pre__directLink_S"""
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'13.0.m.0Countryassoc513.0.m.1City')

		# match association Country--companies-->Companynode
		self.add_node()
		self.vs[6]["MT_pre__attr1"] = """return attr_value == "companies" """
		self.vs[6]["MT_label__"] = """7"""
		self.vs[6]["mm__"] = """MT_pre__directLink_S"""
		self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'13.0.m.0Countryassoc614.0.m.2Company')

		# match association City--companies-->Companynode
		self.add_node()
		self.vs[7]["MT_pre__attr1"] = """return attr_value == "companies" """
		self.vs[7]["MT_label__"] = """8"""
		self.vs[7]["mm__"] = """MT_pre__directLink_S"""
		self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'13.0.m.1Cityassoc714.0.m.2Company')

		# match association Company--isIn-->Citynode
		self.add_node()
		self.vs[8]["MT_pre__attr1"] = """return attr_value == "isIn" """
		self.vs[8]["MT_label__"] = """9"""
		self.vs[8]["mm__"] = """MT_pre__directLink_S"""
		self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'14.0.m.2Companyassoc813.0.m.1City')

		# apply association Community--associations-->Associationnode
		self.add_node()
		self.vs[9]["MT_pre__attr1"] = """return attr_value == "associations" """
		self.vs[9]["MT_label__"] = """10"""
		self.vs[9]["mm__"] = """MT_pre__directLink_T"""
		self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'14.0.a.0Communityassoc914.0.a.1Association')

		# trace association Community--trace-->Countrynode
		self.add_node()
		self.vs[10]["MT_label__"] = """11"""
		self.vs[10]["mm__"] = """MT_pre__trace_link"""
		self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'14.0.a.0Communityassoc1013.0.m.0Country')

		# trace association Association--trace-->Citynode
		self.add_node()
		self.vs[11]["MT_label__"] = """12"""
		self.vs[11]["mm__"] = """MT_pre__trace_link"""
		self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'14.0.a.1Associationassoc1113.0.m.1City')

		# trace association Association--trace-->Companynode
		self.add_node()
		self.vs[12]["MT_label__"] = """13"""
		self.vs[12]["mm__"] = """MT_pre__trace_link"""
		self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'14.0.a.1Associationassoc1214.0.m.2Company')


		# Add the edges
		self.add_edges([
			(0,5), # match class Country(13.0.m.0Country) -> association cities
			(5,2), # association City -> match class City(13.0.m.1City)
			(0,6), # match class Country(13.0.m.0Country) -> association companies
			(6,1), # association Company -> match class Company(14.0.m.2Company)
			(2,7), # match class City(13.0.m.1City) -> association companies
			(7,1), # association Company -> match class Company(14.0.m.2Company)
			(1,8), # match class Company(14.0.m.2Company) -> association isIn
			(8,2), # association City -> match class City(13.0.m.1City)
			(3,9), # apply class Community(14.0.a.0Community) -> association associations
			(9,4), # association Association -> apply class Association(14.0.a.1Association)
			(3,10), # apply class Community(13.0.m.0Country) -> backward_association 
			(10,0), # backward_associationCountry -> match_class Country(13.0.m.0Country)
			(4,11), # apply class Association(13.0.m.1City) -> backward_association 
			(11,2), # backward_associationCity -> match_class City(13.0.m.1City)
			(4,12), # apply class Association(14.0.m.2Company) -> backward_association 
			(12,1), # backward_associationCompany -> match_class Company(14.0.m.2Company)
		])


	# define evaluation methods for each match class.

	def eval_attr11(self, attr_value, this):
		return True

	def eval_attr12(self, attr_value, this):
		return True

	def eval_attr13(self, attr_value, this):
		return True

	# define evaluation methods for each apply class.

	def eval_attr14(self, attr_value, this):
		return True

	def eval_attr15(self, attr_value, this):
		return True

		# define evaluation methods for each match association.

	def eval_attr16(self, attr_value, this):
		return attr_value == "cities"
	def eval_attr17(self, attr_value, this):
		return attr_value == "companies"
	def eval_attr18(self, attr_value, this):
		return attr_value == "companies"
	def eval_attr19(self, attr_value, this):
		return attr_value == "isIn"
		# define evaluation methods for each apply association.

	def eval_attr110(self, attr_value, this):
		return attr_value == "associations"

	def constraint(self, PreNode, graph):
		return True

