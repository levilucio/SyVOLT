from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HUnitR07d_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HUnitR07d_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HUnitR07d_CompleteLHS, self).__init__(name='HUnitR07d_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HUnitR07d_CompleteLHS')
		self["equations"] = []
		# Set the node attributes

		# match class Transition(7.3.m.0Transition) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__Transition"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.3.m.0Transition')

		# match class IN1(7.3.m.1IN1) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__IN1"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.3.m.1IN1')

		# match class State(7.3.m.2State) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__State"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.3.m.2State')

		# match class Vertex(7.3.m.3Vertex) node
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return True"""
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__Vertex"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.3.m.3Vertex')

		# apply class ConditionSet(7.3.a.0ConditionSet) node
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return True"""
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__ConditionSet"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.3.a.0ConditionSet')

		# apply class ConditionBranch(7.3.a.1ConditionBranch) node
		self.add_node()
		self.vs[5]["MT_pre__attr1"] = """return True"""
		self.vs[5]["MT_label__"] = """6"""
		self.vs[5]["mm__"] = """MT_pre__ConditionBranch"""
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.3.a.1ConditionBranch')

		# apply class Expr(7.3.a.2Expr) node
		self.add_node()
		self.vs[6]["MT_pre__attr1"] = """return True"""
		self.vs[6]["MT_label__"] = """7"""
		self.vs[6]["mm__"] = """MT_pre__Expr"""
		self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.3.a.2Expr')

		# apply class Inst(7.3.a.3Inst) node
		self.add_node()
		self.vs[7]["MT_pre__attr1"] = """return True"""
		self.vs[7]["MT_label__"] = """8"""
		self.vs[7]["mm__"] = """MT_pre__Inst"""
		self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.3.a.3Inst')

		# match association State--transitions-->Transitionnode
		self.add_node()
		self.vs[8]["MT_pre__attr1"] = """return attr_value == "transitions" """
		self.vs[8]["MT_label__"] = """9"""
		self.vs[8]["mm__"] = """MT_pre__directLink_S"""
		self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.3.m.2Stateassoc87.3.m.0Transition')

		# match association Transition--type-->IN1node
		self.add_node()
		self.vs[9]["MT_pre__attr1"] = """return attr_value == "type" """
		self.vs[9]["MT_label__"] = """10"""
		self.vs[9]["mm__"] = """MT_pre__directLink_S"""
		self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.3.m.0Transitionassoc97.3.m.1IN1')

		# match association Transition--src-->Vertexnode
		self.add_node()
		self.vs[10]["MT_pre__attr1"] = """return attr_value == "src" """
		self.vs[10]["MT_label__"] = """11"""
		self.vs[10]["mm__"] = """MT_pre__directLink_S"""
		self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.3.m.0Transitionassoc107.3.m.3Vertex')

		# apply association ConditionSet--branches-->ConditionBranchnode
		self.add_node()
		self.vs[11]["MT_pre__attr1"] = """return attr_value == "branches" """
		self.vs[11]["MT_label__"] = """12"""
		self.vs[11]["mm__"] = """MT_pre__directLink_T"""
		self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.3.a.0ConditionSetassoc117.3.a.1ConditionBranch')

		# apply association ConditionBranch--if-->Exprnode
		self.add_node()
		self.vs[12]["MT_pre__attr1"] = """return attr_value == "if" """
		self.vs[12]["MT_label__"] = """13"""
		self.vs[12]["mm__"] = """MT_pre__directLink_T"""
		self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.3.a.1ConditionBranchassoc127.3.a.2Expr')

		# apply association ConditionBranch--then-->Instnode
		self.add_node()
		self.vs[13]["MT_pre__attr1"] = """return attr_value == "then" """
		self.vs[13]["MT_label__"] = """14"""
		self.vs[13]["mm__"] = """MT_pre__directLink_T"""
		self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.3.a.1ConditionBranchassoc137.3.a.3Inst')

		# trace association ConditionSet--trace-->Statenode
		self.add_node()
		self.vs[14]["MT_label__"] = """15"""
		self.vs[14]["mm__"] = """MT_pre__trace_link"""
		self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.3.a.0ConditionSetassoc147.3.m.2State')

		# trace association Inst--trace-->Transitionnode
		self.add_node()
		self.vs[15]["MT_label__"] = """16"""
		self.vs[15]["mm__"] = """MT_pre__trace_link"""
		self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'7.3.a.3Instassoc157.3.m.0Transition')

		self['equations'].append(((6,'literal'),('concat',(('constant','enp=A'),('concat',((3,'name'),('constant','A')))))))

		# Add the edges
		self.add_edges([
			(2,8), # match class State(7.3.m.2State) -> association transitions
			(8,0), # association Transition -> match class Transition(7.3.m.0Transition)
			(0,9), # match class Transition(7.3.m.0Transition) -> association type
			(9,1), # association IN1 -> match class IN1(7.3.m.1IN1)
			(0,10), # match class Transition(7.3.m.0Transition) -> association src
			(10,3), # association Vertex -> match class Vertex(7.3.m.3Vertex)
			(4,11), # apply class ConditionSet(7.3.a.0ConditionSet) -> association branches
			(11,5), # association ConditionBranch -> apply class ConditionBranch(7.3.a.1ConditionBranch)
			(5,12), # apply class ConditionBranch(7.3.a.1ConditionBranch) -> association if
			(12,6), # association Expr -> apply class Expr(7.3.a.2Expr)
			(5,13), # apply class ConditionBranch(7.3.a.1ConditionBranch) -> association then
			(13,7), # association Inst -> apply class Inst(7.3.a.3Inst)
			(4,14), # apply class ConditionSet(7.3.m.2State) -> backward_association 
			(14,2), # backward_associationState -> match_class State(7.3.m.2State)
			(7,15), # apply class Inst(7.3.m.0Transition) -> backward_association 
			(15,0), # backward_associationTransition -> match_class Transition(7.3.m.0Transition)
		])


	# define evaluation methods for each match class.

	def eval_attr11(self, attr_value, this):
		return True

	def eval_attr12(self, attr_value, this):
		return True

	def eval_attr13(self, attr_value, this):
		return True

	def eval_attr14(self, attr_value, this):
		return True

	# define evaluation methods for each apply class.

	def eval_attr15(self, attr_value, this):
		return True

	def eval_attr16(self, attr_value, this):
		return True

	def eval_attr17(self, attr_value, this):
		return True

	def eval_attr18(self, attr_value, this):
		return True

		# define evaluation methods for each match association.

	def eval_attr19(self, attr_value, this):
		return attr_value == "transitions"
	def eval_attr110(self, attr_value, this):
		return attr_value == "type"
	def eval_attr111(self, attr_value, this):
		return attr_value == "src"
		# define evaluation methods for each apply association.

	def eval_attr112(self, attr_value, this):
		return attr_value == "branches"
	def eval_attr113(self, attr_value, this):
		return attr_value == "if"
	def eval_attr114(self, attr_value, this):
		return attr_value == "then"

	def constraint(self, PreNode, graph):
		return True

