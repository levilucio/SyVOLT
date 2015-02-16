from core.himesis import Himesis
import cPickle as pickle
import uuid

class Hlayer3rule5(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule layer3rule5.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer3rule5, self).__init__(name='Hlayer3rule5', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        # TODO Levi, need some help here because I don't know where does 
        # this value come from.
        self["mm__"] = pickle.loads("""(lp1
S'HimesisMM'
p2
a.""")
        
        self["name"] = """layer3rule5"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule5')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule5matchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule5applymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule5pairedwith2')
        
    	# match class ImplementationModule(layer3rule5class0) node
    	self.add_node()
    	self.vs[3]["name"] = """layer3rule5class0"""
        self.vs[3]["classtype"] = """ImplementationModule"""
        self.vs[3]["mm__"] = """ImplementationModule"""
        self.vs[3]["cardinality"] = """+"""
        #self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule5class0')
    	# match_contains node for class ImplementationModule(layer3rule5class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        #self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule5class0matchcontains4')
    	# match class TestCase(layer3rule5class1) node
    	self.add_node()
    	self.vs[5]["name"] = """layer3rule5class1"""
        self.vs[5]["classtype"] = """TestCase"""
        self.vs[5]["mm__"] = """TestCase"""
        self.vs[5]["cardinality"] = """+"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule5class1')
    	# match_contains node for class TestCase(layer3rule5class1)
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        #self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule5class1matchcontains6')
        
        
    	# apply class ImplementationModule(layer3rule5class2) node
    	self.add_node()
    	self.vs[7]["name"] = """layer3rule5class2"""
        self.vs[7]["classtype"] = """ImplementationModule"""
        self.vs[7]["mm__"] = """ImplementationModule"""
        self.vs[7]["cardinality"] = """1"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule5class2')
    	# apply_contains node for class ImplementationModule(layer3rule5class2)
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        #self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule5class2applycontains8')
    	# apply class FunctionPrototype(layer3rule5class3) node
    	self.add_node()
    	self.vs[9]["name"] = """layer3rule5class3"""
        self.vs[9]["classtype"] = """FunctionPrototype"""
        self.vs[9]["mm__"] = """FunctionPrototype"""
        self.vs[9]["cardinality"] = """1"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule5class3')
    	# apply_contains node for class FunctionPrototype(layer3rule5class3)
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        #self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule5class3applycontains10')
    	# apply class VoidType(layer3rule5class4) node
    	self.add_node()
    	self.vs[11]["name"] = """layer3rule5class4"""
        self.vs[11]["classtype"] = """VoidType"""
        self.vs[11]["mm__"] = """VoidType"""
        self.vs[11]["cardinality"] = """1"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule5class4')
    	# apply_contains node for class VoidType(layer3rule5class4)
        self.add_node()
        self.vs[12]["mm__"] = """apply_contains"""
        #self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule5class4applycontains12')
        
        
    	# match association ImplementationModule--contents-->TestCase node
    	self.add_node()
    	self.vs[13]["associationType"] = """contents"""
        self.vs[13]["mm__"] = """directLink_S"""
        #self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule5class0assoc13layer3rule5class1')
        
    	# apply association ImplementationModule--contents-->FunctionPrototype node
    	self.add_node()
    	self.vs[14]["associationType"] = """contents"""
        self.vs[14]["mm__"] = """directLink_T"""
        #self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule5class2assoc14layer3rule5class3')
    	# apply association FunctionPrototype--type-->VoidType node
    	self.add_node()
    	self.vs[15]["associationType"] = """type"""
        self.vs[15]["mm__"] = """directLink_T"""
        #self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule5class3assoc15layer3rule5class4')
        
    	# backward association ImplementationModule---->ImplementationModule node
    	self.add_node()
    	self.vs[16]["type"] = """ruleDef"""
        self.vs[16]["mm__"] = """backward_link"""
        #self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule5class0blink16layer3rule5class2')
        
        
    	# has match attribute name(layer3rule5class0attribute0) node
    	self.add_node()
    	self.vs[17]["mm__"] = """hasAttribute_S"""
        #self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer3rule5class0attribute0')
    	# match attribute name(layer3rule5class0attribute0) node
    	self.add_node()
    	self.vs[18]["name"] = """name"""
        self.vs[18]["mm__"] = """Attribute"""
        self.vs[18]["Type"] = """'String'"""
        #self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule5class0attribute0')
    	# has match attribute name(layer3rule5class1attribute0) node
    	self.add_node()
    	self.vs[19]["mm__"] = """hasAttribute_S"""
        #self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer3rule5class1attribute0')
    	# match attribute name(layer3rule5class1attribute0) node
    	self.add_node()
    	self.vs[20]["name"] = """name"""
        self.vs[20]["mm__"] = """Attribute"""
        self.vs[20]["Type"] = """'String'"""
        #self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule5class1attribute0')
        
        
    	# has apply attribute name(layer3rule5class3attribute0) node
    	self.add_node()
    	self.vs[21]["mm__"] = """hasAttribute_T"""
        #self.vs[21]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer3rule5class3attribute0')
    	# apply attribute name(layer3rule5class3attribute0) node
    	self.add_node()
    	self.vs[22]["name"] = """name"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["Type"] = """'String'"""
        #self.vs[22]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule5class3attribute0')
    	# apply attribute equation name(layer3rule5class3attribute0) node
    	self.add_node()
    	self.vs[23]["name"] = """eq_"""
        self.vs[23]["mm__"] = """Equation"""
        #self.vs[23]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equationlayer3rule5class3attribute0')
    	# apply attribute equation left expr name(layer3rule5class3attribute0) node
    	self.add_node()
    	self.vs[24]["mm__"] = """leftExpr"""
        #self.vs[24]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExprlayer3rule5class3attribute0')
    	# apply attribute equation right expr name(layer3rule5class3attribute0) node
    	self.add_node()
    	self.vs[25]["mm__"] = """rightExpr"""
        #self.vs[25]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExprlayer3rule5class3attribute0')
    	# attribute concat name(layer3rule5class3attribute0) node
    	self.add_node()
    	self.vs[26]["name"] = """Concatlayer3rule5class3attribute026"""
        self.vs[26]["mm__"] = """Concat"""
        self.vs[26]["Type"] = """'String'"""
        #self.vs[26]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concatlayer3rule5class3attribute026')
    	# apply attribute concat has left args name(layer3rule5class3attribute0) node
        self.add_node()
    	self.vs[27]["mm__"] = """hasArgs"""
        #self.vs[27]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgslayer3rule5class3attribute027')
    	# apply attribute concat has right args name(layer3rule5class3attribute0) node
        self.add_node()
    	self.vs[28]["mm__"] = """hasArgs"""
        #self.vs[28]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgslayer3rule5class3attribute028')
    	# attribute concat name(layer3rule5class3attribute0) node
    	self.add_node()
    	self.vs[29]["name"] = """Concatlayer3rule5class3attribute029"""
        self.vs[29]["mm__"] = """Concat"""
        self.vs[29]["Type"] = """'String'"""
        #self.vs[29]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concatlayer3rule5class3attribute029')
    	# apply attribute concat has left args name(layer3rule5class3attribute0) node
        self.add_node()
    	self.vs[30]["mm__"] = """hasArgs"""
        #self.vs[30]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgslayer3rule5class3attribute030')
    	# apply attribute concat has right args name(layer3rule5class3attribute0) node
        self.add_node()
    	self.vs[31]["mm__"] = """hasArgs"""
        #self.vs[31]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgslayer3rule5class3attribute031')
    	# apply attribute atom name(layer3rule5class3attribute0) node
    	self.add_node()
    	self.vs[32]["name"] = """_"""
        self.vs[32]["mm__"] = """Constant"""
        self.vs[32]["Type"] = """'String'"""
        #self.vs[32]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atomlayer3rule5class3attribute032')
        
        
        # Add the edges
        self.add_edges([
    		(0,4), # matchmodel -> match_contains
    		(4,3), # match_contains -> match_class ImplementationModule(layer3rule5class0)
    		(0,6), # matchmodel -> match_contains
    		(6,5), # match_contains -> match_class TestCase(layer3rule5class1)
    		(1,8), # applymodel -> apply_contains
    		(8,7), # apply_contains -> apply_class ImplementationModule(layer3rule5class2)
    		(1,10), # applymodel -> apply_contains
    		(10,9), # apply_contains -> apply_class FunctionPrototype(layer3rule5class3)
    		(1,12), # applymodel -> apply_contains
    		(12,11), # apply_contains -> apply_class VoidType(layer3rule5class4)
    		(3,13), # match_class ImplementationModule(layer3rule5class0) -> association contents
    		(13,5), # association contents  -> match_class TestCase(layer3rule5class1)
    		(7,14), # apply_class ImplementationModule(layer3rule5class2) -> association contents
    		(14,9), # association contents  -> apply_class FunctionPrototype(layer3rule5class3)
    		(9,15), # apply_class FunctionPrototype(layer3rule5class3) -> association type
    		(15,11), # association type  -> apply_class VoidType(layer3rule5class4)
    		(7,16), # apply_class ImplementationModule(layer3rule5class2) -> backward_association
    		(16,3), #  backward_association -> apply_class ImplementationModule(layer3rule5class0)
    		(3,17), # match_class ImplementationModule(layer3rule5class0) -> has_match_attribute name (layer3rule5class0attribute0)
    		(17,18), #  has_match_attribute name (layer3rule5class0attribute0) -> match_attribute name (layer3rule5class0attribute0)
    		(5,19), # match_class TestCase(layer3rule5class1) -> has_match_attribute name (layer3rule5class1attribute0)
    		(19,20), #  has_match_attribute name (layer3rule5class1attribute0) -> match_attribute name (layer3rule5class1attribute0)
    		(9,21), # apply_class FunctionPrototype(layer3rule5class3) -> has_apply_attribute name (layer3rule5class3attribute0)
    		(21,22), #  has_apply_attribute name (layer3rule5class3attribute0) -> apply_attribute name (layer3rule5class3attribute0)
    		(23,24), #  equation of apply attribute name (layer3rule5class3attribute0) -> left_expr
    		(24,22), #  left_expr -> apply_attribute name (layer3rule5class3attribute0)
    		(23,25), #  equation of apply attribute name (layer3rule5class3attribute0) -> right_expr
    		(29,30), #  apply attribute concat name (layer3rule5class3attribute0) -> left has_args  
    		(30,32), #  left has_args -> term
    		(29,31), #  apply attribute concat name (layer3rule5class3attribute0) -> right has_args  
    		(31,20), #  right has_args -> term
    		(26,27), #  apply attribute concat name (layer3rule5class3attribute0) -> left has_args  
    		(27,18), #  left has_args -> term
    		(26,28), #  apply attribute concat name (layer3rule5class3attribute0) -> right has_args  
    		(28,29), #  right has_args -> term
    		(25,26), # right_expr --> term
        	(0,2), # matchmodel -> pairedwith
        	(2,1) # pairedwith -> applyModel
        ])
        
