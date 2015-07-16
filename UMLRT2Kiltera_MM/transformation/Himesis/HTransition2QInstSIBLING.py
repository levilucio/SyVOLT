from core.himesis import Himesis
import uuid

class HTransition2QInstSIBLING(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule Transition2QInstSIBLING.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HTransition2QInstSIBLING, self).__init__(name='HTransition2QInstSIBLING', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """Transition2QInstSIBLING"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Transition2QInstSIBLING')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Transition2QInstSIBLINGmatchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Transition2QInstSIBLINGapplymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Transition2QInstSIBLINGpairedwith2')
        self.vs[2]["rulename"] = """Transition2QInstSIBLING"""
        
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
        # match class Vertex() node
        self.add_node()
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """Vertex"""
        self.vs[5]["mm__"] = """Vertex"""
        self.vs[5]["cardinality"] = """1"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match_contains node for class Vertex()
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        #self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'matchcontains6')
        # match class SIBLING0() node
        self.add_node()
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """SIBLING0"""
        self.vs[7]["mm__"] = """SIBLING0"""
        self.vs[7]["cardinality"] = """1"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match_contains node for class SIBLING0()
        self.add_node()
        self.vs[8]["mm__"] = """match_contains"""
        #self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'matchcontains8')
        # match class StateMachine() node
        self.add_node()
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """StateMachine"""
        self.vs[9]["mm__"] = """StateMachine"""
        self.vs[9]["cardinality"] = """1"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match_contains node for class StateMachine()
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
        # apply class Name() node
        self.add_node()
        self.vs[15]["name"] = """"""
        self.vs[15]["classtype"] = """Name"""
        self.vs[15]["mm__"] = """Name"""
        self.vs[15]["cardinality"] = """1"""
        #self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply_contains node for class Name()
        self.add_node()
        self.vs[16]["mm__"] = """apply_contains"""
        #self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains16')
        # apply class Name() node
        self.add_node()
        self.vs[17]["name"] = """"""
        self.vs[17]["classtype"] = """Name"""
        self.vs[17]["mm__"] = """Name"""
        self.vs[17]["cardinality"] = """1"""
        #self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply_contains node for class Name()
        self.add_node()
        self.vs[18]["mm__"] = """apply_contains"""
        #self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains18')
        # apply class Name() node
        self.add_node()
        self.vs[19]["name"] = """"""
        self.vs[19]["classtype"] = """Name"""
        self.vs[19]["mm__"] = """Name"""
        self.vs[19]["cardinality"] = """1"""
        #self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply_contains node for class Name()
        self.add_node()
        self.vs[20]["mm__"] = """apply_contains"""
        #self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains20')
        
        
        # match association Transition--dest-->Vertex node
        self.add_node()
        self.vs[21]["associationType"] = """dest"""
        self.vs[21]["mm__"] = """directLink_S"""
        #self.vs[21]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc21')
        # match association Transition--type-->SIBLING0 node
        self.add_node()
        self.vs[22]["associationType"] = """type"""
        self.vs[22]["mm__"] = """directLink_S"""
        #self.vs[22]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc22')
        # match association Vertex--owningStateMachine-->StateMachine node
        self.add_node()
        self.vs[23]["associationType"] = """owningStateMachine"""
        self.vs[23]["mm__"] = """directLink_S"""
        #self.vs[23]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc23')
        
        # apply association Inst--channelNames-->Name node
        self.add_node()
        self.vs[24]["associationType"] = """channelNames"""
        self.vs[24]["mm__"] = """directLink_T"""
        #self.vs[24]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc24')
        # apply association Inst--channelNames-->Name node
        self.add_node()
        self.vs[25]["associationType"] = """channelNames"""
        self.vs[25]["mm__"] = """directLink_T"""
        #self.vs[25]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc25')
        # apply association Inst--channelNames-->Name node
        self.add_node()
        self.vs[26]["associationType"] = """channelNames"""
        self.vs[26]["mm__"] = """directLink_T"""
        #self.vs[26]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc26')
        # apply association Inst--channelNames-->Name node
        self.add_node()
        self.vs[27]["associationType"] = """channelNames"""
        self.vs[27]["mm__"] = """directLink_T"""
        #self.vs[27]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc27')
        
        
        
        # has match attribute name() node
        self.add_node()
        self.vs[28]["mm__"] = """hasAttribute_S"""
        #self.vs[28]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # match attribute name() node
        self.add_node()
        self.vs[29]["name"] = """name"""
        self.vs[29]["mm__"] = """Attribute"""
        self.vs[29]["Type"] = """'String'"""
        #self.vs[29]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # has match attribute name() node
        self.add_node()
        self.vs[30]["mm__"] = """hasAttribute_S"""
        #self.vs[30]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # match attribute name() node
        self.add_node()
        self.vs[31]["name"] = """name"""
        self.vs[31]["mm__"] = """Attribute"""
        self.vs[31]["Type"] = """'String'"""
        #self.vs[31]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        
        
        # has apply attribute name() node
        self.add_node()
        self.vs[32]["mm__"] = """hasAttribute_T"""
        #self.vs[32]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # apply attribute name() node
        self.add_node()
        self.vs[33]["name"] = """name"""
        self.vs[33]["mm__"] = """Attribute"""
        self.vs[33]["Type"] = """'String'"""
        #self.vs[33]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply attribute equation name() node
        self.add_node()
        self.vs[34]["name"] = """eq_"""
        self.vs[34]["mm__"] = """Equation"""
        #self.vs[34]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # apply attribute equation left expr name() node
        self.add_node()
        self.vs[35]["mm__"] = """leftExpr"""
        #self.vs[35]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # apply attribute equation right expr name() node
        self.add_node()
        self.vs[36]["mm__"] = """rightExpr"""
        #self.vs[36]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # attribute concat name() node
        self.add_node()
        self.vs[37]["name"] = """Concat37"""
        self.vs[37]["mm__"] = """Concat"""
        self.vs[37]["Type"] = """'String'"""
        #self.vs[37]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concat37')
        # apply attribute concat has left args name() node
        self.add_node()
        self.vs[38]["mm__"] = """hasArgs"""
        #self.vs[38]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgs38')
        # apply attribute concat has right args name() node
        self.add_node()
        self.vs[39]["mm__"] = """hasArgs"""
        #self.vs[39]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgs39')
        # apply attribute atom name() node
        self.add_node()
        self.vs[40]["name"] = """S"""
        self.vs[40]["mm__"] = """Constant"""
        self.vs[40]["Type"] = """'String'"""
        #self.vs[40]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom40')
        # has apply attribute literal() node
        self.add_node()
        self.vs[41]["mm__"] = """hasAttribute_T"""
        #self.vs[41]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # apply attribute literal() node
        self.add_node()
        self.vs[42]["name"] = """literal"""
        self.vs[42]["mm__"] = """Attribute"""
        self.vs[42]["Type"] = """'String'"""
        #self.vs[42]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply attribute equation literal() node
        self.add_node()
        self.vs[43]["name"] = """eq_"""
        self.vs[43]["mm__"] = """Equation"""
        #self.vs[43]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # apply attribute equation left expr literal() node
        self.add_node()
        self.vs[44]["mm__"] = """leftExpr"""
        #self.vs[44]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # apply attribute equation right expr literal() node
        self.add_node()
        self.vs[45]["mm__"] = """rightExpr"""
        #self.vs[45]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # apply attribute atom literal() node
        self.add_node()
        self.vs[46]["name"] = """exack"""
        self.vs[46]["mm__"] = """Constant"""
        self.vs[46]["Type"] = """'String'"""
        #self.vs[46]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom46')
        # has apply attribute literal() node
        self.add_node()
        self.vs[47]["mm__"] = """hasAttribute_T"""
        #self.vs[47]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # apply attribute literal() node
        self.add_node()
        self.vs[48]["name"] = """literal"""
        self.vs[48]["mm__"] = """Attribute"""
        self.vs[48]["Type"] = """'String'"""
        #self.vs[48]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply attribute equation literal() node
        self.add_node()
        self.vs[49]["name"] = """eq_"""
        self.vs[49]["mm__"] = """Equation"""
        #self.vs[49]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # apply attribute equation left expr literal() node
        self.add_node()
        self.vs[50]["mm__"] = """leftExpr"""
        #self.vs[50]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # apply attribute equation right expr literal() node
        self.add_node()
        self.vs[51]["mm__"] = """rightExpr"""
        #self.vs[51]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # attribute concat literal() node
        self.add_node()
        self.vs[52]["name"] = """Concat52"""
        self.vs[52]["mm__"] = """Concat"""
        self.vs[52]["Type"] = """'String'"""
        #self.vs[52]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concat52')
        # apply attribute concat has left args literal() node
        self.add_node()
        self.vs[53]["mm__"] = """hasArgs"""
        #self.vs[53]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgs53')
        # apply attribute concat has right args literal() node
        self.add_node()
        self.vs[54]["mm__"] = """hasArgs"""
        #self.vs[54]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgs54')
        # apply attribute atom literal() node
        self.add_node()
        self.vs[55]["name"] = """A"""
        self.vs[55]["mm__"] = """Constant"""
        self.vs[55]["Type"] = """'String'"""
        #self.vs[55]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom55')
        # attribute concat literal() node
        self.add_node()
        self.vs[56]["name"] = """Concat56"""
        self.vs[56]["mm__"] = """Concat"""
        self.vs[56]["Type"] = """'String'"""
        #self.vs[56]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concat56')
        # apply attribute concat has left args literal() node
        self.add_node()
        self.vs[57]["mm__"] = """hasArgs"""
        #self.vs[57]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgs57')
        # apply attribute concat has right args literal() node
        self.add_node()
        self.vs[58]["mm__"] = """hasArgs"""
        #self.vs[58]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgs58')
        # apply attribute atom literal() node
        self.add_node()
        self.vs[59]["name"] = """A"""
        self.vs[59]["mm__"] = """Constant"""
        self.vs[59]["Type"] = """'String'"""
        #self.vs[59]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom59')
        # has apply attribute literal() node
        self.add_node()
        self.vs[60]["mm__"] = """hasAttribute_T"""
        #self.vs[60]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # apply attribute literal() node
        self.add_node()
        self.vs[61]["name"] = """literal"""
        self.vs[61]["mm__"] = """Attribute"""
        self.vs[61]["Type"] = """'String'"""
        #self.vs[61]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply attribute equation literal() node
        self.add_node()
        self.vs[62]["name"] = """eq_"""
        self.vs[62]["mm__"] = """Equation"""
        #self.vs[62]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # apply attribute equation left expr literal() node
        self.add_node()
        self.vs[63]["mm__"] = """leftExpr"""
        #self.vs[63]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # apply attribute equation right expr literal() node
        self.add_node()
        self.vs[64]["mm__"] = """rightExpr"""
        #self.vs[64]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # apply attribute atom literal() node
        self.add_node()
        self.vs[65]["name"] = """exit"""
        self.vs[65]["mm__"] = """Constant"""
        self.vs[65]["Type"] = """'String'"""
        #self.vs[65]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom65')
        # has apply attribute literal() node
        self.add_node()
        self.vs[66]["mm__"] = """hasAttribute_T"""
        #self.vs[66]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # apply attribute literal() node
        self.add_node()
        self.vs[67]["name"] = """literal"""
        self.vs[67]["mm__"] = """Attribute"""
        self.vs[67]["Type"] = """'String'"""
        #self.vs[67]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply attribute equation literal() node
        self.add_node()
        self.vs[68]["name"] = """eq_"""
        self.vs[68]["mm__"] = """Equation"""
        #self.vs[68]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # apply attribute equation left expr literal() node
        self.add_node()
        self.vs[69]["mm__"] = """leftExpr"""
        #self.vs[69]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # apply attribute equation right expr literal() node
        self.add_node()
        self.vs[70]["mm__"] = """rightExpr"""
        #self.vs[70]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # apply attribute atom literal() node
        self.add_node()
        self.vs[71]["name"] = """sh"""
        self.vs[71]["mm__"] = """Constant"""
        self.vs[71]["Type"] = """'String'"""
        #self.vs[71]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom71')
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class Transition()
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class Vertex()
                (0,8), # matchmodel -> match_contains
                (8,7), # match_contains -> match_class SIBLING0()
                (0,10), # matchmodel -> match_contains
                (10,9), # match_contains -> match_class StateMachine()
                (1,12), # applymodel -> apply_contains
                (12,11), # apply_contains -> apply_class Inst()
                (1,14), # applymodel -> apply_contains
                (14,13), # apply_contains -> apply_class Name()
                (1,16), # applymodel -> apply_contains
                (16,15), # apply_contains -> apply_class Name()
                (1,18), # applymodel -> apply_contains
                (18,17), # apply_contains -> apply_class Name()
                (1,20), # applymodel -> apply_contains
                (20,19), # apply_contains -> apply_class Name()
                (3,21), # match_class Transition() -> association dest
                (21,5), # association dest  -> match_class Vertex()
                (3,22), # match_class Transition() -> association type
                (22,7), # association type  -> match_class SIBLING0()
                (5,23), # match_class Vertex() -> association owningStateMachine
                (23,9), # association owningStateMachine  -> match_class StateMachine()
                (11,24), # apply_class Inst() -> association channelNames
                (24,17), # association channelNames  -> apply_class Name()
                (11,25), # apply_class Inst() -> association channelNames
                (25,13), # association channelNames  -> apply_class Name()
                (11,26), # apply_class Inst() -> association channelNames
                (26,15), # association channelNames  -> apply_class Name()
                (11,27), # apply_class Inst() -> association channelNames
                (27,19), # association channelNames  -> apply_class Name()
                (5,28), # match_class Vertex() -> has_match_attribute name ()
                (28,29), #  has_match_attribute name () -> match_attribute name ()
                (9,30), # match_class StateMachine() -> has_match_attribute name ()
                (30,31), #  has_match_attribute name () -> match_attribute name ()
                (11,32), # apply_class Inst() -> has_apply_attribute name ()
                (32,33), #  has_apply_attribute name () -> apply_attribute name ()
                (34,35), #  equation of apply attribute name () -> left_expr
                (35,33), #  left_expr -> apply_attribute name ()
                (34,36), #  equation of apply attribute name () -> right_expr
                (37,38), #  apply attribute concat name () -> left has_args
                (38,40), #  left has_args -> term
                (37,39), #  apply attribute concat name () -> right has_args
                (39,31), #  right has_args -> term
                (36,37), # right_expr --> term
                (13,41), # apply_class Name() -> has_apply_attribute literal ()
                (41,42), #  has_apply_attribute literal () -> apply_attribute literal ()
                (43,44), #  equation of apply attribute literal () -> left_expr
                (44,42), #  left_expr -> apply_attribute literal ()
                (43,45), #  equation of apply attribute literal () -> right_expr
                (45,46), # right_expr --> term
                (15,47), # apply_class Name() -> has_apply_attribute literal ()
                (47,48), #  has_apply_attribute literal () -> apply_attribute literal ()
                (49,50), #  equation of apply attribute literal () -> left_expr
                (50,48), #  left_expr -> apply_attribute literal ()
                (49,51), #  equation of apply attribute literal () -> right_expr
                (56,57), #  apply attribute concat literal () -> left has_args
                (57,29), #  left has_args -> term
                (56,58), #  apply attribute concat literal () -> right has_args
                (58,59), #  right has_args -> term
                (52,53), #  apply attribute concat literal () -> left has_args
                (53,55), #  left has_args -> term
                (52,54), #  apply attribute concat literal () -> right has_args
                (54,56), #  right has_args -> term
                (51,52), # right_expr --> term
                (17,60), # apply_class Name() -> has_apply_attribute literal ()
                (60,61), #  has_apply_attribute literal () -> apply_attribute literal ()
                (62,63), #  equation of apply attribute literal () -> left_expr
                (63,61), #  left_expr -> apply_attribute literal ()
                (62,64), #  equation of apply attribute literal () -> right_expr
                (64,65), # right_expr --> term
                (19,66), # apply_class Name() -> has_apply_attribute literal ()
                (66,67), #  has_apply_attribute literal () -> apply_attribute literal ()
                (68,69), #  equation of apply attribute literal () -> left_expr
                (69,67), #  left_expr -> apply_attribute literal ()
                (68,70), #  equation of apply attribute literal () -> right_expr
                (70,71), # right_expr --> term
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel
        ])
        
