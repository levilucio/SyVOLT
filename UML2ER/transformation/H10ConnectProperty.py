from core.himesis import Himesis
import uuid

class H10ConnectProperty(Himesis):
	def __init__(self):
		"""
		Creates the himesis graph representing the DSLTrans rule 10ConnectProperty.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(H10ConnectProperty, self).__init__(name='H10ConnectProperty', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """10ConnectProperty"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'10ConnectProperty')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """10ConnectProperty"""

		# match class Property(Property) node
		self.add_node()
		self.vs[3]["mm__"] = """Property"""
		self.vs[3]["attr1"] = """+"""

		# match class Class(Class) node
		self.add_node()
		self.vs[4]["mm__"] = """Class"""
		self.vs[4]["attr1"] = """+"""

		# apply class Feature(Feature) node
		self.add_node()
		self.vs[5]["mm__"] = """Feature"""
		self.vs[5]["attr1"] = """1"""

		# apply class EntityType(EntityType) node
		self.add_node()
		self.vs[6]["mm__"] = """EntityType"""
		self.vs[6]["attr1"] = """1"""

		# match association Class--ownedProperty-->Property node 
		self.add_node()
		self.vs[7]["attr1"] = """ownedProperty"""
		self.vs[7]["mm__"] = """directLink_S"""

		# apply association EntityType--features-->Feature node 
		self.add_node()
		self.vs[8]["attr1"] = """features"""
		self.vs[8]["mm__"] = """directLink_T"""

		# backward association EntityType-->Classnode 
		self.add_node()
		self.vs[9]["mm__"] = """backward_link"""

		# backward association Feature-->Propertynode 
		self.add_node()
		self.vs[10]["mm__"] = """backward_link"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class Property(Property)
			(0,4), # matchmodel -> match_class Class(Class)
			(1,5), # applymodel -> apply_classFeature(Feature)
			(1,6), # applymodel -> apply_classEntityType(EntityType)
			(4,7), # match classClass(Class) -> association ownedProperty
			(7,3), # associationownedProperty -> match_classClass(Property)
			(6,8), # apply class EntityType(EntityType) -> association features
			(8,5), # associationfeatures -> apply_classFeature(Feature)
			(6,9), # apply class EntityType(Class) -> backward_association 
			(9,4), # backward_associationClass -> match_class Class(Class)
			(5,10), # apply class Feature(Property) -> backward_association 
			(10,3), # backward_associationProperty -> match_class Property(Property)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = []
