from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HUnitCountry2Community_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HUnitCountry2Community_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HUnitCountry2Community_CompleteLHS, self).__init__(name='HUnitCountry2Community_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HUnitCountry2Community_CompleteLHS')
		self["equations"] = []
		# Set the node attributes

		# match class Country(AnyMatch-3f6342dd) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__Country"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'AnyMatch-3f6342dd')

		# apply class Community(ApplyClass-b83c61db) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__Community"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ApplyClass-b83c61db')

		# trace association null--trace-->nullnode
		self.add_node()
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__trace_link"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ApplyClass-b83c61dbassoc2AnyMatch-3f6342dd')


		# Add the edges
		self.add_edges([
			(1,2), # apply class null(AnyMatch-3f6342dd) -> backward_association 
			(2,0), # backward_associationnull -> match_class null(AnyMatch-3f6342dd)
		])


	# define evaluation methods for each match class.

	def eval_attr11(self, attr_value, this):
		return True

	# define evaluation methods for each apply class.

	def eval_attr12(self, attr_value, this):
		return True

		# define evaluation methods for each match association.

		# define evaluation methods for each apply association.


	def constraint(self, PreNode, graph):
		return True

