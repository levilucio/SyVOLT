from core.himesis import Himesis
import uuid

class HConnectPPortPrototype(Himesis):
	def __init__(self):
		"""
		Creates the himesis graph representing the DSLTrans rule ConnectPPortPrototype.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HConnectPPortPrototype, self).__init__(name='HConnectPPortPrototype', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """ConnectPPortPrototype"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConnectPPortPrototype')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """ConnectPPortPrototype"""

		# match class PhysicalNode(4.0.m.0PhysicalNode) node
		self.add_node()
		self.vs[3]["mm__"] = """PhysicalNode"""
		self.vs[3]["attr1"] = """+"""

		# match class Partition(4.0.m.1Partition) node
		self.add_node()
		self.vs[4]["mm__"] = """Partition"""
		self.vs[4]["attr1"] = """+"""

		# match class Module(4.0.m.2Module) node
		self.add_node()
		self.vs[5]["mm__"] = """Module"""
		self.vs[5]["attr1"] = """+"""

		# match class Scheduler(4.0.m.3Scheduler) node
		self.add_node()
		self.vs[6]["mm__"] = """Scheduler"""
		self.vs[6]["attr1"] = """+"""

		# match class Service(4.0.m.4Service) node
		self.add_node()
		self.vs[7]["mm__"] = """Service"""
		self.vs[7]["attr1"] = """1"""

		# apply class CompositionType(4.0.a.0CompositionType) node
		self.add_node()
		self.vs[8]["mm__"] = """CompositionType"""
		self.vs[8]["attr1"] = """1"""

		# apply class PPortPrototype(4.0.a.1PPortPrototype) node
		self.add_node()
		self.vs[9]["mm__"] = """PPortPrototype"""
		self.vs[9]["attr1"] = """1"""

		# match association PhysicalNode--partition-->Partition node 
		self.add_node()
		self.vs[10]["attr1"] = """partition"""
		self.vs[10]["mm__"] = """directLink_S"""

		# match association Partition--module-->Module node 
		self.add_node()
		self.vs[11]["attr1"] = """module"""
		self.vs[11]["mm__"] = """directLink_S"""

		# match association Module--scheduler-->Scheduler node 
		self.add_node()
		self.vs[12]["attr1"] = """scheduler"""
		self.vs[12]["mm__"] = """directLink_S"""

		# match association Scheduler--provided-->Service node 
		self.add_node()
		self.vs[13]["attr1"] = """provided"""
		self.vs[13]["mm__"] = """directLink_S"""

		# apply association CompositionType--port-->PPortPrototype node 
		self.add_node()
		self.vs[14]["attr1"] = """port"""
		self.vs[14]["mm__"] = """directLink_T"""

		# backward association CompositionType-->PhysicalNodenode 
		self.add_node()
		self.vs[15]["mm__"] = """backward_link"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class PhysicalNode(4.0.m.0PhysicalNode)
			(0,4), # matchmodel -> match_class Partition(4.0.m.1Partition)
			(0,5), # matchmodel -> match_class Module(4.0.m.2Module)
			(0,6), # matchmodel -> match_class Scheduler(4.0.m.3Scheduler)
			(0,7), # matchmodel -> match_class Service(4.0.m.4Service)
			(1,8), # applymodel -> apply_classCompositionType(4.0.a.0CompositionType)
			(1,9), # applymodel -> apply_classPPortPrototype(4.0.a.1PPortPrototype)
			(3,10), # match classPhysicalNode(4.0.m.0PhysicalNode) -> association partition
			(10,4), # associationpartition -> match_classPhysicalNode(4.0.m.1Partition)
			(4,11), # match classPartition(4.0.m.1Partition) -> association module
			(11,5), # associationmodule -> match_classPartition(4.0.m.2Module)
			(5,12), # match classModule(4.0.m.2Module) -> association scheduler
			(12,6), # associationscheduler -> match_classModule(4.0.m.3Scheduler)
			(6,13), # match classScheduler(4.0.m.3Scheduler) -> association provided
			(13,7), # associationprovided -> match_classScheduler(4.0.m.4Service)
			(8,14), # apply class CompositionType(4.0.a.0CompositionType) -> association port
			(14,9), # associationport -> apply_classPPortPrototype(4.0.a.1PPortPrototype)
			(8,15), # apply class CompositionType(4.0.m.0PhysicalNode) -> backward_association 
			(15,3), # backward_associationPhysicalNode -> match_class PhysicalNode(4.0.m.0PhysicalNode)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = [((9,'shortName'),('concat',((6,'name'),('constant','PROV')))),]
