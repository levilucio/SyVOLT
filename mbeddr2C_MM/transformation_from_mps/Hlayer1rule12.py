from core.himesis import Himesis
import uuid

class Hlayer1rule12(Himesis):
	def __init__(self):
		"""
		Creates the himesis graph representing the DSLTrans rule layer1rule12.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(Hlayer1rule12, self).__init__(name='Hlayer1rule12', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """layer1rule12"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule12')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """layer1rule12"""

		# match class ImplementationModule(layer1rule12class0ImplementationModule) node
		self.add_node()
		self.vs[3]["mm__"] = """ImplementationModule"""
		self.vs[3]["attr1"] = """+"""

		# match class AtomicComponent(AtomicComponent) node
		self.add_node()
		self.vs[4]["mm__"] = """AtomicComponent"""
		self.vs[4]["attr1"] = """+"""

		# match class ProvidedPort(ProvidedPort) node
		self.add_node()
		self.vs[5]["mm__"] = """ProvidedPort"""
		self.vs[5]["attr1"] = """+"""

		# match class ClientServerInterface(ClientServerInterface) node
		self.add_node()
		self.vs[6]["mm__"] = """ClientServerInterface"""
		self.vs[6]["attr1"] = """+"""

		# match class Operation(Operation) node
		self.add_node()
		self.vs[7]["mm__"] = """Operation"""
		self.vs[7]["attr1"] = """+"""

		# apply class ImplementationModule(layer1rule12class1ImplementationModule) node
		self.add_node()
		self.vs[8]["mm__"] = """ImplementationModule"""
		self.vs[8]["attr1"] = """1"""

		# apply class FunctionPrototype(layer1rule12class2FunctionPrototype) node
		self.add_node()
		self.vs[9]["mm__"] = """FunctionPrototype"""
		self.vs[9]["attr1"] = """1"""

		# match association ImplementationModule--contents-->AtomicComponent node 
		self.add_node()
		self.vs[10]["attr1"] = """contents"""
		self.vs[10]["mm__"] = """directLink_S"""

		# match association AtomicComponent--contents-->ProvidedPort node 
		self.add_node()
		self.vs[11]["attr1"] = """contents"""
		self.vs[11]["mm__"] = """directLink_S"""

		# match association ProvidedPort--intf-->ClientServerInterface node 
		self.add_node()
		self.vs[12]["attr1"] = """intf"""
		self.vs[12]["mm__"] = """directLink_S"""

		# match association ClientServerInterface--contents-->Operation node 
		self.add_node()
		self.vs[13]["attr1"] = """contents"""
		self.vs[13]["mm__"] = """directLink_S"""

		# apply association ImplementationModule--contents-->FunctionPrototype node 
		self.add_node()
		self.vs[14]["attr1"] = """contents"""
		self.vs[14]["mm__"] = """directLink_T"""

		# backward association ImplementationModule-->ImplementationModulenode 
		self.add_node()
		self.vs[15]["mm__"] = """backward_link"""

		# backward association FunctionPrototype-->Operationnode 
		self.add_node()
		self.vs[16]["mm__"] = """backward_link"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class ImplementationModule(layer1rule12class0ImplementationModule)
			(0,4), # matchmodel -> match_class AtomicComponent(AtomicComponent)
			(0,5), # matchmodel -> match_class ProvidedPort(ProvidedPort)
			(0,6), # matchmodel -> match_class ClientServerInterface(ClientServerInterface)
			(0,7), # matchmodel -> match_class Operation(Operation)
			(1,8), # applymodel -> apply_classImplementationModule(layer1rule12class1ImplementationModule)
			(1,9), # applymodel -> apply_classFunctionPrototype(layer1rule12class2FunctionPrototype)
			(3,10), # match classImplementationModule(layer1rule12class0ImplementationModule) -> association contents
			(10,4), # associationcontents -> match_classImplementationModule(AtomicComponent)
			(4,11), # match classAtomicComponent(AtomicComponent) -> association contents
			(11,5), # associationcontents -> match_classAtomicComponent(ProvidedPort)
			(5,12), # match classProvidedPort(ProvidedPort) -> association intf
			(12,6), # associationintf -> match_classProvidedPort(ClientServerInterface)
			(6,13), # match classClientServerInterface(ClientServerInterface) -> association contents
			(13,7), # associationcontents -> match_classClientServerInterface(Operation)
			(8,14), # apply class ImplementationModule(layer1rule12class1ImplementationModule) -> association contents
			(14,9), # associationcontents -> apply_classFunctionPrototype(layer1rule12class2FunctionPrototype)
			(8,15), # apply class ImplementationModule(layer1rule12class0ImplementationModule) -> backward_association 
			(15,3), # backward_associationImplementationModule -> match_class ImplementationModule(layer1rule12class0ImplementationModule)
			(9,16), # apply class FunctionPrototype(Operation) -> backward_association 
			(16,7), # backward_associationOperation -> match_class Operation(Operation)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = []
