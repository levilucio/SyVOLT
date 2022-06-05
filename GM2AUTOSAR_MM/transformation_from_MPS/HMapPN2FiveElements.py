from core.himesis import Himesis
import uuid

class HMapPN2FiveElements(Himesis):
	def __init__(self, *args, **kwargs):
		"""
		Creates the himesis graph representing the DSLTrans rule MapPN2FiveElements.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HMapPN2FiveElements, self).__init__(name='HMapPN2FiveElements', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """MapPN2FiveElements"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'MapPN2FiveElements')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """MapPN2FiveElements"""

		# match class PhysicalNode(1.0.m.0PhysicalNode) node
		self.add_node()
		self.vs[3]["mm__"] = """PhysicalNode"""
		self.vs[3]["attr1"] = """+"""

		# match class Partition(1.0.m.1Partition) node
		self.add_node()
		self.vs[4]["mm__"] = """Partition"""
		self.vs[4]["attr1"] = """1"""

		# match class Module(1.0.m.2Module) node
		self.add_node()
		self.vs[5]["mm__"] = """Module"""
		self.vs[5]["attr1"] = """1"""

		# apply class SystemMapping(1.0.a.0SystemMapping) node
		self.add_node()
		self.vs[6]["mm__"] = """SystemMapping"""
		self.vs[6]["attr1"] = """1"""

		# apply class System(1.0.a.1System) node
		self.add_node()
		self.vs[7]["mm__"] = """System"""
		self.vs[7]["attr1"] = """1"""

		# apply class SoftwareComposition(1.0.a.2SoftwareComposition) node
		self.add_node()
		self.vs[8]["mm__"] = """SoftwareComposition"""
		self.vs[8]["attr1"] = """1"""

		# apply class CompositionType(1.0.a.3CompositionType) node
		self.add_node()
		self.vs[9]["mm__"] = """CompositionType"""
		self.vs[9]["attr1"] = """1"""

		# apply class EcuInstance(1.0.a.4EcuInstance) node
		self.add_node()
		self.vs[10]["mm__"] = """EcuInstance"""
		self.vs[10]["attr1"] = """1"""

		# match association PhysicalNode--partition-->Partition node 
		self.add_node()
		self.vs[11]["attr1"] = """partition"""
		self.vs[11]["mm__"] = """directLink_S"""

		# match association Partition--module-->Module node 
		self.add_node()
		self.vs[12]["attr1"] = """module"""
		self.vs[12]["mm__"] = """directLink_S"""

		# apply association System--mapping-->SystemMapping node 
		self.add_node()
		self.vs[13]["attr1"] = """mapping"""
		self.vs[13]["mm__"] = """directLink_T"""

		# apply association System--softwareComposition-->SoftwareComposition node 
		self.add_node()
		self.vs[14]["attr1"] = """softwareComposition"""
		self.vs[14]["mm__"] = """directLink_T"""

		# apply association SoftwareComposition--softwareComposition-->CompositionType node 
		self.add_node()
		self.vs[15]["attr1"] = """softwareComposition"""
		self.vs[15]["mm__"] = """directLink_T"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class PhysicalNode(1.0.m.0PhysicalNode)
			(0,4), # matchmodel -> match_class Partition(1.0.m.1Partition)
			(0,5), # matchmodel -> match_class Module(1.0.m.2Module)
			(1,6), # applymodel -> apply_classSystemMapping(1.0.a.0SystemMapping)
			(1,7), # applymodel -> apply_classSystem(1.0.a.1System)
			(1,8), # applymodel -> apply_classSoftwareComposition(1.0.a.2SoftwareComposition)
			(1,9), # applymodel -> apply_classCompositionType(1.0.a.3CompositionType)
			(1,10), # applymodel -> apply_classEcuInstance(1.0.a.4EcuInstance)
			(3,11), # match classPhysicalNode(1.0.m.0PhysicalNode) -> association partition
			(11,4), # associationpartition -> match_classPhysicalNode(1.0.m.1Partition)
			(4,12), # match classPartition(1.0.m.1Partition) -> association module
			(12,5), # associationmodule -> match_classPartition(1.0.m.2Module)
			(7,13), # apply class System(1.0.a.1System) -> association mapping
			(13,6), # associationmapping -> apply_classSystemMapping(1.0.a.0SystemMapping)
			(7,14), # apply class System(1.0.a.1System) -> association softwareComposition
			(14,8), # associationsoftwareComposition -> apply_classSoftwareComposition(1.0.a.2SoftwareComposition)
			(8,15), # apply class SoftwareComposition(1.0.a.2SoftwareComposition) -> association softwareComposition
			(15,9), # associationsoftwareComposition -> apply_classCompositionType(1.0.a.3CompositionType)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = [((6,'shortName'),('concat',(('constant','SysMapping_'),(3,'name')))),((7,'shortName'),('concat',(('constant','SysTemplate_'),(3,'name')))),((8,'shortName'),('concat',(('constant','SoftwareComposition_'),(3,'name')))),((9,'shortName'),('concat',(('constant','CompositionType_'),(3,'name')))),((10,'shortName'),('concat',(('constant','EcuInstance_'),(3,'name')))),]
