from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HPos_FourMembers_ConnectedLHS(HimesisPreConditionPatternLHS):
  def __init__(self):
    """
    Creates the himesis graph representing the AToM3 model HPos_FourMembers_ConnectedLHS
    """
    # Flag this instance as compiled now
    self.is_compiled = True

    super(HPos_FourMembers_ConnectedLHS, self).__init__(name='HPos_FourMembers_ConnectedLHS', num_nodes=0, edges=[])

    # Add the edges
    self.add_edges([])

    # Set the graph attributes
    self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
    self["MT_constraint__"] = """return True"""
    self["name"] = """"""
    self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Pos_FourMembers')

    # Set the node attributes

    # match class Family(FourMem_M1) node
    self.add_node()
    self.vs[0]["MT_pre__attr1"] = """return True"""
    self.vs[0]["MT_label__"] = """1"""
    self.vs[0]["MT_dirty"] = False
    self.vs[0]["mm__"] = """MT_pre__Family"""
    self.vs[0]["GUID"] = uuid.uuid3(uuid.NAMESPACE_DNS,'FourMem_M1')

    # match class Member(FourMem_M2) node
    self.add_node()
    self.vs[1]["MT_pre__attr1"] = """return True"""
    self.vs[1]["MT_label__"] = """2"""
    self.vs[1]["MT_dirty"] = False
    self.vs[1]["mm__"] = """MT_pre__Member"""
    self.vs[1]["GUID"] = uuid.uuid3(uuid.NAMESPACE_DNS,'FourMem_M2')

    # match class Member(FourMem_M3) node
    self.add_node()
    self.vs[2]["MT_pre__attr1"] = """return True"""
    self.vs[2]["MT_label__"] = """3"""
    self.vs[2]["MT_dirty"] = False
    self.vs[2]["mm__"] = """MT_pre__Member"""
    self.vs[2]["GUID"] = uuid.uuid3(uuid.NAMESPACE_DNS,'FourMem_M3')

    # match class Member(FourMem_M4) node
    self.add_node()
    self.vs[3]["MT_pre__attr1"] = """return True"""
    self.vs[3]["MT_label__"] = """4"""
    self.vs[3]["MT_dirty"] = False
    self.vs[3]["mm__"] = """MT_pre__Member"""
    self.vs[3]["GUID"] = uuid.uuid3(uuid.NAMESPACE_DNS,'FourMem_M4')

    # match class Member(FourMem_M5) node
    self.add_node()
    self.vs[4]["MT_pre__attr1"] = """return True"""
    self.vs[4]["MT_label__"] = """5"""
    self.vs[4]["MT_dirty"] = False
    self.vs[4]["mm__"] = """MT_pre__Member"""
    self.vs[4]["GUID"] = uuid.uuid3(uuid.NAMESPACE_DNS,'FourMem_M5')

    # match association Family--fathers-->Membernode
    self.add_node()
    self.vs[5]["MT_pre__attr1"] = """fathers"""
    self.vs[5]["MT_label__"] = """6"""
    self.vs[5]["MT_subtypes__"] = []
    self.vs[5]["MT_dirty"] = False
    self.vs[5]["mm__"] = """MT_pre__directLink_S"""
    self.vs[5]["GUID"] = uuid.uuid3(uuid.NAMESPACE_DNS,'FourMem_M1assoc5FourMem_M2')

    # match association Family--mothers-->Membernode
    self.add_node()
    self.vs[6]["MT_pre__attr1"] = """mothers"""
    self.vs[6]["MT_label__"] = """7"""
    self.vs[6]["MT_subtypes__"] = []
    self.vs[6]["MT_dirty"] = False
    self.vs[6]["mm__"] = """MT_pre__directLink_S"""
    self.vs[6]["GUID"] = uuid.uuid3(uuid.NAMESPACE_DNS,'FourMem_M1assoc6FourMem_M3')

    # match association Family--sons-->Membernode
    self.add_node()
    self.vs[7]["MT_pre__attr1"] = """sons"""
    self.vs[7]["MT_label__"] = """8"""
    self.vs[7]["MT_subtypes__"] = []
    self.vs[7]["MT_dirty"] = False
    self.vs[7]["mm__"] = """MT_pre__directLink_S"""
    self.vs[7]["GUID"] = uuid.uuid3(uuid.NAMESPACE_DNS,'FourMem_M1assoc7FourMem_M4')

    # match association Family--daughters-->Membernode
    self.add_node()
    self.vs[8]["MT_pre__attr1"] = """daughters"""
    self.vs[8]["MT_label__"] = """9"""
    self.vs[8]["MT_subtypes__"] = []
    self.vs[8]["MT_dirty"] = False
    self.vs[8]["mm__"] = """MT_pre__directLink_S"""
    self.vs[8]["GUID"] = uuid.uuid3(uuid.NAMESPACE_DNS,'FourMem_M1assoc8FourMem_M5')

    # Add the edges
    self.add_edges([
      (0,5), # match classFamily(FourMem_M1) -> association fathers
      (5,1), # associationMember -> match_classMember(FourMem_M2)
      (0,6), # match classFamily(FourMem_M1) -> association mothers
      (6,2), # associationMember -> match_classMember(FourMem_M3)
      (0,7), # match classFamily(FourMem_M1) -> association sons
      (7,3), # associationMember -> match_classMember(FourMem_M4)
      (0,8), # match classFamily(FourMem_M1) -> association daughters
      (8,4), # associationMember -> match_classMember(FourMem_M5)
    ])

    # Add the attribute equations

    self["equations"] = []

  # define evaluation methods for each class.

  def eval_attr11(self, attr_value, this):
    return True

  def eval_attr12(self, attr_value, this):
    return True

  def eval_attr13(self, attr_value, this):
    return True

  def eval_attr14(self, attr_value, this):
    return True

  def eval_attr15(self, attr_value, this):
    return True

  # define evaluation methods for each association.

  def eval_attr16(self, attr_value, this):
    return attr_value == "fathers"
  def eval_attr17(self, attr_value, this):
    return attr_value == "mothers"
  def eval_attr18(self, attr_value, this):
    return attr_value == "sons"
  def eval_attr19(self, attr_value, this):
    return attr_value == "daughters"

  def constraint(self, PreNode, graph):
    return True
