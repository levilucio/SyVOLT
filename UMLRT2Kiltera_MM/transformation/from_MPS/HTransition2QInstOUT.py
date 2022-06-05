from core.himesis import Himesis
import uuid

class HTransition2QInstOUT(Himesis):
	def __init__(self, *args, **kwargs):
		"""
		Creates the himesis graph representing the DSLTrans rule Transition2QInstOUT.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HTransition2QInstOUT, self).__init__(name='HTransition2QInstOUT', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """Transition2QInstOUT"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Transition2QInstOUT')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """Transition2QInstOUT"""

		# match class Transition(6.1.m.0Transition) node
		self.add_node()
		self.vs[3]["mm__"] = """Transition"""
		self.vs[3]["attr1"] = """+"""

		# match class OUT2(6.1.m.1OUT2) node
		self.add_node()
		self.vs[4]["mm__"] = """OUT2"""
		self.vs[4]["attr1"] = """1"""

		# match class StateMachine(6.1.m.2StateMachine) node
		self.add_node()
		self.vs[5]["mm__"] = """StateMachine"""
		self.vs[5]["attr1"] = """1"""

		# match class Vertex(6.1.m.3Vertex) node
		self.add_node()
		self.vs[6]["mm__"] = """Vertex"""
		self.vs[6]["attr1"] = """1"""

		# apply class Inst(6.1.a.0Inst) node
		self.add_node()
		self.vs[7]["mm__"] = """Inst"""
		self.vs[7]["attr1"] = """1"""

		# apply class Name(6.1.a.1Name) node
		self.add_node()
		self.vs[8]["mm__"] = """Name"""
		self.vs[8]["attr1"] = """1"""

		# match association Transition--type-->OUT2 node 
		self.add_node()
		self.vs[9]["attr1"] = """type"""
		self.vs[9]["mm__"] = """directLink_S"""

		# match association Transition--owningStateMachine-->StateMachine node 
		self.add_node()
		self.vs[10]["attr1"] = """owningStateMachine"""
		self.vs[10]["mm__"] = """directLink_S"""

		# match association StateMachine--exitPoints-->Vertex node 
		self.add_node()
		self.vs[11]["attr1"] = """exitPoints"""
		self.vs[11]["mm__"] = """directLink_S"""

		# match association Transition--dest-->Vertex node 
		self.add_node()
		self.vs[12]["attr1"] = """dest"""
		self.vs[12]["mm__"] = """directLink_S"""

		# apply association Inst--channelNames-->Name node 
		self.add_node()
		self.vs[13]["attr1"] = """channelNames"""
		self.vs[13]["mm__"] = """directLink_T"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class Transition(6.1.m.0Transition)
			(0,4), # matchmodel -> match_class OUT2(6.1.m.1OUT2)
			(0,5), # matchmodel -> match_class StateMachine(6.1.m.2StateMachine)
			(0,6), # matchmodel -> match_class Vertex(6.1.m.3Vertex)
			(1,7), # applymodel -> apply_classInst(6.1.a.0Inst)
			(1,8), # applymodel -> apply_className(6.1.a.1Name)
			(3,9), # match classTransition(6.1.m.0Transition) -> association type
			(9,4), # associationtype -> match_classTransition(6.1.m.1OUT2)
			(3,10), # match classTransition(6.1.m.0Transition) -> association owningStateMachine
			(10,5), # associationowningStateMachine -> match_classTransition(6.1.m.2StateMachine)
			(5,11), # match classStateMachine(6.1.m.2StateMachine) -> association exitPoints
			(11,6), # associationexitPoints -> match_classStateMachine(6.1.m.3Vertex)
			(3,12), # match classTransition(6.1.m.0Transition) -> association dest
			(12,6), # associationdest -> match_classTransition(6.1.m.3Vertex)
			(7,13), # apply class Inst(6.1.a.0Inst) -> association channelNames
			(13,8), # associationchannelNames -> apply_className(6.1.a.1Name)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = [((7,'name'),('concat',(('constant','B'),(6,'name')))),((8,'literal'),('constant','sh')),]
