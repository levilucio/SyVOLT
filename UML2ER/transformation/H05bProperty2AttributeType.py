from core.himesis import Himesis
import uuid

class H05bProperty2AttributeType(Himesis):
	def __init__(self, *args, **kwargs):
		"""
		Creates the himesis graph representing the DSLTrans rule 05bProperty2AttributeType.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(H05bProperty2AttributeType, self).__init__(name='H05bProperty2AttributeType', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """05bProperty2AttributeType"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'05bProperty2AttributeType')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """05bProperty2AttributeType"""

		# match class Property(Property) node
		self.add_node()
		self.vs[3]["mm__"] = """Property"""
		self.vs[3]["attr1"] = """+"""

		# apply class Attribute(Attribute) node
		self.add_node()
		self.vs[4]["mm__"] = """Attribute"""
		self.vs[4]["attr1"] = """1"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class Property(Property)
			(1,4), # applymodel -> apply_classAttribute(Attribute)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = [((3,'primitiveType'),('constant','NOT NULL')),((3,'isComplex'),('constant','FALSE')),((4,'type'),(3,'primitiveType')),((4,'name'),(3,'name')),]
