from core.himesis import Himesis
import uuid

class HCompositeState2ProcDef(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule CompositeState2ProcDef.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HCompositeState2ProcDef, self).__init__(name='HCompositeState2ProcDef', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """CompositeState2ProcDef"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'CompositeState2ProcDef')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'CompositeState2ProcDefmatchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'CompositeState2ProcDefapplymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'CompositeState2ProcDefpairedwith2')
        self.vs[2]["rulename"] = """CompositeState2ProcDef"""
        
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
        # apply class New() node
        self.add_node()
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """New"""
        self.vs[11]["mm__"] = """New"""
        self.vs[11]["cardinality"] = """1"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply_contains node for class New()
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
        # apply class Par() node
        self.add_node()
        self.vs[19]["name"] = """"""
        self.vs[19]["classtype"] = """Par"""
        self.vs[19]["mm__"] = """Par"""
        self.vs[19]["cardinality"] = """1"""
        #self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply_contains node for class Par()
        self.add_node()
        self.vs[20]["mm__"] = """apply_contains"""
        #self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains20')
        # apply class Inst() node
        self.add_node()
        self.vs[21]["name"] = """"""
        self.vs[21]["classtype"] = """Inst"""
        self.vs[21]["mm__"] = """Inst"""
        self.vs[21]["cardinality"] = """1"""
        #self.vs[21]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply_contains node for class Inst()
        self.add_node()
        self.vs[22]["mm__"] = """apply_contains"""
        #self.vs[22]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains22')
        # apply class Inst() node
        self.add_node()
        self.vs[23]["name"] = """"""
        self.vs[23]["classtype"] = """Inst"""
        self.vs[23]["mm__"] = """Inst"""
        self.vs[23]["cardinality"] = """1"""
        #self.vs[23]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply_contains node for class Inst()
        self.add_node()
        self.vs[24]["mm__"] = """apply_contains"""
        #self.vs[24]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains24')
        # apply class Name() node
        self.add_node()
        self.vs[25]["name"] = """"""
        self.vs[25]["classtype"] = """Name"""
        self.vs[25]["mm__"] = """Name"""
        self.vs[25]["cardinality"] = """1"""
        #self.vs[25]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply_contains node for class Name()
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
        # apply class Name() node
        self.add_node()
        self.vs[35]["name"] = """"""
        self.vs[35]["classtype"] = """Name"""
        self.vs[35]["mm__"] = """Name"""
        self.vs[35]["cardinality"] = """1"""
        #self.vs[35]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply_contains node for class Name()
        self.add_node()
        self.vs[36]["mm__"] = """apply_contains"""
        #self.vs[36]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains36')
        # apply class Name() node
        self.add_node()
        self.vs[37]["name"] = """"""
        self.vs[37]["classtype"] = """Name"""
        self.vs[37]["mm__"] = """Name"""
        self.vs[37]["cardinality"] = """1"""
        #self.vs[37]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply_contains node for class Name()
        self.add_node()
        self.vs[38]["mm__"] = """apply_contains"""
        #self.vs[38]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains38')
        
        
        
        # apply association ProcDef--p-->LocalDef node
        self.add_node()
        self.vs[39]["associationType"] = """p"""
        self.vs[39]["mm__"] = """directLink_T"""
        #self.vs[39]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc39')
        # apply association ProcDef--channelNames-->Name node
        self.add_node()
        self.vs[40]["associationType"] = """channelNames"""
        self.vs[40]["mm__"] = """directLink_T"""
        #self.vs[40]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc40')
        # apply association LocalDef--p-->New node
        self.add_node()
        self.vs[41]["associationType"] = """p"""
        self.vs[41]["mm__"] = """directLink_T"""
        #self.vs[41]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc41')
        # apply association New--channelNames-->Name node
        self.add_node()
        self.vs[42]["associationType"] = """channelNames"""
        self.vs[42]["mm__"] = """directLink_T"""
        #self.vs[42]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc42')
        # apply association New--channelNames-->Name node
        self.add_node()
        self.vs[43]["associationType"] = """channelNames"""
        self.vs[43]["mm__"] = """directLink_T"""
        #self.vs[43]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc43')
        # apply association New--channelNames-->Name node
        self.add_node()
        self.vs[44]["associationType"] = """channelNames"""
        self.vs[44]["mm__"] = """directLink_T"""
        #self.vs[44]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc44')
        # apply association New--p-->Par node
        self.add_node()
        self.vs[45]["associationType"] = """p"""
        self.vs[45]["mm__"] = """directLink_T"""
        #self.vs[45]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc45')
        # apply association Par--p-->Inst node
        self.add_node()
        self.vs[46]["associationType"] = """p"""
        self.vs[46]["mm__"] = """directLink_T"""
        #self.vs[46]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc46')
        # apply association Par--p-->Inst node
        self.add_node()
        self.vs[47]["associationType"] = """p"""
        self.vs[47]["mm__"] = """directLink_T"""
        #self.vs[47]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc47')
        # apply association Inst--channelNames-->Name node
        self.add_node()
        self.vs[48]["associationType"] = """channelNames"""
        self.vs[48]["mm__"] = """directLink_T"""
        #self.vs[48]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc48')
        # apply association Inst--channelNames-->Name node
        self.add_node()
        self.vs[49]["associationType"] = """channelNames"""
        self.vs[49]["mm__"] = """directLink_T"""
        #self.vs[49]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc49')
        # apply association Inst--channelNames-->Name node
        self.add_node()
        self.vs[50]["associationType"] = """channelNames"""
        self.vs[50]["mm__"] = """directLink_T"""
        #self.vs[50]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc50')
        # apply association Inst--channelNames-->Name node
        self.add_node()
        self.vs[51]["associationType"] = """channelNames"""
        self.vs[51]["mm__"] = """directLink_T"""
        #self.vs[51]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc51')
        # apply association Inst--channelNames-->Name node
        self.add_node()
        self.vs[52]["associationType"] = """channelNames"""
        self.vs[52]["mm__"] = """directLink_T"""
        #self.vs[52]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc52')
        # apply association Inst--channelNames-->Name node
        self.add_node()
        self.vs[53]["associationType"] = """channelNames"""
        self.vs[53]["mm__"] = """directLink_T"""
        #self.vs[53]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc53')
        # apply association Inst--channelNames-->Name node
        self.add_node()
        self.vs[54]["associationType"] = """channelNames"""
        self.vs[54]["mm__"] = """directLink_T"""
        #self.vs[54]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc54')
        
        # backward association State---->ProcDef node
        self.add_node()
        self.vs[55]["type"] = """ruleDef"""
        self.vs[55]["mm__"] = """backward_link"""
        #self.vs[55]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'blink55')
        
        
        # has match attribute isComposite() node
        self.add_node()
        self.vs[56]["mm__"] = """hasAttribute_S"""
        #self.vs[56]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # match attribute isComposite() node
        self.add_node()
        self.vs[57]["name"] = """isComposite"""
        self.vs[57]["mm__"] = """Attribute"""
        self.vs[57]["Type"] = """'String'"""
        #self.vs[57]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match attribute equation isComposite() node
        self.add_node()
        self.vs[58]["name"] = """eq_"""
        self.vs[58]["mm__"] = """Equation"""
        #self.vs[58]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # match attribute equation left expr isComposite() node
        self.add_node()
        self.vs[59]["mm__"] = """leftExpr"""
        #self.vs[59]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # match attribute equation right expr isComposite() node
        self.add_node()
        self.vs[60]["mm__"] = """rightExpr"""
        #self.vs[60]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # apply attribute atom isComposite() node
        self.add_node()
        self.vs[61]["name"] = """true"""
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
        # apply attribute atom literal() node
        self.add_node()
        self.vs[67]["name"] = """sh"""
        self.vs[67]["mm__"] = """Constant"""
        self.vs[67]["Type"] = """'String'"""
        #self.vs[67]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom67')
        # has apply attribute literal() node
        self.add_node()
        self.vs[68]["mm__"] = """hasAttribute_T"""
        #self.vs[68]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # apply attribute literal() node
        self.add_node()
        self.vs[69]["name"] = """literal"""
        self.vs[69]["mm__"] = """Attribute"""
        self.vs[69]["Type"] = """'String'"""
        #self.vs[69]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply attribute equation literal() node
        self.add_node()
        self.vs[70]["name"] = """eq_"""
        self.vs[70]["mm__"] = """Equation"""
        #self.vs[70]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # apply attribute equation left expr literal() node
        self.add_node()
        self.vs[71]["mm__"] = """leftExpr"""
        #self.vs[71]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # apply attribute equation right expr literal() node
        self.add_node()
        self.vs[72]["mm__"] = """rightExpr"""
        #self.vs[72]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # apply attribute atom literal() node
        self.add_node()
        self.vs[73]["name"] = """exit_in"""
        self.vs[73]["mm__"] = """Constant"""
        self.vs[73]["Type"] = """'String'"""
        #self.vs[73]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom73')
        # has apply attribute literal() node
        self.add_node()
        self.vs[74]["mm__"] = """hasAttribute_T"""
        #self.vs[74]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # apply attribute literal() node
        self.add_node()
        self.vs[75]["name"] = """literal"""
        self.vs[75]["mm__"] = """Attribute"""
        self.vs[75]["Type"] = """'String'"""
        #self.vs[75]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply attribute equation literal() node
        self.add_node()
        self.vs[76]["name"] = """eq_"""
        self.vs[76]["mm__"] = """Equation"""
        #self.vs[76]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # apply attribute equation left expr literal() node
        self.add_node()
        self.vs[77]["mm__"] = """leftExpr"""
        #self.vs[77]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # apply attribute equation right expr literal() node
        self.add_node()
        self.vs[78]["mm__"] = """rightExpr"""
        #self.vs[78]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # apply attribute atom literal() node
        self.add_node()
        self.vs[79]["name"] = """exack_in"""
        self.vs[79]["mm__"] = """Constant"""
        self.vs[79]["Type"] = """'String'"""
        #self.vs[79]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom79')
        # has apply attribute literal() node
        self.add_node()
        self.vs[80]["mm__"] = """hasAttribute_T"""
        #self.vs[80]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # apply attribute literal() node
        self.add_node()
        self.vs[81]["name"] = """literal"""
        self.vs[81]["mm__"] = """Attribute"""
        self.vs[81]["Type"] = """'String'"""
        #self.vs[81]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply attribute equation literal() node
        self.add_node()
        self.vs[82]["name"] = """eq_"""
        self.vs[82]["mm__"] = """Equation"""
        #self.vs[82]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # apply attribute equation left expr literal() node
        self.add_node()
        self.vs[83]["mm__"] = """leftExpr"""
        #self.vs[83]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # apply attribute equation right expr literal() node
        self.add_node()
        self.vs[84]["mm__"] = """rightExpr"""
        #self.vs[84]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # apply attribute atom literal() node
        self.add_node()
        self.vs[85]["name"] = """sh_in"""
        self.vs[85]["mm__"] = """Constant"""
        self.vs[85]["Type"] = """'String'"""
        #self.vs[85]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom85')
        # has apply attribute name() node
        self.add_node()
        self.vs[86]["mm__"] = """hasAttribute_T"""
        #self.vs[86]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # apply attribute name() node
        self.add_node()
        self.vs[87]["name"] = """name"""
        self.vs[87]["mm__"] = """Attribute"""
        self.vs[87]["Type"] = """'String'"""
        #self.vs[87]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply attribute equation name() node
        self.add_node()
        self.vs[88]["name"] = """eq_"""
        self.vs[88]["mm__"] = """Equation"""
        #self.vs[88]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # apply attribute equation left expr name() node
        self.add_node()
        self.vs[89]["mm__"] = """leftExpr"""
        #self.vs[89]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # apply attribute equation right expr name() node
        self.add_node()
        self.vs[90]["mm__"] = """rightExpr"""
        #self.vs[90]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # apply attribute atom name() node
        self.add_node()
        self.vs[91]["name"] = """C"""
        self.vs[91]["mm__"] = """Constant"""
        self.vs[91]["Type"] = """'String'"""
        #self.vs[91]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom91')
        # has apply attribute name() node
        self.add_node()
        self.vs[92]["mm__"] = """hasAttribute_T"""
        #self.vs[92]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # apply attribute name() node
        self.add_node()
        self.vs[93]["name"] = """name"""
        self.vs[93]["mm__"] = """Attribute"""
        self.vs[93]["Type"] = """'String'"""
        #self.vs[93]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply attribute equation name() node
        self.add_node()
        self.vs[94]["name"] = """eq_"""
        self.vs[94]["mm__"] = """Equation"""
        #self.vs[94]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # apply attribute equation left expr name() node
        self.add_node()
        self.vs[95]["mm__"] = """leftExpr"""
        #self.vs[95]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # apply attribute equation right expr name() node
        self.add_node()
        self.vs[96]["mm__"] = """rightExpr"""
        #self.vs[96]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # apply attribute atom name() node
        self.add_node()
        self.vs[97]["name"] = """H"""
        self.vs[97]["mm__"] = """Constant"""
        self.vs[97]["Type"] = """'String'"""
        #self.vs[97]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom97')
        # has apply attribute literal() node
        self.add_node()
        self.vs[98]["mm__"] = """hasAttribute_T"""
        #self.vs[98]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # apply attribute literal() node
        self.add_node()
        self.vs[99]["name"] = """literal"""
        self.vs[99]["mm__"] = """Attribute"""
        self.vs[99]["Type"] = """'String'"""
        #self.vs[99]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply attribute equation literal() node
        self.add_node()
        self.vs[100]["name"] = """eq_"""
        self.vs[100]["mm__"] = """Equation"""
        #self.vs[100]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # apply attribute equation left expr literal() node
        self.add_node()
        self.vs[101]["mm__"] = """leftExpr"""
        #self.vs[101]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # apply attribute equation right expr literal() node
        self.add_node()
        self.vs[102]["mm__"] = """rightExpr"""
        #self.vs[102]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # apply attribute atom literal() node
        self.add_node()
        self.vs[103]["name"] = """enp"""
        self.vs[103]["mm__"] = """Constant"""
        self.vs[103]["Type"] = """'String'"""
        #self.vs[103]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom103')
        # has apply attribute literal() node
        self.add_node()
        self.vs[104]["mm__"] = """hasAttribute_T"""
        #self.vs[104]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # apply attribute literal() node
        self.add_node()
        self.vs[105]["name"] = """literal"""
        self.vs[105]["mm__"] = """Attribute"""
        self.vs[105]["Type"] = """'String'"""
        #self.vs[105]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply attribute equation literal() node
        self.add_node()
        self.vs[106]["name"] = """eq_"""
        self.vs[106]["mm__"] = """Equation"""
        #self.vs[106]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # apply attribute equation left expr literal() node
        self.add_node()
        self.vs[107]["mm__"] = """leftExpr"""
        #self.vs[107]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # apply attribute equation right expr literal() node
        self.add_node()
        self.vs[108]["mm__"] = """rightExpr"""
        #self.vs[108]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # apply attribute atom literal() node
        self.add_node()
        self.vs[109]["name"] = """exit_in"""
        self.vs[109]["mm__"] = """Constant"""
        self.vs[109]["Type"] = """'String'"""
        #self.vs[109]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom109')
        # has apply attribute literal() node
        self.add_node()
        self.vs[110]["mm__"] = """hasAttribute_T"""
        #self.vs[110]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # apply attribute literal() node
        self.add_node()
        self.vs[111]["name"] = """literal"""
        self.vs[111]["mm__"] = """Attribute"""
        self.vs[111]["Type"] = """'String'"""
        #self.vs[111]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply attribute equation literal() node
        self.add_node()
        self.vs[112]["name"] = """eq_"""
        self.vs[112]["mm__"] = """Equation"""
        #self.vs[112]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # apply attribute equation left expr literal() node
        self.add_node()
        self.vs[113]["mm__"] = """leftExpr"""
        #self.vs[113]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # apply attribute equation right expr literal() node
        self.add_node()
        self.vs[114]["mm__"] = """rightExpr"""
        #self.vs[114]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # apply attribute atom literal() node
        self.add_node()
        self.vs[115]["name"] = """exack_in"""
        self.vs[115]["mm__"] = """Constant"""
        self.vs[115]["Type"] = """'String'"""
        #self.vs[115]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom115')
        # has apply attribute literal() node
        self.add_node()
        self.vs[116]["mm__"] = """hasAttribute_T"""
        #self.vs[116]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # apply attribute literal() node
        self.add_node()
        self.vs[117]["name"] = """literal"""
        self.vs[117]["mm__"] = """Attribute"""
        self.vs[117]["Type"] = """'String'"""
        #self.vs[117]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply attribute equation literal() node
        self.add_node()
        self.vs[118]["name"] = """eq_"""
        self.vs[118]["mm__"] = """Equation"""
        #self.vs[118]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # apply attribute equation left expr literal() node
        self.add_node()
        self.vs[119]["mm__"] = """leftExpr"""
        #self.vs[119]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # apply attribute equation right expr literal() node
        self.add_node()
        self.vs[120]["mm__"] = """rightExpr"""
        #self.vs[120]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # apply attribute atom literal() node
        self.add_node()
        self.vs[121]["name"] = """sh_in"""
        self.vs[121]["mm__"] = """Constant"""
        self.vs[121]["Type"] = """'String'"""
        #self.vs[121]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom121')
        # has apply attribute literal() node
        self.add_node()
        self.vs[122]["mm__"] = """hasAttribute_T"""
        #self.vs[122]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # apply attribute literal() node
        self.add_node()
        self.vs[123]["name"] = """literal"""
        self.vs[123]["mm__"] = """Attribute"""
        self.vs[123]["Type"] = """'String'"""
        #self.vs[123]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply attribute equation literal() node
        self.add_node()
        self.vs[124]["name"] = """eq_"""
        self.vs[124]["mm__"] = """Equation"""
        #self.vs[124]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # apply attribute equation left expr literal() node
        self.add_node()
        self.vs[125]["mm__"] = """leftExpr"""
        #self.vs[125]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # apply attribute equation right expr literal() node
        self.add_node()
        self.vs[126]["mm__"] = """rightExpr"""
        #self.vs[126]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # apply attribute atom literal() node
        self.add_node()
        self.vs[127]["name"] = """exit_in"""
        self.vs[127]["mm__"] = """Constant"""
        self.vs[127]["Type"] = """'String'"""
        #self.vs[127]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom127')
        # has apply attribute literal() node
        self.add_node()
        self.vs[128]["mm__"] = """hasAttribute_T"""
        #self.vs[128]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # apply attribute literal() node
        self.add_node()
        self.vs[129]["name"] = """literal"""
        self.vs[129]["mm__"] = """Attribute"""
        self.vs[129]["Type"] = """'String'"""
        #self.vs[129]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply attribute equation literal() node
        self.add_node()
        self.vs[130]["name"] = """eq_"""
        self.vs[130]["mm__"] = """Equation"""
        #self.vs[130]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # apply attribute equation left expr literal() node
        self.add_node()
        self.vs[131]["mm__"] = """leftExpr"""
        #self.vs[131]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # apply attribute equation right expr literal() node
        self.add_node()
        self.vs[132]["mm__"] = """rightExpr"""
        #self.vs[132]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # apply attribute atom literal() node
        self.add_node()
        self.vs[133]["name"] = """exack_in"""
        self.vs[133]["mm__"] = """Constant"""
        self.vs[133]["Type"] = """'String'"""
        #self.vs[133]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom133')
        # has apply attribute literal() node
        self.add_node()
        self.vs[134]["mm__"] = """hasAttribute_T"""
        #self.vs[134]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
        # apply attribute literal() node
        self.add_node()
        self.vs[135]["name"] = """literal"""
        self.vs[135]["mm__"] = """Attribute"""
        self.vs[135]["Type"] = """'String'"""
        #self.vs[135]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # apply attribute equation literal() node
        self.add_node()
        self.vs[136]["name"] = """eq_"""
        self.vs[136]["mm__"] = """Equation"""
        #self.vs[136]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
        # apply attribute equation left expr literal() node
        self.add_node()
        self.vs[137]["mm__"] = """leftExpr"""
        #self.vs[137]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
        # apply attribute equation right expr literal() node
        self.add_node()
        self.vs[138]["mm__"] = """rightExpr"""
        #self.vs[138]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        # apply attribute atom literal() node
        self.add_node()
        self.vs[139]["name"] = """sh_in"""
        self.vs[139]["mm__"] = """Constant"""
        self.vs[139]["Type"] = """'String'"""
        #self.vs[139]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom139')
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class State()
                (1,6), # applymodel -> apply_contains
                (6,5), # apply_contains -> apply_class ProcDef()
                (1,8), # applymodel -> apply_contains
                (8,7), # apply_contains -> apply_class LocalDef()
                (1,10), # applymodel -> apply_contains
                (10,9), # apply_contains -> apply_class Name()
                (1,12), # applymodel -> apply_contains
                (12,11), # apply_contains -> apply_class New()
                (1,14), # applymodel -> apply_contains
                (14,13), # apply_contains -> apply_class Name()
                (1,16), # applymodel -> apply_contains
                (16,15), # apply_contains -> apply_class Name()
                (1,18), # applymodel -> apply_contains
                (18,17), # apply_contains -> apply_class Name()
                (1,20), # applymodel -> apply_contains
                (20,19), # apply_contains -> apply_class Par()
                (1,22), # applymodel -> apply_contains
                (22,21), # apply_contains -> apply_class Inst()
                (1,24), # applymodel -> apply_contains
                (24,23), # apply_contains -> apply_class Inst()
                (1,26), # applymodel -> apply_contains
                (26,25), # apply_contains -> apply_class Name()
                (1,28), # applymodel -> apply_contains
                (28,27), # apply_contains -> apply_class Name()
                (1,30), # applymodel -> apply_contains
                (30,29), # apply_contains -> apply_class Name()
                (1,32), # applymodel -> apply_contains
                (32,31), # apply_contains -> apply_class Name()
                (1,34), # applymodel -> apply_contains
                (34,33), # apply_contains -> apply_class Name()
                (1,36), # applymodel -> apply_contains
                (36,35), # apply_contains -> apply_class Name()
                (1,38), # applymodel -> apply_contains
                (38,37), # apply_contains -> apply_class Name()
                (5,39), # apply_class ProcDef() -> association p
                (39,7), # association p  -> apply_class LocalDef()
                (5,40), # apply_class ProcDef() -> association channelNames
                (40,9), # association channelNames  -> apply_class Name()
                (7,41), # apply_class LocalDef() -> association p
                (41,11), # association p  -> apply_class New()
                (11,42), # apply_class New() -> association channelNames
                (42,13), # association channelNames  -> apply_class Name()
                (11,43), # apply_class New() -> association channelNames
                (43,15), # association channelNames  -> apply_class Name()
                (11,44), # apply_class New() -> association channelNames
                (44,17), # association channelNames  -> apply_class Name()
                (11,45), # apply_class New() -> association p
                (45,19), # association p  -> apply_class Par()
                (19,46), # apply_class Par() -> association p
                (46,23), # association p  -> apply_class Inst()
                (19,47), # apply_class Par() -> association p
                (47,21), # association p  -> apply_class Inst()
                (21,48), # apply_class Inst() -> association channelNames
                (48,25), # association channelNames  -> apply_class Name()
                (21,49), # apply_class Inst() -> association channelNames
                (49,27), # association channelNames  -> apply_class Name()
                (21,50), # apply_class Inst() -> association channelNames
                (50,29), # association channelNames  -> apply_class Name()
                (21,51), # apply_class Inst() -> association channelNames
                (51,31), # association channelNames  -> apply_class Name()
                (23,52), # apply_class Inst() -> association channelNames
                (52,33), # association channelNames  -> apply_class Name()
                (23,53), # apply_class Inst() -> association channelNames
                (53,35), # association channelNames  -> apply_class Name()
                (23,54), # apply_class Inst() -> association channelNames
                (54,37), # association channelNames  -> apply_class Name()
                (5,55), # apply_class ProcDef() -> backward_association
                (55,3), #  backward_association -> apply_class State()
                (3,56), # match_class State() -> has_match_attribute isComposite ()
                (56,57), #  has_match_attribute isComposite () -> match_attribute isComposite ()
                (58,59), #  equation of match attribute isComposite () -> left_expr
                (59,57), #  left_expr -> match_attribute isComposite ()
                (58,60), #  equation of match attribute isComposite () -> right_expr
                (60,61), # right_expr --> term
                (9,62), # apply_class Name() -> has_apply_attribute literal ()
                (62,63), #  has_apply_attribute literal () -> apply_attribute literal ()
                (64,65), #  equation of apply attribute literal () -> left_expr
                (65,63), #  left_expr -> apply_attribute literal ()
                (64,66), #  equation of apply attribute literal () -> right_expr
                (66,67), # right_expr --> term
                (13,68), # apply_class Name() -> has_apply_attribute literal ()
                (68,69), #  has_apply_attribute literal () -> apply_attribute literal ()
                (70,71), #  equation of apply attribute literal () -> left_expr
                (71,69), #  left_expr -> apply_attribute literal ()
                (70,72), #  equation of apply attribute literal () -> right_expr
                (72,73), # right_expr --> term
                (15,74), # apply_class Name() -> has_apply_attribute literal ()
                (74,75), #  has_apply_attribute literal () -> apply_attribute literal ()
                (76,77), #  equation of apply attribute literal () -> left_expr
                (77,75), #  left_expr -> apply_attribute literal ()
                (76,78), #  equation of apply attribute literal () -> right_expr
                (78,79), # right_expr --> term
                (17,80), # apply_class Name() -> has_apply_attribute literal ()
                (80,81), #  has_apply_attribute literal () -> apply_attribute literal ()
                (82,83), #  equation of apply attribute literal () -> left_expr
                (83,81), #  left_expr -> apply_attribute literal ()
                (82,84), #  equation of apply attribute literal () -> right_expr
                (84,85), # right_expr --> term
                (21,86), # apply_class Inst() -> has_apply_attribute name ()
                (86,87), #  has_apply_attribute name () -> apply_attribute name ()
                (88,89), #  equation of apply attribute name () -> left_expr
                (89,87), #  left_expr -> apply_attribute name ()
                (88,90), #  equation of apply attribute name () -> right_expr
                (90,91), # right_expr --> term
                (23,92), # apply_class Inst() -> has_apply_attribute name ()
                (92,93), #  has_apply_attribute name () -> apply_attribute name ()
                (94,95), #  equation of apply attribute name () -> left_expr
                (95,93), #  left_expr -> apply_attribute name ()
                (94,96), #  equation of apply attribute name () -> right_expr
                (96,97), # right_expr --> term
                (25,98), # apply_class Name() -> has_apply_attribute literal ()
                (98,99), #  has_apply_attribute literal () -> apply_attribute literal ()
                (100,101), #  equation of apply attribute literal () -> left_expr
                (101,99), #  left_expr -> apply_attribute literal ()
                (100,102), #  equation of apply attribute literal () -> right_expr
                (102,103), # right_expr --> term
                (27,104), # apply_class Name() -> has_apply_attribute literal ()
                (104,105), #  has_apply_attribute literal () -> apply_attribute literal ()
                (106,107), #  equation of apply attribute literal () -> left_expr
                (107,105), #  left_expr -> apply_attribute literal ()
                (106,108), #  equation of apply attribute literal () -> right_expr
                (108,109), # right_expr --> term
                (29,110), # apply_class Name() -> has_apply_attribute literal ()
                (110,111), #  has_apply_attribute literal () -> apply_attribute literal ()
                (112,113), #  equation of apply attribute literal () -> left_expr
                (113,111), #  left_expr -> apply_attribute literal ()
                (112,114), #  equation of apply attribute literal () -> right_expr
                (114,115), # right_expr --> term
                (31,116), # apply_class Name() -> has_apply_attribute literal ()
                (116,117), #  has_apply_attribute literal () -> apply_attribute literal ()
                (118,119), #  equation of apply attribute literal () -> left_expr
                (119,117), #  left_expr -> apply_attribute literal ()
                (118,120), #  equation of apply attribute literal () -> right_expr
                (120,121), # right_expr --> term
                (33,122), # apply_class Name() -> has_apply_attribute literal ()
                (122,123), #  has_apply_attribute literal () -> apply_attribute literal ()
                (124,125), #  equation of apply attribute literal () -> left_expr
                (125,123), #  left_expr -> apply_attribute literal ()
                (124,126), #  equation of apply attribute literal () -> right_expr
                (126,127), # right_expr --> term
                (35,128), # apply_class Name() -> has_apply_attribute literal ()
                (128,129), #  has_apply_attribute literal () -> apply_attribute literal ()
                (130,131), #  equation of apply attribute literal () -> left_expr
                (131,129), #  left_expr -> apply_attribute literal ()
                (130,132), #  equation of apply attribute literal () -> right_expr
                (132,133), # right_expr --> term
                (37,134), # apply_class Name() -> has_apply_attribute literal ()
                (134,135), #  has_apply_attribute literal () -> apply_attribute literal ()
                (136,137), #  equation of apply attribute literal () -> left_expr
                (137,135), #  left_expr -> apply_attribute literal ()
                (136,138), #  equation of apply attribute literal () -> right_expr
                (138,139), # right_expr --> term
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel
        ])
        
