from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HUnitConnectCommittee_ConnectedLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HUnitConnectCommittee_ConnectedLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HUnitConnectCommittee_ConnectedLHS, self).__init__(name='HUnitConnectCommittee_ConnectedLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HUnitConnectCommittee_ConnectedLHS')
		self["equations"] = []
		# Set the node attributes

		# match class Company(17.0.m.0Company) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__Company"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'17.0.m.0Company')

		# match class City(17.0.m.1City) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__City"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'17.0.m.1City')


		# match association Company--isIn-->Citynode
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return attr_value == "isIn" """
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__directLink_S"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'17.0.m.0Companyassoc217.0.m.1City')

		# match association City--companies-->Companynode
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return attr_value == "companies" """
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__directLink_S"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'17.0.m.1Cityassoc317.0.m.0Company')

		# Add the edges
		self.add_edges([
			(0,2), # match class Company(17.0.m.0Company) -> association isIn
			(2,1), # association City -> match class City(17.0.m.1City)
			(1,3), # match class City(17.0.m.1City) -> association companies
			(3,0), # association Company -> match class Company(17.0.m.0Company)
		])


	# define evaluation methods for each match class.

	def eval_attr11(self, attr_value, this):
		return True

	def eval_attr12(self, attr_value, this):
		return True

	# define evaluation methods for each match association.

	def eval_attr13(self, attr_value, this):
		return attr_value == "isIn"
	def eval_attr14(self, attr_value, this):
		return attr_value == "companies"

	def constraint(self, PreNode, graph):
		return True

