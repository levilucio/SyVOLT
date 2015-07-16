from core.himesis import Himesis
import uuid

class HState2CProcDef(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule State2CProcDef.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HState2CProcDef, self).__init__(name='HState2CProcDef', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """State2CProcDef"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'State2CProcDef')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'State2CProcDefmatchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'State2CProcDefapplymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'State2CProcDefpairedwith2')
        self.vs[2]["rulename"] = """State2CProcDef"""
        
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
        self.vs[5]["cardinality"] = """1"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match_contains node for class Transition()
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        #self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'matchcontains6')
        # match class EntryPoint() node
        self.add_node()
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EntryPoint"""
        self.vs[7]["mm__"] = """EntryPoint"""
        self.vs[7]["cardinality"] = """1"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match_contains node for class EntryPoint()
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
        
        
        # apply class LocalDef() node
        self.add_node()
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """LocalDef"""
        self.vs[11]["mm__"] = """LocalDef"""
        self.vs[11]["cardinality"] = """1"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply_contains node for class LocalDef()
        self.add_node()
        self.vs[12]["mm__"] = """apply_contains"""
        #self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains12')
        # apply class ProcDef() node
        self.add_node()
        self.vs[13]["name"] = """"""
        self.vs[13]["classtype"] = """ProcDef"""
        self.vs[13]["mm__"] = """ProcDef"""
        self.vs[13]["cardinality"] = """1"""
        #self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply_contains node for class ProcDef()
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
        # apply class ConditionSet() node
        self.add_node()
        self.vs[23]["name"] = """"""
        self.vs[23]["classtype"] = """ConditionSet"""
        self.vs[23]["mm__"] = """ConditionSet"""
        self.vs[23]["cardinality"] = """1"""
        #self.vs[23]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply_contains node for class ConditionSet()
        self.add_node()
        self.vs[24]["mm__"] = """apply_contains"""
        #self.vs[24]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains24')
        # apply class Inst() node
        self.add_node()
        self.vs[25]["name"] = """"""
        self.vs[25]["classtype"] = """Inst"""
        self.vs[25]["mm__"] = """Inst"""
        self.vs[25]["cardinality"] = """1"""
        #self.vs[25]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply_contains node for class Inst()
        self.add_node()
        self.vs[26]["mm__"] = """apply_contains"""
        #self.vs[26]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains26')
        # apply class Name() node
        self.add_node()
        self.vs[27]["name"] = """"""
        self.vs[27]["classtype"] = """Name"""
        self.vs[27]["mm__"] = """Name"""
        self.vs[27]["cardinality"] = """1"""
        #self.vs[27]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply_contains node for class Name()
        self.add_node()
        self.vs[28]["mm__"] = """apply_contains"""
        #self.vs[28]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains28')
        # apply class Name() node
        self.add_node()
        self.vs[29]["name"] = """"""
        self.vs[29]["classtype"] = """Name"""
        self.vs[29]["mm__"] = """Name"""
        self.vs[29]["cardinality"] = """1"""
        #self.vs[29]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply_contains node for class Name()
        self.add_node()
        self.vs[30]["mm__"] = """apply_contains"""
        #self.vs[30]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains30')
        # apply class Name() node
        self.add_node()
        self.vs[31]["name"] = """"""
        self.vs[31]["classtype"] = """Name"""
        self.vs[31]["mm__"] = """Name"""
        self.vs[31]["cardinality"] = """1"""
        #self.vs[31]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply_contains node for class Name()
        self.add_node()
        self.vs[32]["mm__"] = """apply_contains"""
        #self.vs[32]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains32')
        # apply class Name() node
        self.add_node()
        self.vs[33]["name"] = """"""
        self.vs[33]["classtype"] = """Name"""
        self.vs[33]["mm__"] = """Name"""
        self.vs[33]["cardinality"] = """1"""
        #self.vs[33]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply_contains node for class Name()
        self.add_node()
        self.vs[34]["mm__"] = """apply_contains"""
        #self.vs[34]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains34')
        
        
        # match association State--initialTransition-->Transition node
        self.add_node()
        self.vs[35]["associationType"] = """initialTransition"""
        self.vs[35]["mm__"] = """directLink_S"""
        #self.vs[35]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc35')
        # match association Transition--dest-->EntryPoint node
        self.add_node()
        self.vs[36]["associationType"] = """dest"""
        self.vs[36]["mm__"] = """directLink_S"""
        #self.vs[36]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc36')
        # match association EntryPoint--owningStateMachine-->StateMachine node
        self.add_node()
        self.vs[37]["associationType"] = """owningStateMachine"""
        self.vs[37]["mm__"] = """directLink_S"""
        #self.vs[37]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc37')
        
        # apply association LocalDef--def-->ProcDef node
        self.add_node()
        self.vs[38]["associationType"] = """def"""
        self.vs[38]["mm__"] = """directLink_T"""
        #self.vs[38]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc38')
        # apply association ProcDef--channelNames-->Name node
        self.add_node()
        self.vs[39]["associationType"] = """channelNames"""
        self.vs[39]["mm__"] = """directLink_T"""
        #self.vs[39]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc39')
        # apply association ProcDef--channelNames-->Name node
        self.add_node()
        self.vs[40]["associationType"] = """channelNames"""
        self.vs[40]["mm__"] = """directLink_T"""
        #self.vs[40]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc40')
        # apply association ProcDef--channelNames-->Name node
        self.add_node()
        self.vs[41]["associationType"] = """channelNames"""
        self.vs[41]["mm__"] = """directLink_T"""
        #self.vs[41]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc41')
        # apply association ProcDef--channelNames-->Name node
        self.add_node()
        self.vs[42]["associationType"] = """channelNames"""
        self.vs[42]["mm__"] = """directLink_T"""
        #self.vs[42]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc42')
        # apply association ProcDef--p-->ConditionSet node
        self.add_node()
        self.vs[43]["associationType"] = """p"""
        self.vs[43]["mm__"] = """directLink_T"""
        #self.vs[43]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc43')
        # apply association ConditionSet--alternative-->Inst node
        self.add_node()
        self.vs[44]["associationType"] = """alternative"""
        self.vs[44]["mm__"] = """directLink_T"""
        #self.vs[44]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc44')
        # apply association Inst--channelNames-->Name node
        self.add_node()
        self.vs[45]["associationType"] = """channelNames"""
        self.vs[45]["mm__"] = """directLink_T"""
        #self.vs[45]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc45')
        # apply association Inst--channelNames-->Name node
        self.add_node()
        self.vs[46]["associationType"] = """channelNames"""
        self.vs[46]["mm__"] = """directLink_T"""
        #self.vs[46]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc46')
        # apply association Inst--channelNames-->Name node
        self.add_node()
        self.vs[47]["associationType"] = """channelNames"""
        self.vs[47]["mm__"] = """directLink_T"""
        #self.vs[47]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc47')
        # apply association Inst--channelNames-->Name node
        self.add_node()
        self.vs[48]["associationType"] = """channelNames"""
        self.vs[48]["mm__"] = """directLink_T"""
        #self.vs[48]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc48')
        
        # backward association State---->LocalDef node
        self.add_node()
        self.vs[49]["type"] = """ruleDef"""
        self.vs[49]["mm__"] = """backward_link"""
        #self.vs[49]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'blink49')
        
        
        # has match attribute isComposite() node
        self.add_node()
        self.vs[50]["mm__"] = """hasAttribute_S"""
        #self.vs[50]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # match attribute isComposite() node
        self.add_node()
        self.vs[51]["name"] = """isComposite"""
        self.vs[51]["mm__"] = """Attribute"""
        self.vs[51]["Type"] = """'String'"""
        #self.vs[51]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match attribute equation isComposite() node
        self.add_node()
        self.vs[52]["name"] = """eq_"""
        self.vs[52]["mm__"] = """Equation"""
        #self.vs[52]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # match attribute equation left expr isComposite() node
        self.add_node()
        self.vs[53]["mm__"] = """leftExpr"""
        #self.vs[53]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # match attribute equation right expr isComposite() node
        self.add_node()
        self.vs[54]["mm__"] = """rightExpr"""
        #self.vs[54]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # apply attribute atom isComposite() node
        self.add_node()
        self.vs[55]["name"] = """true"""
        self.vs[55]["mm__"] = """Constant"""
        self.vs[55]["Type"] = """'String'"""
        #self.vs[55]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom55')
        # has match attribute name() node
        self.add_node()
        self.vs[56]["mm__"] = """hasAttribute_S"""
        #self.vs[56]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # match attribute name() node
        self.add_node()
        self.vs[57]["name"] = """name"""
        self.vs[57]["mm__"] = """Attribute"""
        self.vs[57]["Type"] = """'String'"""
        #self.vs[57]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # has match attribute name() node
        self.add_node()
        self.vs[58]["mm__"] = """hasAttribute_S"""
        #self.vs[58]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # match attribute name() node
        self.add_node()
        self.vs[59]["name"] = """name"""
        self.vs[59]["mm__"] = """Attribute"""
        self.vs[59]["Type"] = """'String'"""
        #self.vs[59]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        
        
        # has apply attribute name() node
        self.add_node()
        self.vs[60]["mm__"] = """hasAttribute_T"""
        #self.vs[60]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # apply attribute name() node
        self.add_node()
        self.vs[61]["name"] = """name"""
        self.vs[61]["mm__"] = """Attribute"""
        self.vs[61]["Type"] = """'String'"""
        #self.vs[61]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply attribute equation name() node
        self.add_node()
        self.vs[62]["name"] = """eq_"""
        self.vs[62]["mm__"] = """Equation"""
        #self.vs[62]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # apply attribute equation left expr name() node
        self.add_node()
        self.vs[63]["mm__"] = """leftExpr"""
        #self.vs[63]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # apply attribute equation right expr name() node
        self.add_node()
        self.vs[64]["mm__"] = """rightExpr"""
        #self.vs[64]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # apply attribute atom name() node
        self.add_node()
        self.vs[65]["name"] = """C"""
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
        self.vs[71]["name"] = """exit"""
        self.vs[71]["mm__"] = """Constant"""
        self.vs[71]["Type"] = """'String'"""
        #self.vs[71]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom71')
        # has apply attribute literal() node
        self.add_node()
        self.vs[72]["mm__"] = """hasAttribute_T"""
        #self.vs[72]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # apply attribute literal() node
        self.add_node()
        self.vs[73]["name"] = """literal"""
        self.vs[73]["mm__"] = """Attribute"""
        self.vs[73]["Type"] = """'String'"""
        #self.vs[73]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply attribute equation literal() node
        self.add_node()
        self.vs[74]["name"] = """eq_"""
        self.vs[74]["mm__"] = """Equation"""
        #self.vs[74]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # apply attribute equation left expr literal() node
        self.add_node()
        self.vs[75]["mm__"] = """leftExpr"""
        #self.vs[75]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # apply attribute equation right expr literal() node
        self.add_node()
        self.vs[76]["mm__"] = """rightExpr"""
        #self.vs[76]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # apply attribute atom literal() node
        self.add_node()
        self.vs[77]["name"] = """exack"""
        self.vs[77]["mm__"] = """Constant"""
        self.vs[77]["Type"] = """'String'"""
        #self.vs[77]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom77')
        # has apply attribute literal() node
        self.add_node()
        self.vs[78]["mm__"] = """hasAttribute_T"""
        #self.vs[78]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # apply attribute literal() node
        self.add_node()
        self.vs[79]["name"] = """literal"""
        self.vs[79]["mm__"] = """Attribute"""
        self.vs[79]["Type"] = """'String'"""
        #self.vs[79]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply attribute equation literal() node
        self.add_node()
        self.vs[80]["name"] = """eq_"""
        self.vs[80]["mm__"] = """Equation"""
        #self.vs[80]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # apply attribute equation left expr literal() node
        self.add_node()
        self.vs[81]["mm__"] = """leftExpr"""
        #self.vs[81]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # apply attribute equation right expr literal() node
        self.add_node()
        self.vs[82]["mm__"] = """rightExpr"""
        #self.vs[82]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # apply attribute atom literal() node
        self.add_node()
        self.vs[83]["name"] = """enp"""
        self.vs[83]["mm__"] = """Constant"""
        self.vs[83]["Type"] = """'String'"""
        #self.vs[83]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom83')
        # has apply attribute literal() node
        self.add_node()
        self.vs[84]["mm__"] = """hasAttribute_T"""
        #self.vs[84]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # apply attribute literal() node
        self.add_node()
        self.vs[85]["name"] = """literal"""
        self.vs[85]["mm__"] = """Attribute"""
        self.vs[85]["Type"] = """'String'"""
        #self.vs[85]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply attribute equation literal() node
        self.add_node()
        self.vs[86]["name"] = """eq_"""
        self.vs[86]["mm__"] = """Equation"""
        #self.vs[86]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # apply attribute equation left expr literal() node
        self.add_node()
        self.vs[87]["mm__"] = """leftExpr"""
        #self.vs[87]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # apply attribute equation right expr literal() node
        self.add_node()
        self.vs[88]["mm__"] = """rightExpr"""
        #self.vs[88]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # apply attribute atom literal() node
        self.add_node()
        self.vs[89]["name"] = """sh"""
        self.vs[89]["mm__"] = """Constant"""
        self.vs[89]["Type"] = """'String'"""
        #self.vs[89]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom89')
        # has apply attribute name() node
        self.add_node()
        self.vs[90]["mm__"] = """hasAttribute_T"""
        #self.vs[90]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # apply attribute name() node
        self.add_node()
        self.vs[91]["name"] = """name"""
        self.vs[91]["mm__"] = """Attribute"""
        self.vs[91]["Type"] = """'String'"""
        #self.vs[91]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply attribute equation name() node
        self.add_node()
        self.vs[92]["name"] = """eq_"""
        self.vs[92]["mm__"] = """Equation"""
        #self.vs[92]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # apply attribute equation left expr name() node
        self.add_node()
        self.vs[93]["mm__"] = """leftExpr"""
        #self.vs[93]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # apply attribute equation right expr name() node
        self.add_node()
        self.vs[94]["mm__"] = """rightExpr"""
        #self.vs[94]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # attribute concat name() node
        self.add_node()
        self.vs[95]["name"] = """Concat95"""
        self.vs[95]["mm__"] = """Concat"""
        self.vs[95]["Type"] = """'String'"""
        #self.vs[95]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concat95')
        # apply attribute concat has left args name() node
        self.add_node()
        self.vs[96]["mm__"] = """hasArgs"""
        #self.vs[96]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgs96')
        # apply attribute concat has right args name() node
        self.add_node()
        self.vs[97]["mm__"] = """hasArgs"""
        #self.vs[97]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgs97')
        # apply attribute atom name() node
        self.add_node()
        self.vs[98]["name"] = """S"""
        self.vs[98]["mm__"] = """Constant"""
        self.vs[98]["Type"] = """'String'"""
        #self.vs[98]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom98')
        # has apply attribute literal() node
        self.add_node()
        self.vs[99]["mm__"] = """hasAttribute_T"""
        #self.vs[99]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # apply attribute literal() node
        self.add_node()
        self.vs[100]["name"] = """literal"""
        self.vs[100]["mm__"] = """Attribute"""
        self.vs[100]["Type"] = """'String'"""
        #self.vs[100]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply attribute equation literal() node
        self.add_node()
        self.vs[101]["name"] = """eq_"""
        self.vs[101]["mm__"] = """Equation"""
        #self.vs[101]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # apply attribute equation left expr literal() node
        self.add_node()
        self.vs[102]["mm__"] = """leftExpr"""
        #self.vs[102]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # apply attribute equation right expr literal() node
        self.add_node()
        self.vs[103]["mm__"] = """rightExpr"""
        #self.vs[103]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # apply attribute atom literal() node
        self.add_node()
        self.vs[104]["name"] = """exit_in"""
        self.vs[104]["mm__"] = """Constant"""
        self.vs[104]["Type"] = """'String'"""
        #self.vs[104]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom104')
        # has apply attribute literal() node
        self.add_node()
        self.vs[105]["mm__"] = """hasAttribute_T"""
        #self.vs[105]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # apply attribute literal() node
        self.add_node()
        self.vs[106]["name"] = """literal"""
        self.vs[106]["mm__"] = """Attribute"""
        self.vs[106]["Type"] = """'String'"""
        #self.vs[106]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply attribute equation literal() node
        self.add_node()
        self.vs[107]["name"] = """eq_"""
        self.vs[107]["mm__"] = """Equation"""
        #self.vs[107]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # apply attribute equation left expr literal() node
        self.add_node()
        self.vs[108]["mm__"] = """leftExpr"""
        #self.vs[108]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # apply attribute equation right expr literal() node
        self.add_node()
        self.vs[109]["mm__"] = """rightExpr"""
        #self.vs[109]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # apply attribute atom literal() node
        self.add_node()
        self.vs[110]["name"] = """exack_in"""
        self.vs[110]["mm__"] = """Constant"""
        self.vs[110]["Type"] = """'String'"""
        #self.vs[110]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom110')
        # has apply attribute literal() node
        self.add_node()
        self.vs[111]["mm__"] = """hasAttribute_T"""
        #self.vs[111]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # apply attribute literal() node
        self.add_node()
        self.vs[112]["name"] = """literal"""
        self.vs[112]["mm__"] = """Attribute"""
        self.vs[112]["Type"] = """'String'"""
        #self.vs[112]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply attribute equation literal() node
        self.add_node()
        self.vs[113]["name"] = """eq_"""
        self.vs[113]["mm__"] = """Equation"""
        #self.vs[113]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # apply attribute equation left expr literal() node
        self.add_node()
        self.vs[114]["mm__"] = """leftExpr"""
        #self.vs[114]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # apply attribute equation right expr literal() node
        self.add_node()
        self.vs[115]["mm__"] = """rightExpr"""
        #self.vs[115]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # attribute concat literal() node
        self.add_node()
        self.vs[116]["name"] = """Concat116"""
        self.vs[116]["mm__"] = """Concat"""
        self.vs[116]["Type"] = """'String'"""
        #self.vs[116]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concat116')
        # apply attribute concat has left args literal() node
        self.add_node()
        self.vs[117]["mm__"] = """hasArgs"""
        #self.vs[117]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgs117')
        # apply attribute concat has right args literal() node
        self.add_node()
        self.vs[118]["mm__"] = """hasArgs"""
        #self.vs[118]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgs118')
        # apply attribute atom literal() node
        self.add_node()
        self.vs[119]["name"] = """A"""
        self.vs[119]["mm__"] = """Constant"""
        self.vs[119]["Type"] = """'String'"""
        #self.vs[119]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom119')
        # attribute concat literal() node
        self.add_node()
        self.vs[120]["name"] = """Concat120"""
        self.vs[120]["mm__"] = """Concat"""
        self.vs[120]["Type"] = """'String'"""
        #self.vs[120]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concat120')
        # apply attribute concat has left args literal() node
        self.add_node()
        self.vs[121]["mm__"] = """hasArgs"""
        #self.vs[121]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgs121')
        # apply attribute concat has right args literal() node
        self.add_node()
        self.vs[122]["mm__"] = """hasArgs"""
        #self.vs[122]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgs122')
        # apply attribute atom literal() node
        self.add_node()
        self.vs[123]["name"] = """A"""
        self.vs[123]["mm__"] = """Constant"""
        self.vs[123]["Type"] = """'String'"""
        #self.vs[123]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom123')
        # has apply attribute literal() node
        self.add_node()
        self.vs[124]["mm__"] = """hasAttribute_T"""
        #self.vs[124]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # apply attribute literal() node
        self.add_node()
        self.vs[125]["name"] = """literal"""
        self.vs[125]["mm__"] = """Attribute"""
        self.vs[125]["Type"] = """'String'"""
        #self.vs[125]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply attribute equation literal() node
        self.add_node()
        self.vs[126]["name"] = """eq_"""
        self.vs[126]["mm__"] = """Equation"""
        #self.vs[126]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # apply attribute equation left expr literal() node
        self.add_node()
        self.vs[127]["mm__"] = """leftExpr"""
        #self.vs[127]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # apply attribute equation right expr literal() node
        self.add_node()
        self.vs[128]["mm__"] = """rightExpr"""
        #self.vs[128]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # apply attribute atom literal() node
        self.add_node()
        self.vs[129]["name"] = """sh_in"""
        self.vs[129]["mm__"] = """Constant"""
        self.vs[129]["Type"] = """'String'"""
        #self.vs[129]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom129')
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class State()
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class Transition()
                (0,8), # matchmodel -> match_contains
                (8,7), # match_contains -> match_class EntryPoint()
                (0,10), # matchmodel -> match_contains
                (10,9), # match_contains -> match_class StateMachine()
                (1,12), # applymodel -> apply_contains
                (12,11), # apply_contains -> apply_class LocalDef()
                (1,14), # applymodel -> apply_contains
                (14,13), # apply_contains -> apply_class ProcDef()
                (1,16), # applymodel -> apply_contains
                (16,15), # apply_contains -> apply_class Name()
                (1,18), # applymodel -> apply_contains
                (18,17), # apply_contains -> apply_class Name()
                (1,20), # applymodel -> apply_contains
                (20,19), # apply_contains -> apply_class Name()
                (1,22), # applymodel -> apply_contains
                (22,21), # apply_contains -> apply_class Name()
                (1,24), # applymodel -> apply_contains
                (24,23), # apply_contains -> apply_class ConditionSet()
                (1,26), # applymodel -> apply_contains
                (26,25), # apply_contains -> apply_class Inst()
                (1,28), # applymodel -> apply_contains
                (28,27), # apply_contains -> apply_class Name()
                (1,30), # applymodel -> apply_contains
                (30,29), # apply_contains -> apply_class Name()
                (1,32), # applymodel -> apply_contains
                (32,31), # apply_contains -> apply_class Name()
                (1,34), # applymodel -> apply_contains
                (34,33), # apply_contains -> apply_class Name()
                (3,35), # match_class State() -> association initialTransition
                (35,5), # association initialTransition  -> match_class Transition()
                (5,36), # match_class Transition() -> association dest
                (36,7), # association dest  -> match_class EntryPoint()
                (7,37), # match_class EntryPoint() -> association owningStateMachine
                (37,9), # association owningStateMachine  -> match_class StateMachine()
                (11,38), # apply_class LocalDef() -> association def
                (38,13), # association def  -> apply_class ProcDef()
                (13,39), # apply_class ProcDef() -> association channelNames
                (39,15), # association channelNames  -> apply_class Name()
                (13,40), # apply_class ProcDef() -> association channelNames
                (40,17), # association channelNames  -> apply_class Name()
                (13,41), # apply_class ProcDef() -> association channelNames
                (41,19), # association channelNames  -> apply_class Name()
                (13,42), # apply_class ProcDef() -> association channelNames
                (42,21), # association channelNames  -> apply_class Name()
                (13,43), # apply_class ProcDef() -> association p
                (43,23), # association p  -> apply_class ConditionSet()
                (23,44), # apply_class ConditionSet() -> association alternative
                (44,25), # association alternative  -> apply_class Inst()
                (25,45), # apply_class Inst() -> association channelNames
                (45,27), # association channelNames  -> apply_class Name()
                (25,46), # apply_class Inst() -> association channelNames
                (46,29), # association channelNames  -> apply_class Name()
                (25,47), # apply_class Inst() -> association channelNames
                (47,31), # association channelNames  -> apply_class Name()
                (25,48), # apply_class Inst() -> association channelNames
                (48,33), # association channelNames  -> apply_class Name()
                (11,49), # apply_class LocalDef() -> backward_association
                (49,3), #  backward_association -> apply_class State()
                (3,50), # match_class State() -> has_match_attribute isComposite ()
                (50,51), #  has_match_attribute isComposite () -> match_attribute isComposite ()
                (52,53), #  equation of match attribute isComposite () -> left_expr
                (53,51), #  left_expr -> match_attribute isComposite ()
                (52,54), #  equation of match attribute isComposite () -> right_expr
                (54,55), # right_expr --> term
                (7,56), # match_class EntryPoint() -> has_match_attribute name ()
                (56,57), #  has_match_attribute name () -> match_attribute name ()
                (9,58), # match_class StateMachine() -> has_match_attribute name ()
                (58,59), #  has_match_attribute name () -> match_attribute name ()
                (13,60), # apply_class ProcDef() -> has_apply_attribute name ()
                (60,61), #  has_apply_attribute name () -> apply_attribute name ()
                (62,63), #  equation of apply attribute name () -> left_expr
                (63,61), #  left_expr -> apply_attribute name ()
                (62,64), #  equation of apply attribute name () -> right_expr
                (64,65), # right_expr --> term
                (15,66), # apply_class Name() -> has_apply_attribute literal ()
                (66,67), #  has_apply_attribute literal () -> apply_attribute literal ()
                (68,69), #  equation of apply attribute literal () -> left_expr
                (69,67), #  left_expr -> apply_attribute literal ()
                (68,70), #  equation of apply attribute literal () -> right_expr
                (70,71), # right_expr --> term
                (17,72), # apply_class Name() -> has_apply_attribute literal ()
                (72,73), #  has_apply_attribute literal () -> apply_attribute literal ()
                (74,75), #  equation of apply attribute literal () -> left_expr
                (75,73), #  left_expr -> apply_attribute literal ()
                (74,76), #  equation of apply attribute literal () -> right_expr
                (76,77), # right_expr --> term
                (19,78), # apply_class Name() -> has_apply_attribute literal ()
                (78,79), #  has_apply_attribute literal () -> apply_attribute literal ()
                (80,81), #  equation of apply attribute literal () -> left_expr
                (81,79), #  left_expr -> apply_attribute literal ()
                (80,82), #  equation of apply attribute literal () -> right_expr
                (82,83), # right_expr --> term
                (21,84), # apply_class Name() -> has_apply_attribute literal ()
                (84,85), #  has_apply_attribute literal () -> apply_attribute literal ()
                (86,87), #  equation of apply attribute literal () -> left_expr
                (87,85), #  left_expr -> apply_attribute literal ()
                (86,88), #  equation of apply attribute literal () -> right_expr
                (88,89), # right_expr --> term
                (25,90), # apply_class Inst() -> has_apply_attribute name ()
                (90,91), #  has_apply_attribute name () -> apply_attribute name ()
                (92,93), #  equation of apply attribute name () -> left_expr
                (93,91), #  left_expr -> apply_attribute name ()
                (92,94), #  equation of apply attribute name () -> right_expr
                (95,96), #  apply attribute concat name () -> left has_args
                (96,98), #  left has_args -> term
                (95,97), #  apply attribute concat name () -> right has_args
                (97,59), #  right has_args -> term
                (94,95), # right_expr --> term
                (27,99), # apply_class Name() -> has_apply_attribute literal ()
                (99,100), #  has_apply_attribute literal () -> apply_attribute literal ()
                (101,102), #  equation of apply attribute literal () -> left_expr
                (102,100), #  left_expr -> apply_attribute literal ()
                (101,103), #  equation of apply attribute literal () -> right_expr
                (103,104), # right_expr --> term
                (29,105), # apply_class Name() -> has_apply_attribute literal ()
                (105,106), #  has_apply_attribute literal () -> apply_attribute literal ()
                (107,108), #  equation of apply attribute literal () -> left_expr
                (108,106), #  left_expr -> apply_attribute literal ()
                (107,109), #  equation of apply attribute literal () -> right_expr
                (109,110), # right_expr --> term
                (31,111), # apply_class Name() -> has_apply_attribute literal ()
                (111,112), #  has_apply_attribute literal () -> apply_attribute literal ()
                (113,114), #  equation of apply attribute literal () -> left_expr
                (114,112), #  left_expr -> apply_attribute literal ()
                (113,115), #  equation of apply attribute literal () -> right_expr
                (120,121), #  apply attribute concat literal () -> left has_args
                (121,57), #  left has_args -> term
                (120,122), #  apply attribute concat literal () -> right has_args
                (122,123), #  right has_args -> term
                (116,117), #  apply attribute concat literal () -> left has_args
                (117,119), #  left has_args -> term
                (116,118), #  apply attribute concat literal () -> right has_args
                (118,120), #  right has_args -> term
                (115,116), # right_expr --> term
                (33,124), # apply_class Name() -> has_apply_attribute literal ()
                (124,125), #  has_apply_attribute literal () -> apply_attribute literal ()
                (126,127), #  equation of apply attribute literal () -> left_expr
                (127,125), #  left_expr -> apply_attribute literal ()
                (126,128), #  equation of apply attribute literal () -> right_expr
                (128,129), # right_expr --> term
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel
        ])
        
