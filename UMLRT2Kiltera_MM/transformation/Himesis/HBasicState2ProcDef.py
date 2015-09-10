from core.himesis import Himesis
import uuid

class HBasicState2ProcDef(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule BasicState2ProcDef.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HBasicState2ProcDef, self).__init__(name='HBasicState2ProcDef', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """BasicState2ProcDef"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'BasicState2ProcDef')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'BasicState2ProcDefmatchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'BasicState2ProcDefapplymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'BasicState2ProcDefpairedwith2')
        self.vs[2]["rulename"] = """BasicState2ProcDef"""
        
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
        
        
        # apply class ProcDef() node
        self.add_node()
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """ProcDef"""
        self.vs[5]["mm__"] = """ProcDef"""
        self.vs[5]["cardinality"] = """1"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply_contains node for class ProcDef()
        self.add_node()
        self.vs[6]["mm__"] = """apply_contains"""
        #self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains6')
        # apply class Listen() node
        self.add_node()
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """Listen"""
        self.vs[7]["mm__"] = """Listen"""
        self.vs[7]["cardinality"] = """1"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply_contains node for class Listen()
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        #self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains8')
        # apply class ListenBranch() node
        self.add_node()
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """ListenBranch"""
        self.vs[9]["mm__"] = """ListenBranch"""
        self.vs[9]["cardinality"] = """1"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply_contains node for class ListenBranch()
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        #self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains10')
        # apply class Trigger() node
        self.add_node()
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """Trigger"""
        self.vs[11]["mm__"] = """Trigger"""
        self.vs[11]["cardinality"] = """1"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply_contains node for class Trigger()
        self.add_node()
        self.vs[12]["mm__"] = """apply_contains"""
        #self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains12')
        
        
        
        # apply association ProcDef--p-->Listen node
        self.add_node()
        self.vs[13]["associationType"] = """p"""
        self.vs[13]["mm__"] = """directLink_T"""
        #self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc13')
        # apply association Listen--branches-->ListenBranch node
        self.add_node()
        self.vs[14]["associationType"] = """branches"""
        self.vs[14]["mm__"] = """directLink_T"""
        #self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc14')
        # apply association ListenBranch--p-->Trigger node
        self.add_node()
        self.vs[15]["associationType"] = """p"""
        self.vs[15]["mm__"] = """directLink_T"""
        #self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc15')
        
        # backward association State---->ProcDef node
        self.add_node()
        self.vs[16]["type"] = """ruleDef"""
        self.vs[16]["mm__"] = """backward_link"""
        #self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'blink16')
        
        
        # has match attribute isComposite() node
        self.add_node()
        self.vs[17]["mm__"] = """hasAttribute_S"""
        #self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # match attribute isComposite() node
        self.add_node()
        self.vs[18]["name"] = """isComposite"""
        self.vs[18]["mm__"] = """Attribute"""
        self.vs[18]["Type"] = """'String'"""
        #self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match attribute equation isComposite() node
        self.add_node()
        self.vs[19]["name"] = """eq_"""
        self.vs[19]["mm__"] = """Equation"""
        #self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # match attribute equation left expr isComposite() node
        self.add_node()
        self.vs[20]["mm__"] = """leftExpr"""
        #self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # match attribute equation right expr isComposite() node
        self.add_node()
        self.vs[21]["mm__"] = """rightExpr"""
        #self.vs[21]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # apply attribute atom isComposite() node
        self.add_node()
        self.vs[22]["name"] = """false"""
        self.vs[22]["mm__"] = """Constant"""
        self.vs[22]["Type"] = """'String'"""
        #self.vs[22]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom22')
        # has match attribute hasOutgoingTransitions() node
        self.add_node()
        self.vs[23]["mm__"] = """hasAttribute_S"""
        #self.vs[23]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # match attribute hasOutgoingTransitions() node
        self.add_node()
        self.vs[24]["name"] = """hasOutgoingTransitions"""
        self.vs[24]["mm__"] = """Attribute"""
        self.vs[24]["Type"] = """'String'"""
        #self.vs[24]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match attribute equation hasOutgoingTransitions() node
        self.add_node()
        self.vs[25]["name"] = """eq_"""
        self.vs[25]["mm__"] = """Equation"""
        #self.vs[25]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # match attribute equation left expr hasOutgoingTransitions() node
        self.add_node()
        self.vs[26]["mm__"] = """leftExpr"""
        #self.vs[26]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # match attribute equation right expr hasOutgoingTransitions() node
        self.add_node()
        self.vs[27]["mm__"] = """rightExpr"""
        #self.vs[27]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # apply attribute atom hasOutgoingTransitions() node
        self.add_node()
        self.vs[28]["name"] = """true"""
        self.vs[28]["mm__"] = """Constant"""
        self.vs[28]["Type"] = """'String'"""
        #self.vs[28]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom28')
        
        
        # has apply attribute channel() node
        self.add_node()
        self.vs[29]["mm__"] = """hasAttribute_T"""
        #self.vs[29]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # apply attribute channel() node
        self.add_node()
        self.vs[30]["name"] = """channel"""
        self.vs[30]["mm__"] = """Attribute"""
        self.vs[30]["Type"] = """'String'"""
        #self.vs[30]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply attribute equation channel() node
        self.add_node()
        self.vs[31]["name"] = """eq_"""
        self.vs[31]["mm__"] = """Equation"""
        #self.vs[31]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # apply attribute equation left expr channel() node
        self.add_node()
        self.vs[32]["mm__"] = """leftExpr"""
        #self.vs[32]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # apply attribute equation right expr channel() node
        self.add_node()
        self.vs[33]["mm__"] = """rightExpr"""
        #self.vs[33]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # apply attribute atom channel() node
        self.add_node()
        self.vs[34]["name"] = """exit"""
        self.vs[34]["mm__"] = """Constant"""
        self.vs[34]["Type"] = """'String'"""
        #self.vs[34]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom34')
        # has apply attribute channel() node
        self.add_node()
        self.vs[35]["mm__"] = """hasAttribute_T"""
        #self.vs[35]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # apply attribute channel() node
        self.add_node()
        self.vs[36]["name"] = """channel"""
        self.vs[36]["mm__"] = """Attribute"""
        self.vs[36]["Type"] = """'String'"""
        #self.vs[36]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply attribute equation channel() node
        self.add_node()
        self.vs[37]["name"] = """eq_"""
        self.vs[37]["mm__"] = """Equation"""
        #self.vs[37]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # apply attribute equation left expr channel() node
        self.add_node()
        self.vs[38]["mm__"] = """leftExpr"""
        #self.vs[38]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # apply attribute equation right expr channel() node
        self.add_node()
        self.vs[39]["mm__"] = """rightExpr"""
        #self.vs[39]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # apply attribute atom channel() node
        self.add_node()
        self.vs[40]["name"] = """exack"""
        self.vs[40]["mm__"] = """Constant"""
        self.vs[40]["Type"] = """'String'"""
        #self.vs[40]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom40')
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class State()
                (1,6), # applymodel -> apply_contains
                (6,5), # apply_contains -> apply_class ProcDef()
                (1,8), # applymodel -> apply_contains
                (8,7), # apply_contains -> apply_class Listen()
                (1,10), # applymodel -> apply_contains
                (10,9), # apply_contains -> apply_class ListenBranch()
                (1,12), # applymodel -> apply_contains
                (12,11), # apply_contains -> apply_class Trigger()
                (5,13), # apply_class ProcDef() -> association p
                (13,7), # association p  -> apply_class Listen()
                (7,14), # apply_class Listen() -> association branches
                (14,9), # association branches  -> apply_class ListenBranch()
                (9,15), # apply_class ListenBranch() -> association p
                (15,11), # association p  -> apply_class Trigger()
                (5,16), # apply_class ProcDef() -> backward_association
                (16,3), #  backward_association -> apply_class State()
                (3,17), # match_class State() -> has_match_attribute isComposite ()
                (17,18), #  has_match_attribute isComposite () -> match_attribute isComposite ()
                (19,20), #  equation of match attribute isComposite () -> left_expr
                (20,18), #  left_expr -> match_attribute isComposite ()
                (19,21), #  equation of match attribute isComposite () -> right_expr
                (21,22), # right_expr --> term
                (3,23), # match_class State() -> has_match_attribute hasOutgoingTransitions ()
                (23,24), #  has_match_attribute hasOutgoingTransitions () -> match_attribute hasOutgoingTransitions ()
                (25,26), #  equation of match attribute hasOutgoingTransitions () -> left_expr
                (26,24), #  left_expr -> match_attribute hasOutgoingTransitions ()
                (25,27), #  equation of match attribute hasOutgoingTransitions () -> right_expr
                (27,28), # right_expr --> term
                (9,29), # apply_class ListenBranch() -> has_apply_attribute channel ()
                (29,30), #  has_apply_attribute channel () -> apply_attribute channel ()
                (31,32), #  equation of apply attribute channel () -> left_expr
                (32,30), #  left_expr -> apply_attribute channel ()
                (31,33), #  equation of apply attribute channel () -> right_expr
                (33,34), # right_expr --> term
                (11,35), # apply_class Trigger() -> has_apply_attribute channel ()
                (35,36), #  has_apply_attribute channel () -> apply_attribute channel ()
                (37,38), #  equation of apply attribute channel () -> left_expr
                (38,36), #  left_expr -> apply_attribute channel ()
                (37,39), #  equation of apply attribute channel () -> right_expr
                (39,40), # right_expr --> term
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel
        ])
        
