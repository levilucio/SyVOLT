from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HContract14Then_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HContract14Then_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HContract14Then_CompleteLHS, self).__init__(name='HContract14Then_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HContract14Then_CompleteLHS')
		self["equations"] = []
		# Set the node attributes

		# match class Property(Property) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__Property"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Property')

		# match class ClassRef(ClassRef) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__ClassRef"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ClassRef')

		# match class Class(Class) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__Class"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Class')

		# apply class EntityType(EntityType) node
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return True"""
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__EntityType"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EntityType')

		# apply class StrongReference(StrongReference) node
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return True"""
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__StrongReference"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'StrongReference')

		# match association null--complexType-->nullnode
		self.add_node()
		self.vs[5]["MT_pre__attr1"] = """return attr_value == "complexType" """
		self.vs[5]["MT_label__"] = """6"""
		self.vs[5]["mm__"] = """MT_pre__directLink_S"""
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Propertyassoc5ClassRef')

		# match association null--class-->nullnode
		self.add_node()
		self.vs[6]["MT_pre__attr1"] = """return attr_value == "class" """
		self.vs[6]["MT_label__"] = """7"""
		self.vs[6]["mm__"] = """MT_pre__directLink_S"""
		self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ClassRefassoc6Class')

		# apply association null--type-->nullnode
		self.add_node()
		self.vs[7]["MT_pre__attr1"] = """return attr_value == "type" """
		self.vs[7]["MT_label__"] = """8"""
		self.vs[7]["mm__"] = """MT_pre__directLink_T"""
		self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'StrongReferenceassoc7EntityType')

		# trace association null--trace-->nullnode
		self.add_node()
		self.vs[8]["MT_label__"] = """9"""
		self.vs[8]["mm__"] = """MT_pre__trace_link"""
		self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EntityTypeassoc8Class')

		# trace association null--trace-->nullnode
		self.add_node()
		self.vs[9]["MT_label__"] = """10"""
		self.vs[9]["mm__"] = """MT_pre__trace_link"""
		self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'StrongReferenceassoc9Property')

		self['equations'].append(((3,'name'),(2,'name')))
		self["equations"].append(((4,'pivot'),('constant','StrongReferenced91baae5StrongReference')))


		# Add the edges
		self.add_edges([
			(0,5), # match class null(Property) -> association complexType
			(5,1), # association null -> match class null(ClassRef)
			(1,6), # match class null(ClassRef) -> association class
			(6,2), # association null -> match class null(Class)
			(4,7), # apply class null(StrongReference) -> association type
			(7,3), # association null -> apply class null(EntityType)
			(3,8), # apply class null(Class) -> backward_association 
			(8,2), # backward_associationnull -> match_class null(Class)
			(4,9), # apply class null(Property) -> backward_association 
			(9,0), # backward_associationnull -> match_class null(Property)
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

		# define evaluation methods for each match association.

	def eval_attr16(self, attr_value, this):
		return attr_value == "complexType"
	def eval_attr17(self, attr_value, this):
		return attr_value == "class"
		# define evaluation methods for each apply association.

	def eval_attr18(self, attr_value, this):
		return attr_value == "type"

	def constraint(self, PreNode, graph):
		return True

