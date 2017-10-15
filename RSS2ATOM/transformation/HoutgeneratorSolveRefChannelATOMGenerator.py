from core.himesis import Himesis
import uuid

class HoutgeneratorSolveRefChannelATOMGenerator(Himesis):
	def __init__(self):
		"""
		Creates the himesis graph representing the DSLTrans rule outgeneratorSolveRefChannelATOMGenerator.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HoutgeneratorSolveRefChannelATOMGenerator, self).__init__(name='HoutgeneratorSolveRefChannelATOMGenerator', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """outgeneratorSolveRefChannelATOMGenerator"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'outgeneratorSolveRefChannelATOMGenerator')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """outgeneratorSolveRefChannelATOMGenerator"""

		# match class Channel(4.0.m.0Channel) node
		self.add_node()
		self.vs[3]["mm__"] = """Channel"""
		self.vs[3]["attr1"] = """+"""

		# apply class ATOM(4.0.a.0ATOM) node
		self.add_node()
		self.vs[4]["mm__"] = """ATOM"""
		self.vs[4]["attr1"] = """1"""

		# apply class Generator(4.0.a.1Generator) node
		self.add_node()
		self.vs[5]["mm__"] = """Generator"""
		self.vs[5]["attr1"] = """1"""

		# apply association ATOM--generator-->Generator node 
		self.add_node()
		self.vs[6]["attr1"] = """generator"""
		self.vs[6]["mm__"] = """directLink_T"""

		# backward association ATOM-->Channelnode 
		self.add_node()
		self.vs[7]["mm__"] = """backward_link"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class Channel(4.0.m.0Channel)
			(1,4), # applymodel -> apply_classATOM(4.0.a.0ATOM)
			(1,5), # applymodel -> apply_classGenerator(4.0.a.1Generator)
			(4,6), # apply class ATOM(4.0.a.0ATOM) -> association generator
			(6,5), # associationgenerator -> apply_classGenerator(4.0.a.1Generator)
			(4,7), # apply class ATOM(4.0.m.0Channel) -> backward_association 
			(7,3), # backward_associationChannel -> match_class Channel(4.0.m.0Channel)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = []
