from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HUnitC2C_IsolatedLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HUnitC2C_IsolatedLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HUnitC2C_IsolatedLHS, self).__init__(name='HUnitC2C_IsolatedLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HUnitC2C_IsolatedLHS')
		self["equations"] = []
		# Set the node attributes

		# match class Category(MCategory) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__Category"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'MCategory')

	# define evaluation methods for each apply class.

	def eval_attr11(self, attr_value, this):
		return True


	def constraint(self, PreNode, graph):
		return True
