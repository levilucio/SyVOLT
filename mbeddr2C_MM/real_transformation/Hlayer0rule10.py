from core.himesis import Himesis
import cPickle as pickle
import uuid

class Hlayer0rule10(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule layer0rule10.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer0rule10, self).__init__(name='Hlayer0rule10', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        # TODO Levi, need some help here because I don't know where does 
        # this value come from.
        self["mm__"] = pickle.loads("""(lp1
S'HimesisMM'
p2
a.""")
        
        self["name"] = """layer0rule10"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule10')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule10matchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule10applymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule10pairedwith2')
        
    	# match class RequiredPort(layer0rule10class0) node
    	self.add_node()
    	self.vs[3]["name"] = """layer0rule10class0"""
        self.vs[3]["classtype"] = """RequiredPort"""
        self.vs[3]["mm__"] = """RequiredPort"""
        self.vs[3]["cardinality"] = """+"""
        #self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule10class0')
    	# match_contains node for class RequiredPort(layer0rule10class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        #self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule10class0matchcontains4')
        
        
    	# apply class Member(layer0rule10class1) node
    	self.add_node()
    	self.vs[5]["name"] = """layer0rule10class1"""
        self.vs[5]["classtype"] = """Member"""
        self.vs[5]["mm__"] = """Member"""
        self.vs[5]["cardinality"] = """1"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule10class1')
    	# apply_contains node for class Member(layer0rule10class1)
        self.add_node()
        self.vs[6]["mm__"] = """apply_contains"""
        #self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule10class1applycontains6')
        
        
        
        
        
        
    	# has match attribute name(layer0rule10class0attribute0) node
    	self.add_node()
    	self.vs[7]["mm__"] = """hasAttribute_S"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer0rule10class0attribute0')
    	# match attribute name(layer0rule10class0attribute0) node
    	self.add_node()
    	self.vs[8]["name"] = """name"""
        self.vs[8]["mm__"] = """Attribute"""
        self.vs[8]["Type"] = """'String'"""
        #self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule10class0attribute0')
        
        
    	# has apply attribute name(layer0rule10class1attribute0) node
    	self.add_node()
    	self.vs[9]["mm__"] = """hasAttribute_T"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer0rule10class1attribute0')
    	# apply attribute name(layer0rule10class1attribute0) node
    	self.add_node()
    	self.vs[10]["name"] = """name"""
        self.vs[10]["mm__"] = """Attribute"""
        self.vs[10]["Type"] = """'String'"""
        #self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule10class1attribute0')
    	# apply attribute equation name(layer0rule10class1attribute0) node
    	self.add_node()
    	self.vs[11]["name"] = """eq_"""
        self.vs[11]["mm__"] = """Equation"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equationlayer0rule10class1attribute0')
    	# apply attribute equation left expr name(layer0rule10class1attribute0) node
    	self.add_node()
    	self.vs[12]["mm__"] = """leftExpr"""
        #self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExprlayer0rule10class1attribute0')
    	# apply attribute equation right expr name(layer0rule10class1attribute0) node
    	self.add_node()
    	self.vs[13]["mm__"] = """rightExpr"""
        #self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExprlayer0rule10class1attribute0')
    	# attribute concat name(layer0rule10class1attribute0) node
    	self.add_node()
    	self.vs[14]["name"] = """Concatlayer0rule10class1attribute014"""
        self.vs[14]["mm__"] = """Concat"""
        self.vs[14]["Type"] = """'String'"""
        #self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concatlayer0rule10class1attribute014')
    	# apply attribute concat has left args name(layer0rule10class1attribute0) node
        self.add_node()
    	self.vs[15]["mm__"] = """hasArgs"""
        #self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgslayer0rule10class1attribute015')
    	# apply attribute concat has right args name(layer0rule10class1attribute0) node
        self.add_node()
    	self.vs[16]["mm__"] = """hasArgs"""
        #self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgslayer0rule10class1attribute016')
    	# apply attribute atom name(layer0rule10class1attribute0) node
    	self.add_node()
    	self.vs[17]["name"] = """__ops"""
        self.vs[17]["mm__"] = """Constant"""
        self.vs[17]["Type"] = """'String'"""
        #self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atomlayer0rule10class1attribute017')
        
        
        # Add the edges
        self.add_edges([
    		(0,4), # matchmodel -> match_contains
    		(4,3), # match_contains -> match_class RequiredPort(layer0rule10class0)
    		(1,6), # applymodel -> apply_contains
    		(6,5), # apply_contains -> apply_class Member(layer0rule10class1)
    		(3,7), # match_class RequiredPort(layer0rule10class0) -> has_match_attribute name (layer0rule10class0attribute0)
    		(7,8), #  has_match_attribute name (layer0rule10class0attribute0) -> match_attribute name (layer0rule10class0attribute0)
    		(5,9), # apply_class Member(layer0rule10class1) -> has_apply_attribute name (layer0rule10class1attribute0)
    		(9,10), #  has_apply_attribute name (layer0rule10class1attribute0) -> apply_attribute name (layer0rule10class1attribute0)
    		(11,12), #  equation of apply attribute name (layer0rule10class1attribute0) -> left_expr
    		(12,10), #  left_expr -> apply_attribute name (layer0rule10class1attribute0)
    		(11,13), #  equation of apply attribute name (layer0rule10class1attribute0) -> right_expr
    		(14,15), #  apply attribute concat name (layer0rule10class1attribute0) -> left has_args  
    		(15,8), #  left has_args -> term
    		(14,16), #  apply attribute concat name (layer0rule10class1attribute0) -> right has_args  
    		(16,17), #  right has_args -> term
    		(13,14), # right_expr --> term
        	(0,2), # matchmodel -> pairedwith
        	(2,1) # pairedwith -> applyModel
        ])
        
