from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HGlobalVarGetsCorrectFunctionAddress_ConnectedLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HGlobalVarGetsCorrectFunctionAddress_ConnectedLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HGlobalVarGetsCorrectFunctionAddress_ConnectedLHS, self).__init__(name='HGlobalVarGetsCorrectFunctionAddress_ConnectedLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HGlobalVarGetsCorrectFunctionAddress_ConnectedLHS')
		self["equations"] = []
		# Set the node attributes

		# match class ComponentInstance(0.2.m.0ComponentInstance) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__ComponentInstance"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.m.0ComponentInstance')

		# match class Operation(0.2.m.1Operation) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__Operation"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.m.1Operation')

		# match class OperationTrigger(0.2.m.2OperationTrigger) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__OperationTrigger"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.m.2OperationTrigger')

		# match class Executable(0.2.m.3Executable) node
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return True"""
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__Executable"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.m.3Executable')

		# match class ProvidedPort(0.2.m.4ProvidedPort) node
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return True"""
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__ProvidedPort"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.m.4ProvidedPort')

		# match class InstanceConfiguration(0.2.m.5InstanceConfiguration) node
		self.add_node()
		self.vs[5]["MT_pre__attr1"] = """return True"""
		self.vs[5]["MT_label__"] = """6"""
		self.vs[5]["mm__"] = """MT_pre__InstanceConfiguration"""
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.m.5InstanceConfiguration')

		# match class ClientServerInterface(0.2.m.6ClientServerInterface) node
		self.add_node()
		self.vs[6]["MT_pre__attr1"] = """return True"""
		self.vs[6]["MT_label__"] = """7"""
		self.vs[6]["mm__"] = """MT_pre__ClientServerInterface"""
		self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.m.6ClientServerInterface')

		# match class AtomicComponent(0.2.m.7AtomicComponent) node
		self.add_node()
		self.vs[7]["MT_pre__attr1"] = """return True"""
		self.vs[7]["MT_label__"] = """8"""
		self.vs[7]["mm__"] = """MT_pre__AtomicComponent"""
		self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.m.7AtomicComponent')


		# match association InstanceConfiguration--contents-->ComponentInstancenode
		self.add_node()
		self.vs[8]["MT_pre__attr1"] = """return attr_value == "contents" """
		self.vs[8]["MT_label__"] = """9"""
		self.vs[8]["mm__"] = """MT_pre__directLink_S"""
		self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.m.5InstanceConfigurationassoc80.2.m.0ComponentInstance')

		# match association AtomicComponent--contents-->ProvidedPortnode
		self.add_node()
		self.vs[9]["MT_pre__attr1"] = """return attr_value == "contents" """
		self.vs[9]["MT_label__"] = """10"""
		self.vs[9]["mm__"] = """MT_pre__directLink_S"""
		self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.m.7AtomicComponentassoc90.2.m.4ProvidedPort')

		# match association ComponentInstance--component-->AtomicComponentnode
		self.add_node()
		self.vs[10]["MT_pre__attr1"] = """return attr_value == "component" """
		self.vs[10]["MT_label__"] = """11"""
		self.vs[10]["mm__"] = """MT_pre__directLink_S"""
		self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.m.0ComponentInstanceassoc100.2.m.7AtomicComponent')

		# match association AtomicComponent--contents-->Executablenode
		self.add_node()
		self.vs[11]["MT_pre__attr1"] = """return attr_value == "contents" """
		self.vs[11]["MT_label__"] = """12"""
		self.vs[11]["mm__"] = """MT_pre__directLink_S"""
		self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.m.7AtomicComponentassoc110.2.m.3Executable')

		# match association Executable--trigger-->OperationTriggernode
		self.add_node()
		self.vs[12]["MT_pre__attr1"] = """return attr_value == "trigger" """
		self.vs[12]["MT_label__"] = """13"""
		self.vs[12]["mm__"] = """MT_pre__directLink_S"""
		self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.m.3Executableassoc120.2.m.2OperationTrigger')

		# match association OperationTrigger--calledOperation-->Operationnode
		self.add_node()
		self.vs[13]["MT_pre__attr1"] = """return attr_value == "calledOperation" """
		self.vs[13]["MT_label__"] = """14"""
		self.vs[13]["mm__"] = """MT_pre__directLink_S"""
		self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.m.2OperationTriggerassoc130.2.m.1Operation')

		# match association ProvidedPort--intf-->ClientServerInterfacenode
		self.add_node()
		self.vs[14]["MT_pre__attr1"] = """return attr_value == "intf" """
		self.vs[14]["MT_label__"] = """15"""
		self.vs[14]["mm__"] = """MT_pre__directLink_S"""
		self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.m.4ProvidedPortassoc140.2.m.6ClientServerInterface')

		# match association ClientServerInterface--contents-->Operationnode
		self.add_node()
		self.vs[15]["MT_pre__attr1"] = """return attr_value == "contents" """
		self.vs[15]["MT_label__"] = """16"""
		self.vs[15]["mm__"] = """MT_pre__directLink_S"""
		self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.m.6ClientServerInterfaceassoc150.2.m.1Operation')

		# match association OperationTrigger--providedPort-->ProvidedPortnode
		self.add_node()
		self.vs[16]["MT_pre__attr1"] = """return attr_value == "providedPort" """
		self.vs[16]["MT_label__"] = """17"""
		self.vs[16]["mm__"] = """MT_pre__directLink_S"""
		self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.2.m.2OperationTriggerassoc160.2.m.4ProvidedPort')

		# Add the edges
		self.add_edges([
			(5,8), # match class InstanceConfiguration(0.2.m.5InstanceConfiguration) -> association contents
			(8,0), # association ComponentInstance -> match class ComponentInstance(0.2.m.0ComponentInstance)
			(7,9), # match class AtomicComponent(0.2.m.7AtomicComponent) -> association contents
			(9,4), # association ProvidedPort -> match class ProvidedPort(0.2.m.4ProvidedPort)
			(0,10), # match class ComponentInstance(0.2.m.0ComponentInstance) -> association component
			(10,7), # association AtomicComponent -> match class AtomicComponent(0.2.m.7AtomicComponent)
			(7,11), # match class AtomicComponent(0.2.m.7AtomicComponent) -> association contents
			(11,3), # association Executable -> match class Executable(0.2.m.3Executable)
			(3,12), # match class Executable(0.2.m.3Executable) -> association trigger
			(12,2), # association OperationTrigger -> match class OperationTrigger(0.2.m.2OperationTrigger)
			(2,13), # match class OperationTrigger(0.2.m.2OperationTrigger) -> association calledOperation
			(13,1), # association Operation -> match class Operation(0.2.m.1Operation)
			(4,14), # match class ProvidedPort(0.2.m.4ProvidedPort) -> association intf
			(14,6), # association ClientServerInterface -> match class ClientServerInterface(0.2.m.6ClientServerInterface)
			(6,15), # match class ClientServerInterface(0.2.m.6ClientServerInterface) -> association contents
			(15,1), # association Operation -> match class Operation(0.2.m.1Operation)
			(2,16), # match class OperationTrigger(0.2.m.2OperationTrigger) -> association providedPort
			(16,4), # association ProvidedPort -> match class ProvidedPort(0.2.m.4ProvidedPort)
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

	# define evaluation methods for each match association.

	def eval_attr19(self, attr_value, this):
		return attr_value == "contents"
	def eval_attr110(self, attr_value, this):
		return attr_value == "contents"
	def eval_attr111(self, attr_value, this):
		return attr_value == "component"
	def eval_attr112(self, attr_value, this):
		return attr_value == "contents"
	def eval_attr113(self, attr_value, this):
		return attr_value == "trigger"
	def eval_attr114(self, attr_value, this):
		return attr_value == "calledOperation"
	def eval_attr115(self, attr_value, this):
		return attr_value == "intf"
	def eval_attr116(self, attr_value, this):
		return attr_value == "contents"
	def eval_attr117(self, attr_value, this):
		return attr_value == "providedPort"

	def constraint(self, PreNode, graph):
		return True

