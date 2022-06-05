from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HContract10_ConnectedLHS(HimesisPreConditionPatternLHS):
	def __init__(self, *args, **kwargs):
		"""
		Creates the himesis graph representing the AToM3 model HContract10_ConnectedLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HContract10_ConnectedLHS, self).__init__(name='HContract10_ConnectedLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HContract10_ConnectedLHS')
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

		self['equations'].append(((0,'isContainment'),('constant','TRUE')))
		self['equations'].append(((0,'isComplex'),('constant','TRUE')))

		# match association null--ownedProperty-->nullnode
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return attr_value == "ownedProperty" """
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__directLink_S"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Classassoc3Property')

		# match association null--ownedElement-->nullnode
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return attr_value == "ownedElement" """
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__directLink_S"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Packageassoc4Class')

		# Add the edges
		self.add_edges([
			(1,3), # match class null(Class) -> association ownedProperty
			(3,0), # association null -> match class null(Property)
			(2,4), # match class null(Package) -> association ownedElement
			(4,1), # association null -> match class null(Class)
		])


	# define evaluation methods for each match class.

	def eval_attr11(self, attr_value, this):
		return True

	def eval_attr12(self, attr_value, this):
		return True

	def eval_attr13(self, attr_value, this):
		return True

	# define evaluation methods for each match association.

	def eval_attr14(self, attr_value, this):
		return attr_value == "ownedProperty"
	def eval_attr15(self, attr_value, this):
		return attr_value == "ownedElement"

	def constraint(self, PreNode, graph):
		return True

