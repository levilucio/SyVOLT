from core.himesis import Himesis
import uuid

class HMapPartition(Himesis):
	def __init__(self, *args, **kwargs):
		"""
		Creates the himesis graph representing the DSLTrans rule MapPartition.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HMapPartition, self).__init__(name='HMapPartition', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """MapPartition"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'MapPartition')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """MapPartition"""

		# match class Partition(1.1.m.0Partition) node
		self.add_node()
		self.vs[3]["mm__"] = """Partition"""
		self.vs[3]["attr1"] = """+"""

		# match class PhysicalNode(1.1.m.1PhysicalNode) node
		self.add_node()
		self.vs[4]["mm__"] = """PhysicalNode"""
		self.vs[4]["attr1"] = """1"""

		# match class Module(1.1.m.2Module) node
		self.add_node()
		self.vs[5]["mm__"] = """Module"""
		self.vs[5]["attr1"] = """1"""

		# apply class SwcToEcuMapping(1.1.a.0SwcToEcuMapping) node
		self.add_node()
		self.vs[6]["mm__"] = """SwcToEcuMapping"""
		self.vs[6]["attr1"] = """1"""

		# match association PhysicalNode--partition-->Partition node 
		self.add_node()
		self.vs[7]["attr1"] = """partition"""
		self.vs[7]["mm__"] = """directLink_S"""

		# match association Partition--module-->Module node 
		self.add_node()
		self.vs[8]["attr1"] = """module"""
		self.vs[8]["mm__"] = """directLink_S"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class Partition(1.1.m.0Partition)
			(0,4), # matchmodel -> match_class PhysicalNode(1.1.m.1PhysicalNode)
			(0,5), # matchmodel -> match_class Module(1.1.m.2Module)
			(1,6), # applymodel -> apply_classSwcToEcuMapping(1.1.a.0SwcToEcuMapping)
			(4,7), # match classPhysicalNode(1.1.m.1PhysicalNode) -> association partition
			(7,3), # associationpartition -> match_classPhysicalNode(1.1.m.0Partition)
			(3,8), # match classPartition(1.1.m.0Partition) -> association module
			(8,5), # associationmodule -> match_classPartition(1.1.m.2Module)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = [((6,'shortName'),('concat',(('constant','Swc2EcuMapping_'),(3,'name')))),]
