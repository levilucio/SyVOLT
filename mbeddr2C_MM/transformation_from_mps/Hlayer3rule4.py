from core.himesis import Himesis
import uuid

class Hlayer3rule4(Himesis):
	def __init__(self):
		"""
		Creates the himesis graph representing the DSLTrans rule layer3rule4.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(Hlayer3rule4, self).__init__(name='Hlayer3rule4', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """layer3rule4"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule4')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """layer3rule4"""

		# match class ImplementationModule(layer3rule4class0ImplementationModule) node
		self.add_node()
		self.vs[3]["mm__"] = """ImplementationModule"""
		self.vs[3]["attr1"] = """+"""

		# match class InstanceConfiguration(layer3rule4class1InstanceConfiguration) node
		self.add_node()
		self.vs[4]["mm__"] = """InstanceConfiguration"""
		self.vs[4]["attr1"] = """+"""

		# match class ComponentInstance(layer3rule4class2ComponentInstance) node
		self.add_node()
		self.vs[5]["mm__"] = """ComponentInstance"""
		self.vs[5]["attr1"] = """+"""

		# match class AtomicComponent(layer3rule4class3AtomicComponent) node
		self.add_node()
		self.vs[6]["mm__"] = """AtomicComponent"""
		self.vs[6]["attr1"] = """+"""

		# apply class ImplementationModule(layer3rule4class4ImplementationModule) node
		self.add_node()
		self.vs[7]["mm__"] = """ImplementationModule"""
		self.vs[7]["attr1"] = """1"""

		# apply class GlobalVariableDeclaration(layer3rule4class5GlobalVariableDeclaration) node
		self.add_node()
		self.vs[8]["mm__"] = """GlobalVariableDeclaration"""
		self.vs[8]["attr1"] = """1"""

		# apply class TypeDef(layer3rule4class6TypeDef) node
		self.add_node()
		self.vs[9]["mm__"] = """TypeDef"""
		self.vs[9]["attr1"] = """1"""

		# apply class TypeDefType(layer3rule4class7TypeDefType) node
		self.add_node()
		self.vs[10]["mm__"] = """TypeDefType"""
		self.vs[10]["attr1"] = """1"""

		# match association ImplementationModule--contents-->InstanceConfiguration node 
		self.add_node()
		self.vs[11]["attr1"] = """contents"""
		self.vs[11]["mm__"] = """directLink_S"""

		# match association InstanceConfiguration--contents-->ComponentInstance node 
		self.add_node()
		self.vs[12]["attr1"] = """contents"""
		self.vs[12]["mm__"] = """directLink_S"""

		# match association ComponentInstance--component-->AtomicComponent node 
		self.add_node()
		self.vs[13]["attr1"] = """component"""
		self.vs[13]["mm__"] = """directLink_S"""

		# apply association ImplementationModule--contents-->GlobalVariableDeclaration node 
		self.add_node()
		self.vs[14]["attr1"] = """contents"""
		self.vs[14]["mm__"] = """directLink_T"""

		# apply association GlobalVariableDeclaration--type-->TypeDefType node 
		self.add_node()
		self.vs[15]["attr1"] = """type"""
		self.vs[15]["mm__"] = """directLink_T"""

		# apply association TypeDefType--typeDef-->TypeDef node 
		self.add_node()
		self.vs[16]["attr1"] = """typeDef"""
		self.vs[16]["mm__"] = """directLink_T"""

		# backward association ImplementationModule-->ImplementationModulenode 
		self.add_node()
		self.vs[17]["mm__"] = """backward_link"""

		# backward association TypeDef-->AtomicComponentnode 
		self.add_node()
		self.vs[18]["mm__"] = """backward_link"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class ImplementationModule(layer3rule4class0ImplementationModule)
			(0,4), # matchmodel -> match_class InstanceConfiguration(layer3rule4class1InstanceConfiguration)
			(0,5), # matchmodel -> match_class ComponentInstance(layer3rule4class2ComponentInstance)
			(0,6), # matchmodel -> match_class AtomicComponent(layer3rule4class3AtomicComponent)
			(1,7), # applymodel -> apply_classImplementationModule(layer3rule4class4ImplementationModule)
			(1,8), # applymodel -> apply_classGlobalVariableDeclaration(layer3rule4class5GlobalVariableDeclaration)
			(1,9), # applymodel -> apply_classTypeDef(layer3rule4class6TypeDef)
			(1,10), # applymodel -> apply_classTypeDefType(layer3rule4class7TypeDefType)
			(3,11), # match classImplementationModule(layer3rule4class0ImplementationModule) -> association contents
			(11,4), # associationcontents -> match_classImplementationModule(layer3rule4class1InstanceConfiguration)
			(4,12), # match classInstanceConfiguration(layer3rule4class1InstanceConfiguration) -> association contents
			(12,5), # associationcontents -> match_classInstanceConfiguration(layer3rule4class2ComponentInstance)
			(5,13), # match classComponentInstance(layer3rule4class2ComponentInstance) -> association component
			(13,6), # associationcomponent -> match_classComponentInstance(layer3rule4class3AtomicComponent)
			(7,14), # apply class ImplementationModule(layer3rule4class4ImplementationModule) -> association contents
			(14,8), # associationcontents -> apply_classGlobalVariableDeclaration(layer3rule4class5GlobalVariableDeclaration)
			(8,15), # apply class GlobalVariableDeclaration(layer3rule4class5GlobalVariableDeclaration) -> association type
			(15,10), # associationtype -> apply_classTypeDefType(layer3rule4class7TypeDefType)
			(10,16), # apply class TypeDefType(layer3rule4class7TypeDefType) -> association typeDef
			(16,9), # associationtypeDef -> apply_classTypeDef(layer3rule4class6TypeDef)
			(7,17), # apply class ImplementationModule(layer3rule4class0ImplementationModule) -> backward_association 
			(17,3), # backward_associationImplementationModule -> match_class ImplementationModule(layer3rule4class0ImplementationModule)
			(9,18), # apply class TypeDef(layer3rule4class3AtomicComponent) -> backward_association 
			(18,6), # backward_associationAtomicComponent -> match_class AtomicComponent(layer3rule4class3AtomicComponent)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = [((8,'name'),('concat',((3,'name'),('concat',(('constant','_'),('concat',((4,'name'),('concat',(('constant','_'),('concat',((5,'name'),('constant','__instance')))))))))))),]
