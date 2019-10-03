from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HUnitConnectCCAC_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HUnitConnectCCAC_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HUnitConnectCCAC_CompleteLHS, self).__init__(name='HUnitConnectCCAC_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HUnitConnectCCAC_CompleteLHS')
		self["equations"] = []
		# Set the node attributes

		# match class Channel(Channel) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__Channel"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Channel')

		# match class Category(MCategory) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__Category"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'MCategory')

		# apply class ATOM(ATOM) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__ATOM"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ATOM')

		# apply class Category(ACategory) node
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return True"""
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__Category"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ACategory')

		# match association null--category-->nullnode
		self.add_node()
		self.vs[4]["MT_pre__attr1"] = """return attr_value == "category" """
		self.vs[4]["MT_label__"] = """5"""
		self.vs[4]["mm__"] = """MT_pre__directLink_S"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Channelassoc4MCategory')

		# apply association null--categories-->nullnode
		self.add_node()
		self.vs[5]["MT_pre__attr1"] = """return attr_value == "categories" """
		self.vs[5]["MT_label__"] = """6"""
		self.vs[5]["mm__"] = """MT_pre__directLink_T"""
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ATOMassoc5ACategory')

		# trace association null--trace-->nullnode
		self.add_node()
		self.vs[6]["MT_label__"] = """7"""
		self.vs[6]["mm__"] = """MT_pre__trace_link"""
		self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ATOMassoc6Channel')

		# trace association null--trace-->nullnode
		self.add_node()
		self.vs[7]["MT_label__"] = """8"""
		self.vs[7]["mm__"] = """MT_pre__trace_link"""
		self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ACategoryassoc7MCategory')


		# Add the edges
		self.add_edges([
			(0,4), # match class null(Channel) -> association category
			(4,1), # association null -> match class null(MCategory)
			(2,5), # apply class null(ATOM) -> association categories
			(5,3), # association null -> apply class null(ACategory)
			(2,6), # apply class null(Channel) -> backward_association 
			(6,0), # backward_associationnull -> match_class null(Channel)
			(3,7), # apply class null(MCategory) -> backward_association 
			(7,1), # backward_associationnull -> match_class null(MCategory)
		])


	# define evaluation methods for each match class.

	def eval_attr11(self, attr_value, this):
		return True

	def eval_attr12(self, attr_value, this):
		return True

	# define evaluation methods for each apply class.

	def eval_attr13(self, attr_value, this):
		return True

	def eval_attr14(self, attr_value, this):
		return True

		# define evaluation methods for each match association.

	def eval_attr15(self, attr_value, this):
		return attr_value == "category"
		# define evaluation methods for each apply association.

	def eval_attr16(self, attr_value, this):
		return attr_value == "categories"

	def constraint(self, PreNode, graph):
		return True

