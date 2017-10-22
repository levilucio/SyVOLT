from core.himesis import Himesis
import uuid

class HTransition2Inst(Himesis):
	def __init__(self):
		"""
		Creates the himesis graph representing the DSLTrans rule Transition2Inst.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HTransition2Inst, self).__init__(name='HTransition2Inst', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """Transition2Inst"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Transition2Inst')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """Transition2Inst"""

		# match class State(6.2.m.0State) node
		self.add_node()
		self.vs[3]["mm__"] = """State"""
		self.vs[3]["attr1"] = """+"""

		# match class Transition(6.2.m.1Transition) node
		self.add_node()
		self.vs[4]["mm__"] = """Transition"""
		self.vs[4]["attr1"] = """+"""

		# match class IN1(6.2.m.2IN1) node
		self.add_node()
		self.vs[5]["mm__"] = """IN1"""
		self.vs[5]["attr1"] = """1"""

		# match class EntryPoint(6.2.m.3EntryPoint) node
		self.add_node()
		self.vs[6]["mm__"] = """EntryPoint"""
		self.vs[6]["attr1"] = """1"""

		# match class StateMachine(6.2.m.4StateMachine) node
		self.add_node()
		self.vs[7]["mm__"] = """StateMachine"""
		self.vs[7]["attr1"] = """1"""

		# apply class Inst(6.2.a.0Inst) node
		self.add_node()
		self.vs[8]["mm__"] = """Inst"""
		self.vs[8]["attr1"] = """1"""

		# apply class Name(6.2.a.1Name) node
		self.add_node()
		self.vs[9]["mm__"] = """Name"""
		self.vs[9]["attr1"] = """1"""

		# apply class Name(6.2.a.2Name) node
		self.add_node()
		self.vs[10]["mm__"] = """Name"""
		self.vs[10]["attr1"] = """1"""

		# apply class Name(6.2.a.3Name) node
		self.add_node()
		self.vs[11]["mm__"] = """Name"""
		self.vs[11]["attr1"] = """1"""

		# apply class Name(6.2.a.4Name) node
		self.add_node()
		self.vs[12]["mm__"] = """Name"""
		self.vs[12]["attr1"] = """1"""

		# match association State--transitions-->Transition node 
		self.add_node()
		self.vs[13]["attr1"] = """transitions"""
		self.vs[13]["mm__"] = """directLink_S"""

		# match association Transition--type-->IN1 node 
		self.add_node()
		self.vs[14]["attr1"] = """type"""
		self.vs[14]["mm__"] = """directLink_S"""

		# match association Transition--dest-->EntryPoint node 
		self.add_node()
		self.vs[15]["attr1"] = """dest"""
		self.vs[15]["mm__"] = """directLink_S"""

		# match association EntryPoint--owningStateMachine-->StateMachine node 
		self.add_node()
		self.vs[16]["attr1"] = """owningStateMachine"""
		self.vs[16]["mm__"] = """directLink_S"""

		# apply association Inst--channelNames-->Name node 
		self.add_node()
		self.vs[17]["attr1"] = """channelNames"""
		self.vs[17]["mm__"] = """directLink_T"""

		# apply association Inst--channelNames-->Name node 
		self.add_node()
		self.vs[18]["attr1"] = """channelNames"""
		self.vs[18]["mm__"] = """directLink_T"""

		# apply association Inst--channelNames-->Name node 
		self.add_node()
		self.vs[19]["attr1"] = """channelNames"""
		self.vs[19]["mm__"] = """directLink_T"""

		# apply association Inst--channelNames-->Name node 
		self.add_node()
		self.vs[20]["attr1"] = """channelNames"""
		self.vs[20]["mm__"] = """directLink_T"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class State(6.2.m.0State)
			(0,4), # matchmodel -> match_class Transition(6.2.m.1Transition)
			(0,5), # matchmodel -> match_class IN1(6.2.m.2IN1)
			(0,6), # matchmodel -> match_class EntryPoint(6.2.m.3EntryPoint)
			(0,7), # matchmodel -> match_class StateMachine(6.2.m.4StateMachine)
			(1,8), # applymodel -> apply_classInst(6.2.a.0Inst)
			(1,9), # applymodel -> apply_className(6.2.a.1Name)
			(1,10), # applymodel -> apply_className(6.2.a.2Name)
			(1,11), # applymodel -> apply_className(6.2.a.3Name)
			(1,12), # applymodel -> apply_className(6.2.a.4Name)
			(3,13), # match classState(6.2.m.0State) -> association transitions
			(13,4), # associationtransitions -> match_classState(6.2.m.1Transition)
			(4,14), # match classTransition(6.2.m.1Transition) -> association type
			(14,5), # associationtype -> match_classTransition(6.2.m.2IN1)
			(4,15), # match classTransition(6.2.m.1Transition) -> association dest
			(15,6), # associationdest -> match_classTransition(6.2.m.3EntryPoint)
			(6,16), # match classEntryPoint(6.2.m.3EntryPoint) -> association owningStateMachine
			(16,7), # associationowningStateMachine -> match_classEntryPoint(6.2.m.4StateMachine)
			(8,17), # apply class Inst(6.2.a.0Inst) -> association channelNames
			(17,9), # associationchannelNames -> apply_className(6.2.a.1Name)
			(8,18), # apply class Inst(6.2.a.0Inst) -> association channelNames
			(18,10), # associationchannelNames -> apply_className(6.2.a.2Name)
			(8,19), # apply class Inst(6.2.a.0Inst) -> association channelNames
			(19,11), # associationchannelNames -> apply_className(6.2.a.3Name)
			(8,20), # apply class Inst(6.2.a.0Inst) -> association channelNames
			(20,12), # associationchannelNames -> apply_className(6.2.a.4Name)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = [((8,'name'),('concat',(('constant','S'),(7,'name')))),((9,'literal'),('constant','exit_in')),((10,'literal'),('constant','exack_in')),((11,'literal'),('concat',(('constant','A'),('concat',((6,'name'),('constant','A')))))),((12,'literal'),('constant','sh_in')),]
