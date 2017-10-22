from core.himesis import Himesis
import uuid

class HState2CProcDef(Himesis):
	def __init__(self):
		"""
		Creates the himesis graph representing the DSLTrans rule State2CProcDef.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HState2CProcDef, self).__init__(name='HState2CProcDef', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """State2CProcDef"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'State2CProcDef')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """State2CProcDef"""

		# match class State(5.2.m.0State) node
		self.add_node()
		self.vs[3]["mm__"] = """State"""
		self.vs[3]["attr1"] = """+"""

		# match class Transition(5.2.m.1Transition) node
		self.add_node()
		self.vs[4]["mm__"] = """Transition"""
		self.vs[4]["attr1"] = """1"""

		# match class EntryPoint(5.2.m.2EntryPoint) node
		self.add_node()
		self.vs[5]["mm__"] = """EntryPoint"""
		self.vs[5]["attr1"] = """1"""

		# match class StateMachine(5.2.m.3StateMachine) node
		self.add_node()
		self.vs[6]["mm__"] = """StateMachine"""
		self.vs[6]["attr1"] = """1"""

		# apply class LocalDef(5.2.a.0LocalDef) node
		self.add_node()
		self.vs[7]["mm__"] = """LocalDef"""
		self.vs[7]["attr1"] = """1"""

		# apply class ProcDef(5.2.a.1ProcDef) node
		self.add_node()
		self.vs[8]["mm__"] = """ProcDef"""
		self.vs[8]["attr1"] = """1"""

		# apply class Name(5.2.a.2Name) node
		self.add_node()
		self.vs[9]["mm__"] = """Name"""
		self.vs[9]["attr1"] = """1"""

		# apply class Name(5.2.a.3Name) node
		self.add_node()
		self.vs[10]["mm__"] = """Name"""
		self.vs[10]["attr1"] = """1"""

		# apply class Name(5.2.a.4Name) node
		self.add_node()
		self.vs[11]["mm__"] = """Name"""
		self.vs[11]["attr1"] = """1"""

		# apply class Name(5.2.a.5Name) node
		self.add_node()
		self.vs[12]["mm__"] = """Name"""
		self.vs[12]["attr1"] = """1"""

		# apply class ConditionSet(5.2.a.6ConditionSet) node
		self.add_node()
		self.vs[13]["mm__"] = """ConditionSet"""
		self.vs[13]["attr1"] = """1"""

		# apply class Inst(5.2.a.7Inst) node
		self.add_node()
		self.vs[14]["mm__"] = """Inst"""
		self.vs[14]["attr1"] = """1"""

		# apply class Name(5.2.a.8Name) node
		self.add_node()
		self.vs[15]["mm__"] = """Name"""
		self.vs[15]["attr1"] = """1"""

		# apply class Name(5.2.a.9Name) node
		self.add_node()
		self.vs[16]["mm__"] = """Name"""
		self.vs[16]["attr1"] = """1"""

		# apply class Name(5.2.a.10Name) node
		self.add_node()
		self.vs[17]["mm__"] = """Name"""
		self.vs[17]["attr1"] = """1"""

		# apply class Name(5.2.a.11Name) node
		self.add_node()
		self.vs[18]["mm__"] = """Name"""
		self.vs[18]["attr1"] = """1"""

		# match association State--initialTransition-->Transition node 
		self.add_node()
		self.vs[19]["attr1"] = """initialTransition"""
		self.vs[19]["mm__"] = """directLink_S"""

		# match association Transition--dest-->EntryPoint node 
		self.add_node()
		self.vs[20]["attr1"] = """dest"""
		self.vs[20]["mm__"] = """directLink_S"""

		# match association EntryPoint--owningStateMachine-->StateMachine node 
		self.add_node()
		self.vs[21]["attr1"] = """owningStateMachine"""
		self.vs[21]["mm__"] = """directLink_S"""

		# apply association LocalDef--def-->ProcDef node 
		self.add_node()
		self.vs[22]["attr1"] = """def"""
		self.vs[22]["mm__"] = """directLink_T"""

		# apply association ProcDef--channelNames-->Name node 
		self.add_node()
		self.vs[23]["attr1"] = """channelNames"""
		self.vs[23]["mm__"] = """directLink_T"""

		# apply association ProcDef--channelNames-->Name node 
		self.add_node()
		self.vs[24]["attr1"] = """channelNames"""
		self.vs[24]["mm__"] = """directLink_T"""

		# apply association ProcDef--channelNames-->Name node 
		self.add_node()
		self.vs[25]["attr1"] = """channelNames"""
		self.vs[25]["mm__"] = """directLink_T"""

		# apply association ProcDef--channelNames-->Name node 
		self.add_node()
		self.vs[26]["attr1"] = """channelNames"""
		self.vs[26]["mm__"] = """directLink_T"""

		# apply association ProcDef--p-->ConditionSet node 
		self.add_node()
		self.vs[27]["attr1"] = """p"""
		self.vs[27]["mm__"] = """directLink_T"""

		# apply association ConditionSet--alternative-->Inst node 
		self.add_node()
		self.vs[28]["attr1"] = """alternative"""
		self.vs[28]["mm__"] = """directLink_T"""

		# apply association Inst--channelNames-->Name node 
		self.add_node()
		self.vs[29]["attr1"] = """channelNames"""
		self.vs[29]["mm__"] = """directLink_T"""

		# apply association Inst--channelNames-->Name node 
		self.add_node()
		self.vs[30]["attr1"] = """channelNames"""
		self.vs[30]["mm__"] = """directLink_T"""

		# apply association Inst--channelNames-->Name node 
		self.add_node()
		self.vs[31]["attr1"] = """channelNames"""
		self.vs[31]["mm__"] = """directLink_T"""

		# apply association Inst--channelNames-->Name node 
		self.add_node()
		self.vs[32]["attr1"] = """channelNames"""
		self.vs[32]["mm__"] = """directLink_T"""

		# backward association LocalDef-->Statenode 
		self.add_node()
		self.vs[33]["mm__"] = """backward_link"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class State(5.2.m.0State)
			(0,4), # matchmodel -> match_class Transition(5.2.m.1Transition)
			(0,5), # matchmodel -> match_class EntryPoint(5.2.m.2EntryPoint)
			(0,6), # matchmodel -> match_class StateMachine(5.2.m.3StateMachine)
			(1,7), # applymodel -> apply_classLocalDef(5.2.a.0LocalDef)
			(1,8), # applymodel -> apply_classProcDef(5.2.a.1ProcDef)
			(1,9), # applymodel -> apply_className(5.2.a.2Name)
			(1,10), # applymodel -> apply_className(5.2.a.3Name)
			(1,11), # applymodel -> apply_className(5.2.a.4Name)
			(1,12), # applymodel -> apply_className(5.2.a.5Name)
			(1,13), # applymodel -> apply_classConditionSet(5.2.a.6ConditionSet)
			(1,14), # applymodel -> apply_classInst(5.2.a.7Inst)
			(1,15), # applymodel -> apply_className(5.2.a.8Name)
			(1,16), # applymodel -> apply_className(5.2.a.9Name)
			(1,17), # applymodel -> apply_className(5.2.a.10Name)
			(1,18), # applymodel -> apply_className(5.2.a.11Name)
			(3,19), # match classState(5.2.m.0State) -> association initialTransition
			(19,4), # associationinitialTransition -> match_classState(5.2.m.1Transition)
			(4,20), # match classTransition(5.2.m.1Transition) -> association dest
			(20,5), # associationdest -> match_classTransition(5.2.m.2EntryPoint)
			(5,21), # match classEntryPoint(5.2.m.2EntryPoint) -> association owningStateMachine
			(21,6), # associationowningStateMachine -> match_classEntryPoint(5.2.m.3StateMachine)
			(7,22), # apply class LocalDef(5.2.a.0LocalDef) -> association def
			(22,8), # associationdef -> apply_classProcDef(5.2.a.1ProcDef)
			(8,23), # apply class ProcDef(5.2.a.1ProcDef) -> association channelNames
			(23,9), # associationchannelNames -> apply_className(5.2.a.2Name)
			(8,24), # apply class ProcDef(5.2.a.1ProcDef) -> association channelNames
			(24,10), # associationchannelNames -> apply_className(5.2.a.3Name)
			(8,25), # apply class ProcDef(5.2.a.1ProcDef) -> association channelNames
			(25,11), # associationchannelNames -> apply_className(5.2.a.4Name)
			(8,26), # apply class ProcDef(5.2.a.1ProcDef) -> association channelNames
			(26,12), # associationchannelNames -> apply_className(5.2.a.5Name)
			(8,27), # apply class ProcDef(5.2.a.1ProcDef) -> association p
			(27,13), # associationp -> apply_classConditionSet(5.2.a.6ConditionSet)
			(13,28), # apply class ConditionSet(5.2.a.6ConditionSet) -> association alternative
			(28,14), # associationalternative -> apply_classInst(5.2.a.7Inst)
			(14,29), # apply class Inst(5.2.a.7Inst) -> association channelNames
			(29,15), # associationchannelNames -> apply_className(5.2.a.8Name)
			(14,30), # apply class Inst(5.2.a.7Inst) -> association channelNames
			(30,16), # associationchannelNames -> apply_className(5.2.a.9Name)
			(14,31), # apply class Inst(5.2.a.7Inst) -> association channelNames
			(31,17), # associationchannelNames -> apply_className(5.2.a.10Name)
			(14,32), # apply class Inst(5.2.a.7Inst) -> association channelNames
			(32,18), # associationchannelNames -> apply_className(5.2.a.11Name)
			(7,33), # apply class LocalDef(5.2.m.0State) -> backward_association 
			(33,3), # backward_associationState -> match_class State(5.2.m.0State)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = [((8,'name'),('constant','C')),((9,'literal'),('constant','exit')),((10,'literal'),('constant','exack')),((11,'literal'),('constant','enp')),((12,'literal'),('constant','sh')),((14,'name'),('concat',(('constant','S'),(6,'name')))),((15,'literal'),('constant','exit_in')),((16,'literal'),('constant','exack_in')),((17,'literal'),('concat',(('constant','A'),('concat',((5,'name'),('constant','A')))))),((18,'literal'),('constant','sh_in')),]
