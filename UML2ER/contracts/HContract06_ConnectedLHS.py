from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HContract06_ConnectedLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HContract06_ConnectedLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HContract06_ConnectedLHS, self).__init__(name='HContract06_ConnectedLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HContract06_ConnectedLHS')
		self["equations"] = []
		# Set the node attributes

		# match class Class(Class) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__Class"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Class')


		# Add the edges
		self.add_edges([
		])


	# define evaluation methods for each match class.

	def eval_attr11(self, attr_value, this):
		return True

	# define evaluation methods for each match association.


	def constraint(self, PreNode, graph):
		return True

