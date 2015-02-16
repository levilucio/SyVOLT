from core.himesis import Himesis
import cPickle as pickle
import uuid

class Hlayer0rule7(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule layer0rule7.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer0rule7, self).__init__(name='Hlayer0rule7', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        # TODO Levi, need some help here because I don't know where does 
        # this value come from.
        self["mm__"] = pickle.loads("""(lp1
S'HimesisMM'
p2
a.""")
        
        self["name"] = """layer0rule7"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule7')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule7matchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule7applymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule7pairedwith2')
        
    	# match class AtomicComponent(layer0rule7class0) node
    	self.add_node()
    	self.vs[3]["name"] = """layer0rule7class0"""
        self.vs[3]["classtype"] = """AtomicComponent"""
        self.vs[3]["mm__"] = """AtomicComponent"""
        self.vs[3]["cardinality"] = """+"""
        #self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule7class0')
    	# match_contains node for class AtomicComponent(layer0rule7class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        #self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule7class0matchcontains4')
    	# match class ImplementationModule(layer0rule7class1) node
    	self.add_node()
    	self.vs[5]["name"] = """layer0rule7class1"""
        self.vs[5]["classtype"] = """ImplementationModule"""
        self.vs[5]["mm__"] = """ImplementationModule"""
        self.vs[5]["cardinality"] = """+"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule7class1')
    	# match_contains node for class ImplementationModule(layer0rule7class1)
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        #self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule7class1matchcontains6')
        
        
    	# apply class StructDeclaration(layer0rule7class2) node
    	self.add_node()
    	self.vs[7]["name"] = """layer0rule7class2"""
        self.vs[7]["classtype"] = """StructDeclaration"""
        self.vs[7]["mm__"] = """StructDeclaration"""
        self.vs[7]["cardinality"] = """1"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule7class2')
    	# apply_contains node for class StructDeclaration(layer0rule7class2)
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        #self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule7class2applycontains8')
    	# apply class Member(layer0rule7class3) node
    	self.add_node()
    	self.vs[9]["name"] = """layer0rule7class3"""
        self.vs[9]["classtype"] = """Member"""
        self.vs[9]["mm__"] = """Member"""
        self.vs[9]["cardinality"] = """1"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule7class3')
    	# apply_contains node for class Member(layer0rule7class3)
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        #self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule7class3applycontains10')
    	# apply class Int32Type(layer0rule7class4) node
    	self.add_node()
    	self.vs[11]["name"] = """layer0rule7class4"""
        self.vs[11]["classtype"] = """Int32Type"""
        self.vs[11]["mm__"] = """Int32Type"""
        self.vs[11]["cardinality"] = """1"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule7class4')
    	# apply_contains node for class Int32Type(layer0rule7class4)
        self.add_node()
        self.vs[12]["mm__"] = """apply_contains"""
        #self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule7class4applycontains12')
        
        
    	# match association ImplementationModule--contents-->AtomicComponent node
    	self.add_node()
    	self.vs[13]["associationType"] = """contents"""
        self.vs[13]["mm__"] = """directLink_S"""
        #self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule7class1assoc13layer0rule7class0')
        
    	# apply association StructDeclaration--members-->Member node
    	self.add_node()
    	self.vs[14]["associationType"] = """members"""
        self.vs[14]["mm__"] = """directLink_T"""
        #self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule7class2assoc14layer0rule7class3')
    	# apply association Member--type-->Int32Type node
    	self.add_node()
    	self.vs[15]["associationType"] = """type"""
        self.vs[15]["mm__"] = """directLink_T"""
        #self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule7class3assoc15layer0rule7class4')
        
        
        
    	# has match attribute name(layer0rule7class0attribute0) node
    	self.add_node()
    	self.vs[16]["mm__"] = """hasAttribute_S"""
        #self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer0rule7class0attribute0')
    	# match attribute name(layer0rule7class0attribute0) node
    	self.add_node()
    	self.vs[17]["name"] = """name"""
        self.vs[17]["mm__"] = """Attribute"""
        self.vs[17]["Type"] = """'String'"""
        #self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule7class0attribute0')
    	# has match attribute name(layer0rule7class1attribute0) node
    	self.add_node()
    	self.vs[18]["mm__"] = """hasAttribute_S"""
        #self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer0rule7class1attribute0')
    	# match attribute name(layer0rule7class1attribute0) node
    	self.add_node()
    	self.vs[19]["name"] = """name"""
        self.vs[19]["mm__"] = """Attribute"""
        self.vs[19]["Type"] = """'String'"""
        #self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule7class1attribute0')
        
        
    	# has apply attribute name(layer0rule7class2attribute0) node
    	self.add_node()
    	self.vs[20]["mm__"] = """hasAttribute_T"""
        #self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer0rule7class2attribute0')
    	# apply attribute name(layer0rule7class2attribute0) node
    	self.add_node()
    	self.vs[21]["name"] = """name"""
        self.vs[21]["mm__"] = """Attribute"""
        self.vs[21]["Type"] = """'String'"""
        #self.vs[21]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule7class2attribute0')
    	# apply attribute equation name(layer0rule7class2attribute0) node
    	self.add_node()
    	self.vs[22]["name"] = """eq_"""
        self.vs[22]["mm__"] = """Equation"""
        #self.vs[22]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equationlayer0rule7class2attribute0')
    	# apply attribute equation left expr name(layer0rule7class2attribute0) node
    	self.add_node()
    	self.vs[23]["mm__"] = """leftExpr"""
        #self.vs[23]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExprlayer0rule7class2attribute0')
    	# apply attribute equation right expr name(layer0rule7class2attribute0) node
    	self.add_node()
    	self.vs[24]["mm__"] = """rightExpr"""
        #self.vs[24]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExprlayer0rule7class2attribute0')
    	# attribute concat name(layer0rule7class2attribute0) node
    	self.add_node()
    	self.vs[25]["name"] = """Concatlayer0rule7class2attribute025"""
        self.vs[25]["mm__"] = """Concat"""
        self.vs[25]["Type"] = """'String'"""
        #self.vs[25]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concatlayer0rule7class2attribute025')
    	# apply attribute concat has left args name(layer0rule7class2attribute0) node
        self.add_node()
    	self.vs[26]["mm__"] = """hasArgs"""
        #self.vs[26]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgslayer0rule7class2attribute026')
    	# apply attribute concat has right args name(layer0rule7class2attribute0) node
        self.add_node()
    	self.vs[27]["mm__"] = """hasArgs"""
        #self.vs[27]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgslayer0rule7class2attribute027')
    	# attribute concat name(layer0rule7class2attribute0) node
    	self.add_node()
    	self.vs[28]["name"] = """Concatlayer0rule7class2attribute028"""
        self.vs[28]["mm__"] = """Concat"""
        self.vs[28]["Type"] = """'String'"""
        #self.vs[28]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concatlayer0rule7class2attribute028')
    	# apply attribute concat has left args name(layer0rule7class2attribute0) node
        self.add_node()
    	self.vs[29]["mm__"] = """hasArgs"""
        #self.vs[29]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgslayer0rule7class2attribute029')
    	# apply attribute concat has right args name(layer0rule7class2attribute0) node
        self.add_node()
    	self.vs[30]["mm__"] = """hasArgs"""
        #self.vs[30]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgslayer0rule7class2attribute030')
    	# apply attribute atom name(layer0rule7class2attribute0) node
    	self.add_node()
    	self.vs[31]["name"] = """_"""
        self.vs[31]["mm__"] = """Constant"""
        self.vs[31]["Type"] = """'String'"""
        #self.vs[31]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atomlayer0rule7class2attribute031')
    	# attribute concat name(layer0rule7class2attribute0) node
    	self.add_node()
    	self.vs[32]["name"] = """Concatlayer0rule7class2attribute032"""
        self.vs[32]["mm__"] = """Concat"""
        self.vs[32]["Type"] = """'String'"""
        #self.vs[32]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concatlayer0rule7class2attribute032')
    	# apply attribute concat has left args name(layer0rule7class2attribute0) node
        self.add_node()
    	self.vs[33]["mm__"] = """hasArgs"""
        #self.vs[33]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgslayer0rule7class2attribute033')
    	# apply attribute concat has right args name(layer0rule7class2attribute0) node
        self.add_node()
    	self.vs[34]["mm__"] = """hasArgs"""
        #self.vs[34]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgslayer0rule7class2attribute034')
    	# attribute concat name(layer0rule7class2attribute0) node
    	self.add_node()
    	self.vs[35]["name"] = """Concatlayer0rule7class2attribute035"""
        self.vs[35]["mm__"] = """Concat"""
        self.vs[35]["Type"] = """'String'"""
        #self.vs[35]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concatlayer0rule7class2attribute035')
    	# apply attribute concat has left args name(layer0rule7class2attribute0) node
        self.add_node()
    	self.vs[36]["mm__"] = """hasArgs"""
        #self.vs[36]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgslayer0rule7class2attribute036')
    	# apply attribute concat has right args name(layer0rule7class2attribute0) node
        self.add_node()
    	self.vs[37]["mm__"] = """hasArgs"""
        #self.vs[37]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgslayer0rule7class2attribute037')
    	# apply attribute atom name(layer0rule7class2attribute0) node
    	self.add_node()
    	self.vs[38]["name"] = """__"""
        self.vs[38]["mm__"] = """Constant"""
        self.vs[38]["Type"] = """'String'"""
        #self.vs[38]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atomlayer0rule7class2attribute038')
    	# apply attribute atom name(layer0rule7class2attribute0) node
    	self.add_node()
    	self.vs[39]["name"] = """cdata"""
        self.vs[39]["mm__"] = """Constant"""
        self.vs[39]["Type"] = """'String'"""
        #self.vs[39]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atomlayer0rule7class2attribute039')
    	# has apply attribute name(layer0rule7class3attribute0) node
    	self.add_node()
    	self.vs[40]["mm__"] = """hasAttribute_T"""
        #self.vs[40]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer0rule7class3attribute0')
    	# apply attribute name(layer0rule7class3attribute0) node
    	self.add_node()
    	self.vs[41]["name"] = """name"""
        self.vs[41]["mm__"] = """Attribute"""
        self.vs[41]["Type"] = """'String'"""
        #self.vs[41]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule7class3attribute0')
    	# apply attribute equation name(layer0rule7class3attribute0) node
    	self.add_node()
    	self.vs[42]["name"] = """eq_"""
        self.vs[42]["mm__"] = """Equation"""
        #self.vs[42]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equationlayer0rule7class3attribute0')
    	# apply attribute equation left expr name(layer0rule7class3attribute0) node
    	self.add_node()
    	self.vs[43]["mm__"] = """leftExpr"""
        #self.vs[43]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExprlayer0rule7class3attribute0')
    	# apply attribute equation right expr name(layer0rule7class3attribute0) node
    	self.add_node()
    	self.vs[44]["mm__"] = """rightExpr"""
        #self.vs[44]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExprlayer0rule7class3attribute0')
    	# apply attribute atom name(layer0rule7class3attribute0) node
    	self.add_node()
    	self.vs[45]["name"] = """aMemberSoTheStructIsNotEmpty"""
        self.vs[45]["mm__"] = """Constant"""
        self.vs[45]["Type"] = """'String'"""
        #self.vs[45]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atomlayer0rule7class3attribute045')
        
        
        # Add the edges
        self.add_edges([
    		(0,4), # matchmodel -> match_contains
    		(4,3), # match_contains -> match_class AtomicComponent(layer0rule7class0)
    		(0,6), # matchmodel -> match_contains
    		(6,5), # match_contains -> match_class ImplementationModule(layer0rule7class1)
    		(1,8), # applymodel -> apply_contains
    		(8,7), # apply_contains -> apply_class StructDeclaration(layer0rule7class2)
    		(1,10), # applymodel -> apply_contains
    		(10,9), # apply_contains -> apply_class Member(layer0rule7class3)
    		(1,12), # applymodel -> apply_contains
    		(12,11), # apply_contains -> apply_class Int32Type(layer0rule7class4)
    		(5,13), # match_class ImplementationModule(layer0rule7class1) -> association contents
    		(13,3), # association contents  -> match_class AtomicComponent(layer0rule7class0)
    		(7,14), # apply_class StructDeclaration(layer0rule7class2) -> association members
    		(14,9), # association members  -> apply_class Member(layer0rule7class3)
    		(9,15), # apply_class Member(layer0rule7class3) -> association type
    		(15,11), # association type  -> apply_class Int32Type(layer0rule7class4)
    		(3,16), # match_class AtomicComponent(layer0rule7class0) -> has_match_attribute name (layer0rule7class0attribute0)
    		(16,17), #  has_match_attribute name (layer0rule7class0attribute0) -> match_attribute name (layer0rule7class0attribute0)
    		(5,18), # match_class ImplementationModule(layer0rule7class1) -> has_match_attribute name (layer0rule7class1attribute0)
    		(18,19), #  has_match_attribute name (layer0rule7class1attribute0) -> match_attribute name (layer0rule7class1attribute0)
    		(7,20), # apply_class StructDeclaration(layer0rule7class2) -> has_apply_attribute name (layer0rule7class2attribute0)
    		(20,21), #  has_apply_attribute name (layer0rule7class2attribute0) -> apply_attribute name (layer0rule7class2attribute0)
    		(22,23), #  equation of apply attribute name (layer0rule7class2attribute0) -> left_expr
    		(23,21), #  left_expr -> apply_attribute name (layer0rule7class2attribute0)
    		(22,24), #  equation of apply attribute name (layer0rule7class2attribute0) -> right_expr
    		(35,36), #  apply attribute concat name (layer0rule7class2attribute0) -> left has_args  
    		(36,38), #  left has_args -> term
    		(35,37), #  apply attribute concat name (layer0rule7class2attribute0) -> right has_args  
    		(37,39), #  right has_args -> term
    		(32,33), #  apply attribute concat name (layer0rule7class2attribute0) -> left has_args  
    		(33,17), #  left has_args -> term
    		(32,34), #  apply attribute concat name (layer0rule7class2attribute0) -> right has_args  
    		(34,35), #  right has_args -> term
    		(28,29), #  apply attribute concat name (layer0rule7class2attribute0) -> left has_args  
    		(29,31), #  left has_args -> term
    		(28,30), #  apply attribute concat name (layer0rule7class2attribute0) -> right has_args  
    		(30,32), #  right has_args -> term
    		(25,26), #  apply attribute concat name (layer0rule7class2attribute0) -> left has_args  
    		(26,19), #  left has_args -> term
    		(25,27), #  apply attribute concat name (layer0rule7class2attribute0) -> right has_args  
    		(27,28), #  right has_args -> term
    		(24,25), # right_expr --> term
    		(9,40), # apply_class Member(layer0rule7class3) -> has_apply_attribute name (layer0rule7class3attribute0)
    		(40,41), #  has_apply_attribute name (layer0rule7class3attribute0) -> apply_attribute name (layer0rule7class3attribute0)
    		(42,43), #  equation of apply attribute name (layer0rule7class3attribute0) -> left_expr
    		(43,41), #  left_expr -> apply_attribute name (layer0rule7class3attribute0)
    		(42,44), #  equation of apply attribute name (layer0rule7class3attribute0) -> right_expr
    		(44,45), # right_expr --> term
        	(0,2), # matchmodel -> pairedwith
        	(2,1) # pairedwith -> applyModel
        ])
        
