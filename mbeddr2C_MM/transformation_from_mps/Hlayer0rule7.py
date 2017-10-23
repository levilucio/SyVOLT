from core.himesis import Himesis
import uuid

class Hlayer0rule7(Himesis):
	def __init__(self):
		"""
		Creates the himesis graph representing the DSLTrans rule layer0rule7.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(Hlayer0rule7, self).__init__(name='Hlayer0rule7', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """layer0rule7"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule7')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """layer0rule7"""

		# match class AtomicComponent(layer0rule7class0AtomicComponent) node
		self.add_node()
		self.vs[3]["mm__"] = """AtomicComponent"""
		self.vs[3]["attr1"] = """+"""

		# match class ImplementationModule(layer0rule7class1ImplementationModule) node
		self.add_node()
		self.vs[4]["mm__"] = """ImplementationModule"""
		self.vs[4]["attr1"] = """+"""

		# apply class StructDeclaration(layer0rule7class2StructDeclaration) node
		self.add_node()
		self.vs[5]["mm__"] = """StructDeclaration"""
		self.vs[5]["attr1"] = """1"""

		# apply class Member(layer0rule7class3Member) node
		self.add_node()
		self.vs[6]["mm__"] = """Member"""
		self.vs[6]["attr1"] = """1"""

		# apply class Int32Type(layer0rule7class4Int32Type) node
		self.add_node()
		self.vs[7]["mm__"] = """Int32Type"""
		self.vs[7]["attr1"] = """1"""

		# match association ImplementationModule--contents-->AtomicComponent node 
		self.add_node()
		self.vs[8]["attr1"] = """contents"""
		self.vs[8]["mm__"] = """directLink_S"""

		# apply association StructDeclaration--members-->Member node 
		self.add_node()
		self.vs[9]["attr1"] = """members"""
		self.vs[9]["mm__"] = """directLink_T"""

		# apply association Member--type-->Int32Type node 
		self.add_node()
		self.vs[10]["attr1"] = """type"""
		self.vs[10]["mm__"] = """directLink_T"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class AtomicComponent(layer0rule7class0AtomicComponent)
			(0,4), # matchmodel -> match_class ImplementationModule(layer0rule7class1ImplementationModule)
			(1,5), # applymodel -> apply_classStructDeclaration(layer0rule7class2StructDeclaration)
			(1,6), # applymodel -> apply_classMember(layer0rule7class3Member)
			(1,7), # applymodel -> apply_classInt32Type(layer0rule7class4Int32Type)
			(4,8), # match classImplementationModule(layer0rule7class1ImplementationModule) -> association contents
			(8,3), # associationcontents -> match_classImplementationModule(layer0rule7class0AtomicComponent)
			(5,9), # apply class StructDeclaration(layer0rule7class2StructDeclaration) -> association members
			(9,6), # associationmembers -> apply_classMember(layer0rule7class3Member)
			(6,10), # apply class Member(layer0rule7class3Member) -> association type
			(10,7), # associationtype -> apply_classInt32Type(layer0rule7class4Int32Type)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = [((5,'name'),('concat',((4,'name'),('concat',(('constant','_'),('concat',((3,'name'),('concat',(('constant','__'),('constant','cdata')))))))))),((6,'name'),('constant','aMemberSoTheStructIsNotEmpty')),]
