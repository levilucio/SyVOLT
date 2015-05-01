from core.himesis import Himesis
import cPickle as pickle
import uuid

class HcreateComponent(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule createComponent.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HcreateComponent, self).__init__(name='HcreateComponent', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        # TODO Levi, need some help here because I don't know where does 
        # this value come from.
        self["mm__"] = pickle.loads("""(lp1
S'HimesisMM'
p2
a.""")
        
        self["name"] = """createComponent"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'createComponent')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'createComponentmatchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'createComponentapplymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'createComponentpairedwith2')
        
    	# match class Module() node
    	self.add_node()
    	self.vs[3]["name"] = """"""
        self.vs[3]["classtype"] = """Module"""
        self.vs[3]["mm__"] = """Module"""
        self.vs[3]["cardinality"] = """+"""
        #self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# match_contains node for class Module()
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        #self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'matchcontains4')
    	# match class Partition() node
    	self.add_node()
    	self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """Partition"""
        self.vs[5]["mm__"] = """Partition"""
        self.vs[5]["cardinality"] = """1"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# match_contains node for class Partition()
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        #self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'matchcontains6')
    	# match class PhysicalNode() node
    	self.add_node()
    	self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """PhysicalNode"""
        self.vs[7]["mm__"] = """PhysicalNode"""
        self.vs[7]["cardinality"] = """1"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# match_contains node for class PhysicalNode()
        self.add_node()
        self.vs[8]["mm__"] = """match_contains"""
        #self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'matchcontains8')
        
        
    	# apply class SwCompToEcuMapping_component() node
    	self.add_node()
    	self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """SwCompToEcuMapping_component"""
        self.vs[9]["mm__"] = """SwCompToEcuMapping_component"""
        self.vs[9]["cardinality"] = """1"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply_contains node for class SwCompToEcuMapping_component()
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
        
    	# apply association SwCompToEcuMapping_component--componentPrototype-->ComponentPrototype node
    	self.add_node()
    	self.vs[15]["associationType"] = """componentPrototype"""
        self.vs[15]["mm__"] = """directLink_T"""
        #self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc15')
        
        
        
    	# has match attribute name() node
    	self.add_node()
    	self.vs[16]["mm__"] = """hasAttribute_S"""
        #self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# match attribute name() node
    	self.add_node()
    	self.vs[17]["name"] = """name"""
        self.vs[17]["mm__"] = """Attribute"""
        self.vs[17]["Type"] = """'String'"""
        #self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        
        
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
    	# has apply attribute shortName() node
    	self.add_node()
    	self.vs[24]["mm__"] = """hasAttribute_T"""
        #self.vs[24]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute shortName() node
    	self.add_node()
    	self.vs[25]["name"] = """shortName"""
        self.vs[25]["mm__"] = """Attribute"""
        self.vs[25]["Type"] = """'String'"""
        #self.vs[25]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation shortName() node
    	self.add_node()
    	self.vs[26]["name"] = """eq_"""
        self.vs[26]["mm__"] = """Equation"""
        #self.vs[26]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr shortName() node
    	self.add_node()
    	self.vs[27]["mm__"] = """leftExpr"""
        #self.vs[27]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr shortName() node
    	self.add_node()
    	self.vs[28]["mm__"] = """rightExpr"""
        #self.vs[28]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# has apply attribute ApplyAttribute() node
    	self.add_node()
    	self.vs[29]["mm__"] = """hasAttribute_T"""
        #self.vs[29]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute ApplyAttribute() node
    	self.add_node()
    	self.vs[30]["name"] = """ApplyAttribute"""
        self.vs[30]["mm__"] = """Attribute"""
        self.vs[30]["Type"] = """'String'"""
        #self.vs[30]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation ApplyAttribute() node
    	self.add_node()
    	self.vs[31]["name"] = """eq_"""
        self.vs[31]["mm__"] = """Equation"""
        #self.vs[31]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr ApplyAttribute() node
    	self.add_node()
    	self.vs[32]["mm__"] = """leftExpr"""
        #self.vs[32]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr ApplyAttribute() node
    	self.add_node()
    	self.vs[33]["mm__"] = """rightExpr"""
        #self.vs[33]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# apply attribute atom ApplyAttribute() node
    	self.add_node()
    	self.vs[34]["name"] = """solveRef"""
        self.vs[34]["mm__"] = """Constant"""
        self.vs[34]["Type"] = """'String'"""
        #self.vs[34]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom34')
        
        
        # Add the edges
        self.add_edges([
    		(0,4), # matchmodel -> match_contains
    		(4,3), # match_contains -> match_class Module()
    		(0,6), # matchmodel -> match_contains
    		(6,5), # match_contains -> match_class Partition()
    		(0,8), # matchmodel -> match_contains
    		(8,7), # match_contains -> match_class PhysicalNode()
    		(1,10), # applymodel -> apply_contains
    		(10,9), # apply_contains -> apply_class SwCompToEcuMapping_component()
    		(1,12), # applymodel -> apply_contains
    		(12,11), # apply_contains -> apply_class ComponentPrototype()
    		(7,13), # match_class PhysicalNode() -> association partition
    		(13,5), # association partition  -> match_class Partition()
    		(5,14), # match_class Partition() -> association module
    		(14,3), # association module  -> match_class Module()
    		(9,15), # apply_class SwCompToEcuMapping_component() -> association componentPrototype
    		(15,11), # association componentPrototype  -> apply_class ComponentPrototype()
    		(3,16), # match_class Module() -> has_match_attribute name ()
    		(16,17), #  has_match_attribute name () -> match_attribute name ()
    		(9,18), # apply_class SwCompToEcuMapping_component() -> has_apply_attribute ApplyAttribute ()
    		(18,19), #  has_apply_attribute ApplyAttribute () -> apply_attribute ApplyAttribute ()
    		(20,21), #  equation of apply attribute ApplyAttribute () -> left_expr
    		(21,19), #  left_expr -> apply_attribute ApplyAttribute ()
    		(20,22), #  equation of apply attribute ApplyAttribute () -> right_expr
    		(22,23), # right_expr --> term
    		(11,24), # apply_class ComponentPrototype() -> has_apply_attribute shortName ()
    		(24,25), #  has_apply_attribute shortName () -> apply_attribute shortName ()
    		(26,27), #  equation of apply attribute shortName () -> left_expr
    		(27,25), #  left_expr -> apply_attribute shortName ()
    		(26,28), #  equation of apply attribute shortName () -> right_expr
    		(28,17), # right_expr --> term
    		(11,29), # apply_class ComponentPrototype() -> has_apply_attribute ApplyAttribute ()
    		(29,30), #  has_apply_attribute ApplyAttribute () -> apply_attribute ApplyAttribute ()
    		(31,32), #  equation of apply attribute ApplyAttribute () -> left_expr
    		(32,30), #  left_expr -> apply_attribute ApplyAttribute ()
    		(31,33), #  equation of apply attribute ApplyAttribute () -> right_expr
    		(33,34), # right_expr --> term
        	(0,2), # matchmodel -> pairedwith
        	(2,1) # pairedwith -> applyModel
        ])
        
