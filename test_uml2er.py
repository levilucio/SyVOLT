# autogenerated from MPS
from util.parser import load_parser
from util.test_script_base import Test

class ProverTest(Test):

	def __init__(self):
		Test.__init__(self)


		#============TRANSFORMATION=================
		self.full_transformation = []
		self.full_transformation.append(['H02Package2ERModel',]) #L1
		self.full_transformation.append(['H03Class2EntityType',]) #L2
		self.full_transformation.append(['H05aProperty2AttributeNoType','H05bProperty2AttributeType',]) #L3
		self.full_transformation.append(['H07Property2WeakReference','H08Property2StrongReference',]) #L5
		self.full_transformation.append(['H09ConnectClass',]) #L7
		self.full_transformation.append(['H10ConnectProperty',]) #L8
		self.full_transformation.append(['H11ConnectReference',]) #L9
		self.artifact_directory = "~/Projects/SyVOLT/"
		self.transformation_directory = "~/Projects/SyVOLT/UML2ER/transformation/"


		#=====METAMODELS=================
		self.inputMM = "~/Projects/SyVOLT/UML2ER/UML.ecore"
		self.outputMM = "~/Projects/SyVOLT/UML2ER/ER.ecore"


		#====CONTRACTS==================
		self.contract_directory = "~/Projects/SyVOLT/UML2ER/contracts/"
		self.atomic_contracts = [
			"Contract01",
			"Contract02",
			"Contract03",
			"Contract05",
			"Contract06",
			"Contract07",
			"Contract08",
			"Contract09",
			"Contract10",
			"Contract12a",
			"Contract12b",
#			"Contract13Then",
#			"Contract13If",
#			"Contract14Then",
#			"Contract14If",
		]
		self.if_then_contracts = [
			[["Contract13If"], ["Contract13Then"]],
			[["Contract14If"], ["Contract14Then"]],
		]


		#=========PC SAVE LOCATION

		self.pc_save_filename = "pcs_UML2ER.txt"



if __name__ == "__main__":
	parser = load_parser()
	args = parser.parse_args()

	test = ProverTest()
	test.test_correct(args)