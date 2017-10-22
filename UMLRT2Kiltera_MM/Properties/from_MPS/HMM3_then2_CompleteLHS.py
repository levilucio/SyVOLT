from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HMM3_then2_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HMM3_then2_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HMM3_then2_CompleteLHS, self).__init__(name='HMM3_then2_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HMM3_then2_CompleteLHS')
		self["equations"] = []
		# Set the node attributes

		# apply class ConditionBranch(0.14.a.0ConditionBranch) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__ConditionBranch"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.14.a.0ConditionBranch')

		# apply class Expr(0.14.a.1Expr) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__Expr"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.14.a.1Expr')

		# apply class Expr(0.14.a.2Expr) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__Expr"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.14.a.2Expr')

		# apply association ConditionBranch--if-->Exprnode
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return attr_value == "if" """
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__directLink_T"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.14.a.0ConditionBranchassoc30.14.a.1Expr')

		# apply association ConditionBranch--if-->Exprnode
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return attr_value == "if" """
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__directLink_T"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.14.a.0ConditionBranchassoc40.14.a.2Expr')

		self["equations"].append(((0,'pivot'),('constant','ConditionBranche1a6b24fConditionBranch')))


		# Add the edges
		self.add_edges([
			(0,3), # apply class ConditionBranch(0.14.a.0ConditionBranch) -> association if
			(3,1), # association Expr -> apply class Expr(0.14.a.1Expr)
			(0,4), # apply class ConditionBranch(0.14.a.0ConditionBranch) -> association if
			(4,2), # association Expr -> apply class Expr(0.14.a.2Expr)
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
		return attr_value == "if"
	def eval_attr15(self, attr_value, this):
		return attr_value == "if"

	def constraint(self, PreNode, graph):
		return True

