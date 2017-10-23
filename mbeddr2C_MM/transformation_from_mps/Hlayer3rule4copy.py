from core.himesis import Himesis
import uuid

class Hlayer3rule4copy(Himesis):
	def __init__(self):
		"""
		Creates the himesis graph representing the DSLTrans rule layer3rule4copy.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(Hlayer3rule4copy, self).__init__(name='Hlayer3rule4copy', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """layer3rule4copy"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule4copy')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """layer3rule4copy"""

		# match class ImplementationModule(4.6.m.0ImplementationModule) node
		self.add_node()
		self.vs[3]["mm__"] = """ImplementationModule"""
		self.vs[3]["attr1"] = """+"""

		# match class InstanceConfiguration(4.6.m.1InstanceConfiguration) node
		self.add_node()
		self.vs[4]["mm__"] = """InstanceConfiguration"""
		self.vs[4]["attr1"] = """+"""

		# match class ComponentInstance(4.6.m.2ComponentInstance) node
		self.add_node()
		self.vs[5]["mm__"] = """ComponentInstance"""
		self.vs[5]["attr1"] = """+"""

		# match class AtomicComponent(4.6.m.3AtomicComponent) node
		self.add_node()
		self.vs[6]["mm__"] = """AtomicComponent"""
		self.vs[6]["attr1"] = """+"""

		# apply class ImplementationModule(4.6.a.0ImplementationModule) node
		self.add_node()
		self.vs[7]["mm__"] = """ImplementationModule"""
		self.vs[7]["attr1"] = """1"""

		# apply class GlobalVariableDeclaration(4.6.a.1GlobalVariableDeclaration) node
		self.add_node()
		self.vs[8]["mm__"] = """GlobalVariableDeclaration"""
		self.vs[8]["attr1"] = """1"""

		# apply class TypeDef(4.6.a.2TypeDef) node
		self.add_node()
		self.vs[9]["mm__"] = """TypeDef"""
		self.vs[9]["attr1"] = """1"""

		# apply class TypeDefType(4.6.a.3TypeDefType) node
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

		# apply association TypeDefType--typeDef-->TypeDef node 
		self.add_node()
		self.vs[14]["attr1"] = """typeDef"""
		self.vs[14]["mm__"] = """directLink_T"""

		# apply association GlobalVariableDeclaration--type-->TypeDefType node 
		self.add_node()
		self.vs[15]["attr1"] = """type"""
		self.vs[15]["mm__"] = """directLink_T"""

		# apply association ImplementationModule--contents-->GlobalVariableDeclaration node 
		self.add_node()
		self.vs[16]["attr1"] = """contents"""
		self.vs[16]["mm__"] = """directLink_T"""

		# backward association ImplementationModule-->ImplementationModulenode 
		self.add_node()
		self.vs[17]["mm__"] = """backward_link"""

		# backward association TypeDef-->AtomicComponentnode 
		self.add_node()
		self.vs[18]["mm__"] = """backward_link"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class ImplementationModule(4.6.m.0ImplementationModule)
			(0,4), # matchmodel -> match_class InstanceConfiguration(4.6.m.1InstanceConfiguration)
			(0,5), # matchmodel -> match_class ComponentInstance(4.6.m.2ComponentInstance)
			(0,6), # matchmodel -> match_class AtomicComponent(4.6.m.3AtomicComponent)
			(1,7), # applymodel -> apply_classImplementationModule(4.6.a.0ImplementationModule)
			(1,8), # applymodel -> apply_classGlobalVariableDeclaration(4.6.a.1GlobalVariableDeclaration)
			(1,9), # applymodel -> apply_classTypeDef(4.6.a.2TypeDef)
			(1,10), # applymodel -> apply_classTypeDefType(4.6.a.3TypeDefType)
			(3,11), # match classImplementationModule(4.6.m.0ImplementationModule) -> association contents
			(11,4), # associationcontents -> match_classImplementationModule(4.6.m.1InstanceConfiguration)
			(4,12), # match classInstanceConfiguration(4.6.m.1InstanceConfiguration) -> association contents
			(12,5), # associationcontents -> match_classInstanceConfiguration(4.6.m.2ComponentInstance)
			(5,13), # match classComponentInstance(4.6.m.2ComponentInstance) -> association component
			(13,6), # associationcomponent -> match_classComponentInstance(4.6.m.3AtomicComponent)
			(10,14), # apply class TypeDefType(4.6.a.3TypeDefType) -> association typeDef
			(14,9), # associationtypeDef -> apply_classTypeDef(4.6.a.2TypeDef)
			(8,15), # apply class GlobalVariableDeclaration(4.6.a.1GlobalVariableDeclaration) -> association type
			(15,10), # associationtype -> apply_classTypeDefType(4.6.a.3TypeDefType)
			(7,16), # apply class ImplementationModule(4.6.a.0ImplementationModule) -> association contents
			(16,8), # associationcontents -> apply_classGlobalVariableDeclaration(4.6.a.1GlobalVariableDeclaration)
			(7,17), # apply class ImplementationModule(4.6.m.0ImplementationModule) -> backward_association 
			(17,3), # backward_associationImplementationModule -> match_class ImplementationModule(4.6.m.0ImplementationModule)
			(9,18), # apply class TypeDef(4.6.m.3AtomicComponent) -> backward_association 
			(18,6), # backward_associationAtomicComponent -> match_class AtomicComponent(4.6.m.3AtomicComponent)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = [((8,'name'),('concat',((3,'name'),('constant','_instance')))),]
