from core.himesis import Himesis
import cPickle as pickle
import uuid

class Hlayer0rule1(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule layer0rule1.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer0rule1, self).__init__(name='Hlayer0rule1', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        # TODO Levi, need some help here because I don't know where does 
        # this value come from.
        self["mm__"] = pickle.loads("""(lp1
S'HimesisMM'
p2
a.""")
        
        self["name"] = """layer0rule1"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule1')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule1matchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule1applymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule1pairedwith2')
        
    	# match class ClientServerInterface(layer0rule1class0) node
    	self.add_node()
    	self.vs[3]["name"] = """layer0rule1class0"""
        self.vs[3]["classtype"] = """ClientServerInterface"""
        self.vs[3]["mm__"] = """ClientServerInterface"""
        self.vs[3]["cardinality"] = """+"""
        #self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule1class0')
    	# match_contains node for class ClientServerInterface(layer0rule1class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        #self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule1class0matchcontains4')
    	# match class ImplementationModule(layer0rule1class1) node
    	self.add_node()
    	self.vs[5]["name"] = """layer0rule1class1"""
        self.vs[5]["classtype"] = """ImplementationModule"""
        self.vs[5]["mm__"] = """ImplementationModule"""
        self.vs[5]["cardinality"] = """+"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule1class1')
    	# match_contains node for class ImplementationModule(layer0rule1class1)
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        #self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule1class1matchcontains6')
        
        
    	# apply class StructDeclaration(layer0rule1class2) node
    	self.add_node()
    	self.vs[7]["name"] = """layer0rule1class2"""
        self.vs[7]["classtype"] = """StructDeclaration"""
        self.vs[7]["mm__"] = """StructDeclaration"""
        self.vs[7]["cardinality"] = """1"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule1class2')
    	# apply_contains node for class StructDeclaration(layer0rule1class2)
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        #self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule1class2applycontains8')
        
        
    	# match association ImplementationModule--contents-->ClientServerInterface node
    	self.add_node()
    	self.vs[9]["associationType"] = """contents"""
        self.vs[9]["mm__"] = """directLink_S"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule1class1assoc9layer0rule1class0')
        
        
        
        
    	# has match attribute name(layer0rule1class0attribute0) node
    	self.add_node()
    	self.vs[10]["mm__"] = """hasAttribute_S"""
        #self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer0rule1class0attribute0')
    	# match attribute name(layer0rule1class0attribute0) node
    	self.add_node()
    	self.vs[11]["name"] = """name"""
        self.vs[11]["mm__"] = """Attribute"""
        self.vs[11]["Type"] = """'String'"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule1class0attribute0')
    	# has match attribute name(layer0rule1class1attribute0) node
    	self.add_node()
    	self.vs[12]["mm__"] = """hasAttribute_S"""
        #self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer0rule1class1attribute0')
    	# match attribute name(layer0rule1class1attribute0) node
    	self.add_node()
    	self.vs[13]["name"] = """name"""
        self.vs[13]["mm__"] = """Attribute"""
        self.vs[13]["Type"] = """'String'"""
        #self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule1class1attribute0')
        
        
    	# has apply attribute name(layer0rule1class2attribute0) node
    	self.add_node()
    	self.vs[14]["mm__"] = """hasAttribute_T"""
        #self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer0rule1class2attribute0')
    	# apply attribute name(layer0rule1class2attribute0) node
    	self.add_node()
    	self.vs[15]["name"] = """name"""
        self.vs[15]["mm__"] = """Attribute"""
        self.vs[15]["Type"] = """'String'"""
        #self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule1class2attribute0')
    	# apply attribute equation name(layer0rule1class2attribute0) node
    	self.add_node()
    	self.vs[16]["name"] = """eq_"""
        self.vs[16]["mm__"] = """Equation"""
        #self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equationlayer0rule1class2attribute0')
    	# apply attribute equation left expr name(layer0rule1class2attribute0) node
    	self.add_node()
    	self.vs[17]["mm__"] = """leftExpr"""
        #self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExprlayer0rule1class2attribute0')
    	# apply attribute equation right expr name(layer0rule1class2attribute0) node
    	self.add_node()
    	self.vs[18]["mm__"] = """rightExpr"""
        #self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExprlayer0rule1class2attribute0')
    	# attribute concat name(layer0rule1class2attribute0) node
    	self.add_node()
    	self.vs[19]["name"] = """Concatlayer0rule1class2attribute019"""
        self.vs[19]["mm__"] = """Concat"""
        self.vs[19]["Type"] = """'String'"""
        #self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concatlayer0rule1class2attribute019')
    	# apply attribute concat has left args name(layer0rule1class2attribute0) node
        self.add_node()
    	self.vs[20]["mm__"] = """hasArgs"""
        #self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgslayer0rule1class2attribute020')
    	# apply attribute concat has right args name(layer0rule1class2attribute0) node
        self.add_node()
    	self.vs[21]["mm__"] = """hasArgs"""
        #self.vs[21]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgslayer0rule1class2attribute021')
    	# attribute concat name(layer0rule1class2attribute0) node
    	self.add_node()
    	self.vs[22]["name"] = """Concatlayer0rule1class2attribute022"""
        self.vs[22]["mm__"] = """Concat"""
        self.vs[22]["Type"] = """'String'"""
        #self.vs[22]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concatlayer0rule1class2attribute022')
    	# apply attribute concat has left args name(layer0rule1class2attribute0) node
        self.add_node()
    	self.vs[23]["mm__"] = """hasArgs"""
        #self.vs[23]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgslayer0rule1class2attribute023')
    	# apply attribute concat has right args name(layer0rule1class2attribute0) node
        self.add_node()
    	self.vs[24]["mm__"] = """hasArgs"""
        #self.vs[24]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgslayer0rule1class2attribute024')
    	# apply attribute atom name(layer0rule1class2attribute0) node
    	self.add_node()
    	self.vs[25]["name"] = """_"""
        self.vs[25]["mm__"] = """Constant"""
        self.vs[25]["Type"] = """'String'"""
        #self.vs[25]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atomlayer0rule1class2attribute025')
    	# attribute concat name(layer0rule1class2attribute0) node
    	self.add_node()
    	self.vs[26]["name"] = """Concatlayer0rule1class2attribute026"""
        self.vs[26]["mm__"] = """Concat"""
        self.vs[26]["Type"] = """'String'"""
        #self.vs[26]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concatlayer0rule1class2attribute026')
    	# apply attribute concat has left args name(layer0rule1class2attribute0) node
        self.add_node()
    	self.vs[27]["mm__"] = """hasArgs"""
        #self.vs[27]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgslayer0rule1class2attribute027')
    	# apply attribute concat has right args name(layer0rule1class2attribute0) node
        self.add_node()
    	self.vs[28]["mm__"] = """hasArgs"""
        #self.vs[28]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgslayer0rule1class2attribute028')
    	# attribute concat name(layer0rule1class2attribute0) node
    	self.add_node()
    	self.vs[29]["name"] = """Concatlayer0rule1class2attribute029"""
        self.vs[29]["mm__"] = """Concat"""
        self.vs[29]["Type"] = """'String'"""
        #self.vs[29]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concatlayer0rule1class2attribute029')
    	# apply attribute concat has left args name(layer0rule1class2attribute0) node
        self.add_node()
    	self.vs[30]["mm__"] = """hasArgs"""
        #self.vs[30]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgslayer0rule1class2attribute030')
    	# apply attribute concat has right args name(layer0rule1class2attribute0) node
        self.add_node()
    	self.vs[31]["mm__"] = """hasArgs"""
        #self.vs[31]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgslayer0rule1class2attribute031')
    	# apply attribute atom name(layer0rule1class2attribute0) node
    	self.add_node()
    	self.vs[32]["name"] = """__"""
        self.vs[32]["mm__"] = """Constant"""
        self.vs[32]["Type"] = """'String'"""
        #self.vs[32]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atomlayer0rule1class2attribute032')
    	# apply attribute atom name(layer0rule1class2attribute0) node
    	self.add_node()
    	self.vs[33]["name"] = """idata"""
        self.vs[33]["mm__"] = """Constant"""
        self.vs[33]["Type"] = """'String'"""
        #self.vs[33]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atomlayer0rule1class2attribute033')
        
        
        # Add the edges
        self.add_edges([
    		(0,4), # matchmodel -> match_contains
    		(4,3), # match_contains -> match_class ClientServerInterface(layer0rule1class0)
    		(0,6), # matchmodel -> match_contains
    		(6,5), # match_contains -> match_class ImplementationModule(layer0rule1class1)
    		(1,8), # applymodel -> apply_contains
    		(8,7), # apply_contains -> apply_class StructDeclaration(layer0rule1class2)
    		(5,9), # match_class ImplementationModule(layer0rule1class1) -> association contents
    		(9,3), # association contents  -> match_class ClientServerInterface(layer0rule1class0)
    		(3,10), # match_class ClientServerInterface(layer0rule1class0) -> has_match_attribute name (layer0rule1class0attribute0)
    		(10,11), #  has_match_attribute name (layer0rule1class0attribute0) -> match_attribute name (layer0rule1class0attribute0)
    		(5,12), # match_class ImplementationModule(layer0rule1class1) -> has_match_attribute name (layer0rule1class1attribute0)
    		(12,13), #  has_match_attribute name (layer0rule1class1attribute0) -> match_attribute name (layer0rule1class1attribute0)
    		(7,14), # apply_class StructDeclaration(layer0rule1class2) -> has_apply_attribute name (layer0rule1class2attribute0)
    		(14,15), #  has_apply_attribute name (layer0rule1class2attribute0) -> apply_attribute name (layer0rule1class2attribute0)
    		(16,17), #  equation of apply attribute name (layer0rule1class2attribute0) -> left_expr
    		(17,15), #  left_expr -> apply_attribute name (layer0rule1class2attribute0)
    		(16,18), #  equation of apply attribute name (layer0rule1class2attribute0) -> right_expr
    		(29,30), #  apply attribute concat name (layer0rule1class2attribute0) -> left has_args  
    		(30,32), #  left has_args -> term
    		(29,31), #  apply attribute concat name (layer0rule1class2attribute0) -> right has_args  
    		(31,33), #  right has_args -> term
    		(26,27), #  apply attribute concat name (layer0rule1class2attribute0) -> left has_args  
    		(27,11), #  left has_args -> term
    		(26,28), #  apply attribute concat name (layer0rule1class2attribute0) -> right has_args  
    		(28,29), #  right has_args -> term
    		(22,23), #  apply attribute concat name (layer0rule1class2attribute0) -> left has_args  
    		(23,25), #  left has_args -> term
    		(22,24), #  apply attribute concat name (layer0rule1class2attribute0) -> right has_args  
    		(24,26), #  right has_args -> term
    		(19,20), #  apply attribute concat name (layer0rule1class2attribute0) -> left has_args  
    		(20,13), #  left has_args -> term
    		(19,21), #  apply attribute concat name (layer0rule1class2attribute0) -> right has_args  
    		(21,22), #  right has_args -> term
    		(18,19), # right_expr --> term
        	(0,2), # matchmodel -> pairedwith
        	(2,1) # pairedwith -> applyModel
        ])
        
