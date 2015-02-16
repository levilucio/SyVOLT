from core.himesis import Himesis
import cPickle as pickle
import uuid

class Hlayer0rule11(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule layer0rule11.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer0rule11, self).__init__(name='Hlayer0rule11', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        # TODO Levi, need some help here because I don't know where does 
        # this value come from.
        self["mm__"] = pickle.loads("""(lp1
S'HimesisMM'
p2
a.""")
        
        self["name"] = """layer0rule11"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule11')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule11matchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule11applymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule11pairedwith2')
        
    	# match class ProvidedPort(layer0rule11class0) node
    	self.add_node()
    	self.vs[3]["name"] = """layer0rule11class0"""
        self.vs[3]["classtype"] = """ProvidedPort"""
        self.vs[3]["mm__"] = """ProvidedPort"""
        self.vs[3]["cardinality"] = """+"""
        #self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule11class0')
    	# match_contains node for class ProvidedPort(layer0rule11class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        #self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule11class0matchcontains4')
    	# match class AtomicComponent(layer0rule11class1) node
    	self.add_node()
    	self.vs[5]["name"] = """layer0rule11class1"""
        self.vs[5]["classtype"] = """AtomicComponent"""
        self.vs[5]["mm__"] = """AtomicComponent"""
        self.vs[5]["cardinality"] = """+"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule11class1')
    	# match_contains node for class AtomicComponent(layer0rule11class1)
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        #self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule11class1matchcontains6')
    	# match class ClientServerInterface(layer0rule11class2) node
    	self.add_node()
    	self.vs[7]["name"] = """layer0rule11class2"""
        self.vs[7]["classtype"] = """ClientServerInterface"""
        self.vs[7]["mm__"] = """ClientServerInterface"""
        self.vs[7]["cardinality"] = """+"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule11class2')
    	# match_contains node for class ClientServerInterface(layer0rule11class2)
        self.add_node()
        self.vs[8]["mm__"] = """match_contains"""
        #self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule11class2matchcontains8')
    	# match class Operation(layer0rule11class3) node
    	self.add_node()
    	self.vs[9]["name"] = """layer0rule11class3"""
        self.vs[9]["classtype"] = """Operation"""
        self.vs[9]["mm__"] = """Operation"""
        self.vs[9]["cardinality"] = """+"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule11class3')
    	# match_contains node for class Operation(layer0rule11class3)
        self.add_node()
        self.vs[10]["mm__"] = """match_contains"""
        #self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule11class3matchcontains10')
    	# match class ImplementationModule(layer0rule11class4) node
    	self.add_node()
    	self.vs[11]["name"] = """layer0rule11class4"""
        self.vs[11]["classtype"] = """ImplementationModule"""
        self.vs[11]["mm__"] = """ImplementationModule"""
        self.vs[11]["cardinality"] = """+"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule11class4')
    	# match_contains node for class ImplementationModule(layer0rule11class4)
        self.add_node()
        self.vs[12]["mm__"] = """match_contains"""
        #self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule11class4matchcontains12')
        
        
    	# apply class FunctionPrototype(layer0rule11class5) node
    	self.add_node()
    	self.vs[13]["name"] = """layer0rule11class5"""
        self.vs[13]["classtype"] = """FunctionPrototype"""
        self.vs[13]["mm__"] = """FunctionPrototype"""
        self.vs[13]["cardinality"] = """1"""
        #self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule11class5')
    	# apply_contains node for class FunctionPrototype(layer0rule11class5)
        self.add_node()
        self.vs[14]["mm__"] = """apply_contains"""
        #self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule11class5applycontains14')
        
        
    	# match association AtomicComponent--contents-->ProvidedPort node
    	self.add_node()
    	self.vs[15]["associationType"] = """contents"""
        self.vs[15]["mm__"] = """directLink_S"""
        #self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule11class1assoc15layer0rule11class0')
    	# match association ProvidedPort--intf-->ClientServerInterface node
    	self.add_node()
    	self.vs[16]["associationType"] = """intf"""
        self.vs[16]["mm__"] = """directLink_S"""
        #self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule11class0assoc16layer0rule11class2')
    	# match association ClientServerInterface--contents-->Operation node
    	self.add_node()
    	self.vs[17]["associationType"] = """contents"""
        self.vs[17]["mm__"] = """directLink_S"""
        #self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule11class2assoc17layer0rule11class3')
    	# match association ImplementationModule--contents-->AtomicComponent node
    	self.add_node()
    	self.vs[18]["associationType"] = """contents"""
        self.vs[18]["mm__"] = """directLink_S"""
        #self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule11class4assoc18layer0rule11class1')
        
        
        
        
    	# has match attribute name(layer0rule11class0attribute0) node
    	self.add_node()
    	self.vs[19]["mm__"] = """hasAttribute_S"""
        #self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer0rule11class0attribute0')
    	# match attribute name(layer0rule11class0attribute0) node
    	self.add_node()
    	self.vs[20]["name"] = """name"""
        self.vs[20]["mm__"] = """Attribute"""
        self.vs[20]["Type"] = """'String'"""
        #self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule11class0attribute0')
    	# has match attribute name(layer0rule11class1attribute0) node
    	self.add_node()
    	self.vs[21]["mm__"] = """hasAttribute_S"""
        #self.vs[21]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer0rule11class1attribute0')
    	# match attribute name(layer0rule11class1attribute0) node
    	self.add_node()
    	self.vs[22]["name"] = """name"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["Type"] = """'String'"""
        #self.vs[22]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule11class1attribute0')
    	# has match attribute name(layer0rule11class3attribute0) node
    	self.add_node()
    	self.vs[23]["mm__"] = """hasAttribute_S"""
        #self.vs[23]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer0rule11class3attribute0')
    	# match attribute name(layer0rule11class3attribute0) node
    	self.add_node()
    	self.vs[24]["name"] = """name"""
        self.vs[24]["mm__"] = """Attribute"""
        self.vs[24]["Type"] = """'String'"""
        #self.vs[24]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule11class3attribute0')
    	# has match attribute name(layer0rule11class4attribute0) node
    	self.add_node()
    	self.vs[25]["mm__"] = """hasAttribute_S"""
        #self.vs[25]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer0rule11class4attribute0')
    	# match attribute name(layer0rule11class4attribute0) node
    	self.add_node()
    	self.vs[26]["name"] = """name"""
        self.vs[26]["mm__"] = """Attribute"""
        self.vs[26]["Type"] = """'String'"""
        #self.vs[26]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule11class4attribute0')
        
        
    	# has apply attribute name(layer0rule11class5attribute0) node
    	self.add_node()
    	self.vs[27]["mm__"] = """hasAttribute_T"""
        #self.vs[27]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer0rule11class5attribute0')
    	# apply attribute name(layer0rule11class5attribute0) node
    	self.add_node()
    	self.vs[28]["name"] = """name"""
        self.vs[28]["mm__"] = """Attribute"""
        self.vs[28]["Type"] = """'String'"""
        #self.vs[28]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule11class5attribute0')
    	# apply attribute equation name(layer0rule11class5attribute0) node
    	self.add_node()
    	self.vs[29]["name"] = """eq_"""
        self.vs[29]["mm__"] = """Equation"""
        #self.vs[29]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equationlayer0rule11class5attribute0')
    	# apply attribute equation left expr name(layer0rule11class5attribute0) node
    	self.add_node()
    	self.vs[30]["mm__"] = """leftExpr"""
        #self.vs[30]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExprlayer0rule11class5attribute0')
    	# apply attribute equation right expr name(layer0rule11class5attribute0) node
    	self.add_node()
    	self.vs[31]["mm__"] = """rightExpr"""
        #self.vs[31]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExprlayer0rule11class5attribute0')
    	# attribute concat name(layer0rule11class5attribute0) node
    	self.add_node()
    	self.vs[32]["name"] = """Concatlayer0rule11class5attribute032"""
        self.vs[32]["mm__"] = """Concat"""
        self.vs[32]["Type"] = """'String'"""
        #self.vs[32]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concatlayer0rule11class5attribute032')
    	# apply attribute concat has left args name(layer0rule11class5attribute0) node
        self.add_node()
    	self.vs[33]["mm__"] = """hasArgs"""
        #self.vs[33]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgslayer0rule11class5attribute033')
    	# apply attribute concat has right args name(layer0rule11class5attribute0) node
        self.add_node()
    	self.vs[34]["mm__"] = """hasArgs"""
        #self.vs[34]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgslayer0rule11class5attribute034')
    	# attribute concat name(layer0rule11class5attribute0) node
    	self.add_node()
    	self.vs[35]["name"] = """Concatlayer0rule11class5attribute035"""
        self.vs[35]["mm__"] = """Concat"""
        self.vs[35]["Type"] = """'String'"""
        #self.vs[35]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concatlayer0rule11class5attribute035')
    	# apply attribute concat has left args name(layer0rule11class5attribute0) node
        self.add_node()
    	self.vs[36]["mm__"] = """hasArgs"""
        #self.vs[36]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgslayer0rule11class5attribute036')
    	# apply attribute concat has right args name(layer0rule11class5attribute0) node
        self.add_node()
    	self.vs[37]["mm__"] = """hasArgs"""
        #self.vs[37]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgslayer0rule11class5attribute037')
    	# apply attribute atom name(layer0rule11class5attribute0) node
    	self.add_node()
    	self.vs[38]["name"] = """_"""
        self.vs[38]["mm__"] = """Constant"""
        self.vs[38]["Type"] = """'String'"""
        #self.vs[38]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atomlayer0rule11class5attribute038')
    	# attribute concat name(layer0rule11class5attribute0) node
    	self.add_node()
    	self.vs[39]["name"] = """Concatlayer0rule11class5attribute039"""
        self.vs[39]["mm__"] = """Concat"""
        self.vs[39]["Type"] = """'String'"""
        #self.vs[39]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concatlayer0rule11class5attribute039')
    	# apply attribute concat has left args name(layer0rule11class5attribute0) node
        self.add_node()
    	self.vs[40]["mm__"] = """hasArgs"""
        #self.vs[40]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgslayer0rule11class5attribute040')
    	# apply attribute concat has right args name(layer0rule11class5attribute0) node
        self.add_node()
    	self.vs[41]["mm__"] = """hasArgs"""
        #self.vs[41]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgslayer0rule11class5attribute041')
    	# attribute concat name(layer0rule11class5attribute0) node
    	self.add_node()
    	self.vs[42]["name"] = """Concatlayer0rule11class5attribute042"""
        self.vs[42]["mm__"] = """Concat"""
        self.vs[42]["Type"] = """'String'"""
        #self.vs[42]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concatlayer0rule11class5attribute042')
    	# apply attribute concat has left args name(layer0rule11class5attribute0) node
        self.add_node()
    	self.vs[43]["mm__"] = """hasArgs"""
        #self.vs[43]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgslayer0rule11class5attribute043')
    	# apply attribute concat has right args name(layer0rule11class5attribute0) node
        self.add_node()
    	self.vs[44]["mm__"] = """hasArgs"""
        #self.vs[44]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgslayer0rule11class5attribute044')
    	# apply attribute atom name(layer0rule11class5attribute0) node
    	self.add_node()
    	self.vs[45]["name"] = """_"""
        self.vs[45]["mm__"] = """Constant"""
        self.vs[45]["Type"] = """'String'"""
        #self.vs[45]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atomlayer0rule11class5attribute045')
    	# attribute concat name(layer0rule11class5attribute0) node
    	self.add_node()
    	self.vs[46]["name"] = """Concatlayer0rule11class5attribute046"""
        self.vs[46]["mm__"] = """Concat"""
        self.vs[46]["Type"] = """'String'"""
        #self.vs[46]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concatlayer0rule11class5attribute046')
    	# apply attribute concat has left args name(layer0rule11class5attribute0) node
        self.add_node()
    	self.vs[47]["mm__"] = """hasArgs"""
        #self.vs[47]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgslayer0rule11class5attribute047')
    	# apply attribute concat has right args name(layer0rule11class5attribute0) node
        self.add_node()
    	self.vs[48]["mm__"] = """hasArgs"""
        #self.vs[48]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgslayer0rule11class5attribute048')
    	# attribute concat name(layer0rule11class5attribute0) node
    	self.add_node()
    	self.vs[49]["name"] = """Concatlayer0rule11class5attribute049"""
        self.vs[49]["mm__"] = """Concat"""
        self.vs[49]["Type"] = """'String'"""
        #self.vs[49]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concatlayer0rule11class5attribute049')
    	# apply attribute concat has left args name(layer0rule11class5attribute0) node
        self.add_node()
    	self.vs[50]["mm__"] = """hasArgs"""
        #self.vs[50]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgslayer0rule11class5attribute050')
    	# apply attribute concat has right args name(layer0rule11class5attribute0) node
        self.add_node()
    	self.vs[51]["mm__"] = """hasArgs"""
        #self.vs[51]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgslayer0rule11class5attribute051')
    	# apply attribute atom name(layer0rule11class5attribute0) node
    	self.add_node()
    	self.vs[52]["name"] = """_"""
        self.vs[52]["mm__"] = """Constant"""
        self.vs[52]["Type"] = """'String'"""
        #self.vs[52]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atomlayer0rule11class5attribute052')
        
        
        # Add the edges
        self.add_edges([
    		(0,4), # matchmodel -> match_contains
    		(4,3), # match_contains -> match_class ProvidedPort(layer0rule11class0)
    		(0,6), # matchmodel -> match_contains
    		(6,5), # match_contains -> match_class AtomicComponent(layer0rule11class1)
    		(0,8), # matchmodel -> match_contains
    		(8,7), # match_contains -> match_class ClientServerInterface(layer0rule11class2)
    		(0,10), # matchmodel -> match_contains
    		(10,9), # match_contains -> match_class Operation(layer0rule11class3)
    		(0,12), # matchmodel -> match_contains
    		(12,11), # match_contains -> match_class ImplementationModule(layer0rule11class4)
    		(1,14), # applymodel -> apply_contains
    		(14,13), # apply_contains -> apply_class FunctionPrototype(layer0rule11class5)
    		(5,15), # match_class AtomicComponent(layer0rule11class1) -> association contents
    		(15,3), # association contents  -> match_class ProvidedPort(layer0rule11class0)
    		(3,16), # match_class ProvidedPort(layer0rule11class0) -> association intf
    		(16,7), # association intf  -> match_class ClientServerInterface(layer0rule11class2)
    		(7,17), # match_class ClientServerInterface(layer0rule11class2) -> association contents
    		(17,9), # association contents  -> match_class Operation(layer0rule11class3)
    		(11,18), # match_class ImplementationModule(layer0rule11class4) -> association contents
    		(18,5), # association contents  -> match_class AtomicComponent(layer0rule11class1)
    		(3,19), # match_class ProvidedPort(layer0rule11class0) -> has_match_attribute name (layer0rule11class0attribute0)
    		(19,20), #  has_match_attribute name (layer0rule11class0attribute0) -> match_attribute name (layer0rule11class0attribute0)
    		(5,21), # match_class AtomicComponent(layer0rule11class1) -> has_match_attribute name (layer0rule11class1attribute0)
    		(21,22), #  has_match_attribute name (layer0rule11class1attribute0) -> match_attribute name (layer0rule11class1attribute0)
    		(9,23), # match_class Operation(layer0rule11class3) -> has_match_attribute name (layer0rule11class3attribute0)
    		(23,24), #  has_match_attribute name (layer0rule11class3attribute0) -> match_attribute name (layer0rule11class3attribute0)
    		(11,25), # match_class ImplementationModule(layer0rule11class4) -> has_match_attribute name (layer0rule11class4attribute0)
    		(25,26), #  has_match_attribute name (layer0rule11class4attribute0) -> match_attribute name (layer0rule11class4attribute0)
    		(13,27), # apply_class FunctionPrototype(layer0rule11class5) -> has_apply_attribute name (layer0rule11class5attribute0)
    		(27,28), #  has_apply_attribute name (layer0rule11class5attribute0) -> apply_attribute name (layer0rule11class5attribute0)
    		(29,30), #  equation of apply attribute name (layer0rule11class5attribute0) -> left_expr
    		(30,28), #  left_expr -> apply_attribute name (layer0rule11class5attribute0)
    		(29,31), #  equation of apply attribute name (layer0rule11class5attribute0) -> right_expr
    		(49,50), #  apply attribute concat name (layer0rule11class5attribute0) -> left has_args  
    		(50,52), #  left has_args -> term
    		(49,51), #  apply attribute concat name (layer0rule11class5attribute0) -> right has_args  
    		(51,24), #  right has_args -> term
    		(46,47), #  apply attribute concat name (layer0rule11class5attribute0) -> left has_args  
    		(47,20), #  left has_args -> term
    		(46,48), #  apply attribute concat name (layer0rule11class5attribute0) -> right has_args  
    		(48,49), #  right has_args -> term
    		(42,43), #  apply attribute concat name (layer0rule11class5attribute0) -> left has_args  
    		(43,45), #  left has_args -> term
    		(42,44), #  apply attribute concat name (layer0rule11class5attribute0) -> right has_args  
    		(44,46), #  right has_args -> term
    		(39,40), #  apply attribute concat name (layer0rule11class5attribute0) -> left has_args  
    		(40,22), #  left has_args -> term
    		(39,41), #  apply attribute concat name (layer0rule11class5attribute0) -> right has_args  
    		(41,42), #  right has_args -> term
    		(35,36), #  apply attribute concat name (layer0rule11class5attribute0) -> left has_args  
    		(36,38), #  left has_args -> term
    		(35,37), #  apply attribute concat name (layer0rule11class5attribute0) -> right has_args  
    		(37,39), #  right has_args -> term
    		(32,33), #  apply attribute concat name (layer0rule11class5attribute0) -> left has_args  
    		(33,26), #  left has_args -> term
    		(32,34), #  apply attribute concat name (layer0rule11class5attribute0) -> right has_args  
    		(34,35), #  right has_args -> term
    		(31,32), # right_expr --> term
        	(0,2), # matchmodel -> pairedwith
        	(2,1) # pairedwith -> applyModel
        ])
        
