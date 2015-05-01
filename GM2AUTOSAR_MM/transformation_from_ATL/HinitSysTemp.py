from core.himesis import Himesis
import cPickle as pickle
import uuid

class HinitSysTemp(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule initSysTemp.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HinitSysTemp, self).__init__(name='HinitSysTemp', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        # TODO Levi, need some help here because I don't know where does 
        # this value come from.
        self["mm__"] = pickle.loads("""(lp1
S'HimesisMM'
p2
a.""")
        
        self["name"] = """initSysTemp"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'initSysTemp')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'initSysTempmatchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'initSysTempapplymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'initSysTemppairedwith2')
        
    	# match class PhysicalNode() node
    	self.add_node()
    	self.vs[3]["name"] = """"""
        self.vs[3]["classtype"] = """PhysicalNode"""
        self.vs[3]["mm__"] = """PhysicalNode"""
        self.vs[3]["cardinality"] = """+"""
        #self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# match_contains node for class PhysicalNode()
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        #self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'matchcontains4')
    	# match class Partition() node
    	self.add_node()
    	self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """Partition"""
        self.vs[5]["mm__"] = """Partition"""
        self.vs[5]["cardinality"] = """1"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# match_contains node for class Partition()
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        #self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'matchcontains6')
    	# match class Module() node
    	self.add_node()
    	self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """Module"""
        self.vs[7]["mm__"] = """Module"""
        self.vs[7]["cardinality"] = """1"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# match_contains node for class Module()
        self.add_node()
        self.vs[8]["mm__"] = """match_contains"""
        #self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'matchcontains8')
        
        
    	# apply class SystemMapping() node
    	self.add_node()
    	self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """SystemMapping"""
        self.vs[9]["mm__"] = """SystemMapping"""
        self.vs[9]["cardinality"] = """1"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply_contains node for class SystemMapping()
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        #self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains10')
    	# apply class System() node
    	self.add_node()
    	self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """System"""
        self.vs[11]["mm__"] = """System"""
        self.vs[11]["cardinality"] = """1"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply_contains node for class System()
        self.add_node()
        self.vs[12]["mm__"] = """apply_contains"""
        #self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains12')
    	# apply class SoftwareComposition() node
    	self.add_node()
    	self.vs[13]["name"] = """"""
        self.vs[13]["classtype"] = """SoftwareComposition"""
        self.vs[13]["mm__"] = """SoftwareComposition"""
        self.vs[13]["cardinality"] = """1"""
        #self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply_contains node for class SoftwareComposition()
        self.add_node()
        self.vs[14]["mm__"] = """apply_contains"""
        #self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains14')
    	# apply class CompositionType() node
    	self.add_node()
    	self.vs[15]["name"] = """"""
        self.vs[15]["classtype"] = """CompositionType"""
        self.vs[15]["mm__"] = """CompositionType"""
        self.vs[15]["cardinality"] = """1"""
        #self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply_contains node for class CompositionType()
        self.add_node()
        self.vs[16]["mm__"] = """apply_contains"""
        #self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains16')
    	# apply class EcuInstance() node
    	self.add_node()
    	self.vs[17]["name"] = """"""
        self.vs[17]["classtype"] = """EcuInstance"""
        self.vs[17]["mm__"] = """EcuInstance"""
        self.vs[17]["cardinality"] = """1"""
        #self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply_contains node for class EcuInstance()
        self.add_node()
        self.vs[18]["mm__"] = """apply_contains"""
        #self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains18')
        
        
    	# match association PhysicalNode--partition-->Partition node
    	self.add_node()
    	self.vs[19]["associationType"] = """partition"""
        self.vs[19]["mm__"] = """directLink_S"""
        #self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc19')
    	# match association Partition--module-->Module node
    	self.add_node()
    	self.vs[20]["associationType"] = """module"""
        self.vs[20]["mm__"] = """directLink_S"""
        #self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc20')
        
    	# apply association System--mapping-->SystemMapping node
    	self.add_node()
    	self.vs[21]["associationType"] = """mapping"""
        self.vs[21]["mm__"] = """directLink_T"""
        #self.vs[21]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc21')
    	# apply association System--softwareComposition-->SoftwareComposition node
    	self.add_node()
    	self.vs[22]["associationType"] = """softwareComposition"""
        self.vs[22]["mm__"] = """directLink_T"""
        #self.vs[22]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc22')
    	# apply association SoftwareComposition--softwareComposition-->CompositionType node
    	self.add_node()
    	self.vs[23]["associationType"] = """softwareComposition"""
        self.vs[23]["mm__"] = """directLink_T"""
        #self.vs[23]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc23')
        
        
        
    	# has match attribute name() node
    	self.add_node()
    	self.vs[24]["mm__"] = """hasAttribute_S"""
        #self.vs[24]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# match attribute name() node
    	self.add_node()
    	self.vs[25]["name"] = """name"""
        self.vs[25]["mm__"] = """Attribute"""
        self.vs[25]["Type"] = """'String'"""
        #self.vs[25]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        
        
    	# has apply attribute shortName() node
    	self.add_node()
    	self.vs[26]["mm__"] = """hasAttribute_T"""
        #self.vs[26]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute shortName() node
    	self.add_node()
    	self.vs[27]["name"] = """shortName"""
        self.vs[27]["mm__"] = """Attribute"""
        self.vs[27]["Type"] = """'String'"""
        #self.vs[27]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation shortName() node
    	self.add_node()
    	self.vs[28]["name"] = """eq_"""
        self.vs[28]["mm__"] = """Equation"""
        #self.vs[28]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr shortName() node
    	self.add_node()
    	self.vs[29]["mm__"] = """leftExpr"""
        #self.vs[29]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr shortName() node
    	self.add_node()
    	self.vs[30]["mm__"] = """rightExpr"""
        #self.vs[30]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# attribute concat shortName() node
    	self.add_node()
    	self.vs[31]["name"] = """Concat31"""
        self.vs[31]["mm__"] = """Concat"""
        self.vs[31]["Type"] = """'String'"""
        #self.vs[31]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concat31')
    	# apply attribute concat has left args shortName() node
        self.add_node()
    	self.vs[32]["mm__"] = """hasArgs"""
        #self.vs[32]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgs32')
    	# apply attribute concat has right args shortName() node
        self.add_node()
    	self.vs[33]["mm__"] = """hasArgs"""
        #self.vs[33]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgs33')
    	# apply attribute atom shortName() node
    	self.add_node()
    	self.vs[34]["name"] = """SysMapping_"""
        self.vs[34]["mm__"] = """Constant"""
        self.vs[34]["Type"] = """'String'"""
        #self.vs[34]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom34')
    	# has apply attribute ApplyAttribute() node
    	self.add_node()
    	self.vs[35]["mm__"] = """hasAttribute_T"""
        #self.vs[35]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute ApplyAttribute() node
    	self.add_node()
    	self.vs[36]["name"] = """ApplyAttribute"""
        self.vs[36]["mm__"] = """Attribute"""
        self.vs[36]["Type"] = """'String'"""
        #self.vs[36]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation ApplyAttribute() node
    	self.add_node()
    	self.vs[37]["name"] = """eq_"""
        self.vs[37]["mm__"] = """Equation"""
        #self.vs[37]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr ApplyAttribute() node
    	self.add_node()
    	self.vs[38]["mm__"] = """leftExpr"""
        #self.vs[38]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr ApplyAttribute() node
    	self.add_node()
    	self.vs[39]["mm__"] = """rightExpr"""
        #self.vs[39]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# apply attribute atom ApplyAttribute() node
    	self.add_node()
    	self.vs[40]["name"] = """solveRef"""
        self.vs[40]["mm__"] = """Constant"""
        self.vs[40]["Type"] = """'String'"""
        #self.vs[40]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom40')
    	# has apply attribute shortName() node
    	self.add_node()
    	self.vs[41]["mm__"] = """hasAttribute_T"""
        #self.vs[41]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute shortName() node
    	self.add_node()
    	self.vs[42]["name"] = """shortName"""
        self.vs[42]["mm__"] = """Attribute"""
        self.vs[42]["Type"] = """'String'"""
        #self.vs[42]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation shortName() node
    	self.add_node()
    	self.vs[43]["name"] = """eq_"""
        self.vs[43]["mm__"] = """Equation"""
        #self.vs[43]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr shortName() node
    	self.add_node()
    	self.vs[44]["mm__"] = """leftExpr"""
        #self.vs[44]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr shortName() node
    	self.add_node()
    	self.vs[45]["mm__"] = """rightExpr"""
        #self.vs[45]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# attribute concat shortName() node
    	self.add_node()
    	self.vs[46]["name"] = """Concat46"""
        self.vs[46]["mm__"] = """Concat"""
        self.vs[46]["Type"] = """'String'"""
        #self.vs[46]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concat46')
    	# apply attribute concat has left args shortName() node
        self.add_node()
    	self.vs[47]["mm__"] = """hasArgs"""
        #self.vs[47]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgs47')
    	# apply attribute concat has right args shortName() node
        self.add_node()
    	self.vs[48]["mm__"] = """hasArgs"""
        #self.vs[48]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgs48')
    	# apply attribute atom shortName() node
    	self.add_node()
    	self.vs[49]["name"] = """SysTemplate_"""
        self.vs[49]["mm__"] = """Constant"""
        self.vs[49]["Type"] = """'String'"""
        #self.vs[49]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom49')
    	# has apply attribute ApplyAttribute() node
    	self.add_node()
    	self.vs[50]["mm__"] = """hasAttribute_T"""
        #self.vs[50]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute ApplyAttribute() node
    	self.add_node()
    	self.vs[51]["name"] = """ApplyAttribute"""
        self.vs[51]["mm__"] = """Attribute"""
        self.vs[51]["Type"] = """'String'"""
        #self.vs[51]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation ApplyAttribute() node
    	self.add_node()
    	self.vs[52]["name"] = """eq_"""
        self.vs[52]["mm__"] = """Equation"""
        #self.vs[52]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr ApplyAttribute() node
    	self.add_node()
    	self.vs[53]["mm__"] = """leftExpr"""
        #self.vs[53]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr ApplyAttribute() node
    	self.add_node()
    	self.vs[54]["mm__"] = """rightExpr"""
        #self.vs[54]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# apply attribute atom ApplyAttribute() node
    	self.add_node()
    	self.vs[55]["name"] = """solveRef"""
        self.vs[55]["mm__"] = """Constant"""
        self.vs[55]["Type"] = """'String'"""
        #self.vs[55]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom55')
    	# has apply attribute shortName() node
    	self.add_node()
    	self.vs[56]["mm__"] = """hasAttribute_T"""
        #self.vs[56]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute shortName() node
    	self.add_node()
    	self.vs[57]["name"] = """shortName"""
        self.vs[57]["mm__"] = """Attribute"""
        self.vs[57]["Type"] = """'String'"""
        #self.vs[57]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation shortName() node
    	self.add_node()
    	self.vs[58]["name"] = """eq_"""
        self.vs[58]["mm__"] = """Equation"""
        #self.vs[58]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr shortName() node
    	self.add_node()
    	self.vs[59]["mm__"] = """leftExpr"""
        #self.vs[59]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr shortName() node
    	self.add_node()
    	self.vs[60]["mm__"] = """rightExpr"""
        #self.vs[60]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# attribute concat shortName() node
    	self.add_node()
    	self.vs[61]["name"] = """Concat61"""
        self.vs[61]["mm__"] = """Concat"""
        self.vs[61]["Type"] = """'String'"""
        #self.vs[61]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concat61')
    	# apply attribute concat has left args shortName() node
        self.add_node()
    	self.vs[62]["mm__"] = """hasArgs"""
        #self.vs[62]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgs62')
    	# apply attribute concat has right args shortName() node
        self.add_node()
    	self.vs[63]["mm__"] = """hasArgs"""
        #self.vs[63]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgs63')
    	# apply attribute atom shortName() node
    	self.add_node()
    	self.vs[64]["name"] = """SoftwareComposition_"""
        self.vs[64]["mm__"] = """Constant"""
        self.vs[64]["Type"] = """'String'"""
        #self.vs[64]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom64')
    	# has apply attribute ApplyAttribute() node
    	self.add_node()
    	self.vs[65]["mm__"] = """hasAttribute_T"""
        #self.vs[65]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute ApplyAttribute() node
    	self.add_node()
    	self.vs[66]["name"] = """ApplyAttribute"""
        self.vs[66]["mm__"] = """Attribute"""
        self.vs[66]["Type"] = """'String'"""
        #self.vs[66]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation ApplyAttribute() node
    	self.add_node()
    	self.vs[67]["name"] = """eq_"""
        self.vs[67]["mm__"] = """Equation"""
        #self.vs[67]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr ApplyAttribute() node
    	self.add_node()
    	self.vs[68]["mm__"] = """leftExpr"""
        #self.vs[68]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr ApplyAttribute() node
    	self.add_node()
    	self.vs[69]["mm__"] = """rightExpr"""
        #self.vs[69]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# apply attribute atom ApplyAttribute() node
    	self.add_node()
    	self.vs[70]["name"] = """solveRef"""
        self.vs[70]["mm__"] = """Constant"""
        self.vs[70]["Type"] = """'String'"""
        #self.vs[70]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom70')
    	# has apply attribute shortName() node
    	self.add_node()
    	self.vs[71]["mm__"] = """hasAttribute_T"""
        #self.vs[71]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute shortName() node
    	self.add_node()
    	self.vs[72]["name"] = """shortName"""
        self.vs[72]["mm__"] = """Attribute"""
        self.vs[72]["Type"] = """'String'"""
        #self.vs[72]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation shortName() node
    	self.add_node()
    	self.vs[73]["name"] = """eq_"""
        self.vs[73]["mm__"] = """Equation"""
        #self.vs[73]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr shortName() node
    	self.add_node()
    	self.vs[74]["mm__"] = """leftExpr"""
        #self.vs[74]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr shortName() node
    	self.add_node()
    	self.vs[75]["mm__"] = """rightExpr"""
        #self.vs[75]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# attribute concat shortName() node
    	self.add_node()
    	self.vs[76]["name"] = """Concat76"""
        self.vs[76]["mm__"] = """Concat"""
        self.vs[76]["Type"] = """'String'"""
        #self.vs[76]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concat76')
    	# apply attribute concat has left args shortName() node
        self.add_node()
    	self.vs[77]["mm__"] = """hasArgs"""
        #self.vs[77]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgs77')
    	# apply attribute concat has right args shortName() node
        self.add_node()
    	self.vs[78]["mm__"] = """hasArgs"""
        #self.vs[78]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgs78')
    	# apply attribute atom shortName() node
    	self.add_node()
    	self.vs[79]["name"] = """CompositionType_"""
        self.vs[79]["mm__"] = """Constant"""
        self.vs[79]["Type"] = """'String'"""
        #self.vs[79]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom79')
    	# has apply attribute ApplyAttribute() node
    	self.add_node()
    	self.vs[80]["mm__"] = """hasAttribute_T"""
        #self.vs[80]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute ApplyAttribute() node
    	self.add_node()
    	self.vs[81]["name"] = """ApplyAttribute"""
        self.vs[81]["mm__"] = """Attribute"""
        self.vs[81]["Type"] = """'String'"""
        #self.vs[81]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation ApplyAttribute() node
    	self.add_node()
    	self.vs[82]["name"] = """eq_"""
        self.vs[82]["mm__"] = """Equation"""
        #self.vs[82]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr ApplyAttribute() node
    	self.add_node()
    	self.vs[83]["mm__"] = """leftExpr"""
        #self.vs[83]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr ApplyAttribute() node
    	self.add_node()
    	self.vs[84]["mm__"] = """rightExpr"""
        #self.vs[84]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# apply attribute atom ApplyAttribute() node
    	self.add_node()
    	self.vs[85]["name"] = """solveRef"""
        self.vs[85]["mm__"] = """Constant"""
        self.vs[85]["Type"] = """'String'"""
        #self.vs[85]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom85')
    	# has apply attribute shortName() node
    	self.add_node()
    	self.vs[86]["mm__"] = """hasAttribute_T"""
        #self.vs[86]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute shortName() node
    	self.add_node()
    	self.vs[87]["name"] = """shortName"""
        self.vs[87]["mm__"] = """Attribute"""
        self.vs[87]["Type"] = """'String'"""
        #self.vs[87]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation shortName() node
    	self.add_node()
    	self.vs[88]["name"] = """eq_"""
        self.vs[88]["mm__"] = """Equation"""
        #self.vs[88]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr shortName() node
    	self.add_node()
    	self.vs[89]["mm__"] = """leftExpr"""
        #self.vs[89]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr shortName() node
    	self.add_node()
    	self.vs[90]["mm__"] = """rightExpr"""
        #self.vs[90]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# attribute concat shortName() node
    	self.add_node()
    	self.vs[91]["name"] = """Concat91"""
        self.vs[91]["mm__"] = """Concat"""
        self.vs[91]["Type"] = """'String'"""
        #self.vs[91]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concat91')
    	# apply attribute concat has left args shortName() node
        self.add_node()
    	self.vs[92]["mm__"] = """hasArgs"""
        #self.vs[92]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgs92')
    	# apply attribute concat has right args shortName() node
        self.add_node()
    	self.vs[93]["mm__"] = """hasArgs"""
        #self.vs[93]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgs93')
    	# apply attribute atom shortName() node
    	self.add_node()
    	self.vs[94]["name"] = """EcuInstance_"""
        self.vs[94]["mm__"] = """Constant"""
        self.vs[94]["Type"] = """'String'"""
        #self.vs[94]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom94')
        
        
        # Add the edges
        self.add_edges([
    		(0,4), # matchmodel -> match_contains
    		(4,3), # match_contains -> match_class PhysicalNode()
    		(0,6), # matchmodel -> match_contains
    		(6,5), # match_contains -> match_class Partition()
    		(0,8), # matchmodel -> match_contains
    		(8,7), # match_contains -> match_class Module()
    		(1,10), # applymodel -> apply_contains
    		(10,9), # apply_contains -> apply_class SystemMapping()
    		(1,12), # applymodel -> apply_contains
    		(12,11), # apply_contains -> apply_class System()
    		(1,14), # applymodel -> apply_contains
    		(14,13), # apply_contains -> apply_class SoftwareComposition()
    		(1,16), # applymodel -> apply_contains
    		(16,15), # apply_contains -> apply_class CompositionType()
    		(1,18), # applymodel -> apply_contains
    		(18,17), # apply_contains -> apply_class EcuInstance()
    		(3,19), # match_class PhysicalNode() -> association partition
    		(19,5), # association partition  -> match_class Partition()
    		(5,20), # match_class Partition() -> association module
    		(20,7), # association module  -> match_class Module()
    		(11,21), # apply_class System() -> association mapping
    		(21,9), # association mapping  -> apply_class SystemMapping()
    		(11,22), # apply_class System() -> association softwareComposition
    		(22,13), # association softwareComposition  -> apply_class SoftwareComposition()
    		(13,23), # apply_class SoftwareComposition() -> association softwareComposition
    		(23,15), # association softwareComposition  -> apply_class CompositionType()
    		(3,24), # match_class PhysicalNode() -> has_match_attribute name ()
    		(24,25), #  has_match_attribute name () -> match_attribute name ()
    		(9,26), # apply_class SystemMapping() -> has_apply_attribute shortName ()
    		(26,27), #  has_apply_attribute shortName () -> apply_attribute shortName ()
    		(28,29), #  equation of apply attribute shortName () -> left_expr
    		(29,27), #  left_expr -> apply_attribute shortName ()
    		(28,30), #  equation of apply attribute shortName () -> right_expr
    		(31,32), #  apply attribute concat shortName () -> left has_args  
    		(32,34), #  left has_args -> term
    		(31,33), #  apply attribute concat shortName () -> right has_args  
    		(33,25), #  right has_args -> term
    		(30,31), # right_expr --> term
    		(9,35), # apply_class SystemMapping() -> has_apply_attribute ApplyAttribute ()
    		(35,36), #  has_apply_attribute ApplyAttribute () -> apply_attribute ApplyAttribute ()
    		(37,38), #  equation of apply attribute ApplyAttribute () -> left_expr
    		(38,36), #  left_expr -> apply_attribute ApplyAttribute ()
    		(37,39), #  equation of apply attribute ApplyAttribute () -> right_expr
    		(39,40), # right_expr --> term
    		(11,41), # apply_class System() -> has_apply_attribute shortName ()
    		(41,42), #  has_apply_attribute shortName () -> apply_attribute shortName ()
    		(43,44), #  equation of apply attribute shortName () -> left_expr
    		(44,42), #  left_expr -> apply_attribute shortName ()
    		(43,45), #  equation of apply attribute shortName () -> right_expr
    		(46,47), #  apply attribute concat shortName () -> left has_args  
    		(47,49), #  left has_args -> term
    		(46,48), #  apply attribute concat shortName () -> right has_args  
    		(48,25), #  right has_args -> term
    		(45,46), # right_expr --> term
    		(11,50), # apply_class System() -> has_apply_attribute ApplyAttribute ()
    		(50,51), #  has_apply_attribute ApplyAttribute () -> apply_attribute ApplyAttribute ()
    		(52,53), #  equation of apply attribute ApplyAttribute () -> left_expr
    		(53,51), #  left_expr -> apply_attribute ApplyAttribute ()
    		(52,54), #  equation of apply attribute ApplyAttribute () -> right_expr
    		(54,55), # right_expr --> term
    		(13,56), # apply_class SoftwareComposition() -> has_apply_attribute shortName ()
    		(56,57), #  has_apply_attribute shortName () -> apply_attribute shortName ()
    		(58,59), #  equation of apply attribute shortName () -> left_expr
    		(59,57), #  left_expr -> apply_attribute shortName ()
    		(58,60), #  equation of apply attribute shortName () -> right_expr
    		(61,62), #  apply attribute concat shortName () -> left has_args  
    		(62,64), #  left has_args -> term
    		(61,63), #  apply attribute concat shortName () -> right has_args  
    		(63,25), #  right has_args -> term
    		(60,61), # right_expr --> term
    		(13,65), # apply_class SoftwareComposition() -> has_apply_attribute ApplyAttribute ()
    		(65,66), #  has_apply_attribute ApplyAttribute () -> apply_attribute ApplyAttribute ()
    		(67,68), #  equation of apply attribute ApplyAttribute () -> left_expr
    		(68,66), #  left_expr -> apply_attribute ApplyAttribute ()
    		(67,69), #  equation of apply attribute ApplyAttribute () -> right_expr
    		(69,70), # right_expr --> term
    		(15,71), # apply_class CompositionType() -> has_apply_attribute shortName ()
    		(71,72), #  has_apply_attribute shortName () -> apply_attribute shortName ()
    		(73,74), #  equation of apply attribute shortName () -> left_expr
    		(74,72), #  left_expr -> apply_attribute shortName ()
    		(73,75), #  equation of apply attribute shortName () -> right_expr
    		(76,77), #  apply attribute concat shortName () -> left has_args  
    		(77,79), #  left has_args -> term
    		(76,78), #  apply attribute concat shortName () -> right has_args  
    		(78,25), #  right has_args -> term
    		(75,76), # right_expr --> term
    		(15,80), # apply_class CompositionType() -> has_apply_attribute ApplyAttribute ()
    		(80,81), #  has_apply_attribute ApplyAttribute () -> apply_attribute ApplyAttribute ()
    		(82,83), #  equation of apply attribute ApplyAttribute () -> left_expr
    		(83,81), #  left_expr -> apply_attribute ApplyAttribute ()
    		(82,84), #  equation of apply attribute ApplyAttribute () -> right_expr
    		(84,85), # right_expr --> term
    		(17,86), # apply_class EcuInstance() -> has_apply_attribute shortName ()
    		(86,87), #  has_apply_attribute shortName () -> apply_attribute shortName ()
    		(88,89), #  equation of apply attribute shortName () -> left_expr
    		(89,87), #  left_expr -> apply_attribute shortName ()
    		(88,90), #  equation of apply attribute shortName () -> right_expr
    		(91,92), #  apply attribute concat shortName () -> left has_args  
    		(92,94), #  left has_args -> term
    		(91,93), #  apply attribute concat shortName () -> right has_args  
    		(93,25), #  right has_args -> term
    		(90,91), # right_expr --> term
        	(0,2), # matchmodel -> pairedwith
        	(2,1) # pairedwith -> applyModel
        ])
        
