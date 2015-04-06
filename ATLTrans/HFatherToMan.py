from core.himesis import Himesis
import cPickle as pickle
import uuid

class HFatherToMan(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule FatherToMan.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HFatherToMan, self).__init__(name='HFatherToMan', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        # TODO Levi, need some help here because I don't know where does 
        # this value come from.
        self["mm__"] = pickle.loads("""(lp1
S'HimesisMM'
p2
a.""")
        
        self["name"] = """FatherToMan"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'FatherToMan')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'FatherToManmatchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'FatherToManapplymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'FatherToManpairedwith2')
        
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
        
        
    	# match association Family--father-->Member node
    	self.add_node()
    	self.vs[9]["associationType"] = """father"""
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
        
        
    	# has apply attribute name() node
    	self.add_node()
    	self.vs[12]["mm__"] = """hasAttribute_T"""
        #self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute name() node
    	self.add_node()
    	self.vs[13]["name"] = """name"""
        self.vs[13]["mm__"] = """Attribute"""
        self.vs[13]["Type"] = """'String'"""
        #self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation name() node
    	self.add_node()
    	self.vs[14]["name"] = """eq_"""
        self.vs[14]["mm__"] = """Equation"""
        #self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr name() node
    	self.add_node()
    	self.vs[15]["mm__"] = """leftExpr"""
        #self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr name() node
    	self.add_node()
    	self.vs[16]["mm__"] = """rightExpr"""
        #self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        
        
        # Add the edges
        self.add_edges([
    		(0,4), # matchmodel -> match_contains
    		(4,3), # match_contains -> match_class Family()
    		(0,6), # matchmodel -> match_contains
    		(6,5), # match_contains -> match_class Member()
    		(1,8), # applymodel -> apply_contains
    		(8,7), # apply_contains -> apply_class Man()
    		(3,9), # match_class Family() -> association father
    		(9,5), # association father  -> match_class Member()
    		(5,10), # match_class Member() -> has_match_attribute name ()
    		(10,11), #  has_match_attribute name () -> match_attribute name ()
    		(7,12), # apply_class Man() -> has_apply_attribute name ()
    		(12,13), #  has_apply_attribute name () -> apply_attribute name ()
    		(14,15), #  equation of apply attribute name () -> left_expr
    		(15,13), #  left_expr -> apply_attribute name ()
    		(14,16), #  equation of apply attribute name () -> right_expr
    		(16,11), # right_expr --> term
        	(0,2), # matchmodel -> pairedwith
        	(2,1) # pairedwith -> applyModel
        ])
        
