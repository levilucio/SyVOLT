from core.himesis import Himesis
import uuid

class HState2ProcDef(Himesis):
	def __init__(self, *args, **kwargs):
		"""
		Creates the himesis graph representing the DSLTrans rule State2ProcDef.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HState2ProcDef, self).__init__(name='HState2ProcDef', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """State2ProcDef"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'State2ProcDef')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """State2ProcDef"""

		# match class State(State) node
		self.add_node()
		self.vs[3]["mm__"] = """State"""
		self.vs[3]["attr1"] = """+"""

		# apply class ProcDef(1.0.a.0ProcDef) node
		self.add_node()
		self.vs[4]["mm__"] = """ProcDef"""
		self.vs[4]["attr1"] = """1"""

		# apply class Name(1.0.a.1Name) node
		self.add_node()
		self.vs[5]["mm__"] = """Name"""
		self.vs[5]["attr1"] = """1"""

		# apply class Name(1.0.a.2Name) node
		self.add_node()
		self.vs[6]["mm__"] = """Name"""
		self.vs[6]["attr1"] = """1"""

		# apply class Name(1.0.a.3Name) node
		self.add_node()
		self.vs[7]["mm__"] = """Name"""
		self.vs[7]["attr1"] = """1"""

		# apply association ProcDef--channelNames-->Name node 
		self.add_node()
		self.vs[8]["attr1"] = """channelNames"""
		self.vs[8]["mm__"] = """directLink_T"""

		# apply association ProcDef--channelNames-->Name node 
		self.add_node()
		self.vs[9]["attr1"] = """channelNames"""
		self.vs[9]["mm__"] = """directLink_T"""

		# apply association ProcDef--channelNames-->Name node 
		self.add_node()
		self.vs[10]["attr1"] = """channelNames"""
		self.vs[10]["mm__"] = """directLink_T"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class State(State)
			(1,4), # applymodel -> apply_classProcDef(1.0.a.0ProcDef)
			(1,5), # applymodel -> apply_className(1.0.a.1Name)
			(1,6), # applymodel -> apply_className(1.0.a.2Name)
			(1,7), # applymodel -> apply_className(1.0.a.3Name)
			(4,8), # apply class ProcDef(1.0.a.0ProcDef) -> association channelNames
			(8,5), # associationchannelNames -> apply_className(1.0.a.1Name)
			(4,9), # apply class ProcDef(1.0.a.0ProcDef) -> association channelNames
			(9,6), # associationchannelNames -> apply_className(1.0.a.2Name)
			(4,10), # apply class ProcDef(1.0.a.0ProcDef) -> association channelNames
			(10,7), # associationchannelNames -> apply_className(1.0.a.3Name)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = [((4,'name'),('concat',(('constant','S'),(3,'name')))),((5,'literal'),('constant','exit')),((6,'literal'),('constant','exack')),((7,'literal'),('constant','enp')),]
