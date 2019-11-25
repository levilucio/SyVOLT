from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HUnitR01a_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HUnitR01a_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HUnitR01a_CompleteLHS, self).__init__(name='HUnitR01a_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HUnitR01a_CompleteLHS')
		self["equations"] = []
		# Set the node attributes

		# match class PhysicalNode(1.0.m.0PhysicalNode) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__PhysicalNode"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'1.0.m.0PhysicalNode')

		# match class Partition(1.0.m.1Partition) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__Partition"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'1.0.m.1Partition')

		# match class Module(1.0.m.2Module) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__Module"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'1.0.m.2Module')

		# apply class SystemMapping(1.0.a.0SystemMapping) node
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return True"""
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__SystemMapping"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'1.0.a.0SystemMapping')

		# apply class System(1.0.a.1System) node
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return True"""
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__System"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'1.0.a.1System')

		# apply class SoftwareComposition(1.0.a.2SoftwareComposition) node
		self.add_node()
		self.vs[5]["MT_pre__attr1"] = """return True"""
		self.vs[5]["MT_label__"] = """6"""
		self.vs[5]["mm__"] = """MT_pre__SoftwareComposition"""
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'1.0.a.2SoftwareComposition')

		# apply class CompositionType(1.0.a.3CompositionType) node
		self.add_node()
		self.vs[6]["MT_pre__attr1"] = """return True"""
		self.vs[6]["MT_label__"] = """7"""
		self.vs[6]["mm__"] = """MT_pre__CompositionType"""
		self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'1.0.a.3CompositionType')

		# apply class EcuInstance(1.0.a.4EcuInstance) node
		self.add_node()
		self.vs[7]["MT_pre__attr1"] = """return True"""
		self.vs[7]["MT_label__"] = """8"""
		self.vs[7]["mm__"] = """MT_pre__EcuInstance"""
		self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'1.0.a.4EcuInstance')

		# match association PhysicalNode--partition-->Partitionnode
		self.add_node()
		self.vs[8]["MT_pre__attr1"] = """return attr_value == "partition" """
		self.vs[8]["MT_label__"] = """9"""
		self.vs[8]["mm__"] = """MT_pre__directLink_S"""
		self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'1.0.m.0PhysicalNodeassoc81.0.m.1Partition')

		# match association Partition--module-->Modulenode
		self.add_node()
		self.vs[9]["MT_pre__attr1"] = """return attr_value == "module" """
		self.vs[9]["MT_label__"] = """10"""
		self.vs[9]["mm__"] = """MT_pre__directLink_S"""
		self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'1.0.m.1Partitionassoc91.0.m.2Module')

		# apply association System--mapping-->SystemMappingnode
		self.add_node()
		self.vs[10]["MT_pre__attr1"] = """return attr_value == "mapping" """
		self.vs[10]["MT_label__"] = """11"""
		self.vs[10]["mm__"] = """MT_pre__directLink_T"""
		self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'1.0.a.1Systemassoc101.0.a.0SystemMapping')

		# apply association System--softwareComposition-->SoftwareCompositionnode
		self.add_node()
		self.vs[11]["MT_pre__attr1"] = """return attr_value == "softwareComposition" """
		self.vs[11]["MT_label__"] = """12"""
		self.vs[11]["mm__"] = """MT_pre__directLink_T"""
		self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'1.0.a.1Systemassoc111.0.a.2SoftwareComposition')

		# apply association SoftwareComposition--softwareComposition-->CompositionTypenode
		self.add_node()
		self.vs[12]["MT_pre__attr1"] = """return attr_value == "softwareComposition" """
		self.vs[12]["MT_label__"] = """13"""
		self.vs[12]["mm__"] = """MT_pre__directLink_T"""
		self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'1.0.a.2SoftwareCompositionassoc121.0.a.3CompositionType')

		self['equations'].append(((3,'shortName'),('concat',(('constant','SysMapping_'),(0,'name')))))
		self['equations'].append(((4,'shortName'),('concat',(('constant','SysTemplate_'),(0,'name')))))
		self['equations'].append(((5,'shortName'),('concat',(('constant','SoftwareComposition_'),(0,'name')))))
		self['equations'].append(((6,'shortName'),('concat',(('constant','CompositionType_'),(0,'name')))))
		self['equations'].append(((7,'shortName'),('concat',(('constant','EcuInstance_'),(0,'name')))))

		# Add the edges
		self.add_edges([
			(0,8), # match class PhysicalNode(1.0.m.0PhysicalNode) -> association partition
			(8,1), # association Partition -> match class Partition(1.0.m.1Partition)
			(1,9), # match class Partition(1.0.m.1Partition) -> association module
			(9,2), # association Module -> match class Module(1.0.m.2Module)
			(4,10), # apply class System(1.0.a.1System) -> association mapping
			(10,3), # association SystemMapping -> apply class SystemMapping(1.0.a.0SystemMapping)
			(4,11), # apply class System(1.0.a.1System) -> association softwareComposition
			(11,5), # association SoftwareComposition -> apply class SoftwareComposition(1.0.a.2SoftwareComposition)
			(5,12), # apply class SoftwareComposition(1.0.a.2SoftwareComposition) -> association softwareComposition
			(12,6), # association CompositionType -> apply class CompositionType(1.0.a.3CompositionType)
		])


	# define evaluation methods for each match class.

	def eval_attr11(self, attr_value, this):
		return True

	def eval_attr12(self, attr_value, this):
		return True

	def eval_attr13(self, attr_value, this):
		return True

	# define evaluation methods for each apply class.

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

		# define evaluation methods for each match association.

	def eval_attr19(self, attr_value, this):
		return attr_value == "partition"
	def eval_attr110(self, attr_value, this):
		return attr_value == "module"
		# define evaluation methods for each apply association.

	def eval_attr111(self, attr_value, this):
		return attr_value == "mapping"
	def eval_attr112(self, attr_value, this):
		return attr_value == "softwareComposition"
	def eval_attr113(self, attr_value, this):
		return attr_value == "softwareComposition"

	def constraint(self, PreNode, graph):
		return True

