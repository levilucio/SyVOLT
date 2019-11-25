from core.himesis import Himesis
import uuid

class HConnVirtualDevice2Distributable2(Himesis):
	def __init__(self):
		"""
		Creates the himesis graph representing the DSLTrans rule ConnVirtualDevice2Distributable2.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HConnVirtualDevice2Distributable2, self).__init__(name='HConnVirtualDevice2Distributable2', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """ConnVirtualDevice2Distributable2"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConnVirtualDevice2Distributable2')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """ConnVirtualDevice2Distributable2"""

		# match class Partition(5.0.m.0Partition) node
		self.add_node()
		self.vs[3]["mm__"] = """Partition"""
		self.vs[3]["attr1"] = """+"""

		# match class Module(5.0.m.1Module) node
		self.add_node()
		self.vs[4]["mm__"] = """Module"""
		self.vs[4]["attr1"] = """+"""

		# apply class SwcToEcuMapping(5.0.a.0SwcToEcuMapping) node
		self.add_node()
		self.vs[5]["mm__"] = """SwcToEcuMapping"""
		self.vs[5]["attr1"] = """1"""

		# apply class SwCompToEcuMapping_component(5.0.a.1SwCompToEcuMapping_component) node
		self.add_node()
		self.vs[6]["mm__"] = """SwCompToEcuMapping_component"""
		self.vs[6]["attr1"] = """1"""

		# match association Partition--module-->Module node 
		self.add_node()
		self.vs[7]["attr1"] = """module"""
		self.vs[7]["mm__"] = """directLink_S"""

		# apply association SwcToEcuMapping--component-->SwCompToEcuMapping_component node 
		self.add_node()
		self.vs[8]["attr1"] = """component"""
		self.vs[8]["mm__"] = """directLink_T"""

		# backward association SwcToEcuMapping-->Partitionnode 
		self.add_node()
		self.vs[9]["mm__"] = """backward_link"""

		# backward association SwCompToEcuMapping_component-->Modulenode 
		self.add_node()
		self.vs[10]["mm__"] = """backward_link"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class Partition(5.0.m.0Partition)
			(0,4), # matchmodel -> match_class Module(5.0.m.1Module)
			(1,5), # applymodel -> apply_classSwcToEcuMapping(5.0.a.0SwcToEcuMapping)
			(1,6), # applymodel -> apply_classSwCompToEcuMapping_component(5.0.a.1SwCompToEcuMapping_component)
			(3,7), # match classPartition(5.0.m.0Partition) -> association module
			(7,4), # associationmodule -> match_classPartition(5.0.m.1Module)
			(5,8), # apply class SwcToEcuMapping(5.0.a.0SwcToEcuMapping) -> association component
			(8,6), # associationcomponent -> apply_classSwCompToEcuMapping_component(5.0.a.1SwCompToEcuMapping_component)
			(5,9), # apply class SwcToEcuMapping(5.0.m.0Partition) -> backward_association 
			(9,3), # backward_associationPartition -> match_class Partition(5.0.m.0Partition)
			(6,10), # apply class SwCompToEcuMapping_component(5.0.m.1Module) -> backward_association 
			(10,4), # backward_associationModule -> match_class Module(5.0.m.1Module)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = []
