from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HContractUnitR03_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HContractUnitR03_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HContractUnitR03_CompleteLHS, self).__init__(name='HContractUnitR03_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HContractUnitR03_CompleteLHS')
		self["equations"] = []
		# Set the node attributes

		# match class Class(Class) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__Class"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Class')

		# apply class EntityType(EntityType) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__EntityType"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EntityType')

		# trace association null--trace-->nullnode
		self.add_node()
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__trace_link"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EntityTypeassoc2Class')

		self['equations'].append(((1,'name'),(0,'name')))

		# Add the edges
		self.add_edges([
			(1,2), # apply class null(Class) -> backward_association 
			(2,0), # backward_associationnull -> match_class null(Class)
		])


	# define evaluation methods for each match class.

	def eval_attr11(self, attr_value, this):
		return True

	# define evaluation methods for each apply class.

	def eval_attr12(self, attr_value, this):
		return True

		# define evaluation methods for each match association.

		# define evaluation methods for each apply association.


	def constraint(self, PreNode, graph):
		return True

