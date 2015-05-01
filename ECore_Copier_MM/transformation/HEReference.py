from core.himesis import Himesis
import cPickle as pickle
import uuid

class HEReference(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule EReference.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HEReference, self).__init__(name='HEReference', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        # TODO Levi, need some help here because I don't know where does 
        # this value come from.
        self["mm__"] = pickle.loads("""(lp1
S'HimesisMM'
p2
a.""")
        
        self["name"] = """EReference"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EReference')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EReferencematchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EReferenceapplymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EReferencepairedwith2')
        
    	# match class EReference() node
    	self.add_node()
    	self.vs[3]["name"] = """"""
        self.vs[3]["classtype"] = """EReference"""
        self.vs[3]["mm__"] = """EReference"""
        self.vs[3]["cardinality"] = """+"""
        #self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# match_contains node for class EReference()
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        #self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'matchcontains4')
        
        
    	# apply class EReference() node
    	self.add_node()
    	self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EReference"""
        self.vs[5]["mm__"] = """EReference"""
        self.vs[5]["cardinality"] = """1"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply_contains node for class EReference()
        self.add_node()
        self.vs[6]["mm__"] = """apply_contains"""
        #self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains6')
        
        
        
        
        
        
    	# has match attribute name() node
    	self.add_node()
    	self.vs[7]["mm__"] = """hasAttribute_S"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# match attribute name() node
    	self.add_node()
    	self.vs[8]["name"] = """name"""
        self.vs[8]["mm__"] = """Attribute"""
        self.vs[8]["Type"] = """'String'"""
        #self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# has match attribute ordered() node
    	self.add_node()
    	self.vs[9]["mm__"] = """hasAttribute_S"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# match attribute ordered() node
    	self.add_node()
    	self.vs[10]["name"] = """ordered"""
        self.vs[10]["mm__"] = """Attribute"""
        self.vs[10]["Type"] = """'String'"""
        #self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# has match attribute unique() node
    	self.add_node()
    	self.vs[11]["mm__"] = """hasAttribute_S"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# match attribute unique() node
    	self.add_node()
    	self.vs[12]["name"] = """unique"""
        self.vs[12]["mm__"] = """Attribute"""
        self.vs[12]["Type"] = """'String'"""
        #self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# has match attribute lowerBound() node
    	self.add_node()
    	self.vs[13]["mm__"] = """hasAttribute_S"""
        #self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# match attribute lowerBound() node
    	self.add_node()
    	self.vs[14]["name"] = """lowerBound"""
        self.vs[14]["mm__"] = """Attribute"""
        self.vs[14]["Type"] = """'String'"""
        #self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# has match attribute upperBound() node
    	self.add_node()
    	self.vs[15]["mm__"] = """hasAttribute_S"""
        #self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# match attribute upperBound() node
    	self.add_node()
    	self.vs[16]["name"] = """upperBound"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["Type"] = """'String'"""
        #self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# has match attribute changeable() node
    	self.add_node()
    	self.vs[17]["mm__"] = """hasAttribute_S"""
        #self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# match attribute changeable() node
    	self.add_node()
    	self.vs[18]["name"] = """changeable"""
        self.vs[18]["mm__"] = """Attribute"""
        self.vs[18]["Type"] = """'String'"""
        #self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# has match attribute volatile() node
    	self.add_node()
    	self.vs[19]["mm__"] = """hasAttribute_S"""
        #self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# match attribute volatile() node
    	self.add_node()
    	self.vs[20]["name"] = """volatile"""
        self.vs[20]["mm__"] = """Attribute"""
        self.vs[20]["Type"] = """'String'"""
        #self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# has match attribute transient() node
    	self.add_node()
    	self.vs[21]["mm__"] = """hasAttribute_S"""
        #self.vs[21]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# match attribute transient() node
    	self.add_node()
    	self.vs[22]["name"] = """transient"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["Type"] = """'String'"""
        #self.vs[22]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# has match attribute defaultValueLiteral() node
    	self.add_node()
    	self.vs[23]["mm__"] = """hasAttribute_S"""
        #self.vs[23]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# match attribute defaultValueLiteral() node
    	self.add_node()
    	self.vs[24]["name"] = """defaultValueLiteral"""
        self.vs[24]["mm__"] = """Attribute"""
        self.vs[24]["Type"] = """'String'"""
        #self.vs[24]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# has match attribute unsettable() node
    	self.add_node()
    	self.vs[25]["mm__"] = """hasAttribute_S"""
        #self.vs[25]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# match attribute unsettable() node
    	self.add_node()
    	self.vs[26]["name"] = """unsettable"""
        self.vs[26]["mm__"] = """Attribute"""
        self.vs[26]["Type"] = """'String'"""
        #self.vs[26]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# has match attribute derived() node
    	self.add_node()
    	self.vs[27]["mm__"] = """hasAttribute_S"""
        #self.vs[27]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# match attribute derived() node
    	self.add_node()
    	self.vs[28]["name"] = """derived"""
        self.vs[28]["mm__"] = """Attribute"""
        self.vs[28]["Type"] = """'String'"""
        #self.vs[28]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# has match attribute containment() node
    	self.add_node()
    	self.vs[29]["mm__"] = """hasAttribute_S"""
        #self.vs[29]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# match attribute containment() node
    	self.add_node()
    	self.vs[30]["name"] = """containment"""
        self.vs[30]["mm__"] = """Attribute"""
        self.vs[30]["Type"] = """'String'"""
        #self.vs[30]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# has match attribute resolveProxies() node
    	self.add_node()
    	self.vs[31]["mm__"] = """hasAttribute_S"""
        #self.vs[31]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# match attribute resolveProxies() node
    	self.add_node()
    	self.vs[32]["name"] = """resolveProxies"""
        self.vs[32]["mm__"] = """Attribute"""
        self.vs[32]["Type"] = """'String'"""
        #self.vs[32]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        
        
    	# has apply attribute name() node
    	self.add_node()
    	self.vs[33]["mm__"] = """hasAttribute_T"""
        #self.vs[33]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute name() node
    	self.add_node()
    	self.vs[34]["name"] = """name"""
        self.vs[34]["mm__"] = """Attribute"""
        self.vs[34]["Type"] = """'String'"""
        #self.vs[34]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation name() node
    	self.add_node()
    	self.vs[35]["name"] = """eq_"""
        self.vs[35]["mm__"] = """Equation"""
        #self.vs[35]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr name() node
    	self.add_node()
    	self.vs[36]["mm__"] = """leftExpr"""
        #self.vs[36]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr name() node
    	self.add_node()
    	self.vs[37]["mm__"] = """rightExpr"""
        #self.vs[37]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# has apply attribute ordered() node
    	self.add_node()
    	self.vs[38]["mm__"] = """hasAttribute_T"""
        #self.vs[38]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute ordered() node
    	self.add_node()
    	self.vs[39]["name"] = """ordered"""
        self.vs[39]["mm__"] = """Attribute"""
        self.vs[39]["Type"] = """'String'"""
        #self.vs[39]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation ordered() node
    	self.add_node()
    	self.vs[40]["name"] = """eq_"""
        self.vs[40]["mm__"] = """Equation"""
        #self.vs[40]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr ordered() node
    	self.add_node()
    	self.vs[41]["mm__"] = """leftExpr"""
        #self.vs[41]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr ordered() node
    	self.add_node()
    	self.vs[42]["mm__"] = """rightExpr"""
        #self.vs[42]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# has apply attribute unique() node
    	self.add_node()
    	self.vs[43]["mm__"] = """hasAttribute_T"""
        #self.vs[43]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute unique() node
    	self.add_node()
    	self.vs[44]["name"] = """unique"""
        self.vs[44]["mm__"] = """Attribute"""
        self.vs[44]["Type"] = """'String'"""
        #self.vs[44]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation unique() node
    	self.add_node()
    	self.vs[45]["name"] = """eq_"""
        self.vs[45]["mm__"] = """Equation"""
        #self.vs[45]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr unique() node
    	self.add_node()
    	self.vs[46]["mm__"] = """leftExpr"""
        #self.vs[46]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr unique() node
    	self.add_node()
    	self.vs[47]["mm__"] = """rightExpr"""
        #self.vs[47]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# has apply attribute lowerBound() node
    	self.add_node()
    	self.vs[48]["mm__"] = """hasAttribute_T"""
        #self.vs[48]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute lowerBound() node
    	self.add_node()
    	self.vs[49]["name"] = """lowerBound"""
        self.vs[49]["mm__"] = """Attribute"""
        self.vs[49]["Type"] = """'String'"""
        #self.vs[49]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation lowerBound() node
    	self.add_node()
    	self.vs[50]["name"] = """eq_"""
        self.vs[50]["mm__"] = """Equation"""
        #self.vs[50]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr lowerBound() node
    	self.add_node()
    	self.vs[51]["mm__"] = """leftExpr"""
        #self.vs[51]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr lowerBound() node
    	self.add_node()
    	self.vs[52]["mm__"] = """rightExpr"""
        #self.vs[52]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# has apply attribute upperBound() node
    	self.add_node()
    	self.vs[53]["mm__"] = """hasAttribute_T"""
        #self.vs[53]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute upperBound() node
    	self.add_node()
    	self.vs[54]["name"] = """upperBound"""
        self.vs[54]["mm__"] = """Attribute"""
        self.vs[54]["Type"] = """'String'"""
        #self.vs[54]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation upperBound() node
    	self.add_node()
    	self.vs[55]["name"] = """eq_"""
        self.vs[55]["mm__"] = """Equation"""
        #self.vs[55]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr upperBound() node
    	self.add_node()
    	self.vs[56]["mm__"] = """leftExpr"""
        #self.vs[56]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr upperBound() node
    	self.add_node()
    	self.vs[57]["mm__"] = """rightExpr"""
        #self.vs[57]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# has apply attribute changeable() node
    	self.add_node()
    	self.vs[58]["mm__"] = """hasAttribute_T"""
        #self.vs[58]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute changeable() node
    	self.add_node()
    	self.vs[59]["name"] = """changeable"""
        self.vs[59]["mm__"] = """Attribute"""
        self.vs[59]["Type"] = """'String'"""
        #self.vs[59]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation changeable() node
    	self.add_node()
    	self.vs[60]["name"] = """eq_"""
        self.vs[60]["mm__"] = """Equation"""
        #self.vs[60]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr changeable() node
    	self.add_node()
    	self.vs[61]["mm__"] = """leftExpr"""
        #self.vs[61]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr changeable() node
    	self.add_node()
    	self.vs[62]["mm__"] = """rightExpr"""
        #self.vs[62]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# has apply attribute volatile() node
    	self.add_node()
    	self.vs[63]["mm__"] = """hasAttribute_T"""
        #self.vs[63]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute volatile() node
    	self.add_node()
    	self.vs[64]["name"] = """volatile"""
        self.vs[64]["mm__"] = """Attribute"""
        self.vs[64]["Type"] = """'String'"""
        #self.vs[64]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation volatile() node
    	self.add_node()
    	self.vs[65]["name"] = """eq_"""
        self.vs[65]["mm__"] = """Equation"""
        #self.vs[65]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr volatile() node
    	self.add_node()
    	self.vs[66]["mm__"] = """leftExpr"""
        #self.vs[66]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr volatile() node
    	self.add_node()
    	self.vs[67]["mm__"] = """rightExpr"""
        #self.vs[67]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# has apply attribute transient() node
    	self.add_node()
    	self.vs[68]["mm__"] = """hasAttribute_T"""
        #self.vs[68]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute transient() node
    	self.add_node()
    	self.vs[69]["name"] = """transient"""
        self.vs[69]["mm__"] = """Attribute"""
        self.vs[69]["Type"] = """'String'"""
        #self.vs[69]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation transient() node
    	self.add_node()
    	self.vs[70]["name"] = """eq_"""
        self.vs[70]["mm__"] = """Equation"""
        #self.vs[70]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr transient() node
    	self.add_node()
    	self.vs[71]["mm__"] = """leftExpr"""
        #self.vs[71]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr transient() node
    	self.add_node()
    	self.vs[72]["mm__"] = """rightExpr"""
        #self.vs[72]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# has apply attribute defaultValueLiteral() node
    	self.add_node()
    	self.vs[73]["mm__"] = """hasAttribute_T"""
        #self.vs[73]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute defaultValueLiteral() node
    	self.add_node()
    	self.vs[74]["name"] = """defaultValueLiteral"""
        self.vs[74]["mm__"] = """Attribute"""
        self.vs[74]["Type"] = """'String'"""
        #self.vs[74]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation defaultValueLiteral() node
    	self.add_node()
    	self.vs[75]["name"] = """eq_"""
        self.vs[75]["mm__"] = """Equation"""
        #self.vs[75]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr defaultValueLiteral() node
    	self.add_node()
    	self.vs[76]["mm__"] = """leftExpr"""
        #self.vs[76]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr defaultValueLiteral() node
    	self.add_node()
    	self.vs[77]["mm__"] = """rightExpr"""
        #self.vs[77]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# has apply attribute unsettable() node
    	self.add_node()
    	self.vs[78]["mm__"] = """hasAttribute_T"""
        #self.vs[78]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute unsettable() node
    	self.add_node()
    	self.vs[79]["name"] = """unsettable"""
        self.vs[79]["mm__"] = """Attribute"""
        self.vs[79]["Type"] = """'String'"""
        #self.vs[79]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation unsettable() node
    	self.add_node()
    	self.vs[80]["name"] = """eq_"""
        self.vs[80]["mm__"] = """Equation"""
        #self.vs[80]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr unsettable() node
    	self.add_node()
    	self.vs[81]["mm__"] = """leftExpr"""
        #self.vs[81]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr unsettable() node
    	self.add_node()
    	self.vs[82]["mm__"] = """rightExpr"""
        #self.vs[82]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# has apply attribute derived() node
    	self.add_node()
    	self.vs[83]["mm__"] = """hasAttribute_T"""
        #self.vs[83]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute derived() node
    	self.add_node()
    	self.vs[84]["name"] = """derived"""
        self.vs[84]["mm__"] = """Attribute"""
        self.vs[84]["Type"] = """'String'"""
        #self.vs[84]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation derived() node
    	self.add_node()
    	self.vs[85]["name"] = """eq_"""
        self.vs[85]["mm__"] = """Equation"""
        #self.vs[85]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr derived() node
    	self.add_node()
    	self.vs[86]["mm__"] = """leftExpr"""
        #self.vs[86]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr derived() node
    	self.add_node()
    	self.vs[87]["mm__"] = """rightExpr"""
        #self.vs[87]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# has apply attribute containment() node
    	self.add_node()
    	self.vs[88]["mm__"] = """hasAttribute_T"""
        #self.vs[88]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute containment() node
    	self.add_node()
    	self.vs[89]["name"] = """containment"""
        self.vs[89]["mm__"] = """Attribute"""
        self.vs[89]["Type"] = """'String'"""
        #self.vs[89]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation containment() node
    	self.add_node()
    	self.vs[90]["name"] = """eq_"""
        self.vs[90]["mm__"] = """Equation"""
        #self.vs[90]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr containment() node
    	self.add_node()
    	self.vs[91]["mm__"] = """leftExpr"""
        #self.vs[91]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr containment() node
    	self.add_node()
    	self.vs[92]["mm__"] = """rightExpr"""
        #self.vs[92]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# has apply attribute resolveProxies() node
    	self.add_node()
    	self.vs[93]["mm__"] = """hasAttribute_T"""
        #self.vs[93]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute resolveProxies() node
    	self.add_node()
    	self.vs[94]["name"] = """resolveProxies"""
        self.vs[94]["mm__"] = """Attribute"""
        self.vs[94]["Type"] = """'String'"""
        #self.vs[94]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation resolveProxies() node
    	self.add_node()
    	self.vs[95]["name"] = """eq_"""
        self.vs[95]["mm__"] = """Equation"""
        #self.vs[95]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr resolveProxies() node
    	self.add_node()
    	self.vs[96]["mm__"] = """leftExpr"""
        #self.vs[96]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr resolveProxies() node
    	self.add_node()
    	self.vs[97]["mm__"] = """rightExpr"""
        #self.vs[97]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# has apply attribute ApplyAttribute() node
    	self.add_node()
    	self.vs[98]["mm__"] = """hasAttribute_T"""
        #self.vs[98]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute ApplyAttribute() node
    	self.add_node()
    	self.vs[99]["name"] = """ApplyAttribute"""
        self.vs[99]["mm__"] = """Attribute"""
        self.vs[99]["Type"] = """'String'"""
        #self.vs[99]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation ApplyAttribute() node
    	self.add_node()
    	self.vs[100]["name"] = """eq_"""
        self.vs[100]["mm__"] = """Equation"""
        #self.vs[100]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr ApplyAttribute() node
    	self.add_node()
    	self.vs[101]["mm__"] = """leftExpr"""
        #self.vs[101]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr ApplyAttribute() node
    	self.add_node()
    	self.vs[102]["mm__"] = """rightExpr"""
        #self.vs[102]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# apply attribute atom ApplyAttribute() node
    	self.add_node()
    	self.vs[103]["name"] = """solveRef"""
        self.vs[103]["mm__"] = """Constant"""
        self.vs[103]["Type"] = """'String'"""
        #self.vs[103]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom103')
        
        
        # Add the edges
        self.add_edges([
    		(0,4), # matchmodel -> match_contains
    		(4,3), # match_contains -> match_class EReference()
    		(1,6), # applymodel -> apply_contains
    		(6,5), # apply_contains -> apply_class EReference()
    		(3,7), # match_class EReference() -> has_match_attribute name ()
    		(7,8), #  has_match_attribute name () -> match_attribute name ()
    		(3,9), # match_class EReference() -> has_match_attribute ordered ()
    		(9,10), #  has_match_attribute ordered () -> match_attribute ordered ()
    		(3,11), # match_class EReference() -> has_match_attribute unique ()
    		(11,12), #  has_match_attribute unique () -> match_attribute unique ()
    		(3,13), # match_class EReference() -> has_match_attribute lowerBound ()
    		(13,14), #  has_match_attribute lowerBound () -> match_attribute lowerBound ()
    		(3,15), # match_class EReference() -> has_match_attribute upperBound ()
    		(15,16), #  has_match_attribute upperBound () -> match_attribute upperBound ()
    		(3,17), # match_class EReference() -> has_match_attribute changeable ()
    		(17,18), #  has_match_attribute changeable () -> match_attribute changeable ()
    		(3,19), # match_class EReference() -> has_match_attribute volatile ()
    		(19,20), #  has_match_attribute volatile () -> match_attribute volatile ()
    		(3,21), # match_class EReference() -> has_match_attribute transient ()
    		(21,22), #  has_match_attribute transient () -> match_attribute transient ()
    		(3,23), # match_class EReference() -> has_match_attribute defaultValueLiteral ()
    		(23,24), #  has_match_attribute defaultValueLiteral () -> match_attribute defaultValueLiteral ()
    		(3,25), # match_class EReference() -> has_match_attribute unsettable ()
    		(25,26), #  has_match_attribute unsettable () -> match_attribute unsettable ()
    		(3,27), # match_class EReference() -> has_match_attribute derived ()
    		(27,28), #  has_match_attribute derived () -> match_attribute derived ()
    		(3,29), # match_class EReference() -> has_match_attribute containment ()
    		(29,30), #  has_match_attribute containment () -> match_attribute containment ()
    		(3,31), # match_class EReference() -> has_match_attribute resolveProxies ()
    		(31,32), #  has_match_attribute resolveProxies () -> match_attribute resolveProxies ()
    		(5,33), # apply_class EReference() -> has_apply_attribute name ()
    		(33,34), #  has_apply_attribute name () -> apply_attribute name ()
    		(35,36), #  equation of apply attribute name () -> left_expr
    		(36,34), #  left_expr -> apply_attribute name ()
    		(35,37), #  equation of apply attribute name () -> right_expr
    		(37,8), # right_expr --> term
    		(5,38), # apply_class EReference() -> has_apply_attribute ordered ()
    		(38,39), #  has_apply_attribute ordered () -> apply_attribute ordered ()
    		(40,41), #  equation of apply attribute ordered () -> left_expr
    		(41,39), #  left_expr -> apply_attribute ordered ()
    		(40,42), #  equation of apply attribute ordered () -> right_expr
    		(42,10), # right_expr --> term
    		(5,43), # apply_class EReference() -> has_apply_attribute unique ()
    		(43,44), #  has_apply_attribute unique () -> apply_attribute unique ()
    		(45,46), #  equation of apply attribute unique () -> left_expr
    		(46,44), #  left_expr -> apply_attribute unique ()
    		(45,47), #  equation of apply attribute unique () -> right_expr
    		(47,12), # right_expr --> term
    		(5,48), # apply_class EReference() -> has_apply_attribute lowerBound ()
    		(48,49), #  has_apply_attribute lowerBound () -> apply_attribute lowerBound ()
    		(50,51), #  equation of apply attribute lowerBound () -> left_expr
    		(51,49), #  left_expr -> apply_attribute lowerBound ()
    		(50,52), #  equation of apply attribute lowerBound () -> right_expr
    		(52,14), # right_expr --> term
    		(5,53), # apply_class EReference() -> has_apply_attribute upperBound ()
    		(53,54), #  has_apply_attribute upperBound () -> apply_attribute upperBound ()
    		(55,56), #  equation of apply attribute upperBound () -> left_expr
    		(56,54), #  left_expr -> apply_attribute upperBound ()
    		(55,57), #  equation of apply attribute upperBound () -> right_expr
    		(57,16), # right_expr --> term
    		(5,58), # apply_class EReference() -> has_apply_attribute changeable ()
    		(58,59), #  has_apply_attribute changeable () -> apply_attribute changeable ()
    		(60,61), #  equation of apply attribute changeable () -> left_expr
    		(61,59), #  left_expr -> apply_attribute changeable ()
    		(60,62), #  equation of apply attribute changeable () -> right_expr
    		(62,18), # right_expr --> term
    		(5,63), # apply_class EReference() -> has_apply_attribute volatile ()
    		(63,64), #  has_apply_attribute volatile () -> apply_attribute volatile ()
    		(65,66), #  equation of apply attribute volatile () -> left_expr
    		(66,64), #  left_expr -> apply_attribute volatile ()
    		(65,67), #  equation of apply attribute volatile () -> right_expr
    		(67,20), # right_expr --> term
    		(5,68), # apply_class EReference() -> has_apply_attribute transient ()
    		(68,69), #  has_apply_attribute transient () -> apply_attribute transient ()
    		(70,71), #  equation of apply attribute transient () -> left_expr
    		(71,69), #  left_expr -> apply_attribute transient ()
    		(70,72), #  equation of apply attribute transient () -> right_expr
    		(72,22), # right_expr --> term
    		(5,73), # apply_class EReference() -> has_apply_attribute defaultValueLiteral ()
    		(73,74), #  has_apply_attribute defaultValueLiteral () -> apply_attribute defaultValueLiteral ()
    		(75,76), #  equation of apply attribute defaultValueLiteral () -> left_expr
    		(76,74), #  left_expr -> apply_attribute defaultValueLiteral ()
    		(75,77), #  equation of apply attribute defaultValueLiteral () -> right_expr
    		(77,24), # right_expr --> term
    		(5,78), # apply_class EReference() -> has_apply_attribute unsettable ()
    		(78,79), #  has_apply_attribute unsettable () -> apply_attribute unsettable ()
    		(80,81), #  equation of apply attribute unsettable () -> left_expr
    		(81,79), #  left_expr -> apply_attribute unsettable ()
    		(80,82), #  equation of apply attribute unsettable () -> right_expr
    		(82,26), # right_expr --> term
    		(5,83), # apply_class EReference() -> has_apply_attribute derived ()
    		(83,84), #  has_apply_attribute derived () -> apply_attribute derived ()
    		(85,86), #  equation of apply attribute derived () -> left_expr
    		(86,84), #  left_expr -> apply_attribute derived ()
    		(85,87), #  equation of apply attribute derived () -> right_expr
    		(87,28), # right_expr --> term
    		(5,88), # apply_class EReference() -> has_apply_attribute containment ()
    		(88,89), #  has_apply_attribute containment () -> apply_attribute containment ()
    		(90,91), #  equation of apply attribute containment () -> left_expr
    		(91,89), #  left_expr -> apply_attribute containment ()
    		(90,92), #  equation of apply attribute containment () -> right_expr
    		(92,30), # right_expr --> term
    		(5,93), # apply_class EReference() -> has_apply_attribute resolveProxies ()
    		(93,94), #  has_apply_attribute resolveProxies () -> apply_attribute resolveProxies ()
    		(95,96), #  equation of apply attribute resolveProxies () -> left_expr
    		(96,94), #  left_expr -> apply_attribute resolveProxies ()
    		(95,97), #  equation of apply attribute resolveProxies () -> right_expr
    		(97,32), # right_expr --> term
    		(5,98), # apply_class EReference() -> has_apply_attribute ApplyAttribute ()
    		(98,99), #  has_apply_attribute ApplyAttribute () -> apply_attribute ApplyAttribute ()
    		(100,101), #  equation of apply attribute ApplyAttribute () -> left_expr
    		(101,99), #  left_expr -> apply_attribute ApplyAttribute ()
    		(100,102), #  equation of apply attribute ApplyAttribute () -> right_expr
    		(102,103), # right_expr --> term
        	(0,2), # matchmodel -> pairedwith
        	(2,1) # pairedwith -> applyModel
        ])
        
