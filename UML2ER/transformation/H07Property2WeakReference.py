from core.himesis import Himesis
import uuid

class H07Property2WeakReference(Himesis):
	def __init__(self, *args, **kwargs):
		"""
		Creates the himesis graph representing the DSLTrans rule 07Property2WeakReference.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(H07Property2WeakReference, self).__init__(name='H07Property2WeakReference', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """07Property2WeakReference"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'07Property2WeakReference')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """07Property2WeakReference"""

		# match class Property(Property) node
		self.add_node()
		self.vs[3]["mm__"] = """Property"""
		self.vs[3]["attr1"] = """+"""

		# apply class WeakReference(WeakReference) node
		self.add_node()
		self.vs[4]["mm__"] = """WeakReference"""
		self.vs[4]["attr1"] = """1"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class Property(Property)
			(1,4), # applymodel -> apply_classWeakReference(WeakReference)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = [((3,'isContainment'),('constant','FALSE')),((3,'isComplex'),('constant','TRUE')),((4,'name'),(3,'name')),]
