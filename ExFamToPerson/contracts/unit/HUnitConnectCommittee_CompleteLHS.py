from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HUnitConnectCommittee_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HUnitConnectCommittee_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HUnitConnectCommittee_CompleteLHS, self).__init__(name='HUnitConnectCommittee_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HUnitConnectCommittee_CompleteLHS')
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

		# apply class Association(17.0.a.0Association) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__Association"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'17.0.a.0Association')

		# apply class Committee(17.0.a.1Committee) node
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return True"""
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__Committee"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'17.0.a.1Committee')

		# match association Company--isIn-->Citynode
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return attr_value == "isIn" """
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__directLink_S"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'17.0.m.0Companyassoc417.0.m.1City')

		# match association City--companies-->Companynode
		self.add_node()
		self.vs[5]["MT_pre__attr1"] = """return attr_value == "companies" """
		self.vs[5]["MT_label__"] = """6"""
		self.vs[5]["mm__"] = """MT_pre__directLink_S"""
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'17.0.m.1Cityassoc517.0.m.0Company')

		# apply association Association--committee-->Committeenode
		self.add_node()
		self.vs[6]["MT_pre__attr1"] = """return attr_value == "committee" """
		self.vs[6]["MT_label__"] = """7"""
		self.vs[6]["mm__"] = """MT_pre__directLink_T"""
		self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'17.0.a.0Associationassoc617.0.a.1Committee')

		# trace association Association--trace-->Companynode
		self.add_node()
		self.vs[7]["MT_label__"] = """8"""
		self.vs[7]["mm__"] = """MT_pre__trace_link"""
		self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'17.0.a.0Associationassoc717.0.m.0Company')

		# trace association Association--trace-->Citynode
		self.add_node()
		self.vs[8]["MT_label__"] = """9"""
		self.vs[8]["mm__"] = """MT_pre__trace_link"""
		self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'17.0.a.0Associationassoc817.0.m.1City')

		# trace association Committee--trace-->Citynode
		self.add_node()
		self.vs[9]["MT_label__"] = """10"""
		self.vs[9]["mm__"] = """MT_pre__trace_link"""
		self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'17.0.a.1Committeeassoc917.0.m.1City')


		# Add the edges
		self.add_edges([
			(0,4), # match class Company(17.0.m.0Company) -> association isIn
			(4,1), # association City -> match class City(17.0.m.1City)
			(1,5), # match class City(17.0.m.1City) -> association companies
			(5,0), # association Company -> match class Company(17.0.m.0Company)
			(2,6), # apply class Association(17.0.a.0Association) -> association committee
			(6,3), # association Committee -> apply class Committee(17.0.a.1Committee)
			(2,7), # apply class Association(17.0.m.0Company) -> backward_association 
			(7,0), # backward_associationCompany -> match_class Company(17.0.m.0Company)
			(2,8), # apply class Association(17.0.m.1City) -> backward_association 
			(8,1), # backward_associationCity -> match_class City(17.0.m.1City)
			(3,9), # apply class Committee(17.0.m.1City) -> backward_association 
			(9,1), # backward_associationCity -> match_class City(17.0.m.1City)
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
		return attr_value == "isIn"
	def eval_attr16(self, attr_value, this):
		return attr_value == "companies"
		# define evaluation methods for each apply association.

	def eval_attr17(self, attr_value, this):
		return attr_value == "committee"

	def constraint(self, PreNode, graph):
		return True

