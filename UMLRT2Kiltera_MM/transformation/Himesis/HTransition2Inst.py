from core.himesis import Himesis
import uuid

class HTransition2Inst(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule Transition2Inst.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HTransition2Inst, self).__init__(name='HTransition2Inst', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """Transition2Inst"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Transition2Inst')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Transition2Instmatchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Transition2Instapplymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Transition2Instpairedwith2')
        self.vs[2]["rulename"] = """Transition2Inst"""
        
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
        # match class IN1() node
        self.add_node()
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """IN1"""
        self.vs[7]["mm__"] = """IN1"""
        self.vs[7]["cardinality"] = """1"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match_contains node for class IN1()
        self.add_node()
        self.vs[8]["mm__"] = """match_contains"""
        #self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'matchcontains8')
        # match class EntryPoint() node
        self.add_node()
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """EntryPoint"""
        self.vs[9]["mm__"] = """EntryPoint"""
        self.vs[9]["cardinality"] = """1"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match_contains node for class EntryPoint()
        self.add_node()
        self.vs[10]["mm__"] = """match_contains"""
        #self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'matchcontains10')
        # match class StateMachine() node
        self.add_node()
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """StateMachine"""
        self.vs[11]["mm__"] = """StateMachine"""
        self.vs[11]["cardinality"] = """1"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match_contains node for class StateMachine()
        self.add_node()
        self.vs[12]["mm__"] = """match_contains"""
        #self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'matchcontains12')
        
        
        # apply class Inst() node
        self.add_node()
        self.vs[13]["name"] = """"""
        self.vs[13]["classtype"] = """Inst"""
        self.vs[13]["mm__"] = """Inst"""
        self.vs[13]["cardinality"] = """1"""
        #self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply_contains node for class Inst()
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
        # apply class Name() node
        self.add_node()
        self.vs[21]["name"] = """"""
        self.vs[21]["classtype"] = """Name"""
        self.vs[21]["mm__"] = """Name"""
        self.vs[21]["cardinality"] = """1"""
        #self.vs[21]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply_contains node for class Name()
        self.add_node()
        self.vs[22]["mm__"] = """apply_contains"""
        #self.vs[22]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains22')
        
        
        # match association State--transitions-->Transition node
        self.add_node()
        self.vs[23]["associationType"] = """transitions"""
        self.vs[23]["mm__"] = """directLink_S"""
        #self.vs[23]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc23')
        # match association Transition--type-->IN1 node
        self.add_node()
        self.vs[24]["associationType"] = """type"""
        self.vs[24]["mm__"] = """directLink_S"""
        #self.vs[24]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc24')
        # match association Transition--dest-->EntryPoint node
        self.add_node()
        self.vs[25]["associationType"] = """dest"""
        self.vs[25]["mm__"] = """directLink_S"""
        #self.vs[25]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc25')
        # match association EntryPoint--owningStateMachine-->StateMachine node
        self.add_node()
        self.vs[26]["associationType"] = """owningStateMachine"""
        self.vs[26]["mm__"] = """directLink_S"""
        #self.vs[26]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc26')
        
        # apply association Inst--channelNames-->Name node
        self.add_node()
        self.vs[27]["associationType"] = """channelNames"""
        self.vs[27]["mm__"] = """directLink_T"""
        #self.vs[27]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc27')
        # apply association Inst--channelNames-->Name node
        self.add_node()
        self.vs[28]["associationType"] = """channelNames"""
        self.vs[28]["mm__"] = """directLink_T"""
        #self.vs[28]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc28')
        # apply association Inst--channelNames-->Name node
        self.add_node()
        self.vs[29]["associationType"] = """channelNames"""
        self.vs[29]["mm__"] = """directLink_T"""
        #self.vs[29]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc29')
        # apply association Inst--channelNames-->Name node
        self.add_node()
        self.vs[30]["associationType"] = """channelNames"""
        self.vs[30]["mm__"] = """directLink_T"""
        #self.vs[30]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc30')
        
        
        
        # has match attribute isComposite() node
        self.add_node()
        self.vs[31]["mm__"] = """hasAttribute_S"""
        #self.vs[31]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # match attribute isComposite() node
        self.add_node()
        self.vs[32]["name"] = """isComposite"""
        self.vs[32]["mm__"] = """Attribute"""
        self.vs[32]["Type"] = """'String'"""
        #self.vs[32]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match attribute equation isComposite() node
        self.add_node()
        self.vs[33]["name"] = """eq_"""
        self.vs[33]["mm__"] = """Equation"""
        #self.vs[33]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # match attribute equation left expr isComposite() node
        self.add_node()
        self.vs[34]["mm__"] = """leftExpr"""
        #self.vs[34]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # match attribute equation right expr isComposite() node
        self.add_node()
        self.vs[35]["mm__"] = """rightExpr"""
        #self.vs[35]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # apply attribute atom isComposite() node
        self.add_node()
        self.vs[36]["name"] = """true"""
        self.vs[36]["mm__"] = """Constant"""
        self.vs[36]["Type"] = """'String'"""
        #self.vs[36]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom36')
        # has match attribute name() node
        self.add_node()
        self.vs[37]["mm__"] = """hasAttribute_S"""
        #self.vs[37]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # match attribute name() node
        self.add_node()
        self.vs[38]["name"] = """name"""
        self.vs[38]["mm__"] = """Attribute"""
        self.vs[38]["Type"] = """'String'"""
        #self.vs[38]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # has match attribute name() node
        self.add_node()
        self.vs[39]["mm__"] = """hasAttribute_S"""
        #self.vs[39]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # match attribute name() node
        self.add_node()
        self.vs[40]["name"] = """name"""
        self.vs[40]["mm__"] = """Attribute"""
        self.vs[40]["Type"] = """'String'"""
        #self.vs[40]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        
        
        # has apply attribute name() node
        self.add_node()
        self.vs[41]["mm__"] = """hasAttribute_T"""
        #self.vs[41]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # apply attribute name() node
        self.add_node()
        self.vs[42]["name"] = """name"""
        self.vs[42]["mm__"] = """Attribute"""
        self.vs[42]["Type"] = """'String'"""
        #self.vs[42]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply attribute equation name() node
        self.add_node()
        self.vs[43]["name"] = """eq_"""
        self.vs[43]["mm__"] = """Equation"""
        #self.vs[43]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # apply attribute equation left expr name() node
        self.add_node()
        self.vs[44]["mm__"] = """leftExpr"""
        #self.vs[44]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # apply attribute equation right expr name() node
        self.add_node()
        self.vs[45]["mm__"] = """rightExpr"""
        #self.vs[45]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # attribute concat name() node
        self.add_node()
        self.vs[46]["name"] = """Concat46"""
        self.vs[46]["mm__"] = """Concat"""
        self.vs[46]["Type"] = """'String'"""
        #self.vs[46]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concat46')
        # apply attribute concat has left args name() node
        self.add_node()
        self.vs[47]["mm__"] = """hasArgs"""
        #self.vs[47]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgs47')
        # apply attribute concat has right args name() node
        self.add_node()
        self.vs[48]["mm__"] = """hasArgs"""
        #self.vs[48]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgs48')
        # apply attribute atom name() node
        self.add_node()
        self.vs[49]["name"] = """S"""
        self.vs[49]["mm__"] = """Constant"""
        self.vs[49]["Type"] = """'String'"""
        #self.vs[49]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom49')
        # has apply attribute literal() node
        self.add_node()
        self.vs[50]["mm__"] = """hasAttribute_T"""
        #self.vs[50]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # apply attribute literal() node
        self.add_node()
        self.vs[51]["name"] = """literal"""
        self.vs[51]["mm__"] = """Attribute"""
        self.vs[51]["Type"] = """'String'"""
        #self.vs[51]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply attribute equation literal() node
        self.add_node()
        self.vs[52]["name"] = """eq_"""
        self.vs[52]["mm__"] = """Equation"""
        #self.vs[52]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # apply attribute equation left expr literal() node
        self.add_node()
        self.vs[53]["mm__"] = """leftExpr"""
        #self.vs[53]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # apply attribute equation right expr literal() node
        self.add_node()
        self.vs[54]["mm__"] = """rightExpr"""
        #self.vs[54]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # apply attribute atom literal() node
        self.add_node()
        self.vs[55]["name"] = """exit_in"""
        self.vs[55]["mm__"] = """Constant"""
        self.vs[55]["Type"] = """'String'"""
        #self.vs[55]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom55')
        # has apply attribute literal() node
        self.add_node()
        self.vs[56]["mm__"] = """hasAttribute_T"""
        #self.vs[56]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # apply attribute literal() node
        self.add_node()
        self.vs[57]["name"] = """literal"""
        self.vs[57]["mm__"] = """Attribute"""
        self.vs[57]["Type"] = """'String'"""
        #self.vs[57]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply attribute equation literal() node
        self.add_node()
        self.vs[58]["name"] = """eq_"""
        self.vs[58]["mm__"] = """Equation"""
        #self.vs[58]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # apply attribute equation left expr literal() node
        self.add_node()
        self.vs[59]["mm__"] = """leftExpr"""
        #self.vs[59]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # apply attribute equation right expr literal() node
        self.add_node()
        self.vs[60]["mm__"] = """rightExpr"""
        #self.vs[60]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # apply attribute atom literal() node
        self.add_node()
        self.vs[61]["name"] = """exack_in"""
        self.vs[61]["mm__"] = """Constant"""
        self.vs[61]["Type"] = """'String'"""
        #self.vs[61]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom61')
        # has apply attribute literal() node
        self.add_node()
        self.vs[62]["mm__"] = """hasAttribute_T"""
        #self.vs[62]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # apply attribute literal() node
        self.add_node()
        self.vs[63]["name"] = """literal"""
        self.vs[63]["mm__"] = """Attribute"""
        self.vs[63]["Type"] = """'String'"""
        #self.vs[63]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply attribute equation literal() node
        self.add_node()
        self.vs[64]["name"] = """eq_"""
        self.vs[64]["mm__"] = """Equation"""
        #self.vs[64]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # apply attribute equation left expr literal() node
        self.add_node()
        self.vs[65]["mm__"] = """leftExpr"""
        #self.vs[65]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # apply attribute equation right expr literal() node
        self.add_node()
        self.vs[66]["mm__"] = """rightExpr"""
        #self.vs[66]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # attribute concat literal() node
        self.add_node()
        self.vs[67]["name"] = """Concat67"""
        self.vs[67]["mm__"] = """Concat"""
        self.vs[67]["Type"] = """'String'"""
        #self.vs[67]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concat67')
        # apply attribute concat has left args literal() node
        self.add_node()
        self.vs[68]["mm__"] = """hasArgs"""
        #self.vs[68]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgs68')
        # apply attribute concat has right args literal() node
        self.add_node()
        self.vs[69]["mm__"] = """hasArgs"""
        #self.vs[69]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgs69')
        # apply attribute atom literal() node
        self.add_node()
        self.vs[70]["name"] = """A"""
        self.vs[70]["mm__"] = """Constant"""
        self.vs[70]["Type"] = """'String'"""
        #self.vs[70]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom70')
        # attribute concat literal() node
        self.add_node()
        self.vs[71]["name"] = """Concat71"""
        self.vs[71]["mm__"] = """Concat"""
        self.vs[71]["Type"] = """'String'"""
        #self.vs[71]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concat71')
        # apply attribute concat has left args literal() node
        self.add_node()
        self.vs[72]["mm__"] = """hasArgs"""
        #self.vs[72]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgs72')
        # apply attribute concat has right args literal() node
        self.add_node()
        self.vs[73]["mm__"] = """hasArgs"""
        #self.vs[73]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgs73')
        # apply attribute atom literal() node
        self.add_node()
        self.vs[74]["name"] = """A"""
        self.vs[74]["mm__"] = """Constant"""
        self.vs[74]["Type"] = """'String'"""
        #self.vs[74]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom74')
        # has apply attribute literal() node
        self.add_node()
        self.vs[75]["mm__"] = """hasAttribute_T"""
        #self.vs[75]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # apply attribute literal() node
        self.add_node()
        self.vs[76]["name"] = """literal"""
        self.vs[76]["mm__"] = """Attribute"""
        self.vs[76]["Type"] = """'String'"""
        #self.vs[76]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply attribute equation literal() node
        self.add_node()
        self.vs[77]["name"] = """eq_"""
        self.vs[77]["mm__"] = """Equation"""
        #self.vs[77]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # apply attribute equation left expr literal() node
        self.add_node()
        self.vs[78]["mm__"] = """leftExpr"""
        #self.vs[78]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # apply attribute equation right expr literal() node
        self.add_node()
        self.vs[79]["mm__"] = """rightExpr"""
        #self.vs[79]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # apply attribute atom literal() node
        self.add_node()
        self.vs[80]["name"] = """sh_in"""
        self.vs[80]["mm__"] = """Constant"""
        self.vs[80]["Type"] = """'String'"""
        #self.vs[80]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom80')
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class State()
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class Transition()
                (0,8), # matchmodel -> match_contains
                (8,7), # match_contains -> match_class IN1()
                (0,10), # matchmodel -> match_contains
                (10,9), # match_contains -> match_class EntryPoint()
                (0,12), # matchmodel -> match_contains
                (12,11), # match_contains -> match_class StateMachine()
                (1,14), # applymodel -> apply_contains
                (14,13), # apply_contains -> apply_class Inst()
                (1,16), # applymodel -> apply_contains
                (16,15), # apply_contains -> apply_class Name()
                (1,18), # applymodel -> apply_contains
                (18,17), # apply_contains -> apply_class Name()
                (1,20), # applymodel -> apply_contains
                (20,19), # apply_contains -> apply_class Name()
                (1,22), # applymodel -> apply_contains
                (22,21), # apply_contains -> apply_class Name()
                (3,23), # match_class State() -> association transitions
                (23,5), # association transitions  -> match_class Transition()
                (5,24), # match_class Transition() -> association type
                (24,7), # association type  -> match_class IN1()
                (5,25), # match_class Transition() -> association dest
                (25,9), # association dest  -> match_class EntryPoint()
                (9,26), # match_class EntryPoint() -> association owningStateMachine
                (26,11), # association owningStateMachine  -> match_class StateMachine()
                (13,27), # apply_class Inst() -> association channelNames
                (27,15), # association channelNames  -> apply_class Name()
                (13,28), # apply_class Inst() -> association channelNames
                (28,17), # association channelNames  -> apply_class Name()
                (13,29), # apply_class Inst() -> association channelNames
                (29,19), # association channelNames  -> apply_class Name()
                (13,30), # apply_class Inst() -> association channelNames
                (30,21), # association channelNames  -> apply_class Name()
                (3,31), # match_class State() -> has_match_attribute isComposite ()
                (31,32), #  has_match_attribute isComposite () -> match_attribute isComposite ()
                (33,34), #  equation of match attribute isComposite () -> left_expr
                (34,32), #  left_expr -> match_attribute isComposite ()
                (33,35), #  equation of match attribute isComposite () -> right_expr
                (35,36), # right_expr --> term
                (9,37), # match_class EntryPoint() -> has_match_attribute name ()
                (37,38), #  has_match_attribute name () -> match_attribute name ()
                (11,39), # match_class StateMachine() -> has_match_attribute name ()
                (39,40), #  has_match_attribute name () -> match_attribute name ()
                (13,41), # apply_class Inst() -> has_apply_attribute name ()
                (41,42), #  has_apply_attribute name () -> apply_attribute name ()
                (43,44), #  equation of apply attribute name () -> left_expr
                (44,42), #  left_expr -> apply_attribute name ()
                (43,45), #  equation of apply attribute name () -> right_expr
                (46,47), #  apply attribute concat name () -> left has_args
                (47,49), #  left has_args -> term
                (46,48), #  apply attribute concat name () -> right has_args
                (48,40), #  right has_args -> term
                (45,46), # right_expr --> term
                (15,50), # apply_class Name() -> has_apply_attribute literal ()
                (50,51), #  has_apply_attribute literal () -> apply_attribute literal ()
                (52,53), #  equation of apply attribute literal () -> left_expr
                (53,51), #  left_expr -> apply_attribute literal ()
                (52,54), #  equation of apply attribute literal () -> right_expr
                (54,55), # right_expr --> term
                (17,56), # apply_class Name() -> has_apply_attribute literal ()
                (56,57), #  has_apply_attribute literal () -> apply_attribute literal ()
                (58,59), #  equation of apply attribute literal () -> left_expr
                (59,57), #  left_expr -> apply_attribute literal ()
                (58,60), #  equation of apply attribute literal () -> right_expr
                (60,61), # right_expr --> term
                (19,62), # apply_class Name() -> has_apply_attribute literal ()
                (62,63), #  has_apply_attribute literal () -> apply_attribute literal ()
                (64,65), #  equation of apply attribute literal () -> left_expr
                (65,63), #  left_expr -> apply_attribute literal ()
                (64,66), #  equation of apply attribute literal () -> right_expr
                (71,72), #  apply attribute concat literal () -> left has_args
                (72,38), #  left has_args -> term
                (71,73), #  apply attribute concat literal () -> right has_args
                (73,74), #  right has_args -> term
                (67,68), #  apply attribute concat literal () -> left has_args
                (68,70), #  left has_args -> term
                (67,69), #  apply attribute concat literal () -> right has_args
                (69,71), #  right has_args -> term
                (66,67), # right_expr --> term
                (21,75), # apply_class Name() -> has_apply_attribute literal ()
                (75,76), #  has_apply_attribute literal () -> apply_attribute literal ()
                (77,78), #  equation of apply attribute literal () -> left_expr
                (78,76), #  left_expr -> apply_attribute literal ()
                (77,79), #  equation of apply attribute literal () -> right_expr
                (79,80), # right_expr --> term
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel
        ])
        
