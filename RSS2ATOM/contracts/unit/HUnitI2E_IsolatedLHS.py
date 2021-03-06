from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HUnitI2E_IsolatedLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HUnitI2E_IsolatedLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HUnitI2E_IsolatedLHS, self).__init__(name='HUnitI2E_IsolatedLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HUnitI2E_IsolatedLHS')
		self["equations"] = []
		# Set the node attributes

		# match class Item(Item) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__Item"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Item')

	# define evaluation methods for each apply class.

	def eval_attr11(self, attr_value, this):
		return True


	def constraint(self, PreNode, graph):
		return True

