from core.himesis import Himesis
import uuid

class HMapRootElementRule(Himesis):
	def __init__(self, *args, **kwargs):
		"""
		Creates the himesis graph representing the DSLTrans rule MapRootElementRule.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HMapRootElementRule, self).__init__(name='HMapRootElementRule', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """MapRootElementRule"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'MapRootElementRule')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """MapRootElementRule"""

		# match class RootElement(2.0.m.0RootElement) node
		self.add_node()
		self.vs[3]["mm__"] = """RootElement"""
		self.vs[3]["attr1"] = """+"""

		# apply class RootElement(2.0.a.0RootElement) node
		self.add_node()
		self.vs[4]["mm__"] = """RootElement"""
		self.vs[4]["attr1"] = """1"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class RootElement(2.0.m.0RootElement)
			(1,4), # applymodel -> apply_classRootElement(2.0.a.0RootElement)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = []
