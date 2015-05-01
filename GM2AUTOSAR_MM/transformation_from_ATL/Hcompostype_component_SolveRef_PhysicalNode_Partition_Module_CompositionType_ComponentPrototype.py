from core.himesis import Himesis
import cPickle as pickle
import uuid

class Hcompostype_component_SolveRef_PhysicalNode_Partition_Module_CompositionType_ComponentPrototype(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule compostype_component_SolveRef_PhysicalNode_Partition_Module_CompositionType_ComponentPrototype.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hcompostype_component_SolveRef_PhysicalNode_Partition_Module_CompositionType_ComponentPrototype, self).__init__(name='Hcompostype_component_SolveRef_PhysicalNode_Partition_Module_CompositionType_ComponentPrototype', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        # TODO Levi, need some help here because I don't know where does 
        # this value come from.
        self["mm__"] = pickle.loads("""(lp1
S'HimesisMM'
p2
a.""")
        
        self["name"] = """compostype_component_SolveRef_PhysicalNode_Partition_Module_CompositionType_ComponentPrototype"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'compostype_component_SolveRef_PhysicalNode_Partition_Module_CompositionType_ComponentPrototype')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'compostype_component_SolveRef_PhysicalNode_Partition_Module_CompositionType_ComponentPrototypematchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'compostype_component_SolveRef_PhysicalNode_Partition_Module_CompositionType_ComponentPrototypeapplymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'compostype_component_SolveRef_PhysicalNode_Partition_Module_CompositionType_ComponentPrototypepairedwith2')
        
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
    	# match class Module() node
    	self.add_node()
    	self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """Module"""
        self.vs[7]["mm__"] = """Module"""
        self.vs[7]["cardinality"] = """+"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# match_contains node for class Module()
        self.add_node()
        self.vs[8]["mm__"] = """match_contains"""
        #self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'matchcontains8')
        
        
    	# apply class CompositionType() node
    	self.add_node()
    	self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """CompositionType"""
        self.vs[9]["mm__"] = """CompositionType"""
        self.vs[9]["cardinality"] = """1"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply_contains node for class CompositionType()
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        #self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains10')
    	# apply class ComponentPrototype() node
    	self.add_node()
    	self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """ComponentPrototype"""
        self.vs[11]["mm__"] = """ComponentPrototype"""
        self.vs[11]["cardinality"] = """1"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply_contains node for class ComponentPrototype()
        self.add_node()
        self.vs[12]["mm__"] = """apply_contains"""
        #self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains12')
        
        
    	# match association PhysicalNode--partition-->Partition node
    	self.add_node()
    	self.vs[13]["associationType"] = """partition"""
        self.vs[13]["mm__"] = """directLink_S"""
        #self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc13')
    	# match association Partition--module-->Module node
    	self.add_node()
    	self.vs[14]["associationType"] = """module"""
        self.vs[14]["mm__"] = """directLink_S"""
        #self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc14')
        
    	# apply association CompositionType--component-->ComponentPrototype node
    	self.add_node()
    	self.vs[15]["associationType"] = """component"""
        self.vs[15]["mm__"] = """directLink_T"""
        #self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc15')
        
    	# backward association PhysicalNode---->CompositionType node
    	self.add_node()
    	self.vs[16]["type"] = """ruleDef"""
        self.vs[16]["mm__"] = """backward_link"""
        #self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'blink16')
    	# backward association Module---->ComponentPrototype node
    	self.add_node()
    	self.vs[17]["type"] = """ruleDef"""
        self.vs[17]["mm__"] = """backward_link"""
        #self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'blink17')
        
        
        
        
    	# has apply attribute ApplyAttribute() node
    	self.add_node()
    	self.vs[18]["mm__"] = """hasAttribute_T"""
        #self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute ApplyAttribute() node
    	self.add_node()
    	self.vs[19]["name"] = """ApplyAttribute"""
        self.vs[19]["mm__"] = """Attribute"""
        self.vs[19]["Type"] = """'String'"""
        #self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation ApplyAttribute() node
    	self.add_node()
    	self.vs[20]["name"] = """eq_"""
        self.vs[20]["mm__"] = """Equation"""
        #self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr ApplyAttribute() node
    	self.add_node()
    	self.vs[21]["mm__"] = """leftExpr"""
        #self.vs[21]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr ApplyAttribute() node
    	self.add_node()
    	self.vs[22]["mm__"] = """rightExpr"""
        #self.vs[22]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# apply attribute atom ApplyAttribute() node
    	self.add_node()
    	self.vs[23]["name"] = """solveRef"""
        self.vs[23]["mm__"] = """Constant"""
        self.vs[23]["Type"] = """'String'"""
        #self.vs[23]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom23')
    	# has apply attribute ApplyAttribute() node
    	self.add_node()
    	self.vs[24]["mm__"] = """hasAttribute_T"""
        #self.vs[24]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute ApplyAttribute() node
    	self.add_node()
    	self.vs[25]["name"] = """ApplyAttribute"""
        self.vs[25]["mm__"] = """Attribute"""
        self.vs[25]["Type"] = """'String'"""
        #self.vs[25]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation ApplyAttribute() node
    	self.add_node()
    	self.vs[26]["name"] = """eq_"""
        self.vs[26]["mm__"] = """Equation"""
        #self.vs[26]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr ApplyAttribute() node
    	self.add_node()
    	self.vs[27]["mm__"] = """leftExpr"""
        #self.vs[27]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr ApplyAttribute() node
    	self.add_node()
    	self.vs[28]["mm__"] = """rightExpr"""
        #self.vs[28]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# apply attribute atom ApplyAttribute() node
    	self.add_node()
    	self.vs[29]["name"] = """solveRef"""
        self.vs[29]["mm__"] = """Constant"""
        self.vs[29]["Type"] = """'String'"""
        #self.vs[29]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom29')
        
        
        # Add the edges
        self.add_edges([
    		(0,4), # matchmodel -> match_contains
    		(4,3), # match_contains -> match_class PhysicalNode()
    		(0,6), # matchmodel -> match_contains
    		(6,5), # match_contains -> match_class Partition()
    		(0,8), # matchmodel -> match_contains
    		(8,7), # match_contains -> match_class Module()
    		(1,10), # applymodel -> apply_contains
    		(10,9), # apply_contains -> apply_class CompositionType()
    		(1,12), # applymodel -> apply_contains
    		(12,11), # apply_contains -> apply_class ComponentPrototype()
    		(3,13), # match_class PhysicalNode() -> association partition
    		(13,5), # association partition  -> match_class Partition()
    		(5,14), # match_class Partition() -> association module
    		(14,7), # association module  -> match_class Module()
    		(9,15), # apply_class CompositionType() -> association component
    		(15,11), # association component  -> apply_class ComponentPrototype()
    		(9,16), # apply_class CompositionType() -> backward_association
    		(16,3), #  backward_association -> apply_class PhysicalNode()
    		(11,17), # apply_class ComponentPrototype() -> backward_association
    		(17,7), #  backward_association -> apply_class Module()
    		(9,18), # apply_class CompositionType() -> has_apply_attribute ApplyAttribute ()
    		(18,19), #  has_apply_attribute ApplyAttribute () -> apply_attribute ApplyAttribute ()
    		(20,21), #  equation of apply attribute ApplyAttribute () -> left_expr
    		(21,19), #  left_expr -> apply_attribute ApplyAttribute ()
    		(20,22), #  equation of apply attribute ApplyAttribute () -> right_expr
    		(22,23), # right_expr --> term
    		(11,24), # apply_class ComponentPrototype() -> has_apply_attribute ApplyAttribute ()
    		(24,25), #  has_apply_attribute ApplyAttribute () -> apply_attribute ApplyAttribute ()
    		(26,27), #  equation of apply attribute ApplyAttribute () -> left_expr
    		(27,25), #  left_expr -> apply_attribute ApplyAttribute ()
    		(26,28), #  equation of apply attribute ApplyAttribute () -> right_expr
    		(28,29), # right_expr --> term
        	(0,2), # matchmodel -> pairedwith
        	(2,1) # pairedwith -> applyModel
        ])
        
