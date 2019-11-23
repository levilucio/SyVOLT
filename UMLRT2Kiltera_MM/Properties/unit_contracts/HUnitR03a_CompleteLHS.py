from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HUnitR03a_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HUnitR03a_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HUnitR03a_CompleteLHS, self).__init__(name='HUnitR03a_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HUnitR03a_CompleteLHS')
		self["equations"] = []
		# Set the node attributes

		# match class RootElement(RootElement) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__RootElement"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'RootElement')

		# match class TopLevelElement(TopLevelElement) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__TopLevelElement"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'TopLevelElement')

		# apply class RootElement(RootElement) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__RootElement"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'RootElement')

		# apply class TopLevelElement(TopLevelStatement) node
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return True"""
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__TopLevelElement"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'TopLevelStatement')

		# match association null--contains-->nullnode
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return attr_value == "contains" """
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__directLink_S"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'RootElementassoc4TopLevelElement')

		# apply association null--contains-->nullnode
		self.add_node()
		self.vs[5]["MT_pre__attr1"] = """return attr_value == "contains" """
		self.vs[5]["MT_label__"] = """6"""
		self.vs[5]["mm__"] = """MT_pre__directLink_T"""
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'RootElementassoc5TopLevelStatement')

		# trace association null--trace-->nullnode
		self.add_node()
		self.vs[6]["MT_label__"] = """7"""
		self.vs[6]["mm__"] = """MT_pre__trace_link"""
		self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'RootElementassoc6RootElement')

		# trace association null--trace-->nullnode
		self.add_node()
		self.vs[7]["MT_label__"] = """8"""
		self.vs[7]["mm__"] = """MT_pre__trace_link"""
		self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'TopLevelStatementassoc7TopLevelElement')


		# Add the edges
		self.add_edges([
			(0,4), # match class null(RootElement) -> association contains
			(4,1), # association null -> match class null(TopLevelElement)
			(2,5), # apply class null(RootElement) -> association contains
			(5,3), # association null -> apply class null(TopLevelStatement)
			(2,6), # apply class null(RootElement) -> backward_association 
			(6,0), # backward_associationnull -> match_class null(RootElement)
			(3,7), # apply class null(TopLevelElement) -> backward_association 
			(7,1), # backward_associationnull -> match_class null(TopLevelElement)
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
		return attr_value == "contains"
		# define evaluation methods for each apply association.

	def eval_attr16(self, attr_value, this):
		return attr_value == "contains"

	def constraint(self, PreNode, graph):
		return True

