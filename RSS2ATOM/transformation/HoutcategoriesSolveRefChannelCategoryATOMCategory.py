from core.himesis import Himesis
import uuid

class HoutcategoriesSolveRefChannelCategoryATOMCategory(Himesis):
	def __init__(self, *args, **kwargs):
		"""
		Creates the himesis graph representing the DSLTrans rule outcategoriesSolveRefChannelCategoryATOMCategory.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HoutcategoriesSolveRefChannelCategoryATOMCategory, self).__init__(name='HoutcategoriesSolveRefChannelCategoryATOMCategory', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """outcategoriesSolveRefChannelCategoryATOMCategory"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'outcategoriesSolveRefChannelCategoryATOMCategory')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """outcategoriesSolveRefChannelCategoryATOMCategory"""

		# match class Channel(5.0.m.0Channel) node
		self.add_node()
		self.vs[3]["mm__"] = """Channel"""
		self.vs[3]["attr1"] = """+"""

		# match class Category(5.0.m.1Category) node
		self.add_node()
		self.vs[4]["mm__"] = """Category"""
		self.vs[4]["attr1"] = """+"""

		# apply class ATOM(5.0.a.0ATOM) node
		self.add_node()
		self.vs[5]["mm__"] = """ATOM"""
		self.vs[5]["attr1"] = """1"""

		# apply class Category(5.0.a.1Category) node
		self.add_node()
		self.vs[6]["mm__"] = """Category"""
		self.vs[6]["attr1"] = """1"""

		# match association Channel--category-->Category node 
		self.add_node()
		self.vs[7]["attr1"] = """category"""
		self.vs[7]["mm__"] = """directLink_S"""

		# apply association ATOM--categories-->Category node 
		self.add_node()
		self.vs[8]["attr1"] = """categories"""
		self.vs[8]["mm__"] = """directLink_T"""

		# backward association ATOM-->Channelnode 
		self.add_node()
		self.vs[9]["mm__"] = """backward_link"""

		# backward association Category-->Categorynode 
		self.add_node()
		self.vs[10]["mm__"] = """backward_link"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class Channel(5.0.m.0Channel)
			(0,4), # matchmodel -> match_class Category(5.0.m.1Category)
			(1,5), # applymodel -> apply_classATOM(5.0.a.0ATOM)
			(1,6), # applymodel -> apply_classCategory(5.0.a.1Category)
			(3,7), # match classChannel(5.0.m.0Channel) -> association category
			(7,4), # associationcategory -> match_classChannel(5.0.m.1Category)
			(5,8), # apply class ATOM(5.0.a.0ATOM) -> association categories
			(8,6), # associationcategories -> apply_classCategory(5.0.a.1Category)
			(5,9), # apply class ATOM(5.0.m.0Channel) -> backward_association 
			(9,3), # backward_associationChannel -> match_class Channel(5.0.m.0Channel)
			(6,10), # apply class Category(5.0.m.1Category) -> backward_association 
			(10,4), # backward_associationCategory -> match_class Category(5.0.m.1Category)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = []
