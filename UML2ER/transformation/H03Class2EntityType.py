from core.himesis import Himesis
import uuid

class H03Class2EntityType(Himesis):
	def __init__(self):
		"""
		Creates the himesis graph representing the DSLTrans rule 03Class2EntityType.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(H03Class2EntityType, self).__init__(name='H03Class2EntityType', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """03Class2EntityType"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'03Class2EntityType')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """03Class2EntityType"""

		# match class Class(AnyMatch-5f5cf29d) node
		self.add_node()
		self.vs[3]["mm__"] = """Class"""
		self.vs[3]["attr1"] = """+"""

		# apply class EntityType(ApplyClass-f9ee3482) node
		self.add_node()
		self.vs[4]["mm__"] = """EntityType"""
		self.vs[4]["attr1"] = """1"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class Class(AnyMatch-5f5cf29d)
			(1,4), # applymodel -> apply_classEntityType(ApplyClass-f9ee3482)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = [((4,'name'),(3,'name')),]
