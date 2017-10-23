from core.himesis import Himesis
import uuid

class Hlayer0rule9(Himesis):
	def __init__(self):
		"""
		Creates the himesis graph representing the DSLTrans rule layer0rule9.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(Hlayer0rule9, self).__init__(name='Hlayer0rule9', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """layer0rule9"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule9')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """layer0rule9"""

		# match class RequiredPort(layer0rule9class0RequiredPort) node
		self.add_node()
		self.vs[3]["mm__"] = """RequiredPort"""
		self.vs[3]["attr1"] = """+"""

		# apply class Member(layer0rule9class1Member) node
		self.add_node()
		self.vs[4]["mm__"] = """Member"""
		self.vs[4]["attr1"] = """1"""

		# apply class VoidType(layer0rule9class2VoidType) node
		self.add_node()
		self.vs[5]["mm__"] = """VoidType"""
		self.vs[5]["attr1"] = """1"""

		# apply class PointerType(layer0rule9class3PointerType) node
		self.add_node()
		self.vs[6]["mm__"] = """PointerType"""
		self.vs[6]["attr1"] = """1"""

		# apply association Member--type-->PointerType node 
		self.add_node()
		self.vs[7]["attr1"] = """type"""
		self.vs[7]["mm__"] = """directLink_T"""

		# apply association PointerType--baseType-->VoidType node 
		self.add_node()
		self.vs[8]["attr1"] = """baseType"""
		self.vs[8]["mm__"] = """directLink_T"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class RequiredPort(layer0rule9class0RequiredPort)
			(1,4), # applymodel -> apply_classMember(layer0rule9class1Member)
			(1,5), # applymodel -> apply_classVoidType(layer0rule9class2VoidType)
			(1,6), # applymodel -> apply_classPointerType(layer0rule9class3PointerType)
			(4,7), # apply class Member(layer0rule9class1Member) -> association type
			(7,6), # associationtype -> apply_classPointerType(layer0rule9class3PointerType)
			(6,8), # apply class PointerType(layer0rule9class3PointerType) -> association baseType
			(8,5), # associationbaseType -> apply_classVoidType(layer0rule9class2VoidType)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = [((4,'name'),('concat',((3,'name'),('constant','__port')))),]
