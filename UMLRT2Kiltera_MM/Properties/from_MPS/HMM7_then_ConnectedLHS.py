from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HMM7_then_ConnectedLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HMM7_then_ConnectedLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HMM7_then_ConnectedLHS, self).__init__(name='HMM7_then_ConnectedLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HMM7_then_ConnectedLHS')
		self["equations"] = []
		# Set the node attributes


		# Add the edges
		self.add_edges([
		])


	# define evaluation methods for each match class.

	# define evaluation methods for each match association.


	def constraint(self, PreNode, graph):
		return True
