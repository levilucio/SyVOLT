from core.himesis import Himesis
import cPickle as pickle
import uuid

class Hlayer0rule6(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule layer0rule6.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer0rule6, self).__init__(name='Hlayer0rule6', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        # TODO Levi, need some help here because I don't know where does 
        # this value come from.
        self["mm__"] = pickle.loads("""(lp1
S'HimesisMM'
p2
a.""")
        
        self["name"] = """layer0rule6"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule6')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule6matchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule6applymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule6pairedwith2')
        
    	# match class ClientServerInterface(layer0rule6class0) node
    	self.add_node()
    	self.vs[3]["name"] = """layer0rule6class0"""
        self.vs[3]["classtype"] = """ClientServerInterface"""
        self.vs[3]["mm__"] = """ClientServerInterface"""
        self.vs[3]["cardinality"] = """+"""
        #self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule6class0')
    	# match_contains node for class ClientServerInterface(layer0rule6class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        #self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule6class0matchcontains4')
    	# match class ImplementationModule(layer0rule6class1) node
    	self.add_node()
    	self.vs[5]["name"] = """layer0rule6class1"""
        self.vs[5]["classtype"] = """ImplementationModule"""
        self.vs[5]["mm__"] = """ImplementationModule"""
        self.vs[5]["cardinality"] = """+"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule6class1')
    	# match_contains node for class ImplementationModule(layer0rule6class1)
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        #self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule6class1matchcontains6')
        
        
    	# apply class TypeDef(layer0rule6class2) node
    	self.add_node()
    	self.vs[7]["name"] = """layer0rule6class2"""
        self.vs[7]["classtype"] = """TypeDef"""
        self.vs[7]["mm__"] = """TypeDef"""
        self.vs[7]["cardinality"] = """1"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule6class2')
    	# apply_contains node for class TypeDef(layer0rule6class2)
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        #self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule6class2applycontains8')
    	# apply class StructType(layer0rule6class3) node
    	self.add_node()
    	self.vs[9]["name"] = """layer0rule6class3"""
        self.vs[9]["classtype"] = """StructType"""
        self.vs[9]["mm__"] = """StructType"""
        self.vs[9]["cardinality"] = """1"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule6class3')
    	# apply_contains node for class StructType(layer0rule6class3)
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        #self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule6class3applycontains10')
        
        
    	# match association ImplementationModule--contents-->ClientServerInterface node
    	self.add_node()
    	self.vs[11]["associationType"] = """contents"""
        self.vs[11]["mm__"] = """directLink_S"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule6class1assoc11layer0rule6class0')
        
    	# apply association TypeDef--original-->StructType node
    	self.add_node()
    	self.vs[12]["associationType"] = """original"""
        self.vs[12]["mm__"] = """directLink_T"""
        #self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule6class2assoc12layer0rule6class3')
        
        
        
    	# has match attribute name(layer0rule6class0attribute0) node
    	self.add_node()
    	self.vs[13]["mm__"] = """hasAttribute_S"""
        #self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer0rule6class0attribute0')
    	# match attribute name(layer0rule6class0attribute0) node
    	self.add_node()
    	self.vs[14]["name"] = """name"""
        self.vs[14]["mm__"] = """Attribute"""
        self.vs[14]["Type"] = """'String'"""
        #self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule6class0attribute0')
    	# has match attribute name(layer0rule6class1attribute0) node
    	self.add_node()
    	self.vs[15]["mm__"] = """hasAttribute_S"""
        #self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer0rule6class1attribute0')
    	# match attribute name(layer0rule6class1attribute0) node
    	self.add_node()
    	self.vs[16]["name"] = """name"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["Type"] = """'String'"""
        #self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule6class1attribute0')
        
        
    	# has apply attribute name(layer0rule6class2attribute0) node
    	self.add_node()
    	self.vs[17]["mm__"] = """hasAttribute_T"""
        #self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer0rule6class2attribute0')
    	# apply attribute name(layer0rule6class2attribute0) node
    	self.add_node()
    	self.vs[18]["name"] = """name"""
        self.vs[18]["mm__"] = """Attribute"""
        self.vs[18]["Type"] = """'String'"""
        #self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule6class2attribute0')
    	# apply attribute equation name(layer0rule6class2attribute0) node
    	self.add_node()
    	self.vs[19]["name"] = """eq_"""
        self.vs[19]["mm__"] = """Equation"""
        #self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equationlayer0rule6class2attribute0')
    	# apply attribute equation left expr name(layer0rule6class2attribute0) node
    	self.add_node()
    	self.vs[20]["mm__"] = """leftExpr"""
        #self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExprlayer0rule6class2attribute0')
    	# apply attribute equation right expr name(layer0rule6class2attribute0) node
    	self.add_node()
    	self.vs[21]["mm__"] = """rightExpr"""
        #self.vs[21]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExprlayer0rule6class2attribute0')
    	# attribute concat name(layer0rule6class2attribute0) node
    	self.add_node()
    	self.vs[22]["name"] = """Concatlayer0rule6class2attribute022"""
        self.vs[22]["mm__"] = """Concat"""
        self.vs[22]["Type"] = """'String'"""
        #self.vs[22]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concatlayer0rule6class2attribute022')
    	# apply attribute concat has left args name(layer0rule6class2attribute0) node
        self.add_node()
    	self.vs[23]["mm__"] = """hasArgs"""
        #self.vs[23]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgslayer0rule6class2attribute023')
    	# apply attribute concat has right args name(layer0rule6class2attribute0) node
        self.add_node()
    	self.vs[24]["mm__"] = """hasArgs"""
        #self.vs[24]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgslayer0rule6class2attribute024')
    	# attribute concat name(layer0rule6class2attribute0) node
    	self.add_node()
    	self.vs[25]["name"] = """Concatlayer0rule6class2attribute025"""
        self.vs[25]["mm__"] = """Concat"""
        self.vs[25]["Type"] = """'String'"""
        #self.vs[25]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concatlayer0rule6class2attribute025')
    	# apply attribute concat has left args name(layer0rule6class2attribute0) node
        self.add_node()
    	self.vs[26]["mm__"] = """hasArgs"""
        #self.vs[26]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgslayer0rule6class2attribute026')
    	# apply attribute concat has right args name(layer0rule6class2attribute0) node
        self.add_node()
    	self.vs[27]["mm__"] = """hasArgs"""
        #self.vs[27]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgslayer0rule6class2attribute027')
    	# apply attribute atom name(layer0rule6class2attribute0) node
    	self.add_node()
    	self.vs[28]["name"] = """_"""
        self.vs[28]["mm__"] = """Constant"""
        self.vs[28]["Type"] = """'String'"""
        #self.vs[28]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atomlayer0rule6class2attribute028')
    	# attribute concat name(layer0rule6class2attribute0) node
    	self.add_node()
    	self.vs[29]["name"] = """Concatlayer0rule6class2attribute029"""
        self.vs[29]["mm__"] = """Concat"""
        self.vs[29]["Type"] = """'String'"""
        #self.vs[29]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concatlayer0rule6class2attribute029')
    	# apply attribute concat has left args name(layer0rule6class2attribute0) node
        self.add_node()
    	self.vs[30]["mm__"] = """hasArgs"""
        #self.vs[30]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgslayer0rule6class2attribute030')
    	# apply attribute concat has right args name(layer0rule6class2attribute0) node
        self.add_node()
    	self.vs[31]["mm__"] = """hasArgs"""
        #self.vs[31]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgslayer0rule6class2attribute031')
    	# attribute concat name(layer0rule6class2attribute0) node
    	self.add_node()
    	self.vs[32]["name"] = """Concatlayer0rule6class2attribute032"""
        self.vs[32]["mm__"] = """Concat"""
        self.vs[32]["Type"] = """'String'"""
        #self.vs[32]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concatlayer0rule6class2attribute032')
    	# apply attribute concat has left args name(layer0rule6class2attribute0) node
        self.add_node()
    	self.vs[33]["mm__"] = """hasArgs"""
        #self.vs[33]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgslayer0rule6class2attribute033')
    	# apply attribute concat has right args name(layer0rule6class2attribute0) node
        self.add_node()
    	self.vs[34]["mm__"] = """hasArgs"""
        #self.vs[34]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgslayer0rule6class2attribute034')
    	# apply attribute atom name(layer0rule6class2attribute0) node
    	self.add_node()
    	self.vs[35]["name"] = """__"""
        self.vs[35]["mm__"] = """Constant"""
        self.vs[35]["Type"] = """'String'"""
        #self.vs[35]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atomlayer0rule6class2attribute035')
    	# apply attribute atom name(layer0rule6class2attribute0) node
    	self.add_node()
    	self.vs[36]["name"] = """idata_t"""
        self.vs[36]["mm__"] = """Constant"""
        self.vs[36]["Type"] = """'String'"""
        #self.vs[36]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atomlayer0rule6class2attribute036')
        
        
        # Add the edges
        self.add_edges([
    		(0,4), # matchmodel -> match_contains
    		(4,3), # match_contains -> match_class ClientServerInterface(layer0rule6class0)
    		(0,6), # matchmodel -> match_contains
    		(6,5), # match_contains -> match_class ImplementationModule(layer0rule6class1)
    		(1,8), # applymodel -> apply_contains
    		(8,7), # apply_contains -> apply_class TypeDef(layer0rule6class2)
    		(1,10), # applymodel -> apply_contains
    		(10,9), # apply_contains -> apply_class StructType(layer0rule6class3)
    		(5,11), # match_class ImplementationModule(layer0rule6class1) -> association contents
    		(11,3), # association contents  -> match_class ClientServerInterface(layer0rule6class0)
    		(7,12), # apply_class TypeDef(layer0rule6class2) -> association original
    		(12,9), # association original  -> apply_class StructType(layer0rule6class3)
    		(3,13), # match_class ClientServerInterface(layer0rule6class0) -> has_match_attribute name (layer0rule6class0attribute0)
    		(13,14), #  has_match_attribute name (layer0rule6class0attribute0) -> match_attribute name (layer0rule6class0attribute0)
    		(5,15), # match_class ImplementationModule(layer0rule6class1) -> has_match_attribute name (layer0rule6class1attribute0)
    		(15,16), #  has_match_attribute name (layer0rule6class1attribute0) -> match_attribute name (layer0rule6class1attribute0)
    		(7,17), # apply_class TypeDef(layer0rule6class2) -> has_apply_attribute name (layer0rule6class2attribute0)
    		(17,18), #  has_apply_attribute name (layer0rule6class2attribute0) -> apply_attribute name (layer0rule6class2attribute0)
    		(19,20), #  equation of apply attribute name (layer0rule6class2attribute0) -> left_expr
    		(20,18), #  left_expr -> apply_attribute name (layer0rule6class2attribute0)
    		(19,21), #  equation of apply attribute name (layer0rule6class2attribute0) -> right_expr
    		(32,33), #  apply attribute concat name (layer0rule6class2attribute0) -> left has_args  
    		(33,35), #  left has_args -> term
    		(32,34), #  apply attribute concat name (layer0rule6class2attribute0) -> right has_args  
    		(34,36), #  right has_args -> term
    		(29,30), #  apply attribute concat name (layer0rule6class2attribute0) -> left has_args  
    		(30,14), #  left has_args -> term
    		(29,31), #  apply attribute concat name (layer0rule6class2attribute0) -> right has_args  
    		(31,32), #  right has_args -> term
    		(25,26), #  apply attribute concat name (layer0rule6class2attribute0) -> left has_args  
    		(26,28), #  left has_args -> term
    		(25,27), #  apply attribute concat name (layer0rule6class2attribute0) -> right has_args  
    		(27,29), #  right has_args -> term
    		(22,23), #  apply attribute concat name (layer0rule6class2attribute0) -> left has_args  
    		(23,16), #  left has_args -> term
    		(22,24), #  apply attribute concat name (layer0rule6class2attribute0) -> right has_args  
    		(24,25), #  right has_args -> term
    		(21,22), # right_expr --> term
        	(0,2), # matchmodel -> pairedwith
        	(2,1) # pairedwith -> applyModel
        ])
        
