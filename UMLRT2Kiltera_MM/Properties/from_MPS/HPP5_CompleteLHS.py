from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HPP5_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HPP5_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HPP5_CompleteLHS, self).__init__(name='HPP5_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HPP5_CompleteLHS')
		self["equations"] = []
		# Set the node attributes

		# match class State(0.34.m.0State) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__State"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.34.m.0State')

		# match class State(0.34.m.1State) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__State"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.34.m.1State')

		# apply class ProcDef(0.34.a.0ProcDef) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__ProcDef"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.34.a.0ProcDef')

		# apply class ProcDef(0.34.a.1ProcDef) node
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return True"""
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__ProcDef"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.34.a.1ProcDef')

		# apply class LocalDef(0.34.a.2LocalDef) node
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return True"""
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__LocalDef"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.34.a.2LocalDef')

		# match association State--states-->Statenode
		self.add_node()
		self.vs[5]["MT_pre__attr1"] = """return attr_value == "states" """
		self.vs[5]["MT_label__"] = """6"""
		self.vs[5]["mm__"] = """MT_pre__directLink_S"""
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.34.m.0Stateassoc50.34.m.1State')

		# apply association ProcDef--p-->LocalDefnode
		self.add_node()
		self.vs[6]["MT_pre__attr1"] = """return attr_value == "p" """
		self.vs[6]["MT_label__"] = """7"""
		self.vs[6]["mm__"] = """MT_pre__directLink_T"""
		self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.34.a.0ProcDefassoc60.34.a.2LocalDef')

		# apply association LocalDef--def-->ProcDefnode
		self.add_node()
		self.vs[7]["MT_pre__attr1"] = """return attr_value == "def" """
		self.vs[7]["MT_label__"] = """8"""
		self.vs[7]["mm__"] = """MT_pre__directLink_T"""
		self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.34.a.2LocalDefassoc70.34.a.1ProcDef')

		# trace association ProcDef--trace-->Statenode
		self.add_node()
		self.vs[8]["MT_label__"] = """9"""
		self.vs[8]["mm__"] = """MT_pre__trace_link"""
		self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.34.a.0ProcDefassoc80.34.m.0State')

		# trace association LocalDef--trace-->Statenode
		self.add_node()
		self.vs[9]["MT_label__"] = """10"""
		self.vs[9]["mm__"] = """MT_pre__trace_link"""
		self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.34.a.2LocalDefassoc90.34.m.0State')

		# trace association ProcDef--trace-->Statenode
		self.add_node()
		self.vs[10]["MT_label__"] = """11"""
		self.vs[10]["mm__"] = """MT_pre__trace_link"""
		self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.34.a.1ProcDefassoc100.34.m.1State')


		# Add the edges
		self.add_edges([
			(0,5), # match class State(0.34.m.0State) -> association states
			(5,1), # association State -> match class State(0.34.m.1State)
			(2,6), # apply class ProcDef(0.34.a.0ProcDef) -> association p
			(6,4), # association LocalDef -> apply class LocalDef(0.34.a.2LocalDef)
			(4,7), # apply class LocalDef(0.34.a.2LocalDef) -> association def
			(7,3), # association ProcDef -> apply class ProcDef(0.34.a.1ProcDef)
			(2,8), # apply class ProcDef(0.34.m.0State) -> backward_association 
			(8,0), # backward_associationState -> match_class State(0.34.m.0State)
			(4,9), # apply class LocalDef(0.34.m.0State) -> backward_association 
			(9,0), # backward_associationState -> match_class State(0.34.m.0State)
			(3,10), # apply class ProcDef(0.34.m.1State) -> backward_association 
			(10,1), # backward_associationState -> match_class State(0.34.m.1State)
		])


	# define evaluation methods for each match class.

	def eval_attr11(self, attr_value, this):
		return True

	def eval_attr12(self, attr_value, this):
		return True

	# define evaluation methods for each apply class.

	def eval_attr13(self, attr_value, this):
		return True

	def eval_attr14(self, attr_value, this):
		return True

	def eval_attr15(self, attr_value, this):
		return True

		# define evaluation methods for each match association.

	def eval_attr16(self, attr_value, this):
		return attr_value == "states"
		# define evaluation methods for each apply association.

	def eval_attr17(self, attr_value, this):
		return attr_value == "p"
	def eval_attr18(self, attr_value, this):
		return attr_value == "def"

	def constraint(self, PreNode, graph):
		return True

