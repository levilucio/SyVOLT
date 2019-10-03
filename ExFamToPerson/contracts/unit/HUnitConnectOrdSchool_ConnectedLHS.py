from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HUnitConnectOrdSchool_ConnectedLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HUnitConnectOrdSchool_ConnectedLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HUnitConnectOrdSchool_ConnectedLHS, self).__init__(name='HUnitConnectOrdSchool_ConnectedLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HUnitConnectOrdSchool_ConnectedLHS')
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


		# match association Neighborhood--schools-->Schoolnode
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return attr_value == "schools" """
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__directLink_S"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'18.0.m.0Neighborhoodassoc418.0.m.1School')

		# match association School--ordinary-->Servicenode
		self.add_node()
		self.vs[5]["MT_pre__attr1"] = """return attr_value == "ordinary" """
		self.vs[5]["MT_label__"] = """6"""
		self.vs[5]["mm__"] = """MT_pre__directLink_S"""
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'18.0.m.1Schoolassoc518.0.m.2Service')

		# match association School--students-->Childnode
		self.add_node()
		self.vs[6]["MT_pre__attr1"] = """return attr_value == "students" """
		self.vs[6]["MT_label__"] = """7"""
		self.vs[6]["mm__"] = """MT_pre__directLink_S"""
		self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'18.0.m.1Schoolassoc618.0.m.3Child')

		# match association Child--goesTo-->Schoolnode
		self.add_node()
		self.vs[7]["MT_pre__attr1"] = """return attr_value == "goesTo" """
		self.vs[7]["MT_label__"] = """8"""
		self.vs[7]["mm__"] = """MT_pre__directLink_S"""
		self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'18.0.m.3Childassoc718.0.m.1School')

		# Add the edges
		self.add_edges([
			(0,4), # match class Neighborhood(18.0.m.0Neighborhood) -> association schools
			(4,1), # association School -> match class School(18.0.m.1School)
			(1,5), # match class School(18.0.m.1School) -> association ordinary
			(5,2), # association Service -> match class Service(18.0.m.2Service)
			(1,6), # match class School(18.0.m.1School) -> association students
			(6,3), # association Child -> match class Child(18.0.m.3Child)
			(3,7), # match class Child(18.0.m.3Child) -> association goesTo
			(7,1), # association School -> match class School(18.0.m.1School)
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

	# define evaluation methods for each match association.

	def eval_attr15(self, attr_value, this):
		return attr_value == "schools"
	def eval_attr16(self, attr_value, this):
		return attr_value == "ordinary"
	def eval_attr17(self, attr_value, this):
		return attr_value == "students"
	def eval_attr18(self, attr_value, this):
		return attr_value == "goesTo"

	def constraint(self, PreNode, graph):
		return True

