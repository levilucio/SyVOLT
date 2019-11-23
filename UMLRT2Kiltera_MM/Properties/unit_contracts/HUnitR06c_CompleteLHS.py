from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HUnitR06c_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HUnitR06c_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HUnitR06c_CompleteLHS, self).__init__(name='HUnitR06c_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HUnitR06c_CompleteLHS')
		self["equations"] = []
		# Set the node attributes

		# match class State(6.2.m.0State) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__State"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.2.m.0State')

		# match class Transition(6.2.m.1Transition) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__Transition"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.2.m.1Transition')

		# match class IN1(6.2.m.2IN1) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__IN1"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.2.m.2IN1')

		# match class EntryPoint(6.2.m.3EntryPoint) node
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return True"""
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__EntryPoint"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.2.m.3EntryPoint')

		# match class StateMachine(6.2.m.4StateMachine) node
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return True"""
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__StateMachine"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.2.m.4StateMachine')

		# apply class Inst(6.2.a.0Inst) node
		self.add_node()
		self.vs[5]["MT_pre__attr1"] = """return True"""
		self.vs[5]["MT_label__"] = """6"""
		self.vs[5]["mm__"] = """MT_pre__Inst"""
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.2.a.0Inst')

		# apply class Name(6.2.a.1Name) node
		self.add_node()
		self.vs[6]["MT_pre__attr1"] = """return True"""
		self.vs[6]["MT_label__"] = """7"""
		self.vs[6]["mm__"] = """MT_pre__Name"""
		self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.2.a.1Name')

		# apply class Name(6.2.a.2Name) node
		self.add_node()
		self.vs[7]["MT_pre__attr1"] = """return True"""
		self.vs[7]["MT_label__"] = """8"""
		self.vs[7]["mm__"] = """MT_pre__Name"""
		self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.2.a.2Name')

		# apply class Name(6.2.a.3Name) node
		self.add_node()
		self.vs[8]["MT_pre__attr1"] = """return True"""
		self.vs[8]["MT_label__"] = """9"""
		self.vs[8]["mm__"] = """MT_pre__Name"""
		self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.2.a.3Name')

		# apply class Name(6.2.a.4Name) node
		self.add_node()
		self.vs[9]["MT_pre__attr1"] = """return True"""
		self.vs[9]["MT_label__"] = """10"""
		self.vs[9]["mm__"] = """MT_pre__Name"""
		self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.2.a.4Name')

		# match association State--transitions-->Transitionnode
		self.add_node()
		self.vs[10]["MT_pre__attr1"] = """return attr_value == "transitions" """
		self.vs[10]["MT_label__"] = """11"""
		self.vs[10]["mm__"] = """MT_pre__directLink_S"""
		self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.2.m.0Stateassoc106.2.m.1Transition')

		# match association Transition--type-->IN1node
		self.add_node()
		self.vs[11]["MT_pre__attr1"] = """return attr_value == "type" """
		self.vs[11]["MT_label__"] = """12"""
		self.vs[11]["mm__"] = """MT_pre__directLink_S"""
		self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.2.m.1Transitionassoc116.2.m.2IN1')

		# match association Transition--dest-->EntryPointnode
		self.add_node()
		self.vs[12]["MT_pre__attr1"] = """return attr_value == "dest" """
		self.vs[12]["MT_label__"] = """13"""
		self.vs[12]["mm__"] = """MT_pre__directLink_S"""
		self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.2.m.1Transitionassoc126.2.m.3EntryPoint')

		# match association EntryPoint--owningStateMachine-->StateMachinenode
		self.add_node()
		self.vs[13]["MT_pre__attr1"] = """return attr_value == "owningStateMachine" """
		self.vs[13]["MT_label__"] = """14"""
		self.vs[13]["mm__"] = """MT_pre__directLink_S"""
		self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.2.m.3EntryPointassoc136.2.m.4StateMachine')

		# apply association Inst--channelNames-->Namenode
		self.add_node()
		self.vs[14]["MT_pre__attr1"] = """return attr_value == "channelNames" """
		self.vs[14]["MT_label__"] = """15"""
		self.vs[14]["mm__"] = """MT_pre__directLink_T"""
		self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.2.a.0Instassoc146.2.a.1Name')

		# apply association Inst--channelNames-->Namenode
		self.add_node()
		self.vs[15]["MT_pre__attr1"] = """return attr_value == "channelNames" """
		self.vs[15]["MT_label__"] = """16"""
		self.vs[15]["mm__"] = """MT_pre__directLink_T"""
		self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.2.a.0Instassoc156.2.a.2Name')

		# apply association Inst--channelNames-->Namenode
		self.add_node()
		self.vs[16]["MT_pre__attr1"] = """return attr_value == "channelNames" """
		self.vs[16]["MT_label__"] = """17"""
		self.vs[16]["mm__"] = """MT_pre__directLink_T"""
		self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.2.a.0Instassoc166.2.a.3Name')

		# apply association Inst--channelNames-->Namenode
		self.add_node()
		self.vs[17]["MT_pre__attr1"] = """return attr_value == "channelNames" """
		self.vs[17]["MT_label__"] = """18"""
		self.vs[17]["mm__"] = """MT_pre__directLink_T"""
		self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'6.2.a.0Instassoc176.2.a.4Name')

		self['equations'].append(((5,'name'),('concat',(('constant','S'),(4,'name')))))
		self['equations'].append(((6,'literal'),('constant','exit_in')))
		self['equations'].append(((7,'literal'),('constant','exack_in')))
		self['equations'].append(((8,'literal'),('concat',(('constant','A'),('concat',((3,'name'),('constant','A')))))))
		self['equations'].append(((9,'literal'),('constant','sh_in')))

		# Add the edges
		self.add_edges([
			(0,10), # match class State(6.2.m.0State) -> association transitions
			(10,1), # association Transition -> match class Transition(6.2.m.1Transition)
			(1,11), # match class Transition(6.2.m.1Transition) -> association type
			(11,2), # association IN1 -> match class IN1(6.2.m.2IN1)
			(1,12), # match class Transition(6.2.m.1Transition) -> association dest
			(12,3), # association EntryPoint -> match class EntryPoint(6.2.m.3EntryPoint)
			(3,13), # match class EntryPoint(6.2.m.3EntryPoint) -> association owningStateMachine
			(13,4), # association StateMachine -> match class StateMachine(6.2.m.4StateMachine)
			(5,14), # apply class Inst(6.2.a.0Inst) -> association channelNames
			(14,6), # association Name -> apply class Name(6.2.a.1Name)
			(5,15), # apply class Inst(6.2.a.0Inst) -> association channelNames
			(15,7), # association Name -> apply class Name(6.2.a.2Name)
			(5,16), # apply class Inst(6.2.a.0Inst) -> association channelNames
			(16,8), # association Name -> apply class Name(6.2.a.3Name)
			(5,17), # apply class Inst(6.2.a.0Inst) -> association channelNames
			(17,9), # association Name -> apply class Name(6.2.a.4Name)
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

	def eval_attr15(self, attr_value, this):
		return True

	# define evaluation methods for each apply class.

	def eval_attr16(self, attr_value, this):
		return True

	def eval_attr17(self, attr_value, this):
		return True

	def eval_attr18(self, attr_value, this):
		return True

	def eval_attr19(self, attr_value, this):
		return True

	def eval_attr110(self, attr_value, this):
		return True

		# define evaluation methods for each match association.

	def eval_attr111(self, attr_value, this):
		return attr_value == "transitions"
	def eval_attr112(self, attr_value, this):
		return attr_value == "type"
	def eval_attr113(self, attr_value, this):
		return attr_value == "dest"
	def eval_attr114(self, attr_value, this):
		return attr_value == "owningStateMachine"
		# define evaluation methods for each apply association.

	def eval_attr115(self, attr_value, this):
		return attr_value == "channelNames"
	def eval_attr116(self, attr_value, this):
		return attr_value == "channelNames"
	def eval_attr117(self, attr_value, this):
		return attr_value == "channelNames"
	def eval_attr118(self, attr_value, this):
		return attr_value == "channelNames"

	def constraint(self, PreNode, graph):
		return True

