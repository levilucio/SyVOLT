from core.himesis import Himesis
import uuid

class HTransition2ListenBranch(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule Transition2ListenBranch.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HTransition2ListenBranch, self).__init__(name='HTransition2ListenBranch', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """Transition2ListenBranch"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Transition2ListenBranch')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Transition2ListenBranchmatchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Transition2ListenBranchapplymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Transition2ListenBranchpairedwith2')
        self.vs[2]["rulename"] = """Transition2ListenBranch"""
        
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
        # match class Transition() node
        self.add_node()
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """Transition"""
        self.vs[5]["mm__"] = """Transition"""
        self.vs[5]["cardinality"] = """+"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match_contains node for class Transition()
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        #self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'matchcontains6')
        # match class Trigger() node
        self.add_node()
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """Trigger"""
        self.vs[7]["mm__"] = """Trigger"""
        self.vs[7]["cardinality"] = """1"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match_contains node for class Trigger()
        self.add_node()
        self.vs[8]["mm__"] = """match_contains"""
        #self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'matchcontains8')
        # match class Signal() node
        self.add_node()
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """Signal"""
        self.vs[9]["mm__"] = """Signal"""
        self.vs[9]["cardinality"] = """1"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match_contains node for class Signal()
        self.add_node()
        self.vs[10]["mm__"] = """match_contains"""
        #self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'matchcontains10')
        
        
        # apply class Listen() node
        self.add_node()
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """Listen"""
        self.vs[11]["mm__"] = """Listen"""
        self.vs[11]["cardinality"] = """1"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply_contains node for class Listen()
        self.add_node()
        self.vs[12]["mm__"] = """apply_contains"""
        #self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains12')
        # apply class ListenBranch() node
        self.add_node()
        self.vs[13]["name"] = """"""
        self.vs[13]["classtype"] = """ListenBranch"""
        self.vs[13]["mm__"] = """ListenBranch"""
        self.vs[13]["cardinality"] = """1"""
        #self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply_contains node for class ListenBranch()
        self.add_node()
        self.vs[14]["mm__"] = """apply_contains"""
        #self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains14')
        # apply class Inst() node
        self.add_node()
        self.vs[15]["name"] = """"""
        self.vs[15]["classtype"] = """Inst"""
        self.vs[15]["mm__"] = """Inst"""
        self.vs[15]["cardinality"] = """1"""
        #self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply_contains node for class Inst()
        self.add_node()
        self.vs[16]["mm__"] = """apply_contains"""
        #self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains16')
        
        
        # match association State--outgoingTransitions-->Transition node
        self.add_node()
        self.vs[17]["associationType"] = """outgoingTransitions"""
        self.vs[17]["mm__"] = """directLink_S"""
        #self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc17')
        # match association Transition--triggers-->Trigger node
        self.add_node()
        self.vs[18]["associationType"] = """triggers"""
        self.vs[18]["mm__"] = """directLink_S"""
        #self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc18')
        # match association Trigger--signal-->Signal node
        self.add_node()
        self.vs[19]["associationType"] = """signal"""
        self.vs[19]["mm__"] = """directLink_S"""
        #self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc19')
        
        # apply association Listen--branches-->ListenBranch node
        self.add_node()
        self.vs[20]["associationType"] = """branches"""
        self.vs[20]["mm__"] = """directLink_T"""
        #self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc20')
        # apply association ListenBranch--p-->Inst node
        self.add_node()
        self.vs[21]["associationType"] = """p"""
        self.vs[21]["mm__"] = """directLink_T"""
        #self.vs[21]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc21')
        
        # backward association State---->Listen node
        self.add_node()
        self.vs[22]["type"] = """ruleDef"""
        self.vs[22]["mm__"] = """backward_link"""
        #self.vs[22]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'blink22')
        # backward association Transition---->Inst node
        self.add_node()
        self.vs[23]["type"] = """ruleDef"""
        self.vs[23]["mm__"] = """backward_link"""
        #self.vs[23]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'blink23')
        
        
        # has match attribute isComposite() node
        self.add_node()
        self.vs[24]["mm__"] = """hasAttribute_S"""
        #self.vs[24]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # match attribute isComposite() node
        self.add_node()
        self.vs[25]["name"] = """isComposite"""
        self.vs[25]["mm__"] = """Attribute"""
        self.vs[25]["Type"] = """'String'"""
        #self.vs[25]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match attribute equation isComposite() node
        self.add_node()
        self.vs[26]["name"] = """eq_"""
        self.vs[26]["mm__"] = """Equation"""
        #self.vs[26]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # match attribute equation left expr isComposite() node
        self.add_node()
        self.vs[27]["mm__"] = """leftExpr"""
        #self.vs[27]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # match attribute equation right expr isComposite() node
        self.add_node()
        self.vs[28]["mm__"] = """rightExpr"""
        #self.vs[28]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # apply attribute atom isComposite() node
        self.add_node()
        self.vs[29]["name"] = """false"""
        self.vs[29]["mm__"] = """Constant"""
        self.vs[29]["Type"] = """'String'"""
        #self.vs[29]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom29')
        # has match attribute hasOutgoingTransitions() node
        self.add_node()
        self.vs[30]["mm__"] = """hasAttribute_S"""
        #self.vs[30]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # match attribute hasOutgoingTransitions() node
        self.add_node()
        self.vs[31]["name"] = """hasOutgoingTransitions"""
        self.vs[31]["mm__"] = """Attribute"""
        self.vs[31]["Type"] = """'String'"""
        #self.vs[31]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match attribute equation hasOutgoingTransitions() node
        self.add_node()
        self.vs[32]["name"] = """eq_"""
        self.vs[32]["mm__"] = """Equation"""
        #self.vs[32]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # match attribute equation left expr hasOutgoingTransitions() node
        self.add_node()
        self.vs[33]["mm__"] = """leftExpr"""
        #self.vs[33]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # match attribute equation right expr hasOutgoingTransitions() node
        self.add_node()
        self.vs[34]["mm__"] = """rightExpr"""
        #self.vs[34]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # apply attribute atom hasOutgoingTransitions() node
        self.add_node()
        self.vs[35]["name"] = """true"""
        self.vs[35]["mm__"] = """Constant"""
        self.vs[35]["Type"] = """'String'"""
        #self.vs[35]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom35')
        # has match attribute name() node
        self.add_node()
        self.vs[36]["mm__"] = """hasAttribute_S"""
        #self.vs[36]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # match attribute name() node
        self.add_node()
        self.vs[37]["name"] = """name"""
        self.vs[37]["mm__"] = """Attribute"""
        self.vs[37]["Type"] = """'String'"""
        #self.vs[37]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        
        
        # has apply attribute channel() node
        self.add_node()
        self.vs[38]["mm__"] = """hasAttribute_T"""
        #self.vs[38]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # apply attribute channel() node
        self.add_node()
        self.vs[39]["name"] = """channel"""
        self.vs[39]["mm__"] = """Attribute"""
        self.vs[39]["Type"] = """'String'"""
        #self.vs[39]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply attribute equation channel() node
        self.add_node()
        self.vs[40]["name"] = """eq_"""
        self.vs[40]["mm__"] = """Equation"""
        #self.vs[40]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # apply attribute equation left expr channel() node
        self.add_node()
        self.vs[41]["mm__"] = """leftExpr"""
        #self.vs[41]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # apply attribute equation right expr channel() node
        self.add_node()
        self.vs[42]["mm__"] = """rightExpr"""
        #self.vs[42]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class State()
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class Transition()
                (0,8), # matchmodel -> match_contains
                (8,7), # match_contains -> match_class Trigger()
                (0,10), # matchmodel -> match_contains
                (10,9), # match_contains -> match_class Signal()
                (1,12), # applymodel -> apply_contains
                (12,11), # apply_contains -> apply_class Listen()
                (1,14), # applymodel -> apply_contains
                (14,13), # apply_contains -> apply_class ListenBranch()
                (1,16), # applymodel -> apply_contains
                (16,15), # apply_contains -> apply_class Inst()
                (3,17), # match_class State() -> association outgoingTransitions
                (17,5), # association outgoingTransitions  -> match_class Transition()
                (5,18), # match_class Transition() -> association triggers
                (18,7), # association triggers  -> match_class Trigger()
                (7,19), # match_class Trigger() -> association signal
                (19,9), # association signal  -> match_class Signal()
                (11,20), # apply_class Listen() -> association branches
                (20,13), # association branches  -> apply_class ListenBranch()
                (13,21), # apply_class ListenBranch() -> association p
                (21,15), # association p  -> apply_class Inst()
                (11,22), # apply_class Listen() -> backward_association
                (22,3), #  backward_association -> apply_class State()
                (15,23), # apply_class Inst() -> backward_association
                (23,5), #  backward_association -> apply_class Transition()
                (3,24), # match_class State() -> has_match_attribute isComposite ()
                (24,25), #  has_match_attribute isComposite () -> match_attribute isComposite ()
                (26,27), #  equation of match attribute isComposite () -> left_expr
                (27,25), #  left_expr -> match_attribute isComposite ()
                (26,28), #  equation of match attribute isComposite () -> right_expr
                (28,29), # right_expr --> term
                (3,30), # match_class State() -> has_match_attribute hasOutgoingTransitions ()
                (30,31), #  has_match_attribute hasOutgoingTransitions () -> match_attribute hasOutgoingTransitions ()
                (32,33), #  equation of match attribute hasOutgoingTransitions () -> left_expr
                (33,31), #  left_expr -> match_attribute hasOutgoingTransitions ()
                (32,34), #  equation of match attribute hasOutgoingTransitions () -> right_expr
                (34,35), # right_expr --> term
                (9,36), # match_class Signal() -> has_match_attribute name ()
                (36,37), #  has_match_attribute name () -> match_attribute name ()
                (13,38), # apply_class ListenBranch() -> has_apply_attribute channel ()
                (38,39), #  has_apply_attribute channel () -> apply_attribute channel ()
                (40,41), #  equation of apply attribute channel () -> left_expr
                (41,39), #  left_expr -> apply_attribute channel ()
                (40,42), #  equation of apply attribute channel () -> right_expr
                (42,37), # right_expr --> term
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel
        ])
        
