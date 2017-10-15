from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HEntryContent_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HEntryContent_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HEntryContent_CompleteLHS, self).__init__(name='HEntryContent_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HEntryContent_CompleteLHS')
		self["equations"] = []
		# Set the node attributes

		# apply class Entry(Entry) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__Entry"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Entry')

		# apply class Content(Content) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__Content"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Content')

		# apply association null--content-->nullnode
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return attr_value == "content" """
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__directLink_T"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Entryassoc2Content')


		# Add the edges
		self.add_edges([
			(0,2), # apply class null(Entry) -> association content
			(2,1), # association null -> apply class null(Content)
		])


	# define evaluation methods for each match class.

	# define evaluation methods for each apply class.

	def eval_attr11(self, attr_value, this):
		return True

	def eval_attr12(self, attr_value, this):
		return True

		# define evaluation methods for each match association.

		# define evaluation methods for each apply association.

	def eval_attr13(self, attr_value, this):
		return attr_value == "content"

	def constraint(self, PreNode, graph):
		return True

