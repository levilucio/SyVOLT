from core.himesis import Himesis
import cPickle as pickle
import uuid

class HeoperationOUTeParametersSolveRefEOperationEParameterEOperationEParameter(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule eoperationOUTeParametersSolveRefEOperationEParameterEOperationEParameter.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HeoperationOUTeParametersSolveRefEOperationEParameterEOperationEParameter, self).__init__(name='HeoperationOUTeParametersSolveRefEOperationEParameterEOperationEParameter', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        # TODO Levi, need some help here because I don't know where does 
        # this value come from.
        self["mm__"] = pickle.loads("""(lp1
S'HimesisMM'
p2
a.""")
        
        self["name"] = """eoperationOUTeParametersSolveRefEOperationEParameterEOperationEParameter"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'eoperationOUTeParametersSolveRefEOperationEParameterEOperationEParameter')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'eoperationOUTeParametersSolveRefEOperationEParameterEOperationEParametermatchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'eoperationOUTeParametersSolveRefEOperationEParameterEOperationEParameterapplymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'eoperationOUTeParametersSolveRefEOperationEParameterEOperationEParameterpairedwith2')
        
    	# match class EOperation() node
    	self.add_node()
    	self.vs[3]["name"] = """"""
        self.vs[3]["classtype"] = """EOperation"""
        self.vs[3]["mm__"] = """EOperation"""
        self.vs[3]["cardinality"] = """+"""
        #self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# match_contains node for class EOperation()
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        #self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'matchcontains4')
    	# match class EParameter() node
    	self.add_node()
    	self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EParameter"""
        self.vs[5]["mm__"] = """EParameter"""
        self.vs[5]["cardinality"] = """+"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# match_contains node for class EParameter()
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        #self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'matchcontains6')
        
        
    	# apply class EOperation() node
    	self.add_node()
    	self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EOperation"""
        self.vs[7]["mm__"] = """EOperation"""
        self.vs[7]["cardinality"] = """1"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply_contains node for class EOperation()
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        #self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains8')
    	# apply class EParameter() node
    	self.add_node()
    	self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """EParameter"""
        self.vs[9]["mm__"] = """EParameter"""
        self.vs[9]["cardinality"] = """1"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply_contains node for class EParameter()
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        #self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains10')
        
        
    	# match association EOperation--eParameters-->EParameter node
    	self.add_node()
    	self.vs[11]["associationType"] = """eParameters"""
        self.vs[11]["mm__"] = """directLink_S"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc11')
        
    	# apply association EOperation--eParameters-->EParameter node
    	self.add_node()
    	self.vs[12]["associationType"] = """eParameters"""
        self.vs[12]["mm__"] = """directLink_T"""
        #self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc12')
        
    	# backward association EOperation---->EOperation node
    	self.add_node()
    	self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["mm__"] = """backward_link"""
        #self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'blink13')
    	# backward association EParameter---->EParameter node
    	self.add_node()
    	self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["mm__"] = """backward_link"""
        #self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'blink14')
        
        
        
        
    	# has apply attribute ApplyAttribute() node
    	self.add_node()
    	self.vs[15]["mm__"] = """hasAttribute_T"""
        #self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute ApplyAttribute() node
    	self.add_node()
    	self.vs[16]["name"] = """ApplyAttribute"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["Type"] = """'String'"""
        #self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation ApplyAttribute() node
    	self.add_node()
    	self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        #self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr ApplyAttribute() node
    	self.add_node()
    	self.vs[18]["mm__"] = """leftExpr"""
        #self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr ApplyAttribute() node
    	self.add_node()
    	self.vs[19]["mm__"] = """rightExpr"""
        #self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# apply attribute atom ApplyAttribute() node
    	self.add_node()
    	self.vs[20]["name"] = """solveRef"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["Type"] = """'String'"""
        #self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom20')
    	# has apply attribute ApplyAttribute() node
    	self.add_node()
    	self.vs[21]["mm__"] = """hasAttribute_T"""
        #self.vs[21]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute ApplyAttribute() node
    	self.add_node()
    	self.vs[22]["name"] = """ApplyAttribute"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["Type"] = """'String'"""
        #self.vs[22]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation ApplyAttribute() node
    	self.add_node()
    	self.vs[23]["name"] = """eq_"""
        self.vs[23]["mm__"] = """Equation"""
        #self.vs[23]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr ApplyAttribute() node
    	self.add_node()
    	self.vs[24]["mm__"] = """leftExpr"""
        #self.vs[24]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr ApplyAttribute() node
    	self.add_node()
    	self.vs[25]["mm__"] = """rightExpr"""
        #self.vs[25]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# apply attribute atom ApplyAttribute() node
    	self.add_node()
    	self.vs[26]["name"] = """solveRef"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["Type"] = """'String'"""
        #self.vs[26]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom26')
        
        
        # Add the edges
        self.add_edges([
    		(0,4), # matchmodel -> match_contains
    		(4,3), # match_contains -> match_class EOperation()
    		(0,6), # matchmodel -> match_contains
    		(6,5), # match_contains -> match_class EParameter()
    		(1,8), # applymodel -> apply_contains
    		(8,7), # apply_contains -> apply_class EOperation()
    		(1,10), # applymodel -> apply_contains
    		(10,9), # apply_contains -> apply_class EParameter()
    		(3,11), # match_class EOperation() -> association eParameters
    		(11,5), # association eParameters  -> match_class EParameter()
    		(7,12), # apply_class EOperation() -> association eParameters
    		(12,9), # association eParameters  -> apply_class EParameter()
    		(7,13), # apply_class EOperation() -> backward_association
    		(13,3), #  backward_association -> apply_class EOperation()
    		(9,14), # apply_class EParameter() -> backward_association
    		(14,5), #  backward_association -> apply_class EParameter()
    		(7,15), # apply_class EOperation() -> has_apply_attribute ApplyAttribute ()
    		(15,16), #  has_apply_attribute ApplyAttribute () -> apply_attribute ApplyAttribute ()
    		(17,18), #  equation of apply attribute ApplyAttribute () -> left_expr
    		(18,16), #  left_expr -> apply_attribute ApplyAttribute ()
    		(17,19), #  equation of apply attribute ApplyAttribute () -> right_expr
    		(19,20), # right_expr --> term
    		(9,21), # apply_class EParameter() -> has_apply_attribute ApplyAttribute ()
    		(21,22), #  has_apply_attribute ApplyAttribute () -> apply_attribute ApplyAttribute ()
    		(23,24), #  equation of apply attribute ApplyAttribute () -> left_expr
    		(24,22), #  left_expr -> apply_attribute ApplyAttribute ()
    		(23,25), #  equation of apply attribute ApplyAttribute () -> right_expr
    		(25,26), # right_expr --> term
        	(0,2), # matchmodel -> pairedwith
        	(2,1) # pairedwith -> applyModel
        ])
        