from core.himesis import Himesis
import cPickle as pickle
import uuid

class HinitSingleSwc2EcuMapping(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule initSingleSwc2EcuMapping.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HinitSingleSwc2EcuMapping, self).__init__(name='HinitSingleSwc2EcuMapping', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        # TODO Levi, need some help here because I don't know where does 
        # this value come from.
        self["mm__"] = pickle.loads("""(lp1
S'HimesisMM'
p2
a.""")
        
        self["name"] = """initSingleSwc2EcuMapping"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'initSingleSwc2EcuMapping')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'initSingleSwc2EcuMappingmatchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'initSingleSwc2EcuMappingapplymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'initSingleSwc2EcuMappingpairedwith2')
        
    	# match class Partition() node
    	self.add_node()
    	self.vs[3]["name"] = """"""
        self.vs[3]["classtype"] = """Partition"""
        self.vs[3]["mm__"] = """Partition"""
        self.vs[3]["cardinality"] = """+"""
        #self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# match_contains node for class Partition()
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        #self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'matchcontains4')
    	# match class PhysicalNode() node
    	self.add_node()
    	self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """PhysicalNode"""
        self.vs[5]["mm__"] = """PhysicalNode"""
        self.vs[5]["cardinality"] = """1"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# match_contains node for class PhysicalNode()
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        #self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'matchcontains6')
    	# match class Module() node
    	self.add_node()
    	self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """Module"""
        self.vs[7]["mm__"] = """Module"""
        self.vs[7]["cardinality"] = """1"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# match_contains node for class Module()
        self.add_node()
        self.vs[8]["mm__"] = """match_contains"""
        #self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'matchcontains8')
        
        
    	# apply class SwcToEcuMapping() node
    	self.add_node()
    	self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """SwcToEcuMapping"""
        self.vs[9]["mm__"] = """SwcToEcuMapping"""
        self.vs[9]["cardinality"] = """1"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply_contains node for class SwcToEcuMapping()
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        #self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains10')
        
        
    	# match association PhysicalNode--partition-->Partition node
    	self.add_node()
    	self.vs[11]["associationType"] = """partition"""
        self.vs[11]["mm__"] = """directLink_S"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc11')
    	# match association Partition--module-->Module node
    	self.add_node()
    	self.vs[12]["associationType"] = """module"""
        self.vs[12]["mm__"] = """directLink_S"""
        #self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc12')
        
        
        
        
    	# has match attribute name() node
    	self.add_node()
    	self.vs[13]["mm__"] = """hasAttribute_S"""
        #self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# match attribute name() node
    	self.add_node()
    	self.vs[14]["name"] = """name"""
        self.vs[14]["mm__"] = """Attribute"""
        self.vs[14]["Type"] = """'String'"""
        #self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        
        
    	# has apply attribute shortName() node
    	self.add_node()
    	self.vs[15]["mm__"] = """hasAttribute_T"""
        #self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute shortName() node
    	self.add_node()
    	self.vs[16]["name"] = """shortName"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["Type"] = """'String'"""
        #self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation shortName() node
    	self.add_node()
    	self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        #self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr shortName() node
    	self.add_node()
    	self.vs[18]["mm__"] = """leftExpr"""
        #self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr shortName() node
    	self.add_node()
    	self.vs[19]["mm__"] = """rightExpr"""
        #self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# attribute concat shortName() node
    	self.add_node()
    	self.vs[20]["name"] = """Concat20"""
        self.vs[20]["mm__"] = """Concat"""
        self.vs[20]["Type"] = """'String'"""
        #self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concat20')
    	# apply attribute concat has left args shortName() node
        self.add_node()
    	self.vs[21]["mm__"] = """hasArgs"""
        #self.vs[21]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgs21')
    	# apply attribute concat has right args shortName() node
        self.add_node()
    	self.vs[22]["mm__"] = """hasArgs"""
        #self.vs[22]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgs22')
    	# apply attribute atom shortName() node
    	self.add_node()
    	self.vs[23]["name"] = """Swc2EcuMapping_"""
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
    		(4,3), # match_contains -> match_class Partition()
    		(0,6), # matchmodel -> match_contains
    		(6,5), # match_contains -> match_class PhysicalNode()
    		(0,8), # matchmodel -> match_contains
    		(8,7), # match_contains -> match_class Module()
    		(1,10), # applymodel -> apply_contains
    		(10,9), # apply_contains -> apply_class SwcToEcuMapping()
    		(5,11), # match_class PhysicalNode() -> association partition
    		(11,3), # association partition  -> match_class Partition()
    		(3,12), # match_class Partition() -> association module
    		(12,7), # association module  -> match_class Module()
    		(3,13), # match_class Partition() -> has_match_attribute name ()
    		(13,14), #  has_match_attribute name () -> match_attribute name ()
    		(9,15), # apply_class SwcToEcuMapping() -> has_apply_attribute shortName ()
    		(15,16), #  has_apply_attribute shortName () -> apply_attribute shortName ()
    		(17,18), #  equation of apply attribute shortName () -> left_expr
    		(18,16), #  left_expr -> apply_attribute shortName ()
    		(17,19), #  equation of apply attribute shortName () -> right_expr
    		(20,21), #  apply attribute concat shortName () -> left has_args  
    		(21,23), #  left has_args -> term
    		(20,22), #  apply attribute concat shortName () -> right has_args  
    		(22,14), #  right has_args -> term
    		(19,20), # right_expr --> term
    		(9,24), # apply_class SwcToEcuMapping() -> has_apply_attribute ApplyAttribute ()
    		(24,25), #  has_apply_attribute ApplyAttribute () -> apply_attribute ApplyAttribute ()
    		(26,27), #  equation of apply attribute ApplyAttribute () -> left_expr
    		(27,25), #  left_expr -> apply_attribute ApplyAttribute ()
    		(26,28), #  equation of apply attribute ApplyAttribute () -> right_expr
    		(28,29), # right_expr --> term
        	(0,2), # matchmodel -> pairedwith
        	(2,1) # pairedwith -> applyModel
        ])
        
