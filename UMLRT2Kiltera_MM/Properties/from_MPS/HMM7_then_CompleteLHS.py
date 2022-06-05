from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HMM7_then_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self, *args, **kwargs):
		"""
		Creates the himesis graph representing the AToM3 model HMM7_then_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HMM7_then_CompleteLHS, self).__init__(name='HMM7_then_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HMM7_then_CompleteLHS')
		self["equations"] = []
		# Set the node attributes

		# apply class LocalDef(0.23.a.0LocalDef) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__LocalDef"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.23.a.0LocalDef')

		# apply class Def(0.23.a.1Def) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__Def"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.23.a.1Def')

		# apply association LocalDef--def-->Defnode
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return attr_value == "def" """
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__directLink_T"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.23.a.0LocalDefassoc20.23.a.1Def')

		self["equations"].append(((0,'pivot'),('constant','LocalDef42013119LocalDef')))


		# Add the edges
		self.add_edges([
			(0,2), # apply class LocalDef(0.23.a.0LocalDef) -> association def
			(2,1), # association Def -> apply class Def(0.23.a.1Def)
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
		return attr_value == "def"

	def constraint(self, PreNode, graph):
		return True

