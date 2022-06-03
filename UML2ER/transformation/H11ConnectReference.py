from core.himesis import Himesis
import uuid

class H11ConnectReference(Himesis):
	def __init__(self, *args, **kwargs):
		"""
		Creates the himesis graph representing the DSLTrans rule 11ConnectReference.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(H11ConnectReference, self).__init__(name='H11ConnectReference', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """11ConnectReference"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'11ConnectReference')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """11ConnectReference"""

		# match class Property(Property) node
		self.add_node()
		self.vs[3]["mm__"] = """Property"""
		self.vs[3]["attr1"] = """+"""

		# match class Class(Class) node
		self.add_node()
		self.vs[4]["mm__"] = """Class"""
		self.vs[4]["attr1"] = """+"""

		# match class ClassRef(ClassRef) node
		self.add_node()
		self.vs[5]["mm__"] = """ClassRef"""
		self.vs[5]["attr1"] = """+"""

		# apply class Reference(Reference) node
		self.add_node()
		self.vs[6]["mm__"] = """Reference"""
		self.vs[6]["attr1"] = """1"""

		# apply class EntityType(EntityType) node
		self.add_node()
		self.vs[7]["mm__"] = """EntityType"""
		self.vs[7]["attr1"] = """1"""

		# match association Property--complexType-->ClassRef node 
		self.add_node()
		self.vs[8]["attr1"] = """complexType"""
		self.vs[8]["mm__"] = """directLink_S"""

		# match association ClassRef--class-->Class node 
		self.add_node()
		self.vs[9]["attr1"] = """class"""
		self.vs[9]["mm__"] = """directLink_S"""

		# apply association Reference--type-->EntityType node 
		self.add_node()
		self.vs[10]["attr1"] = """type"""
		self.vs[10]["mm__"] = """directLink_T"""

		# backward association Reference-->Propertynode 
		self.add_node()
		self.vs[11]["mm__"] = """backward_link"""

		# backward association EntityType-->Classnode 
		self.add_node()
		self.vs[12]["mm__"] = """backward_link"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class Property(Property)
			(0,4), # matchmodel -> match_class Class(Class)
			(0,5), # matchmodel -> match_class ClassRef(ClassRef)
			(1,6), # applymodel -> apply_classReference(Reference)
			(1,7), # applymodel -> apply_classEntityType(EntityType)
			(3,8), # match classProperty(Property) -> association complexType
			(8,5), # associationcomplexType -> match_classProperty(ClassRef)
			(5,9), # match classClassRef(ClassRef) -> association class
			(9,4), # associationclass -> match_classClassRef(Class)
			(6,10), # apply class Reference(Reference) -> association type
			(10,7), # associationtype -> apply_classEntityType(EntityType)
			(6,11), # apply class Reference(Property) -> backward_association 
			(11,3), # backward_associationProperty -> match_class Property(Property)
			(7,12), # apply class EntityType(Class) -> backward_association 
			(12,4), # backward_associationClass -> match_class Class(Class)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = [((3,'isComplex'),('constant','TRUE')),]
