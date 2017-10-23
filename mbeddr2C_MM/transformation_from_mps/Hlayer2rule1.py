from core.himesis import Himesis
import uuid

class Hlayer2rule1(Himesis):
	def __init__(self):
		"""
		Creates the himesis graph representing the DSLTrans rule layer2rule1.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(Hlayer2rule1, self).__init__(name='Hlayer2rule1', num_nodes=0, edges=[])

		# Set the graph attributes
		self["mm__"] = ['HimesisMM']
		self["name"] = """layer2rule1"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer2rule1')

		# match model. We only support one match model
		self.add_node()
		self.vs[0]["mm__"] = """MatchModel"""

		# apply model node
		self.add_node()
		self.vs[1]["mm__"] = """ApplyModel"""

		# paired with relation between match and apply models
		self.add_node()
		self.vs[2]["mm__"] = """paired_with"""
		self.vs[2]["attr1"] = """layer2rule1"""

		# match class StringType(layer2rule1class0StringType) node
		self.add_node()
		self.vs[3]["mm__"] = """StringType"""
		self.vs[3]["attr1"] = """+"""

		# match class OperationParameter(layer2rule1class1OperationParameter) node
		self.add_node()
		self.vs[4]["mm__"] = """OperationParameter"""
		self.vs[4]["attr1"] = """+"""

		# apply class StringType(layer2rule1class2StringType) node
		self.add_node()
		self.vs[5]["mm__"] = """StringType"""
		self.vs[5]["attr1"] = """1"""

		# apply class Argument(layer2rule1class3Argument) node
		self.add_node()
		self.vs[6]["mm__"] = """Argument"""
		self.vs[6]["attr1"] = """1"""

		# match association OperationParameter--type-->StringType node 
		self.add_node()
		self.vs[7]["attr1"] = """type"""
		self.vs[7]["mm__"] = """directLink_S"""

		# apply association Argument--type-->StringType node 
		self.add_node()
		self.vs[8]["attr1"] = """type"""
		self.vs[8]["mm__"] = """directLink_T"""

		# backward association Argument-->OperationParameternode 
		self.add_node()
		self.vs[9]["mm__"] = """backward_link"""

		# Add the edges
		self.add_edges([
			(0,3), # matchmodel -> match_class StringType(layer2rule1class0StringType)
			(0,4), # matchmodel -> match_class OperationParameter(layer2rule1class1OperationParameter)
			(1,5), # applymodel -> apply_classStringType(layer2rule1class2StringType)
			(1,6), # applymodel -> apply_classArgument(layer2rule1class3Argument)
			(4,7), # match classOperationParameter(layer2rule1class1OperationParameter) -> association type
			(7,3), # associationtype -> match_classOperationParameter(layer2rule1class0StringType)
			(6,8), # apply class Argument(layer2rule1class3Argument) -> association type
			(8,5), # associationtype -> apply_classStringType(layer2rule1class2StringType)
			(6,9), # apply class Argument(layer2rule1class1OperationParameter) -> backward_association 
			(9,4), # backward_associationOperationParameter -> match_class OperationParameter(layer2rule1class1OperationParameter)
			(0,2), # matchmodel -> pairedwith
			(2,1) # pairedwith -> applyModel
		])

		self["equations"] = []
