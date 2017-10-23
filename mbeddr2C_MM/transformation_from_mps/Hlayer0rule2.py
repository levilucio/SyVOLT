from core.himesis import Himesis
import uuid

class Hlayer0rule2(Himesis):
	def __init__(self):
		"""
		Creates the himesis graph representing the DSLTrans rule layer0rule2.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(Hlayer0rule2, self).__init__(name='Hlayer0rule2', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """layer0rule2"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule2')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """layer0rule2"""

		# match class Operation(layer0rule2class0Operation) node
		self.add_node()
		self.vs[3]["mm__"] = """Operation"""
		self.vs[3]["attr1"] = """+"""

		# apply class CFunctionPointerStructMember(layer0rule2class2CFunctionPointerStructMember) node
		self.add_node()
		self.vs[4]["mm__"] = """CFunctionPointerStructMember"""
		self.vs[4]["attr1"] = """1"""

		# apply class FunctionRefType(layer0rule2class3FunctionRefType) node
		self.add_node()
		self.vs[5]["mm__"] = """FunctionRefType"""
		self.vs[5]["attr1"] = """1"""

		# apply class PointerType(layer0rule5class2PointerType) node
		self.add_node()
		self.vs[6]["mm__"] = """PointerType"""
		self.vs[6]["attr1"] = """1"""

		# apply class VoidType(layer0rule5class3VoidType) node
		self.add_node()
		self.vs[7]["mm__"] = """VoidType"""
		self.vs[7]["attr1"] = """1"""

		# apply association CFunctionPointerStructMember--type-->FunctionRefType node 
		self.add_node()
		self.vs[8]["attr1"] = """type"""
		self.vs[8]["mm__"] = """directLink_T"""

		# apply association FunctionRefType--argTypes-->PointerType node 
		self.add_node()
		self.vs[9]["attr1"] = """argTypes"""
		self.vs[9]["mm__"] = """directLink_T"""

		# apply association PointerType--baseType-->VoidType node 
		self.add_node()
		self.vs[10]["attr1"] = """baseType"""
		self.vs[10]["mm__"] = """directLink_T"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class Operation(layer0rule2class0Operation)
			(1,4), # applymodel -> apply_classCFunctionPointerStructMember(layer0rule2class2CFunctionPointerStructMember)
			(1,5), # applymodel -> apply_classFunctionRefType(layer0rule2class3FunctionRefType)
			(1,6), # applymodel -> apply_classPointerType(layer0rule5class2PointerType)
			(1,7), # applymodel -> apply_classVoidType(layer0rule5class3VoidType)
			(4,8), # apply class CFunctionPointerStructMember(layer0rule2class2CFunctionPointerStructMember) -> association type
			(8,5), # associationtype -> apply_classFunctionRefType(layer0rule2class3FunctionRefType)
			(5,9), # apply class FunctionRefType(layer0rule2class3FunctionRefType) -> association argTypes
			(9,6), # associationargTypes -> apply_classPointerType(layer0rule5class2PointerType)
			(6,10), # apply class PointerType(layer0rule5class2PointerType) -> association baseType
			(10,7), # associationbaseType -> apply_classVoidType(layer0rule5class3VoidType)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = [((4,'name'),(3,'name')),]
