from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HUnitI2E_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HUnitI2E_CompleteLHS
		"""
		# Flag this instance as compiled now
		self.is_compiled = True

		super(HUnitI2E_CompleteLHS, self).__init__(name='HUnitI2E_CompleteLHS', num_nodes=0, edges=[])

		# Add the edges
		self.add_edges([])

		# Set the graph attributes
		self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
		self["MT_constraint__"] = """return True"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HUnitI2E_CompleteLHS')
		self["equations"] = []
		# Set the node attributes

		# match class Item(Item) node
		self.add_node()
		self.vs[0]["MT_pre__attr1"] = """return True"""
		self.vs[0]["MT_label__"] = """1"""
		self.vs[0]["mm__"] = """MT_pre__Item"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Item')

		# apply class Entry(Entry) node
		self.add_node()
		self.vs[1]["MT_pre__attr1"] = """return True"""
		self.vs[1]["MT_label__"] = """2"""
		self.vs[1]["mm__"] = """MT_pre__Entry"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Entry')

		# apply class Link(Link) node
		self.add_node()
		self.vs[2]["MT_pre__attr1"] = """return True"""
		self.vs[2]["MT_label__"] = """3"""
		self.vs[2]["mm__"] = """MT_pre__Link"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Link')

		# apply association null--links-->nullnode
		self.add_node()
		self.vs[3]["MT_pre__attr1"] = """return attr_value == "links" """
		self.vs[3]["MT_label__"] = """4"""
		self.vs[3]["mm__"] = """MT_pre__directLink_T"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Entryassoc3Link')

		self['equations'].append(((1,'title'),(0,'title')))
		self['equations'].append(((1,'id'),(0,'guid')))
		self['equations'].append(((1,'published'),(0,'pubDate')))
		self['equations'].append(((1,'summary'),(0,'comments')))
		self['equations'].append(((2,'hrefl'),(0,'link')))

		# Add the edges
		self.add_edges([
			(1,3), # apply class null(Entry) -> association links
			(3,2), # association null -> apply class null(Link)
		])


	# define evaluation methods for each match class.

	def eval_attr11(self, attr_value, this):
		return True

	# define evaluation methods for each apply class.

	def eval_attr12(self, attr_value, this):
		return True

	def eval_attr13(self, attr_value, this):
		return True

		# define evaluation methods for each match association.

		# define evaluation methods for each apply association.

	def eval_attr14(self, attr_value, this):
		return attr_value == "links"

	def constraint(self, PreNode, graph):
		return True

