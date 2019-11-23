from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HUnitR06a_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HUnitR06a_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HUnitR06a_CompleteLHS, self).__init__(name='HUnitR06a_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HUnitR06a_CompleteLHS')
		self["equations"] = []
		# Set the node attributes

		# match class Transition(6.0.m.0Transition) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__Transition"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.0.m.0Transition')

		# match class Vertex(6.0.m.1Vertex) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__Vertex"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.0.m.1Vertex')

		# match class SIBLING0(6.0.m.2SIBLING0) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__SIBLING0"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.0.m.2SIBLING0')

		# match class StateMachine(6.0.m.3StateMachine) node
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return True"""
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__StateMachine"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.0.m.3StateMachine')

		# apply class Inst(6.0.a.0Inst) node
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return True"""
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__Inst"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.0.a.0Inst')

		# apply class Name(6.0.a.1Name) node
		self.add_node()
		self.vs[5]["MT_pre__attr1"] = """return True"""
		self.vs[5]["MT_label__"] = """6"""
		self.vs[5]["mm__"] = """MT_pre__Name"""
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.0.a.1Name')

		# apply class Name(6.0.a.2Name) node
		self.add_node()
		self.vs[6]["MT_pre__attr1"] = """return True"""
		self.vs[6]["MT_label__"] = """7"""
		self.vs[6]["mm__"] = """MT_pre__Name"""
		self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.0.a.2Name')

		# apply class Name(6.0.a.3Name) node
		self.add_node()
		self.vs[7]["MT_pre__attr1"] = """return True"""
		self.vs[7]["MT_label__"] = """8"""
		self.vs[7]["mm__"] = """MT_pre__Name"""
		self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.0.a.3Name')

		# apply class Name(6.0.a.4Name) node
		self.add_node()
		self.vs[8]["MT_pre__attr1"] = """return True"""
		self.vs[8]["MT_label__"] = """9"""
		self.vs[8]["mm__"] = """MT_pre__Name"""
		self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.0.a.4Name')

		# match association Transition--dest-->Vertexnode
		self.add_node()
		self.vs[9]["MT_pre__attr1"] = """return attr_value == "dest" """
		self.vs[9]["MT_label__"] = """10"""
		self.vs[9]["mm__"] = """MT_pre__directLink_S"""
		self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.0.m.0Transitionassoc96.0.m.1Vertex')

		# match association Transition--type-->SIBLING0node
		self.add_node()
		self.vs[10]["MT_pre__attr1"] = """return attr_value == "type" """
		self.vs[10]["MT_label__"] = """11"""
		self.vs[10]["mm__"] = """MT_pre__directLink_S"""
		self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.0.m.0Transitionassoc106.0.m.2SIBLING0')

		# match association Vertex--owningStateMachine-->StateMachinenode
		self.add_node()
		self.vs[11]["MT_pre__attr1"] = """return attr_value == "owningStateMachine" """
		self.vs[11]["MT_label__"] = """12"""
		self.vs[11]["mm__"] = """MT_pre__directLink_S"""
		self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.0.m.1Vertexassoc116.0.m.3StateMachine')

		# apply association Inst--channelNames-->Namenode
		self.add_node()
		self.vs[12]["MT_pre__attr1"] = """return attr_value == "channelNames" """
		self.vs[12]["MT_label__"] = """13"""
		self.vs[12]["mm__"] = """MT_pre__directLink_T"""
		self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.0.a.0Instassoc126.0.a.3Name')

		# apply association Inst--channelNames-->Namenode
		self.add_node()
		self.vs[13]["MT_pre__attr1"] = """return attr_value == "channelNames" """
		self.vs[13]["MT_label__"] = """14"""
		self.vs[13]["mm__"] = """MT_pre__directLink_T"""
		self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.0.a.0Instassoc136.0.a.1Name')

		# apply association Inst--channelNames-->Namenode
		self.add_node()
		self.vs[14]["MT_pre__attr1"] = """return attr_value == "channelNames" """
		self.vs[14]["MT_label__"] = """15"""
		self.vs[14]["mm__"] = """MT_pre__directLink_T"""
		self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.0.a.0Instassoc146.0.a.2Name')

		# apply association Inst--channelNames-->Namenode
		self.add_node()
		self.vs[15]["MT_pre__attr1"] = """return attr_value == "channelNames" """
		self.vs[15]["MT_label__"] = """16"""
		self.vs[15]["mm__"] = """MT_pre__directLink_T"""
		self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.0.a.0Instassoc156.0.a.4Name')

		self['equations'].append(((4,'name'),('concat',(('constant','S'),(3,'name')))))
		self['equations'].append(((5,'literal'),('constant','exack')))
		self['equations'].append(((6,'literal'),('concat',(('constant','A'),('concat',((1,'name'),('constant','A')))))))
		self['equations'].append(((7,'literal'),('constant','exit')))
		self['equations'].append(((8,'literal'),('constant','sh')))

		# Add the edges
		self.add_edges([
			(0,9), # match class Transition(6.0.m.0Transition) -> association dest
			(9,1), # association Vertex -> match class Vertex(6.0.m.1Vertex)
			(0,10), # match class Transition(6.0.m.0Transition) -> association type
			(10,2), # association SIBLING0 -> match class SIBLING0(6.0.m.2SIBLING0)
			(1,11), # match class Vertex(6.0.m.1Vertex) -> association owningStateMachine
			(11,3), # association StateMachine -> match class StateMachine(6.0.m.3StateMachine)
			(4,12), # apply class Inst(6.0.a.0Inst) -> association channelNames
			(12,7), # association Name -> apply class Name(6.0.a.3Name)
			(4,13), # apply class Inst(6.0.a.0Inst) -> association channelNames
			(13,5), # association Name -> apply class Name(6.0.a.1Name)
			(4,14), # apply class Inst(6.0.a.0Inst) -> association channelNames
			(14,6), # association Name -> apply class Name(6.0.a.2Name)
			(4,15), # apply class Inst(6.0.a.0Inst) -> association channelNames
			(15,8), # association Name -> apply class Name(6.0.a.4Name)
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

	def eval_attr19(self, attr_value, this):
		return True

		# define evaluation methods for each match association.

	def eval_attr110(self, attr_value, this):
		return attr_value == "dest"
	def eval_attr111(self, attr_value, this):
		return attr_value == "type"
	def eval_attr112(self, attr_value, this):
		return attr_value == "owningStateMachine"
		# define evaluation methods for each apply association.

	def eval_attr113(self, attr_value, this):
		return attr_value == "channelNames"
	def eval_attr114(self, attr_value, this):
		return attr_value == "channelNames"
	def eval_attr115(self, attr_value, this):
		return attr_value == "channelNames"
	def eval_attr116(self, attr_value, this):
		return attr_value == "channelNames"

	def constraint(self, PreNode, graph):
		return True

