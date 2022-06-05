from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HSS3_then2_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self, *args, **kwargs):
		"""
		Creates the himesis graph representing the AToM3 model HSS3_then2_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HSS3_then2_CompleteLHS, self).__init__(name='HSS3_then2_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HSS3_then2_CompleteLHS')
		self["equations"] = []
		# Set the node attributes

		# apply class Inst(0.42.a.0Inst) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__Inst"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.42.a.0Inst')

		# apply class Name(0.42.a.1Name) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__Name"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.42.a.1Name')

		# apply class Name(0.42.a.2Name) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__Name"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.42.a.2Name')

		# apply class Name(0.42.a.3Name) node
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return True"""
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__Name"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.42.a.3Name')

		# apply class Name(0.42.a.4Name) node
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return True"""
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__Name"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.42.a.4Name')

		# apply class ProcDef(0.42.a.5ProcDef) node
		self.add_node()
		self.vs[5]["MT_pre__attr1"] = """return True"""
		self.vs[5]["MT_label__"] = """6"""
		self.vs[5]["mm__"] = """MT_pre__ProcDef"""
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.42.a.5ProcDef')

		# apply association ProcDef--channelNames-->Namenode
		self.add_node()
		self.vs[6]["MT_pre__attr1"] = """return attr_value == "channelNames" """
		self.vs[6]["MT_label__"] = """7"""
		self.vs[6]["mm__"] = """MT_pre__directLink_T"""
		self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.42.a.5ProcDefassoc60.42.a.1Name')

		# apply association ProcDef--channelNames-->Namenode
		self.add_node()
		self.vs[7]["MT_pre__attr1"] = """return attr_value == "channelNames" """
		self.vs[7]["MT_label__"] = """8"""
		self.vs[7]["mm__"] = """MT_pre__directLink_T"""
		self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.42.a.5ProcDefassoc70.42.a.2Name')

		# apply association ProcDef--channelNames-->Namenode
		self.add_node()
		self.vs[8]["MT_pre__attr1"] = """return attr_value == "channelNames" """
		self.vs[8]["MT_label__"] = """9"""
		self.vs[8]["mm__"] = """MT_pre__directLink_T"""
		self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.42.a.5ProcDefassoc80.42.a.3Name')

		# apply association ProcDef--channelNames-->Namenode
		self.add_node()
		self.vs[9]["MT_pre__attr1"] = """return attr_value == "channelNames" """
		self.vs[9]["MT_label__"] = """10"""
		self.vs[9]["mm__"] = """MT_pre__directLink_T"""
		self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.42.a.5ProcDefassoc90.42.a.4Name')

		self['equations'].append(((0,'name'),('constant','Handler')))
		self['equations'].append(((5,'name'),('constant','Handler')))
		self["equations"].append(((0,'pivot'),('constant','Inst10faf3b1Inst')))


		# Add the edges
		self.add_edges([
			(5,6), # apply class ProcDef(0.42.a.5ProcDef) -> association channelNames
			(6,1), # association Name -> apply class Name(0.42.a.1Name)
			(5,7), # apply class ProcDef(0.42.a.5ProcDef) -> association channelNames
			(7,2), # association Name -> apply class Name(0.42.a.2Name)
			(5,8), # apply class ProcDef(0.42.a.5ProcDef) -> association channelNames
			(8,3), # association Name -> apply class Name(0.42.a.3Name)
			(5,9), # apply class ProcDef(0.42.a.5ProcDef) -> association channelNames
			(9,4), # association Name -> apply class Name(0.42.a.4Name)
		])


	# define evaluation methods for each match class.

	# define evaluation methods for each apply class.

	def eval_attr11(self, attr_value, this):
		return True

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

		# define evaluation methods for each match association.

		# define evaluation methods for each apply association.

	def eval_attr17(self, attr_value, this):
		return attr_value == "channelNames"
	def eval_attr18(self, attr_value, this):
		return attr_value == "channelNames"
	def eval_attr19(self, attr_value, this):
		return attr_value == "channelNames"
	def eval_attr110(self, attr_value, this):
		return attr_value == "channelNames"

	def constraint(self, PreNode, graph):
		return True

