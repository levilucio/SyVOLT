from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HUnitR04c_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HUnitR04c_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HUnitR04c_CompleteLHS, self).__init__(name='HUnitR04c_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HUnitR04c_CompleteLHS')
		self["equations"] = []
		# Set the node attributes

		# match class State(State) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__State"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'State')

		# apply class ProcDef(4.2.a.0ProcDef) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__ProcDef"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'4.2.a.0ProcDef')

		# apply class LocalDef(4.2.a.1LocalDef) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__LocalDef"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'4.2.a.1LocalDef')

		# apply class Name(4.2.a.2Name) node
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return True"""
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__Name"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'4.2.a.2Name')

		# apply class New(4.2.a.3New) node
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return True"""
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__New"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'4.2.a.3New')

		# apply class Name(4.2.a.4Name) node
		self.add_node()
		self.vs[5]["MT_pre__attr1"] = """return True"""
		self.vs[5]["MT_label__"] = """6"""
		self.vs[5]["mm__"] = """MT_pre__Name"""
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'4.2.a.4Name')

		# apply class Name(4.2.a.5Name) node
		self.add_node()
		self.vs[6]["MT_pre__attr1"] = """return True"""
		self.vs[6]["MT_label__"] = """7"""
		self.vs[6]["mm__"] = """MT_pre__Name"""
		self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'4.2.a.5Name')

		# apply class Name(4.2.a.6Name) node
		self.add_node()
		self.vs[7]["MT_pre__attr1"] = """return True"""
		self.vs[7]["MT_label__"] = """8"""
		self.vs[7]["mm__"] = """MT_pre__Name"""
		self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'4.2.a.6Name')

		# apply class Par(4.2.a.7Par) node
		self.add_node()
		self.vs[8]["MT_pre__attr1"] = """return True"""
		self.vs[8]["MT_label__"] = """9"""
		self.vs[8]["mm__"] = """MT_pre__Par"""
		self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'4.2.a.7Par')

		# apply class Inst(4.2.a.8Inst) node
		self.add_node()
		self.vs[9]["MT_pre__attr1"] = """return True"""
		self.vs[9]["MT_label__"] = """10"""
		self.vs[9]["mm__"] = """MT_pre__Inst"""
		self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'4.2.a.8Inst')

		# apply class Inst(4.2.a.9Inst) node
		self.add_node()
		self.vs[10]["MT_pre__attr1"] = """return True"""
		self.vs[10]["MT_label__"] = """11"""
		self.vs[10]["mm__"] = """MT_pre__Inst"""
		self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'4.2.a.9Inst')

		# apply class Name(4.2.a.10Name) node
		self.add_node()
		self.vs[11]["MT_pre__attr1"] = """return True"""
		self.vs[11]["MT_label__"] = """12"""
		self.vs[11]["mm__"] = """MT_pre__Name"""
		self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'4.2.a.10Name')

		# apply class Name(4.2.a.11Name) node
		self.add_node()
		self.vs[12]["MT_pre__attr1"] = """return True"""
		self.vs[12]["MT_label__"] = """13"""
		self.vs[12]["mm__"] = """MT_pre__Name"""
		self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'4.2.a.11Name')

		# apply class Name(4.2.a.12Name) node
		self.add_node()
		self.vs[13]["MT_pre__attr1"] = """return True"""
		self.vs[13]["MT_label__"] = """14"""
		self.vs[13]["mm__"] = """MT_pre__Name"""
		self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'4.2.a.12Name')

		# apply class Name(4.2.a.13Name) node
		self.add_node()
		self.vs[14]["MT_pre__attr1"] = """return True"""
		self.vs[14]["MT_label__"] = """15"""
		self.vs[14]["mm__"] = """MT_pre__Name"""
		self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'4.2.a.13Name')

		# apply class Name(4.2.a.14Name) node
		self.add_node()
		self.vs[15]["MT_pre__attr1"] = """return True"""
		self.vs[15]["MT_label__"] = """16"""
		self.vs[15]["mm__"] = """MT_pre__Name"""
		self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'4.2.a.14Name')

		# apply class Name(4.2.a.15Name) node
		self.add_node()
		self.vs[16]["MT_pre__attr1"] = """return True"""
		self.vs[16]["MT_label__"] = """17"""
		self.vs[16]["mm__"] = """MT_pre__Name"""
		self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'4.2.a.15Name')

		# apply class Name(4.2.a.16Name) node
		self.add_node()
		self.vs[17]["MT_pre__attr1"] = """return True"""
		self.vs[17]["MT_label__"] = """18"""
		self.vs[17]["mm__"] = """MT_pre__Name"""
		self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'4.2.a.16Name')

		# apply association ProcDef--p-->LocalDefnode
		self.add_node()
		self.vs[18]["MT_pre__attr1"] = """return attr_value == "p" """
		self.vs[18]["MT_label__"] = """19"""
		self.vs[18]["mm__"] = """MT_pre__directLink_T"""
		self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'4.2.a.0ProcDefassoc184.2.a.1LocalDef')

		# apply association ProcDef--channelNames-->Namenode
		self.add_node()
		self.vs[19]["MT_pre__attr1"] = """return attr_value == "channelNames" """
		self.vs[19]["MT_label__"] = """20"""
		self.vs[19]["mm__"] = """MT_pre__directLink_T"""
		self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'4.2.a.0ProcDefassoc194.2.a.2Name')

		# apply association LocalDef--p-->Newnode
		self.add_node()
		self.vs[20]["MT_pre__attr1"] = """return attr_value == "p" """
		self.vs[20]["MT_label__"] = """21"""
		self.vs[20]["mm__"] = """MT_pre__directLink_T"""
		self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'4.2.a.1LocalDefassoc204.2.a.3New')

		# apply association New--channelNames-->Namenode
		self.add_node()
		self.vs[21]["MT_pre__attr1"] = """return attr_value == "channelNames" """
		self.vs[21]["MT_label__"] = """22"""
		self.vs[21]["mm__"] = """MT_pre__directLink_T"""
		self.vs[21]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'4.2.a.3Newassoc214.2.a.4Name')

		# apply association New--channelNames-->Namenode
		self.add_node()
		self.vs[22]["MT_pre__attr1"] = """return attr_value == "channelNames" """
		self.vs[22]["MT_label__"] = """23"""
		self.vs[22]["mm__"] = """MT_pre__directLink_T"""
		self.vs[22]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'4.2.a.3Newassoc224.2.a.5Name')

		# apply association New--channelNames-->Namenode
		self.add_node()
		self.vs[23]["MT_pre__attr1"] = """return attr_value == "channelNames" """
		self.vs[23]["MT_label__"] = """24"""
		self.vs[23]["mm__"] = """MT_pre__directLink_T"""
		self.vs[23]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'4.2.a.3Newassoc234.2.a.6Name')

		# apply association New--p-->Parnode
		self.add_node()
		self.vs[24]["MT_pre__attr1"] = """return attr_value == "p" """
		self.vs[24]["MT_label__"] = """25"""
		self.vs[24]["mm__"] = """MT_pre__directLink_T"""
		self.vs[24]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'4.2.a.3Newassoc244.2.a.7Par')

		# apply association Par--p-->Instnode
		self.add_node()
		self.vs[25]["MT_pre__attr1"] = """return attr_value == "p" """
		self.vs[25]["MT_label__"] = """26"""
		self.vs[25]["mm__"] = """MT_pre__directLink_T"""
		self.vs[25]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'4.2.a.7Parassoc254.2.a.9Inst')

		# apply association Par--p-->Instnode
		self.add_node()
		self.vs[26]["MT_pre__attr1"] = """return attr_value == "p" """
		self.vs[26]["MT_label__"] = """27"""
		self.vs[26]["mm__"] = """MT_pre__directLink_T"""
		self.vs[26]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'4.2.a.7Parassoc264.2.a.8Inst')

		# apply association Inst--channelNames-->Namenode
		self.add_node()
		self.vs[27]["MT_pre__attr1"] = """return attr_value == "channelNames" """
		self.vs[27]["MT_label__"] = """28"""
		self.vs[27]["mm__"] = """MT_pre__directLink_T"""
		self.vs[27]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'4.2.a.8Instassoc274.2.a.10Name')

		# apply association Inst--channelNames-->Namenode
		self.add_node()
		self.vs[28]["MT_pre__attr1"] = """return attr_value == "channelNames" """
		self.vs[28]["MT_label__"] = """29"""
		self.vs[28]["mm__"] = """MT_pre__directLink_T"""
		self.vs[28]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'4.2.a.8Instassoc284.2.a.11Name')

		# apply association Inst--channelNames-->Namenode
		self.add_node()
		self.vs[29]["MT_pre__attr1"] = """return attr_value == "channelNames" """
		self.vs[29]["MT_label__"] = """30"""
		self.vs[29]["mm__"] = """MT_pre__directLink_T"""
		self.vs[29]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'4.2.a.8Instassoc294.2.a.12Name')

		# apply association Inst--channelNames-->Namenode
		self.add_node()
		self.vs[30]["MT_pre__attr1"] = """return attr_value == "channelNames" """
		self.vs[30]["MT_label__"] = """31"""
		self.vs[30]["mm__"] = """MT_pre__directLink_T"""
		self.vs[30]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'4.2.a.8Instassoc304.2.a.13Name')

		# apply association Inst--channelNames-->Namenode
		self.add_node()
		self.vs[31]["MT_pre__attr1"] = """return attr_value == "channelNames" """
		self.vs[31]["MT_label__"] = """32"""
		self.vs[31]["mm__"] = """MT_pre__directLink_T"""
		self.vs[31]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'4.2.a.9Instassoc314.2.a.14Name')

		# apply association Inst--channelNames-->Namenode
		self.add_node()
		self.vs[32]["MT_pre__attr1"] = """return attr_value == "channelNames" """
		self.vs[32]["MT_label__"] = """33"""
		self.vs[32]["mm__"] = """MT_pre__directLink_T"""
		self.vs[32]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'4.2.a.9Instassoc324.2.a.15Name')

		# apply association Inst--channelNames-->Namenode
		self.add_node()
		self.vs[33]["MT_pre__attr1"] = """return attr_value == "channelNames" """
		self.vs[33]["MT_label__"] = """34"""
		self.vs[33]["mm__"] = """MT_pre__directLink_T"""
		self.vs[33]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'4.2.a.9Instassoc334.2.a.16Name')

		# trace association ProcDef--trace-->nullnode
		self.add_node()
		self.vs[34]["MT_label__"] = """35"""
		self.vs[34]["mm__"] = """MT_pre__trace_link"""
		self.vs[34]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'4.2.a.0ProcDefassoc34State')

		self['equations'].append(((3,'literal'),('constant','sh')))
		self['equations'].append(((5,'literal'),('constant','exit_in')))
		self['equations'].append(((6,'literal'),('constant','exack_in')))
		self['equations'].append(((7,'literal'),('constant','sh_in')))
		self['equations'].append(((9,'name'),('constant','C')))
		self['equations'].append(((10,'name'),('constant','H')))
		self['equations'].append(((11,'literal'),('constant','enp')))
		self['equations'].append(((12,'literal'),('constant','exit_in')))
		self['equations'].append(((13,'literal'),('constant','exack_in')))
		self['equations'].append(((14,'literal'),('constant','sh_in')))
		self['equations'].append(((15,'literal'),('constant','exit_in')))
		self['equations'].append(((16,'literal'),('constant','exack_in')))
		self['equations'].append(((17,'literal'),('constant','sh_in')))

		# Add the edges
		self.add_edges([
			(1,18), # apply class ProcDef(4.2.a.0ProcDef) -> association p
			(18,2), # association LocalDef -> apply class LocalDef(4.2.a.1LocalDef)
			(1,19), # apply class ProcDef(4.2.a.0ProcDef) -> association channelNames
			(19,3), # association Name -> apply class Name(4.2.a.2Name)
			(2,20), # apply class LocalDef(4.2.a.1LocalDef) -> association p
			(20,4), # association New -> apply class New(4.2.a.3New)
			(4,21), # apply class New(4.2.a.3New) -> association channelNames
			(21,5), # association Name -> apply class Name(4.2.a.4Name)
			(4,22), # apply class New(4.2.a.3New) -> association channelNames
			(22,6), # association Name -> apply class Name(4.2.a.5Name)
			(4,23), # apply class New(4.2.a.3New) -> association channelNames
			(23,7), # association Name -> apply class Name(4.2.a.6Name)
			(4,24), # apply class New(4.2.a.3New) -> association p
			(24,8), # association Par -> apply class Par(4.2.a.7Par)
			(8,25), # apply class Par(4.2.a.7Par) -> association p
			(25,10), # association Inst -> apply class Inst(4.2.a.9Inst)
			(8,26), # apply class Par(4.2.a.7Par) -> association p
			(26,9), # association Inst -> apply class Inst(4.2.a.8Inst)
			(9,27), # apply class Inst(4.2.a.8Inst) -> association channelNames
			(27,11), # association Name -> apply class Name(4.2.a.10Name)
			(9,28), # apply class Inst(4.2.a.8Inst) -> association channelNames
			(28,12), # association Name -> apply class Name(4.2.a.11Name)
			(9,29), # apply class Inst(4.2.a.8Inst) -> association channelNames
			(29,13), # association Name -> apply class Name(4.2.a.12Name)
			(9,30), # apply class Inst(4.2.a.8Inst) -> association channelNames
			(30,14), # association Name -> apply class Name(4.2.a.13Name)
			(10,31), # apply class Inst(4.2.a.9Inst) -> association channelNames
			(31,15), # association Name -> apply class Name(4.2.a.14Name)
			(10,32), # apply class Inst(4.2.a.9Inst) -> association channelNames
			(32,16), # association Name -> apply class Name(4.2.a.15Name)
			(10,33), # apply class Inst(4.2.a.9Inst) -> association channelNames
			(33,17), # association Name -> apply class Name(4.2.a.16Name)
			(1,34), # apply class ProcDef(State) -> backward_association 
			(34,0), # backward_associationnull -> match_class null(State)
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

	def eval_attr16(self, attr_value, this):
		return True

	def eval_attr17(self, attr_value, this):
		return True

	def eval_attr18(self, attr_value, this):
		return True

	def eval_attr19(self, attr_value, this):
		return True

	def eval_attr110(self, attr_value, this):
		return True

	def eval_attr111(self, attr_value, this):
		return True

	def eval_attr112(self, attr_value, this):
		return True

	def eval_attr113(self, attr_value, this):
		return True

	def eval_attr114(self, attr_value, this):
		return True

	def eval_attr115(self, attr_value, this):
		return True

	def eval_attr116(self, attr_value, this):
		return True

	def eval_attr117(self, attr_value, this):
		return True

	def eval_attr118(self, attr_value, this):
		return True

		# define evaluation methods for each match association.

		# define evaluation methods for each apply association.

	def eval_attr119(self, attr_value, this):
		return attr_value == "p"
	def eval_attr120(self, attr_value, this):
		return attr_value == "channelNames"
	def eval_attr121(self, attr_value, this):
		return attr_value == "p"
	def eval_attr122(self, attr_value, this):
		return attr_value == "channelNames"
	def eval_attr123(self, attr_value, this):
		return attr_value == "channelNames"
	def eval_attr124(self, attr_value, this):
		return attr_value == "channelNames"
	def eval_attr125(self, attr_value, this):
		return attr_value == "p"
	def eval_attr126(self, attr_value, this):
		return attr_value == "p"
	def eval_attr127(self, attr_value, this):
		return attr_value == "p"
	def eval_attr128(self, attr_value, this):
		return attr_value == "channelNames"
	def eval_attr129(self, attr_value, this):
		return attr_value == "channelNames"
	def eval_attr130(self, attr_value, this):
		return attr_value == "channelNames"
	def eval_attr131(self, attr_value, this):
		return attr_value == "channelNames"
	def eval_attr132(self, attr_value, this):
		return attr_value == "channelNames"
	def eval_attr133(self, attr_value, this):
		return attr_value == "channelNames"
	def eval_attr134(self, attr_value, this):
		return attr_value == "channelNames"

	def constraint(self, PreNode, graph):
		return True

