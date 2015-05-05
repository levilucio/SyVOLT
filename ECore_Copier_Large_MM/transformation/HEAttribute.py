from core.himesis import Himesis
import cPickle as pickle
import uuid

class HEAttribute(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule EAttribute.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HEAttribute, self).__init__(name='HEAttribute', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        # TODO Levi, need some help here because I don't know where does 
        # this value come from.
        self["mm__"] = pickle.loads("""(lp1
S'HimesisMM'
p2
a.""")
        
        self["name"] = """EAttribute"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EAttribute')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EAttributematchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EAttributeapplymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EAttributepairedwith2')
        
    	# match class EAttribute() node
    	self.add_node()
    	self.vs[3]["name"] = """"""
        self.vs[3]["classtype"] = """EAttribute"""
        self.vs[3]["mm__"] = """EAttribute"""
        self.vs[3]["cardinality"] = """+"""
        #self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# match_contains node for class EAttribute()
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        #self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'matchcontains4')
        
        
    	# apply class EAttribute() node
    	self.add_node()
    	self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EAttribute"""
        self.vs[5]["mm__"] = """EAttribute"""
        self.vs[5]["cardinality"] = """1"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply_contains node for class EAttribute()
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
    	# has match attribute iD() node
    	self.add_node()
    	self.vs[29]["mm__"] = """hasAttribute_S"""
        #self.vs[29]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# match attribute iD() node
    	self.add_node()
    	self.vs[30]["name"] = """iD"""
        self.vs[30]["mm__"] = """Attribute"""
        self.vs[30]["Type"] = """'String'"""
        #self.vs[30]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        
        
    	# has apply attribute name() node
    	self.add_node()
    	self.vs[31]["mm__"] = """hasAttribute_T"""
        #self.vs[31]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute name() node
    	self.add_node()
    	self.vs[32]["name"] = """name"""
        self.vs[32]["mm__"] = """Attribute"""
        self.vs[32]["Type"] = """'String'"""
        #self.vs[32]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation name() node
    	self.add_node()
    	self.vs[33]["name"] = """eq_"""
        self.vs[33]["mm__"] = """Equation"""
        #self.vs[33]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr name() node
    	self.add_node()
    	self.vs[34]["mm__"] = """leftExpr"""
        #self.vs[34]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr name() node
    	self.add_node()
    	self.vs[35]["mm__"] = """rightExpr"""
        #self.vs[35]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# has apply attribute ordered() node
    	self.add_node()
    	self.vs[36]["mm__"] = """hasAttribute_T"""
        #self.vs[36]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute ordered() node
    	self.add_node()
    	self.vs[37]["name"] = """ordered"""
        self.vs[37]["mm__"] = """Attribute"""
        self.vs[37]["Type"] = """'String'"""
        #self.vs[37]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation ordered() node
    	self.add_node()
    	self.vs[38]["name"] = """eq_"""
        self.vs[38]["mm__"] = """Equation"""
        #self.vs[38]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr ordered() node
    	self.add_node()
    	self.vs[39]["mm__"] = """leftExpr"""
        #self.vs[39]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr ordered() node
    	self.add_node()
    	self.vs[40]["mm__"] = """rightExpr"""
        #self.vs[40]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# has apply attribute unique() node
    	self.add_node()
    	self.vs[41]["mm__"] = """hasAttribute_T"""
        #self.vs[41]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute unique() node
    	self.add_node()
    	self.vs[42]["name"] = """unique"""
        self.vs[42]["mm__"] = """Attribute"""
        self.vs[42]["Type"] = """'String'"""
        #self.vs[42]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation unique() node
    	self.add_node()
    	self.vs[43]["name"] = """eq_"""
        self.vs[43]["mm__"] = """Equation"""
        #self.vs[43]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr unique() node
    	self.add_node()
    	self.vs[44]["mm__"] = """leftExpr"""
        #self.vs[44]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr unique() node
    	self.add_node()
    	self.vs[45]["mm__"] = """rightExpr"""
        #self.vs[45]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# has apply attribute lowerBound() node
    	self.add_node()
    	self.vs[46]["mm__"] = """hasAttribute_T"""
        #self.vs[46]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute lowerBound() node
    	self.add_node()
    	self.vs[47]["name"] = """lowerBound"""
        self.vs[47]["mm__"] = """Attribute"""
        self.vs[47]["Type"] = """'String'"""
        #self.vs[47]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation lowerBound() node
    	self.add_node()
    	self.vs[48]["name"] = """eq_"""
        self.vs[48]["mm__"] = """Equation"""
        #self.vs[48]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr lowerBound() node
    	self.add_node()
    	self.vs[49]["mm__"] = """leftExpr"""
        #self.vs[49]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr lowerBound() node
    	self.add_node()
    	self.vs[50]["mm__"] = """rightExpr"""
        #self.vs[50]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# has apply attribute upperBound() node
    	self.add_node()
    	self.vs[51]["mm__"] = """hasAttribute_T"""
        #self.vs[51]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute upperBound() node
    	self.add_node()
    	self.vs[52]["name"] = """upperBound"""
        self.vs[52]["mm__"] = """Attribute"""
        self.vs[52]["Type"] = """'String'"""
        #self.vs[52]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation upperBound() node
    	self.add_node()
    	self.vs[53]["name"] = """eq_"""
        self.vs[53]["mm__"] = """Equation"""
        #self.vs[53]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr upperBound() node
    	self.add_node()
    	self.vs[54]["mm__"] = """leftExpr"""
        #self.vs[54]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr upperBound() node
    	self.add_node()
    	self.vs[55]["mm__"] = """rightExpr"""
        #self.vs[55]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# has apply attribute changeable() node
    	self.add_node()
    	self.vs[56]["mm__"] = """hasAttribute_T"""
        #self.vs[56]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute changeable() node
    	self.add_node()
    	self.vs[57]["name"] = """changeable"""
        self.vs[57]["mm__"] = """Attribute"""
        self.vs[57]["Type"] = """'String'"""
        #self.vs[57]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation changeable() node
    	self.add_node()
    	self.vs[58]["name"] = """eq_"""
        self.vs[58]["mm__"] = """Equation"""
        #self.vs[58]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr changeable() node
    	self.add_node()
    	self.vs[59]["mm__"] = """leftExpr"""
        #self.vs[59]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr changeable() node
    	self.add_node()
    	self.vs[60]["mm__"] = """rightExpr"""
        #self.vs[60]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# has apply attribute volatile() node
    	self.add_node()
    	self.vs[61]["mm__"] = """hasAttribute_T"""
        #self.vs[61]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute volatile() node
    	self.add_node()
    	self.vs[62]["name"] = """volatile"""
        self.vs[62]["mm__"] = """Attribute"""
        self.vs[62]["Type"] = """'String'"""
        #self.vs[62]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation volatile() node
    	self.add_node()
    	self.vs[63]["name"] = """eq_"""
        self.vs[63]["mm__"] = """Equation"""
        #self.vs[63]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr volatile() node
    	self.add_node()
    	self.vs[64]["mm__"] = """leftExpr"""
        #self.vs[64]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr volatile() node
    	self.add_node()
    	self.vs[65]["mm__"] = """rightExpr"""
        #self.vs[65]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# has apply attribute transient() node
    	self.add_node()
    	self.vs[66]["mm__"] = """hasAttribute_T"""
        #self.vs[66]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute transient() node
    	self.add_node()
    	self.vs[67]["name"] = """transient"""
        self.vs[67]["mm__"] = """Attribute"""
        self.vs[67]["Type"] = """'String'"""
        #self.vs[67]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation transient() node
    	self.add_node()
    	self.vs[68]["name"] = """eq_"""
        self.vs[68]["mm__"] = """Equation"""
        #self.vs[68]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr transient() node
    	self.add_node()
    	self.vs[69]["mm__"] = """leftExpr"""
        #self.vs[69]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr transient() node
    	self.add_node()
    	self.vs[70]["mm__"] = """rightExpr"""
        #self.vs[70]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# has apply attribute defaultValueLiteral() node
    	self.add_node()
    	self.vs[71]["mm__"] = """hasAttribute_T"""
        #self.vs[71]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute defaultValueLiteral() node
    	self.add_node()
    	self.vs[72]["name"] = """defaultValueLiteral"""
        self.vs[72]["mm__"] = """Attribute"""
        self.vs[72]["Type"] = """'String'"""
        #self.vs[72]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation defaultValueLiteral() node
    	self.add_node()
    	self.vs[73]["name"] = """eq_"""
        self.vs[73]["mm__"] = """Equation"""
        #self.vs[73]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr defaultValueLiteral() node
    	self.add_node()
    	self.vs[74]["mm__"] = """leftExpr"""
        #self.vs[74]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr defaultValueLiteral() node
    	self.add_node()
    	self.vs[75]["mm__"] = """rightExpr"""
        #self.vs[75]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# has apply attribute unsettable() node
    	self.add_node()
    	self.vs[76]["mm__"] = """hasAttribute_T"""
        #self.vs[76]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute unsettable() node
    	self.add_node()
    	self.vs[77]["name"] = """unsettable"""
        self.vs[77]["mm__"] = """Attribute"""
        self.vs[77]["Type"] = """'String'"""
        #self.vs[77]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation unsettable() node
    	self.add_node()
    	self.vs[78]["name"] = """eq_"""
        self.vs[78]["mm__"] = """Equation"""
        #self.vs[78]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr unsettable() node
    	self.add_node()
    	self.vs[79]["mm__"] = """leftExpr"""
        #self.vs[79]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr unsettable() node
    	self.add_node()
    	self.vs[80]["mm__"] = """rightExpr"""
        #self.vs[80]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# has apply attribute derived() node
    	self.add_node()
    	self.vs[81]["mm__"] = """hasAttribute_T"""
        #self.vs[81]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute derived() node
    	self.add_node()
    	self.vs[82]["name"] = """derived"""
        self.vs[82]["mm__"] = """Attribute"""
        self.vs[82]["Type"] = """'String'"""
        #self.vs[82]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation derived() node
    	self.add_node()
    	self.vs[83]["name"] = """eq_"""
        self.vs[83]["mm__"] = """Equation"""
        #self.vs[83]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr derived() node
    	self.add_node()
    	self.vs[84]["mm__"] = """leftExpr"""
        #self.vs[84]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr derived() node
    	self.add_node()
    	self.vs[85]["mm__"] = """rightExpr"""
        #self.vs[85]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# has apply attribute iD() node
    	self.add_node()
    	self.vs[86]["mm__"] = """hasAttribute_T"""
        #self.vs[86]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute iD() node
    	self.add_node()
    	self.vs[87]["name"] = """iD"""
        self.vs[87]["mm__"] = """Attribute"""
        self.vs[87]["Type"] = """'String'"""
        #self.vs[87]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation iD() node
    	self.add_node()
    	self.vs[88]["name"] = """eq_"""
        self.vs[88]["mm__"] = """Equation"""
        #self.vs[88]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr iD() node
    	self.add_node()
    	self.vs[89]["mm__"] = """leftExpr"""
        #self.vs[89]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr iD() node
    	self.add_node()
    	self.vs[90]["mm__"] = """rightExpr"""
        #self.vs[90]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# has apply attribute ApplyAttribute() node
    	self.add_node()
    	self.vs[91]["mm__"] = """hasAttribute_T"""
        #self.vs[91]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute ApplyAttribute() node
    	self.add_node()
    	self.vs[92]["name"] = """ApplyAttribute"""
        self.vs[92]["mm__"] = """Attribute"""
        self.vs[92]["Type"] = """'String'"""
        #self.vs[92]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation ApplyAttribute() node
    	self.add_node()
    	self.vs[93]["name"] = """eq_"""
        self.vs[93]["mm__"] = """Equation"""
        #self.vs[93]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr ApplyAttribute() node
    	self.add_node()
    	self.vs[94]["mm__"] = """leftExpr"""
        #self.vs[94]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr ApplyAttribute() node
    	self.add_node()
    	self.vs[95]["mm__"] = """rightExpr"""
        #self.vs[95]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# apply attribute atom ApplyAttribute() node
    	self.add_node()
    	self.vs[96]["name"] = """solveRef"""
        self.vs[96]["mm__"] = """Constant"""
        self.vs[96]["Type"] = """'String'"""
        #self.vs[96]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom96')
        
        
        # Add the edges
        self.add_edges([
    		(0,4), # matchmodel -> match_contains
    		(4,3), # match_contains -> match_class EAttribute()
    		(1,6), # applymodel -> apply_contains
    		(6,5), # apply_contains -> apply_class EAttribute()
    		(3,7), # match_class EAttribute() -> has_match_attribute name ()
    		(7,8), #  has_match_attribute name () -> match_attribute name ()
    		(3,9), # match_class EAttribute() -> has_match_attribute ordered ()
    		(9,10), #  has_match_attribute ordered () -> match_attribute ordered ()
    		(3,11), # match_class EAttribute() -> has_match_attribute unique ()
    		(11,12), #  has_match_attribute unique () -> match_attribute unique ()
    		(3,13), # match_class EAttribute() -> has_match_attribute lowerBound ()
    		(13,14), #  has_match_attribute lowerBound () -> match_attribute lowerBound ()
    		(3,15), # match_class EAttribute() -> has_match_attribute upperBound ()
    		(15,16), #  has_match_attribute upperBound () -> match_attribute upperBound ()
    		(3,17), # match_class EAttribute() -> has_match_attribute changeable ()
    		(17,18), #  has_match_attribute changeable () -> match_attribute changeable ()
    		(3,19), # match_class EAttribute() -> has_match_attribute volatile ()
    		(19,20), #  has_match_attribute volatile () -> match_attribute volatile ()
    		(3,21), # match_class EAttribute() -> has_match_attribute transient ()
    		(21,22), #  has_match_attribute transient () -> match_attribute transient ()
    		(3,23), # match_class EAttribute() -> has_match_attribute defaultValueLiteral ()
    		(23,24), #  has_match_attribute defaultValueLiteral () -> match_attribute defaultValueLiteral ()
    		(3,25), # match_class EAttribute() -> has_match_attribute unsettable ()
    		(25,26), #  has_match_attribute unsettable () -> match_attribute unsettable ()
    		(3,27), # match_class EAttribute() -> has_match_attribute derived ()
    		(27,28), #  has_match_attribute derived () -> match_attribute derived ()
    		(3,29), # match_class EAttribute() -> has_match_attribute iD ()
    		(29,30), #  has_match_attribute iD () -> match_attribute iD ()
    		(5,31), # apply_class EAttribute() -> has_apply_attribute name ()
    		(31,32), #  has_apply_attribute name () -> apply_attribute name ()
    		(33,34), #  equation of apply attribute name () -> left_expr
    		(34,32), #  left_expr -> apply_attribute name ()
    		(33,35), #  equation of apply attribute name () -> right_expr
    		(35,8), # right_expr --> term
    		(5,36), # apply_class EAttribute() -> has_apply_attribute ordered ()
    		(36,37), #  has_apply_attribute ordered () -> apply_attribute ordered ()
    		(38,39), #  equation of apply attribute ordered () -> left_expr
    		(39,37), #  left_expr -> apply_attribute ordered ()
    		(38,40), #  equation of apply attribute ordered () -> right_expr
    		(40,10), # right_expr --> term
    		(5,41), # apply_class EAttribute() -> has_apply_attribute unique ()
    		(41,42), #  has_apply_attribute unique () -> apply_attribute unique ()
    		(43,44), #  equation of apply attribute unique () -> left_expr
    		(44,42), #  left_expr -> apply_attribute unique ()
    		(43,45), #  equation of apply attribute unique () -> right_expr
    		(45,12), # right_expr --> term
    		(5,46), # apply_class EAttribute() -> has_apply_attribute lowerBound ()
    		(46,47), #  has_apply_attribute lowerBound () -> apply_attribute lowerBound ()
    		(48,49), #  equation of apply attribute lowerBound () -> left_expr
    		(49,47), #  left_expr -> apply_attribute lowerBound ()
    		(48,50), #  equation of apply attribute lowerBound () -> right_expr
    		(50,14), # right_expr --> term
    		(5,51), # apply_class EAttribute() -> has_apply_attribute upperBound ()
    		(51,52), #  has_apply_attribute upperBound () -> apply_attribute upperBound ()
    		(53,54), #  equation of apply attribute upperBound () -> left_expr
    		(54,52), #  left_expr -> apply_attribute upperBound ()
    		(53,55), #  equation of apply attribute upperBound () -> right_expr
    		(55,16), # right_expr --> term
    		(5,56), # apply_class EAttribute() -> has_apply_attribute changeable ()
    		(56,57), #  has_apply_attribute changeable () -> apply_attribute changeable ()
    		(58,59), #  equation of apply attribute changeable () -> left_expr
    		(59,57), #  left_expr -> apply_attribute changeable ()
    		(58,60), #  equation of apply attribute changeable () -> right_expr
    		(60,18), # right_expr --> term
    		(5,61), # apply_class EAttribute() -> has_apply_attribute volatile ()
    		(61,62), #  has_apply_attribute volatile () -> apply_attribute volatile ()
    		(63,64), #  equation of apply attribute volatile () -> left_expr
    		(64,62), #  left_expr -> apply_attribute volatile ()
    		(63,65), #  equation of apply attribute volatile () -> right_expr
    		(65,20), # right_expr --> term
    		(5,66), # apply_class EAttribute() -> has_apply_attribute transient ()
    		(66,67), #  has_apply_attribute transient () -> apply_attribute transient ()
    		(68,69), #  equation of apply attribute transient () -> left_expr
    		(69,67), #  left_expr -> apply_attribute transient ()
    		(68,70), #  equation of apply attribute transient () -> right_expr
    		(70,22), # right_expr --> term
    		(5,71), # apply_class EAttribute() -> has_apply_attribute defaultValueLiteral ()
    		(71,72), #  has_apply_attribute defaultValueLiteral () -> apply_attribute defaultValueLiteral ()
    		(73,74), #  equation of apply attribute defaultValueLiteral () -> left_expr
    		(74,72), #  left_expr -> apply_attribute defaultValueLiteral ()
    		(73,75), #  equation of apply attribute defaultValueLiteral () -> right_expr
    		(75,24), # right_expr --> term
    		(5,76), # apply_class EAttribute() -> has_apply_attribute unsettable ()
    		(76,77), #  has_apply_attribute unsettable () -> apply_attribute unsettable ()
    		(78,79), #  equation of apply attribute unsettable () -> left_expr
    		(79,77), #  left_expr -> apply_attribute unsettable ()
    		(78,80), #  equation of apply attribute unsettable () -> right_expr
    		(80,26), # right_expr --> term
    		(5,81), # apply_class EAttribute() -> has_apply_attribute derived ()
    		(81,82), #  has_apply_attribute derived () -> apply_attribute derived ()
    		(83,84), #  equation of apply attribute derived () -> left_expr
    		(84,82), #  left_expr -> apply_attribute derived ()
    		(83,85), #  equation of apply attribute derived () -> right_expr
    		(85,28), # right_expr --> term
    		(5,86), # apply_class EAttribute() -> has_apply_attribute iD ()
    		(86,87), #  has_apply_attribute iD () -> apply_attribute iD ()
    		(88,89), #  equation of apply attribute iD () -> left_expr
    		(89,87), #  left_expr -> apply_attribute iD ()
    		(88,90), #  equation of apply attribute iD () -> right_expr
    		(90,30), # right_expr --> term
    		(5,91), # apply_class EAttribute() -> has_apply_attribute ApplyAttribute ()
    		(91,92), #  has_apply_attribute ApplyAttribute () -> apply_attribute ApplyAttribute ()
    		(93,94), #  equation of apply attribute ApplyAttribute () -> left_expr
    		(94,92), #  left_expr -> apply_attribute ApplyAttribute ()
    		(93,95), #  equation of apply attribute ApplyAttribute () -> right_expr
    		(95,96), # right_expr --> term
        	(0,2), # matchmodel -> pairedwith
        	(2,1) # pairedwith -> applyModel
        ])
        
