from core.himesis import Himesis
import uuid

class HState2HProcDef(Himesis):
	def __init__(self, *args, **kwargs):
		"""
		Creates the himesis graph representing the DSLTrans rule State2HProcDef.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HState2HProcDef, self).__init__(name='HState2HProcDef', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """State2HProcDef"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'State2HProcDef')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """State2HProcDef"""

		# match class State(5.1.m.0State) node
		self.add_node()
		self.vs[3]["mm__"] = """State"""
		self.vs[3]["attr1"] = """+"""

		# apply class LocalDef(5.1.a.0LocalDef) node
		self.add_node()
		self.vs[4]["mm__"] = """LocalDef"""
		self.vs[4]["attr1"] = """1"""

		# apply class ProcDef(5.1.a.1ProcDef) node
		self.add_node()
		self.vs[5]["mm__"] = """ProcDef"""
		self.vs[5]["attr1"] = """1"""

		# apply class Name(5.1.a.2Name) node
		self.add_node()
		self.vs[6]["mm__"] = """Name"""
		self.vs[6]["attr1"] = """1"""

		# apply class Name(5.1.a.3Name) node
		self.add_node()
		self.vs[7]["mm__"] = """Name"""
		self.vs[7]["attr1"] = """1"""

		# apply class Name(5.1.a.4Name) node
		self.add_node()
		self.vs[8]["mm__"] = """Name"""
		self.vs[8]["attr1"] = """1"""

		# apply class Listen(5.1.a.5Listen) node
		self.add_node()
		self.vs[9]["mm__"] = """Listen"""
		self.vs[9]["attr1"] = """1"""

		# apply class ListenBranch(5.1.a.6ListenBranch) node
		self.add_node()
		self.vs[10]["mm__"] = """ListenBranch"""
		self.vs[10]["attr1"] = """1"""

		# apply class Null(5.1.a.7Null) node
		self.add_node()
		self.vs[11]["mm__"] = """Null"""
		self.vs[11]["attr1"] = """1"""

		# apply class ListenBranch(5.1.a.8ListenBranch) node
		self.add_node()
		self.vs[12]["mm__"] = """ListenBranch"""
		self.vs[12]["attr1"] = """1"""

		# apply class Seq(5.1.a.9Seq) node
		self.add_node()
		self.vs[13]["mm__"] = """Seq"""
		self.vs[13]["attr1"] = """1"""

		# apply class Trigger(5.1.a.10Trigger) node
		self.add_node()
		self.vs[14]["mm__"] = """Trigger"""
		self.vs[14]["attr1"] = """1"""

		# apply class Listen(5.1.a.11Listen) node
		self.add_node()
		self.vs[15]["mm__"] = """Listen"""
		self.vs[15]["attr1"] = """1"""

		# apply class ListenBranch(5.1.a.12ListenBranch) node
		self.add_node()
		self.vs[16]["mm__"] = """ListenBranch"""
		self.vs[16]["attr1"] = """1"""

		# apply class Trigger(5.1.a.13Trigger) node
		self.add_node()
		self.vs[17]["mm__"] = """Trigger"""
		self.vs[17]["attr1"] = """1"""

		# apply association LocalDef--def-->ProcDef node 
		self.add_node()
		self.vs[18]["attr1"] = """def"""
		self.vs[18]["mm__"] = """directLink_T"""

		# apply association ProcDef--channelNames-->Name node 
		self.add_node()
		self.vs[19]["attr1"] = """channelNames"""
		self.vs[19]["mm__"] = """directLink_T"""

		# apply association ProcDef--channelNames-->Name node 
		self.add_node()
		self.vs[20]["attr1"] = """channelNames"""
		self.vs[20]["mm__"] = """directLink_T"""

		# apply association ProcDef--channelNames-->Name node 
		self.add_node()
		self.vs[21]["attr1"] = """channelNames"""
		self.vs[21]["mm__"] = """directLink_T"""

		# apply association ProcDef--p-->Listen node 
		self.add_node()
		self.vs[22]["attr1"] = """p"""
		self.vs[22]["mm__"] = """directLink_T"""

		# apply association Listen--branches-->ListenBranch node 
		self.add_node()
		self.vs[23]["attr1"] = """branches"""
		self.vs[23]["mm__"] = """directLink_T"""

		# apply association ListenBranch--p-->Null node 
		self.add_node()
		self.vs[24]["attr1"] = """p"""
		self.vs[24]["mm__"] = """directLink_T"""

		# apply association Listen--branches-->ListenBranch node 
		self.add_node()
		self.vs[25]["attr1"] = """branches"""
		self.vs[25]["mm__"] = """directLink_T"""

		# apply association ListenBranch--p-->Seq node 
		self.add_node()
		self.vs[26]["attr1"] = """p"""
		self.vs[26]["mm__"] = """directLink_T"""

		# apply association Seq--p-->Trigger node 
		self.add_node()
		self.vs[27]["attr1"] = """p"""
		self.vs[27]["mm__"] = """directLink_T"""

		# apply association Seq--p-->Listen node 
		self.add_node()
		self.vs[28]["attr1"] = """p"""
		self.vs[28]["mm__"] = """directLink_T"""

		# apply association Listen--branches-->ListenBranch node 
		self.add_node()
		self.vs[29]["attr1"] = """branches"""
		self.vs[29]["mm__"] = """directLink_T"""

		# apply association ListenBranch--p-->Trigger node 
		self.add_node()
		self.vs[30]["attr1"] = """p"""
		self.vs[30]["mm__"] = """directLink_T"""

		# backward association LocalDef-->Statenode 
		self.add_node()
		self.vs[31]["mm__"] = """backward_link"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class State(5.1.m.0State)
			(1,4), # applymodel -> apply_classLocalDef(5.1.a.0LocalDef)
			(1,5), # applymodel -> apply_classProcDef(5.1.a.1ProcDef)
			(1,6), # applymodel -> apply_className(5.1.a.2Name)
			(1,7), # applymodel -> apply_className(5.1.a.3Name)
			(1,8), # applymodel -> apply_className(5.1.a.4Name)
			(1,9), # applymodel -> apply_classListen(5.1.a.5Listen)
			(1,10), # applymodel -> apply_classListenBranch(5.1.a.6ListenBranch)
			(1,11), # applymodel -> apply_classNull(5.1.a.7Null)
			(1,12), # applymodel -> apply_classListenBranch(5.1.a.8ListenBranch)
			(1,13), # applymodel -> apply_classSeq(5.1.a.9Seq)
			(1,14), # applymodel -> apply_classTrigger(5.1.a.10Trigger)
			(1,15), # applymodel -> apply_classListen(5.1.a.11Listen)
			(1,16), # applymodel -> apply_classListenBranch(5.1.a.12ListenBranch)
			(1,17), # applymodel -> apply_classTrigger(5.1.a.13Trigger)
			(4,18), # apply class LocalDef(5.1.a.0LocalDef) -> association def
			(18,5), # associationdef -> apply_classProcDef(5.1.a.1ProcDef)
			(5,19), # apply class ProcDef(5.1.a.1ProcDef) -> association channelNames
			(19,6), # associationchannelNames -> apply_className(5.1.a.2Name)
			(5,20), # apply class ProcDef(5.1.a.1ProcDef) -> association channelNames
			(20,7), # associationchannelNames -> apply_className(5.1.a.3Name)
			(5,21), # apply class ProcDef(5.1.a.1ProcDef) -> association channelNames
			(21,8), # associationchannelNames -> apply_className(5.1.a.4Name)
			(5,22), # apply class ProcDef(5.1.a.1ProcDef) -> association p
			(22,9), # associationp -> apply_classListen(5.1.a.5Listen)
			(9,23), # apply class Listen(5.1.a.5Listen) -> association branches
			(23,10), # associationbranches -> apply_classListenBranch(5.1.a.6ListenBranch)
			(10,24), # apply class ListenBranch(5.1.a.6ListenBranch) -> association p
			(24,11), # associationp -> apply_classNull(5.1.a.7Null)
			(9,25), # apply class Listen(5.1.a.5Listen) -> association branches
			(25,12), # associationbranches -> apply_classListenBranch(5.1.a.8ListenBranch)
			(12,26), # apply class ListenBranch(5.1.a.8ListenBranch) -> association p
			(26,13), # associationp -> apply_classSeq(5.1.a.9Seq)
			(13,27), # apply class Seq(5.1.a.9Seq) -> association p
			(27,14), # associationp -> apply_classTrigger(5.1.a.10Trigger)
			(13,28), # apply class Seq(5.1.a.9Seq) -> association p
			(28,15), # associationp -> apply_classListen(5.1.a.11Listen)
			(15,29), # apply class Listen(5.1.a.11Listen) -> association branches
			(29,16), # associationbranches -> apply_classListenBranch(5.1.a.12ListenBranch)
			(16,30), # apply class ListenBranch(5.1.a.12ListenBranch) -> association p
			(30,17), # associationp -> apply_classTrigger(5.1.a.13Trigger)
			(4,31), # apply class LocalDef(5.1.m.0State) -> backward_association 
			(31,3), # backward_associationState -> match_class State(5.1.m.0State)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = [((5,'name'),('constant','H')),((6,'literal'),('constant','exit_in')),((7,'literal'),('constant','exack_in')),((8,'literal'),('constant','sh_in')),((10,'channel'),('constant','sh_in')),((12,'channel'),('constant','exit')),((14,'channel'),('constant','exit_in')),((16,'channel'),('constant','exack_in')),((17,'channel'),('constant','exack')),]
