from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HSS1_then_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HSS1_then_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HSS1_then_CompleteLHS, self).__init__(name='HSS1_then_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HSS1_then_CompleteLHS')
		self["equations"] = []
		# Set the node attributes

		# apply class Inst(0.36.a.0Inst) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__Inst"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.36.a.0Inst')

		# apply class ProcDef(0.36.a.1ProcDef) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__ProcDef"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.36.a.1ProcDef')

		self['equations'].append(((1,'name'),('concat', (('constant', 'S'), (0, 'name')))))
		self["equations"].append(((0,'pivot'),('constant','Inst0c012f83Inst')))


		# Add the edges
		self.add_edges([
		])


	# define evaluation methods for each match class.

	# define evaluation methods for each apply class.

	def eval_attr11(self, attr_value, this):
		return True

	def eval_attr12(self, attr_value, this):
		return True

		# define evaluation methods for each match association.

		# define evaluation methods for each apply association.


	def constraint(self, PreNode, graph):
		return True

