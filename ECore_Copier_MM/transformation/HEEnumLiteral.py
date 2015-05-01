from core.himesis import Himesis
import cPickle as pickle
import uuid

class HEEnumLiteral(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule EEnumLiteral.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HEEnumLiteral, self).__init__(name='HEEnumLiteral', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        # TODO Levi, need some help here because I don't know where does 
        # this value come from.
        self["mm__"] = pickle.loads("""(lp1
S'HimesisMM'
p2
a.""")
        
        self["name"] = """EEnumLiteral"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EEnumLiteral')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EEnumLiteralmatchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EEnumLiteralapplymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EEnumLiteralpairedwith2')
        
    	# match class EEnumLiteral() node
    	self.add_node()
    	self.vs[3]["name"] = """"""
        self.vs[3]["classtype"] = """EEnumLiteral"""
        self.vs[3]["mm__"] = """EEnumLiteral"""
        self.vs[3]["cardinality"] = """+"""
        #self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# match_contains node for class EEnumLiteral()
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        #self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'matchcontains4')
        
        
    	# apply class EEnumLiteral() node
    	self.add_node()
    	self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EEnumLiteral"""
        self.vs[5]["mm__"] = """EEnumLiteral"""
        self.vs[5]["cardinality"] = """1"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply_contains node for class EEnumLiteral()
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
    	# has match attribute value() node
    	self.add_node()
    	self.vs[9]["mm__"] = """hasAttribute_S"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# match attribute value() node
    	self.add_node()
    	self.vs[10]["name"] = """value"""
        self.vs[10]["mm__"] = """Attribute"""
        self.vs[10]["Type"] = """'String'"""
        #self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# has match attribute instance() node
    	self.add_node()
    	self.vs[11]["mm__"] = """hasAttribute_S"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# match attribute instance() node
    	self.add_node()
    	self.vs[12]["name"] = """instance"""
        self.vs[12]["mm__"] = """Attribute"""
        self.vs[12]["Type"] = """'String'"""
        #self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        
        
    	# has apply attribute name() node
    	self.add_node()
    	self.vs[13]["mm__"] = """hasAttribute_T"""
        #self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute name() node
    	self.add_node()
    	self.vs[14]["name"] = """name"""
        self.vs[14]["mm__"] = """Attribute"""
        self.vs[14]["Type"] = """'String'"""
        #self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation name() node
    	self.add_node()
    	self.vs[15]["name"] = """eq_"""
        self.vs[15]["mm__"] = """Equation"""
        #self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr name() node
    	self.add_node()
    	self.vs[16]["mm__"] = """leftExpr"""
        #self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr name() node
    	self.add_node()
    	self.vs[17]["mm__"] = """rightExpr"""
        #self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# has apply attribute value() node
    	self.add_node()
    	self.vs[18]["mm__"] = """hasAttribute_T"""
        #self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute value() node
    	self.add_node()
    	self.vs[19]["name"] = """value"""
        self.vs[19]["mm__"] = """Attribute"""
        self.vs[19]["Type"] = """'String'"""
        #self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation value() node
    	self.add_node()
    	self.vs[20]["name"] = """eq_"""
        self.vs[20]["mm__"] = """Equation"""
        #self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr value() node
    	self.add_node()
    	self.vs[21]["mm__"] = """leftExpr"""
        #self.vs[21]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr value() node
    	self.add_node()
    	self.vs[22]["mm__"] = """rightExpr"""
        #self.vs[22]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# has apply attribute instance() node
    	self.add_node()
    	self.vs[23]["mm__"] = """hasAttribute_T"""
        #self.vs[23]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute instance() node
    	self.add_node()
    	self.vs[24]["name"] = """instance"""
        self.vs[24]["mm__"] = """Attribute"""
        self.vs[24]["Type"] = """'String'"""
        #self.vs[24]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation instance() node
    	self.add_node()
    	self.vs[25]["name"] = """eq_"""
        self.vs[25]["mm__"] = """Equation"""
        #self.vs[25]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr instance() node
    	self.add_node()
    	self.vs[26]["mm__"] = """leftExpr"""
        #self.vs[26]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr instance() node
    	self.add_node()
    	self.vs[27]["mm__"] = """rightExpr"""
        #self.vs[27]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# has apply attribute ApplyAttribute() node
    	self.add_node()
    	self.vs[28]["mm__"] = """hasAttribute_T"""
        #self.vs[28]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute ApplyAttribute() node
    	self.add_node()
    	self.vs[29]["name"] = """ApplyAttribute"""
        self.vs[29]["mm__"] = """Attribute"""
        self.vs[29]["Type"] = """'String'"""
        #self.vs[29]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation ApplyAttribute() node
    	self.add_node()
    	self.vs[30]["name"] = """eq_"""
        self.vs[30]["mm__"] = """Equation"""
        #self.vs[30]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr ApplyAttribute() node
    	self.add_node()
    	self.vs[31]["mm__"] = """leftExpr"""
        #self.vs[31]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr ApplyAttribute() node
    	self.add_node()
    	self.vs[32]["mm__"] = """rightExpr"""
        #self.vs[32]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# apply attribute atom ApplyAttribute() node
    	self.add_node()
    	self.vs[33]["name"] = """solveRef"""
        self.vs[33]["mm__"] = """Constant"""
        self.vs[33]["Type"] = """'String'"""
        #self.vs[33]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom33')
        
        
        # Add the edges
        self.add_edges([
    		(0,4), # matchmodel -> match_contains
    		(4,3), # match_contains -> match_class EEnumLiteral()
    		(1,6), # applymodel -> apply_contains
    		(6,5), # apply_contains -> apply_class EEnumLiteral()
    		(3,7), # match_class EEnumLiteral() -> has_match_attribute name ()
    		(7,8), #  has_match_attribute name () -> match_attribute name ()
    		(3,9), # match_class EEnumLiteral() -> has_match_attribute value ()
    		(9,10), #  has_match_attribute value () -> match_attribute value ()
    		(3,11), # match_class EEnumLiteral() -> has_match_attribute instance ()
    		(11,12), #  has_match_attribute instance () -> match_attribute instance ()
    		(5,13), # apply_class EEnumLiteral() -> has_apply_attribute name ()
    		(13,14), #  has_apply_attribute name () -> apply_attribute name ()
    		(15,16), #  equation of apply attribute name () -> left_expr
    		(16,14), #  left_expr -> apply_attribute name ()
    		(15,17), #  equation of apply attribute name () -> right_expr
    		(17,8), # right_expr --> term
    		(5,18), # apply_class EEnumLiteral() -> has_apply_attribute value ()
    		(18,19), #  has_apply_attribute value () -> apply_attribute value ()
    		(20,21), #  equation of apply attribute value () -> left_expr
    		(21,19), #  left_expr -> apply_attribute value ()
    		(20,22), #  equation of apply attribute value () -> right_expr
    		(22,10), # right_expr --> term
    		(5,23), # apply_class EEnumLiteral() -> has_apply_attribute instance ()
    		(23,24), #  has_apply_attribute instance () -> apply_attribute instance ()
    		(25,26), #  equation of apply attribute instance () -> left_expr
    		(26,24), #  left_expr -> apply_attribute instance ()
    		(25,27), #  equation of apply attribute instance () -> right_expr
    		(27,12), # right_expr --> term
    		(5,28), # apply_class EEnumLiteral() -> has_apply_attribute ApplyAttribute ()
    		(28,29), #  has_apply_attribute ApplyAttribute () -> apply_attribute ApplyAttribute ()
    		(30,31), #  equation of apply attribute ApplyAttribute () -> left_expr
    		(31,29), #  left_expr -> apply_attribute ApplyAttribute ()
    		(30,32), #  equation of apply attribute ApplyAttribute () -> right_expr
    		(32,33), # right_expr --> term
        	(0,2), # matchmodel -> pairedwith
        	(2,1) # pairedwith -> applyModel
        ])
        
