from core.himesis import Himesis
import cPickle as pickle
import uuid

class Hlayer1rule15(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule layer1rule15.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer1rule15, self).__init__(name='Hlayer1rule15', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        # TODO Levi, need some help here because I don't know where does 
        # this value come from.
        self["mm__"] = pickle.loads("""(lp1
S'HimesisMM'
p2
a.""")
        
        self["name"] = """layer1rule15"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule15')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule15matchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule15applymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule15pairedwith2')
        
    	# match class Operation(layer1rule15class0) node
    	self.add_node()
    	self.vs[3]["name"] = """layer1rule15class0"""
        self.vs[3]["classtype"] = """Operation"""
        self.vs[3]["mm__"] = """Operation"""
        self.vs[3]["cardinality"] = """+"""
        #self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule15class0')
    	# match_contains node for class Operation(layer1rule15class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        #self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule15class0matchcontains4')
    	# match class OperationParameter(layer1rule15class1) node
    	self.add_node()
    	self.vs[5]["name"] = """layer1rule15class1"""
        self.vs[5]["classtype"] = """OperationParameter"""
        self.vs[5]["mm__"] = """OperationParameter"""
        self.vs[5]["cardinality"] = """+"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule15class1')
    	# match_contains node for class OperationParameter(layer1rule15class1)
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        #self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule15class1matchcontains6')
        
        
    	# apply class FunctionPrototype(layer1rule15class2) node
    	self.add_node()
    	self.vs[7]["name"] = """layer1rule15class2"""
        self.vs[7]["classtype"] = """FunctionPrototype"""
        self.vs[7]["mm__"] = """FunctionPrototype"""
        self.vs[7]["cardinality"] = """1"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule15class2')
    	# apply_contains node for class FunctionPrototype(layer1rule15class2)
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        #self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule15class2applycontains8')
    	# apply class Argument(layer1rule15class3) node
    	self.add_node()
    	self.vs[9]["name"] = """layer1rule15class3"""
        self.vs[9]["classtype"] = """Argument"""
        self.vs[9]["mm__"] = """Argument"""
        self.vs[9]["cardinality"] = """1"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule15class3')
    	# apply_contains node for class Argument(layer1rule15class3)
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        #self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule15class3applycontains10')
        
        
    	# match association Operation--parameters-->OperationParameter node
    	self.add_node()
    	self.vs[11]["associationType"] = """parameters"""
        self.vs[11]["mm__"] = """directLink_S"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule15class0assoc11layer1rule15class1')
        
    	# apply association FunctionPrototype--arguments-->Argument node
    	self.add_node()
    	self.vs[12]["associationType"] = """arguments"""
        self.vs[12]["mm__"] = """directLink_T"""
        #self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule15class2assoc12layer1rule15class3')
        
    	# backward association Operation---->FunctionPrototype node
    	self.add_node()
    	self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["mm__"] = """backward_link"""
        #self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule15class0blink13layer1rule15class2')
        
        
    	# has match attribute name(layer1rule15class1attribute0) node
    	self.add_node()
    	self.vs[14]["mm__"] = """hasAttribute_S"""
        #self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer1rule15class1attribute0')
    	# match attribute name(layer1rule15class1attribute0) node
    	self.add_node()
    	self.vs[15]["name"] = """name"""
        self.vs[15]["mm__"] = """Attribute"""
        self.vs[15]["Type"] = """'String'"""
        #self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule15class1attribute0')
        
        
    	# has apply attribute name(layer1rule15class3attribute1) node
    	self.add_node()
    	self.vs[16]["mm__"] = """hasAttribute_T"""
        #self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer1rule15class3attribute1')
    	# apply attribute name(layer1rule15class3attribute1) node
    	self.add_node()
    	self.vs[17]["name"] = """name"""
        self.vs[17]["mm__"] = """Attribute"""
        self.vs[17]["Type"] = """'String'"""
        #self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule15class3attribute1')
    	# apply attribute equation name(layer1rule15class3attribute1) node
    	self.add_node()
    	self.vs[18]["name"] = """eq_"""
        self.vs[18]["mm__"] = """Equation"""
        #self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equationlayer1rule15class3attribute1')
    	# apply attribute equation left expr name(layer1rule15class3attribute1) node
    	self.add_node()
    	self.vs[19]["mm__"] = """leftExpr"""
        #self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExprlayer1rule15class3attribute1')
    	# apply attribute equation right expr name(layer1rule15class3attribute1) node
    	self.add_node()
    	self.vs[20]["mm__"] = """rightExpr"""
        #self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExprlayer1rule15class3attribute1')
        
        
        # Add the edges
        self.add_edges([
    		(0,4), # matchmodel -> match_contains
    		(4,3), # match_contains -> match_class Operation(layer1rule15class0)
    		(0,6), # matchmodel -> match_contains
    		(6,5), # match_contains -> match_class OperationParameter(layer1rule15class1)
    		(1,8), # applymodel -> apply_contains
    		(8,7), # apply_contains -> apply_class FunctionPrototype(layer1rule15class2)
    		(1,10), # applymodel -> apply_contains
    		(10,9), # apply_contains -> apply_class Argument(layer1rule15class3)
    		(3,11), # match_class Operation(layer1rule15class0) -> association parameters
    		(11,5), # association parameters  -> match_class OperationParameter(layer1rule15class1)
    		(7,12), # apply_class FunctionPrototype(layer1rule15class2) -> association arguments
    		(12,9), # association arguments  -> apply_class Argument(layer1rule15class3)
    		(7,13), # apply_class FunctionPrototype(layer1rule15class2) -> backward_association
    		(13,3), #  backward_association -> apply_class Operation(layer1rule15class0)
    		(5,14), # match_class OperationParameter(layer1rule15class1) -> has_match_attribute name (layer1rule15class1attribute0)
    		(14,15), #  has_match_attribute name (layer1rule15class1attribute0) -> match_attribute name (layer1rule15class1attribute0)
    		(9,16), # apply_class Argument(layer1rule15class3) -> has_apply_attribute name (layer1rule15class3attribute1)
    		(16,17), #  has_apply_attribute name (layer1rule15class3attribute1) -> apply_attribute name (layer1rule15class3attribute1)
    		(18,19), #  equation of apply attribute name (layer1rule15class3attribute1) -> left_expr
    		(19,17), #  left_expr -> apply_attribute name (layer1rule15class3attribute1)
    		(18,20), #  equation of apply attribute name (layer1rule15class3attribute1) -> right_expr
    		(20,15), # right_expr --> term
        	(0,2), # matchmodel -> pairedwith
        	(2,1) # pairedwith -> applyModel
        ])
        
