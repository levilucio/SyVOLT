from core.himesis import Himesis
import uuid

class Hlayer3rule3(Himesis):
	def __init__(self):
		"""
		Creates the himesis graph representing the DSLTrans rule layer3rule3.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(Hlayer3rule3, self).__init__(name='Hlayer3rule3', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """layer3rule3"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule3')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """layer3rule3"""

		# match class ImplementationModule(layer3rule3class0ImplementationModule) node
		self.add_node()
		self.vs[3]["mm__"] = """ImplementationModule"""
		self.vs[3]["attr1"] = """+"""

		# match class InstanceConfiguration(layer3rule3class1InstanceConfiguration) node
		self.add_node()
		self.vs[4]["mm__"] = """InstanceConfiguration"""
		self.vs[4]["attr1"] = """+"""

		# match class ComponentInstance(layer3rule3class2ComponentInstance) node
		self.add_node()
		self.vs[5]["mm__"] = """ComponentInstance"""
		self.vs[5]["attr1"] = """+"""

		# match class AtomicComponent(layer3rule3class3AtomicComponent) node
		self.add_node()
		self.vs[6]["mm__"] = """AtomicComponent"""
		self.vs[6]["attr1"] = """+"""

		# match class ProvidedPort(layer3rule3class4ProvidedPort) node
		self.add_node()
		self.vs[7]["mm__"] = """ProvidedPort"""
		self.vs[7]["attr1"] = """+"""

		# match class ClientServerInterface(layer3rule3class5ClientServerInterface) node
		self.add_node()
		self.vs[8]["mm__"] = """ClientServerInterface"""
		self.vs[8]["attr1"] = """+"""

		# apply class ImplementationModule(layer3rule3class6ImplementationModule) node
		self.add_node()
		self.vs[9]["mm__"] = """ImplementationModule"""
		self.vs[9]["attr1"] = """1"""

		# apply class GlobalVariableDeclaration(layer3rule3class7GlobalVariableDeclaration) node
		self.add_node()
		self.vs[10]["mm__"] = """GlobalVariableDeclaration"""
		self.vs[10]["attr1"] = """1"""

		# apply class TypeDef(layer3rule3class8TypeDef) node
		self.add_node()
		self.vs[11]["mm__"] = """TypeDef"""
		self.vs[11]["attr1"] = """1"""

		# apply class TypeDefType(layer3rule3class9TypeDefType) node
		self.add_node()
		self.vs[12]["mm__"] = """TypeDefType"""
		self.vs[12]["attr1"] = """1"""

		# match association ImplementationModule--contents-->InstanceConfiguration node 
		self.add_node()
		self.vs[13]["attr1"] = """contents"""
		self.vs[13]["mm__"] = """directLink_S"""

		# match association InstanceConfiguration--contents-->ComponentInstance node 
		self.add_node()
		self.vs[14]["attr1"] = """contents"""
		self.vs[14]["mm__"] = """directLink_S"""

		# match association ComponentInstance--component-->AtomicComponent node 
		self.add_node()
		self.vs[15]["attr1"] = """component"""
		self.vs[15]["mm__"] = """directLink_S"""

		# match association AtomicComponent--contents-->ProvidedPort node 
		self.add_node()
		self.vs[16]["attr1"] = """contents"""
		self.vs[16]["mm__"] = """directLink_S"""

		# match association ProvidedPort--intf-->ClientServerInterface node 
		self.add_node()
		self.vs[17]["attr1"] = """intf"""
		self.vs[17]["mm__"] = """directLink_S"""

		# apply association ImplementationModule--contents-->GlobalVariableDeclaration node 
		self.add_node()
		self.vs[18]["attr1"] = """contents"""
		self.vs[18]["mm__"] = """directLink_T"""

		# apply association GlobalVariableDeclaration--type-->TypeDefType node 
		self.add_node()
		self.vs[19]["attr1"] = """type"""
		self.vs[19]["mm__"] = """directLink_T"""

		# apply association TypeDefType--typeDef-->TypeDef node 
		self.add_node()
		self.vs[20]["attr1"] = """typeDef"""
		self.vs[20]["mm__"] = """directLink_T"""

		# backward association ImplementationModule-->ImplementationModulenode 
		self.add_node()
		self.vs[21]["mm__"] = """backward_link"""

		# backward association TypeDef-->ClientServerInterfacenode 
		self.add_node()
		self.vs[22]["mm__"] = """backward_link"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class ImplementationModule(layer3rule3class0ImplementationModule)
			(0,4), # matchmodel -> match_class InstanceConfiguration(layer3rule3class1InstanceConfiguration)
			(0,5), # matchmodel -> match_class ComponentInstance(layer3rule3class2ComponentInstance)
			(0,6), # matchmodel -> match_class AtomicComponent(layer3rule3class3AtomicComponent)
			(0,7), # matchmodel -> match_class ProvidedPort(layer3rule3class4ProvidedPort)
			(0,8), # matchmodel -> match_class ClientServerInterface(layer3rule3class5ClientServerInterface)
			(1,9), # applymodel -> apply_classImplementationModule(layer3rule3class6ImplementationModule)
			(1,10), # applymodel -> apply_classGlobalVariableDeclaration(layer3rule3class7GlobalVariableDeclaration)
			(1,11), # applymodel -> apply_classTypeDef(layer3rule3class8TypeDef)
			(1,12), # applymodel -> apply_classTypeDefType(layer3rule3class9TypeDefType)
			(3,13), # match classImplementationModule(layer3rule3class0ImplementationModule) -> association contents
			(13,4), # associationcontents -> match_classImplementationModule(layer3rule3class1InstanceConfiguration)
			(4,14), # match classInstanceConfiguration(layer3rule3class1InstanceConfiguration) -> association contents
			(14,5), # associationcontents -> match_classInstanceConfiguration(layer3rule3class2ComponentInstance)
			(5,15), # match classComponentInstance(layer3rule3class2ComponentInstance) -> association component
			(15,6), # associationcomponent -> match_classComponentInstance(layer3rule3class3AtomicComponent)
			(6,16), # match classAtomicComponent(layer3rule3class3AtomicComponent) -> association contents
			(16,7), # associationcontents -> match_classAtomicComponent(layer3rule3class4ProvidedPort)
			(7,17), # match classProvidedPort(layer3rule3class4ProvidedPort) -> association intf
			(17,8), # associationintf -> match_classProvidedPort(layer3rule3class5ClientServerInterface)
			(9,18), # apply class ImplementationModule(layer3rule3class6ImplementationModule) -> association contents
			(18,10), # associationcontents -> apply_classGlobalVariableDeclaration(layer3rule3class7GlobalVariableDeclaration)
			(10,19), # apply class GlobalVariableDeclaration(layer3rule3class7GlobalVariableDeclaration) -> association type
			(19,12), # associationtype -> apply_classTypeDefType(layer3rule3class9TypeDefType)
			(12,20), # apply class TypeDefType(layer3rule3class9TypeDefType) -> association typeDef
			(20,11), # associationtypeDef -> apply_classTypeDef(layer3rule3class8TypeDef)
			(9,21), # apply class ImplementationModule(layer3rule3class0ImplementationModule) -> backward_association 
			(21,3), # backward_associationImplementationModule -> match_class ImplementationModule(layer3rule3class0ImplementationModule)
			(11,22), # apply class TypeDef(layer3rule3class5ClientServerInterface) -> backward_association 
			(22,8), # backward_associationClientServerInterface -> match_class ClientServerInterface(layer3rule3class5ClientServerInterface)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = [((10,'name'),('concat',((3,'name'),('concat',(('constant','_'),('concat',((5,'name'),('concat',(('constant','_'),('concat',((8,'name'),('constant','__ops')))))))))))),]
