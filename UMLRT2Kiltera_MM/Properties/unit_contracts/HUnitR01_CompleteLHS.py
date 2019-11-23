from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HUnitR01_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HUnitR01_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HUnitR01_CompleteLHS, self).__init__(name='HUnitR01_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HUnitR01_CompleteLHS')
		self["equations"] = []
		# Set the node attributes

		# match class State(State) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__State"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'State')

		# apply class ProcDef(ProcDef) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__ProcDef"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ProcDef')

		# apply class Name(Name1) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__Name"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Name1')

		# apply class Name(Name2) node
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return True"""
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__Name"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Name2')

		# apply class Name(Name3) node
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return True"""
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__Name"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Name3')

		# apply association null--channelNames-->nullnode
		self.add_node()
		self.vs[5]["MT_pre__attr1"] = """return attr_value == "channelNames" """
		self.vs[5]["MT_label__"] = """6"""
		self.vs[5]["mm__"] = """MT_pre__directLink_T"""
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ProcDefassoc5Name1')

		# apply association null--channelNames-->nullnode
		self.add_node()
		self.vs[6]["MT_pre__attr1"] = """return attr_value == "channelNames" """
		self.vs[6]["MT_label__"] = """7"""
		self.vs[6]["mm__"] = """MT_pre__directLink_T"""
		self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ProcDefassoc6Name2')

		# apply association null--channelNames-->nullnode
		self.add_node()
		self.vs[7]["MT_pre__attr1"] = """return attr_value == "channelNames" """
		self.vs[7]["MT_label__"] = """8"""
		self.vs[7]["mm__"] = """MT_pre__directLink_T"""
		self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ProcDefassoc7Name3')

		self['equations'].append(((1,'name'),('concat',(('constant','S'),(0,'name')))))
		self['equations'].append(((2,'literal'),('constant','exit')))
		self['equations'].append(((3,'literal'),('constant','exack')))
		self['equations'].append(((4,'literal'),('constant','enp')))

		# Add the edges
		self.add_edges([
			(1,5), # apply class null(ProcDef) -> association channelNames
			(5,2), # association null -> apply class null(Name1)
			(1,6), # apply class null(ProcDef) -> association channelNames
			(6,3), # association null -> apply class null(Name2)
			(1,7), # apply class null(ProcDef) -> association channelNames
			(7,4), # association null -> apply class null(Name3)
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
		return attr_value == "channelNames"
	def eval_attr17(self, attr_value, this):
		return attr_value == "channelNames"
	def eval_attr18(self, attr_value, this):
		return attr_value == "channelNames"

	def constraint(self, PreNode, graph):
		return True

