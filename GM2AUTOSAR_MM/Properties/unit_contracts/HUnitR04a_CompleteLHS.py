from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HUnitR04a_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HUnitR04a_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HUnitR04a_CompleteLHS, self).__init__(name='HUnitR04a_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HUnitR04a_CompleteLHS')
		self["equations"] = []
		# Set the node attributes

		# match class PhysicalNode(4.0.m.0PhysicalNode) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__PhysicalNode"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'4.0.m.0PhysicalNode')

		# match class Partition(4.0.m.1Partition) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__Partition"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'4.0.m.1Partition')

		# match class Module(4.0.m.2Module) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__Module"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'4.0.m.2Module')

		# match class Scheduler(4.0.m.3Scheduler) node
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return True"""
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__Scheduler"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'4.0.m.3Scheduler')

		# match class Service(4.0.m.4Service) node
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return True"""
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__Service"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'4.0.m.4Service')

		# apply class CompositionType(4.0.a.0CompositionType) node
		self.add_node()
		self.vs[5]["MT_pre__attr1"] = """return True"""
		self.vs[5]["MT_label__"] = """6"""
		self.vs[5]["mm__"] = """MT_pre__CompositionType"""
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'4.0.a.0CompositionType')

		# apply class PPortPrototype(4.0.a.1PPortPrototype) node
		self.add_node()
		self.vs[6]["MT_pre__attr1"] = """return True"""
		self.vs[6]["MT_label__"] = """7"""
		self.vs[6]["mm__"] = """MT_pre__PPortPrototype"""
		self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'4.0.a.1PPortPrototype')

		# match association PhysicalNode--partition-->Partitionnode
		self.add_node()
		self.vs[7]["MT_pre__attr1"] = """return attr_value == "partition" """
		self.vs[7]["MT_label__"] = """8"""
		self.vs[7]["mm__"] = """MT_pre__directLink_S"""
		self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'4.0.m.0PhysicalNodeassoc74.0.m.1Partition')

		# match association Partition--module-->Modulenode
		self.add_node()
		self.vs[8]["MT_pre__attr1"] = """return attr_value == "module" """
		self.vs[8]["MT_label__"] = """9"""
		self.vs[8]["mm__"] = """MT_pre__directLink_S"""
		self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'4.0.m.1Partitionassoc84.0.m.2Module')

		# match association Module--scheduler-->Schedulernode
		self.add_node()
		self.vs[9]["MT_pre__attr1"] = """return attr_value == "scheduler" """
		self.vs[9]["MT_label__"] = """10"""
		self.vs[9]["mm__"] = """MT_pre__directLink_S"""
		self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'4.0.m.2Moduleassoc94.0.m.3Scheduler')

		# match association Scheduler--provided-->Servicenode
		self.add_node()
		self.vs[10]["MT_pre__attr1"] = """return attr_value == "provided" """
		self.vs[10]["MT_label__"] = """11"""
		self.vs[10]["mm__"] = """MT_pre__directLink_S"""
		self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'4.0.m.3Schedulerassoc104.0.m.4Service')

		# apply association CompositionType--port-->PPortPrototypenode
		self.add_node()
		self.vs[11]["MT_pre__attr1"] = """return attr_value == "port" """
		self.vs[11]["MT_label__"] = """12"""
		self.vs[11]["mm__"] = """MT_pre__directLink_T"""
		self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'4.0.a.0CompositionTypeassoc114.0.a.1PPortPrototype')

		# trace association CompositionType--trace-->PhysicalNodenode
		self.add_node()
		self.vs[12]["MT_label__"] = """13"""
		self.vs[12]["mm__"] = """MT_pre__trace_link"""
		self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'4.0.a.0CompositionTypeassoc124.0.m.0PhysicalNode')

		self['equations'].append(((6,'shortName'),('concat',((3,'name'),('constant','PROV')))))

		# Add the edges
		self.add_edges([
			(0,7), # match class PhysicalNode(4.0.m.0PhysicalNode) -> association partition
			(7,1), # association Partition -> match class Partition(4.0.m.1Partition)
			(1,8), # match class Partition(4.0.m.1Partition) -> association module
			(8,2), # association Module -> match class Module(4.0.m.2Module)
			(2,9), # match class Module(4.0.m.2Module) -> association scheduler
			(9,3), # association Scheduler -> match class Scheduler(4.0.m.3Scheduler)
			(3,10), # match class Scheduler(4.0.m.3Scheduler) -> association provided
			(10,4), # association Service -> match class Service(4.0.m.4Service)
			(5,11), # apply class CompositionType(4.0.a.0CompositionType) -> association port
			(11,6), # association PPortPrototype -> apply class PPortPrototype(4.0.a.1PPortPrototype)
			(5,12), # apply class CompositionType(4.0.m.0PhysicalNode) -> backward_association 
			(12,0), # backward_associationPhysicalNode -> match_class PhysicalNode(4.0.m.0PhysicalNode)
		])


	# define evaluation methods for each match class.

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

	# define evaluation methods for each apply class.

	def eval_attr16(self, attr_value, this):
		return True

	def eval_attr17(self, attr_value, this):
		return True

		# define evaluation methods for each match association.

	def eval_attr18(self, attr_value, this):
		return attr_value == "partition"
	def eval_attr19(self, attr_value, this):
		return attr_value == "module"
	def eval_attr110(self, attr_value, this):
		return attr_value == "scheduler"
	def eval_attr111(self, attr_value, this):
		return attr_value == "provided"
		# define evaluation methods for each apply association.

	def eval_attr112(self, attr_value, this):
		return attr_value == "port"

	def constraint(self, PreNode, graph):
		return True

