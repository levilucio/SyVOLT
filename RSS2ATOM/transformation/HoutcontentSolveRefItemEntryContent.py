from core.himesis import Himesis
import uuid

class HoutcontentSolveRefItemEntryContent(Himesis):
	def __init__(self, *args, **kwargs):
		"""
		Creates the himesis graph representing the DSLTrans rule outcontentSolveRefItemEntryContent.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HoutcontentSolveRefItemEntryContent, self).__init__(name='HoutcontentSolveRefItemEntryContent', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """outcontentSolveRefItemEntryContent"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'outcontentSolveRefItemEntryContent')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """outcontentSolveRefItemEntryContent"""

		# match class Item(7.0.m.0Item) node
		self.add_node()
		self.vs[3]["mm__"] = """Item"""
		self.vs[3]["attr1"] = """+"""

		# apply class Entry(7.0.a.0Entry) node
		self.add_node()
		self.vs[4]["mm__"] = """Entry"""
		self.vs[4]["attr1"] = """1"""

		# apply class Content(7.0.a.1Content) node
		self.add_node()
		self.vs[5]["mm__"] = """Content"""
		self.vs[5]["attr1"] = """1"""

		# apply association Entry--content-->Content node 
		self.add_node()
		self.vs[6]["attr1"] = """content"""
		self.vs[6]["mm__"] = """directLink_T"""

		# backward association Entry-->Itemnode 
		self.add_node()
		self.vs[7]["mm__"] = """backward_link"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class Item(7.0.m.0Item)
			(1,4), # applymodel -> apply_classEntry(7.0.a.0Entry)
			(1,5), # applymodel -> apply_classContent(7.0.a.1Content)
			(4,6), # apply class Entry(7.0.a.0Entry) -> association content
			(6,5), # associationcontent -> apply_classContent(7.0.a.1Content)
			(4,7), # apply class Entry(7.0.m.0Item) -> backward_association 
			(7,3), # backward_associationItem -> match_class Item(7.0.m.0Item)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = []
