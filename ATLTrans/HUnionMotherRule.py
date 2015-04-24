from core.himesis import Himesis
import cPickle as pickle
import uuid

class HUnionMotherRule(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule UnionMotherRule.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HUnionMotherRule, self).__init__(name='HUnionMotherRule', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        # TODO Levi, need some help here because I don't know where does 
        # this value come from.
        self["mm__"] = pickle.loads("""(lp1
S'HimesisMM'
p2
a.""")
        
        self["name"] = """UnionMotherRule"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'UnionMotherRule')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'UnionMotherRulematchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'UnionMotherRuleapplymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'UnionMotherRulepairedwith2')
        
    	# match class HouseholdRoot() node
    	self.add_node()
    	self.vs[3]["name"] = """"""
        self.vs[3]["classtype"] = """HouseholdRoot"""
        self.vs[3]["mm__"] = """HouseholdRoot"""
        self.vs[3]["cardinality"] = """+"""
        #self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# match_contains node for class HouseholdRoot()
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        #self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'matchcontains4')
    	# match class Family() node
    	self.add_node()
    	self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """Family"""
        self.vs[5]["mm__"] = """Family"""
        self.vs[5]["cardinality"] = """+"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# match_contains node for class Family()
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        #self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'matchcontains6')
    	# match class Member() node
    	self.add_node()
    	self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """Member"""
        self.vs[7]["mm__"] = """Member"""
        self.vs[7]["cardinality"] = """+"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# match_contains node for class Member()
        self.add_node()
        self.vs[8]["mm__"] = """match_contains"""
        #self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'matchcontains8')
        
        
    	# apply class CommunityRoot() node
    	self.add_node()
    	self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """CommunityRoot"""
        self.vs[9]["mm__"] = """CommunityRoot"""
        self.vs[9]["cardinality"] = """1"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply_contains node for class CommunityRoot()
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        #self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains10')
    	# apply class Woman() node
    	self.add_node()
    	self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """Woman"""
        self.vs[11]["mm__"] = """Woman"""
        self.vs[11]["cardinality"] = """1"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply_contains node for class Woman()
        self.add_node()
        self.vs[12]["mm__"] = """apply_contains"""
        #self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains12')
        
        
    	# match association HouseholdRoot--have-->Family node
    	self.add_node()
    	self.vs[13]["associationType"] = """have"""
        self.vs[13]["mm__"] = """directLink_S"""
        #self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc13')
    	# match association Family--mother-->Member node
    	self.add_node()
    	self.vs[14]["associationType"] = """mother"""
        self.vs[14]["mm__"] = """directLink_S"""
        #self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc14')
        
    	# apply association CommunityRoot--has-->Woman node
    	self.add_node()
    	self.vs[15]["associationType"] = """has"""
        self.vs[15]["mm__"] = """directLink_T"""
        #self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc15')
        
    	# backward association HouseholdRoot---->CommunityRoot node
    	self.add_node()
    	self.vs[16]["type"] = """ruleDef"""
        self.vs[16]["mm__"] = """backward_link"""
        #self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'blink16')
    	# backward association Family---->Woman node
    	self.add_node()
    	self.vs[17]["type"] = """ruleDef"""
        self.vs[17]["mm__"] = """backward_link"""
        #self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'blink17')
    	# backward association Member---->Woman node
    	self.add_node()
    	self.vs[18]["type"] = """ruleDef"""
        self.vs[18]["mm__"] = """backward_link"""
        #self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'blink18')
        
        
        
        
    	# has apply attribute ApplyAttribute() node
    	self.add_node()
    	self.vs[19]["mm__"] = """hasAttribute_T"""
        #self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute ApplyAttribute() node
    	self.add_node()
    	self.vs[20]["name"] = """ApplyAttribute"""
        self.vs[20]["mm__"] = """Attribute"""
        self.vs[20]["Type"] = """'String'"""
        #self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation ApplyAttribute() node
    	self.add_node()
    	self.vs[21]["name"] = """eq_"""
        self.vs[21]["mm__"] = """Equation"""
        #self.vs[21]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr ApplyAttribute() node
    	self.add_node()
    	self.vs[22]["mm__"] = """leftExpr"""
        #self.vs[22]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr ApplyAttribute() node
    	self.add_node()
    	self.vs[23]["mm__"] = """rightExpr"""
        #self.vs[23]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# apply attribute atom ApplyAttribute() node
    	self.add_node()
    	self.vs[24]["name"] = """root"""
        self.vs[24]["mm__"] = """Constant"""
        self.vs[24]["Type"] = """'String'"""
        #self.vs[24]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom24')
    	# has apply attribute ApplyAttribute() node
    	self.add_node()
    	self.vs[25]["mm__"] = """hasAttribute_T"""
        #self.vs[25]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute ApplyAttribute() node
    	self.add_node()
    	self.vs[26]["name"] = """ApplyAttribute"""
        self.vs[26]["mm__"] = """Attribute"""
        self.vs[26]["Type"] = """'String'"""
        #self.vs[26]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation ApplyAttribute() node
    	self.add_node()
    	self.vs[27]["name"] = """eq_"""
        self.vs[27]["mm__"] = """Equation"""
        #self.vs[27]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr ApplyAttribute() node
    	self.add_node()
    	self.vs[28]["mm__"] = """leftExpr"""
        #self.vs[28]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr ApplyAttribute() node
    	self.add_node()
    	self.vs[29]["mm__"] = """rightExpr"""
        #self.vs[29]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# apply attribute atom ApplyAttribute() node
    	self.add_node()
    	self.vs[30]["name"] = """famMemberMother"""
        self.vs[30]["mm__"] = """Constant"""
        self.vs[30]["Type"] = """'String'"""
        #self.vs[30]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom30')
        
        
        # Add the edges
        self.add_edges([
    		(0,4), # matchmodel -> match_contains
    		(4,3), # match_contains -> match_class HouseholdRoot()
    		(0,6), # matchmodel -> match_contains
    		(6,5), # match_contains -> match_class Family()
    		(0,8), # matchmodel -> match_contains
    		(8,7), # match_contains -> match_class Member()
    		(1,10), # applymodel -> apply_contains
    		(10,9), # apply_contains -> apply_class CommunityRoot()
    		(1,12), # applymodel -> apply_contains
    		(12,11), # apply_contains -> apply_class Woman()
    		(3,13), # match_class HouseholdRoot() -> association have
    		(13,5), # association have  -> match_class Family()
    		(5,14), # match_class Family() -> association mother
    		(14,7), # association mother  -> match_class Member()
    		(9,15), # apply_class CommunityRoot() -> association has
    		(15,11), # association has  -> apply_class Woman()
    		(9,16), # apply_class CommunityRoot() -> backward_association
    		(16,3), #  backward_association -> apply_class HouseholdRoot()
    		(11,17), # apply_class Woman() -> backward_association
    		(17,5), #  backward_association -> apply_class Family()
    		(11,18), # apply_class Woman() -> backward_association
    		(18,7), #  backward_association -> apply_class Member()
    		(9,19), # apply_class CommunityRoot() -> has_apply_attribute ApplyAttribute ()
    		(19,20), #  has_apply_attribute ApplyAttribute () -> apply_attribute ApplyAttribute ()
    		(21,22), #  equation of apply attribute ApplyAttribute () -> left_expr
    		(22,20), #  left_expr -> apply_attribute ApplyAttribute ()
    		(21,23), #  equation of apply attribute ApplyAttribute () -> right_expr
    		(23,24), # right_expr --> term
    		(11,25), # apply_class Woman() -> has_apply_attribute ApplyAttribute ()
    		(25,26), #  has_apply_attribute ApplyAttribute () -> apply_attribute ApplyAttribute ()
    		(27,28), #  equation of apply attribute ApplyAttribute () -> left_expr
    		(28,26), #  left_expr -> apply_attribute ApplyAttribute ()
    		(27,29), #  equation of apply attribute ApplyAttribute () -> right_expr
    		(29,30), # right_expr --> term
        	(0,2), # matchmodel -> pairedwith
        	(2,1) # pairedwith -> applyModel
        ])
        