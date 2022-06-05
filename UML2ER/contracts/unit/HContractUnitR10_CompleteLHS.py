from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HContractUnitR10_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self, *args, **kwargs):
		"""
		Creates the himesis graph representing the AToM3 model HContractUnitR10_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HContractUnitR10_CompleteLHS, self).__init__(name='HContractUnitR10_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HContractUnitR10_CompleteLHS')
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

		# apply class Feature(Feature) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__Feature"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Feature')

		# apply class EntityType(EntityType) node
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return True"""
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__EntityType"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EntityType')

		# match association null--ownedProperty-->nullnode
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return attr_value == "ownedProperty" """
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__directLink_S"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Classassoc4Property')

		# apply association null--features-->nullnode
		self.add_node()
		self.vs[5]["MT_pre__attr1"] = """return attr_value == "features" """
		self.vs[5]["MT_label__"] = """6"""
		self.vs[5]["mm__"] = """MT_pre__directLink_T"""
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EntityTypeassoc5Feature')

		# trace association null--trace-->nullnode
		self.add_node()
		self.vs[6]["MT_label__"] = """7"""
		self.vs[6]["mm__"] = """MT_pre__trace_link"""
		self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EntityTypeassoc6Class')

		# trace association null--trace-->nullnode
		self.add_node()
		self.vs[7]["MT_label__"] = """8"""
		self.vs[7]["mm__"] = """MT_pre__trace_link"""
		self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Featureassoc7Property')


		# Add the edges
		self.add_edges([
			(1,4), # match class null(Class) -> association ownedProperty
			(4,0), # association null -> match class null(Property)
			(3,5), # apply class null(EntityType) -> association features
			(5,2), # association null -> apply class null(Feature)
			(3,6), # apply class null(Class) -> backward_association 
			(6,1), # backward_associationnull -> match_class null(Class)
			(2,7), # apply class null(Property) -> backward_association 
			(7,0), # backward_associationnull -> match_class null(Property)
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
		return attr_value == "ownedProperty"
		# define evaluation methods for each apply association.

	def eval_attr16(self, attr_value, this):
		return attr_value == "features"

	def constraint(self, PreNode, graph):
		return True

