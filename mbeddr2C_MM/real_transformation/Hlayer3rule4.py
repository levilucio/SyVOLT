from core.himesis import Himesis
import cPickle as pickle
import uuid

class Hlayer3rule4(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule layer3rule4.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer3rule4, self).__init__(name='Hlayer3rule4', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        # TODO Levi, need some help here because I don't know where does 
        # this value come from.
        self["mm__"] = pickle.loads("""(lp1
S'HimesisMM'
p2
a.""")
        
        self["name"] = """layer3rule4"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule4')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule4matchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule4applymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule4pairedwith2')
        
    	# match class ImplementationModule(layer3rule4class0) node
    	self.add_node()
    	self.vs[3]["name"] = """layer3rule4class0"""
        self.vs[3]["classtype"] = """ImplementationModule"""
        self.vs[3]["mm__"] = """ImplementationModule"""
        self.vs[3]["cardinality"] = """+"""
        #self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule4class0')
    	# match_contains node for class ImplementationModule(layer3rule4class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        #self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule4class0matchcontains4')
    	# match class InstanceConfiguration(layer3rule4class1) node
    	self.add_node()
    	self.vs[5]["name"] = """layer3rule4class1"""
        self.vs[5]["classtype"] = """InstanceConfiguration"""
        self.vs[5]["mm__"] = """InstanceConfiguration"""
        self.vs[5]["cardinality"] = """+"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule4class1')
    	# match_contains node for class InstanceConfiguration(layer3rule4class1)
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        #self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule4class1matchcontains6')
    	# match class ComponentInstance(layer3rule4class2) node
    	self.add_node()
    	self.vs[7]["name"] = """layer3rule4class2"""
        self.vs[7]["classtype"] = """ComponentInstance"""
        self.vs[7]["mm__"] = """ComponentInstance"""
        self.vs[7]["cardinality"] = """+"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule4class2')
    	# match_contains node for class ComponentInstance(layer3rule4class2)
        self.add_node()
        self.vs[8]["mm__"] = """match_contains"""
        #self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule4class2matchcontains8')
    	# match class AtomicComponent(layer3rule4class3) node
    	self.add_node()
    	self.vs[9]["name"] = """layer3rule4class3"""
        self.vs[9]["classtype"] = """AtomicComponent"""
        self.vs[9]["mm__"] = """AtomicComponent"""
        self.vs[9]["cardinality"] = """+"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule4class3')
    	# match_contains node for class AtomicComponent(layer3rule4class3)
        self.add_node()
        self.vs[10]["mm__"] = """match_contains"""
        #self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule4class3matchcontains10')
        
        
    	# apply class ImplementationModule(layer3rule4class4) node
    	self.add_node()
    	self.vs[11]["name"] = """layer3rule4class4"""
        self.vs[11]["classtype"] = """ImplementationModule"""
        self.vs[11]["mm__"] = """ImplementationModule"""
        self.vs[11]["cardinality"] = """1"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule4class4')
    	# apply_contains node for class ImplementationModule(layer3rule4class4)
        self.add_node()
        self.vs[12]["mm__"] = """apply_contains"""
        #self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule4class4applycontains12')
    	# apply class GlobalVariableDeclaration(layer3rule4class5) node
    	self.add_node()
    	self.vs[13]["name"] = """layer3rule4class5"""
        self.vs[13]["classtype"] = """GlobalVariableDeclaration"""
        self.vs[13]["mm__"] = """GlobalVariableDeclaration"""
        self.vs[13]["cardinality"] = """1"""
        #self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule4class5')
    	# apply_contains node for class GlobalVariableDeclaration(layer3rule4class5)
        self.add_node()
        self.vs[14]["mm__"] = """apply_contains"""
        #self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule4class5applycontains14')
    	# apply class TypeDef(layer3rule4class6) node
    	self.add_node()
    	self.vs[15]["name"] = """layer3rule4class6"""
        self.vs[15]["classtype"] = """TypeDef"""
        self.vs[15]["mm__"] = """TypeDef"""
        self.vs[15]["cardinality"] = """1"""
        #self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule4class6')
    	# apply_contains node for class TypeDef(layer3rule4class6)
        self.add_node()
        self.vs[16]["mm__"] = """apply_contains"""
        #self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule4class6applycontains16')
    	# apply class TypeDefType(layer3rule4class7) node
    	self.add_node()
    	self.vs[17]["name"] = """layer3rule4class7"""
        self.vs[17]["classtype"] = """TypeDefType"""
        self.vs[17]["mm__"] = """TypeDefType"""
        self.vs[17]["cardinality"] = """1"""
        #self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule4class7')
    	# apply_contains node for class TypeDefType(layer3rule4class7)
        self.add_node()
        self.vs[18]["mm__"] = """apply_contains"""
        #self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule4class7applycontains18')
        
        
    	# match association ImplementationModule--contents-->InstanceConfiguration node
    	self.add_node()
    	self.vs[19]["associationType"] = """contents"""
        self.vs[19]["mm__"] = """directLink_S"""
        #self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule4class0assoc19layer3rule4class1')
    	# match association InstanceConfiguration--contents-->ComponentInstance node
    	self.add_node()
    	self.vs[20]["associationType"] = """contents"""
        self.vs[20]["mm__"] = """directLink_S"""
        #self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule4class1assoc20layer3rule4class2')
    	# match association ComponentInstance--component-->AtomicComponent node
    	self.add_node()
    	self.vs[21]["associationType"] = """component"""
        self.vs[21]["mm__"] = """directLink_S"""
        #self.vs[21]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule4class2assoc21layer3rule4class3')
        
    	# apply association ImplementationModule--contents-->GlobalVariableDeclaration node
    	self.add_node()
    	self.vs[22]["associationType"] = """contents"""
        self.vs[22]["mm__"] = """directLink_T"""
        #self.vs[22]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule4class4assoc22layer3rule4class5')
    	# apply association GlobalVariableDeclaration--type-->TypeDefType node
    	self.add_node()
    	self.vs[23]["associationType"] = """type"""
        self.vs[23]["mm__"] = """directLink_T"""
        #self.vs[23]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule4class5assoc23layer3rule4class7')
    	# apply association TypeDefType--typeDef-->TypeDef node
    	self.add_node()
    	self.vs[24]["associationType"] = """typeDef"""
        self.vs[24]["mm__"] = """directLink_T"""
        #self.vs[24]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule4class7assoc24layer3rule4class6')
        
    	# backward association ImplementationModule---->ImplementationModule node
    	self.add_node()
    	self.vs[25]["type"] = """ruleDef"""
        self.vs[25]["mm__"] = """backward_link"""
        #self.vs[25]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule4class0blink25layer3rule4class4')
    	# backward association AtomicComponent---->TypeDef node
    	self.add_node()
    	self.vs[26]["type"] = """ruleDef"""
        self.vs[26]["mm__"] = """backward_link"""
        #self.vs[26]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule4class3blink26layer3rule4class6')
        
        
    	# has match attribute name(layer3rule4class0attribute0) node
    	self.add_node()
    	self.vs[27]["mm__"] = """hasAttribute_S"""
        #self.vs[27]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer3rule4class0attribute0')
    	# match attribute name(layer3rule4class0attribute0) node
    	self.add_node()
    	self.vs[28]["name"] = """name"""
        self.vs[28]["mm__"] = """Attribute"""
        self.vs[28]["Type"] = """'String'"""
        #self.vs[28]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule4class0attribute0')
    	# has match attribute name(layer3rule4class1attribute0) node
    	self.add_node()
    	self.vs[29]["mm__"] = """hasAttribute_S"""
        #self.vs[29]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer3rule4class1attribute0')
    	# match attribute name(layer3rule4class1attribute0) node
    	self.add_node()
    	self.vs[30]["name"] = """name"""
        self.vs[30]["mm__"] = """Attribute"""
        self.vs[30]["Type"] = """'String'"""
        #self.vs[30]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule4class1attribute0')
    	# has match attribute name(layer3rule4class2attribute0) node
    	self.add_node()
    	self.vs[31]["mm__"] = """hasAttribute_S"""
        #self.vs[31]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer3rule4class2attribute0')
    	# match attribute name(layer3rule4class2attribute0) node
    	self.add_node()
    	self.vs[32]["name"] = """name"""
        self.vs[32]["mm__"] = """Attribute"""
        self.vs[32]["Type"] = """'String'"""
        #self.vs[32]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule4class2attribute0')
        
        
    	# has apply attribute name(layer3rule4class5attribute0) node
    	self.add_node()
    	self.vs[33]["mm__"] = """hasAttribute_T"""
        #self.vs[33]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer3rule4class5attribute0')
    	# apply attribute name(layer3rule4class5attribute0) node
    	self.add_node()
    	self.vs[34]["name"] = """name"""
        self.vs[34]["mm__"] = """Attribute"""
        self.vs[34]["Type"] = """'String'"""
        #self.vs[34]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule4class5attribute0')
    	# apply attribute equation name(layer3rule4class5attribute0) node
    	self.add_node()
    	self.vs[35]["name"] = """eq_"""
        self.vs[35]["mm__"] = """Equation"""
        #self.vs[35]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equationlayer3rule4class5attribute0')
    	# apply attribute equation left expr name(layer3rule4class5attribute0) node
    	self.add_node()
    	self.vs[36]["mm__"] = """leftExpr"""
        #self.vs[36]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExprlayer3rule4class5attribute0')
    	# apply attribute equation right expr name(layer3rule4class5attribute0) node
    	self.add_node()
    	self.vs[37]["mm__"] = """rightExpr"""
        #self.vs[37]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExprlayer3rule4class5attribute0')
    	# attribute concat name(layer3rule4class5attribute0) node
    	self.add_node()
    	self.vs[38]["name"] = """Concatlayer3rule4class5attribute038"""
        self.vs[38]["mm__"] = """Concat"""
        self.vs[38]["Type"] = """'String'"""
        #self.vs[38]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concatlayer3rule4class5attribute038')
    	# apply attribute concat has left args name(layer3rule4class5attribute0) node
        self.add_node()
    	self.vs[39]["mm__"] = """hasArgs"""
        #self.vs[39]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgslayer3rule4class5attribute039')
    	# apply attribute concat has right args name(layer3rule4class5attribute0) node
        self.add_node()
    	self.vs[40]["mm__"] = """hasArgs"""
        #self.vs[40]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgslayer3rule4class5attribute040')
    	# attribute concat name(layer3rule4class5attribute0) node
    	self.add_node()
    	self.vs[41]["name"] = """Concatlayer3rule4class5attribute041"""
        self.vs[41]["mm__"] = """Concat"""
        self.vs[41]["Type"] = """'String'"""
        #self.vs[41]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concatlayer3rule4class5attribute041')
    	# apply attribute concat has left args name(layer3rule4class5attribute0) node
        self.add_node()
    	self.vs[42]["mm__"] = """hasArgs"""
        #self.vs[42]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgslayer3rule4class5attribute042')
    	# apply attribute concat has right args name(layer3rule4class5attribute0) node
        self.add_node()
    	self.vs[43]["mm__"] = """hasArgs"""
        #self.vs[43]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgslayer3rule4class5attribute043')
    	# apply attribute atom name(layer3rule4class5attribute0) node
    	self.add_node()
    	self.vs[44]["name"] = """_"""
        self.vs[44]["mm__"] = """Constant"""
        self.vs[44]["Type"] = """'String'"""
        #self.vs[44]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atomlayer3rule4class5attribute044')
    	# attribute concat name(layer3rule4class5attribute0) node
    	self.add_node()
    	self.vs[45]["name"] = """Concatlayer3rule4class5attribute045"""
        self.vs[45]["mm__"] = """Concat"""
        self.vs[45]["Type"] = """'String'"""
        #self.vs[45]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concatlayer3rule4class5attribute045')
    	# apply attribute concat has left args name(layer3rule4class5attribute0) node
        self.add_node()
    	self.vs[46]["mm__"] = """hasArgs"""
        #self.vs[46]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgslayer3rule4class5attribute046')
    	# apply attribute concat has right args name(layer3rule4class5attribute0) node
        self.add_node()
    	self.vs[47]["mm__"] = """hasArgs"""
        #self.vs[47]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgslayer3rule4class5attribute047')
    	# attribute concat name(layer3rule4class5attribute0) node
    	self.add_node()
    	self.vs[48]["name"] = """Concatlayer3rule4class5attribute048"""
        self.vs[48]["mm__"] = """Concat"""
        self.vs[48]["Type"] = """'String'"""
        #self.vs[48]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concatlayer3rule4class5attribute048')
    	# apply attribute concat has left args name(layer3rule4class5attribute0) node
        self.add_node()
    	self.vs[49]["mm__"] = """hasArgs"""
        #self.vs[49]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgslayer3rule4class5attribute049')
    	# apply attribute concat has right args name(layer3rule4class5attribute0) node
        self.add_node()
    	self.vs[50]["mm__"] = """hasArgs"""
        #self.vs[50]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgslayer3rule4class5attribute050')
    	# apply attribute atom name(layer3rule4class5attribute0) node
    	self.add_node()
    	self.vs[51]["name"] = """_"""
        self.vs[51]["mm__"] = """Constant"""
        self.vs[51]["Type"] = """'String'"""
        #self.vs[51]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atomlayer3rule4class5attribute051')
    	# attribute concat name(layer3rule4class5attribute0) node
    	self.add_node()
    	self.vs[52]["name"] = """Concatlayer3rule4class5attribute052"""
        self.vs[52]["mm__"] = """Concat"""
        self.vs[52]["Type"] = """'String'"""
        #self.vs[52]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concatlayer3rule4class5attribute052')
    	# apply attribute concat has left args name(layer3rule4class5attribute0) node
        self.add_node()
    	self.vs[53]["mm__"] = """hasArgs"""
        #self.vs[53]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgslayer3rule4class5attribute053')
    	# apply attribute concat has right args name(layer3rule4class5attribute0) node
        self.add_node()
    	self.vs[54]["mm__"] = """hasArgs"""
        #self.vs[54]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgslayer3rule4class5attribute054')
    	# apply attribute atom name(layer3rule4class5attribute0) node
    	self.add_node()
    	self.vs[55]["name"] = """__instance"""
        self.vs[55]["mm__"] = """Constant"""
        self.vs[55]["Type"] = """'String'"""
        #self.vs[55]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atomlayer3rule4class5attribute055')
        
        
        # Add the edges
        self.add_edges([
    		(0,4), # matchmodel -> match_contains
    		(4,3), # match_contains -> match_class ImplementationModule(layer3rule4class0)
    		(0,6), # matchmodel -> match_contains
    		(6,5), # match_contains -> match_class InstanceConfiguration(layer3rule4class1)
    		(0,8), # matchmodel -> match_contains
    		(8,7), # match_contains -> match_class ComponentInstance(layer3rule4class2)
    		(0,10), # matchmodel -> match_contains
    		(10,9), # match_contains -> match_class AtomicComponent(layer3rule4class3)
    		(1,12), # applymodel -> apply_contains
    		(12,11), # apply_contains -> apply_class ImplementationModule(layer3rule4class4)
    		(1,14), # applymodel -> apply_contains
    		(14,13), # apply_contains -> apply_class GlobalVariableDeclaration(layer3rule4class5)
    		(1,16), # applymodel -> apply_contains
    		(16,15), # apply_contains -> apply_class TypeDef(layer3rule4class6)
    		(1,18), # applymodel -> apply_contains
    		(18,17), # apply_contains -> apply_class TypeDefType(layer3rule4class7)
    		(3,19), # match_class ImplementationModule(layer3rule4class0) -> association contents
    		(19,5), # association contents  -> match_class InstanceConfiguration(layer3rule4class1)
    		(5,20), # match_class InstanceConfiguration(layer3rule4class1) -> association contents
    		(20,7), # association contents  -> match_class ComponentInstance(layer3rule4class2)
    		(7,21), # match_class ComponentInstance(layer3rule4class2) -> association component
    		(21,9), # association component  -> match_class AtomicComponent(layer3rule4class3)
    		(11,22), # apply_class ImplementationModule(layer3rule4class4) -> association contents
    		(22,13), # association contents  -> apply_class GlobalVariableDeclaration(layer3rule4class5)
    		(13,23), # apply_class GlobalVariableDeclaration(layer3rule4class5) -> association type
    		(23,17), # association type  -> apply_class TypeDefType(layer3rule4class7)
    		(17,24), # apply_class TypeDefType(layer3rule4class7) -> association typeDef
    		(24,15), # association typeDef  -> apply_class TypeDef(layer3rule4class6)
    		(11,25), # apply_class ImplementationModule(layer3rule4class4) -> backward_association
    		(25,3), #  backward_association -> apply_class ImplementationModule(layer3rule4class0)
    		(15,26), # apply_class TypeDef(layer3rule4class6) -> backward_association
    		(26,9), #  backward_association -> apply_class AtomicComponent(layer3rule4class3)
    		(3,27), # match_class ImplementationModule(layer3rule4class0) -> has_match_attribute name (layer3rule4class0attribute0)
    		(27,28), #  has_match_attribute name (layer3rule4class0attribute0) -> match_attribute name (layer3rule4class0attribute0)
    		(5,29), # match_class InstanceConfiguration(layer3rule4class1) -> has_match_attribute name (layer3rule4class1attribute0)
    		(29,30), #  has_match_attribute name (layer3rule4class1attribute0) -> match_attribute name (layer3rule4class1attribute0)
    		(7,31), # match_class ComponentInstance(layer3rule4class2) -> has_match_attribute name (layer3rule4class2attribute0)
    		(31,32), #  has_match_attribute name (layer3rule4class2attribute0) -> match_attribute name (layer3rule4class2attribute0)
    		(13,33), # apply_class GlobalVariableDeclaration(layer3rule4class5) -> has_apply_attribute name (layer3rule4class5attribute0)
    		(33,34), #  has_apply_attribute name (layer3rule4class5attribute0) -> apply_attribute name (layer3rule4class5attribute0)
    		(35,36), #  equation of apply attribute name (layer3rule4class5attribute0) -> left_expr
    		(36,34), #  left_expr -> apply_attribute name (layer3rule4class5attribute0)
    		(35,37), #  equation of apply attribute name (layer3rule4class5attribute0) -> right_expr
    		(52,53), #  apply attribute concat name (layer3rule4class5attribute0) -> left has_args  
    		(53,32), #  left has_args -> term
    		(52,54), #  apply attribute concat name (layer3rule4class5attribute0) -> right has_args  
    		(54,55), #  right has_args -> term
    		(48,49), #  apply attribute concat name (layer3rule4class5attribute0) -> left has_args  
    		(49,51), #  left has_args -> term
    		(48,50), #  apply attribute concat name (layer3rule4class5attribute0) -> right has_args  
    		(50,52), #  right has_args -> term
    		(45,46), #  apply attribute concat name (layer3rule4class5attribute0) -> left has_args  
    		(46,30), #  left has_args -> term
    		(45,47), #  apply attribute concat name (layer3rule4class5attribute0) -> right has_args  
    		(47,48), #  right has_args -> term
    		(41,42), #  apply attribute concat name (layer3rule4class5attribute0) -> left has_args  
    		(42,44), #  left has_args -> term
    		(41,43), #  apply attribute concat name (layer3rule4class5attribute0) -> right has_args  
    		(43,45), #  right has_args -> term
    		(38,39), #  apply attribute concat name (layer3rule4class5attribute0) -> left has_args  
    		(39,28), #  left has_args -> term
    		(38,40), #  apply attribute concat name (layer3rule4class5attribute0) -> right has_args  
    		(40,41), #  right has_args -> term
    		(37,38), # right_expr --> term
        	(0,2), # matchmodel -> pairedwith
        	(2,1) # pairedwith -> applyModel
        ])
        
