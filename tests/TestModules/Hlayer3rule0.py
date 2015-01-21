from core.himesis import Himesis
import cPickle as pickle
import uuid

class Hlayer3rule0(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule layer3rule0.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer3rule0, self).__init__(name='Hlayer3rule0', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        # TODO Levi, need some help here because I don't know where does 
        # this value come from.
        self["mm__"] = pickle.loads("""(lp1
S'HimesisMM'
p2
a.""")
        
        self["name"] = """layer3rule0"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule0')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule0matchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule0applymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule0pairedwith2')
        
    	# match class ImplementationModule(layer3rule0class0) node
    	self.add_node()
    	self.vs[3]["name"] = """layer3rule0class0"""
        self.vs[3]["classtype"] = """ImplementationModule"""
        self.vs[3]["mm__"] = """ImplementationModule"""
        self.vs[3]["cardinality"] = """+"""
        #self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule0class0')
    	# match_contains node for class ImplementationModule(layer3rule0class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        #self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule0class0matchcontains4')
    	# match class Function(layer3rule0class1) node
    	self.add_node()
    	self.vs[5]["name"] = """layer3rule0class1"""
        self.vs[5]["classtype"] = """Function"""
        self.vs[5]["mm__"] = """Function"""
        self.vs[5]["cardinality"] = """+"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule0class1')
    	# match_contains node for class Function(layer3rule0class1)
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        #self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule0class1matchcontains6')
    	# match class Int32Type(layer3rule0class2) node
    	self.add_node()
    	self.vs[7]["name"] = """layer3rule0class2"""
        self.vs[7]["classtype"] = """Int32Type"""
        self.vs[7]["mm__"] = """Int32Type"""
        self.vs[7]["cardinality"] = """+"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule0class2')
    	# match_contains node for class Int32Type(layer3rule0class2)
        self.add_node()
        self.vs[8]["mm__"] = """match_contains"""
        #self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule0class2matchcontains8')
        
        
    	# apply class ImplementationModule(layer3rule0class3) node
    	self.add_node()
    	self.vs[9]["name"] = """layer3rule0class3"""
        self.vs[9]["classtype"] = """ImplementationModule"""
        self.vs[9]["mm__"] = """ImplementationModule"""
        self.vs[9]["cardinality"] = """1"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule0class3')
    	# apply_contains node for class ImplementationModule(layer3rule0class3)
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        #self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule0class3applycontains10')
    	# apply class FunctionPrototype(layer3rule0class4) node
    	self.add_node()
    	self.vs[11]["name"] = """layer3rule0class4"""
        self.vs[11]["classtype"] = """FunctionPrototype"""
        self.vs[11]["mm__"] = """FunctionPrototype"""
        self.vs[11]["cardinality"] = """1"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule0class4')
    	# apply_contains node for class FunctionPrototype(layer3rule0class4)
        self.add_node()
        self.vs[12]["mm__"] = """apply_contains"""
        #self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule0class4applycontains12')
    	# apply class VoidType(layer3rule0class5) node
    	self.add_node()
    	self.vs[13]["name"] = """layer3rule0class5"""
        self.vs[13]["classtype"] = """VoidType"""
        self.vs[13]["mm__"] = """VoidType"""
        self.vs[13]["cardinality"] = """1"""
        #self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule0class5')
    	# apply_contains node for class VoidType(layer3rule0class5)
        self.add_node()
        self.vs[14]["mm__"] = """apply_contains"""
        #self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule0class5applycontains14')
        
        
    	# match association ImplementationModule--contents-->Function node
    	self.add_node()
    	self.vs[15]["associationType"] = """contents"""
        self.vs[15]["mm__"] = """directLink_S"""
        #self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule0class0assoc15layer3rule0class1')
    	# match association Function--type-->Int32Type node
    	self.add_node()
    	self.vs[16]["associationType"] = """type"""
        self.vs[16]["mm__"] = """directLink_S"""
        #self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule0class1assoc16layer3rule0class2')
        
    	# apply association ImplementationModule--contents-->FunctionPrototype node
    	self.add_node()
    	self.vs[17]["associationType"] = """contents"""
        self.vs[17]["mm__"] = """directLink_T"""
        #self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule0class3assoc17layer3rule0class4')
    	# apply association FunctionPrototype--type-->VoidType node
    	self.add_node()
    	self.vs[18]["associationType"] = """type"""
        self.vs[18]["mm__"] = """directLink_T"""
        #self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule0class4assoc18layer3rule0class5')
        
    	# backward association ImplementationModule---->ImplementationModule node
    	self.add_node()
    	self.vs[19]["type"] = """ruleDef"""
        self.vs[19]["mm__"] = """backward_link"""
        #self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule0class0blink19layer3rule0class3')
        
        
    	# has match attribute name(layer3rule0class0attribute0) node
    	self.add_node()
    	self.vs[20]["mm__"] = """hasAttribute_S"""
        #self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer3rule0class0attribute0')
    	# match attribute name(layer3rule0class0attribute0) node
    	self.add_node()
    	self.vs[21]["name"] = """name"""
        self.vs[21]["mm__"] = """Attribute"""
        self.vs[21]["Type"] = """'String'"""
        #self.vs[21]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule0class0attribute0')
    	# has match attribute name(layer3rule0class1attribute0) node
    	self.add_node()
    	self.vs[22]["mm__"] = """hasAttribute_S"""
        #self.vs[22]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer3rule0class1attribute0')
    	# match attribute name(layer3rule0class1attribute0) node
    	self.add_node()
    	self.vs[23]["name"] = """name"""
        self.vs[23]["mm__"] = """Attribute"""
        self.vs[23]["Type"] = """'String'"""
        #self.vs[23]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule0class1attribute0')
    	# match attribute equation name(layer3rule0class1attribute0) node
    	self.add_node()
    	self.vs[24]["name"] = """eq_"""
        self.vs[24]["mm__"] = """Equation"""
        #self.vs[24]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equationlayer3rule0class1attribute0')
    	# match attribute equation left expr name(layer3rule0class1attribute0) node
    	self.add_node()
    	self.vs[25]["name"] = """leftExpr"""
        #self.vs[25]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExprlayer3rule0class1attribute0')
    	# match attribute equation right expr name(layer3rule0class1attribute0) node
    	self.add_node()
    	self.vs[26]["name"] = """rightExpr"""
        #self.vs[26]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExprlayer3rule0class1attribute0')
    	# apply attribute atom name(layer3rule0class1attribute0) node
    	self.add_node()
    	self.vs[27]["name"] = """main"""
        self.vs[27]["mm__"] = """Constant"""
        self.vs[27]["Type"] = """'String'"""
        #self.vs[27]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atomlayer3rule0class1attribute027')
        
        
    	# has apply attribute name(layer3rule0class4attribute0) node
    	self.add_node()
    	self.vs[28]["mm__"] = """hasAttribute_T"""
        #self.vs[28]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer3rule0class4attribute0')
    	# apply attribute name(layer3rule0class4attribute0) node
    	self.add_node()
    	self.vs[29]["name"] = """name"""
        self.vs[29]["mm__"] = """Attribute"""
        self.vs[29]["Type"] = """'String'"""
        #self.vs[29]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule0class4attribute0')
    	# apply attribute equation name(layer3rule0class4attribute0) node
    	self.add_node()
    	self.vs[30]["name"] = """eq_"""
        self.vs[30]["mm__"] = """Equation"""
        #self.vs[30]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equationlayer3rule0class4attribute0')
    	# apply attribute equation left expr name(layer3rule0class4attribute0) node
    	self.add_node()
    	self.vs[31]["name"] = """leftExpr"""
        #self.vs[31]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExprlayer3rule0class4attribute0')
    	# apply attribute equation right expr name(layer3rule0class4attribute0) node
    	self.add_node()
    	self.vs[32]["name"] = """rightExpr"""
        #self.vs[32]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExprlayer3rule0class4attribute0')
    	# attribute concat name(layer3rule0class4attribute0) node
    	self.add_node()
    	self.vs[33]["name"] = """Concatlayer3rule0class4attribute033"""
        self.vs[33]["mm__"] = """Concat"""
        self.vs[33]["Type"] = """'String'"""
        #self.vs[33]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concatlayer3rule0class4attribute033')
    	# apply attribute concat has left args name(layer3rule0class4attribute0) node
        self.add_node()
    	self.vs[34]["mm__"] = """hasArgs"""
        #self.vs[34]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgslayer3rule0class4attribute034')
    	# apply attribute concat has right args name(layer3rule0class4attribute0) node
        self.add_node()
    	self.vs[35]["mm__"] = """hasArgs"""
        #self.vs[35]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgslayer3rule0class4attribute035')
    	# apply attribute atom name(layer3rule0class4attribute0) node
    	self.add_node()
    	self.vs[36]["name"] = """_blockexpr_main_2"""
        self.vs[36]["mm__"] = """Constant"""
        self.vs[36]["Type"] = """'String'"""
        #self.vs[36]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atomlayer3rule0class4attribute036')
        
        
        # Add the edges
        self.add_edges([
    		(0,4), # matchmodel -> match_contains
    		(4,3), # match_contains -> match_class ImplementationModule(layer3rule0class0)
    		(0,6), # matchmodel -> match_contains
    		(6,5), # match_contains -> match_class Function(layer3rule0class1)
    		(0,8), # matchmodel -> match_contains
    		(8,7), # match_contains -> match_class Int32Type(layer3rule0class2)
    		(1,10), # applymodel -> apply_contains
    		(10,9), # apply_contains -> apply_class ImplementationModule(layer3rule0class3)
    		(1,12), # applymodel -> apply_contains
    		(12,11), # apply_contains -> apply_class FunctionPrototype(layer3rule0class4)
    		(1,14), # applymodel -> apply_contains
    		(14,13), # apply_contains -> apply_class VoidType(layer3rule0class5)
    		(3,15), # match_class ImplementationModule(layer3rule0class0) -> association contents
    		(15,5), # association contents  -> match_class Function(layer3rule0class1)
    		(5,16), # match_class Function(layer3rule0class1) -> association type
    		(16,7), # association type  -> match_class Int32Type(layer3rule0class2)
    		(9,17), # apply_class ImplementationModule(layer3rule0class3) -> association contents
    		(17,11), # association contents  -> apply_class FunctionPrototype(layer3rule0class4)
    		(11,18), # apply_class FunctionPrototype(layer3rule0class4) -> association type
    		(18,13), # association type  -> apply_class VoidType(layer3rule0class5)
    		(9,19), # apply_class ImplementationModule(layer3rule0class3) -> backward_association
    		(19,3), #  backward_association -> apply_class ImplementationModule(layer3rule0class0)
    		(3,20), # match_class ImplementationModule(layer3rule0class0) -> has_match_attribute name (layer3rule0class0attribute0)
    		(20,21), #  has_match_attribute name (layer3rule0class0attribute0) -> match_attribute name (layer3rule0class0attribute0)
    		(5,22), # match_class Function(layer3rule0class1) -> has_match_attribute name (layer3rule0class1attribute0)
    		(22,23), #  has_match_attribute name (layer3rule0class1attribute0) -> match_attribute name (layer3rule0class1attribute0)
	    	(24,25), #  equation of match attribute name (layer3rule0class1attribute0) -> left_expr
    		(25,23), #  left_expr -> match_attribute name (layer3rule0class1attribute0)
    		(24,26), #  equation of match attribute name (layer3rule0class1attribute0) -> right_expr
    		(26,27), # right_expr --> term
    		(11,28), # apply_class FunctionPrototype(layer3rule0class4) -> has_apply_attribute name (layer3rule0class4attribute0)
    		(28,29), #  has_apply_attribute name (layer3rule0class4attribute0) -> apply_attribute name (layer3rule0class4attribute0)
    		(30,31), #  equation of apply attribute name (layer3rule0class4attribute0) -> left_expr
    		(31,29), #  left_expr -> apply_attribute name (layer3rule0class4attribute0)
    		(30,32), #  equation of apply attribute name (layer3rule0class4attribute0) -> right_expr
    		(33,34), #  apply attribute concat name (layer3rule0class4attribute0) -> left has_args  
    		(34,21), #  left has_args -> term
    		(33,35), #  apply attribute concat name (layer3rule0class4attribute0) -> right has_args  
    		(35,36), #  right has_args -> term
    		(32,33), # right_expr --> term
        	(0,2), # matchmodel -> pairedwith
        	(2,1) # pairedwith -> applyModel
        ])
        
