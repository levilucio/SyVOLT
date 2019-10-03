from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HUnitN2D_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HUnitN2D_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HUnitN2D_CompleteLHS, self).__init__(name='HUnitN2D_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HUnitN2D_CompleteLHS')
		self["equations"] = []
		# Set the node attributes

		# match class Family(Family) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__Family"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Family')

		# match class Neighborhood(Neigh) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__Neighborhood"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Neigh')

		# apply class District(District) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__District"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'District')

		# match association null--registeredIn-->nullnode
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return attr_value == "registeredIn" """
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__directLink_S"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Familyassoc3Neigh')


		# Add the edges
		self.add_edges([
			(0,3), # match class null(Family) -> association registeredIn
			(3,1), # association null -> match class null(Neigh)
		])


	# define evaluation methods for each match class.

	def eval_attr11(self, attr_value, this):
		return True

	def eval_attr12(self, attr_value, this):
		return True

	# define evaluation methods for each apply class.

	def eval_attr13(self, attr_value, this):
		return True

		# define evaluation methods for each match association.

	def eval_attr14(self, attr_value, this):
		return attr_value == "registeredIn"
		# define evaluation methods for each apply association.


	def constraint(self, PreNode, graph):
		return True

