from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HUnitConnectSon_ConnectedLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HUnitConnectSon_ConnectedLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HUnitConnectSon_ConnectedLHS, self).__init__(name='HUnitConnectSon_ConnectedLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HUnitConnectSon_ConnectedLHS')
		self["equations"] = []
		# Set the node attributes

		# match class Country(9.0.m.0Country) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__Country"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'9.0.m.0Country')

		# match class Family(9.0.m.1Family) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__Family"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'9.0.m.1Family')

		# match class Child(9.0.m.2Child) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__Child"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'9.0.m.2Child')


		# match association Country--families-->Familynode
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return attr_value == "families" """
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__directLink_S"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'9.0.m.0Countryassoc39.0.m.1Family')

		# match association Family--sons-->Parentnode
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return attr_value == "sons" """
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__directLink_S"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'9.0.m.1Familyassoc49.0.m.2Child')

		# Add the edges
		self.add_edges([
			(0,3), # match class Country(9.0.m.0Country) -> association families
			(3,1), # association Family -> match class Family(9.0.m.1Family)
			(1,4), # match class Family(9.0.m.1Family) -> association sons
			(4,2), # association Parent -> match class Parent(9.0.m.2Child)
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
		return attr_value == "families"
	def eval_attr15(self, attr_value, this):
		return attr_value == "sons"

	def constraint(self, PreNode, graph):
		return True

