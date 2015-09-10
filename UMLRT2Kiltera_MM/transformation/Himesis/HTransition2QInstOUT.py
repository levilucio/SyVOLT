from core.himesis import Himesis
import uuid

class HTransition2QInstOUT(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule Transition2QInstOUT.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HTransition2QInstOUT, self).__init__(name='HTransition2QInstOUT', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """Transition2QInstOUT"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Transition2QInstOUT')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Transition2QInstOUTmatchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Transition2QInstOUTapplymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Transition2QInstOUTpairedwith2')
        self.vs[2]["rulename"] = """Transition2QInstOUT"""
        
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
        # match class OUT2() node
        self.add_node()
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """OUT2"""
        self.vs[5]["mm__"] = """OUT2"""
        self.vs[5]["cardinality"] = """1"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match_contains node for class OUT2()
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        #self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'matchcontains6')
        # match class StateMachine() node
        self.add_node()
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """StateMachine"""
        self.vs[7]["mm__"] = """StateMachine"""
        self.vs[7]["cardinality"] = """1"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match_contains node for class StateMachine()
        self.add_node()
        self.vs[8]["mm__"] = """match_contains"""
        #self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'matchcontains8')
        # match class Vertex() node
        self.add_node()
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """Vertex"""
        self.vs[9]["mm__"] = """Vertex"""
        self.vs[9]["cardinality"] = """1"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match_contains node for class Vertex()
        self.add_node()
        self.vs[10]["mm__"] = """match_contains"""
        #self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'matchcontains10')
        
        
        # apply class Inst() node
        self.add_node()
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """Inst"""
        self.vs[11]["mm__"] = """Inst"""
        self.vs[11]["cardinality"] = """1"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply_contains node for class Inst()
        self.add_node()
        self.vs[12]["mm__"] = """apply_contains"""
        #self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains12')
        # apply class Name() node
        self.add_node()
        self.vs[13]["name"] = """"""
        self.vs[13]["classtype"] = """Name"""
        self.vs[13]["mm__"] = """Name"""
        self.vs[13]["cardinality"] = """1"""
        #self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply_contains node for class Name()
        self.add_node()
        self.vs[14]["mm__"] = """apply_contains"""
        #self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains14')
        
        
        # match association Transition--type-->OUT2 node
        self.add_node()
        self.vs[15]["associationType"] = """type"""
        self.vs[15]["mm__"] = """directLink_S"""
        #self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc15')
        # match association Transition--owningStateMachine-->StateMachine node
        self.add_node()
        self.vs[16]["associationType"] = """owningStateMachine"""
        self.vs[16]["mm__"] = """directLink_S"""
        #self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc16')
        # match association StateMachine--exitPoints-->Vertex node
        self.add_node()
        self.vs[17]["associationType"] = """exitPoints"""
        self.vs[17]["mm__"] = """directLink_S"""
        #self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc17')
        # match association Transition--dest-->Vertex node
        self.add_node()
        self.vs[18]["associationType"] = """dest"""
        self.vs[18]["mm__"] = """directLink_S"""
        #self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc18')
        
        # apply association Inst--channelNames-->Name node
        self.add_node()
        self.vs[19]["associationType"] = """channelNames"""
        self.vs[19]["mm__"] = """directLink_T"""
        #self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc19')
        
        
        
        # has match attribute name() node
        self.add_node()
        self.vs[20]["mm__"] = """hasAttribute_S"""
        #self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # match attribute name() node
        self.add_node()
        self.vs[21]["name"] = """name"""
        self.vs[21]["mm__"] = """Attribute"""
        self.vs[21]["Type"] = """'String'"""
        #self.vs[21]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        
        
        # has apply attribute name() node
        self.add_node()
        self.vs[22]["mm__"] = """hasAttribute_T"""
        #self.vs[22]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # apply attribute name() node
        self.add_node()
        self.vs[23]["name"] = """name"""
        self.vs[23]["mm__"] = """Attribute"""
        self.vs[23]["Type"] = """'String'"""
        #self.vs[23]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply attribute equation name() node
        self.add_node()
        self.vs[24]["name"] = """eq_"""
        self.vs[24]["mm__"] = """Equation"""
        #self.vs[24]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # apply attribute equation left expr name() node
        self.add_node()
        self.vs[25]["mm__"] = """leftExpr"""
        #self.vs[25]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # apply attribute equation right expr name() node
        self.add_node()
        self.vs[26]["mm__"] = """rightExpr"""
        #self.vs[26]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # attribute concat name() node
        self.add_node()
        self.vs[27]["name"] = """Concat27"""
        self.vs[27]["mm__"] = """Concat"""
        self.vs[27]["Type"] = """'String'"""
        #self.vs[27]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concat27')
        # apply attribute concat has left args name() node
        self.add_node()
        self.vs[28]["mm__"] = """hasArgs"""
        #self.vs[28]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgs28')
        # apply attribute concat has right args name() node
        self.add_node()
        self.vs[29]["mm__"] = """hasArgs"""
        #self.vs[29]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgs29')
        # apply attribute atom name() node
        self.add_node()
        self.vs[30]["name"] = """B"""
        self.vs[30]["mm__"] = """Constant"""
        self.vs[30]["Type"] = """'String'"""
        #self.vs[30]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom30')
        # has apply attribute literal() node
        self.add_node()
        self.vs[31]["mm__"] = """hasAttribute_T"""
        #self.vs[31]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # apply attribute literal() node
        self.add_node()
        self.vs[32]["name"] = """literal"""
        self.vs[32]["mm__"] = """Attribute"""
        self.vs[32]["Type"] = """'String'"""
        #self.vs[32]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply attribute equation literal() node
        self.add_node()
        self.vs[33]["name"] = """eq_"""
        self.vs[33]["mm__"] = """Equation"""
        #self.vs[33]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # apply attribute equation left expr literal() node
        self.add_node()
        self.vs[34]["mm__"] = """leftExpr"""
        #self.vs[34]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # apply attribute equation right expr literal() node
        self.add_node()
        self.vs[35]["mm__"] = """rightExpr"""
        #self.vs[35]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # apply attribute atom literal() node
        self.add_node()
        self.vs[36]["name"] = """sh"""
        self.vs[36]["mm__"] = """Constant"""
        self.vs[36]["Type"] = """'String'"""
        #self.vs[36]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom36')
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class Transition()
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class OUT2()
                (0,8), # matchmodel -> match_contains
                (8,7), # match_contains -> match_class StateMachine()
                (0,10), # matchmodel -> match_contains
                (10,9), # match_contains -> match_class Vertex()
                (1,12), # applymodel -> apply_contains
                (12,11), # apply_contains -> apply_class Inst()
                (1,14), # applymodel -> apply_contains
                (14,13), # apply_contains -> apply_class Name()
                (3,15), # match_class Transition() -> association type
                (15,5), # association type  -> match_class OUT2()
                (3,16), # match_class Transition() -> association owningStateMachine
                (16,7), # association owningStateMachine  -> match_class StateMachine()
                (7,17), # match_class StateMachine() -> association exitPoints
                (17,9), # association exitPoints  -> match_class Vertex()
                (3,18), # match_class Transition() -> association dest
                (18,9), # association dest  -> match_class Vertex()
                (11,19), # apply_class Inst() -> association channelNames
                (19,13), # association channelNames  -> apply_class Name()
                (9,20), # match_class Vertex() -> has_match_attribute name ()
                (20,21), #  has_match_attribute name () -> match_attribute name ()
                (11,22), # apply_class Inst() -> has_apply_attribute name ()
                (22,23), #  has_apply_attribute name () -> apply_attribute name ()
                (24,25), #  equation of apply attribute name () -> left_expr
                (25,23), #  left_expr -> apply_attribute name ()
                (24,26), #  equation of apply attribute name () -> right_expr
                (27,28), #  apply attribute concat name () -> left has_args
                (28,30), #  left has_args -> term
                (27,29), #  apply attribute concat name () -> right has_args
                (29,21), #  right has_args -> term
                (26,27), # right_expr --> term
                (13,31), # apply_class Name() -> has_apply_attribute literal ()
                (31,32), #  has_apply_attribute literal () -> apply_attribute literal ()
                (33,34), #  equation of apply attribute literal () -> left_expr
                (34,32), #  left_expr -> apply_attribute literal ()
                (33,35), #  equation of apply attribute literal () -> right_expr
                (35,36), # right_expr --> term
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel
        ])
        
