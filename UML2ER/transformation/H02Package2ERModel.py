from core.himesis import Himesis
import uuid

class H02Package2ERModel(Himesis):
	def __init__(self, *args, **kwargs):
		"""
		Creates the himesis graph representing the DSLTrans rule 02Package2ERModel.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(H02Package2ERModel, self).__init__(name='H02Package2ERModel', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """02Package2ERModel"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'02Package2ERModel')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """02Package2ERModel"""

		# match class Package(Package) node
		self.add_node()
		self.vs[3]["mm__"] = """Package"""
		self.vs[3]["attr1"] = """+"""

		# apply class ERModel(ERModel) node
		self.add_node()
		self.vs[4]["mm__"] = """ERModel"""
		self.vs[4]["attr1"] = """1"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class Package(Package)
			(1,4), # applymodel -> apply_classERModel(ERModel)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = [((4,'name'),(3,'name')),]
