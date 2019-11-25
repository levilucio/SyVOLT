from core.himesis import Himesis
import uuid

class HConnECU2VirtualDevice1(Himesis):
	def __init__(self):
		"""
		Creates the himesis graph representing the DSLTrans rule ConnECU2VirtualDevice1.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HConnECU2VirtualDevice1, self).__init__(name='HConnECU2VirtualDevice1', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """ConnECU2VirtualDevice1"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConnECU2VirtualDevice1')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """ConnECU2VirtualDevice1"""

		# match class PhysicalNode(2.0.m.0PhysicalNode) node
		self.add_node()
		self.vs[3]["mm__"] = """PhysicalNode"""
		self.vs[3]["attr1"] = """+"""

		# match class Partition(2.0.m.1Partition) node
		self.add_node()
		self.vs[4]["mm__"] = """Partition"""
		self.vs[4]["attr1"] = """+"""

		# apply class SystemMapping(2.0.a.0SystemMapping) node
		self.add_node()
		self.vs[5]["mm__"] = """SystemMapping"""
		self.vs[5]["attr1"] = """1"""

		# apply class SwcToEcuMapping(2.0.a.1SwcToEcuMapping) node
		self.add_node()
		self.vs[6]["mm__"] = """SwcToEcuMapping"""
		self.vs[6]["attr1"] = """1"""

		# match association PhysicalNode--partition-->Partition node 
		self.add_node()
		self.vs[7]["attr1"] = """partition"""
		self.vs[7]["mm__"] = """directLink_S"""

		# apply association SystemMapping--swMapping-->SwcToEcuMapping node 
		self.add_node()
		self.vs[8]["attr1"] = """swMapping"""
		self.vs[8]["mm__"] = """directLink_T"""

		# backward association SystemMapping-->PhysicalNodenode 
		self.add_node()
		self.vs[9]["mm__"] = """backward_link"""

		# backward association SwcToEcuMapping-->Partitionnode 
		self.add_node()
		self.vs[10]["mm__"] = """backward_link"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class PhysicalNode(2.0.m.0PhysicalNode)
			(0,4), # matchmodel -> match_class Partition(2.0.m.1Partition)
			(1,5), # applymodel -> apply_classSystemMapping(2.0.a.0SystemMapping)
			(1,6), # applymodel -> apply_classSwcToEcuMapping(2.0.a.1SwcToEcuMapping)
			(3,7), # match classPhysicalNode(2.0.m.0PhysicalNode) -> association partition
			(7,4), # associationpartition -> match_classPhysicalNode(2.0.m.1Partition)
			(5,8), # apply class SystemMapping(2.0.a.0SystemMapping) -> association swMapping
			(8,6), # associationswMapping -> apply_classSwcToEcuMapping(2.0.a.1SwcToEcuMapping)
			(5,9), # apply class SystemMapping(2.0.m.0PhysicalNode) -> backward_association 
			(9,3), # backward_associationPhysicalNode -> match_class PhysicalNode(2.0.m.0PhysicalNode)
			(6,10), # apply class SwcToEcuMapping(2.0.m.1Partition) -> backward_association 
			(10,4), # backward_associationPartition -> match_class Partition(2.0.m.1Partition)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = []
