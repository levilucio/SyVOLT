from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HUnitConnectFather_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HUnitConnectFather_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HUnitConnectFather_CompleteLHS, self).__init__(name='HUnitConnectFather_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HUnitConnectFather_CompleteLHS')
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

		# match class Parent(9.0.m.2Parent) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__Parent"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'9.0.m.2Parent')

		# apply class Community(9.0.a.0Community) node
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return True"""
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__Community"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'9.0.a.0Community')

		# apply class Man(9.0.a.1Man) node
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return True"""
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__Man"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'9.0.a.1Man')

		# match association Country--families-->Familynode
		self.add_node()
		self.vs[5]["MT_pre__attr1"] = """return attr_value == "families" """
		self.vs[5]["MT_label__"] = """6"""
		self.vs[5]["mm__"] = """MT_pre__directLink_S"""
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'9.0.m.0Countryassoc59.0.m.1Family')

		# match association Family--fathers-->Parentnode
		self.add_node()
		self.vs[6]["MT_pre__attr1"] = """return attr_value == "fathers" """
		self.vs[6]["MT_label__"] = """7"""
		self.vs[6]["mm__"] = """MT_pre__directLink_S"""
		self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'9.0.m.1Familyassoc69.0.m.2Parent')

		# apply association Community--persons-->Mannode
		self.add_node()
		self.vs[7]["MT_pre__attr1"] = """return attr_value == "persons" """
		self.vs[7]["MT_label__"] = """8"""
		self.vs[7]["mm__"] = """MT_pre__directLink_T"""
		self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'9.0.a.0Communityassoc79.0.a.1Man')

		# trace association Community--trace-->Countrynode
		self.add_node()
		self.vs[8]["MT_label__"] = """9"""
		self.vs[8]["mm__"] = """MT_pre__trace_link"""
		self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'9.0.a.0Communityassoc89.0.m.0Country')

		# trace association Man--trace-->Parentnode
		self.add_node()
		self.vs[9]["MT_label__"] = """10"""
		self.vs[9]["mm__"] = """MT_pre__trace_link"""
		self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'9.0.a.1Manassoc99.0.m.2Parent')


		# Add the edges
		self.add_edges([
			(0,5), # match class Country(9.0.m.0Country) -> association families
			(5,1), # association Family -> match class Family(9.0.m.1Family)
			(1,6), # match class Family(9.0.m.1Family) -> association fathers
			(6,2), # association Parent -> match class Parent(9.0.m.2Parent)
			(3,7), # apply class Community(9.0.a.0Community) -> association persons
			(7,4), # association Man -> apply class Man(9.0.a.1Man)
			(3,8), # apply class Community(9.0.m.0Country) -> backward_association 
			(8,0), # backward_associationCountry -> match_class Country(9.0.m.0Country)
			(4,9), # apply class Man(9.0.m.2Parent) -> backward_association 
			(9,2), # backward_associationParent -> match_class Parent(9.0.m.2Parent)
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
		return attr_value == "families"
	def eval_attr17(self, attr_value, this):
		return attr_value == "fathers"
		# define evaluation methods for each apply association.

	def eval_attr18(self, attr_value, this):
		return attr_value == "persons"

	def constraint(self, PreNode, graph):
		return True

