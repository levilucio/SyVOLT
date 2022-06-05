from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HMM8_if_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self, *args, **kwargs):
		"""
		Creates the himesis graph representing the AToM3 model HMM8_if_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HMM8_if_CompleteLHS, self).__init__(name='HMM8_if_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HMM8_if_CompleteLHS')
		self["equations"] = []
		# Set the node attributes

		# apply class ListenBranch(0.24.a.0ListenBranch) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__ListenBranch"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.24.a.0ListenBranch')

		self["equations"].append(((0,'pivot'),('constant','ListenBranchf49c25a2ListenBranch')))


		# Add the edges
		self.add_edges([
		])


	# define evaluation methods for each match class.

	# define evaluation methods for each apply class.

	def eval_attr11(self, attr_value, this):
		return True

		# define evaluation methods for each match association.

		# define evaluation methods for each apply association.


	def constraint(self, PreNode, graph):
		return True

