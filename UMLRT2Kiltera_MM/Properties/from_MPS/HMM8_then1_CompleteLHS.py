from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HMM8_then1_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self, *args, **kwargs):
		"""
		Creates the himesis graph representing the AToM3 model HMM8_then1_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HMM8_then1_CompleteLHS, self).__init__(name='HMM8_then1_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HMM8_then1_CompleteLHS')
		self["equations"] = []
		# Set the node attributes

		# apply class ListenBranch(0.25.a.0ListenBranch) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__ListenBranch"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.25.a.0ListenBranch')

		# apply class Pattern(0.25.a.1Pattern) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__Pattern"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.25.a.1Pattern')

		# apply association ListenBranch--match-->Patternnode
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return attr_value == "match" """
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__directLink_T"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.25.a.0ListenBranchassoc20.25.a.1Pattern')

		self["equations"].append(((0,'pivot'),('constant','ListenBranch999e149eListenBranch')))


		# Add the edges
		self.add_edges([
			(0,2), # apply class ListenBranch(0.25.a.0ListenBranch) -> association match
			(2,1), # association Pattern -> apply class Pattern(0.25.a.1Pattern)
		])


	# define evaluation methods for each match class.

	# define evaluation methods for each apply class.

	def eval_attr11(self, attr_value, this):
		return True

	def eval_attr12(self, attr_value, this):
		return True

		# define evaluation methods for each match association.

		# define evaluation methods for each apply association.

	def eval_attr13(self, attr_value, this):
		return attr_value == "match"

	def constraint(self, PreNode, graph):
		return True

