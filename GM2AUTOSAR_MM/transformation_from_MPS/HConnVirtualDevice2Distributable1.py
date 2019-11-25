from core.himesis import Himesis
import uuid

class HConnVirtualDevice2Distributable1(Himesis):
	def __init__(self):
		"""
		Creates the himesis graph representing the DSLTrans rule ConnVirtualDevice2Distributable1.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HConnVirtualDevice2Distributable1, self).__init__(name='HConnVirtualDevice2Distributable1', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """ConnVirtualDevice2Distributable1"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConnVirtualDevice2Distributable1')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """ConnVirtualDevice2Distributable1"""

		# match class PhysicalNode(3.0.m.0PhysicalNode) node
		self.add_node()
		self.vs[3]["mm__"] = """PhysicalNode"""
		self.vs[3]["attr1"] = """+"""

		# match class Partition(3.0.m.1Partition) node
		self.add_node()
		self.vs[4]["mm__"] = """Partition"""
		self.vs[4]["attr1"] = """+"""

		# match class Module(3.0.m.2Module) node
		self.add_node()
		self.vs[5]["mm__"] = """Module"""
		self.vs[5]["attr1"] = """+"""

		# apply class CompositionType(3.0.a.0CompositionType) node
		self.add_node()
		self.vs[6]["mm__"] = """CompositionType"""
		self.vs[6]["attr1"] = """1"""

		# apply class ComponentPrototype(3.0.a.1ComponentPrototype) node
		self.add_node()
		self.vs[7]["mm__"] = """ComponentPrototype"""
		self.vs[7]["attr1"] = """1"""

		# match association PhysicalNode--partition-->Partition node 
		self.add_node()
		self.vs[8]["attr1"] = """partition"""
		self.vs[8]["mm__"] = """directLink_S"""

		# match association Partition--module-->Module node 
		self.add_node()
		self.vs[9]["attr1"] = """module"""
		self.vs[9]["mm__"] = """directLink_S"""

		# apply association CompositionType--component-->ComponentPrototype node 
		self.add_node()
		self.vs[10]["attr1"] = """component"""
		self.vs[10]["mm__"] = """directLink_T"""

		# apply association ComponentPrototype--type-->CompositionType node 
		self.add_node()
		self.vs[11]["attr1"] = """type"""
		self.vs[11]["mm__"] = """directLink_T"""

		# backward association CompositionType-->PhysicalNodenode 
		self.add_node()
		self.vs[12]["mm__"] = """backward_link"""

		# backward association ComponentPrototype-->Modulenode 
		self.add_node()
		self.vs[13]["mm__"] = """backward_link"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class PhysicalNode(3.0.m.0PhysicalNode)
			(0,4), # matchmodel -> match_class Partition(3.0.m.1Partition)
			(0,5), # matchmodel -> match_class Module(3.0.m.2Module)
			(1,6), # applymodel -> apply_classCompositionType(3.0.a.0CompositionType)
			(1,7), # applymodel -> apply_classComponentPrototype(3.0.a.1ComponentPrototype)
			(3,8), # match classPhysicalNode(3.0.m.0PhysicalNode) -> association partition
			(8,4), # associationpartition -> match_classPhysicalNode(3.0.m.1Partition)
			(4,9), # match classPartition(3.0.m.1Partition) -> association module
			(9,5), # associationmodule -> match_classPartition(3.0.m.2Module)
			(6,10), # apply class CompositionType(3.0.a.0CompositionType) -> association component
			(10,7), # associationcomponent -> apply_classComponentPrototype(3.0.a.1ComponentPrototype)
			(7,11), # apply class ComponentPrototype(3.0.a.1ComponentPrototype) -> association type
			(11,6), # associationtype -> apply_classCompositionType(3.0.a.0CompositionType)
			(6,12), # apply class CompositionType(3.0.m.0PhysicalNode) -> backward_association 
			(12,3), # backward_associationPhysicalNode -> match_class PhysicalNode(3.0.m.0PhysicalNode)
			(7,13), # apply class ComponentPrototype(3.0.m.2Module) -> backward_association 
			(13,5), # backward_associationModule -> match_class Module(3.0.m.2Module)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = []
