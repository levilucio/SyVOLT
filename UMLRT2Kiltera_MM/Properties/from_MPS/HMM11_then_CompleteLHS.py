from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HMM11_then_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HMM11_then_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HMM11_then_CompleteLHS, self).__init__(name='HMM11_then_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HMM11_then_CompleteLHS')
		self["equations"] = []
		# Set the node attributes

		# apply class Par(0.8.a.0Par) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__Par"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.8.a.0Par')

		# apply class Proc(0.8.a.1Proc) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__Proc"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.8.a.1Proc')

		# apply class Proc(0.8.a.2Proc) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__Proc"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.8.a.2Proc')

		# apply association Par--p-->Procnode
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return attr_value == "p" """
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__directLink_T"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.8.a.0Parassoc30.8.a.1Proc')

		# apply association Par--p-->Procnode
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return attr_value == "p" """
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__directLink_T"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'0.8.a.0Parassoc40.8.a.2Proc')

		self["equations"].append(((0,'pivot'),('constant','Par6777f1dfPar')))


		# Add the edges
		self.add_edges([
			(0,3), # apply class Par(0.8.a.0Par) -> association p
			(3,1), # association Proc -> apply class Proc(0.8.a.1Proc)
			(0,4), # apply class Par(0.8.a.0Par) -> association p
			(4,2), # association Proc -> apply class Proc(0.8.a.2Proc)
		])


	# define evaluation methods for each match class.

	# define evaluation methods for each apply class.

	def eval_attr11(self, attr_value, this):
		return True

	def eval_attr12(self, attr_value, this):
		return True

	def eval_attr13(self, attr_value, this):
		return True

		# define evaluation methods for each match association.

		# define evaluation methods for each apply association.

	def eval_attr14(self, attr_value, this):
		return attr_value == "p"
	def eval_attr15(self, attr_value, this):
		return attr_value == "p"

	def constraint(self, PreNode, graph):
		return True

