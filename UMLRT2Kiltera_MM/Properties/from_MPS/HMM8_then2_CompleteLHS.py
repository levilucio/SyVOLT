from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HMM8_then2_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self, *args, **kwargs):
		"""
		Creates the himesis graph representing the AToM3 model HMM8_then2_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HMM8_then2_CompleteLHS, self).__init__(name='HMM8_then2_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HMM8_then2_CompleteLHS')
		self["equations"] = []
		# Set the node attributes

		# apply class ListenBranch(0.26.a.0ListenBranch) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__ListenBranch"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.26.a.0ListenBranch')

		# apply class Pattern(0.26.a.1Pattern) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__Pattern"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.26.a.1Pattern')

		# apply class Pattern(0.26.a.2Pattern) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__Pattern"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.26.a.2Pattern')

		# apply association ListenBranch--match-->Patternnode
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return attr_value == "match" """
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__directLink_T"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.26.a.0ListenBranchassoc30.26.a.1Pattern')

		# apply association ListenBranch--p-->Patternnode
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return attr_value == "p" """
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__directLink_T"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.26.a.0ListenBranchassoc40.26.a.2Pattern')

		self["equations"].append(((0,'pivot'),('constant','ListenBranchf49c25a2ListenBranch')))


		# Add the edges
		self.add_edges([
			(0,3), # apply class ListenBranch(0.26.a.0ListenBranch) -> association match
			(3,1), # association Pattern -> apply class Pattern(0.26.a.1Pattern)
			(0,4), # apply class ListenBranch(0.26.a.0ListenBranch) -> association p
			(4,2), # association Pattern -> apply class Pattern(0.26.a.2Pattern)
		])


	# define evaluation methods for each match class.

	# define evaluation methods for each apply class.

	def eval_attr11(self, attr_value, this):
		return True

	def eval_attr12(self, attr_value, this):
		return True

	def eval_attr13(self, attr_value, this):
		return True

		# define evaluation methods for each match association.

		# define evaluation methods for each apply association.

	def eval_attr14(self, attr_value, this):
		return attr_value == "match"
	def eval_attr15(self, attr_value, this):
		return attr_value == "p"

	def constraint(self, PreNode, graph):
		return True

