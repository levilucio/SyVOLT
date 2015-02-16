from core.himesis import Himesis
import cPickle as pickle
import uuid

class Hlayer2rule3(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule layer2rule3.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer2rule3, self).__init__(name='Hlayer2rule3', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        # TODO Levi, need some help here because I don't know where does 
        # this value come from.
        self["mm__"] = pickle.loads("""(lp1
S'HimesisMM'
p2
a.""")
        
        self["name"] = """layer2rule3"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer2rule3')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer2rule3matchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer2rule3applymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer2rule3pairedwith2')
        
    	# match class Operation(layer2rule3class0) node
    	self.add_node()
    	self.vs[3]["name"] = """layer2rule3class0"""
        self.vs[3]["classtype"] = """Operation"""
        self.vs[3]["mm__"] = """Operation"""
        self.vs[3]["cardinality"] = """+"""
        #self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer2rule3class0')
    	# match_contains node for class Operation(layer2rule3class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        #self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer2rule3class0matchcontains4')
        
        
    	# apply class FunctionPrototype(layer2rule3class1) node
    	self.add_node()
    	self.vs[5]["name"] = """layer2rule3class1"""
        self.vs[5]["classtype"] = """FunctionPrototype"""
        self.vs[5]["mm__"] = """FunctionPrototype"""
        self.vs[5]["cardinality"] = """1"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer2rule3class1')
    	# apply_contains node for class FunctionPrototype(layer2rule3class1)
        self.add_node()
        self.vs[6]["mm__"] = """apply_contains"""
        #self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer2rule3class1applycontains6')
    	# apply class Argument(layer2rule3class2) node
    	self.add_node()
    	self.vs[7]["name"] = """layer2rule3class2"""
        self.vs[7]["classtype"] = """Argument"""
        self.vs[7]["mm__"] = """Argument"""
        self.vs[7]["cardinality"] = """1"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer2rule3class2')
    	# apply_contains node for class Argument(layer2rule3class2)
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        #self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer2rule3class2applycontains8')
    	# apply class VoidType(layer2rule3class3) node
    	self.add_node()
    	self.vs[9]["name"] = """layer2rule3class3"""
        self.vs[9]["classtype"] = """VoidType"""
        self.vs[9]["mm__"] = """VoidType"""
        self.vs[9]["cardinality"] = """1"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer2rule3class3')
    	# apply_contains node for class VoidType(layer2rule3class3)
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        #self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer2rule3class3applycontains10')
    	# apply class PointerType(layer2rule3class4) node
    	self.add_node()
    	self.vs[11]["name"] = """layer2rule3class4"""
        self.vs[11]["classtype"] = """PointerType"""
        self.vs[11]["mm__"] = """PointerType"""
        self.vs[11]["cardinality"] = """1"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer2rule3class4')
    	# apply_contains node for class PointerType(layer2rule3class4)
        self.add_node()
        self.vs[12]["mm__"] = """apply_contains"""
        #self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer2rule3class4applycontains12')
        
        
        
    	# apply association FunctionPrototype--arguments-->Argument node
    	self.add_node()
    	self.vs[13]["associationType"] = """arguments"""
        self.vs[13]["mm__"] = """directLink_T"""
        #self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer2rule3class1assoc13layer2rule3class2')
    	# apply association Argument--type-->PointerType node
    	self.add_node()
    	self.vs[14]["associationType"] = """type"""
        self.vs[14]["mm__"] = """directLink_T"""
        #self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer2rule3class2assoc14layer2rule3class4')
    	# apply association PointerType--baseType-->VoidType node
    	self.add_node()
    	self.vs[15]["associationType"] = """baseType"""
        self.vs[15]["mm__"] = """directLink_T"""
        #self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer2rule3class4assoc15layer2rule3class3')
        
    	# backward association Operation---->FunctionPrototype node
    	self.add_node()
    	self.vs[16]["type"] = """ruleDef"""
        self.vs[16]["mm__"] = """backward_link"""
        #self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer2rule3class0blink16layer2rule3class1')
        
        
        
        
    	# has apply attribute name(layer2rule3class2attribute1) node
    	self.add_node()
    	self.vs[17]["mm__"] = """hasAttribute_T"""
        #self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer2rule3class2attribute1')
    	# apply attribute name(layer2rule3class2attribute1) node
    	self.add_node()
    	self.vs[18]["name"] = """name"""
        self.vs[18]["mm__"] = """Attribute"""
        self.vs[18]["Type"] = """'String'"""
        #self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer2rule3class2attribute1')
    	# apply attribute equation name(layer2rule3class2attribute1) node
    	self.add_node()
    	self.vs[19]["name"] = """eq_"""
        self.vs[19]["mm__"] = """Equation"""
        #self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equationlayer2rule3class2attribute1')
    	# apply attribute equation left expr name(layer2rule3class2attribute1) node
    	self.add_node()
    	self.vs[20]["mm__"] = """leftExpr"""
        #self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExprlayer2rule3class2attribute1')
    	# apply attribute equation right expr name(layer2rule3class2attribute1) node
    	self.add_node()
    	self.vs[21]["mm__"] = """rightExpr"""
        #self.vs[21]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExprlayer2rule3class2attribute1')
    	# apply attribute atom name(layer2rule3class2attribute1) node
    	self.add_node()
    	self.vs[22]["name"] = """___id"""
        self.vs[22]["mm__"] = """Constant"""
        self.vs[22]["Type"] = """'String'"""
        #self.vs[22]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atomlayer2rule3class2attribute122')
        
        
        # Add the edges
        self.add_edges([
    		(0,4), # matchmodel -> match_contains
    		(4,3), # match_contains -> match_class Operation(layer2rule3class0)
    		(1,6), # applymodel -> apply_contains
    		(6,5), # apply_contains -> apply_class FunctionPrototype(layer2rule3class1)
    		(1,8), # applymodel -> apply_contains
    		(8,7), # apply_contains -> apply_class Argument(layer2rule3class2)
    		(1,10), # applymodel -> apply_contains
    		(10,9), # apply_contains -> apply_class VoidType(layer2rule3class3)
    		(1,12), # applymodel -> apply_contains
    		(12,11), # apply_contains -> apply_class PointerType(layer2rule3class4)
    		(5,13), # apply_class FunctionPrototype(layer2rule3class1) -> association arguments
    		(13,7), # association arguments  -> apply_class Argument(layer2rule3class2)
    		(7,14), # apply_class Argument(layer2rule3class2) -> association type
    		(14,11), # association type  -> apply_class PointerType(layer2rule3class4)
    		(11,15), # apply_class PointerType(layer2rule3class4) -> association baseType
    		(15,9), # association baseType  -> apply_class VoidType(layer2rule3class3)
    		(5,16), # apply_class FunctionPrototype(layer2rule3class1) -> backward_association
    		(16,3), #  backward_association -> apply_class Operation(layer2rule3class0)
    		(7,17), # apply_class Argument(layer2rule3class2) -> has_apply_attribute name (layer2rule3class2attribute1)
    		(17,18), #  has_apply_attribute name (layer2rule3class2attribute1) -> apply_attribute name (layer2rule3class2attribute1)
    		(19,20), #  equation of apply attribute name (layer2rule3class2attribute1) -> left_expr
    		(20,18), #  left_expr -> apply_attribute name (layer2rule3class2attribute1)
    		(19,21), #  equation of apply attribute name (layer2rule3class2attribute1) -> right_expr
    		(21,22), # right_expr --> term
        	(0,2), # matchmodel -> pairedwith
        	(2,1) # pairedwith -> applyModel
        ])
        
