from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HUnitCity2TownHall_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HUnitCity2TownHall_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HUnitCity2TownHall_CompleteLHS, self).__init__(name='HUnitCity2TownHall_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HUnitCity2TownHall_CompleteLHS')
		self["equations"] = []
		# Set the node attributes

		# match class City(City) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__City"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'City')

		# apply class Committee(Committee) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__Committee"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Committee')

		# apply class TownHall(TownHall) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__TownHall"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'TownHall')

		# apply association null--committee-->nullnode
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return attr_value == "committee" """
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__directLink_T"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'TownHallassoc3Committee')


		# Add the edges
		self.add_edges([
			(2,3), # apply class null(TownHall) -> association committee
			(3,1), # association null -> apply class null(Committee)
		])


	# define evaluation methods for each match class.

	def eval_attr11(self, attr_value, this):
		return True

	# define evaluation methods for each apply class.

	def eval_attr12(self, attr_value, this):
		return True

	def eval_attr13(self, attr_value, this):
		return True

		# define evaluation methods for each match association.

		# define evaluation methods for each apply association.

	def eval_attr14(self, attr_value, this):
		return attr_value == "committee"

	def constraint(self, PreNode, graph):
		return True

