from core.himesis import Himesis
import cPickle as pickle
import uuid

class HSonRule(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule SonRule.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HSonRule, self).__init__(name='HSonRule', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        # TODO Levi, need some help here because I don't know where does 
        # this value come from.
        self["mm__"] = pickle.loads("""(lp1
S'HimesisMM'
p2
a.""")
        
        self["name"] = """SonRule"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'SonRule')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'SonRulematchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'SonRuleapplymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'SonRulepairedwith2')
        
    	# match class Family() node
    	self.add_node()
    	self.vs[3]["name"] = """"""
        self.vs[3]["classtype"] = """Family"""
        self.vs[3]["mm__"] = """Family"""
        self.vs[3]["cardinality"] = """+"""
        #self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# match_contains node for class Family()
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        #self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'matchcontains4')
    	# match class Member() node
    	self.add_node()
    	self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """Member"""
        self.vs[5]["mm__"] = """Member"""
        self.vs[5]["cardinality"] = """+"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# match_contains node for class Member()
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        #self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'matchcontains6')
        
        
    	# apply class Man() node
    	self.add_node()
    	self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """Man"""
        self.vs[7]["mm__"] = """Man"""
        self.vs[7]["cardinality"] = """1"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply_contains node for class Man()
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        #self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains8')
        
        
    	# match association Family--son-->Member node
    	self.add_node()
    	self.vs[9]["associationType"] = """son"""
        self.vs[9]["mm__"] = """directLink_S"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc9')
        
        
        
        
    	# has match attribute name() node
    	self.add_node()
    	self.vs[10]["mm__"] = """hasAttribute_S"""
        #self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# match attribute name() node
    	self.add_node()
    	self.vs[11]["name"] = """name"""
        self.vs[11]["mm__"] = """Attribute"""
        self.vs[11]["Type"] = """'String'"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# has match attribute name() node
    	self.add_node()
    	self.vs[12]["mm__"] = """hasAttribute_S"""
        #self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# match attribute name() node
    	self.add_node()
    	self.vs[13]["name"] = """name"""
        self.vs[13]["mm__"] = """Attribute"""
        self.vs[13]["Type"] = """'String'"""
        #self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        
        
    	# has apply attribute ApplyAttribute() node
    	self.add_node()
    	self.vs[14]["mm__"] = """hasAttribute_T"""
        #self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute ApplyAttribute() node
    	self.add_node()
    	self.vs[15]["name"] = """ApplyAttribute"""
        self.vs[15]["mm__"] = """Attribute"""
        self.vs[15]["Type"] = """'String'"""
        #self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation ApplyAttribute() node
    	self.add_node()
    	self.vs[16]["name"] = """eq_"""
        self.vs[16]["mm__"] = """Equation"""
        #self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr ApplyAttribute() node
    	self.add_node()
    	self.vs[17]["mm__"] = """leftExpr"""
        #self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr ApplyAttribute() node
    	self.add_node()
    	self.vs[18]["mm__"] = """rightExpr"""
        #self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# apply attribute atom ApplyAttribute() node
    	self.add_node()
    	self.vs[19]["name"] = """famMemberSon"""
        self.vs[19]["mm__"] = """Constant"""
        self.vs[19]["Type"] = """'String'"""
        #self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom19')
    	# has apply attribute name() node
    	self.add_node()
    	self.vs[20]["mm__"] = """hasAttribute_T"""
        #self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute name() node
    	self.add_node()
    	self.vs[21]["name"] = """name"""
        self.vs[21]["mm__"] = """Attribute"""
        self.vs[21]["Type"] = """'String'"""
        #self.vs[21]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation name() node
    	self.add_node()
    	self.vs[22]["name"] = """eq_"""
        self.vs[22]["mm__"] = """Equation"""
        #self.vs[22]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr name() node
    	self.add_node()
    	self.vs[23]["mm__"] = """leftExpr"""
        #self.vs[23]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr name() node
    	self.add_node()
    	self.vs[24]["mm__"] = """rightExpr"""
        #self.vs[24]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# attribute concat name() node
    	self.add_node()
    	self.vs[25]["name"] = """Concat25"""
        self.vs[25]["mm__"] = """Concat"""
        self.vs[25]["Type"] = """'String'"""
        #self.vs[25]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concat25')
    	# apply attribute concat has left args name() node
        self.add_node()
    	self.vs[26]["mm__"] = """hasArgs"""
        #self.vs[26]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgs26')
    	# apply attribute concat has right args name() node
        self.add_node()
    	self.vs[27]["mm__"] = """hasArgs"""
        #self.vs[27]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgs27')
        
        
        # Add the edges
        self.add_edges([
    		(0,4), # matchmodel -> match_contains
    		(4,3), # match_contains -> match_class Family()
    		(0,6), # matchmodel -> match_contains
    		(6,5), # match_contains -> match_class Member()
    		(1,8), # applymodel -> apply_contains
    		(8,7), # apply_contains -> apply_class Man()
    		(3,9), # match_class Family() -> association son
    		(9,5), # association son  -> match_class Member()
    		(3,10), # match_class Family() -> has_match_attribute name ()
    		(10,11), #  has_match_attribute name () -> match_attribute name ()
    		(5,12), # match_class Member() -> has_match_attribute name ()
    		(12,13), #  has_match_attribute name () -> match_attribute name ()
    		(7,14), # apply_class Man() -> has_apply_attribute ApplyAttribute ()
    		(14,15), #  has_apply_attribute ApplyAttribute () -> apply_attribute ApplyAttribute ()
    		(16,17), #  equation of apply attribute ApplyAttribute () -> left_expr
    		(17,15), #  left_expr -> apply_attribute ApplyAttribute ()
    		(16,18), #  equation of apply attribute ApplyAttribute () -> right_expr
    		(18,19), # right_expr --> term
    		(7,20), # apply_class Man() -> has_apply_attribute name ()
    		(20,21), #  has_apply_attribute name () -> apply_attribute name ()
    		(22,23), #  equation of apply attribute name () -> left_expr
    		(23,21), #  left_expr -> apply_attribute name ()
    		(22,24), #  equation of apply attribute name () -> right_expr
    		(25,26), #  apply attribute concat name () -> left has_args  
    		(26,13), #  left has_args -> term
    		(25,27), #  apply attribute concat name () -> right has_args  
    		(27,11), #  right has_args -> term
    		(24,25), # right_expr --> term
        	(0,2), # matchmodel -> pairedwith
        	(2,1) # pairedwith -> applyModel
        ])
        
