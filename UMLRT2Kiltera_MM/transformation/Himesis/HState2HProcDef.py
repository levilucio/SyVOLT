from core.himesis import Himesis
import uuid

class HState2HProcDef(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule State2HProcDef.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HState2HProcDef, self).__init__(name='HState2HProcDef', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """State2HProcDef"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'State2HProcDef')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'State2HProcDefmatchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'State2HProcDefapplymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'State2HProcDefpairedwith2')
        self.vs[2]["rulename"] = """State2HProcDef"""
        
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
        
        
        # apply class LocalDef() node
        self.add_node()
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """LocalDef"""
        self.vs[5]["mm__"] = """LocalDef"""
        self.vs[5]["cardinality"] = """1"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply_contains node for class LocalDef()
        self.add_node()
        self.vs[6]["mm__"] = """apply_contains"""
        #self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains6')
        # apply class ProcDef() node
        self.add_node()
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """ProcDef"""
        self.vs[7]["mm__"] = """ProcDef"""
        self.vs[7]["cardinality"] = """1"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply_contains node for class ProcDef()
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        #self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains8')
        # apply class Name() node
        self.add_node()
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """Name"""
        self.vs[9]["mm__"] = """Name"""
        self.vs[9]["cardinality"] = """1"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply_contains node for class Name()
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
        # apply class Listen() node
        self.add_node()
        self.vs[15]["name"] = """"""
        self.vs[15]["classtype"] = """Listen"""
        self.vs[15]["mm__"] = """Listen"""
        self.vs[15]["cardinality"] = """1"""
        #self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply_contains node for class Listen()
        self.add_node()
        self.vs[16]["mm__"] = """apply_contains"""
        #self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains16')
        # apply class ListenBranch() node
        self.add_node()
        self.vs[17]["name"] = """"""
        self.vs[17]["classtype"] = """ListenBranch"""
        self.vs[17]["mm__"] = """ListenBranch"""
        self.vs[17]["cardinality"] = """1"""
        #self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply_contains node for class ListenBranch()
        self.add_node()
        self.vs[18]["mm__"] = """apply_contains"""
        #self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains18')
        # apply class Null() node
        self.add_node()
        self.vs[19]["name"] = """"""
        self.vs[19]["classtype"] = """Null"""
        self.vs[19]["mm__"] = """Null"""
        self.vs[19]["cardinality"] = """1"""
        #self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply_contains node for class Null()
        self.add_node()
        self.vs[20]["mm__"] = """apply_contains"""
        #self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains20')
        # apply class ListenBranch() node
        self.add_node()
        self.vs[21]["name"] = """"""
        self.vs[21]["classtype"] = """ListenBranch"""
        self.vs[21]["mm__"] = """ListenBranch"""
        self.vs[21]["cardinality"] = """1"""
        #self.vs[21]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply_contains node for class ListenBranch()
        self.add_node()
        self.vs[22]["mm__"] = """apply_contains"""
        #self.vs[22]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains22')
        # apply class Seq() node
        self.add_node()
        self.vs[23]["name"] = """"""
        self.vs[23]["classtype"] = """Seq"""
        self.vs[23]["mm__"] = """Seq"""
        self.vs[23]["cardinality"] = """1"""
        #self.vs[23]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply_contains node for class Seq()
        self.add_node()
        self.vs[24]["mm__"] = """apply_contains"""
        #self.vs[24]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains24')
        # apply class Trigger() node
        self.add_node()
        self.vs[25]["name"] = """"""
        self.vs[25]["classtype"] = """Trigger"""
        self.vs[25]["mm__"] = """Trigger"""
        self.vs[25]["cardinality"] = """1"""
        #self.vs[25]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply_contains node for class Trigger()
        self.add_node()
        self.vs[26]["mm__"] = """apply_contains"""
        #self.vs[26]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains26')
        # apply class Listen() node
        self.add_node()
        self.vs[27]["name"] = """"""
        self.vs[27]["classtype"] = """Listen"""
        self.vs[27]["mm__"] = """Listen"""
        self.vs[27]["cardinality"] = """1"""
        #self.vs[27]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply_contains node for class Listen()
        self.add_node()
        self.vs[28]["mm__"] = """apply_contains"""
        #self.vs[28]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains28')
        # apply class ListenBranch() node
        self.add_node()
        self.vs[29]["name"] = """"""
        self.vs[29]["classtype"] = """ListenBranch"""
        self.vs[29]["mm__"] = """ListenBranch"""
        self.vs[29]["cardinality"] = """1"""
        #self.vs[29]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply_contains node for class ListenBranch()
        self.add_node()
        self.vs[30]["mm__"] = """apply_contains"""
        #self.vs[30]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains30')
        # apply class Trigger() node
        self.add_node()
        self.vs[31]["name"] = """"""
        self.vs[31]["classtype"] = """Trigger"""
        self.vs[31]["mm__"] = """Trigger"""
        self.vs[31]["cardinality"] = """1"""
        #self.vs[31]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply_contains node for class Trigger()
        self.add_node()
        self.vs[32]["mm__"] = """apply_contains"""
        #self.vs[32]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains32')
        
        
        
        # apply association LocalDef--def-->ProcDef node
        self.add_node()
        self.vs[33]["associationType"] = """def"""
        self.vs[33]["mm__"] = """directLink_T"""
        #self.vs[33]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc33')
        # apply association ProcDef--channelNames-->Name node
        self.add_node()
        self.vs[34]["associationType"] = """channelNames"""
        self.vs[34]["mm__"] = """directLink_T"""
        #self.vs[34]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc34')
        # apply association ProcDef--channelNames-->Name node
        self.add_node()
        self.vs[35]["associationType"] = """channelNames"""
        self.vs[35]["mm__"] = """directLink_T"""
        #self.vs[35]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc35')
        # apply association ProcDef--channelNames-->Name node
        self.add_node()
        self.vs[36]["associationType"] = """channelNames"""
        self.vs[36]["mm__"] = """directLink_T"""
        #self.vs[36]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc36')
        # apply association ProcDef--p-->Listen node
        self.add_node()
        self.vs[37]["associationType"] = """p"""
        self.vs[37]["mm__"] = """directLink_T"""
        #self.vs[37]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc37')
        # apply association Listen--branches-->ListenBranch node
        self.add_node()
        self.vs[38]["associationType"] = """branches"""
        self.vs[38]["mm__"] = """directLink_T"""
        #self.vs[38]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc38')
        # apply association ListenBranch--p-->Null node
        self.add_node()
        self.vs[39]["associationType"] = """p"""
        self.vs[39]["mm__"] = """directLink_T"""
        #self.vs[39]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc39')
        # apply association Listen--branches-->ListenBranch node
        self.add_node()
        self.vs[40]["associationType"] = """branches"""
        self.vs[40]["mm__"] = """directLink_T"""
        #self.vs[40]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc40')
        # apply association ListenBranch--p-->Seq node
        self.add_node()
        self.vs[41]["associationType"] = """p"""
        self.vs[41]["mm__"] = """directLink_T"""
        #self.vs[41]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc41')
        # apply association Seq--p-->Trigger node
        self.add_node()
        self.vs[42]["associationType"] = """p"""
        self.vs[42]["mm__"] = """directLink_T"""
        #self.vs[42]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc42')
        # apply association Seq--p-->Listen node
        self.add_node()
        self.vs[43]["associationType"] = """p"""
        self.vs[43]["mm__"] = """directLink_T"""
        #self.vs[43]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc43')
        # apply association Listen--branches-->ListenBranch node
        self.add_node()
        self.vs[44]["associationType"] = """branches"""
        self.vs[44]["mm__"] = """directLink_T"""
        #self.vs[44]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc44')
        # apply association ListenBranch--p-->Trigger node
        self.add_node()
        self.vs[45]["associationType"] = """p"""
        self.vs[45]["mm__"] = """directLink_T"""
        #self.vs[45]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc45')
        
        # backward association State---->LocalDef node
        self.add_node()
        self.vs[46]["type"] = """ruleDef"""
        self.vs[46]["mm__"] = """backward_link"""
        #self.vs[46]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'blink46')
        
        
        # has match attribute isComposite() node
        self.add_node()
        self.vs[47]["mm__"] = """hasAttribute_S"""
        #self.vs[47]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # match attribute isComposite() node
        self.add_node()
        self.vs[48]["name"] = """isComposite"""
        self.vs[48]["mm__"] = """Attribute"""
        self.vs[48]["Type"] = """'String'"""
        #self.vs[48]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match attribute equation isComposite() node
        self.add_node()
        self.vs[49]["name"] = """eq_"""
        self.vs[49]["mm__"] = """Equation"""
        #self.vs[49]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # match attribute equation left expr isComposite() node
        self.add_node()
        self.vs[50]["mm__"] = """leftExpr"""
        #self.vs[50]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # match attribute equation right expr isComposite() node
        self.add_node()
        self.vs[51]["mm__"] = """rightExpr"""
        #self.vs[51]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # apply attribute atom isComposite() node
        self.add_node()
        self.vs[52]["name"] = """true"""
        self.vs[52]["mm__"] = """Constant"""
        self.vs[52]["Type"] = """'String'"""
        #self.vs[52]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom52')
        
        
        # has apply attribute name() node
        self.add_node()
        self.vs[53]["mm__"] = """hasAttribute_T"""
        #self.vs[53]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # apply attribute name() node
        self.add_node()
        self.vs[54]["name"] = """name"""
        self.vs[54]["mm__"] = """Attribute"""
        self.vs[54]["Type"] = """'String'"""
        #self.vs[54]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply attribute equation name() node
        self.add_node()
        self.vs[55]["name"] = """eq_"""
        self.vs[55]["mm__"] = """Equation"""
        #self.vs[55]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # apply attribute equation left expr name() node
        self.add_node()
        self.vs[56]["mm__"] = """leftExpr"""
        #self.vs[56]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # apply attribute equation right expr name() node
        self.add_node()
        self.vs[57]["mm__"] = """rightExpr"""
        #self.vs[57]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # apply attribute atom name() node
        self.add_node()
        self.vs[58]["name"] = """H"""
        self.vs[58]["mm__"] = """Constant"""
        self.vs[58]["Type"] = """'String'"""
        #self.vs[58]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom58')
        # has apply attribute literal() node
        self.add_node()
        self.vs[59]["mm__"] = """hasAttribute_T"""
        #self.vs[59]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # apply attribute literal() node
        self.add_node()
        self.vs[60]["name"] = """literal"""
        self.vs[60]["mm__"] = """Attribute"""
        self.vs[60]["Type"] = """'String'"""
        #self.vs[60]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply attribute equation literal() node
        self.add_node()
        self.vs[61]["name"] = """eq_"""
        self.vs[61]["mm__"] = """Equation"""
        #self.vs[61]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # apply attribute equation left expr literal() node
        self.add_node()
        self.vs[62]["mm__"] = """leftExpr"""
        #self.vs[62]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # apply attribute equation right expr literal() node
        self.add_node()
        self.vs[63]["mm__"] = """rightExpr"""
        #self.vs[63]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # apply attribute atom literal() node
        self.add_node()
        self.vs[64]["name"] = """exit_in"""
        self.vs[64]["mm__"] = """Constant"""
        self.vs[64]["Type"] = """'String'"""
        #self.vs[64]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom64')
        # has apply attribute literal() node
        self.add_node()
        self.vs[65]["mm__"] = """hasAttribute_T"""
        #self.vs[65]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # apply attribute literal() node
        self.add_node()
        self.vs[66]["name"] = """literal"""
        self.vs[66]["mm__"] = """Attribute"""
        self.vs[66]["Type"] = """'String'"""
        #self.vs[66]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply attribute equation literal() node
        self.add_node()
        self.vs[67]["name"] = """eq_"""
        self.vs[67]["mm__"] = """Equation"""
        #self.vs[67]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # apply attribute equation left expr literal() node
        self.add_node()
        self.vs[68]["mm__"] = """leftExpr"""
        #self.vs[68]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # apply attribute equation right expr literal() node
        self.add_node()
        self.vs[69]["mm__"] = """rightExpr"""
        #self.vs[69]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # apply attribute atom literal() node
        self.add_node()
        self.vs[70]["name"] = """exack_in"""
        self.vs[70]["mm__"] = """Constant"""
        self.vs[70]["Type"] = """'String'"""
        #self.vs[70]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom70')
        # has apply attribute literal() node
        self.add_node()
        self.vs[71]["mm__"] = """hasAttribute_T"""
        #self.vs[71]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # apply attribute literal() node
        self.add_node()
        self.vs[72]["name"] = """literal"""
        self.vs[72]["mm__"] = """Attribute"""
        self.vs[72]["Type"] = """'String'"""
        #self.vs[72]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply attribute equation literal() node
        self.add_node()
        self.vs[73]["name"] = """eq_"""
        self.vs[73]["mm__"] = """Equation"""
        #self.vs[73]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # apply attribute equation left expr literal() node
        self.add_node()
        self.vs[74]["mm__"] = """leftExpr"""
        #self.vs[74]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # apply attribute equation right expr literal() node
        self.add_node()
        self.vs[75]["mm__"] = """rightExpr"""
        #self.vs[75]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # apply attribute atom literal() node
        self.add_node()
        self.vs[76]["name"] = """sh_in"""
        self.vs[76]["mm__"] = """Constant"""
        self.vs[76]["Type"] = """'String'"""
        #self.vs[76]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom76')
        # has apply attribute channel() node
        self.add_node()
        self.vs[77]["mm__"] = """hasAttribute_T"""
        #self.vs[77]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # apply attribute channel() node
        self.add_node()
        self.vs[78]["name"] = """channel"""
        self.vs[78]["mm__"] = """Attribute"""
        self.vs[78]["Type"] = """'String'"""
        #self.vs[78]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply attribute equation channel() node
        self.add_node()
        self.vs[79]["name"] = """eq_"""
        self.vs[79]["mm__"] = """Equation"""
        #self.vs[79]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # apply attribute equation left expr channel() node
        self.add_node()
        self.vs[80]["mm__"] = """leftExpr"""
        #self.vs[80]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # apply attribute equation right expr channel() node
        self.add_node()
        self.vs[81]["mm__"] = """rightExpr"""
        #self.vs[81]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # apply attribute atom channel() node
        self.add_node()
        self.vs[82]["name"] = """sh_in"""
        self.vs[82]["mm__"] = """Constant"""
        self.vs[82]["Type"] = """'String'"""
        #self.vs[82]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom82')
        # has apply attribute channel() node
        self.add_node()
        self.vs[83]["mm__"] = """hasAttribute_T"""
        #self.vs[83]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # apply attribute channel() node
        self.add_node()
        self.vs[84]["name"] = """channel"""
        self.vs[84]["mm__"] = """Attribute"""
        self.vs[84]["Type"] = """'String'"""
        #self.vs[84]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply attribute equation channel() node
        self.add_node()
        self.vs[85]["name"] = """eq_"""
        self.vs[85]["mm__"] = """Equation"""
        #self.vs[85]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # apply attribute equation left expr channel() node
        self.add_node()
        self.vs[86]["mm__"] = """leftExpr"""
        #self.vs[86]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # apply attribute equation right expr channel() node
        self.add_node()
        self.vs[87]["mm__"] = """rightExpr"""
        #self.vs[87]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # apply attribute atom channel() node
        self.add_node()
        self.vs[88]["name"] = """exit"""
        self.vs[88]["mm__"] = """Constant"""
        self.vs[88]["Type"] = """'String'"""
        #self.vs[88]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom88')
        # has apply attribute channel() node
        self.add_node()
        self.vs[89]["mm__"] = """hasAttribute_T"""
        #self.vs[89]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # apply attribute channel() node
        self.add_node()
        self.vs[90]["name"] = """channel"""
        self.vs[90]["mm__"] = """Attribute"""
        self.vs[90]["Type"] = """'String'"""
        #self.vs[90]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply attribute equation channel() node
        self.add_node()
        self.vs[91]["name"] = """eq_"""
        self.vs[91]["mm__"] = """Equation"""
        #self.vs[91]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # apply attribute equation left expr channel() node
        self.add_node()
        self.vs[92]["mm__"] = """leftExpr"""
        #self.vs[92]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # apply attribute equation right expr channel() node
        self.add_node()
        self.vs[93]["mm__"] = """rightExpr"""
        #self.vs[93]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # apply attribute atom channel() node
        self.add_node()
        self.vs[94]["name"] = """exit_in"""
        self.vs[94]["mm__"] = """Constant"""
        self.vs[94]["Type"] = """'String'"""
        #self.vs[94]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom94')
        # has apply attribute channel() node
        self.add_node()
        self.vs[95]["mm__"] = """hasAttribute_T"""
        #self.vs[95]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # apply attribute channel() node
        self.add_node()
        self.vs[96]["name"] = """channel"""
        self.vs[96]["mm__"] = """Attribute"""
        self.vs[96]["Type"] = """'String'"""
        #self.vs[96]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply attribute equation channel() node
        self.add_node()
        self.vs[97]["name"] = """eq_"""
        self.vs[97]["mm__"] = """Equation"""
        #self.vs[97]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # apply attribute equation left expr channel() node
        self.add_node()
        self.vs[98]["mm__"] = """leftExpr"""
        #self.vs[98]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # apply attribute equation right expr channel() node
        self.add_node()
        self.vs[99]["mm__"] = """rightExpr"""
        #self.vs[99]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # apply attribute atom channel() node
        self.add_node()
        self.vs[100]["name"] = """exack_in"""
        self.vs[100]["mm__"] = """Constant"""
        self.vs[100]["Type"] = """'String'"""
        #self.vs[100]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom100')
        # has apply attribute channel() node
        self.add_node()
        self.vs[101]["mm__"] = """hasAttribute_T"""
        #self.vs[101]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # apply attribute channel() node
        self.add_node()
        self.vs[102]["name"] = """channel"""
        self.vs[102]["mm__"] = """Attribute"""
        self.vs[102]["Type"] = """'String'"""
        #self.vs[102]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply attribute equation channel() node
        self.add_node()
        self.vs[103]["name"] = """eq_"""
        self.vs[103]["mm__"] = """Equation"""
        #self.vs[103]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # apply attribute equation left expr channel() node
        self.add_node()
        self.vs[104]["mm__"] = """leftExpr"""
        #self.vs[104]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # apply attribute equation right expr channel() node
        self.add_node()
        self.vs[105]["mm__"] = """rightExpr"""
        #self.vs[105]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # apply attribute atom channel() node
        self.add_node()
        self.vs[106]["name"] = """exack"""
        self.vs[106]["mm__"] = """Constant"""
        self.vs[106]["Type"] = """'String'"""
        #self.vs[106]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom106')
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class State()
                (1,6), # applymodel -> apply_contains
                (6,5), # apply_contains -> apply_class LocalDef()
                (1,8), # applymodel -> apply_contains
                (8,7), # apply_contains -> apply_class ProcDef()
                (1,10), # applymodel -> apply_contains
                (10,9), # apply_contains -> apply_class Name()
                (1,12), # applymodel -> apply_contains
                (12,11), # apply_contains -> apply_class Name()
                (1,14), # applymodel -> apply_contains
                (14,13), # apply_contains -> apply_class Name()
                (1,16), # applymodel -> apply_contains
                (16,15), # apply_contains -> apply_class Listen()
                (1,18), # applymodel -> apply_contains
                (18,17), # apply_contains -> apply_class ListenBranch()
                (1,20), # applymodel -> apply_contains
                (20,19), # apply_contains -> apply_class Null()
                (1,22), # applymodel -> apply_contains
                (22,21), # apply_contains -> apply_class ListenBranch()
                (1,24), # applymodel -> apply_contains
                (24,23), # apply_contains -> apply_class Seq()
                (1,26), # applymodel -> apply_contains
                (26,25), # apply_contains -> apply_class Trigger()
                (1,28), # applymodel -> apply_contains
                (28,27), # apply_contains -> apply_class Listen()
                (1,30), # applymodel -> apply_contains
                (30,29), # apply_contains -> apply_class ListenBranch()
                (1,32), # applymodel -> apply_contains
                (32,31), # apply_contains -> apply_class Trigger()
                (5,33), # apply_class LocalDef() -> association def
                (33,7), # association def  -> apply_class ProcDef()
                (7,34), # apply_class ProcDef() -> association channelNames
                (34,9), # association channelNames  -> apply_class Name()
                (7,35), # apply_class ProcDef() -> association channelNames
                (35,11), # association channelNames  -> apply_class Name()
                (7,36), # apply_class ProcDef() -> association channelNames
                (36,13), # association channelNames  -> apply_class Name()
                (7,37), # apply_class ProcDef() -> association p
                (37,15), # association p  -> apply_class Listen()
                (15,38), # apply_class Listen() -> association branches
                (38,17), # association branches  -> apply_class ListenBranch()
                (17,39), # apply_class ListenBranch() -> association p
                (39,19), # association p  -> apply_class Null()
                (15,40), # apply_class Listen() -> association branches
                (40,21), # association branches  -> apply_class ListenBranch()
                (21,41), # apply_class ListenBranch() -> association p
                (41,23), # association p  -> apply_class Seq()
                (23,42), # apply_class Seq() -> association p
                (42,25), # association p  -> apply_class Trigger()
                (23,43), # apply_class Seq() -> association p
                (43,27), # association p  -> apply_class Listen()
                (27,44), # apply_class Listen() -> association branches
                (44,29), # association branches  -> apply_class ListenBranch()
                (29,45), # apply_class ListenBranch() -> association p
                (45,31), # association p  -> apply_class Trigger()
                (5,46), # apply_class LocalDef() -> backward_association
                (46,3), #  backward_association -> apply_class State()
                (3,47), # match_class State() -> has_match_attribute isComposite ()
                (47,48), #  has_match_attribute isComposite () -> match_attribute isComposite ()
                (49,50), #  equation of match attribute isComposite () -> left_expr
                (50,48), #  left_expr -> match_attribute isComposite ()
                (49,51), #  equation of match attribute isComposite () -> right_expr
                (51,52), # right_expr --> term
                (7,53), # apply_class ProcDef() -> has_apply_attribute name ()
                (53,54), #  has_apply_attribute name () -> apply_attribute name ()
                (55,56), #  equation of apply attribute name () -> left_expr
                (56,54), #  left_expr -> apply_attribute name ()
                (55,57), #  equation of apply attribute name () -> right_expr
                (57,58), # right_expr --> term
                (9,59), # apply_class Name() -> has_apply_attribute literal ()
                (59,60), #  has_apply_attribute literal () -> apply_attribute literal ()
                (61,62), #  equation of apply attribute literal () -> left_expr
                (62,60), #  left_expr -> apply_attribute literal ()
                (61,63), #  equation of apply attribute literal () -> right_expr
                (63,64), # right_expr --> term
                (11,65), # apply_class Name() -> has_apply_attribute literal ()
                (65,66), #  has_apply_attribute literal () -> apply_attribute literal ()
                (67,68), #  equation of apply attribute literal () -> left_expr
                (68,66), #  left_expr -> apply_attribute literal ()
                (67,69), #  equation of apply attribute literal () -> right_expr
                (69,70), # right_expr --> term
                (13,71), # apply_class Name() -> has_apply_attribute literal ()
                (71,72), #  has_apply_attribute literal () -> apply_attribute literal ()
                (73,74), #  equation of apply attribute literal () -> left_expr
                (74,72), #  left_expr -> apply_attribute literal ()
                (73,75), #  equation of apply attribute literal () -> right_expr
                (75,76), # right_expr --> term
                (17,77), # apply_class ListenBranch() -> has_apply_attribute channel ()
                (77,78), #  has_apply_attribute channel () -> apply_attribute channel ()
                (79,80), #  equation of apply attribute channel () -> left_expr
                (80,78), #  left_expr -> apply_attribute channel ()
                (79,81), #  equation of apply attribute channel () -> right_expr
                (81,82), # right_expr --> term
                (21,83), # apply_class ListenBranch() -> has_apply_attribute channel ()
                (83,84), #  has_apply_attribute channel () -> apply_attribute channel ()
                (85,86), #  equation of apply attribute channel () -> left_expr
                (86,84), #  left_expr -> apply_attribute channel ()
                (85,87), #  equation of apply attribute channel () -> right_expr
                (87,88), # right_expr --> term
                (25,89), # apply_class Trigger() -> has_apply_attribute channel ()
                (89,90), #  has_apply_attribute channel () -> apply_attribute channel ()
                (91,92), #  equation of apply attribute channel () -> left_expr
                (92,90), #  left_expr -> apply_attribute channel ()
                (91,93), #  equation of apply attribute channel () -> right_expr
                (93,94), # right_expr --> term
                (29,95), # apply_class ListenBranch() -> has_apply_attribute channel ()
                (95,96), #  has_apply_attribute channel () -> apply_attribute channel ()
                (97,98), #  equation of apply attribute channel () -> left_expr
                (98,96), #  left_expr -> apply_attribute channel ()
                (97,99), #  equation of apply attribute channel () -> right_expr
                (99,100), # right_expr --> term
                (31,101), # apply_class Trigger() -> has_apply_attribute channel ()
                (101,102), #  has_apply_attribute channel () -> apply_attribute channel ()
                (103,104), #  equation of apply attribute channel () -> left_expr
                (104,102), #  left_expr -> apply_attribute channel ()
                (103,105), #  equation of apply attribute channel () -> right_expr
                (105,106), # right_expr --> term
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel
        ])
        
