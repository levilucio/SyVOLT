from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HContract08_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self, *args, **kwargs):
		"""
		Creates the himesis graph representing the AToM3 model HContract08_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HContract08_CompleteLHS, self).__init__(name='HContract08_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HContract08_CompleteLHS')
		self["equations"] = []
		# Set the node attributes

		# match class Property(Property) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__Property"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Property')

		# match class Class(Class) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__Class"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Class')

		# match class Package(Package) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__Package"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Package')

		# apply class Attribute(Attribute) node
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return True"""
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__Attribute"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Attribute')

		# apply class EntityType(EntityType) node
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return True"""
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__EntityType"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EntityType')

		# apply class ERModel(ERModel) node
		self.add_node()
		self.vs[5]["MT_pre__attr1"] = """return True"""
		self.vs[5]["MT_label__"] = """6"""
		self.vs[5]["mm__"] = """MT_pre__ERModel"""
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ERModel')

		# match association null--ownedProperty-->nullnode
		self.add_node()
		self.vs[6]["MT_pre__attr1"] = """return attr_value == "ownedProperty" """
		self.vs[6]["MT_label__"] = """7"""
		self.vs[6]["mm__"] = """MT_pre__directLink_S"""
		self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Classassoc6Property')

		# match association null--ownedElement-->nullnode
		self.add_node()
		self.vs[7]["MT_pre__attr1"] = """return attr_value == "ownedElement" """
		self.vs[7]["MT_label__"] = """8"""
		self.vs[7]["mm__"] = """MT_pre__directLink_S"""
		self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Packageassoc7Class')

		# apply association null--entities-->nullnode
		self.add_node()
		self.vs[8]["MT_pre__attr1"] = """return attr_value == "entities" """
		self.vs[8]["MT_label__"] = """9"""
		self.vs[8]["mm__"] = """MT_pre__directLink_T"""
		self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ERModelassoc8EntityType')

		# apply association null--features-->nullnode
		self.add_node()
		self.vs[9]["MT_pre__attr1"] = """return attr_value == "features" """
		self.vs[9]["MT_label__"] = """10"""
		self.vs[9]["mm__"] = """MT_pre__directLink_T"""
		self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EntityTypeassoc9Attribute')

		self['equations'].append(((0,'primitiveType'),('constant','NULL')))
		self['equations'].append(((0,'isComplex'),('constant','FALSE')))
		self['equations'].append(((3,'name'),(0,'name')))

		# Add the edges
		self.add_edges([
			(1,6), # match class null(Class) -> association ownedProperty
			(6,0), # association null -> match class null(Property)
			(2,7), # match class null(Package) -> association ownedElement
			(7,1), # association null -> match class null(Class)
			(5,8), # apply class null(ERModel) -> association entities
			(8,4), # association null -> apply class null(EntityType)
			(4,9), # apply class null(EntityType) -> association features
			(9,3), # association null -> apply class null(Attribute)
		])


	# define evaluation methods for each match class.

	def eval_attr11(self, attr_value, this):
		return True

	def eval_attr12(self, attr_value, this):
		return True

	def eval_attr13(self, attr_value, this):
		return True

	# define evaluation methods for each apply class.

	def eval_attr14(self, attr_value, this):
		return True

	def eval_attr15(self, attr_value, this):
		return True

	def eval_attr16(self, attr_value, this):
		return True

		# define evaluation methods for each match association.

	def eval_attr17(self, attr_value, this):
		return attr_value == "ownedProperty"
	def eval_attr18(self, attr_value, this):
		return attr_value == "ownedElement"
		# define evaluation methods for each apply association.

	def eval_attr19(self, attr_value, this):
		return attr_value == "entities"
	def eval_attr110(self, attr_value, this):
		return attr_value == "features"

	def constraint(self, PreNode, graph):
		return True

