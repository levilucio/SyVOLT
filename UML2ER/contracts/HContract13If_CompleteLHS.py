from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HContract13If_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self, *args, **kwargs):
		"""
		Creates the himesis graph representing the AToM3 model HContract13If_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HContract13If_CompleteLHS, self).__init__(name='HContract13If_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HContract13If_CompleteLHS')
		self["equations"] = []
		# Set the node attributes

		# apply class EntityType(EntityType) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__EntityType"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EntityType')

		# apply class WeakReference(WeakReference) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__WeakReference"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'WeakReference')

		# apply association null--type-->nullnode
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return attr_value == "type" """
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__directLink_T"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'WeakReferenceassoc2EntityType')

		self["equations"].append(((1,'pivot'),('constant','WeakReferencea56b1c24WeakReference')))


		# Add the edges
		self.add_edges([
			(1,2), # apply class null(WeakReference) -> association type
			(2,0), # association null -> apply class null(EntityType)
		])


	# define evaluation methods for each match class.

	# define evaluation methods for each apply class.

	def eval_attr11(self, attr_value, this):
		return True

	def eval_attr12(self, attr_value, this):
		return True

		# define evaluation methods for each match association.

		# define evaluation methods for each apply association.

	def eval_attr13(self, attr_value, this):
		return attr_value == "type"

	def constraint(self, PreNode, graph):
		return True

