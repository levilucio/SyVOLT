from core.himesis import Himesis
import cPickle as pickle
import uuid

class Hlayer0rule9(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule layer0rule9.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer0rule9, self).__init__(name='Hlayer0rule9', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        # TODO Levi, need some help here because I don't know where does 
        # this value come from.
        self["mm__"] = pickle.loads("""(lp1
S'HimesisMM'
p2
a.""")
        
        self["name"] = """layer0rule9"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule9')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule9matchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule9applymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule9pairedwith2')
        
    	# match class RequiredPort(layer0rule9class0) node
    	self.add_node()
    	self.vs[3]["name"] = """layer0rule9class0"""
        self.vs[3]["classtype"] = """RequiredPort"""
        self.vs[3]["mm__"] = """RequiredPort"""
        self.vs[3]["cardinality"] = """+"""
        #self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule9class0')
    	# match_contains node for class RequiredPort(layer0rule9class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        #self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule9class0matchcontains4')
        
        
    	# apply class Member(layer0rule9class1) node
    	self.add_node()
    	self.vs[5]["name"] = """layer0rule9class1"""
        self.vs[5]["classtype"] = """Member"""
        self.vs[5]["mm__"] = """Member"""
        self.vs[5]["cardinality"] = """1"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule9class1')
    	# apply_contains node for class Member(layer0rule9class1)
        self.add_node()
        self.vs[6]["mm__"] = """apply_contains"""
        #self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule9class1applycontains6')
    	# apply class VoidType(layer0rule9class2) node
    	self.add_node()
    	self.vs[7]["name"] = """layer0rule9class2"""
        self.vs[7]["classtype"] = """VoidType"""
        self.vs[7]["mm__"] = """VoidType"""
        self.vs[7]["cardinality"] = """1"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule9class2')
    	# apply_contains node for class VoidType(layer0rule9class2)
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        #self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule9class2applycontains8')
    	# apply class PointerType(layer0rule9class3) node
    	self.add_node()
    	self.vs[9]["name"] = """layer0rule9class3"""
        self.vs[9]["classtype"] = """PointerType"""
        self.vs[9]["mm__"] = """PointerType"""
        self.vs[9]["cardinality"] = """1"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule9class3')
    	# apply_contains node for class PointerType(layer0rule9class3)
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        #self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule9class3applycontains10')
        
        
        
    	# apply association Member--type-->PointerType node
    	self.add_node()
    	self.vs[11]["associationType"] = """type"""
        self.vs[11]["mm__"] = """directLink_T"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule9class1assoc11layer0rule9class3')
    	# apply association PointerType--baseType-->VoidType node
    	self.add_node()
    	self.vs[12]["associationType"] = """baseType"""
        self.vs[12]["mm__"] = """directLink_T"""
        #self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule9class3assoc12layer0rule9class2')
        
        
        
    	# has match attribute name(layer0rule9class0attribute0) node
    	self.add_node()
    	self.vs[13]["mm__"] = """hasAttribute_S"""
        #self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer0rule9class0attribute0')
    	# match attribute name(layer0rule9class0attribute0) node
    	self.add_node()
    	self.vs[14]["name"] = """name"""
        self.vs[14]["mm__"] = """Attribute"""
        self.vs[14]["Type"] = """'String'"""
        #self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule9class0attribute0')
        
        
    	# has apply attribute name(layer0rule9class1attribute0) node
    	self.add_node()
    	self.vs[15]["mm__"] = """hasAttribute_T"""
        #self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer0rule9class1attribute0')
    	# apply attribute name(layer0rule9class1attribute0) node
    	self.add_node()
    	self.vs[16]["name"] = """name"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["Type"] = """'String'"""
        #self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule9class1attribute0')
    	# apply attribute equation name(layer0rule9class1attribute0) node
    	self.add_node()
    	self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        #self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equationlayer0rule9class1attribute0')
    	# apply attribute equation left expr name(layer0rule9class1attribute0) node
    	self.add_node()
    	self.vs[18]["mm__"] = """leftExpr"""
        #self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExprlayer0rule9class1attribute0')
    	# apply attribute equation right expr name(layer0rule9class1attribute0) node
    	self.add_node()
    	self.vs[19]["mm__"] = """rightExpr"""
        #self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExprlayer0rule9class1attribute0')
    	# attribute concat name(layer0rule9class1attribute0) node
    	self.add_node()
    	self.vs[20]["name"] = """Concatlayer0rule9class1attribute020"""
        self.vs[20]["mm__"] = """Concat"""
        self.vs[20]["Type"] = """'String'"""
        #self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concatlayer0rule9class1attribute020')
    	# apply attribute concat has left args name(layer0rule9class1attribute0) node
        self.add_node()
    	self.vs[21]["mm__"] = """hasArgs"""
        #self.vs[21]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgslayer0rule9class1attribute021')
    	# apply attribute concat has right args name(layer0rule9class1attribute0) node
        self.add_node()
    	self.vs[22]["mm__"] = """hasArgs"""
        #self.vs[22]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgslayer0rule9class1attribute022')
    	# apply attribute atom name(layer0rule9class1attribute0) node
    	self.add_node()
    	self.vs[23]["name"] = """__port"""
        self.vs[23]["mm__"] = """Constant"""
        self.vs[23]["Type"] = """'String'"""
        #self.vs[23]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atomlayer0rule9class1attribute023')
        
        
        # Add the edges
        self.add_edges([
    		(0,4), # matchmodel -> match_contains
    		(4,3), # match_contains -> match_class RequiredPort(layer0rule9class0)
    		(1,6), # applymodel -> apply_contains
    		(6,5), # apply_contains -> apply_class Member(layer0rule9class1)
    		(1,8), # applymodel -> apply_contains
    		(8,7), # apply_contains -> apply_class VoidType(layer0rule9class2)
    		(1,10), # applymodel -> apply_contains
    		(10,9), # apply_contains -> apply_class PointerType(layer0rule9class3)
    		(5,11), # apply_class Member(layer0rule9class1) -> association type
    		(11,9), # association type  -> apply_class PointerType(layer0rule9class3)
    		(9,12), # apply_class PointerType(layer0rule9class3) -> association baseType
    		(12,7), # association baseType  -> apply_class VoidType(layer0rule9class2)
    		(3,13), # match_class RequiredPort(layer0rule9class0) -> has_match_attribute name (layer0rule9class0attribute0)
    		(13,14), #  has_match_attribute name (layer0rule9class0attribute0) -> match_attribute name (layer0rule9class0attribute0)
    		(5,15), # apply_class Member(layer0rule9class1) -> has_apply_attribute name (layer0rule9class1attribute0)
    		(15,16), #  has_apply_attribute name (layer0rule9class1attribute0) -> apply_attribute name (layer0rule9class1attribute0)
    		(17,18), #  equation of apply attribute name (layer0rule9class1attribute0) -> left_expr
    		(18,16), #  left_expr -> apply_attribute name (layer0rule9class1attribute0)
    		(17,19), #  equation of apply attribute name (layer0rule9class1attribute0) -> right_expr
    		(20,21), #  apply attribute concat name (layer0rule9class1attribute0) -> left has_args  
    		(21,14), #  left has_args -> term
    		(20,22), #  apply attribute concat name (layer0rule9class1attribute0) -> right has_args  
    		(22,23), #  right has_args -> term
    		(19,20), # right_expr --> term
        	(0,2), # matchmodel -> pairedwith
        	(2,1) # pairedwith -> applyModel
        ])
        
