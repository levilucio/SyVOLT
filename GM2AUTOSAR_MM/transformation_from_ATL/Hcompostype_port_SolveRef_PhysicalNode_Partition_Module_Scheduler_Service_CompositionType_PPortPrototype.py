from core.himesis import Himesis
import cPickle as pickle
import uuid

class Hcompostype_port_SolveRef_PhysicalNode_Partition_Module_Scheduler_Service_CompositionType_PPortPrototype(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule compostype_port_SolveRef_PhysicalNode_Partition_Module_Scheduler_Service_CompositionType_PPortPrototype.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hcompostype_port_SolveRef_PhysicalNode_Partition_Module_Scheduler_Service_CompositionType_PPortPrototype, self).__init__(name='Hcompostype_port_SolveRef_PhysicalNode_Partition_Module_Scheduler_Service_CompositionType_PPortPrototype', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        # TODO Levi, need some help here because I don't know where does 
        # this value come from.
        self["mm__"] = pickle.loads("""(lp1
S'HimesisMM'
p2
a.""")
        
        self["name"] = """compostype_port_SolveRef_PhysicalNode_Partition_Module_Scheduler_Service_CompositionType_PPortPrototype"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'compostype_port_SolveRef_PhysicalNode_Partition_Module_Scheduler_Service_CompositionType_PPortPrototype')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'compostype_port_SolveRef_PhysicalNode_Partition_Module_Scheduler_Service_CompositionType_PPortPrototypematchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'compostype_port_SolveRef_PhysicalNode_Partition_Module_Scheduler_Service_CompositionType_PPortPrototypeapplymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'compostype_port_SolveRef_PhysicalNode_Partition_Module_Scheduler_Service_CompositionType_PPortPrototypepairedwith2')
        
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
    	# match class Scheduler() node
    	self.add_node()
    	self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """Scheduler"""
        self.vs[9]["mm__"] = """Scheduler"""
        self.vs[9]["cardinality"] = """+"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# match_contains node for class Scheduler()
        self.add_node()
        self.vs[10]["mm__"] = """match_contains"""
        #self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'matchcontains10')
    	# match class Service() node
    	self.add_node()
    	self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """Service"""
        self.vs[11]["mm__"] = """Service"""
        self.vs[11]["cardinality"] = """1"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# match_contains node for class Service()
        self.add_node()
        self.vs[12]["mm__"] = """match_contains"""
        #self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'matchcontains12')
        
        
    	# apply class CompositionType() node
    	self.add_node()
    	self.vs[13]["name"] = """"""
        self.vs[13]["classtype"] = """CompositionType"""
        self.vs[13]["mm__"] = """CompositionType"""
        self.vs[13]["cardinality"] = """1"""
        #self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply_contains node for class CompositionType()
        self.add_node()
        self.vs[14]["mm__"] = """apply_contains"""
        #self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains14')
    	# apply class PPortPrototype() node
    	self.add_node()
    	self.vs[15]["name"] = """"""
        self.vs[15]["classtype"] = """PPortPrototype"""
        self.vs[15]["mm__"] = """PPortPrototype"""
        self.vs[15]["cardinality"] = """1"""
        #self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply_contains node for class PPortPrototype()
        self.add_node()
        self.vs[16]["mm__"] = """apply_contains"""
        #self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains16')
        
        
    	# match association PhysicalNode--partition-->Partition node
    	self.add_node()
    	self.vs[17]["associationType"] = """partition"""
        self.vs[17]["mm__"] = """directLink_S"""
        #self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc17')
    	# match association Partition--module-->Module node
    	self.add_node()
    	self.vs[18]["associationType"] = """module"""
        self.vs[18]["mm__"] = """directLink_S"""
        #self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc18')
    	# match association Module--scheduler-->Scheduler node
    	self.add_node()
    	self.vs[19]["associationType"] = """scheduler"""
        self.vs[19]["mm__"] = """directLink_S"""
        #self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc19')
    	# match association Scheduler--required-->Service node
    	self.add_node()
    	self.vs[20]["associationType"] = """required"""
        self.vs[20]["mm__"] = """directLink_S"""
        #self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc20')
        
    	# apply association CompositionType--port-->PPortPrototype node
    	self.add_node()
    	self.vs[21]["associationType"] = """port"""
        self.vs[21]["mm__"] = """directLink_T"""
        #self.vs[21]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc21')
        
    	# backward association PhysicalNode---->CompositionType node
    	self.add_node()
    	self.vs[22]["type"] = """ruleDef"""
        self.vs[22]["mm__"] = """backward_link"""
        #self.vs[22]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'blink22')
        
        
    	# has match attribute name() node
    	self.add_node()
    	self.vs[23]["mm__"] = """hasAttribute_S"""
        #self.vs[23]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# match attribute name() node
    	self.add_node()
    	self.vs[24]["name"] = """name"""
        self.vs[24]["mm__"] = """Attribute"""
        self.vs[24]["Type"] = """'String'"""
        #self.vs[24]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        
        
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
    	self.vs[30]["name"] = """solveRef"""
        self.vs[30]["mm__"] = """Constant"""
        self.vs[30]["Type"] = """'String'"""
        #self.vs[30]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom30')
    	# has apply attribute shortName() node
    	self.add_node()
    	self.vs[31]["mm__"] = """hasAttribute_T"""
        #self.vs[31]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute shortName() node
    	self.add_node()
    	self.vs[32]["name"] = """shortName"""
        self.vs[32]["mm__"] = """Attribute"""
        self.vs[32]["Type"] = """'String'"""
        #self.vs[32]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation shortName() node
    	self.add_node()
    	self.vs[33]["name"] = """eq_"""
        self.vs[33]["mm__"] = """Equation"""
        #self.vs[33]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr shortName() node
    	self.add_node()
    	self.vs[34]["mm__"] = """leftExpr"""
        #self.vs[34]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr shortName() node
    	self.add_node()
    	self.vs[35]["mm__"] = """rightExpr"""
        #self.vs[35]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# attribute concat shortName() node
    	self.add_node()
    	self.vs[36]["name"] = """Concat36"""
        self.vs[36]["mm__"] = """Concat"""
        self.vs[36]["Type"] = """'String'"""
        #self.vs[36]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concat36')
    	# apply attribute concat has left args shortName() node
        self.add_node()
    	self.vs[37]["mm__"] = """hasArgs"""
        #self.vs[37]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgs37')
    	# apply attribute concat has right args shortName() node
        self.add_node()
    	self.vs[38]["mm__"] = """hasArgs"""
        #self.vs[38]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgs38')
    	# apply attribute atom shortName() node
    	self.add_node()
    	self.vs[39]["name"] = """PROV"""
        self.vs[39]["mm__"] = """Constant"""
        self.vs[39]["Type"] = """'String'"""
        #self.vs[39]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom39')
        
        
        # Add the edges
        self.add_edges([
    		(0,4), # matchmodel -> match_contains
    		(4,3), # match_contains -> match_class PhysicalNode()
    		(0,6), # matchmodel -> match_contains
    		(6,5), # match_contains -> match_class Partition()
    		(0,8), # matchmodel -> match_contains
    		(8,7), # match_contains -> match_class Module()
    		(0,10), # matchmodel -> match_contains
    		(10,9), # match_contains -> match_class Scheduler()
    		(0,12), # matchmodel -> match_contains
    		(12,11), # match_contains -> match_class Service()
    		(1,14), # applymodel -> apply_contains
    		(14,13), # apply_contains -> apply_class CompositionType()
    		(1,16), # applymodel -> apply_contains
    		(16,15), # apply_contains -> apply_class PPortPrototype()
    		(3,17), # match_class PhysicalNode() -> association partition
    		(17,5), # association partition  -> match_class Partition()
    		(5,18), # match_class Partition() -> association module
    		(18,7), # association module  -> match_class Module()
    		(7,19), # match_class Module() -> association scheduler
    		(19,9), # association scheduler  -> match_class Scheduler()
    		(9,20), # match_class Scheduler() -> association required
    		(20,11), # association required  -> match_class Service()
    		(13,21), # apply_class CompositionType() -> association port
    		(21,15), # association port  -> apply_class PPortPrototype()
    		(13,22), # apply_class CompositionType() -> backward_association
    		(22,3), #  backward_association -> apply_class PhysicalNode()
    		(9,23), # match_class Scheduler() -> has_match_attribute name ()
    		(23,24), #  has_match_attribute name () -> match_attribute name ()
    		(13,25), # apply_class CompositionType() -> has_apply_attribute ApplyAttribute ()
    		(25,26), #  has_apply_attribute ApplyAttribute () -> apply_attribute ApplyAttribute ()
    		(27,28), #  equation of apply attribute ApplyAttribute () -> left_expr
    		(28,26), #  left_expr -> apply_attribute ApplyAttribute ()
    		(27,29), #  equation of apply attribute ApplyAttribute () -> right_expr
    		(29,30), # right_expr --> term
    		(15,31), # apply_class PPortPrototype() -> has_apply_attribute shortName ()
    		(31,32), #  has_apply_attribute shortName () -> apply_attribute shortName ()
    		(33,34), #  equation of apply attribute shortName () -> left_expr
    		(34,32), #  left_expr -> apply_attribute shortName ()
    		(33,35), #  equation of apply attribute shortName () -> right_expr
    		(36,37), #  apply attribute concat shortName () -> left has_args  
    		(37,24), #  left has_args -> term
    		(36,38), #  apply attribute concat shortName () -> right has_args  
    		(38,39), #  right has_args -> term
    		(35,36), # right_expr --> term
        	(0,2), # matchmodel -> pairedwith
        	(2,1) # pairedwith -> applyModel
        ])
        
