from core.himesis import Himesis
import uuid

class Hlayer0rule11(Himesis):
	def __init__(self):
		"""
		Creates the himesis graph representing the DSLTrans rule layer0rule11.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(Hlayer0rule11, self).__init__(name='Hlayer0rule11', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """layer0rule11"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule11')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """layer0rule11"""

		# match class ProvidedPort(layer0rule11class0ProvidedPort) node
		self.add_node()
		self.vs[3]["mm__"] = """ProvidedPort"""
		self.vs[3]["attr1"] = """+"""

		# match class AtomicComponent(layer0rule11class1AtomicComponent) node
		self.add_node()
		self.vs[4]["mm__"] = """AtomicComponent"""
		self.vs[4]["attr1"] = """+"""

		# match class ClientServerInterface(layer0rule11class2ClientServerInterface) node
		self.add_node()
		self.vs[5]["mm__"] = """ClientServerInterface"""
		self.vs[5]["attr1"] = """+"""

		# match class Operation(layer0rule11class3Operation) node
		self.add_node()
		self.vs[6]["mm__"] = """Operation"""
		self.vs[6]["attr1"] = """+"""

		# match class ImplementationModule(layer0rule11class4ImplementationModule) node
		self.add_node()
		self.vs[7]["mm__"] = """ImplementationModule"""
		self.vs[7]["attr1"] = """+"""

		# apply class FunctionPrototype(layer0rule11class5FunctionPrototype) node
		self.add_node()
		self.vs[8]["mm__"] = """FunctionPrototype"""
		self.vs[8]["attr1"] = """1"""

		# match association AtomicComponent--contents-->ProvidedPort node 
		self.add_node()
		self.vs[9]["attr1"] = """contents"""
		self.vs[9]["mm__"] = """directLink_S"""

		# match association ProvidedPort--intf-->ClientServerInterface node 
		self.add_node()
		self.vs[10]["attr1"] = """intf"""
		self.vs[10]["mm__"] = """directLink_S"""

		# match association ClientServerInterface--contents-->Operation node 
		self.add_node()
		self.vs[11]["attr1"] = """contents"""
		self.vs[11]["mm__"] = """directLink_S"""

		# match association ImplementationModule--contents-->AtomicComponent node 
		self.add_node()
		self.vs[12]["attr1"] = """contents"""
		self.vs[12]["mm__"] = """directLink_S"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class ProvidedPort(layer0rule11class0ProvidedPort)
			(0,4), # matchmodel -> match_class AtomicComponent(layer0rule11class1AtomicComponent)
			(0,5), # matchmodel -> match_class ClientServerInterface(layer0rule11class2ClientServerInterface)
			(0,6), # matchmodel -> match_class Operation(layer0rule11class3Operation)
			(0,7), # matchmodel -> match_class ImplementationModule(layer0rule11class4ImplementationModule)
			(1,8), # applymodel -> apply_classFunctionPrototype(layer0rule11class5FunctionPrototype)
			(4,9), # match classAtomicComponent(layer0rule11class1AtomicComponent) -> association contents
			(9,3), # associationcontents -> match_classAtomicComponent(layer0rule11class0ProvidedPort)
			(3,10), # match classProvidedPort(layer0rule11class0ProvidedPort) -> association intf
			(10,5), # associationintf -> match_classProvidedPort(layer0rule11class2ClientServerInterface)
			(5,11), # match classClientServerInterface(layer0rule11class2ClientServerInterface) -> association contents
			(11,6), # associationcontents -> match_classClientServerInterface(layer0rule11class3Operation)
			(7,12), # match classImplementationModule(layer0rule11class4ImplementationModule) -> association contents
			(12,4), # associationcontents -> match_classImplementationModule(layer0rule11class1AtomicComponent)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = [((8,'name'),('concat',((7,'name'),('concat',(('constant','_'),('concat',((4,'name'),('concat',(('constant','_'),('concat',((3,'name'),('concat',(('constant','_'),(6,'name')))))))))))))),]
