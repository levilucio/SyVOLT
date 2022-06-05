from core.himesis import Himesis
import uuid

class HItem2Entry(Himesis):
	def __init__(self, *args, **kwargs):
		"""
		Creates the himesis graph representing the DSLTrans rule Item2Entry.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HItem2Entry, self).__init__(name='HItem2Entry', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """Item2Entry"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Item2Entry')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """Item2Entry"""

		# match class Item(2.0.m.0Item) node
		self.add_node()
		self.vs[3]["mm__"] = """Item"""
		self.vs[3]["attr1"] = """+"""

		# apply class Entry(2.0.a.0Entry) node
		self.add_node()
		self.vs[4]["mm__"] = """Entry"""
		self.vs[4]["attr1"] = """1"""

		# apply class Link(2.0.a.1Link) node
		self.add_node()
		self.vs[5]["mm__"] = """Link"""
		self.vs[5]["attr1"] = """1"""

		# apply association Entry--links-->Link node 
		self.add_node()
		self.vs[6]["attr1"] = """links"""
		self.vs[6]["mm__"] = """directLink_T"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class Item(2.0.m.0Item)
			(1,4), # applymodel -> apply_classEntry(2.0.a.0Entry)
			(1,5), # applymodel -> apply_classLink(2.0.a.1Link)
			(4,6), # apply class Entry(2.0.a.0Entry) -> association links
			(6,5), # associationlinks -> apply_classLink(2.0.a.1Link)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = [((4,'title'),(3,'title')),((4,'id'),(3,'guid')),((4,'published'),(3,'pubDate')),((4,'summary'),(3,'comments')),((5,'hrefl'),(3,'link')),]
