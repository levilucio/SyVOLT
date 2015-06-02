from core.himesis import Himesis
import cPickle as pickle
import uuid

class Hmapping_ecuInstance_SolveRef_PhysicalNode_Partition_SwcToEcuMapping_EcuInstance(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule mapping_ecuInstance_SolveRef_PhysicalNode_Partition_SwcToEcuMapping_EcuInstance.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hmapping_ecuInstance_SolveRef_PhysicalNode_Partition_SwcToEcuMapping_EcuInstance, self).__init__(name='Hmapping_ecuInstance_SolveRef_PhysicalNode_Partition_SwcToEcuMapping_EcuInstance', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        # TODO Levi, need some help here because I don't know where does 
        # this value come from.
        self["mm__"] = pickle.loads("""(lp1
S'HimesisMM'
p2
a.""")
        
        self["name"] = """mapping_ecuInstance_SolveRef_PhysicalNode_Partition_SwcToEcuMapping_EcuInstance"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'mapping_ecuInstance_SolveRef_PhysicalNode_Partition_SwcToEcuMapping_EcuInstance')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'mapping_ecuInstance_SolveRef_PhysicalNode_Partition_SwcToEcuMapping_EcuInstancematchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'mapping_ecuInstance_SolveRef_PhysicalNode_Partition_SwcToEcuMapping_EcuInstanceapplymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'mapping_ecuInstance_SolveRef_PhysicalNode_Partition_SwcToEcuMapping_EcuInstancepairedwith2')
        
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
        self.vs[5]["cardinality"] = """+"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# match_contains node for class Partition()
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        #self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'matchcontains6')
        
        
    	# apply class SwcToEcuMapping() node
    	self.add_node()
    	self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """SwcToEcuMapping"""
        self.vs[7]["mm__"] = """SwcToEcuMapping"""
        self.vs[7]["cardinality"] = """1"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply_contains node for class SwcToEcuMapping()
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        #self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains8')
    	# apply class EcuInstance() node
    	self.add_node()
    	self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """EcuInstance"""
        self.vs[9]["mm__"] = """EcuInstance"""
        self.vs[9]["cardinality"] = """1"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply_contains node for class EcuInstance()
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        #self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains10')
        
        
    	# match association PhysicalNode--partition-->Partition node
    	self.add_node()
    	self.vs[11]["associationType"] = """partition"""
        self.vs[11]["mm__"] = """directLink_S"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc11')
        
    	# apply association SwcToEcuMapping--ecuInstance-->EcuInstance node
    	self.add_node()
    	self.vs[12]["associationType"] = """ecuInstance"""
        self.vs[12]["mm__"] = """directLink_T"""
        #self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc12')
        
    	# backward association PhysicalNode---->EcuInstance node
    	self.add_node()
    	self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["mm__"] = """backward_link"""
        #self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'blink13')
    	# backward association Partition---->SwcToEcuMapping node
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
    		(4,3), # match_contains -> match_class PhysicalNode()
    		(0,6), # matchmodel -> match_contains
    		(6,5), # match_contains -> match_class Partition()
    		(1,8), # applymodel -> apply_contains
    		(8,7), # apply_contains -> apply_class SwcToEcuMapping()
    		(1,10), # applymodel -> apply_contains
    		(10,9), # apply_contains -> apply_class EcuInstance()
    		(3,11), # match_class PhysicalNode() -> association partition
    		(11,5), # association partition  -> match_class Partition()
    		(7,12), # apply_class SwcToEcuMapping() -> association ecuInstance
    		(12,9), # association ecuInstance  -> apply_class EcuInstance()
    		(9,13), # apply_class EcuInstance() -> backward_association
    		(13,3), #  backward_association -> apply_class PhysicalNode()
    		(7,14), # apply_class SwcToEcuMapping() -> backward_association
    		(14,5), #  backward_association -> apply_class Partition()
    		(7,15), # apply_class SwcToEcuMapping() -> has_apply_attribute ApplyAttribute ()
    		(15,16), #  has_apply_attribute ApplyAttribute () -> apply_attribute ApplyAttribute ()
    		(17,18), #  equation of apply attribute ApplyAttribute () -> left_expr
    		(18,16), #  left_expr -> apply_attribute ApplyAttribute ()
    		(17,19), #  equation of apply attribute ApplyAttribute () -> right_expr
    		(19,20), # right_expr --> term
    		(9,21), # apply_class EcuInstance() -> has_apply_attribute ApplyAttribute ()
    		(21,22), #  has_apply_attribute ApplyAttribute () -> apply_attribute ApplyAttribute ()
    		(23,24), #  equation of apply attribute ApplyAttribute () -> left_expr
    		(24,22), #  left_expr -> apply_attribute ApplyAttribute ()
    		(23,25), #  equation of apply attribute ApplyAttribute () -> right_expr
    		(25,26), # right_expr --> term
        	(0,2), # matchmodel -> pairedwith
        	(2,1) # pairedwith -> applyModel
        ])
        