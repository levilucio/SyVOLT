from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HUnitR04b_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HUnitR04b_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HUnitR04b_CompleteLHS, self).__init__(name='HUnitR04b_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HUnitR04b_CompleteLHS')
		self["equations"] = []
		# Set the node attributes

		# match class State(State) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__State"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'State')

		# apply class Listen(Listen) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__Listen"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Listen')

		# apply class ProcDef(ProcDef) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__ProcDef"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ProcDef')

		# apply class ListenBranch(ListenBranch) node
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return True"""
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__ListenBranch"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ListenBranch')

		# apply class Trigger(Trigger) node
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return True"""
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__Trigger"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Trigger')

		# apply association null--p-->nullnode
		self.add_node()
		self.vs[5]["MT_pre__attr1"] = """return attr_value == "p" """
		self.vs[5]["MT_label__"] = """6"""
		self.vs[5]["mm__"] = """MT_pre__directLink_T"""
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ProcDefassoc5Listen')

		# apply association null--branches-->nullnode
		self.add_node()
		self.vs[6]["MT_pre__attr1"] = """return attr_value == "branches" """
		self.vs[6]["MT_label__"] = """7"""
		self.vs[6]["mm__"] = """MT_pre__directLink_T"""
		self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Listenassoc6ListenBranch')

		# apply association null--p-->nullnode
		self.add_node()
		self.vs[7]["MT_pre__attr1"] = """return attr_value == "p" """
		self.vs[7]["MT_label__"] = """8"""
		self.vs[7]["mm__"] = """MT_pre__directLink_T"""
		self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ListenBranchassoc7Trigger')

		# trace association null--trace-->nullnode
		self.add_node()
		self.vs[8]["MT_label__"] = """9"""
		self.vs[8]["mm__"] = """MT_pre__trace_link"""
		self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ProcDefassoc8State')

		self['equations'].append(((3,'channel'),('constant','exit')))
		self['equations'].append(((4,'channel'),('constant','exack')))

		# Add the edges
		self.add_edges([
			(2,5), # apply class null(ProcDef) -> association p
			(5,1), # association null -> apply class null(Listen)
			(1,6), # apply class null(Listen) -> association branches
			(6,3), # association null -> apply class null(ListenBranch)
			(3,7), # apply class null(ListenBranch) -> association p
			(7,4), # association null -> apply class null(Trigger)
			(2,8), # apply class null(State) -> backward_association 
			(8,0), # backward_associationnull -> match_class null(State)
		])


	# define evaluation methods for each match class.

	def eval_attr11(self, attr_value, this):
		return True

	# define evaluation methods for each apply class.

	def eval_attr12(self, attr_value, this):
		return True

	def eval_attr13(self, attr_value, this):
		return True

	def eval_attr14(self, attr_value, this):
		return True

	def eval_attr15(self, attr_value, this):
		return True

		# define evaluation methods for each match association.

		# define evaluation methods for each apply association.

	def eval_attr16(self, attr_value, this):
		return attr_value == "p"
	def eval_attr17(self, attr_value, this):
		return attr_value == "branches"
	def eval_attr18(self, attr_value, this):
		return attr_value == "p"

	def constraint(self, PreNode, graph):
		return True

