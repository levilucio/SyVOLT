from core.himesis import Himesis
import cPickle as pickle
import uuid

class Hlayer3rule2(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule layer3rule2.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer3rule2, self).__init__(name='Hlayer3rule2', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        # TODO Levi, need some help here because I don't know where does 
        # this value come from.
        self["mm__"] = pickle.loads("""(lp1
S'HimesisMM'
p2
a.""")
        
        self["name"] = """layer3rule2"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule2')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule2matchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule2applymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule2pairedwith2')
        
    	# match class ImplementationModule(layer3rule2class0) node
    	self.add_node()
    	self.vs[3]["name"] = """layer3rule2class0"""
        self.vs[3]["classtype"] = """ImplementationModule"""
        self.vs[3]["mm__"] = """ImplementationModule"""
        self.vs[3]["cardinality"] = """+"""
        #self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule2class0')
    	# match_contains node for class ImplementationModule(layer3rule2class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        #self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule2class0matchcontains4')
    	# match class InstanceConfiguration(layer3rule2class1) node
    	self.add_node()
    	self.vs[5]["name"] = """layer3rule2class1"""
        self.vs[5]["classtype"] = """InstanceConfiguration"""
        self.vs[5]["mm__"] = """InstanceConfiguration"""
        self.vs[5]["cardinality"] = """+"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule2class1')
    	# match_contains node for class InstanceConfiguration(layer3rule2class1)
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        #self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule2class1matchcontains6')
    	# match class ComponentInstance(layer3rule2class2) node
    	self.add_node()
    	self.vs[7]["name"] = """layer3rule2class2"""
        self.vs[7]["classtype"] = """ComponentInstance"""
        self.vs[7]["mm__"] = """ComponentInstance"""
        self.vs[7]["cardinality"] = """+"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule2class2')
    	# match_contains node for class ComponentInstance(layer3rule2class2)
        self.add_node()
        self.vs[8]["mm__"] = """match_contains"""
        #self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule2class2matchcontains8')
        
        
    	# apply class ImplementationModule(layer3rule2class3) node
    	self.add_node()
    	self.vs[9]["name"] = """layer3rule2class3"""
        self.vs[9]["classtype"] = """ImplementationModule"""
        self.vs[9]["mm__"] = """ImplementationModule"""
        self.vs[9]["cardinality"] = """1"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule2class3')
    	# apply_contains node for class ImplementationModule(layer3rule2class3)
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        #self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule2class3applycontains10')
    	# apply class FunctionPrototype(layer3rule2class4) node
    	self.add_node()
    	self.vs[11]["name"] = """layer3rule2class4"""
        self.vs[11]["classtype"] = """FunctionPrototype"""
        self.vs[11]["mm__"] = """FunctionPrototype"""
        self.vs[11]["cardinality"] = """1"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule2class4')
    	# apply_contains node for class FunctionPrototype(layer3rule2class4)
        self.add_node()
        self.vs[12]["mm__"] = """apply_contains"""
        #self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule2class4applycontains12')
    	# apply class VoidType(layer3rule2class5) node
    	self.add_node()
    	self.vs[13]["name"] = """layer3rule2class5"""
        self.vs[13]["classtype"] = """VoidType"""
        self.vs[13]["mm__"] = """VoidType"""
        self.vs[13]["cardinality"] = """1"""
        #self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule2class5')
    	# apply_contains node for class VoidType(layer3rule2class5)
        self.add_node()
        self.vs[14]["mm__"] = """apply_contains"""
        #self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule2class5applycontains14')
        
        
    	# match association ImplementationModule--contents-->InstanceConfiguration node
    	self.add_node()
    	self.vs[15]["associationType"] = """contents"""
        self.vs[15]["mm__"] = """directLink_S"""
        #self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule2class0assoc15layer3rule2class1')
    	# match association InstanceConfiguration--contents-->ComponentInstance node
    	self.add_node()
    	self.vs[16]["associationType"] = """contents"""
        self.vs[16]["mm__"] = """directLink_S"""
        #self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule2class1assoc16layer3rule2class2')
        
    	# apply association ImplementationModule--contents-->FunctionPrototype node
    	self.add_node()
    	self.vs[17]["associationType"] = """contents"""
        self.vs[17]["mm__"] = """directLink_T"""
        #self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule2class3assoc17layer3rule2class4')
    	# apply association FunctionPrototype--type-->VoidType node
    	self.add_node()
    	self.vs[18]["associationType"] = """type"""
        self.vs[18]["mm__"] = """directLink_T"""
        #self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule2class4assoc18layer3rule2class5')
        
    	# backward association ImplementationModule---->ImplementationModule node
    	self.add_node()
    	self.vs[19]["type"] = """ruleDef"""
        self.vs[19]["mm__"] = """backward_link"""
        #self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule2class0blink19layer3rule2class3')
        
        
    	# has match attribute name(layer3rule2class0attribute0) node
    	self.add_node()
    	self.vs[20]["mm__"] = """hasAttribute_S"""
        #self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer3rule2class0attribute0')
    	# match attribute name(layer3rule2class0attribute0) node
    	self.add_node()
    	self.vs[21]["name"] = """name"""
        self.vs[21]["mm__"] = """Attribute"""
        self.vs[21]["Type"] = """'String'"""
        #self.vs[21]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule2class0attribute0')
    	# has match attribute name(layer3rule2class1attribute0) node
    	self.add_node()
    	self.vs[22]["mm__"] = """hasAttribute_S"""
        #self.vs[22]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer3rule2class1attribute0')
    	# match attribute name(layer3rule2class1attribute0) node
    	self.add_node()
    	self.vs[23]["name"] = """name"""
        self.vs[23]["mm__"] = """Attribute"""
        self.vs[23]["Type"] = """'String'"""
        #self.vs[23]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule2class1attribute0')
    	# has match attribute name(layer3rule2class2attribute0) node
    	self.add_node()
    	self.vs[24]["mm__"] = """hasAttribute_S"""
        #self.vs[24]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer3rule2class2attribute0')
    	# match attribute name(layer3rule2class2attribute0) node
    	self.add_node()
    	self.vs[25]["name"] = """name"""
        self.vs[25]["mm__"] = """Attribute"""
        self.vs[25]["Type"] = """'String'"""
        #self.vs[25]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule2class2attribute0')
        
        
    	# has apply attribute name(layer3rule2class4attribute0) node
    	self.add_node()
    	self.vs[26]["mm__"] = """hasAttribute_T"""
        #self.vs[26]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer3rule2class4attribute0')
    	# apply attribute name(layer3rule2class4attribute0) node
    	self.add_node()
    	self.vs[27]["name"] = """name"""
        self.vs[27]["mm__"] = """Attribute"""
        self.vs[27]["Type"] = """'String'"""
        #self.vs[27]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule2class4attribute0')
    	# apply attribute equation name(layer3rule2class4attribute0) node
    	self.add_node()
    	self.vs[28]["name"] = """eq_"""
        self.vs[28]["mm__"] = """Equation"""
        #self.vs[28]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equationlayer3rule2class4attribute0')
    	# apply attribute equation left expr name(layer3rule2class4attribute0) node
    	self.add_node()
    	self.vs[29]["mm__"] = """leftExpr"""
        #self.vs[29]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExprlayer3rule2class4attribute0')
    	# apply attribute equation right expr name(layer3rule2class4attribute0) node
    	self.add_node()
    	self.vs[30]["mm__"] = """rightExpr"""
        #self.vs[30]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExprlayer3rule2class4attribute0')
    	# attribute concat name(layer3rule2class4attribute0) node
    	self.add_node()
    	self.vs[31]["name"] = """Concatlayer3rule2class4attribute031"""
        self.vs[31]["mm__"] = """Concat"""
        self.vs[31]["Type"] = """'String'"""
        #self.vs[31]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concatlayer3rule2class4attribute031')
    	# apply attribute concat has left args name(layer3rule2class4attribute0) node
        self.add_node()
    	self.vs[32]["mm__"] = """hasArgs"""
        #self.vs[32]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgslayer3rule2class4attribute032')
    	# apply attribute concat has right args name(layer3rule2class4attribute0) node
        self.add_node()
    	self.vs[33]["mm__"] = """hasArgs"""
        #self.vs[33]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgslayer3rule2class4attribute033')
    	# attribute concat name(layer3rule2class4attribute0) node
    	self.add_node()
    	self.vs[34]["name"] = """Concatlayer3rule2class4attribute034"""
        self.vs[34]["mm__"] = """Concat"""
        self.vs[34]["Type"] = """'String'"""
        #self.vs[34]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concatlayer3rule2class4attribute034')
    	# apply attribute concat has left args name(layer3rule2class4attribute0) node
        self.add_node()
    	self.vs[35]["mm__"] = """hasArgs"""
        #self.vs[35]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgslayer3rule2class4attribute035')
    	# apply attribute concat has right args name(layer3rule2class4attribute0) node
        self.add_node()
    	self.vs[36]["mm__"] = """hasArgs"""
        #self.vs[36]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgslayer3rule2class4attribute036')
    	# apply attribute atom name(layer3rule2class4attribute0) node
    	self.add_node()
    	self.vs[37]["name"] = """_"""
        self.vs[37]["mm__"] = """Constant"""
        self.vs[37]["Type"] = """'String'"""
        #self.vs[37]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atomlayer3rule2class4attribute037')
    	# attribute concat name(layer3rule2class4attribute0) node
    	self.add_node()
    	self.vs[38]["name"] = """Concatlayer3rule2class4attribute038"""
        self.vs[38]["mm__"] = """Concat"""
        self.vs[38]["Type"] = """'String'"""
        #self.vs[38]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concatlayer3rule2class4attribute038')
    	# apply attribute concat has left args name(layer3rule2class4attribute0) node
        self.add_node()
    	self.vs[39]["mm__"] = """hasArgs"""
        #self.vs[39]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgslayer3rule2class4attribute039')
    	# apply attribute concat has right args name(layer3rule2class4attribute0) node
        self.add_node()
    	self.vs[40]["mm__"] = """hasArgs"""
        #self.vs[40]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgslayer3rule2class4attribute040')
    	# attribute concat name(layer3rule2class4attribute0) node
    	self.add_node()
    	self.vs[41]["name"] = """Concatlayer3rule2class4attribute041"""
        self.vs[41]["mm__"] = """Concat"""
        self.vs[41]["Type"] = """'String'"""
        #self.vs[41]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concatlayer3rule2class4attribute041')
    	# apply attribute concat has left args name(layer3rule2class4attribute0) node
        self.add_node()
    	self.vs[42]["mm__"] = """hasArgs"""
        #self.vs[42]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgslayer3rule2class4attribute042')
    	# apply attribute concat has right args name(layer3rule2class4attribute0) node
        self.add_node()
    	self.vs[43]["mm__"] = """hasArgs"""
        #self.vs[43]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgslayer3rule2class4attribute043')
    	# apply attribute atom name(layer3rule2class4attribute0) node
    	self.add_node()
    	self.vs[44]["name"] = """_"""
        self.vs[44]["mm__"] = """Constant"""
        self.vs[44]["Type"] = """'String'"""
        #self.vs[44]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atomlayer3rule2class4attribute044')
    	# attribute concat name(layer3rule2class4attribute0) node
    	self.add_node()
    	self.vs[45]["name"] = """Concatlayer3rule2class4attribute045"""
        self.vs[45]["mm__"] = """Concat"""
        self.vs[45]["Type"] = """'String'"""
        #self.vs[45]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concatlayer3rule2class4attribute045')
    	# apply attribute concat has left args name(layer3rule2class4attribute0) node
        self.add_node()
    	self.vs[46]["mm__"] = """hasArgs"""
        #self.vs[46]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgslayer3rule2class4attribute046')
    	# apply attribute concat has right args name(layer3rule2class4attribute0) node
        self.add_node()
    	self.vs[47]["mm__"] = """hasArgs"""
        #self.vs[47]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgslayer3rule2class4attribute047')
    	# apply attribute atom name(layer3rule2class4attribute0) node
    	self.add_node()
    	self.vs[48]["name"] = """__wire"""
        self.vs[48]["mm__"] = """Constant"""
        self.vs[48]["Type"] = """'String'"""
        #self.vs[48]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atomlayer3rule2class4attribute048')
        
        
        # Add the edges
        self.add_edges([
    		(0,4), # matchmodel -> match_contains
    		(4,3), # match_contains -> match_class ImplementationModule(layer3rule2class0)
    		(0,6), # matchmodel -> match_contains
    		(6,5), # match_contains -> match_class InstanceConfiguration(layer3rule2class1)
    		(0,8), # matchmodel -> match_contains
    		(8,7), # match_contains -> match_class ComponentInstance(layer3rule2class2)
    		(1,10), # applymodel -> apply_contains
    		(10,9), # apply_contains -> apply_class ImplementationModule(layer3rule2class3)
    		(1,12), # applymodel -> apply_contains
    		(12,11), # apply_contains -> apply_class FunctionPrototype(layer3rule2class4)
    		(1,14), # applymodel -> apply_contains
    		(14,13), # apply_contains -> apply_class VoidType(layer3rule2class5)
    		(3,15), # match_class ImplementationModule(layer3rule2class0) -> association contents
    		(15,5), # association contents  -> match_class InstanceConfiguration(layer3rule2class1)
    		(5,16), # match_class InstanceConfiguration(layer3rule2class1) -> association contents
    		(16,7), # association contents  -> match_class ComponentInstance(layer3rule2class2)
    		(9,17), # apply_class ImplementationModule(layer3rule2class3) -> association contents
    		(17,11), # association contents  -> apply_class FunctionPrototype(layer3rule2class4)
    		(11,18), # apply_class FunctionPrototype(layer3rule2class4) -> association type
    		(18,13), # association type  -> apply_class VoidType(layer3rule2class5)
    		(9,19), # apply_class ImplementationModule(layer3rule2class3) -> backward_association
    		(19,3), #  backward_association -> apply_class ImplementationModule(layer3rule2class0)
    		(3,20), # match_class ImplementationModule(layer3rule2class0) -> has_match_attribute name (layer3rule2class0attribute0)
    		(20,21), #  has_match_attribute name (layer3rule2class0attribute0) -> match_attribute name (layer3rule2class0attribute0)
    		(5,22), # match_class InstanceConfiguration(layer3rule2class1) -> has_match_attribute name (layer3rule2class1attribute0)
    		(22,23), #  has_match_attribute name (layer3rule2class1attribute0) -> match_attribute name (layer3rule2class1attribute0)
    		(7,24), # match_class ComponentInstance(layer3rule2class2) -> has_match_attribute name (layer3rule2class2attribute0)
    		(24,25), #  has_match_attribute name (layer3rule2class2attribute0) -> match_attribute name (layer3rule2class2attribute0)
    		(11,26), # apply_class FunctionPrototype(layer3rule2class4) -> has_apply_attribute name (layer3rule2class4attribute0)
    		(26,27), #  has_apply_attribute name (layer3rule2class4attribute0) -> apply_attribute name (layer3rule2class4attribute0)
    		(28,29), #  equation of apply attribute name (layer3rule2class4attribute0) -> left_expr
    		(29,27), #  left_expr -> apply_attribute name (layer3rule2class4attribute0)
    		(28,30), #  equation of apply attribute name (layer3rule2class4attribute0) -> right_expr
    		(45,46), #  apply attribute concat name (layer3rule2class4attribute0) -> left has_args  
    		(46,25), #  left has_args -> term
    		(45,47), #  apply attribute concat name (layer3rule2class4attribute0) -> right has_args  
    		(47,48), #  right has_args -> term
    		(41,42), #  apply attribute concat name (layer3rule2class4attribute0) -> left has_args  
    		(42,44), #  left has_args -> term
    		(41,43), #  apply attribute concat name (layer3rule2class4attribute0) -> right has_args  
    		(43,45), #  right has_args -> term
    		(38,39), #  apply attribute concat name (layer3rule2class4attribute0) -> left has_args  
    		(39,23), #  left has_args -> term
    		(38,40), #  apply attribute concat name (layer3rule2class4attribute0) -> right has_args  
    		(40,41), #  right has_args -> term
    		(34,35), #  apply attribute concat name (layer3rule2class4attribute0) -> left has_args  
    		(35,37), #  left has_args -> term
    		(34,36), #  apply attribute concat name (layer3rule2class4attribute0) -> right has_args  
    		(36,38), #  right has_args -> term
    		(31,32), #  apply attribute concat name (layer3rule2class4attribute0) -> left has_args  
    		(32,21), #  left has_args -> term
    		(31,33), #  apply attribute concat name (layer3rule2class4attribute0) -> right has_args  
    		(33,34), #  right has_args -> term
    		(30,31), # right_expr --> term
        	(0,2), # matchmodel -> pairedwith
        	(2,1) # pairedwith -> applyModel
        ])
        
