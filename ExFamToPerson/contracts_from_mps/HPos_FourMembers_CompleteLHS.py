from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HPos_FourMembers_CompleteLHS(HimesisPreConditionPatternLHS):
  def __init__(self):
    """
    Creates the himesis graph representing the AToM3 model HPos_FourMembers_CompleteLHS
    """
    # Flag this instance as compiled now
    self.is_compiled = True

    super(HPos_FourMembers_CompleteLHS, self).__init__(name='HPos_FourMembers_CompleteLHS', num_nodes=0, edges=[])

    # Add the edges
    self.add_edges([])

    # Set the graph attributes
    self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
    self["MT_constraint__"] = """return True"""
    self["name"] = """"""
    self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'HPos_FourMembers_CompleteLHS')
    self["equations"] = []
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

    # apply class Community(FourMem_A1) node
    self.add_node()
    self.vs[5]["MT_pre__attr1"] = """return True"""
    self.vs[5]["MT_label__"] = """6"""
    self.vs[5]["MT_dirty"] = False
    self.vs[5]["mm__"] = """MT_pre__Community"""
    self.vs[5]["GUID"] = uuid.uuid3(uuid.NAMESPACE_DNS,'FourMem_A1')

    # apply class Man(FourMem_A2) node
    self.add_node()
    self.vs[6]["MT_pre__attr1"] = """return True"""
    self.vs[6]["MT_label__"] = """7"""
    self.vs[6]["MT_dirty"] = False
    self.vs[6]["mm__"] = """MT_pre__Man"""
    self.vs[6]["GUID"] = uuid.uuid3(uuid.NAMESPACE_DNS,'FourMem_A2')

    # apply class Woman(FourMem_A3) node
    self.add_node()
    self.vs[7]["MT_pre__attr1"] = """return True"""
    self.vs[7]["MT_label__"] = """8"""
    self.vs[7]["MT_dirty"] = False
    self.vs[7]["mm__"] = """MT_pre__Woman"""
    self.vs[7]["GUID"] = uuid.uuid3(uuid.NAMESPACE_DNS,'FourMem_A3')

    # apply class Man(FourMem_A4) node
    self.add_node()
    self.vs[8]["MT_pre__attr1"] = """return True"""
    self.vs[8]["MT_label__"] = """9"""
    self.vs[8]["MT_dirty"] = False
    self.vs[8]["mm__"] = """MT_pre__Man"""
    self.vs[8]["GUID"] = uuid.uuid3(uuid.NAMESPACE_DNS,'FourMem_A4')

    # apply class Woman(FourMem_A5) node
    self.add_node()
    self.vs[9]["MT_pre__attr1"] = """return True"""
    self.vs[9]["MT_label__"] = """10"""
    self.vs[9]["MT_dirty"] = False
    self.vs[9]["mm__"] = """MT_pre__Woman"""
    self.vs[9]["GUID"] = uuid.uuid3(uuid.NAMESPACE_DNS,'FourMem_A5')

    # match association Family--fathers-->Membernode
    self.add_node()
    self.vs[10]["MT_pre__attr1"] = """fathers"""
    self.vs[10]["MT_label__"] = """11"""
    self.vs[10]["MT_subtypes__"] = []
    self.vs[10]["MT_dirty"] = False
    self.vs[10]["mm__"] = """MT_pre__directLink_S"""
    self.vs[10]["GUID"] = uuid.uuid3(uuid.NAMESPACE_DNS,'FourMem_M1assoc10FourMem_M2')

    # match association Family--mothers-->Membernode
    self.add_node()
    self.vs[11]["MT_pre__attr1"] = """mothers"""
    self.vs[11]["MT_label__"] = """12"""
    self.vs[11]["MT_subtypes__"] = []
    self.vs[11]["MT_dirty"] = False
    self.vs[11]["mm__"] = """MT_pre__directLink_S"""
    self.vs[11]["GUID"] = uuid.uuid3(uuid.NAMESPACE_DNS,'FourMem_M1assoc11FourMem_M3')

    # match association Family--sons-->Membernode
    self.add_node()
    self.vs[12]["MT_pre__attr1"] = """sons"""
    self.vs[12]["MT_label__"] = """13"""
    self.vs[12]["MT_subtypes__"] = []
    self.vs[12]["MT_dirty"] = False
    self.vs[12]["mm__"] = """MT_pre__directLink_S"""
    self.vs[12]["GUID"] = uuid.uuid3(uuid.NAMESPACE_DNS,'FourMem_M1assoc12FourMem_M4')

    # match association Family--daughters-->Membernode
    self.add_node()
    self.vs[13]["MT_pre__attr1"] = """daughters"""
    self.vs[13]["MT_label__"] = """14"""
    self.vs[13]["MT_subtypes__"] = []
    self.vs[13]["MT_dirty"] = False
    self.vs[13]["mm__"] = """MT_pre__directLink_S"""
    self.vs[13]["GUID"] = uuid.uuid3(uuid.NAMESPACE_DNS,'FourMem_M1assoc13FourMem_M5')

    # apply association Community--persons-->Mannode
    self.add_node()
    self.vs[14]["MT_pre__attr1"] = """persons"""
    self.vs[14]["MT_label__"] = """15"""
    self.vs[14]["MT_subtypes__"] = []
    self.vs[14]["MT_dirty"] = False
    self.vs[14]["mm__"] = """MT_pre__directLink_T"""
    self.vs[14]["GUID"] = uuid.uuid3(uuid.NAMESPACE_DNS,'FourMem_A1assoc14FourMem_A2')

    # apply association Community--persons-->Womannode
    self.add_node()
    self.vs[15]["MT_pre__attr1"] = """persons"""
    self.vs[15]["MT_label__"] = """16"""
    self.vs[15]["MT_subtypes__"] = []
    self.vs[15]["MT_dirty"] = False
    self.vs[15]["mm__"] = """MT_pre__directLink_T"""
    self.vs[15]["GUID"] = uuid.uuid3(uuid.NAMESPACE_DNS,'FourMem_A1assoc15FourMem_A3')

    # apply association Community--persons-->Mannode
    self.add_node()
    self.vs[16]["MT_pre__attr1"] = """persons"""
    self.vs[16]["MT_label__"] = """17"""
    self.vs[16]["MT_subtypes__"] = []
    self.vs[16]["MT_dirty"] = False
    self.vs[16]["mm__"] = """MT_pre__directLink_T"""
    self.vs[16]["GUID"] = uuid.uuid3(uuid.NAMESPACE_DNS,'FourMem_A1assoc16FourMem_A4')

    # apply association Community--persons-->Womannode
    self.add_node()
    self.vs[17]["MT_pre__attr1"] = """persons"""
    self.vs[17]["MT_label__"] = """18"""
    self.vs[17]["MT_subtypes__"] = []
    self.vs[17]["MT_dirty"] = False
    self.vs[17]["mm__"] = """MT_pre__directLink_T"""
    self.vs[17]["GUID"] = uuid.uuid3(uuid.NAMESPACE_DNS,'FourMem_A1assoc17FourMem_A5')

    # trace association Man--trace-->Membernode
    self.add_node()
    self.vs[18]["MT_label__"] = """19"""
    self.vs[18]["MT_subtypes__"] = []
    self.vs[18]["MT_dirty"] = False
    self.vs[18]["mm__"] = """MT_pre__trace_link"""
    self.vs[18]["GUID"] = uuid.uuid3(uuid.NAMESPACE_DNS,'FourMem_A2assoc18FourMem_M2')

    # trace association Woman--trace-->Membernode
    self.add_node()
    self.vs[19]["MT_label__"] = """20"""
    self.vs[19]["MT_subtypes__"] = []
    self.vs[19]["MT_dirty"] = False
    self.vs[19]["mm__"] = """MT_pre__trace_link"""
    self.vs[19]["GUID"] = uuid.uuid3(uuid.NAMESPACE_DNS,'FourMem_A3assoc19FourMem_M3')

    # trace association Man--trace-->Membernode
    self.add_node()
    self.vs[20]["MT_label__"] = """21"""
    self.vs[20]["MT_subtypes__"] = []
    self.vs[20]["MT_dirty"] = False
    self.vs[20]["mm__"] = """MT_pre__trace_link"""
    self.vs[20]["GUID"] = uuid.uuid3(uuid.NAMESPACE_DNS,'FourMem_A4assoc20FourMem_M4')

    # trace association Woman--trace-->Membernode
    self.add_node()
    self.vs[21]["MT_label__"] = """22"""
    self.vs[21]["MT_subtypes__"] = []
    self.vs[21]["MT_dirty"] = False
    self.vs[21]["mm__"] = """MT_pre__trace_link"""
    self.vs[21]["GUID"] = uuid.uuid3(uuid.NAMESPACE_DNS,'FourMem_A5assoc21FourMem_M5')

    # Add the edges
    self.add_edges([
      (0,10), # match class Family(FourMem_M1) -> association fathers
      (10,1), # associationMember -> match class Member(FourMem_M2)
      (0,11), # match class Family(FourMem_M1) -> association mothers
      (11,2), # associationMember -> match class Member(FourMem_M3)
      (0,12), # match class Family(FourMem_M1) -> association sons
      (12,3), # associationMember -> match class Member(FourMem_M4)
      (0,13), # match class Family(FourMem_M1) -> association daughters
      (13,4), # associationMember -> match class Member(FourMem_M5)
      (5,14), # apply class Community(FourMem_A1) -> association persons
      (14,6), # associationMan -> apply class Man(FourMem_A2)
      (5,15), # apply class Community(FourMem_A1) -> association persons
      (15,7), # associationWoman -> apply class Woman(FourMem_A3)
      (5,16), # apply class Community(FourMem_A1) -> association persons
      (16,8), # associationMan -> apply class Man(FourMem_A4)
      (5,17), # apply class Community(FourMem_A1) -> association persons
      (17,9), # associationWoman -> apply class Woman(FourMem_A5)
      (6,18), # apply class Man(FourMem_M2) -> backward_association 
      (18,1), # backward_associationMember -> match_class Member(FourMem_M2)
      (7,19), # apply class Woman(FourMem_M3) -> backward_association 
      (19,2), # backward_associationMember -> match_class Member(FourMem_M3)
      (8,20), # apply class Man(FourMem_M4) -> backward_association 
      (20,3), # backward_associationMember -> match_class Member(FourMem_M4)
      (9,21), # apply class Woman(FourMem_M5) -> backward_association 
      (21,4), # backward_associationMember -> match_class Member(FourMem_M5)
    ])

    # Add the attribute equations

    self["equations"] = []

  # define evaluation methods for each match class.

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

  # define evaluation methods for each apply class.

  def eval_attr16(self, attr_value, this):
    return True

  def eval_attr17(self, attr_value, this):
    return True

  def eval_attr18(self, attr_value, this):
    return True

  def eval_attr19(self, attr_value, this):
    return True

  def eval_attr110(self, attr_value, this):
    return True

  # define evaluation methods for each match association.

  def eval_attr111(self, attr_value, this):
    return attr_value == "fathers"
  def eval_attr112(self, attr_value, this):
    return attr_value == "mothers"
  def eval_attr113(self, attr_value, this):
    return attr_value == "sons"
  def eval_attr114(self, attr_value, this):
    return attr_value == "daughters"
  # define evaluation methods for each apply association.

  def eval_attr115(self, attr_value, this):
    return attr_value == "persons"
  def eval_attr116(self, attr_value, this):
    return attr_value == "persons"
  def eval_attr117(self, attr_value, this):
    return attr_value == "persons"
  def eval_attr118(self, attr_value, this):
    return attr_value == "persons"

  def constraint(self, PreNode, graph):
    return True


