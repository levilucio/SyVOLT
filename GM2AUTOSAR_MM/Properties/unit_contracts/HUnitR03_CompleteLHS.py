from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HUnitR03_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HUnitR03_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HUnitR03_CompleteLHS, self).__init__(name='HUnitR03_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HUnitR03_CompleteLHS')
		self["equations"] = []
		# Set the node attributes

		# match class PhysicalNode(3.0.m.0PhysicalNode) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__PhysicalNode"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'3.0.m.0PhysicalNode')

		# match class Partition(3.0.m.1Partition) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__Partition"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'3.0.m.1Partition')

		# match class Module(3.0.m.2Module) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__Module"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'3.0.m.2Module')

		# apply class CompositionType(3.0.a.0CompositionType) node
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return True"""
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__CompositionType"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'3.0.a.0CompositionType')

		# apply class ComponentPrototype(3.0.a.1ComponentPrototype) node
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return True"""
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__ComponentPrototype"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'3.0.a.1ComponentPrototype')

		# match association PhysicalNode--partition-->Partitionnode
		self.add_node()
		self.vs[5]["MT_pre__attr1"] = """return attr_value == "partition" """
		self.vs[5]["MT_label__"] = """6"""
		self.vs[5]["mm__"] = """MT_pre__directLink_S"""
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'3.0.m.0PhysicalNodeassoc53.0.m.1Partition')

		# match association Partition--module-->Modulenode
		self.add_node()
		self.vs[6]["MT_pre__attr1"] = """return attr_value == "module" """
		self.vs[6]["MT_label__"] = """7"""
		self.vs[6]["mm__"] = """MT_pre__directLink_S"""
		self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'3.0.m.1Partitionassoc63.0.m.2Module')

		# apply association CompositionType--component-->ComponentPrototypenode
		self.add_node()
		self.vs[7]["MT_pre__attr1"] = """return attr_value == "component" """
		self.vs[7]["MT_label__"] = """8"""
		self.vs[7]["mm__"] = """MT_pre__directLink_T"""
		self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'3.0.a.0CompositionTypeassoc73.0.a.1ComponentPrototype')

		# apply association ComponentPrototype--type-->CompositionTypenode
		self.add_node()
		self.vs[8]["MT_pre__attr1"] = """return attr_value == "type" """
		self.vs[8]["MT_label__"] = """9"""
		self.vs[8]["mm__"] = """MT_pre__directLink_T"""
		self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'3.0.a.1ComponentPrototypeassoc83.0.a.0CompositionType')

		# trace association CompositionType--trace-->PhysicalNodenode
		self.add_node()
		self.vs[9]["MT_label__"] = """10"""
		self.vs[9]["mm__"] = """MT_pre__trace_link"""
		self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'3.0.a.0CompositionTypeassoc93.0.m.0PhysicalNode')

		# trace association ComponentPrototype--trace-->Modulenode
		self.add_node()
		self.vs[10]["MT_label__"] = """11"""
		self.vs[10]["mm__"] = """MT_pre__trace_link"""
		self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'3.0.a.1ComponentPrototypeassoc103.0.m.2Module')


		# Add the edges
		self.add_edges([
			(0,5), # match class PhysicalNode(3.0.m.0PhysicalNode) -> association partition
			(5,1), # association Partition -> match class Partition(3.0.m.1Partition)
			(1,6), # match class Partition(3.0.m.1Partition) -> association module
			(6,2), # association Module -> match class Module(3.0.m.2Module)
			(3,7), # apply class CompositionType(3.0.a.0CompositionType) -> association component
			(7,4), # association ComponentPrototype -> apply class ComponentPrototype(3.0.a.1ComponentPrototype)
			(4,8), # apply class ComponentPrototype(3.0.a.1ComponentPrototype) -> association type
			(8,3), # association CompositionType -> apply class CompositionType(3.0.a.0CompositionType)
			(3,9), # apply class CompositionType(3.0.m.0PhysicalNode) -> backward_association 
			(9,0), # backward_associationPhysicalNode -> match_class PhysicalNode(3.0.m.0PhysicalNode)
			(4,10), # apply class ComponentPrototype(3.0.m.2Module) -> backward_association 
			(10,2), # backward_associationModule -> match_class Module(3.0.m.2Module)
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

		# define evaluation methods for each match association.

	def eval_attr16(self, attr_value, this):
		return attr_value == "partition"
	def eval_attr17(self, attr_value, this):
		return attr_value == "module"
		# define evaluation methods for each apply association.

	def eval_attr18(self, attr_value, this):
		return attr_value == "component"
	def eval_attr19(self, attr_value, this):
		return attr_value == "type"

	def constraint(self, PreNode, graph):
		return True

