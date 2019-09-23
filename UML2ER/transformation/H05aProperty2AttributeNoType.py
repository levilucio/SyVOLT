from core.himesis import Himesis
import uuid

class H05aProperty2AttributeNoType(Himesis):
	def __init__(self):
		"""
		Creates the himesis graph representing the DSLTrans rule 05aProperty2AttributeNoType.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(H05aProperty2AttributeNoType, self).__init__(name='H05aProperty2AttributeNoType', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """05aProperty2AttributeNoType"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'05aProperty2AttributeNoType')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """05aProperty2AttributeNoType"""

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

		self["equations"] = [((3,'primitiveType'),('constant','NULL')),((3,'isComplex'),('constant','FALSE')),((4,'type'),('constant','NoType')),((4,'name'),(3,'name')),]
