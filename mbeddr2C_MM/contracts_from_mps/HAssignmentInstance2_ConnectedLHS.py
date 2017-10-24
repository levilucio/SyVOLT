from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HAssignmentInstance2_ConnectedLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HAssignmentInstance2_ConnectedLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HAssignmentInstance2_ConnectedLHS, self).__init__(name='HAssignmentInstance2_ConnectedLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HAssignmentInstance2_ConnectedLHS')
		self["equations"] = []
		# Set the node attributes

		# match class AssemblyConnector(0.3.m.0AssemblyConnector) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__AssemblyConnector"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.0AssemblyConnector')

		# match class InstancePortRef(0.3.m.1InstancePortRef) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__InstancePortRef"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.1InstancePortRef')

		# match class ComponentInstance(0.3.m.2ComponentInstance) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__ComponentInstance"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.2ComponentInstance')

		# match class RequiredPort(0.3.m.3RequiredPort) node
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return True"""
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__RequiredPort"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.3RequiredPort')

		# match class AtomicComponent(0.3.m.4AtomicComponent) node
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return True"""
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__AtomicComponent"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.4AtomicComponent')

		# match class InstancePortRef(0.3.m.5InstancePortRef) node
		self.add_node()
		self.vs[5]["MT_pre__attr1"] = """return True"""
		self.vs[5]["MT_label__"] = """6"""
		self.vs[5]["mm__"] = """MT_pre__InstancePortRef"""
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.5InstancePortRef')

		# match class ComponentInstance(0.3.m.6ComponentInstance) node
		self.add_node()
		self.vs[6]["MT_pre__attr1"] = """return True"""
		self.vs[6]["MT_label__"] = """7"""
		self.vs[6]["mm__"] = """MT_pre__ComponentInstance"""
		self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.6ComponentInstance')

		# match class ProvidedPort(0.3.m.7ProvidedPort) node
		self.add_node()
		self.vs[7]["MT_pre__attr1"] = """return True"""
		self.vs[7]["MT_label__"] = """8"""
		self.vs[7]["mm__"] = """MT_pre__ProvidedPort"""
		self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.7ProvidedPort')

		# match class AtomicComponent(0.3.m.8AtomicComponent) node
		self.add_node()
		self.vs[8]["MT_pre__attr1"] = """return True"""
		self.vs[8]["MT_label__"] = """9"""
		self.vs[8]["mm__"] = """MT_pre__AtomicComponent"""
		self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.8AtomicComponent')


		# match association AssemblyConnector--source-->InstancePortRefnode
		self.add_node()
		self.vs[9]["MT_pre__attr1"] = """return attr_value == "source" """
		self.vs[9]["MT_label__"] = """10"""
		self.vs[9]["mm__"] = """MT_pre__directLink_S"""
		self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.0AssemblyConnectorassoc90.3.m.1InstancePortRef')

		# match association InstancePortRef--instance-->ComponentInstancenode
		self.add_node()
		self.vs[10]["MT_pre__attr1"] = """return attr_value == "instance" """
		self.vs[10]["MT_label__"] = """11"""
		self.vs[10]["mm__"] = """MT_pre__directLink_S"""
		self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.1InstancePortRefassoc100.3.m.2ComponentInstance')

		# match association InstancePortRef--port-->RequiredPortnode
		self.add_node()
		self.vs[11]["MT_pre__attr1"] = """return attr_value == "port" """
		self.vs[11]["MT_label__"] = """12"""
		self.vs[11]["mm__"] = """MT_pre__directLink_S"""
		self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.1InstancePortRefassoc110.3.m.3RequiredPort')

		# match association ComponentInstance--component-->AtomicComponentnode
		self.add_node()
		self.vs[12]["MT_pre__attr1"] = """return attr_value == "component" """
		self.vs[12]["MT_label__"] = """13"""
		self.vs[12]["mm__"] = """MT_pre__directLink_S"""
		self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.2ComponentInstanceassoc120.3.m.4AtomicComponent')

		# match association AtomicComponent--contents-->RequiredPortnode
		self.add_node()
		self.vs[13]["MT_pre__attr1"] = """return attr_value == "contents" """
		self.vs[13]["MT_label__"] = """14"""
		self.vs[13]["mm__"] = """MT_pre__directLink_S"""
		self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.4AtomicComponentassoc130.3.m.3RequiredPort')

		# match association AssemblyConnector--target-->InstancePortRefnode
		self.add_node()
		self.vs[14]["MT_pre__attr1"] = """return attr_value == "target" """
		self.vs[14]["MT_label__"] = """15"""
		self.vs[14]["mm__"] = """MT_pre__directLink_S"""
		self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.0AssemblyConnectorassoc140.3.m.5InstancePortRef')

		# match association InstancePortRef--instance-->ComponentInstancenode
		self.add_node()
		self.vs[15]["MT_pre__attr1"] = """return attr_value == "instance" """
		self.vs[15]["MT_label__"] = """16"""
		self.vs[15]["mm__"] = """MT_pre__directLink_S"""
		self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.5InstancePortRefassoc150.3.m.6ComponentInstance')

		# match association InstancePortRef--port-->ProvidedPortnode
		self.add_node()
		self.vs[16]["MT_pre__attr1"] = """return attr_value == "port" """
		self.vs[16]["MT_label__"] = """17"""
		self.vs[16]["mm__"] = """MT_pre__directLink_S"""
		self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.5InstancePortRefassoc160.3.m.7ProvidedPort')

		# match association ComponentInstance--component-->AtomicComponentnode
		self.add_node()
		self.vs[17]["MT_pre__attr1"] = """return attr_value == "component" """
		self.vs[17]["MT_label__"] = """18"""
		self.vs[17]["mm__"] = """MT_pre__directLink_S"""
		self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.6ComponentInstanceassoc170.3.m.8AtomicComponent')

		# match association AtomicComponent--contents-->ProvidedPortnode
		self.add_node()
		self.vs[18]["MT_pre__attr1"] = """return attr_value == "contents" """
		self.vs[18]["MT_label__"] = """19"""
		self.vs[18]["mm__"] = """MT_pre__directLink_S"""
		self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.3.m.8AtomicComponentassoc180.3.m.7ProvidedPort')

		# Add the edges
		self.add_edges([
			(0,9), # match class AssemblyConnector(0.3.m.0AssemblyConnector) -> association source
			(9,1), # association InstancePortRef -> match class InstancePortRef(0.3.m.1InstancePortRef)
			(1,10), # match class InstancePortRef(0.3.m.1InstancePortRef) -> association instance
			(10,2), # association ComponentInstance -> match class ComponentInstance(0.3.m.2ComponentInstance)
			(1,11), # match class InstancePortRef(0.3.m.1InstancePortRef) -> association port
			(11,3), # association RequiredPort -> match class RequiredPort(0.3.m.3RequiredPort)
			(2,12), # match class ComponentInstance(0.3.m.2ComponentInstance) -> association component
			(12,4), # association AtomicComponent -> match class AtomicComponent(0.3.m.4AtomicComponent)
			(4,13), # match class AtomicComponent(0.3.m.4AtomicComponent) -> association contents
			(13,3), # association RequiredPort -> match class RequiredPort(0.3.m.3RequiredPort)
			(0,14), # match class AssemblyConnector(0.3.m.0AssemblyConnector) -> association target
			(14,5), # association InstancePortRef -> match class InstancePortRef(0.3.m.5InstancePortRef)
			(5,15), # match class InstancePortRef(0.3.m.5InstancePortRef) -> association instance
			(15,6), # association ComponentInstance -> match class ComponentInstance(0.3.m.6ComponentInstance)
			(5,16), # match class InstancePortRef(0.3.m.5InstancePortRef) -> association port
			(16,7), # association ProvidedPort -> match class ProvidedPort(0.3.m.7ProvidedPort)
			(6,17), # match class ComponentInstance(0.3.m.6ComponentInstance) -> association component
			(17,8), # association AtomicComponent -> match class AtomicComponent(0.3.m.8AtomicComponent)
			(8,18), # match class AtomicComponent(0.3.m.8AtomicComponent) -> association contents
			(18,7), # association ProvidedPort -> match class ProvidedPort(0.3.m.7ProvidedPort)
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

	def eval_attr16(self, attr_value, this):
		return True

	def eval_attr17(self, attr_value, this):
		return True

	def eval_attr18(self, attr_value, this):
		return True

	def eval_attr19(self, attr_value, this):
		return True

	# define evaluation methods for each match association.

	def eval_attr110(self, attr_value, this):
		return attr_value == "source"
	def eval_attr111(self, attr_value, this):
		return attr_value == "instance"
	def eval_attr112(self, attr_value, this):
		return attr_value == "port"
	def eval_attr113(self, attr_value, this):
		return attr_value == "component"
	def eval_attr114(self, attr_value, this):
		return attr_value == "contents"
	def eval_attr115(self, attr_value, this):
		return attr_value == "target"
	def eval_attr116(self, attr_value, this):
		return attr_value == "instance"
	def eval_attr117(self, attr_value, this):
		return attr_value == "port"
	def eval_attr118(self, attr_value, this):
		return attr_value == "component"
	def eval_attr119(self, attr_value, this):
		return attr_value == "contents"

	def constraint(self, PreNode, graph):
		return True

