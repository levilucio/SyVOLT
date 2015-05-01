from core.himesis import Himesis
import cPickle as pickle
import uuid

class HEStringToStringMapEntry(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule EStringToStringMapEntry.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HEStringToStringMapEntry, self).__init__(name='HEStringToStringMapEntry', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        # TODO Levi, need some help here because I don't know where does 
        # this value come from.
        self["mm__"] = pickle.loads("""(lp1
S'HimesisMM'
p2
a.""")
        
        self["name"] = """EStringToStringMapEntry"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EStringToStringMapEntry')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EStringToStringMapEntrymatchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EStringToStringMapEntryapplymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EStringToStringMapEntrypairedwith2')
        
    	# match class EStringToStringMapEntry() node
    	self.add_node()
    	self.vs[3]["name"] = """"""
        self.vs[3]["classtype"] = """EStringToStringMapEntry"""
        self.vs[3]["mm__"] = """EStringToStringMapEntry"""
        self.vs[3]["cardinality"] = """+"""
        #self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# match_contains node for class EStringToStringMapEntry()
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        #self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'matchcontains4')
        
        
    	# apply class EStringToStringMapEntry() node
    	self.add_node()
    	self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EStringToStringMapEntry"""
        self.vs[5]["mm__"] = """EStringToStringMapEntry"""
        self.vs[5]["cardinality"] = """1"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply_contains node for class EStringToStringMapEntry()
        self.add_node()
        self.vs[6]["mm__"] = """apply_contains"""
        #self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains6')
        
        
        
        
        
        
    	# has match attribute key() node
    	self.add_node()
    	self.vs[7]["mm__"] = """hasAttribute_S"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# match attribute key() node
    	self.add_node()
    	self.vs[8]["name"] = """key"""
        self.vs[8]["mm__"] = """Attribute"""
        self.vs[8]["Type"] = """'String'"""
        #self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# has match attribute value() node
    	self.add_node()
    	self.vs[9]["mm__"] = """hasAttribute_S"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# match attribute value() node
    	self.add_node()
    	self.vs[10]["name"] = """value"""
        self.vs[10]["mm__"] = """Attribute"""
        self.vs[10]["Type"] = """'String'"""
        #self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        
        
    	# has apply attribute key() node
    	self.add_node()
    	self.vs[11]["mm__"] = """hasAttribute_T"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute key() node
    	self.add_node()
    	self.vs[12]["name"] = """key"""
        self.vs[12]["mm__"] = """Attribute"""
        self.vs[12]["Type"] = """'String'"""
        #self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation key() node
    	self.add_node()
    	self.vs[13]["name"] = """eq_"""
        self.vs[13]["mm__"] = """Equation"""
        #self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr key() node
    	self.add_node()
    	self.vs[14]["mm__"] = """leftExpr"""
        #self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr key() node
    	self.add_node()
    	self.vs[15]["mm__"] = """rightExpr"""
        #self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# has apply attribute value() node
    	self.add_node()
    	self.vs[16]["mm__"] = """hasAttribute_T"""
        #self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute value() node
    	self.add_node()
    	self.vs[17]["name"] = """value"""
        self.vs[17]["mm__"] = """Attribute"""
        self.vs[17]["Type"] = """'String'"""
        #self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation value() node
    	self.add_node()
    	self.vs[18]["name"] = """eq_"""
        self.vs[18]["mm__"] = """Equation"""
        #self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr value() node
    	self.add_node()
    	self.vs[19]["mm__"] = """leftExpr"""
        #self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr value() node
    	self.add_node()
    	self.vs[20]["mm__"] = """rightExpr"""
        #self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
        
        
        # Add the edges
        self.add_edges([
    		(0,4), # matchmodel -> match_contains
    		(4,3), # match_contains -> match_class EStringToStringMapEntry()
    		(1,6), # applymodel -> apply_contains
    		(6,5), # apply_contains -> apply_class EStringToStringMapEntry()
    		(3,7), # match_class EStringToStringMapEntry() -> has_match_attribute key ()
    		(7,8), #  has_match_attribute key () -> match_attribute key ()
    		(3,9), # match_class EStringToStringMapEntry() -> has_match_attribute value ()
    		(9,10), #  has_match_attribute value () -> match_attribute value ()
    		(5,11), # apply_class EStringToStringMapEntry() -> has_apply_attribute key ()
    		(11,12), #  has_apply_attribute key () -> apply_attribute key ()
    		(13,14), #  equation of apply attribute key () -> left_expr
    		(14,12), #  left_expr -> apply_attribute key ()
    		(13,15), #  equation of apply attribute key () -> right_expr
    		(15,8), # right_expr --> term
    		(5,16), # apply_class EStringToStringMapEntry() -> has_apply_attribute value ()
    		(16,17), #  has_apply_attribute value () -> apply_attribute value ()
    		(18,19), #  equation of apply attribute value () -> left_expr
    		(19,17), #  left_expr -> apply_attribute value ()
    		(18,20), #  equation of apply attribute value () -> right_expr
    		(20,10), # right_expr --> term
        	(0,2), # matchmodel -> pairedwith
        	(2,1) # pairedwith -> applyModel
        ])
        
