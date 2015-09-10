from core.himesis import Himesis
import uuid

class HExitPoint2BProcDefWhetherOrNotExitPtHasOutgoingTrans(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule ExitPoint2BProcDefWhetherOrNotExitPtHasOutgoingTrans.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HExitPoint2BProcDefWhetherOrNotExitPtHasOutgoingTrans, self).__init__(name='HExitPoint2BProcDefWhetherOrNotExitPtHasOutgoingTrans', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """ExitPoint2BProcDefWhetherOrNotExitPtHasOutgoingTrans"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ExitPoint2BProcDefWhetherOrNotExitPtHasOutgoingTrans')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ExitPoint2BProcDefWhetherOrNotExitPtHasOutgoingTransmatchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ExitPoint2BProcDefWhetherOrNotExitPtHasOutgoingTransapplymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ExitPoint2BProcDefWhetherOrNotExitPtHasOutgoingTranspairedwith2')
        self.vs[2]["rulename"] = """ExitPoint2BProcDefWhetherOrNotExitPtHasOutgoingTrans"""
        
        # match class State() node
        self.add_node()
        self.vs[3]["name"] = """"""
        self.vs[3]["classtype"] = """State"""
        self.vs[3]["mm__"] = """State"""
        self.vs[3]["cardinality"] = """+"""
        #self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match_contains node for class State()
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        #self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'matchcontains4')
        # match class ExitPoint() node
        self.add_node()
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """ExitPoint"""
        self.vs[5]["mm__"] = """ExitPoint"""
        self.vs[5]["cardinality"] = """+"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match_contains node for class ExitPoint()
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        #self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'matchcontains6')
        
        
        # apply class LocalDef() node
        self.add_node()
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """LocalDef"""
        self.vs[7]["mm__"] = """LocalDef"""
        self.vs[7]["cardinality"] = """1"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply_contains node for class LocalDef()
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        #self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains8')
        # apply class ProcDef() node
        self.add_node()
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """ProcDef"""
        self.vs[9]["mm__"] = """ProcDef"""
        self.vs[9]["cardinality"] = """1"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply_contains node for class ProcDef()
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        #self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains10')
        # apply class Name() node
        self.add_node()
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """Name"""
        self.vs[11]["mm__"] = """Name"""
        self.vs[11]["cardinality"] = """1"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply_contains node for class Name()
        self.add_node()
        self.vs[12]["mm__"] = """apply_contains"""
        #self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains12')
        # apply class Par() node
        self.add_node()
        self.vs[13]["name"] = """"""
        self.vs[13]["classtype"] = """Par"""
        self.vs[13]["mm__"] = """Par"""
        self.vs[13]["cardinality"] = """1"""
        #self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply_contains node for class Par()
        self.add_node()
        self.vs[14]["mm__"] = """apply_contains"""
        #self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains14')
        # apply class Trigger() node
        self.add_node()
        self.vs[15]["name"] = """"""
        self.vs[15]["classtype"] = """Trigger"""
        self.vs[15]["mm__"] = """Trigger"""
        self.vs[15]["cardinality"] = """1"""
        #self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply_contains node for class Trigger()
        self.add_node()
        self.vs[16]["mm__"] = """apply_contains"""
        #self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains16')
        
        
        # match association State--exitPoints-->ExitPoint node
        self.add_node()
        self.vs[17]["associationType"] = """exitPoints"""
        self.vs[17]["mm__"] = """directLink_S"""
        #self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc17')
        
        # apply association LocalDef--def-->ProcDef node
        self.add_node()
        self.vs[18]["associationType"] = """def"""
        self.vs[18]["mm__"] = """directLink_T"""
        #self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc18')
        # apply association ProcDef--channelNames-->Name node
        self.add_node()
        self.vs[19]["associationType"] = """channelNames"""
        self.vs[19]["mm__"] = """directLink_T"""
        #self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc19')
        # apply association ProcDef--p-->Par node
        self.add_node()
        self.vs[20]["associationType"] = """p"""
        self.vs[20]["mm__"] = """directLink_T"""
        #self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc20')
        # apply association Par--p-->Trigger node
        self.add_node()
        self.vs[21]["associationType"] = """p"""
        self.vs[21]["mm__"] = """directLink_T"""
        #self.vs[21]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc21')
        
        # backward association State---->LocalDef node
        self.add_node()
        self.vs[22]["type"] = """ruleDef"""
        self.vs[22]["mm__"] = """backward_link"""
        #self.vs[22]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'blink22')
        
        
        # has match attribute isComposite() node
        self.add_node()
        self.vs[23]["mm__"] = """hasAttribute_S"""
        #self.vs[23]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # match attribute isComposite() node
        self.add_node()
        self.vs[24]["name"] = """isComposite"""
        self.vs[24]["mm__"] = """Attribute"""
        self.vs[24]["Type"] = """'String'"""
        #self.vs[24]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match attribute equation isComposite() node
        self.add_node()
        self.vs[25]["name"] = """eq_"""
        self.vs[25]["mm__"] = """Equation"""
        #self.vs[25]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # match attribute equation left expr isComposite() node
        self.add_node()
        self.vs[26]["mm__"] = """leftExpr"""
        #self.vs[26]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # match attribute equation right expr isComposite() node
        self.add_node()
        self.vs[27]["mm__"] = """rightExpr"""
        #self.vs[27]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # apply attribute atom isComposite() node
        self.add_node()
        self.vs[28]["name"] = """true"""
        self.vs[28]["mm__"] = """Constant"""
        self.vs[28]["Type"] = """'String'"""
        #self.vs[28]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom28')
        # has match attribute name() node
        self.add_node()
        self.vs[29]["mm__"] = """hasAttribute_S"""
        #self.vs[29]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # match attribute name() node
        self.add_node()
        self.vs[30]["name"] = """name"""
        self.vs[30]["mm__"] = """Attribute"""
        self.vs[30]["Type"] = """'String'"""
        #self.vs[30]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        
        
        # has apply attribute name() node
        self.add_node()
        self.vs[31]["mm__"] = """hasAttribute_T"""
        #self.vs[31]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # apply attribute name() node
        self.add_node()
        self.vs[32]["name"] = """name"""
        self.vs[32]["mm__"] = """Attribute"""
        self.vs[32]["Type"] = """'String'"""
        #self.vs[32]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply attribute equation name() node
        self.add_node()
        self.vs[33]["name"] = """eq_"""
        self.vs[33]["mm__"] = """Equation"""
        #self.vs[33]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # apply attribute equation left expr name() node
        self.add_node()
        self.vs[34]["mm__"] = """leftExpr"""
        #self.vs[34]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # apply attribute equation right expr name() node
        self.add_node()
        self.vs[35]["mm__"] = """rightExpr"""
        #self.vs[35]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # attribute concat name() node
        self.add_node()
        self.vs[36]["name"] = """Concat36"""
        self.vs[36]["mm__"] = """Concat"""
        self.vs[36]["Type"] = """'String'"""
        #self.vs[36]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concat36')
        # apply attribute concat has left args name() node
        self.add_node()
        self.vs[37]["mm__"] = """hasArgs"""
        #self.vs[37]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgs37')
        # apply attribute concat has right args name() node
        self.add_node()
        self.vs[38]["mm__"] = """hasArgs"""
        #self.vs[38]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgs38')
        # apply attribute atom name() node
        self.add_node()
        self.vs[39]["name"] = """B"""
        self.vs[39]["mm__"] = """Constant"""
        self.vs[39]["Type"] = """'String'"""
        #self.vs[39]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom39')
        # has apply attribute literal() node
        self.add_node()
        self.vs[40]["mm__"] = """hasAttribute_T"""
        #self.vs[40]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # apply attribute literal() node
        self.add_node()
        self.vs[41]["name"] = """literal"""
        self.vs[41]["mm__"] = """Attribute"""
        self.vs[41]["Type"] = """'String'"""
        #self.vs[41]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply attribute equation literal() node
        self.add_node()
        self.vs[42]["name"] = """eq_"""
        self.vs[42]["mm__"] = """Equation"""
        #self.vs[42]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # apply attribute equation left expr literal() node
        self.add_node()
        self.vs[43]["mm__"] = """leftExpr"""
        #self.vs[43]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # apply attribute equation right expr literal() node
        self.add_node()
        self.vs[44]["mm__"] = """rightExpr"""
        #self.vs[44]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # apply attribute atom literal() node
        self.add_node()
        self.vs[45]["name"] = """sh_in"""
        self.vs[45]["mm__"] = """Constant"""
        self.vs[45]["Type"] = """'String'"""
        #self.vs[45]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom45')
        # has apply attribute channel() node
        self.add_node()
        self.vs[46]["mm__"] = """hasAttribute_T"""
        #self.vs[46]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # apply attribute channel() node
        self.add_node()
        self.vs[47]["name"] = """channel"""
        self.vs[47]["mm__"] = """Attribute"""
        self.vs[47]["Type"] = """'String'"""
        #self.vs[47]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply attribute equation channel() node
        self.add_node()
        self.vs[48]["name"] = """eq_"""
        self.vs[48]["mm__"] = """Equation"""
        #self.vs[48]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # apply attribute equation left expr channel() node
        self.add_node()
        self.vs[49]["mm__"] = """leftExpr"""
        #self.vs[49]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # apply attribute equation right expr channel() node
        self.add_node()
        self.vs[50]["mm__"] = """rightExpr"""
        #self.vs[50]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # apply attribute atom channel() node
        self.add_node()
        self.vs[51]["name"] = """sh_in"""
        self.vs[51]["mm__"] = """Constant"""
        self.vs[51]["Type"] = """'String'"""
        #self.vs[51]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom51')
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class State()
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class ExitPoint()
                (1,8), # applymodel -> apply_contains
                (8,7), # apply_contains -> apply_class LocalDef()
                (1,10), # applymodel -> apply_contains
                (10,9), # apply_contains -> apply_class ProcDef()
                (1,12), # applymodel -> apply_contains
                (12,11), # apply_contains -> apply_class Name()
                (1,14), # applymodel -> apply_contains
                (14,13), # apply_contains -> apply_class Par()
                (1,16), # applymodel -> apply_contains
                (16,15), # apply_contains -> apply_class Trigger()
                (3,17), # match_class State() -> association exitPoints
                (17,5), # association exitPoints  -> match_class ExitPoint()
                (7,18), # apply_class LocalDef() -> association def
                (18,9), # association def  -> apply_class ProcDef()
                (9,19), # apply_class ProcDef() -> association channelNames
                (19,11), # association channelNames  -> apply_class Name()
                (9,20), # apply_class ProcDef() -> association p
                (20,13), # association p  -> apply_class Par()
                (13,21), # apply_class Par() -> association p
                (21,15), # association p  -> apply_class Trigger()
                (7,22), # apply_class LocalDef() -> backward_association
                (22,3), #  backward_association -> apply_class State()
                (3,23), # match_class State() -> has_match_attribute isComposite ()
                (23,24), #  has_match_attribute isComposite () -> match_attribute isComposite ()
                (25,26), #  equation of match attribute isComposite () -> left_expr
                (26,24), #  left_expr -> match_attribute isComposite ()
                (25,27), #  equation of match attribute isComposite () -> right_expr
                (27,28), # right_expr --> term
                (5,29), # match_class ExitPoint() -> has_match_attribute name ()
                (29,30), #  has_match_attribute name () -> match_attribute name ()
                (9,31), # apply_class ProcDef() -> has_apply_attribute name ()
                (31,32), #  has_apply_attribute name () -> apply_attribute name ()
                (33,34), #  equation of apply attribute name () -> left_expr
                (34,32), #  left_expr -> apply_attribute name ()
                (33,35), #  equation of apply attribute name () -> right_expr
                (36,37), #  apply attribute concat name () -> left has_args
                (37,39), #  left has_args -> term
                (36,38), #  apply attribute concat name () -> right has_args
                (38,30), #  right has_args -> term
                (35,36), # right_expr --> term
                (11,40), # apply_class Name() -> has_apply_attribute literal ()
                (40,41), #  has_apply_attribute literal () -> apply_attribute literal ()
                (42,43), #  equation of apply attribute literal () -> left_expr
                (43,41), #  left_expr -> apply_attribute literal ()
                (42,44), #  equation of apply attribute literal () -> right_expr
                (44,45), # right_expr --> term
                (15,46), # apply_class Trigger() -> has_apply_attribute channel ()
                (46,47), #  has_apply_attribute channel () -> apply_attribute channel ()
                (48,49), #  equation of apply attribute channel () -> left_expr
                (49,47), #  left_expr -> apply_attribute channel ()
                (48,50), #  equation of apply attribute channel () -> right_expr
                (50,51), # right_expr --> term
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel
        ])
        
