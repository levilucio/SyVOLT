from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HUnitR06b_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HUnitR06b_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HUnitR06b_CompleteLHS, self).__init__(name='HUnitR06b_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HUnitR06b_CompleteLHS')
		self["equations"] = []
		# Set the node attributes

		# match class Transition(6.1.m.0Transition) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__Transition"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.1.m.0Transition')

		# match class OUT2(6.1.m.1OUT2) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__OUT2"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.1.m.1OUT2')

		# match class StateMachine(6.1.m.2StateMachine) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__StateMachine"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.1.m.2StateMachine')

		# match class Vertex(6.1.m.3Vertex) node
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return True"""
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__Vertex"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.1.m.3Vertex')

		# apply class Inst(6.1.a.0Inst) node
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return True"""
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__Inst"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.1.a.0Inst')

		# apply class Name(6.1.a.1Name) node
		self.add_node()
		self.vs[5]["MT_pre__attr1"] = """return True"""
		self.vs[5]["MT_label__"] = """6"""
		self.vs[5]["mm__"] = """MT_pre__Name"""
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.1.a.1Name')

		# match association Transition--type-->OUT2node
		self.add_node()
		self.vs[6]["MT_pre__attr1"] = """return attr_value == "type" """
		self.vs[6]["MT_label__"] = """7"""
		self.vs[6]["mm__"] = """MT_pre__directLink_S"""
		self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.1.m.0Transitionassoc66.1.m.1OUT2')

		# match association Transition--owningStateMachine-->StateMachinenode
		self.add_node()
		self.vs[7]["MT_pre__attr1"] = """return attr_value == "owningStateMachine" """
		self.vs[7]["MT_label__"] = """8"""
		self.vs[7]["mm__"] = """MT_pre__directLink_S"""
		self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.1.m.0Transitionassoc76.1.m.2StateMachine')

		# match association StateMachine--exitPoints-->Vertexnode
		self.add_node()
		self.vs[8]["MT_pre__attr1"] = """return attr_value == "exitPoints" """
		self.vs[8]["MT_label__"] = """9"""
		self.vs[8]["mm__"] = """MT_pre__directLink_S"""
		self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.1.m.2StateMachineassoc86.1.m.3Vertex')

		# match association Transition--dest-->Vertexnode
		self.add_node()
		self.vs[9]["MT_pre__attr1"] = """return attr_value == "dest" """
		self.vs[9]["MT_label__"] = """10"""
		self.vs[9]["mm__"] = """MT_pre__directLink_S"""
		self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.1.m.0Transitionassoc96.1.m.3Vertex')

		# apply association Inst--channelNames-->Namenode
		self.add_node()
		self.vs[10]["MT_pre__attr1"] = """return attr_value == "channelNames" """
		self.vs[10]["MT_label__"] = """11"""
		self.vs[10]["mm__"] = """MT_pre__directLink_T"""
		self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.1.a.0Instassoc106.1.a.1Name')

		self['equations'].append(((4,'name'),('concat',(('constant','B'),(3,'name')))))
		self['equations'].append(((5,'literal'),('constant','sh')))

		# Add the edges
		self.add_edges([
			(0,6), # match class Transition(6.1.m.0Transition) -> association type
			(6,1), # association OUT2 -> match class OUT2(6.1.m.1OUT2)
			(0,7), # match class Transition(6.1.m.0Transition) -> association owningStateMachine
			(7,2), # association StateMachine -> match class StateMachine(6.1.m.2StateMachine)
			(2,8), # match class StateMachine(6.1.m.2StateMachine) -> association exitPoints
			(8,3), # association Vertex -> match class Vertex(6.1.m.3Vertex)
			(0,9), # match class Transition(6.1.m.0Transition) -> association dest
			(9,3), # association Vertex -> match class Vertex(6.1.m.3Vertex)
			(4,10), # apply class Inst(6.1.a.0Inst) -> association channelNames
			(10,5), # association Name -> apply class Name(6.1.a.1Name)
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

		# define evaluation methods for each match association.

	def eval_attr17(self, attr_value, this):
		return attr_value == "type"
	def eval_attr18(self, attr_value, this):
		return attr_value == "owningStateMachine"
	def eval_attr19(self, attr_value, this):
		return attr_value == "exitPoints"
	def eval_attr110(self, attr_value, this):
		return attr_value == "dest"
		# define evaluation methods for each apply association.

	def eval_attr111(self, attr_value, this):
		return attr_value == "channelNames"

	def constraint(self, PreNode, graph):
		return True

