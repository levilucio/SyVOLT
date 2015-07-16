from core.himesis import Himesis
import uuid

class HBasicStateNoOutgoing2ProcDef(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule BasicStateNoOutgoing2ProcDef.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HBasicStateNoOutgoing2ProcDef, self).__init__(name='HBasicStateNoOutgoing2ProcDef', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """BasicStateNoOutgoing2ProcDef"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'BasicStateNoOutgoing2ProcDef')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'BasicStateNoOutgoing2ProcDefmatchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'BasicStateNoOutgoing2ProcDefapplymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'BasicStateNoOutgoing2ProcDefpairedwith2')
        self.vs[2]["rulename"] = """BasicStateNoOutgoing2ProcDef"""
        
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
        # apply class Null() node
        self.add_node()
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """Null"""
        self.vs[7]["mm__"] = """Null"""
        self.vs[7]["cardinality"] = """1"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply_contains node for class Null()
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        #self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains8')
        
        
        
        # apply association ProcDef--p-->Null node
        self.add_node()
        self.vs[9]["associationType"] = """p"""
        self.vs[9]["mm__"] = """directLink_T"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc9')
        
        # backward association State---->ProcDef node
        self.add_node()
        self.vs[10]["type"] = """ruleDef"""
        self.vs[10]["mm__"] = """backward_link"""
        #self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'blink10')
        
        
        # has match attribute isComposite() node
        self.add_node()
        self.vs[11]["mm__"] = """hasAttribute_S"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # match attribute isComposite() node
        self.add_node()
        self.vs[12]["name"] = """isComposite"""
        self.vs[12]["mm__"] = """Attribute"""
        self.vs[12]["Type"] = """'String'"""
        #self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match attribute equation isComposite() node
        self.add_node()
        self.vs[13]["name"] = """eq_"""
        self.vs[13]["mm__"] = """Equation"""
        #self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # match attribute equation left expr isComposite() node
        self.add_node()
        self.vs[14]["mm__"] = """leftExpr"""
        #self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # match attribute equation right expr isComposite() node
        self.add_node()
        self.vs[15]["mm__"] = """rightExpr"""
        #self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # apply attribute atom isComposite() node
        self.add_node()
        self.vs[16]["name"] = """false"""
        self.vs[16]["mm__"] = """Constant"""
        self.vs[16]["Type"] = """'String'"""
        #self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom16')
        # has match attribute hasOutgoingTransitions() node
        self.add_node()
        self.vs[17]["mm__"] = """hasAttribute_S"""
        #self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # match attribute hasOutgoingTransitions() node
        self.add_node()
        self.vs[18]["name"] = """hasOutgoingTransitions"""
        self.vs[18]["mm__"] = """Attribute"""
        self.vs[18]["Type"] = """'String'"""
        #self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match attribute equation hasOutgoingTransitions() node
        self.add_node()
        self.vs[19]["name"] = """eq_"""
        self.vs[19]["mm__"] = """Equation"""
        #self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # match attribute equation left expr hasOutgoingTransitions() node
        self.add_node()
        self.vs[20]["mm__"] = """leftExpr"""
        #self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # match attribute equation right expr hasOutgoingTransitions() node
        self.add_node()
        self.vs[21]["mm__"] = """rightExpr"""
        #self.vs[21]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # apply attribute atom hasOutgoingTransitions() node
        self.add_node()
        self.vs[22]["name"] = """false"""
        self.vs[22]["mm__"] = """Constant"""
        self.vs[22]["Type"] = """'String'"""
        #self.vs[22]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom22')
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class State()
                (1,6), # applymodel -> apply_contains
                (6,5), # apply_contains -> apply_class ProcDef()
                (1,8), # applymodel -> apply_contains
                (8,7), # apply_contains -> apply_class Null()
                (5,9), # apply_class ProcDef() -> association p
                (9,7), # association p  -> apply_class Null()
                (5,10), # apply_class ProcDef() -> backward_association
                (10,3), #  backward_association -> apply_class State()
                (3,11), # match_class State() -> has_match_attribute isComposite ()
                (11,12), #  has_match_attribute isComposite () -> match_attribute isComposite ()
                (13,14), #  equation of match attribute isComposite () -> left_expr
                (14,12), #  left_expr -> match_attribute isComposite ()
                (13,15), #  equation of match attribute isComposite () -> right_expr
                (15,16), # right_expr --> term
                (3,17), # match_class State() -> has_match_attribute hasOutgoingTransitions ()
                (17,18), #  has_match_attribute hasOutgoingTransitions () -> match_attribute hasOutgoingTransitions ()
                (19,20), #  equation of match attribute hasOutgoingTransitions () -> left_expr
                (20,18), #  left_expr -> match_attribute hasOutgoingTransitions ()
                (19,21), #  equation of match attribute hasOutgoingTransitions () -> right_expr
                (21,22), # right_expr --> term
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel
        ])
        
