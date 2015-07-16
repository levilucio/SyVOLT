from core.himesis import Himesis
import uuid

class HConnectOPState2CProcDefTransition2InstotherInTransitions(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule ConnectOPState2CProcDefTransition2InstotherInTransitions.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HConnectOPState2CProcDefTransition2InstotherInTransitions, self).__init__(name='HConnectOPState2CProcDefTransition2InstotherInTransitions', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """ConnectOPState2CProcDefTransition2InstotherInTransitions"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConnectOPState2CProcDefTransition2InstotherInTransitions')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConnectOPState2CProcDefTransition2InstotherInTransitionsmatchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConnectOPState2CProcDefTransition2InstotherInTransitionsapplymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConnectOPState2CProcDefTransition2InstotherInTransitionspairedwith2')
        self.vs[2]["rulename"] = """ConnectOPState2CProcDefTransition2InstotherInTransitions"""
        
        # match class Transition() node
        self.add_node()
        self.vs[3]["name"] = """"""
        self.vs[3]["classtype"] = """Transition"""
        self.vs[3]["mm__"] = """Transition"""
        self.vs[3]["cardinality"] = """+"""
        #self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match_contains node for class Transition()
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        #self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'matchcontains4')
        # match class IN1() node
        self.add_node()
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """IN1"""
        self.vs[5]["mm__"] = """IN1"""
        self.vs[5]["cardinality"] = """+"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match_contains node for class IN1()
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        #self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'matchcontains6')
        # match class State() node
        self.add_node()
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """State"""
        self.vs[7]["mm__"] = """State"""
        self.vs[7]["cardinality"] = """+"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match_contains node for class State()
        self.add_node()
        self.vs[8]["mm__"] = """match_contains"""
        #self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'matchcontains8')
        # match class Vertex() node
        self.add_node()
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """Vertex"""
        self.vs[9]["mm__"] = """Vertex"""
        self.vs[9]["cardinality"] = """+"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match_contains node for class Vertex()
        self.add_node()
        self.vs[10]["mm__"] = """match_contains"""
        #self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'matchcontains10')
        
        
        # apply class ConditionSet() node
        self.add_node()
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """ConditionSet"""
        self.vs[11]["mm__"] = """ConditionSet"""
        self.vs[11]["cardinality"] = """1"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply_contains node for class ConditionSet()
        self.add_node()
        self.vs[12]["mm__"] = """apply_contains"""
        #self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains12')
        # apply class ConditionBranch() node
        self.add_node()
        self.vs[13]["name"] = """"""
        self.vs[13]["classtype"] = """ConditionBranch"""
        self.vs[13]["mm__"] = """ConditionBranch"""
        self.vs[13]["cardinality"] = """1"""
        #self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply_contains node for class ConditionBranch()
        self.add_node()
        self.vs[14]["mm__"] = """apply_contains"""
        #self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains14')
        # apply class Expr() node
        self.add_node()
        self.vs[15]["name"] = """"""
        self.vs[15]["classtype"] = """Expr"""
        self.vs[15]["mm__"] = """Expr"""
        self.vs[15]["cardinality"] = """1"""
        #self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply_contains node for class Expr()
        self.add_node()
        self.vs[16]["mm__"] = """apply_contains"""
        #self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains16')
        # apply class Inst() node
        self.add_node()
        self.vs[17]["name"] = """"""
        self.vs[17]["classtype"] = """Inst"""
        self.vs[17]["mm__"] = """Inst"""
        self.vs[17]["cardinality"] = """1"""
        #self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply_contains node for class Inst()
        self.add_node()
        self.vs[18]["mm__"] = """apply_contains"""
        #self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains18')
        
        
        # match association State--transitions-->Transition node
        self.add_node()
        self.vs[19]["associationType"] = """transitions"""
        self.vs[19]["mm__"] = """directLink_S"""
        #self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc19')
        # match association Transition--type-->IN1 node
        self.add_node()
        self.vs[20]["associationType"] = """type"""
        self.vs[20]["mm__"] = """directLink_S"""
        #self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc20')
        # match association Transition--src-->Vertex node
        self.add_node()
        self.vs[21]["associationType"] = """src"""
        self.vs[21]["mm__"] = """directLink_S"""
        #self.vs[21]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc21')
        
        # apply association ConditionSet--branches-->ConditionBranch node
        self.add_node()
        self.vs[22]["associationType"] = """branches"""
        self.vs[22]["mm__"] = """directLink_T"""
        #self.vs[22]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc22')
        # apply association ConditionBranch--if-->Expr node
        self.add_node()
        self.vs[23]["associationType"] = """if"""
        self.vs[23]["mm__"] = """directLink_T"""
        #self.vs[23]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc23')
        # apply association ConditionBranch--then-->Inst node
        self.add_node()
        self.vs[24]["associationType"] = """then"""
        self.vs[24]["mm__"] = """directLink_T"""
        #self.vs[24]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc24')
        
        # backward association State---->ConditionSet node
        self.add_node()
        self.vs[25]["type"] = """ruleDef"""
        self.vs[25]["mm__"] = """backward_link"""
        #self.vs[25]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'blink25')
        # backward association Transition---->Inst node
        self.add_node()
        self.vs[26]["type"] = """ruleDef"""
        self.vs[26]["mm__"] = """backward_link"""
        #self.vs[26]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'blink26')
        
        
        # has match attribute isComposite() node
        self.add_node()
        self.vs[27]["mm__"] = """hasAttribute_S"""
        #self.vs[27]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # match attribute isComposite() node
        self.add_node()
        self.vs[28]["name"] = """isComposite"""
        self.vs[28]["mm__"] = """Attribute"""
        self.vs[28]["Type"] = """'String'"""
        #self.vs[28]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match attribute equation isComposite() node
        self.add_node()
        self.vs[29]["name"] = """eq_"""
        self.vs[29]["mm__"] = """Equation"""
        #self.vs[29]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # match attribute equation left expr isComposite() node
        self.add_node()
        self.vs[30]["mm__"] = """leftExpr"""
        #self.vs[30]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # match attribute equation right expr isComposite() node
        self.add_node()
        self.vs[31]["mm__"] = """rightExpr"""
        #self.vs[31]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # apply attribute atom isComposite() node
        self.add_node()
        self.vs[32]["name"] = """true"""
        self.vs[32]["mm__"] = """Constant"""
        self.vs[32]["Type"] = """'String'"""
        #self.vs[32]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom32')
        # has match attribute name() node
        self.add_node()
        self.vs[33]["mm__"] = """hasAttribute_S"""
        #self.vs[33]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # match attribute name() node
        self.add_node()
        self.vs[34]["name"] = """name"""
        self.vs[34]["mm__"] = """Attribute"""
        self.vs[34]["Type"] = """'String'"""
        #self.vs[34]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        
        
        # has apply attribute literal() node
        self.add_node()
        self.vs[35]["mm__"] = """hasAttribute_T"""
        #self.vs[35]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # apply attribute literal() node
        self.add_node()
        self.vs[36]["name"] = """literal"""
        self.vs[36]["mm__"] = """Attribute"""
        self.vs[36]["Type"] = """'String'"""
        #self.vs[36]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply attribute equation literal() node
        self.add_node()
        self.vs[37]["name"] = """eq_"""
        self.vs[37]["mm__"] = """Equation"""
        #self.vs[37]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # apply attribute equation left expr literal() node
        self.add_node()
        self.vs[38]["mm__"] = """leftExpr"""
        #self.vs[38]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # apply attribute equation right expr literal() node
        self.add_node()
        self.vs[39]["mm__"] = """rightExpr"""
        #self.vs[39]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # attribute concat literal() node
        self.add_node()
        self.vs[40]["name"] = """Concat40"""
        self.vs[40]["mm__"] = """Concat"""
        self.vs[40]["Type"] = """'String'"""
        #self.vs[40]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concat40')
        # apply attribute concat has left args literal() node
        self.add_node()
        self.vs[41]["mm__"] = """hasArgs"""
        #self.vs[41]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgs41')
        # apply attribute concat has right args literal() node
        self.add_node()
        self.vs[42]["mm__"] = """hasArgs"""
        #self.vs[42]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgs42')
        # apply attribute atom literal() node
        self.add_node()
        self.vs[43]["name"] = """enp=A"""
        self.vs[43]["mm__"] = """Constant"""
        self.vs[43]["Type"] = """'String'"""
        #self.vs[43]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom43')
        # attribute concat literal() node
        self.add_node()
        self.vs[44]["name"] = """Concat44"""
        self.vs[44]["mm__"] = """Concat"""
        self.vs[44]["Type"] = """'String'"""
        #self.vs[44]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concat44')
        # apply attribute concat has left args literal() node
        self.add_node()
        self.vs[45]["mm__"] = """hasArgs"""
        #self.vs[45]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgs45')
        # apply attribute concat has right args literal() node
        self.add_node()
        self.vs[46]["mm__"] = """hasArgs"""
        #self.vs[46]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgs46')
        # apply attribute atom literal() node
        self.add_node()
        self.vs[47]["name"] = """A"""
        self.vs[47]["mm__"] = """Constant"""
        self.vs[47]["Type"] = """'String'"""
        #self.vs[47]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom47')
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class Transition()
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class IN1()
                (0,8), # matchmodel -> match_contains
                (8,7), # match_contains -> match_class State()
                (0,10), # matchmodel -> match_contains
                (10,9), # match_contains -> match_class Vertex()
                (1,12), # applymodel -> apply_contains
                (12,11), # apply_contains -> apply_class ConditionSet()
                (1,14), # applymodel -> apply_contains
                (14,13), # apply_contains -> apply_class ConditionBranch()
                (1,16), # applymodel -> apply_contains
                (16,15), # apply_contains -> apply_class Expr()
                (1,18), # applymodel -> apply_contains
                (18,17), # apply_contains -> apply_class Inst()
                (7,19), # match_class State() -> association transitions
                (19,3), # association transitions  -> match_class Transition()
                (3,20), # match_class Transition() -> association type
                (20,5), # association type  -> match_class IN1()
                (3,21), # match_class Transition() -> association src
                (21,9), # association src  -> match_class Vertex()
                (11,22), # apply_class ConditionSet() -> association branches
                (22,13), # association branches  -> apply_class ConditionBranch()
                (13,23), # apply_class ConditionBranch() -> association if
                (23,15), # association if  -> apply_class Expr()
                (13,24), # apply_class ConditionBranch() -> association then
                (24,17), # association then  -> apply_class Inst()
                (11,25), # apply_class ConditionSet() -> backward_association
                (25,7), #  backward_association -> apply_class State()
                (17,26), # apply_class Inst() -> backward_association
                (26,3), #  backward_association -> apply_class Transition()
                (7,27), # match_class State() -> has_match_attribute isComposite ()
                (27,28), #  has_match_attribute isComposite () -> match_attribute isComposite ()
                (29,30), #  equation of match attribute isComposite () -> left_expr
                (30,28), #  left_expr -> match_attribute isComposite ()
                (29,31), #  equation of match attribute isComposite () -> right_expr
                (31,32), # right_expr --> term
                (9,33), # match_class Vertex() -> has_match_attribute name ()
                (33,34), #  has_match_attribute name () -> match_attribute name ()
                (15,35), # apply_class Expr() -> has_apply_attribute literal ()
                (35,36), #  has_apply_attribute literal () -> apply_attribute literal ()
                (37,38), #  equation of apply attribute literal () -> left_expr
                (38,36), #  left_expr -> apply_attribute literal ()
                (37,39), #  equation of apply attribute literal () -> right_expr
                (44,45), #  apply attribute concat literal () -> left has_args
                (45,34), #  left has_args -> term
                (44,46), #  apply attribute concat literal () -> right has_args
                (46,47), #  right has_args -> term
                (40,41), #  apply attribute concat literal () -> left has_args
                (41,43), #  left has_args -> term
                (40,42), #  apply attribute concat literal () -> right has_args
                (42,44), #  right has_args -> term
                (39,40), # right_expr --> term
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel
        ])
        
