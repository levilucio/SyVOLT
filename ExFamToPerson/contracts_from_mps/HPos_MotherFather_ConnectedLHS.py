from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HPos_MotherFather_ConnectedLHS(HimesisPreConditionPatternLHS):
  def __init__(self):
    """
    Creates the himesis graph representing the AToM3 model HPos_MotherFather_ConnectedLHS
    """
    # Flag this instance as compiled now
    self.is_compiled = True

    super(HPos_MotherFather_ConnectedLHS, self).__init__(name='HPos_MotherFather_ConnectedLHS', num_nodes=0, edges=[])

    # Add the edges
    self.add_edges([])

    # Set the graph attributes
    self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
    self["MT_constraint__"] = """return True"""
    self["name"] = """"""
    self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HPos_MotherFather_ConnectedLHS')
    self["equations"] = []
    # Set the node attributes

    # match class Family(MotherFather_M1) node
    self.add_node()
    self.vs[0]["MT_pre__attr1"] = """return True"""
    self.vs[0]["MT_label__"] = """1"""
    self.vs[0]["MT_dirty"] = False
    self.vs[0]["mm__"] = """MT_pre__Family"""
    self.vs[0]["GUID"] = uuid.uuid3(uuid.NAMESPACE_DNS,'MotherFather_M1')

    # match class Member(MotherFather_M2) node
    self.add_node()
    self.vs[1]["MT_pre__attr1"] = """return True"""
    self.vs[1]["MT_label__"] = """2"""
    self.vs[1]["MT_dirty"] = False
    self.vs[1]["mm__"] = """MT_pre__Member"""
    self.vs[1]["GUID"] = uuid.uuid3(uuid.NAMESPACE_DNS,'MotherFather_M2')

    # match class Member(MotherFather_M3) node
    self.add_node()
    self.vs[2]["MT_pre__attr1"] = """return True"""
    self.vs[2]["MT_label__"] = """3"""
    self.vs[2]["MT_dirty"] = False
    self.vs[2]["mm__"] = """MT_pre__Member"""
    self.vs[2]["GUID"] = uuid.uuid3(uuid.NAMESPACE_DNS,'MotherFather_M3')


    # match association Family--mothers-->Membernode
    self.add_node()
    self.vs[3]["MT_pre__attr1"] = """mothers"""
    self.vs[3]["MT_label__"] = """4"""
    self.vs[3]["MT_subtypes__"] = []
    self.vs[3]["MT_dirty"] = False
    self.vs[3]["mm__"] = """MT_pre__directLink_S"""
    self.vs[3]["GUID"] = uuid.uuid3(uuid.NAMESPACE_DNS,'MotherFather_M1assoc3MotherFather_M2')

    # match association Family--fathers-->Membernode
    self.add_node()
    self.vs[4]["MT_pre__attr1"] = """fathers"""
    self.vs[4]["MT_label__"] = """5"""
    self.vs[4]["MT_subtypes__"] = []
    self.vs[4]["MT_dirty"] = False
    self.vs[4]["mm__"] = """MT_pre__directLink_S"""
    self.vs[4]["GUID"] = uuid.uuid3(uuid.NAMESPACE_DNS,'MotherFather_M1assoc4MotherFather_M3')

    # Add the edges
    self.add_edges([
      (0,3), # apply class Family(MotherFather_M1) -> association mothers
      (3,1), # associationMember -> apply class Member(MotherFather_M2)
      (0,4), # apply class Family(MotherFather_M1) -> association fathers
      (4,2), # associationMember -> apply class Member(MotherFather_M3)
    ])


  # define evaluation methods for each class.

  def eval_attr11(self, attr_value, this):
    return True

  def eval_attr12(self, attr_value, this):
    return True

  def eval_attr13(self, attr_value, this):
    return True

  # define evaluation methods for each association.

  def eval_attr14(self, attr_value, this):
    return attr_value == "mothers"
  def eval_attr15(self, attr_value, this):
    return attr_value == "fathers"

  def constraint(self, PreNode, graph):
    return True


