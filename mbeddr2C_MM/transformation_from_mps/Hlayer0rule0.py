from core.himesis import Himesis
import uuid

class Hlayer0rule0(Himesis):
	def __init__(self):
		"""
		Creates the himesis graph representing the DSLTrans rule layer0rule0.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(Hlayer0rule0, self).__init__(name='Hlayer0rule0', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """layer0rule0"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule0')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """layer0rule0"""

		# match class ImplementationModule(layer0rule0class0ImplementationModule) node
		self.add_node()
		self.vs[3]["mm__"] = """ImplementationModule"""
		self.vs[3]["attr1"] = """+"""

		# apply class ImplementationModule(layer0rule0class1ImplementationModule) node
		self.add_node()
		self.vs[4]["mm__"] = """ImplementationModule"""
		self.vs[4]["attr1"] = """1"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class ImplementationModule(layer0rule0class0ImplementationModule)
			(1,4), # applymodel -> apply_classImplementationModule(layer0rule0class1ImplementationModule)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = [((4,'name'),(3,'name')),]
