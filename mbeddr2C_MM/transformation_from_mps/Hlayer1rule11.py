from core.himesis import Himesis
import uuid

class Hlayer1rule11(Himesis):
	def __init__(self):
		"""
		Creates the himesis graph representing the DSLTrans rule layer1rule11.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(Hlayer1rule11, self).__init__(name='Hlayer1rule11', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """layer1rule11"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule11')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """layer1rule11"""

		# match class ClientServerInterface(layer1rule11class0ClientServerInterface) node
		self.add_node()
		self.vs[3]["mm__"] = """ClientServerInterface"""
		self.vs[3]["attr1"] = """+"""

		# match class RequiredPort(layer1rule11class1RequiredPort) node
		self.add_node()
		self.vs[4]["mm__"] = """RequiredPort"""
		self.vs[4]["attr1"] = """+"""

		# apply class TypeDef(layer1rule11class2TypeDef) node
		self.add_node()
		self.vs[5]["mm__"] = """TypeDef"""
		self.vs[5]["attr1"] = """1"""

		# apply class Member(layer1rule11class3Member) node
		self.add_node()
		self.vs[6]["mm__"] = """Member"""
		self.vs[6]["attr1"] = """1"""

		# apply class PointerType(layer1rule11class4PointerType) node
		self.add_node()
		self.vs[7]["mm__"] = """PointerType"""
		self.vs[7]["attr1"] = """1"""

		# apply class TypeDefType(layer1rule11class5TypeDefType) node
		self.add_node()
		self.vs[8]["mm__"] = """TypeDefType"""
		self.vs[8]["attr1"] = """1"""

		# match association RequiredPort--intf-->ClientServerInterface node 
		self.add_node()
		self.vs[9]["attr1"] = """intf"""
		self.vs[9]["mm__"] = """directLink_S"""

		# apply association Member--type-->PointerType node 
		self.add_node()
		self.vs[10]["attr1"] = """type"""
		self.vs[10]["mm__"] = """directLink_T"""

		# apply association PointerType--baseType-->TypeDefType node 
		self.add_node()
		self.vs[11]["attr1"] = """baseType"""
		self.vs[11]["mm__"] = """directLink_T"""

		# apply association TypeDefType--typeDef-->TypeDef node 
		self.add_node()
		self.vs[12]["attr1"] = """typeDef"""
		self.vs[12]["mm__"] = """directLink_T"""

		# backward association TypeDef-->ClientServerInterfacenode 
		self.add_node()
		self.vs[13]["mm__"] = """backward_link"""

		# backward association Member-->RequiredPortnode 
		self.add_node()
		self.vs[14]["mm__"] = """backward_link"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class ClientServerInterface(layer1rule11class0ClientServerInterface)
			(0,4), # matchmodel -> match_class RequiredPort(layer1rule11class1RequiredPort)
			(1,5), # applymodel -> apply_classTypeDef(layer1rule11class2TypeDef)
			(1,6), # applymodel -> apply_classMember(layer1rule11class3Member)
			(1,7), # applymodel -> apply_classPointerType(layer1rule11class4PointerType)
			(1,8), # applymodel -> apply_classTypeDefType(layer1rule11class5TypeDefType)
			(4,9), # match classRequiredPort(layer1rule11class1RequiredPort) -> association intf
			(9,3), # associationintf -> match_classRequiredPort(layer1rule11class0ClientServerInterface)
			(6,10), # apply class Member(layer1rule11class3Member) -> association type
			(10,7), # associationtype -> apply_classPointerType(layer1rule11class4PointerType)
			(7,11), # apply class PointerType(layer1rule11class4PointerType) -> association baseType
			(11,8), # associationbaseType -> apply_classTypeDefType(layer1rule11class5TypeDefType)
			(8,12), # apply class TypeDefType(layer1rule11class5TypeDefType) -> association typeDef
			(12,5), # associationtypeDef -> apply_classTypeDef(layer1rule11class2TypeDef)
			(5,13), # apply class TypeDef(layer1rule11class0ClientServerInterface) -> backward_association 
			(13,3), # backward_associationClientServerInterface -> match_class ClientServerInterface(layer1rule11class0ClientServerInterface)
			(6,14), # apply class Member(layer1rule11class1RequiredPort) -> backward_association 
			(14,4), # backward_associationRequiredPort -> match_class RequiredPort(layer1rule11class1RequiredPort)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = []
