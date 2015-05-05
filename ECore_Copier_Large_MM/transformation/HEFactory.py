from core.himesis import Himesis
import cPickle as pickle
import uuid

class HEFactory(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule EFactory.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HEFactory, self).__init__(name='HEFactory', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        # TODO Levi, need some help here because I don't know where does 
        # this value come from.
        self["mm__"] = pickle.loads("""(lp1
S'HimesisMM'
p2
a.""")
        
        self["name"] = """EFactory"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EFactory')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EFactorymatchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EFactoryapplymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EFactorypairedwith2')
        
    	# match class EFactory() node
    	self.add_node()
    	self.vs[3]["name"] = """"""
        self.vs[3]["classtype"] = """EFactory"""
        self.vs[3]["mm__"] = """EFactory"""
        self.vs[3]["cardinality"] = """+"""
        #self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# match_contains node for class EFactory()
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        #self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'matchcontains4')
        
        
    	# apply class EFactory() node
    	self.add_node()
    	self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EFactory"""
        self.vs[5]["mm__"] = """EFactory"""
        self.vs[5]["cardinality"] = """1"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply_contains node for class EFactory()
        self.add_node()
        self.vs[6]["mm__"] = """apply_contains"""
        #self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains6')
        
        
        
        
        
        
        
        
    	# has apply attribute ApplyAttribute() node
    	self.add_node()
    	self.vs[7]["mm__"] = """hasAttribute_T"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute ApplyAttribute() node
    	self.add_node()
    	self.vs[8]["name"] = """ApplyAttribute"""
        self.vs[8]["mm__"] = """Attribute"""
        self.vs[8]["Type"] = """'String'"""
        #self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation ApplyAttribute() node
    	self.add_node()
    	self.vs[9]["name"] = """eq_"""
        self.vs[9]["mm__"] = """Equation"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr ApplyAttribute() node
    	self.add_node()
    	self.vs[10]["mm__"] = """leftExpr"""
        #self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr ApplyAttribute() node
    	self.add_node()
    	self.vs[11]["mm__"] = """rightExpr"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# apply attribute atom ApplyAttribute() node
    	self.add_node()
    	self.vs[12]["name"] = """solveRef"""
        self.vs[12]["mm__"] = """Constant"""
        self.vs[12]["Type"] = """'String'"""
        #self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom12')
        
        
        # Add the edges
        self.add_edges([
    		(0,4), # matchmodel -> match_contains
    		(4,3), # match_contains -> match_class EFactory()
    		(1,6), # applymodel -> apply_contains
    		(6,5), # apply_contains -> apply_class EFactory()
    		(5,7), # apply_class EFactory() -> has_apply_attribute ApplyAttribute ()
    		(7,8), #  has_apply_attribute ApplyAttribute () -> apply_attribute ApplyAttribute ()
    		(9,10), #  equation of apply attribute ApplyAttribute () -> left_expr
    		(10,8), #  left_expr -> apply_attribute ApplyAttribute ()
    		(9,11), #  equation of apply attribute ApplyAttribute () -> right_expr
    		(11,12), # right_expr --> term
        	(0,2), # matchmodel -> pairedwith
        	(2,1) # pairedwith -> applyModel
        ])
        
