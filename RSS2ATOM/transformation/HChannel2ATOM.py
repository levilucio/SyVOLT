from core.himesis import Himesis
import uuid

class HChannel2ATOM(Himesis):
	def __init__(self, *args, **kwargs):
		"""
		Creates the himesis graph representing the DSLTrans rule Channel2ATOM.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HChannel2ATOM, self).__init__(name='HChannel2ATOM', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """Channel2ATOM"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Channel2ATOM')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """Channel2ATOM"""

		# match class Channel(1.0.m.0Channel) node
		self.add_node()
		self.vs[3]["mm__"] = """Channel"""
		self.vs[3]["attr1"] = """+"""

		# apply class ATOM(1.0.a.0ATOM) node
		self.add_node()
		self.vs[4]["mm__"] = """ATOM"""
		self.vs[4]["attr1"] = """1"""

		# apply class Link(1.0.a.1Link) node
		self.add_node()
		self.vs[5]["mm__"] = """Link"""
		self.vs[5]["attr1"] = """1"""

		# apply class Author(1.0.a.2Author) node
		self.add_node()
		self.vs[6]["mm__"] = """Author"""
		self.vs[6]["attr1"] = """1"""

		# apply association ATOM--links-->Link node 
		self.add_node()
		self.vs[7]["attr1"] = """links"""
		self.vs[7]["mm__"] = """directLink_T"""

		# apply association ATOM--authors-->Author node 
		self.add_node()
		self.vs[8]["attr1"] = """authors"""
		self.vs[8]["mm__"] = """directLink_T"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class Channel(1.0.m.0Channel)
			(1,4), # applymodel -> apply_classATOM(1.0.a.0ATOM)
			(1,5), # applymodel -> apply_classLink(1.0.a.1Link)
			(1,6), # applymodel -> apply_classAuthor(1.0.a.2Author)
			(4,7), # apply class ATOM(1.0.a.0ATOM) -> association links
			(7,5), # associationlinks -> apply_classLink(1.0.a.1Link)
			(4,8), # apply class ATOM(1.0.a.0ATOM) -> association authors
			(8,6), # associationauthors -> apply_classAuthor(1.0.a.2Author)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = [((4,'title'),(3,'title')),((4,'subtitle'),(3,'description')),((4,'rights'),(3,'copyright')),((4,'lastUpdate'),(3,'lastBuildDate')),((5,'hrefl'),(3,'link')),((6,'email'),(3,'webmaster')),((6,'name'),(3,'managingEditor')),]
