from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HMM8_then2_IsolatedLHS(HimesisPreConditionPatternLHS):
	def __init__(self, *args, **kwargs):
		"""
		Creates the himesis graph representing the AToM3 model HMM8_then2_IsolatedLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HMM8_then2_IsolatedLHS, self).__init__(name='HMM8_then2_IsolatedLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HMM8_then2_IsolatedLHS')
		self["equations"] = []
		# Set the node attributes

	# define evaluation methods for each apply class.


	def constraint(self, PreNode, graph):
		return True

