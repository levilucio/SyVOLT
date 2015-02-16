from core.himesis import Himesis
import cPickle as pickle
import uuid

class Hlayer0rule2(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule layer0rule2.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer0rule2, self).__init__(name='Hlayer0rule2', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        # TODO Levi, need some help here because I don't know where does 
        # this value come from.
        self["mm__"] = pickle.loads("""(lp1
S'HimesisMM'
p2
a.""")
        
        self["name"] = """layer0rule2"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule2')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule2matchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule2applymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule2pairedwith2')
        
    	# match class Operation(layer0rule2class0) node
    	self.add_node()
    	self.vs[3]["name"] = """layer0rule2class0"""
        self.vs[3]["classtype"] = """Operation"""
        self.vs[3]["mm__"] = """Operation"""
        self.vs[3]["cardinality"] = """+"""
        #self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule2class0')
    	# match_contains node for class Operation(layer0rule2class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        #self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule2class0matchcontains4')
    	# match class ClientServerInterface(layer0rule2class1) node
    	self.add_node()
    	self.vs[5]["name"] = """layer0rule2class1"""
        self.vs[5]["classtype"] = """ClientServerInterface"""
        self.vs[5]["mm__"] = """ClientServerInterface"""
        self.vs[5]["cardinality"] = """+"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule2class1')
    	# match_contains node for class ClientServerInterface(layer0rule2class1)
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        #self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule2class1matchcontains6')
        
        
    	# apply class CFunctionPointerStructMember(layer0rule2class2) node
    	self.add_node()
    	self.vs[7]["name"] = """layer0rule2class2"""
        self.vs[7]["classtype"] = """CFunctionPointerStructMember"""
        self.vs[7]["mm__"] = """CFunctionPointerStructMember"""
        self.vs[7]["cardinality"] = """1"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule2class2')
    	# apply_contains node for class CFunctionPointerStructMember(layer0rule2class2)
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        #self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule2class2applycontains8')
    	# apply class FunctionRefType(layer0rule2class3) node
    	self.add_node()
    	self.vs[9]["name"] = """layer0rule2class3"""
        self.vs[9]["classtype"] = """FunctionRefType"""
        self.vs[9]["mm__"] = """FunctionRefType"""
        self.vs[9]["cardinality"] = """1"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule2class3')
    	# apply_contains node for class FunctionRefType(layer0rule2class3)
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        #self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule2class3applycontains10')
        
        
    	# match association ClientServerInterface--contents-->Operation node
    	self.add_node()
    	self.vs[11]["associationType"] = """contents"""
        self.vs[11]["mm__"] = """directLink_S"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule2class1assoc11layer0rule2class0')
        
    	# apply association CFunctionPointerStructMember--type-->FunctionRefType node
    	self.add_node()
    	self.vs[12]["associationType"] = """type"""
        self.vs[12]["mm__"] = """directLink_T"""
        #self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule2class2assoc12layer0rule2class3')
        
        
        
    	# has match attribute name(layer0rule2class0attribute0) node
    	self.add_node()
    	self.vs[13]["mm__"] = """hasAttribute_S"""
        #self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer0rule2class0attribute0')
    	# match attribute name(layer0rule2class0attribute0) node
    	self.add_node()
    	self.vs[14]["name"] = """name"""
        self.vs[14]["mm__"] = """Attribute"""
        self.vs[14]["Type"] = """'String'"""
        #self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule2class0attribute0')
        
        
    	# has apply attribute name(layer0rule2class2attribute0) node
    	self.add_node()
    	self.vs[15]["mm__"] = """hasAttribute_T"""
        #self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer0rule2class2attribute0')
    	# apply attribute name(layer0rule2class2attribute0) node
    	self.add_node()
    	self.vs[16]["name"] = """name"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["Type"] = """'String'"""
        #self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule2class2attribute0')
    	# apply attribute equation name(layer0rule2class2attribute0) node
    	self.add_node()
    	self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        #self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equationlayer0rule2class2attribute0')
    	# apply attribute equation left expr name(layer0rule2class2attribute0) node
    	self.add_node()
    	self.vs[18]["mm__"] = """leftExpr"""
        #self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExprlayer0rule2class2attribute0')
    	# apply attribute equation right expr name(layer0rule2class2attribute0) node
    	self.add_node()
    	self.vs[19]["mm__"] = """rightExpr"""
        #self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExprlayer0rule2class2attribute0')
        
        
        # Add the edges
        self.add_edges([
    		(0,4), # matchmodel -> match_contains
    		(4,3), # match_contains -> match_class Operation(layer0rule2class0)
    		(0,6), # matchmodel -> match_contains
    		(6,5), # match_contains -> match_class ClientServerInterface(layer0rule2class1)
    		(1,8), # applymodel -> apply_contains
    		(8,7), # apply_contains -> apply_class CFunctionPointerStructMember(layer0rule2class2)
    		(1,10), # applymodel -> apply_contains
    		(10,9), # apply_contains -> apply_class FunctionRefType(layer0rule2class3)
    		(5,11), # match_class ClientServerInterface(layer0rule2class1) -> association contents
    		(11,3), # association contents  -> match_class Operation(layer0rule2class0)
    		(7,12), # apply_class CFunctionPointerStructMember(layer0rule2class2) -> association type
    		(12,9), # association type  -> apply_class FunctionRefType(layer0rule2class3)
    		(3,13), # match_class Operation(layer0rule2class0) -> has_match_attribute name (layer0rule2class0attribute0)
    		(13,14), #  has_match_attribute name (layer0rule2class0attribute0) -> match_attribute name (layer0rule2class0attribute0)
    		(7,15), # apply_class CFunctionPointerStructMember(layer0rule2class2) -> has_apply_attribute name (layer0rule2class2attribute0)
    		(15,16), #  has_apply_attribute name (layer0rule2class2attribute0) -> apply_attribute name (layer0rule2class2attribute0)
    		(17,18), #  equation of apply attribute name (layer0rule2class2attribute0) -> left_expr
    		(18,16), #  left_expr -> apply_attribute name (layer0rule2class2attribute0)
    		(17,19), #  equation of apply attribute name (layer0rule2class2attribute0) -> right_expr
    		(19,14), # right_expr --> term
        	(0,2), # matchmodel -> pairedwith
        	(2,1) # pairedwith -> applyModel
        ])
        
