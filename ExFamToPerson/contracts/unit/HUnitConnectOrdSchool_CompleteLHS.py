from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HUnitConnectOrdSchool_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HUnitConnectOrdSchool_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HUnitConnectOrdSchool_CompleteLHS, self).__init__(name='HUnitConnectOrdSchool_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HUnitConnectOrdSchool_CompleteLHS')
		self["equations"] = []
		# Set the node attributes

		# match class Neighborhood(18.0.m.0Neighborhood) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__Neighborhood"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'18.0.m.0Neighborhood')

		# match class School(18.0.m.1School) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__School"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'18.0.m.1School')

		# match class Service(18.0.m.2Service) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__Service"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'18.0.m.2Service')

		# match class Child(18.0.m.3Child) node
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return True"""
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__Child"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'18.0.m.3Child')

		# apply class District(18.0.a.0District) node
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return True"""
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__District"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'18.0.a.0District')

		# apply class OrdinaryFacility(18.0.a.1OrdinaryFacility) node
		self.add_node()
		self.vs[5]["MT_pre__attr1"] = """return True"""
		self.vs[5]["MT_label__"] = """6"""
		self.vs[5]["mm__"] = """MT_pre__OrdinaryFacility"""
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'18.0.a.1OrdinaryFacility')

		# apply class Person(18.0.a.2Person) node
		self.add_node()
		self.vs[6]["MT_pre__attr1"] = """return True"""
		self.vs[6]["MT_label__"] = """7"""
		self.vs[6]["mm__"] = """MT_pre__Person"""
		self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'18.0.a.2Person')

		# match association Neighborhood--schools-->Schoolnode
		self.add_node()
		self.vs[7]["MT_pre__attr1"] = """return attr_value == "schools" """
		self.vs[7]["MT_label__"] = """8"""
		self.vs[7]["mm__"] = """MT_pre__directLink_S"""
		self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'18.0.m.0Neighborhoodassoc718.0.m.1School')

		# match association School--ordinary-->Servicenode
		self.add_node()
		self.vs[8]["MT_pre__attr1"] = """return attr_value == "ordinary" """
		self.vs[8]["MT_label__"] = """9"""
		self.vs[8]["mm__"] = """MT_pre__directLink_S"""
		self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'18.0.m.1Schoolassoc818.0.m.2Service')

		# match association School--students-->Childnode
		self.add_node()
		self.vs[9]["MT_pre__attr1"] = """return attr_value == "students" """
		self.vs[9]["MT_label__"] = """10"""
		self.vs[9]["mm__"] = """MT_pre__directLink_S"""
		self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'18.0.m.1Schoolassoc918.0.m.3Child')

		# match association Child--goesTo-->Schoolnode
		self.add_node()
		self.vs[10]["MT_pre__attr1"] = """return attr_value == "goesTo" """
		self.vs[10]["MT_label__"] = """11"""
		self.vs[10]["mm__"] = """MT_pre__directLink_S"""
		self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'18.0.m.3Childassoc1018.0.m.1School')

		# apply association District--facilities-->OrdinaryFacilitynode
		self.add_node()
		self.vs[11]["MT_pre__attr1"] = """return attr_value == "facilities" """
		self.vs[11]["MT_label__"] = """12"""
		self.vs[11]["mm__"] = """MT_pre__directLink_T"""
		self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'18.0.a.0Districtassoc1118.0.a.1OrdinaryFacility')

		# apply association OrdinaryFacility--members-->Personnode
		self.add_node()
		self.vs[12]["MT_pre__attr1"] = """return attr_value == "members" """
		self.vs[12]["MT_label__"] = """13"""
		self.vs[12]["mm__"] = """MT_pre__directLink_T"""
		self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'18.0.a.1OrdinaryFacilityassoc1218.0.a.2Person')

		# trace association District--trace-->Neighborhoodnode
		self.add_node()
		self.vs[13]["MT_label__"] = """14"""
		self.vs[13]["mm__"] = """MT_pre__trace_link"""
		self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'18.0.a.0Districtassoc1318.0.m.0Neighborhood')

		# trace association Person--trace-->Childnode
		self.add_node()
		self.vs[14]["MT_label__"] = """15"""
		self.vs[14]["mm__"] = """MT_pre__trace_link"""
		self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'18.0.a.2Personassoc1418.0.m.3Child')

		self['equations'].append(((5,'name'),('concat',(('constant','Ordinary Facility Service for school '),(1,'name')))))

		# Add the edges
		self.add_edges([
			(0,7), # match class Neighborhood(18.0.m.0Neighborhood) -> association schools
			(7,1), # association School -> match class School(18.0.m.1School)
			(1,8), # match class School(18.0.m.1School) -> association ordinary
			(8,2), # association Service -> match class Service(18.0.m.2Service)
			(1,9), # match class School(18.0.m.1School) -> association students
			(9,3), # association Child -> match class Child(18.0.m.3Child)
			(3,10), # match class Child(18.0.m.3Child) -> association goesTo
			(10,1), # association School -> match class School(18.0.m.1School)
			(4,11), # apply class District(18.0.a.0District) -> association facilities
			(11,5), # association OrdinaryFacility -> apply class OrdinaryFacility(18.0.a.1OrdinaryFacility)
			(5,12), # apply class OrdinaryFacility(18.0.a.1OrdinaryFacility) -> association members
			(12,6), # association Person -> apply class Person(18.0.a.2Person)
			(4,13), # apply class District(18.0.m.0Neighborhood) -> backward_association 
			(13,0), # backward_associationNeighborhood -> match_class Neighborhood(18.0.m.0Neighborhood)
			(6,14), # apply class Person(18.0.m.3Child) -> backward_association 
			(14,3), # backward_associationChild -> match_class Child(18.0.m.3Child)
		])


	# define evaluation methods for each match class.

	def eval_attr11(self, attr_value, this):
		return True

	def eval_attr12(self, attr_value, this):
		return True

	def eval_attr13(self, attr_value, this):
		return True

	def eval_attr14(self, attr_value, this):
		return True

	# define evaluation methods for each apply class.

	def eval_attr15(self, attr_value, this):
		return True

	def eval_attr16(self, attr_value, this):
		return True

	def eval_attr17(self, attr_value, this):
		return True

		# define evaluation methods for each match association.

	def eval_attr18(self, attr_value, this):
		return attr_value == "schools"
	def eval_attr19(self, attr_value, this):
		return attr_value == "ordinary"
	def eval_attr110(self, attr_value, this):
		return attr_value == "students"
	def eval_attr111(self, attr_value, this):
		return attr_value == "goesTo"
		# define evaluation methods for each apply association.

	def eval_attr112(self, attr_value, this):
		return attr_value == "facilities"
	def eval_attr113(self, attr_value, this):
		return attr_value == "members"

	def constraint(self, PreNode, graph):
		return True

