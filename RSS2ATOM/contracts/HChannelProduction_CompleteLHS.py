from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HChannelProduction_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self, *args, **kwargs):
		"""
		Creates the himesis graph representing the AToM3 model HChannelProduction_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HChannelProduction_CompleteLHS, self).__init__(name='HChannelProduction_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HChannelProduction_CompleteLHS')
		self["equations"] = []
		# Set the node attributes

		# match class Channel(Channel) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__Channel"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Channel')

		# apply class ATOM(ATOM) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__ATOM"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ATOM')

		# apply class Entry(Entry) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__Entry"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Entry')

		# apply class Generator(Generator) node
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return True"""
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__Generator"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Generator')

		# apply association null--entrie-->nullnode
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return attr_value == "entrie" """
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__directLink_T"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ATOMassoc4Entry')

		# apply association null--generator-->nullnode
		self.add_node()
		self.vs[5]["MT_pre__attr1"] = """return attr_value == "generator" """
		self.vs[5]["MT_label__"] = """6"""
		self.vs[5]["mm__"] = """MT_pre__directLink_T"""
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ATOMassoc5Generator')


		# Add the edges
		self.add_edges([
			(1,4), # apply class null(ATOM) -> association entrie
			(4,2), # association null -> apply class null(Entry)
			(1,5), # apply class null(ATOM) -> association generator
			(5,3), # association null -> apply class null(Generator)
		])


	# define evaluation methods for each match class.

	def eval_attr11(self, attr_value, this):
		return True

	# define evaluation methods for each apply class.

	def eval_attr12(self, attr_value, this):
		return True

	def eval_attr13(self, attr_value, this):
		return True

	def eval_attr14(self, attr_value, this):
		return True

		# define evaluation methods for each match association.

		# define evaluation methods for each apply association.

	def eval_attr15(self, attr_value, this):
		return attr_value == "entrie"
	def eval_attr16(self, attr_value, this):
		return attr_value == "generator"

	def constraint(self, PreNode, graph):
		return True

