from core.himesis import Himesis
import cPickle as pickle
import uuid

class HEParameter(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule EParameter.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HEParameter, self).__init__(name='HEParameter', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        # TODO Levi, need some help here because I don't know where does 
        # this value come from.
        self["mm__"] = pickle.loads("""(lp1
S'HimesisMM'
p2
a.""")
        
        self["name"] = """EParameter"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EParameter')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EParametermatchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EParameterapplymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EParameterpairedwith2')
        
    	# match class EParameter() node
    	self.add_node()
    	self.vs[3]["name"] = """"""
        self.vs[3]["classtype"] = """EParameter"""
        self.vs[3]["mm__"] = """EParameter"""
        self.vs[3]["cardinality"] = """+"""
        #self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# match_contains node for class EParameter()
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        #self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'matchcontains4')
        
        
    	# apply class EParameter() node
    	self.add_node()
    	self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EParameter"""
        self.vs[5]["mm__"] = """EParameter"""
        self.vs[5]["cardinality"] = """1"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply_contains node for class EParameter()
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
        
        
    	# has apply attribute name() node
    	self.add_node()
    	self.vs[17]["mm__"] = """hasAttribute_T"""
        #self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute name() node
    	self.add_node()
    	self.vs[18]["name"] = """name"""
        self.vs[18]["mm__"] = """Attribute"""
        self.vs[18]["Type"] = """'String'"""
        #self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation name() node
    	self.add_node()
    	self.vs[19]["name"] = """eq_"""
        self.vs[19]["mm__"] = """Equation"""
        #self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr name() node
    	self.add_node()
    	self.vs[20]["mm__"] = """leftExpr"""
        #self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr name() node
    	self.add_node()
    	self.vs[21]["mm__"] = """rightExpr"""
        #self.vs[21]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# has apply attribute ordered() node
    	self.add_node()
    	self.vs[22]["mm__"] = """hasAttribute_T"""
        #self.vs[22]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute ordered() node
    	self.add_node()
    	self.vs[23]["name"] = """ordered"""
        self.vs[23]["mm__"] = """Attribute"""
        self.vs[23]["Type"] = """'String'"""
        #self.vs[23]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation ordered() node
    	self.add_node()
    	self.vs[24]["name"] = """eq_"""
        self.vs[24]["mm__"] = """Equation"""
        #self.vs[24]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr ordered() node
    	self.add_node()
    	self.vs[25]["mm__"] = """leftExpr"""
        #self.vs[25]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr ordered() node
    	self.add_node()
    	self.vs[26]["mm__"] = """rightExpr"""
        #self.vs[26]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# has apply attribute unique() node
    	self.add_node()
    	self.vs[27]["mm__"] = """hasAttribute_T"""
        #self.vs[27]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute unique() node
    	self.add_node()
    	self.vs[28]["name"] = """unique"""
        self.vs[28]["mm__"] = """Attribute"""
        self.vs[28]["Type"] = """'String'"""
        #self.vs[28]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation unique() node
    	self.add_node()
    	self.vs[29]["name"] = """eq_"""
        self.vs[29]["mm__"] = """Equation"""
        #self.vs[29]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr unique() node
    	self.add_node()
    	self.vs[30]["mm__"] = """leftExpr"""
        #self.vs[30]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr unique() node
    	self.add_node()
    	self.vs[31]["mm__"] = """rightExpr"""
        #self.vs[31]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# has apply attribute lowerBound() node
    	self.add_node()
    	self.vs[32]["mm__"] = """hasAttribute_T"""
        #self.vs[32]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute lowerBound() node
    	self.add_node()
    	self.vs[33]["name"] = """lowerBound"""
        self.vs[33]["mm__"] = """Attribute"""
        self.vs[33]["Type"] = """'String'"""
        #self.vs[33]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation lowerBound() node
    	self.add_node()
    	self.vs[34]["name"] = """eq_"""
        self.vs[34]["mm__"] = """Equation"""
        #self.vs[34]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr lowerBound() node
    	self.add_node()
    	self.vs[35]["mm__"] = """leftExpr"""
        #self.vs[35]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr lowerBound() node
    	self.add_node()
    	self.vs[36]["mm__"] = """rightExpr"""
        #self.vs[36]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# has apply attribute upperBound() node
    	self.add_node()
    	self.vs[37]["mm__"] = """hasAttribute_T"""
        #self.vs[37]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute upperBound() node
    	self.add_node()
    	self.vs[38]["name"] = """upperBound"""
        self.vs[38]["mm__"] = """Attribute"""
        self.vs[38]["Type"] = """'String'"""
        #self.vs[38]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation upperBound() node
    	self.add_node()
    	self.vs[39]["name"] = """eq_"""
        self.vs[39]["mm__"] = """Equation"""
        #self.vs[39]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr upperBound() node
    	self.add_node()
    	self.vs[40]["mm__"] = """leftExpr"""
        #self.vs[40]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr upperBound() node
    	self.add_node()
    	self.vs[41]["mm__"] = """rightExpr"""
        #self.vs[41]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# has apply attribute ApplyAttribute() node
    	self.add_node()
    	self.vs[42]["mm__"] = """hasAttribute_T"""
        #self.vs[42]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute ApplyAttribute() node
    	self.add_node()
    	self.vs[43]["name"] = """ApplyAttribute"""
        self.vs[43]["mm__"] = """Attribute"""
        self.vs[43]["Type"] = """'String'"""
        #self.vs[43]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation ApplyAttribute() node
    	self.add_node()
    	self.vs[44]["name"] = """eq_"""
        self.vs[44]["mm__"] = """Equation"""
        #self.vs[44]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr ApplyAttribute() node
    	self.add_node()
    	self.vs[45]["mm__"] = """leftExpr"""
        #self.vs[45]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr ApplyAttribute() node
    	self.add_node()
    	self.vs[46]["mm__"] = """rightExpr"""
        #self.vs[46]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# apply attribute atom ApplyAttribute() node
    	self.add_node()
    	self.vs[47]["name"] = """solveRef"""
        self.vs[47]["mm__"] = """Constant"""
        self.vs[47]["Type"] = """'String'"""
        #self.vs[47]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom47')
        
        
        # Add the edges
        self.add_edges([
    		(0,4), # matchmodel -> match_contains
    		(4,3), # match_contains -> match_class EParameter()
    		(1,6), # applymodel -> apply_contains
    		(6,5), # apply_contains -> apply_class EParameter()
    		(3,7), # match_class EParameter() -> has_match_attribute name ()
    		(7,8), #  has_match_attribute name () -> match_attribute name ()
    		(3,9), # match_class EParameter() -> has_match_attribute ordered ()
    		(9,10), #  has_match_attribute ordered () -> match_attribute ordered ()
    		(3,11), # match_class EParameter() -> has_match_attribute unique ()
    		(11,12), #  has_match_attribute unique () -> match_attribute unique ()
    		(3,13), # match_class EParameter() -> has_match_attribute lowerBound ()
    		(13,14), #  has_match_attribute lowerBound () -> match_attribute lowerBound ()
    		(3,15), # match_class EParameter() -> has_match_attribute upperBound ()
    		(15,16), #  has_match_attribute upperBound () -> match_attribute upperBound ()
    		(5,17), # apply_class EParameter() -> has_apply_attribute name ()
    		(17,18), #  has_apply_attribute name () -> apply_attribute name ()
    		(19,20), #  equation of apply attribute name () -> left_expr
    		(20,18), #  left_expr -> apply_attribute name ()
    		(19,21), #  equation of apply attribute name () -> right_expr
    		(21,8), # right_expr --> term
    		(5,22), # apply_class EParameter() -> has_apply_attribute ordered ()
    		(22,23), #  has_apply_attribute ordered () -> apply_attribute ordered ()
    		(24,25), #  equation of apply attribute ordered () -> left_expr
    		(25,23), #  left_expr -> apply_attribute ordered ()
    		(24,26), #  equation of apply attribute ordered () -> right_expr
    		(26,10), # right_expr --> term
    		(5,27), # apply_class EParameter() -> has_apply_attribute unique ()
    		(27,28), #  has_apply_attribute unique () -> apply_attribute unique ()
    		(29,30), #  equation of apply attribute unique () -> left_expr
    		(30,28), #  left_expr -> apply_attribute unique ()
    		(29,31), #  equation of apply attribute unique () -> right_expr
    		(31,12), # right_expr --> term
    		(5,32), # apply_class EParameter() -> has_apply_attribute lowerBound ()
    		(32,33), #  has_apply_attribute lowerBound () -> apply_attribute lowerBound ()
    		(34,35), #  equation of apply attribute lowerBound () -> left_expr
    		(35,33), #  left_expr -> apply_attribute lowerBound ()
    		(34,36), #  equation of apply attribute lowerBound () -> right_expr
    		(36,14), # right_expr --> term
    		(5,37), # apply_class EParameter() -> has_apply_attribute upperBound ()
    		(37,38), #  has_apply_attribute upperBound () -> apply_attribute upperBound ()
    		(39,40), #  equation of apply attribute upperBound () -> left_expr
    		(40,38), #  left_expr -> apply_attribute upperBound ()
    		(39,41), #  equation of apply attribute upperBound () -> right_expr
    		(41,16), # right_expr --> term
    		(5,42), # apply_class EParameter() -> has_apply_attribute ApplyAttribute ()
    		(42,43), #  has_apply_attribute ApplyAttribute () -> apply_attribute ApplyAttribute ()
    		(44,45), #  equation of apply attribute ApplyAttribute () -> left_expr
    		(45,43), #  left_expr -> apply_attribute ApplyAttribute ()
    		(44,46), #  equation of apply attribute ApplyAttribute () -> right_expr
    		(46,47), # right_expr --> term
        	(0,2), # matchmodel -> pairedwith
        	(2,1) # pairedwith -> applyModel
        ])
        
