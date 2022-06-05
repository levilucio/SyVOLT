from core.himesis import Himesis
import uuid

class H09ConnectClass(Himesis):
	def __init__(self, *args, **kwargs):
		"""
		Creates the himesis graph representing the DSLTrans rule 09ConnectClass.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(H09ConnectClass, self).__init__(name='H09ConnectClass', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """09ConnectClass"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'09ConnectClass')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """09ConnectClass"""

		# match class Class(Class) node
		self.add_node()
		self.vs[3]["mm__"] = """Class"""
		self.vs[3]["attr1"] = """+"""

		# match class Package(Package) node
		self.add_node()
		self.vs[4]["mm__"] = """Package"""
		self.vs[4]["attr1"] = """+"""

		# apply class ERModel(ERModel) node
		self.add_node()
		self.vs[5]["mm__"] = """ERModel"""
		self.vs[5]["attr1"] = """1"""

		# apply class EntityType(EntityType) node
		self.add_node()
		self.vs[6]["mm__"] = """EntityType"""
		self.vs[6]["attr1"] = """1"""

		# match association Package--ownedElement-->Class node 
		self.add_node()
		self.vs[7]["attr1"] = """ownedElement"""
		self.vs[7]["mm__"] = """directLink_S"""

		# apply association ERModel--entities-->EntityType node 
		self.add_node()
		self.vs[8]["attr1"] = """entities"""
		self.vs[8]["mm__"] = """directLink_T"""

		# backward association ERModel-->Packagenode 
		self.add_node()
		self.vs[9]["mm__"] = """backward_link"""

		# backward association EntityType-->Classnode 
		self.add_node()
		self.vs[10]["mm__"] = """backward_link"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class Class(Class)
			(0,4), # matchmodel -> match_class Package(Package)
			(1,5), # applymodel -> apply_classERModel(ERModel)
			(1,6), # applymodel -> apply_classEntityType(EntityType)
			(4,7), # match classPackage(Package) -> association ownedElement
			(7,3), # associationownedElement -> match_classPackage(Class)
			(5,8), # apply class ERModel(ERModel) -> association entities
			(8,6), # associationentities -> apply_classEntityType(EntityType)
			(5,9), # apply class ERModel(Package) -> backward_association 
			(9,4), # backward_associationPackage -> match_class Package(Package)
			(6,10), # apply class EntityType(Class) -> backward_association 
			(10,3), # backward_associationClass -> match_class Class(Class)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = []
