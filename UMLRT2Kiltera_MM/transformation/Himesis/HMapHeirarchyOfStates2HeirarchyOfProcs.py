from core.himesis import Himesis
import uuid

class HMapHeirarchyOfStates2HeirarchyOfProcs(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule MapHeirarchyOfStates2HeirarchyOfProcs.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HMapHeirarchyOfStates2HeirarchyOfProcs, self).__init__(name='HMapHeirarchyOfStates2HeirarchyOfProcs', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """MapHeirarchyOfStates2HeirarchyOfProcs"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'MapHeirarchyOfStates2HeirarchyOfProcs')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'MapHeirarchyOfStates2HeirarchyOfProcsmatchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'MapHeirarchyOfStates2HeirarchyOfProcsapplymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'MapHeirarchyOfStates2HeirarchyOfProcspairedwith2')
        self.vs[2]["rulename"] = """MapHeirarchyOfStates2HeirarchyOfProcs"""
        
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
        # match class State() node
        self.add_node()
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """State"""
        self.vs[5]["mm__"] = """State"""
        self.vs[5]["cardinality"] = """+"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match_contains node for class State()
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
        
        
        # match association State--states-->State node
        self.add_node()
        self.vs[11]["associationType"] = """states"""
        self.vs[11]["mm__"] = """directLink_S"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc11')
        
        # apply association LocalDef--def-->ProcDef node
        self.add_node()
        self.vs[12]["associationType"] = """def"""
        self.vs[12]["mm__"] = """directLink_T"""
        #self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc12')
        
        # backward association State---->LocalDef node
        self.add_node()
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["mm__"] = """backward_link"""
        #self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'blink13')
        # backward association State---->ProcDef node
        self.add_node()
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["mm__"] = """backward_link"""
        #self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'blink14')
        
        
        # has match attribute isComposite() node
        self.add_node()
        self.vs[15]["mm__"] = """hasAttribute_S"""
        #self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # match attribute isComposite() node
        self.add_node()
        self.vs[16]["name"] = """isComposite"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["Type"] = """'String'"""
        #self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match attribute equation isComposite() node
        self.add_node()
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        #self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # match attribute equation left expr isComposite() node
        self.add_node()
        self.vs[18]["mm__"] = """leftExpr"""
        #self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # match attribute equation right expr isComposite() node
        self.add_node()
        self.vs[19]["mm__"] = """rightExpr"""
        #self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # apply attribute atom isComposite() node
        self.add_node()
        self.vs[20]["name"] = """true"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["Type"] = """'String'"""
        #self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom20')
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class State()
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class State()
                (1,8), # applymodel -> apply_contains
                (8,7), # apply_contains -> apply_class LocalDef()
                (1,10), # applymodel -> apply_contains
                (10,9), # apply_contains -> apply_class ProcDef()
                (3,11), # match_class State() -> association states
                (11,5), # association states  -> match_class State()
                (7,12), # apply_class LocalDef() -> association def
                (12,9), # association def  -> apply_class ProcDef()
                (7,13), # apply_class LocalDef() -> backward_association
                (13,3), #  backward_association -> apply_class State()
                (9,14), # apply_class ProcDef() -> backward_association
                (14,5), #  backward_association -> apply_class State()
                (3,15), # match_class State() -> has_match_attribute isComposite ()
                (15,16), #  has_match_attribute isComposite () -> match_attribute isComposite ()
                (17,18), #  equation of match attribute isComposite () -> left_expr
                (18,16), #  left_expr -> match_attribute isComposite ()
                (17,19), #  equation of match attribute isComposite () -> right_expr
                (19,20), # right_expr --> term
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel
        ])
        
