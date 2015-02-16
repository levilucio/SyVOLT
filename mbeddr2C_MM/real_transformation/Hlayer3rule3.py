from core.himesis import Himesis
import cPickle as pickle
import uuid

class Hlayer3rule3(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule layer3rule3.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer3rule3, self).__init__(name='Hlayer3rule3', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        # TODO Levi, need some help here because I don't know where does 
        # this value come from.
        self["mm__"] = pickle.loads("""(lp1
S'HimesisMM'
p2
a.""")
        
        self["name"] = """layer3rule3"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule3')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule3matchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule3applymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule3pairedwith2')
        
    	# match class ImplementationModule(layer3rule3class0) node
    	self.add_node()
    	self.vs[3]["name"] = """layer3rule3class0"""
        self.vs[3]["classtype"] = """ImplementationModule"""
        self.vs[3]["mm__"] = """ImplementationModule"""
        self.vs[3]["cardinality"] = """+"""
        #self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule3class0')
    	# match_contains node for class ImplementationModule(layer3rule3class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        #self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule3class0matchcontains4')
    	# match class InstanceConfiguration(layer3rule3class1) node
    	self.add_node()
    	self.vs[5]["name"] = """layer3rule3class1"""
        self.vs[5]["classtype"] = """InstanceConfiguration"""
        self.vs[5]["mm__"] = """InstanceConfiguration"""
        self.vs[5]["cardinality"] = """+"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule3class1')
    	# match_contains node for class InstanceConfiguration(layer3rule3class1)
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        #self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule3class1matchcontains6')
    	# match class ComponentInstance(layer3rule3class2) node
    	self.add_node()
    	self.vs[7]["name"] = """layer3rule3class2"""
        self.vs[7]["classtype"] = """ComponentInstance"""
        self.vs[7]["mm__"] = """ComponentInstance"""
        self.vs[7]["cardinality"] = """+"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule3class2')
    	# match_contains node for class ComponentInstance(layer3rule3class2)
        self.add_node()
        self.vs[8]["mm__"] = """match_contains"""
        #self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule3class2matchcontains8')
    	# match class AtomicComponent(layer3rule3class3) node
    	self.add_node()
    	self.vs[9]["name"] = """layer3rule3class3"""
        self.vs[9]["classtype"] = """AtomicComponent"""
        self.vs[9]["mm__"] = """AtomicComponent"""
        self.vs[9]["cardinality"] = """+"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule3class3')
    	# match_contains node for class AtomicComponent(layer3rule3class3)
        self.add_node()
        self.vs[10]["mm__"] = """match_contains"""
        #self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule3class3matchcontains10')
    	# match class ProvidedPort(layer3rule3class4) node
    	self.add_node()
    	self.vs[11]["name"] = """layer3rule3class4"""
        self.vs[11]["classtype"] = """ProvidedPort"""
        self.vs[11]["mm__"] = """ProvidedPort"""
        self.vs[11]["cardinality"] = """+"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule3class4')
    	# match_contains node for class ProvidedPort(layer3rule3class4)
        self.add_node()
        self.vs[12]["mm__"] = """match_contains"""
        #self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule3class4matchcontains12')
    	# match class ClientServerInterface(layer3rule3class5) node
    	self.add_node()
    	self.vs[13]["name"] = """layer3rule3class5"""
        self.vs[13]["classtype"] = """ClientServerInterface"""
        self.vs[13]["mm__"] = """ClientServerInterface"""
        self.vs[13]["cardinality"] = """+"""
        #self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule3class5')
    	# match_contains node for class ClientServerInterface(layer3rule3class5)
        self.add_node()
        self.vs[14]["mm__"] = """match_contains"""
        #self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule3class5matchcontains14')
        
        
    	# apply class ImplementationModule(layer3rule3class6) node
    	self.add_node()
    	self.vs[15]["name"] = """layer3rule3class6"""
        self.vs[15]["classtype"] = """ImplementationModule"""
        self.vs[15]["mm__"] = """ImplementationModule"""
        self.vs[15]["cardinality"] = """1"""
        #self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule3class6')
    	# apply_contains node for class ImplementationModule(layer3rule3class6)
        self.add_node()
        self.vs[16]["mm__"] = """apply_contains"""
        #self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule3class6applycontains16')
    	# apply class GlobalVariableDeclaration(layer3rule3class7) node
    	self.add_node()
    	self.vs[17]["name"] = """layer3rule3class7"""
        self.vs[17]["classtype"] = """GlobalVariableDeclaration"""
        self.vs[17]["mm__"] = """GlobalVariableDeclaration"""
        self.vs[17]["cardinality"] = """1"""
        #self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule3class7')
    	# apply_contains node for class GlobalVariableDeclaration(layer3rule3class7)
        self.add_node()
        self.vs[18]["mm__"] = """apply_contains"""
        #self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule3class7applycontains18')
    	# apply class TypeDef(layer3rule3class8) node
    	self.add_node()
    	self.vs[19]["name"] = """layer3rule3class8"""
        self.vs[19]["classtype"] = """TypeDef"""
        self.vs[19]["mm__"] = """TypeDef"""
        self.vs[19]["cardinality"] = """1"""
        #self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule3class8')
    	# apply_contains node for class TypeDef(layer3rule3class8)
        self.add_node()
        self.vs[20]["mm__"] = """apply_contains"""
        #self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule3class8applycontains20')
    	# apply class TypeDefType(layer3rule3class9) node
    	self.add_node()
    	self.vs[21]["name"] = """layer3rule3class9"""
        self.vs[21]["classtype"] = """TypeDefType"""
        self.vs[21]["mm__"] = """TypeDefType"""
        self.vs[21]["cardinality"] = """1"""
        #self.vs[21]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule3class9')
    	# apply_contains node for class TypeDefType(layer3rule3class9)
        self.add_node()
        self.vs[22]["mm__"] = """apply_contains"""
        #self.vs[22]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule3class9applycontains22')
        
        
    	# match association ImplementationModule--contents-->InstanceConfiguration node
    	self.add_node()
    	self.vs[23]["associationType"] = """contents"""
        self.vs[23]["mm__"] = """directLink_S"""
        #self.vs[23]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule3class0assoc23layer3rule3class1')
    	# match association InstanceConfiguration--contents-->ComponentInstance node
    	self.add_node()
    	self.vs[24]["associationType"] = """contents"""
        self.vs[24]["mm__"] = """directLink_S"""
        #self.vs[24]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule3class1assoc24layer3rule3class2')
    	# match association ComponentInstance--component-->AtomicComponent node
    	self.add_node()
    	self.vs[25]["associationType"] = """component"""
        self.vs[25]["mm__"] = """directLink_S"""
        #self.vs[25]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule3class2assoc25layer3rule3class3')
    	# match association AtomicComponent--contents-->ProvidedPort node
    	self.add_node()
    	self.vs[26]["associationType"] = """contents"""
        self.vs[26]["mm__"] = """directLink_S"""
        #self.vs[26]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule3class3assoc26layer3rule3class4')
    	# match association ProvidedPort--intf-->ClientServerInterface node
    	self.add_node()
    	self.vs[27]["associationType"] = """intf"""
        self.vs[27]["mm__"] = """directLink_S"""
        #self.vs[27]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule3class4assoc27layer3rule3class5')
        
    	# apply association ImplementationModule--contents-->GlobalVariableDeclaration node
    	self.add_node()
    	self.vs[28]["associationType"] = """contents"""
        self.vs[28]["mm__"] = """directLink_T"""
        #self.vs[28]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule3class6assoc28layer3rule3class7')
    	# apply association GlobalVariableDeclaration--type-->TypeDefType node
    	self.add_node()
    	self.vs[29]["associationType"] = """type"""
        self.vs[29]["mm__"] = """directLink_T"""
        #self.vs[29]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule3class7assoc29layer3rule3class9')
    	# apply association TypeDefType--typeDef-->TypeDef node
    	self.add_node()
    	self.vs[30]["associationType"] = """typeDef"""
        self.vs[30]["mm__"] = """directLink_T"""
        #self.vs[30]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule3class9assoc30layer3rule3class8')
        
    	# backward association ImplementationModule---->ImplementationModule node
    	self.add_node()
    	self.vs[31]["type"] = """ruleDef"""
        self.vs[31]["mm__"] = """backward_link"""
        #self.vs[31]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule3class0blink31layer3rule3class6')
    	# backward association ClientServerInterface---->TypeDef node
    	self.add_node()
    	self.vs[32]["type"] = """ruleDef"""
        self.vs[32]["mm__"] = """backward_link"""
        #self.vs[32]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule3class5blink32layer3rule3class8')
        
        
    	# has match attribute name(layer3rule3class0attribute0) node
    	self.add_node()
    	self.vs[33]["mm__"] = """hasAttribute_S"""
        #self.vs[33]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer3rule3class0attribute0')
    	# match attribute name(layer3rule3class0attribute0) node
    	self.add_node()
    	self.vs[34]["name"] = """name"""
        self.vs[34]["mm__"] = """Attribute"""
        self.vs[34]["Type"] = """'String'"""
        #self.vs[34]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule3class0attribute0')
    	# has match attribute name(layer3rule3class2attribute0) node
    	self.add_node()
    	self.vs[35]["mm__"] = """hasAttribute_S"""
        #self.vs[35]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer3rule3class2attribute0')
    	# match attribute name(layer3rule3class2attribute0) node
    	self.add_node()
    	self.vs[36]["name"] = """name"""
        self.vs[36]["mm__"] = """Attribute"""
        self.vs[36]["Type"] = """'String'"""
        #self.vs[36]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule3class2attribute0')
    	# has match attribute name(layer3rule3class5attribute0) node
    	self.add_node()
    	self.vs[37]["mm__"] = """hasAttribute_S"""
        #self.vs[37]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer3rule3class5attribute0')
    	# match attribute name(layer3rule3class5attribute0) node
    	self.add_node()
    	self.vs[38]["name"] = """name"""
        self.vs[38]["mm__"] = """Attribute"""
        self.vs[38]["Type"] = """'String'"""
        #self.vs[38]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule3class5attribute0')
        
        
    	# has apply attribute name(layer3rule3class7attribute0) node
    	self.add_node()
    	self.vs[39]["mm__"] = """hasAttribute_T"""
        #self.vs[39]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer3rule3class7attribute0')
    	# apply attribute name(layer3rule3class7attribute0) node
    	self.add_node()
    	self.vs[40]["name"] = """name"""
        self.vs[40]["mm__"] = """Attribute"""
        self.vs[40]["Type"] = """'String'"""
        #self.vs[40]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule3class7attribute0')
    	# apply attribute equation name(layer3rule3class7attribute0) node
    	self.add_node()
    	self.vs[41]["name"] = """eq_"""
        self.vs[41]["mm__"] = """Equation"""
        #self.vs[41]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equationlayer3rule3class7attribute0')
    	# apply attribute equation left expr name(layer3rule3class7attribute0) node
    	self.add_node()
    	self.vs[42]["mm__"] = """leftExpr"""
        #self.vs[42]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExprlayer3rule3class7attribute0')
    	# apply attribute equation right expr name(layer3rule3class7attribute0) node
    	self.add_node()
    	self.vs[43]["mm__"] = """rightExpr"""
        #self.vs[43]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExprlayer3rule3class7attribute0')
    	# attribute concat name(layer3rule3class7attribute0) node
    	self.add_node()
    	self.vs[44]["name"] = """Concatlayer3rule3class7attribute044"""
        self.vs[44]["mm__"] = """Concat"""
        self.vs[44]["Type"] = """'String'"""
        #self.vs[44]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concatlayer3rule3class7attribute044')
    	# apply attribute concat has left args name(layer3rule3class7attribute0) node
        self.add_node()
    	self.vs[45]["mm__"] = """hasArgs"""
        #self.vs[45]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgslayer3rule3class7attribute045')
    	# apply attribute concat has right args name(layer3rule3class7attribute0) node
        self.add_node()
    	self.vs[46]["mm__"] = """hasArgs"""
        #self.vs[46]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgslayer3rule3class7attribute046')
    	# attribute concat name(layer3rule3class7attribute0) node
    	self.add_node()
    	self.vs[47]["name"] = """Concatlayer3rule3class7attribute047"""
        self.vs[47]["mm__"] = """Concat"""
        self.vs[47]["Type"] = """'String'"""
        #self.vs[47]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concatlayer3rule3class7attribute047')
    	# apply attribute concat has left args name(layer3rule3class7attribute0) node
        self.add_node()
    	self.vs[48]["mm__"] = """hasArgs"""
        #self.vs[48]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgslayer3rule3class7attribute048')
    	# apply attribute concat has right args name(layer3rule3class7attribute0) node
        self.add_node()
    	self.vs[49]["mm__"] = """hasArgs"""
        #self.vs[49]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgslayer3rule3class7attribute049')
    	# apply attribute atom name(layer3rule3class7attribute0) node
    	self.add_node()
    	self.vs[50]["name"] = """_"""
        self.vs[50]["mm__"] = """Constant"""
        self.vs[50]["Type"] = """'String'"""
        #self.vs[50]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atomlayer3rule3class7attribute050')
    	# attribute concat name(layer3rule3class7attribute0) node
    	self.add_node()
    	self.vs[51]["name"] = """Concatlayer3rule3class7attribute051"""
        self.vs[51]["mm__"] = """Concat"""
        self.vs[51]["Type"] = """'String'"""
        #self.vs[51]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concatlayer3rule3class7attribute051')
    	# apply attribute concat has left args name(layer3rule3class7attribute0) node
        self.add_node()
    	self.vs[52]["mm__"] = """hasArgs"""
        #self.vs[52]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgslayer3rule3class7attribute052')
    	# apply attribute concat has right args name(layer3rule3class7attribute0) node
        self.add_node()
    	self.vs[53]["mm__"] = """hasArgs"""
        #self.vs[53]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgslayer3rule3class7attribute053')
    	# attribute concat name(layer3rule3class7attribute0) node
    	self.add_node()
    	self.vs[54]["name"] = """Concatlayer3rule3class7attribute054"""
        self.vs[54]["mm__"] = """Concat"""
        self.vs[54]["Type"] = """'String'"""
        #self.vs[54]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concatlayer3rule3class7attribute054')
    	# apply attribute concat has left args name(layer3rule3class7attribute0) node
        self.add_node()
    	self.vs[55]["mm__"] = """hasArgs"""
        #self.vs[55]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgslayer3rule3class7attribute055')
    	# apply attribute concat has right args name(layer3rule3class7attribute0) node
        self.add_node()
    	self.vs[56]["mm__"] = """hasArgs"""
        #self.vs[56]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgslayer3rule3class7attribute056')
    	# apply attribute atom name(layer3rule3class7attribute0) node
    	self.add_node()
    	self.vs[57]["name"] = """_"""
        self.vs[57]["mm__"] = """Constant"""
        self.vs[57]["Type"] = """'String'"""
        #self.vs[57]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atomlayer3rule3class7attribute057')
    	# attribute concat name(layer3rule3class7attribute0) node
    	self.add_node()
    	self.vs[58]["name"] = """Concatlayer3rule3class7attribute058"""
        self.vs[58]["mm__"] = """Concat"""
        self.vs[58]["Type"] = """'String'"""
        #self.vs[58]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concatlayer3rule3class7attribute058')
    	# apply attribute concat has left args name(layer3rule3class7attribute0) node
        self.add_node()
    	self.vs[59]["mm__"] = """hasArgs"""
        #self.vs[59]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgslayer3rule3class7attribute059')
    	# apply attribute concat has right args name(layer3rule3class7attribute0) node
        self.add_node()
    	self.vs[60]["mm__"] = """hasArgs"""
        #self.vs[60]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgslayer3rule3class7attribute060')
    	# apply attribute atom name(layer3rule3class7attribute0) node
    	self.add_node()
    	self.vs[61]["name"] = """__ops"""
        self.vs[61]["mm__"] = """Constant"""
        self.vs[61]["Type"] = """'String'"""
        #self.vs[61]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atomlayer3rule3class7attribute061')
        
        
        # Add the edges
        self.add_edges([
    		(0,4), # matchmodel -> match_contains
    		(4,3), # match_contains -> match_class ImplementationModule(layer3rule3class0)
    		(0,6), # matchmodel -> match_contains
    		(6,5), # match_contains -> match_class InstanceConfiguration(layer3rule3class1)
    		(0,8), # matchmodel -> match_contains
    		(8,7), # match_contains -> match_class ComponentInstance(layer3rule3class2)
    		(0,10), # matchmodel -> match_contains
    		(10,9), # match_contains -> match_class AtomicComponent(layer3rule3class3)
    		(0,12), # matchmodel -> match_contains
    		(12,11), # match_contains -> match_class ProvidedPort(layer3rule3class4)
    		(0,14), # matchmodel -> match_contains
    		(14,13), # match_contains -> match_class ClientServerInterface(layer3rule3class5)
    		(1,16), # applymodel -> apply_contains
    		(16,15), # apply_contains -> apply_class ImplementationModule(layer3rule3class6)
    		(1,18), # applymodel -> apply_contains
    		(18,17), # apply_contains -> apply_class GlobalVariableDeclaration(layer3rule3class7)
    		(1,20), # applymodel -> apply_contains
    		(20,19), # apply_contains -> apply_class TypeDef(layer3rule3class8)
    		(1,22), # applymodel -> apply_contains
    		(22,21), # apply_contains -> apply_class TypeDefType(layer3rule3class9)
    		(3,23), # match_class ImplementationModule(layer3rule3class0) -> association contents
    		(23,5), # association contents  -> match_class InstanceConfiguration(layer3rule3class1)
    		(5,24), # match_class InstanceConfiguration(layer3rule3class1) -> association contents
    		(24,7), # association contents  -> match_class ComponentInstance(layer3rule3class2)
    		(7,25), # match_class ComponentInstance(layer3rule3class2) -> association component
    		(25,9), # association component  -> match_class AtomicComponent(layer3rule3class3)
    		(9,26), # match_class AtomicComponent(layer3rule3class3) -> association contents
    		(26,11), # association contents  -> match_class ProvidedPort(layer3rule3class4)
    		(11,27), # match_class ProvidedPort(layer3rule3class4) -> association intf
    		(27,13), # association intf  -> match_class ClientServerInterface(layer3rule3class5)
    		(15,28), # apply_class ImplementationModule(layer3rule3class6) -> association contents
    		(28,17), # association contents  -> apply_class GlobalVariableDeclaration(layer3rule3class7)
    		(17,29), # apply_class GlobalVariableDeclaration(layer3rule3class7) -> association type
    		(29,21), # association type  -> apply_class TypeDefType(layer3rule3class9)
    		(21,30), # apply_class TypeDefType(layer3rule3class9) -> association typeDef
    		(30,19), # association typeDef  -> apply_class TypeDef(layer3rule3class8)
    		(15,31), # apply_class ImplementationModule(layer3rule3class6) -> backward_association
    		(31,3), #  backward_association -> apply_class ImplementationModule(layer3rule3class0)
    		(19,32), # apply_class TypeDef(layer3rule3class8) -> backward_association
    		(32,13), #  backward_association -> apply_class ClientServerInterface(layer3rule3class5)
    		(3,33), # match_class ImplementationModule(layer3rule3class0) -> has_match_attribute name (layer3rule3class0attribute0)
    		(33,34), #  has_match_attribute name (layer3rule3class0attribute0) -> match_attribute name (layer3rule3class0attribute0)
    		(7,35), # match_class ComponentInstance(layer3rule3class2) -> has_match_attribute name (layer3rule3class2attribute0)
    		(35,36), #  has_match_attribute name (layer3rule3class2attribute0) -> match_attribute name (layer3rule3class2attribute0)
    		(13,37), # match_class ClientServerInterface(layer3rule3class5) -> has_match_attribute name (layer3rule3class5attribute0)
    		(37,38), #  has_match_attribute name (layer3rule3class5attribute0) -> match_attribute name (layer3rule3class5attribute0)
    		(17,39), # apply_class GlobalVariableDeclaration(layer3rule3class7) -> has_apply_attribute name (layer3rule3class7attribute0)
    		(39,40), #  has_apply_attribute name (layer3rule3class7attribute0) -> apply_attribute name (layer3rule3class7attribute0)
    		(41,42), #  equation of apply attribute name (layer3rule3class7attribute0) -> left_expr
    		(42,40), #  left_expr -> apply_attribute name (layer3rule3class7attribute0)
    		(41,43), #  equation of apply attribute name (layer3rule3class7attribute0) -> right_expr
    		(58,59), #  apply attribute concat name (layer3rule3class7attribute0) -> left has_args  
    		(59,38), #  left has_args -> term
    		(58,60), #  apply attribute concat name (layer3rule3class7attribute0) -> right has_args  
    		(60,61), #  right has_args -> term
    		(54,55), #  apply attribute concat name (layer3rule3class7attribute0) -> left has_args  
    		(55,57), #  left has_args -> term
    		(54,56), #  apply attribute concat name (layer3rule3class7attribute0) -> right has_args  
    		(56,58), #  right has_args -> term
    		(51,52), #  apply attribute concat name (layer3rule3class7attribute0) -> left has_args  
    		(52,36), #  left has_args -> term
    		(51,53), #  apply attribute concat name (layer3rule3class7attribute0) -> right has_args  
    		(53,54), #  right has_args -> term
    		(47,48), #  apply attribute concat name (layer3rule3class7attribute0) -> left has_args  
    		(48,50), #  left has_args -> term
    		(47,49), #  apply attribute concat name (layer3rule3class7attribute0) -> right has_args  
    		(49,51), #  right has_args -> term
    		(44,45), #  apply attribute concat name (layer3rule3class7attribute0) -> left has_args  
    		(45,34), #  left has_args -> term
    		(44,46), #  apply attribute concat name (layer3rule3class7attribute0) -> right has_args  
    		(46,47), #  right has_args -> term
    		(43,44), # right_expr --> term
        	(0,2), # matchmodel -> pairedwith
        	(2,1) # pairedwith -> applyModel
        ])
        
