from core.himesis import Himesis
import uuid

class Hlayer1rule6(Himesis):
	def __init__(self):
		"""
		Creates the himesis graph representing the DSLTrans rule layer1rule6.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(Hlayer1rule6, self).__init__(name='Hlayer1rule6', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """layer1rule6"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule6')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """layer1rule6"""

		# match class ClientServerInterface(layer1rule6class0ClientServerInterface) node
		self.add_node()
		self.vs[3]["mm__"] = """ClientServerInterface"""
		self.vs[3]["attr1"] = """+"""

		# match class ImplementationModule(layer1rule6class5ImplementationModule) node
		self.add_node()
		self.vs[4]["mm__"] = """ImplementationModule"""
		self.vs[4]["attr1"] = """+"""

		# apply class StructDeclaration(layer1rule6class1StructDeclaration) node
		self.add_node()
		self.vs[5]["mm__"] = """StructDeclaration"""
		self.vs[5]["attr1"] = """1"""

		# apply class StructType(layer1rule6class2StructType) node
		self.add_node()
		self.vs[6]["mm__"] = """StructType"""
		self.vs[6]["attr1"] = """1"""

		# match association ImplementationModule--contents-->ClientServerInterface node 
		self.add_node()
		self.vs[7]["attr1"] = """contents"""
		self.vs[7]["mm__"] = """directLink_S"""

		# apply association StructType--struct-->StructDeclaration node 
		self.add_node()
		self.vs[8]["attr1"] = """struct"""
		self.vs[8]["mm__"] = """directLink_T"""

		# backward association StructType-->ImplementationModulenode 
		self.add_node()
		self.vs[9]["mm__"] = """backward_link"""

		# backward association StructDeclaration-->ClientServerInterfacenode 
		self.add_node()
		self.vs[10]["mm__"] = """backward_link"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class ClientServerInterface(layer1rule6class0ClientServerInterface)
			(0,4), # matchmodel -> match_class ImplementationModule(layer1rule6class5ImplementationModule)
			(1,5), # applymodel -> apply_classStructDeclaration(layer1rule6class1StructDeclaration)
			(1,6), # applymodel -> apply_classStructType(layer1rule6class2StructType)
			(4,7), # match classImplementationModule(layer1rule6class5ImplementationModule) -> association contents
			(7,3), # associationcontents -> match_classImplementationModule(layer1rule6class0ClientServerInterface)
			(6,8), # apply class StructType(layer1rule6class2StructType) -> association struct
			(8,5), # associationstruct -> apply_classStructDeclaration(layer1rule6class1StructDeclaration)
			(6,9), # apply class StructType(layer1rule6class5ImplementationModule) -> backward_association 
			(9,4), # backward_associationImplementationModule -> match_class ImplementationModule(layer1rule6class5ImplementationModule)
			(5,10), # apply class StructDeclaration(layer1rule6class0ClientServerInterface) -> backward_association 
			(10,3), # backward_associationClientServerInterface -> match_class ClientServerInterface(layer1rule6class0ClientServerInterface)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = []
