from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HUnitSon2Man_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HUnitSon2Man_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HUnitSon2Man_CompleteLHS, self).__init__(name='HUnitSon2Man_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HUnitSon2Man_CompleteLHS')
		self["equations"] = []
		# Set the node attributes

		# match class Family(Fam) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__Family"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Fam')

		# match class Child(Child) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__Child"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Child')

		# apply class Man(Man) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__Man"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Man')

		# match association null--sons-->nullnode
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return attr_value == "sons" """
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__directLink_S"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Famassoc3Child')

		# trace association null--trace-->nullnode
		self.add_node()
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__trace_link"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Manassoc4Child')

		self['equations'].append(((2,'fullName'),('concat',((1,'firstName'),(0,'lastName')))))

		# Add the edges
		self.add_edges([
			(0,3), # match class null(Fam) -> association sons
			(3,1), # association null -> match class null(Child)
			(2,4), # apply class null(Child) -> backward_association 
			(4,1), # backward_associationnull -> match_class null(Child)
		])


	# define evaluation methods for each match class.

	def eval_attr11(self, attr_value, this):
		return True

	def eval_attr12(self, attr_value, this):
		return True

	# define evaluation methods for each apply class.

	def eval_attr13(self, attr_value, this):
		return True

		# define evaluation methods for each match association.

	def eval_attr14(self, attr_value, this):
		return attr_value == "sons"
		# define evaluation methods for each apply association.


	def constraint(self, PreNode, graph):
		return True

