from core.himesis import Himesis
import uuid

class HTransition2QInstSIBLING(Himesis):
	def __init__(self):
		"""
		Creates the himesis graph representing the DSLTrans rule Transition2QInstSIBLING.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HTransition2QInstSIBLING, self).__init__(name='HTransition2QInstSIBLING', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """Transition2QInstSIBLING"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Transition2QInstSIBLING')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """Transition2QInstSIBLING"""

		# match class Transition(6.0.m.0Transition) node
		self.add_node()
		self.vs[3]["mm__"] = """Transition"""
		self.vs[3]["attr1"] = """+"""

		# match class Vertex(6.0.m.1Vertex) node
		self.add_node()
		self.vs[4]["mm__"] = """Vertex"""
		self.vs[4]["attr1"] = """1"""

		# match class SIBLING0(6.0.m.2SIBLING0) node
		self.add_node()
		self.vs[5]["mm__"] = """SIBLING0"""
		self.vs[5]["attr1"] = """1"""

		# match class StateMachine(6.0.m.3StateMachine) node
		self.add_node()
		self.vs[6]["mm__"] = """StateMachine"""
		self.vs[6]["attr1"] = """1"""

		# apply class Inst(6.0.a.0Inst) node
		self.add_node()
		self.vs[7]["mm__"] = """Inst"""
		self.vs[7]["attr1"] = """1"""

		# apply class Name(6.0.a.1Name) node
		self.add_node()
		self.vs[8]["mm__"] = """Name"""
		self.vs[8]["attr1"] = """1"""

		# apply class Name(6.0.a.2Name) node
		self.add_node()
		self.vs[9]["mm__"] = """Name"""
		self.vs[9]["attr1"] = """1"""

		# apply class Name(6.0.a.3Name) node
		self.add_node()
		self.vs[10]["mm__"] = """Name"""
		self.vs[10]["attr1"] = """1"""

		# apply class Name(6.0.a.4Name) node
		self.add_node()
		self.vs[11]["mm__"] = """Name"""
		self.vs[11]["attr1"] = """1"""

		# match association Transition--dest-->Vertex node 
		self.add_node()
		self.vs[12]["attr1"] = """dest"""
		self.vs[12]["mm__"] = """directLink_S"""

		# match association Transition--type-->SIBLING0 node 
		self.add_node()
		self.vs[13]["attr1"] = """type"""
		self.vs[13]["mm__"] = """directLink_S"""

		# match association Vertex--owningStateMachine-->StateMachine node 
		self.add_node()
		self.vs[14]["attr1"] = """owningStateMachine"""
		self.vs[14]["mm__"] = """directLink_S"""

		# apply association Inst--channelNames-->Name node 
		self.add_node()
		self.vs[15]["attr1"] = """channelNames"""
		self.vs[15]["mm__"] = """directLink_T"""

		# apply association Inst--channelNames-->Name node 
		self.add_node()
		self.vs[16]["attr1"] = """channelNames"""
		self.vs[16]["mm__"] = """directLink_T"""

		# apply association Inst--channelNames-->Name node 
		self.add_node()
		self.vs[17]["attr1"] = """channelNames"""
		self.vs[17]["mm__"] = """directLink_T"""

		# apply association Inst--channelNames-->Name node 
		self.add_node()
		self.vs[18]["attr1"] = """channelNames"""
		self.vs[18]["mm__"] = """directLink_T"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class Transition(6.0.m.0Transition)
			(0,4), # matchmodel -> match_class Vertex(6.0.m.1Vertex)
			(0,5), # matchmodel -> match_class SIBLING0(6.0.m.2SIBLING0)
			(0,6), # matchmodel -> match_class StateMachine(6.0.m.3StateMachine)
			(1,7), # applymodel -> apply_classInst(6.0.a.0Inst)
			(1,8), # applymodel -> apply_className(6.0.a.1Name)
			(1,9), # applymodel -> apply_className(6.0.a.2Name)
			(1,10), # applymodel -> apply_className(6.0.a.3Name)
			(1,11), # applymodel -> apply_className(6.0.a.4Name)
			(3,12), # match classTransition(6.0.m.0Transition) -> association dest
			(12,4), # associationdest -> match_classTransition(6.0.m.1Vertex)
			(3,13), # match classTransition(6.0.m.0Transition) -> association type
			(13,5), # associationtype -> match_classTransition(6.0.m.2SIBLING0)
			(4,14), # match classVertex(6.0.m.1Vertex) -> association owningStateMachine
			(14,6), # associationowningStateMachine -> match_classVertex(6.0.m.3StateMachine)
			(7,15), # apply class Inst(6.0.a.0Inst) -> association channelNames
			(15,10), # associationchannelNames -> apply_className(6.0.a.3Name)
			(7,16), # apply class Inst(6.0.a.0Inst) -> association channelNames
			(16,8), # associationchannelNames -> apply_className(6.0.a.1Name)
			(7,17), # apply class Inst(6.0.a.0Inst) -> association channelNames
			(17,9), # associationchannelNames -> apply_className(6.0.a.2Name)
			(7,18), # apply class Inst(6.0.a.0Inst) -> association channelNames
			(18,11), # associationchannelNames -> apply_className(6.0.a.4Name)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = [((7,'name'),('concat',(('constant','S'),(6,'name')))),((8,'literal'),('constant','exack')),((9,'literal'),('concat',(('constant','A'),('concat',((4,'name'),('constant','A')))))),((10,'literal'),('constant','exit')),((11,'literal'),('constant','sh')),]
