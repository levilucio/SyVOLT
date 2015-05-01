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
        
        
    	# apply class SwCompToEcuMapping_component() node
    	self.add_node()
    	self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """SwCompToEcuMapping_component"""
        self.vs[5]["mm__"] = """SwCompToEcuMapping_component"""
        self.vs[5]["cardinality"] = """1"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply_contains node for class SwCompToEcuMapping_component()
        self.add_node()
        self.vs[6]["mm__"] = """apply_contains"""
        #self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains6')
    	# apply class ComponentPrototype() node
    	self.add_node()
    	self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """ComponentPrototype"""
        self.vs[7]["mm__"] = """ComponentPrototype"""
        self.vs[7]["cardinality"] = """1"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply_contains node for class ComponentPrototype()
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        #self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains8')
        
        
        
    	# apply association SwCompToEcuMapping_component--componentPrototype-->ComponentPrototype node
    	self.add_node()
    	self.vs[9]["associationType"] = """componentPrototype"""
        self.vs[9]["mm__"] = """directLink_T"""
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
        
        
    	# has apply attribute ApplyAttribute() node
    	self.add_node()
    	self.vs[12]["mm__"] = """hasAttribute_T"""
        #self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute ApplyAttribute() node
    	self.add_node()
    	self.vs[13]["name"] = """ApplyAttribute"""
        self.vs[13]["mm__"] = """Attribute"""
        self.vs[13]["Type"] = """'String'"""
        #self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation ApplyAttribute() node
    	self.add_node()
    	self.vs[14]["name"] = """eq_"""
        self.vs[14]["mm__"] = """Equation"""
        #self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr ApplyAttribute() node
    	self.add_node()
    	self.vs[15]["mm__"] = """leftExpr"""
        #self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr ApplyAttribute() node
    	self.add_node()
    	self.vs[16]["mm__"] = """rightExpr"""
        #self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# apply attribute atom ApplyAttribute() node
    	self.add_node()
    	self.vs[17]["name"] = """solveRef"""
        self.vs[17]["mm__"] = """Constant"""
        self.vs[17]["Type"] = """'String'"""
        #self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom17')
    	# has apply attribute shortName() node
    	self.add_node()
    	self.vs[18]["mm__"] = """hasAttribute_T"""
        #self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute shortName() node
    	self.add_node()
    	self.vs[19]["name"] = """shortName"""
        self.vs[19]["mm__"] = """Attribute"""
        self.vs[19]["Type"] = """'String'"""
        #self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation shortName() node
    	self.add_node()
    	self.vs[20]["name"] = """eq_"""
        self.vs[20]["mm__"] = """Equation"""
        #self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr shortName() node
    	self.add_node()
    	self.vs[21]["mm__"] = """leftExpr"""
        #self.vs[21]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr shortName() node
    	self.add_node()
    	self.vs[22]["mm__"] = """rightExpr"""
        #self.vs[22]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# has apply attribute ApplyAttribute() node
    	self.add_node()
    	self.vs[23]["mm__"] = """hasAttribute_T"""
        #self.vs[23]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute ApplyAttribute() node
    	self.add_node()
    	self.vs[24]["name"] = """ApplyAttribute"""
        self.vs[24]["mm__"] = """Attribute"""
        self.vs[24]["Type"] = """'String'"""
        #self.vs[24]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation ApplyAttribute() node
    	self.add_node()
    	self.vs[25]["name"] = """eq_"""
        self.vs[25]["mm__"] = """Equation"""
        #self.vs[25]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr ApplyAttribute() node
    	self.add_node()
    	self.vs[26]["mm__"] = """leftExpr"""
        #self.vs[26]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr ApplyAttribute() node
    	self.add_node()
    	self.vs[27]["mm__"] = """rightExpr"""
        #self.vs[27]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# apply attribute atom ApplyAttribute() node
    	self.add_node()
    	self.vs[28]["name"] = """solveRef"""
        self.vs[28]["mm__"] = """Constant"""
        self.vs[28]["Type"] = """'String'"""
        #self.vs[28]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom28')
        
        
        # Add the edges
        self.add_edges([
    		(0,4), # matchmodel -> match_contains
    		(4,3), # match_contains -> match_class Module()
    		(1,6), # applymodel -> apply_contains
    		(6,5), # apply_contains -> apply_class SwCompToEcuMapping_component()
    		(1,8), # applymodel -> apply_contains
    		(8,7), # apply_contains -> apply_class ComponentPrototype()
    		(5,9), # apply_class SwCompToEcuMapping_component() -> association componentPrototype
    		(9,7), # association componentPrototype  -> apply_class ComponentPrototype()
    		(3,10), # match_class Module() -> has_match_attribute name ()
    		(10,11), #  has_match_attribute name () -> match_attribute name ()
    		(5,12), # apply_class SwCompToEcuMapping_component() -> has_apply_attribute ApplyAttribute ()
    		(12,13), #  has_apply_attribute ApplyAttribute () -> apply_attribute ApplyAttribute ()
    		(14,15), #  equation of apply attribute ApplyAttribute () -> left_expr
    		(15,13), #  left_expr -> apply_attribute ApplyAttribute ()
    		(14,16), #  equation of apply attribute ApplyAttribute () -> right_expr
    		(16,17), # right_expr --> term
    		(7,18), # apply_class ComponentPrototype() -> has_apply_attribute shortName ()
    		(18,19), #  has_apply_attribute shortName () -> apply_attribute shortName ()
    		(20,21), #  equation of apply attribute shortName () -> left_expr
    		(21,19), #  left_expr -> apply_attribute shortName ()
    		(20,22), #  equation of apply attribute shortName () -> right_expr
    		(22,11), # right_expr --> term
    		(7,23), # apply_class ComponentPrototype() -> has_apply_attribute ApplyAttribute ()
    		(23,24), #  has_apply_attribute ApplyAttribute () -> apply_attribute ApplyAttribute ()
    		(25,26), #  equation of apply attribute ApplyAttribute () -> left_expr
    		(26,24), #  left_expr -> apply_attribute ApplyAttribute ()
    		(25,27), #  equation of apply attribute ApplyAttribute () -> right_expr
    		(27,28), # right_expr --> term
        	(0,2), # matchmodel -> pairedwith
        	(2,1) # pairedwith -> applyModel
        ])
        
