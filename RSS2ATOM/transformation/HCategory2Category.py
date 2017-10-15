from core.himesis import Himesis
import uuid

class HCategory2Category(Himesis):
	def __init__(self):
		"""
		Creates the himesis graph representing the DSLTrans rule Category2Category.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HCategory2Category, self).__init__(name='HCategory2Category', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """Category2Category"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Category2Category')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """Category2Category"""

		# match class Category(3.0.m.0Category) node
		self.add_node()
		self.vs[3]["mm__"] = """Category"""
		self.vs[3]["attr1"] = """+"""

		# apply class Category(3.0.a.0Category) node
		self.add_node()
		self.vs[4]["mm__"] = """Category"""
		self.vs[4]["attr1"] = """1"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class Category(3.0.m.0Category)
			(1,4), # applymodel -> apply_classCategory(3.0.a.0Category)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = [((4,'scheme'),(3,'domain')),((4,'label'),(3,'value')),]
