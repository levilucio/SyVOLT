from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HPos_MotherFather_CompleteLHS(HimesisPreConditionPatternLHS):
  def __init__(self):
    """
    Creates the himesis graph representing the AToM3 model HPos_MotherFather_CompleteLHS
    """
    # Flag this instance as compiled now
    self.is_compiled = True

    super(HPos_MotherFather_CompleteLHS, self).__init__(name='HPos_MotherFather_CompleteLHS', num_nodes=0, edges=[])

    # Add the edges
    self.add_edges([])

    # Set the graph attributes
    self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
    self["MT_constraint__"] = """return True"""
    self["name"] = """"""
    self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HPos_MotherFather_CompleteLHS')
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

    # apply class Community(MotherFather_A1) node
    self.add_node()
    self.vs[3]["MT_pre__attr1"] = """return True"""
    self.vs[3]["MT_label__"] = """4"""
    self.vs[3]["MT_dirty"] = False
    self.vs[3]["mm__"] = """MT_pre__Community"""
    self.vs[3]["GUID"] = uuid.uuid3(uuid.NAMESPACE_DNS,'MotherFather_A1')

    # apply class Woman(MotherFather_AMother) node
    self.add_node()
    self.vs[4]["MT_pre__attr1"] = """return True"""
    self.vs[4]["MT_label__"] = """5"""
    self.vs[4]["MT_dirty"] = False
    self.vs[4]["mm__"] = """MT_pre__Woman"""
    self.vs[4]["GUID"] = uuid.uuid3(uuid.NAMESPACE_DNS,'MotherFather_AMother')

    # apply class Man(MotherFather_AFather) node
    self.add_node()
    self.vs[5]["MT_pre__attr1"] = """return True"""
    self.vs[5]["MT_label__"] = """6"""
    self.vs[5]["MT_dirty"] = False
    self.vs[5]["mm__"] = """MT_pre__Man"""
    self.vs[5]["GUID"] = uuid.uuid3(uuid.NAMESPACE_DNS,'MotherFather_AFather')

    # match association Family--mothers-->Membernode
    self.add_node()
    self.vs[6]["MT_pre__attr1"] = """mothers"""
    self.vs[6]["MT_label__"] = """7"""
    self.vs[6]["MT_subtypes__"] = []
    self.vs[6]["MT_dirty"] = False
    self.vs[6]["mm__"] = """MT_pre__directLink_S"""
    self.vs[6]["GUID"] = uuid.uuid3(uuid.NAMESPACE_DNS,'MotherFather_M1assoc6MotherFather_M2')

    # match association Family--fathers-->Membernode
    self.add_node()
    self.vs[7]["MT_pre__attr1"] = """fathers"""
    self.vs[7]["MT_label__"] = """8"""
    self.vs[7]["MT_subtypes__"] = []
    self.vs[7]["MT_dirty"] = False
    self.vs[7]["mm__"] = """MT_pre__directLink_S"""
    self.vs[7]["GUID"] = uuid.uuid3(uuid.NAMESPACE_DNS,'MotherFather_M1assoc7MotherFather_M3')

    # apply association Community--persons-->Womannode
    self.add_node()
    self.vs[8]["MT_pre__attr1"] = """persons"""
    self.vs[8]["MT_label__"] = """9"""
    self.vs[8]["MT_subtypes__"] = []
    self.vs[8]["MT_dirty"] = False
    self.vs[8]["mm__"] = """MT_pre__directLink_T"""
    self.vs[8]["GUID"] = uuid.uuid3(uuid.NAMESPACE_DNS,'MotherFather_A1assoc8MotherFather_AMother')

    # apply association Community--persons-->Mannode
    self.add_node()
    self.vs[9]["MT_pre__attr1"] = """persons"""
    self.vs[9]["MT_label__"] = """10"""
    self.vs[9]["MT_subtypes__"] = []
    self.vs[9]["MT_dirty"] = False
    self.vs[9]["mm__"] = """MT_pre__directLink_T"""
    self.vs[9]["GUID"] = uuid.uuid3(uuid.NAMESPACE_DNS,'MotherFather_A1assoc9MotherFather_AFather')

    self['equations'].append(((4,'fullName'),('concat',((1,'firstName'),(0,'lastName')))))
    self['equations'].append(((5,'fullName'),('concat',((2,'firstName'),(0,'lastName')))))

    # Add the edges
    self.add_edges([
      (0,6), # match class Family(MotherFather_M1) -> association mothers
      (6,1), # associationMember -> match class Member(MotherFather_M2)
      (0,7), # match class Family(MotherFather_M1) -> association fathers
      (7,2), # associationMember -> match class Member(MotherFather_M3)
      (3,8), # apply class Community(MotherFather_A1) -> association persons
      (8,4), # associationWoman -> apply class Woman(MotherFather_AMother)
      (3,9), # apply class Community(MotherFather_A1) -> association persons
      (9,5), # associationMan -> apply class Man(MotherFather_AFather)
    ])


  # define evaluation methods for each match class.

  def eval_attr11(self, attr_value, this):
    return True

  def eval_attr12(self, attr_value, this):
    return True

  def eval_attr13(self, attr_value, this):
    return True

  # define evaluation methods for each apply class.

  def eval_attr14(self, attr_value, this):
    return True

  def eval_attr15(self, attr_value, this):
    return True

  def eval_attr16(self, attr_value, this):
    return True

  # define evaluation methods for each match association.

  def eval_attr17(self, attr_value, this):
    return attr_value == "mothers"
  def eval_attr18(self, attr_value, this):
    return attr_value == "fathers"
  # define evaluation methods for each apply association.

  def eval_attr19(self, attr_value, this):
    return attr_value == "persons"
  def eval_attr110(self, attr_value, this):
    return attr_value == "persons"

  def constraint(self, PreNode, graph):
    return True


