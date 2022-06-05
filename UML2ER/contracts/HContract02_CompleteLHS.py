from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HContract02_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self, *args, **kwargs):
		"""
		Creates the himesis graph representing the AToM3 model HContract02_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HContract02_CompleteLHS, self).__init__(name='HContract02_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HContract02_CompleteLHS')
		self["equations"] = []
		# Set the node attributes

		# match class Class(Class) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__Class"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Class')

		# match class Package(Package) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__Package"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Package')

		# apply class EntityType(EntityType) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__EntityType"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EntityType')

		# apply class ERModel(ERModel) node
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return True"""
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__ERModel"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ERModel')

		# match association null--ownedElement-->nullnode
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return attr_value == "ownedElement" """
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__directLink_S"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Packageassoc4Class')

		# apply association null--entities-->nullnode
		self.add_node()
		self.vs[5]["MT_pre__attr1"] = """return attr_value == "entities" """
		self.vs[5]["MT_label__"] = """6"""
		self.vs[5]["mm__"] = """MT_pre__directLink_T"""
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ERModelassoc5EntityType')

		self['equations'].append(((2,'name'),(0,'name')))
		self['equations'].append(((3,'name'),(1,'name')))

		# Add the edges
		self.add_edges([
			(1,4), # match class null(Package) -> association ownedElement
			(4,0), # association null -> match class null(Class)
			(3,5), # apply class null(ERModel) -> association entities
			(5,2), # association null -> apply class null(EntityType)
		])


	# define evaluation methods for each match class.

	def eval_attr11(self, attr_value, this):
		return True

	def eval_attr12(self, attr_value, this):
		return True

	# define evaluation methods for each apply class.

	def eval_attr13(self, attr_value, this):
		return True

	def eval_attr14(self, attr_value, this):
		return True

		# define evaluation methods for each match association.

	def eval_attr15(self, attr_value, this):
		return attr_value == "ownedElement"
		# define evaluation methods for each apply association.

	def eval_attr16(self, attr_value, this):
		return attr_value == "entities"

	def constraint(self, PreNode, graph):
		return True

