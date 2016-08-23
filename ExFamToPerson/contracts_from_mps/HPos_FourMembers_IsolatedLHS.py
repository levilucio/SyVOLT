
from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HPos_FourMembers_IsolatedLHS(HimesisPreConditionPatternLHS):
  def __init__(self):
    """
    Creates the himesis graph representing the AToM3 model HPos_FourMembers_IsolatedLHS
    """
    # Flag this instance as compiled now
    self.is_compiled = True

    super(HPos_FourMembers_IsolatedLHS, self).__init__(name='HPos_FourMembers_IsolatedLHS', num_nodes=0, edges=[])

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


  def constraint(self, PreNode, graph):
    return True

