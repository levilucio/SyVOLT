from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HUnitR05a_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HUnitR05a_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HUnitR05a_CompleteLHS, self).__init__(name='HUnitR05a_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HUnitR05a_CompleteLHS')
		self["equations"] = []
		# Set the node attributes

		# match class State(5.0.m.0State) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__State"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'5.0.m.0State')

		# match class ExitPoint(5.0.m.1ExitPoint) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__ExitPoint"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'5.0.m.1ExitPoint')

		# apply class LocalDef(5.0.a.0LocalDef) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__LocalDef"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'5.0.a.0LocalDef')

		# apply class ProcDef(5.0.a.1ProcDef) node
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return True"""
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__ProcDef"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'5.0.a.1ProcDef')

		# apply class Name(5.0.a.2Name) node
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return True"""
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__Name"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'5.0.a.2Name')

		# apply class Par(5.0.a.3Par) node
		self.add_node()
		self.vs[5]["MT_pre__attr1"] = """return True"""
		self.vs[5]["MT_label__"] = """6"""
		self.vs[5]["mm__"] = """MT_pre__Par"""
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'5.0.a.3Par')

		# apply class Trigger(5.0.a.4Trigger) node
		self.add_node()
		self.vs[6]["MT_pre__attr1"] = """return True"""
		self.vs[6]["MT_label__"] = """7"""
		self.vs[6]["mm__"] = """MT_pre__Trigger"""
		self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'5.0.a.4Trigger')

		# match association State--exitPoints-->ExitPointnode
		self.add_node()
		self.vs[7]["MT_pre__attr1"] = """return attr_value == "exitPoints" """
		self.vs[7]["MT_label__"] = """8"""
		self.vs[7]["mm__"] = """MT_pre__directLink_S"""
		self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'5.0.m.0Stateassoc75.0.m.1ExitPoint')

		# apply association LocalDef--def-->ProcDefnode
		self.add_node()
		self.vs[8]["MT_pre__attr1"] = """return attr_value == "def" """
		self.vs[8]["MT_label__"] = """9"""
		self.vs[8]["mm__"] = """MT_pre__directLink_T"""
		self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'5.0.a.0LocalDefassoc85.0.a.1ProcDef')

		# apply association ProcDef--channelNames-->Namenode
		self.add_node()
		self.vs[9]["MT_pre__attr1"] = """return attr_value == "channelNames" """
		self.vs[9]["MT_label__"] = """10"""
		self.vs[9]["mm__"] = """MT_pre__directLink_T"""
		self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'5.0.a.1ProcDefassoc95.0.a.2Name')

		# apply association ProcDef--p-->Parnode
		self.add_node()
		self.vs[10]["MT_pre__attr1"] = """return attr_value == "p" """
		self.vs[10]["MT_label__"] = """11"""
		self.vs[10]["mm__"] = """MT_pre__directLink_T"""
		self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'5.0.a.1ProcDefassoc105.0.a.3Par')

		# apply association Par--p-->Triggernode
		self.add_node()
		self.vs[11]["MT_pre__attr1"] = """return attr_value == "p" """
		self.vs[11]["MT_label__"] = """12"""
		self.vs[11]["mm__"] = """MT_pre__directLink_T"""
		self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'5.0.a.3Parassoc115.0.a.4Trigger')

		# trace association LocalDef--trace-->Statenode
		self.add_node()
		self.vs[12]["MT_label__"] = """13"""
		self.vs[12]["mm__"] = """MT_pre__trace_link"""
		self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'5.0.a.0LocalDefassoc125.0.m.0State')

		self['equations'].append(((3,'name'),('concat',(('constant','B'),(1,'name')))))
		self['equations'].append(((4,'literal'),('constant','sh_in')))
		self['equations'].append(((6,'channel'),('constant','sh_in')))

		# Add the edges
		self.add_edges([
			(0,7), # match class State(5.0.m.0State) -> association exitPoints
			(7,1), # association ExitPoint -> match class ExitPoint(5.0.m.1ExitPoint)
			(2,8), # apply class LocalDef(5.0.a.0LocalDef) -> association def
			(8,3), # association ProcDef -> apply class ProcDef(5.0.a.1ProcDef)
			(3,9), # apply class ProcDef(5.0.a.1ProcDef) -> association channelNames
			(9,4), # association Name -> apply class Name(5.0.a.2Name)
			(3,10), # apply class ProcDef(5.0.a.1ProcDef) -> association p
			(10,5), # association Par -> apply class Par(5.0.a.3Par)
			(5,11), # apply class Par(5.0.a.3Par) -> association p
			(11,6), # association Trigger -> apply class Trigger(5.0.a.4Trigger)
			(2,12), # apply class LocalDef(5.0.m.0State) -> backward_association 
			(12,0), # backward_associationState -> match_class State(5.0.m.0State)
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

	def eval_attr15(self, attr_value, this):
		return True

	def eval_attr16(self, attr_value, this):
		return True

	def eval_attr17(self, attr_value, this):
		return True

		# define evaluation methods for each match association.

	def eval_attr18(self, attr_value, this):
		return attr_value == "exitPoints"
		# define evaluation methods for each apply association.

	def eval_attr19(self, attr_value, this):
		return attr_value == "def"
	def eval_attr110(self, attr_value, this):
		return attr_value == "channelNames"
	def eval_attr111(self, attr_value, this):
		return attr_value == "p"
	def eval_attr112(self, attr_value, this):
		return attr_value == "p"

	def constraint(self, PreNode, graph):
		return True

