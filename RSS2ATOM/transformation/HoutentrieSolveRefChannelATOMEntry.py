from core.himesis import Himesis
import uuid

class HoutentrieSolveRefChannelATOMEntry(Himesis):
	def __init__(self):
		"""
		Creates the himesis graph representing the DSLTrans rule outentrieSolveRefChannelATOMEntry.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HoutentrieSolveRefChannelATOMEntry, self).__init__(name='HoutentrieSolveRefChannelATOMEntry', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """outentrieSolveRefChannelATOMEntry"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'outentrieSolveRefChannelATOMEntry')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """outentrieSolveRefChannelATOMEntry"""

		# match class Channel(6.0.m.0Channel) node
		self.add_node()
		self.vs[3]["mm__"] = """Channel"""
		self.vs[3]["attr1"] = """+"""

		# apply class ATOM(6.0.a.0ATOM) node
		self.add_node()
		self.vs[4]["mm__"] = """ATOM"""
		self.vs[4]["attr1"] = """1"""

		# apply class Entry(6.0.a.1Entry) node
		self.add_node()
		self.vs[5]["mm__"] = """Entry"""
		self.vs[5]["attr1"] = """1"""

		# apply association ATOM--entrie-->Entry node 
		self.add_node()
		self.vs[6]["attr1"] = """entrie"""
		self.vs[6]["mm__"] = """directLink_T"""

		# backward association ATOM-->Channelnode 
		self.add_node()
		self.vs[7]["mm__"] = """backward_link"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class Channel(6.0.m.0Channel)
			(1,4), # applymodel -> apply_classATOM(6.0.a.0ATOM)
			(1,5), # applymodel -> apply_classEntry(6.0.a.1Entry)
			(4,6), # apply class ATOM(6.0.a.0ATOM) -> association entrie
			(6,5), # associationentrie -> apply_classEntry(6.0.a.1Entry)
			(4,7), # apply class ATOM(6.0.m.0Channel) -> backward_association 
			(7,3), # backward_associationChannel -> match_class Channel(6.0.m.0Channel)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = []
