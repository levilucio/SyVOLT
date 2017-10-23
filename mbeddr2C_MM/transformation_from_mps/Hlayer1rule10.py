from core.himesis import Himesis
import uuid

class Hlayer1rule10(Himesis):
	def __init__(self):
		"""
		Creates the himesis graph representing the DSLTrans rule layer1rule10.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(Hlayer1rule10, self).__init__(name='Hlayer1rule10', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """layer1rule10"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule10')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """layer1rule10"""

		# match class AtomicComponent(layer1rule10class0AtomicComponent) node
		self.add_node()
		self.vs[3]["mm__"] = """AtomicComponent"""
		self.vs[3]["attr1"] = """+"""

		# match class RequiredPort(layer1rule10class1RequiredPort) node
		self.add_node()
		self.vs[4]["mm__"] = """RequiredPort"""
		self.vs[4]["attr1"] = """+"""

		# apply class StructDeclaration(layer1rule10class2StructDeclaration) node
		self.add_node()
		self.vs[5]["mm__"] = """StructDeclaration"""
		self.vs[5]["attr1"] = """1"""

		# apply class Member(layer1rule10class3Member) node
		self.add_node()
		self.vs[6]["mm__"] = """Member"""
		self.vs[6]["attr1"] = """1"""

		# apply class Member(layer1rule10class4Member) node
		self.add_node()
		self.vs[7]["mm__"] = """Member"""
		self.vs[7]["attr1"] = """1"""

		# match association AtomicComponent--contents-->RequiredPort node 
		self.add_node()
		self.vs[8]["attr1"] = """contents"""
		self.vs[8]["mm__"] = """directLink_S"""

		# apply association StructDeclaration--members-->Member node 
		self.add_node()
		self.vs[9]["attr1"] = """members"""
		self.vs[9]["mm__"] = """directLink_T"""

		# apply association StructDeclaration--members-->Member node 
		self.add_node()
		self.vs[10]["attr1"] = """members"""
		self.vs[10]["mm__"] = """directLink_T"""

		# backward association StructDeclaration-->AtomicComponentnode 
		self.add_node()
		self.vs[11]["mm__"] = """backward_link"""

		# backward association Member-->RequiredPortnode 
		self.add_node()
		self.vs[12]["mm__"] = """backward_link"""

		# backward association Member-->RequiredPortnode 
		self.add_node()
		self.vs[13]["mm__"] = """backward_link"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class AtomicComponent(layer1rule10class0AtomicComponent)
			(0,4), # matchmodel -> match_class RequiredPort(layer1rule10class1RequiredPort)
			(1,5), # applymodel -> apply_classStructDeclaration(layer1rule10class2StructDeclaration)
			(1,6), # applymodel -> apply_classMember(layer1rule10class3Member)
			(1,7), # applymodel -> apply_classMember(layer1rule10class4Member)
			(3,8), # match classAtomicComponent(layer1rule10class0AtomicComponent) -> association contents
			(8,4), # associationcontents -> match_classAtomicComponent(layer1rule10class1RequiredPort)
			(5,9), # apply class StructDeclaration(layer1rule10class2StructDeclaration) -> association members
			(9,6), # associationmembers -> apply_classMember(layer1rule10class3Member)
			(5,10), # apply class StructDeclaration(layer1rule10class2StructDeclaration) -> association members
			(10,7), # associationmembers -> apply_classMember(layer1rule10class4Member)
			(5,11), # apply class StructDeclaration(layer1rule10class0AtomicComponent) -> backward_association 
			(11,3), # backward_associationAtomicComponent -> match_class AtomicComponent(layer1rule10class0AtomicComponent)
			(6,12), # apply class Member(layer1rule10class1RequiredPort) -> backward_association 
			(12,4), # backward_associationRequiredPort -> match_class RequiredPort(layer1rule10class1RequiredPort)
			(7,13), # apply class Member(layer1rule10class1RequiredPort) -> backward_association 
			(13,4), # backward_associationRequiredPort -> match_class RequiredPort(layer1rule10class1RequiredPort)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = []
