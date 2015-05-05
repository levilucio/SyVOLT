from core.himesis import Himesis
import cPickle as pickle
import uuid

class HEDataType(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule EDataType.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HEDataType, self).__init__(name='HEDataType', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        # TODO Levi, need some help here because I don't know where does 
        # this value come from.
        self["mm__"] = pickle.loads("""(lp1
S'HimesisMM'
p2
a.""")
        
        self["name"] = """EDataType"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EDataType')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EDataTypematchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EDataTypeapplymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EDataTypepairedwith2')
        
    	# match class EDataType() node
    	self.add_node()
    	self.vs[3]["name"] = """"""
        self.vs[3]["classtype"] = """EDataType"""
        self.vs[3]["mm__"] = """EDataType"""
        self.vs[3]["cardinality"] = """+"""
        #self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# match_contains node for class EDataType()
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        #self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'matchcontains4')
        
        
    	# apply class EDataType() node
    	self.add_node()
    	self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EDataType"""
        self.vs[5]["mm__"] = """EDataType"""
        self.vs[5]["cardinality"] = """1"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply_contains node for class EDataType()
        self.add_node()
        self.vs[6]["mm__"] = """apply_contains"""
        #self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains6')
        
        
        
        
        
        
    	# has match attribute name() node
    	self.add_node()
    	self.vs[7]["mm__"] = """hasAttribute_S"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# match attribute name() node
    	self.add_node()
    	self.vs[8]["name"] = """name"""
        self.vs[8]["mm__"] = """Attribute"""
        self.vs[8]["Type"] = """'String'"""
        #self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# has match attribute instanceClassName() node
    	self.add_node()
    	self.vs[9]["mm__"] = """hasAttribute_S"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# match attribute instanceClassName() node
    	self.add_node()
    	self.vs[10]["name"] = """instanceClassName"""
        self.vs[10]["mm__"] = """Attribute"""
        self.vs[10]["Type"] = """'String'"""
        #self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# has match attribute instanceTypeName() node
    	self.add_node()
    	self.vs[11]["mm__"] = """hasAttribute_S"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# match attribute instanceTypeName() node
    	self.add_node()
    	self.vs[12]["name"] = """instanceTypeName"""
        self.vs[12]["mm__"] = """Attribute"""
        self.vs[12]["Type"] = """'String'"""
        #self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# has match attribute serializable() node
    	self.add_node()
    	self.vs[13]["mm__"] = """hasAttribute_S"""
        #self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# match attribute serializable() node
    	self.add_node()
    	self.vs[14]["name"] = """serializable"""
        self.vs[14]["mm__"] = """Attribute"""
        self.vs[14]["Type"] = """'String'"""
        #self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        
        
    	# has apply attribute name() node
    	self.add_node()
    	self.vs[15]["mm__"] = """hasAttribute_T"""
        #self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute name() node
    	self.add_node()
    	self.vs[16]["name"] = """name"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["Type"] = """'String'"""
        #self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation name() node
    	self.add_node()
    	self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        #self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr name() node
    	self.add_node()
    	self.vs[18]["mm__"] = """leftExpr"""
        #self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr name() node
    	self.add_node()
    	self.vs[19]["mm__"] = """rightExpr"""
        #self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# has apply attribute instanceClassName() node
    	self.add_node()
    	self.vs[20]["mm__"] = """hasAttribute_T"""
        #self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute instanceClassName() node
    	self.add_node()
    	self.vs[21]["name"] = """instanceClassName"""
        self.vs[21]["mm__"] = """Attribute"""
        self.vs[21]["Type"] = """'String'"""
        #self.vs[21]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation instanceClassName() node
    	self.add_node()
    	self.vs[22]["name"] = """eq_"""
        self.vs[22]["mm__"] = """Equation"""
        #self.vs[22]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr instanceClassName() node
    	self.add_node()
    	self.vs[23]["mm__"] = """leftExpr"""
        #self.vs[23]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr instanceClassName() node
    	self.add_node()
    	self.vs[24]["mm__"] = """rightExpr"""
        #self.vs[24]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# has apply attribute instanceTypeName() node
    	self.add_node()
    	self.vs[25]["mm__"] = """hasAttribute_T"""
        #self.vs[25]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute instanceTypeName() node
    	self.add_node()
    	self.vs[26]["name"] = """instanceTypeName"""
        self.vs[26]["mm__"] = """Attribute"""
        self.vs[26]["Type"] = """'String'"""
        #self.vs[26]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation instanceTypeName() node
    	self.add_node()
    	self.vs[27]["name"] = """eq_"""
        self.vs[27]["mm__"] = """Equation"""
        #self.vs[27]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr instanceTypeName() node
    	self.add_node()
    	self.vs[28]["mm__"] = """leftExpr"""
        #self.vs[28]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr instanceTypeName() node
    	self.add_node()
    	self.vs[29]["mm__"] = """rightExpr"""
        #self.vs[29]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# has apply attribute serializable() node
    	self.add_node()
    	self.vs[30]["mm__"] = """hasAttribute_T"""
        #self.vs[30]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute serializable() node
    	self.add_node()
    	self.vs[31]["name"] = """serializable"""
        self.vs[31]["mm__"] = """Attribute"""
        self.vs[31]["Type"] = """'String'"""
        #self.vs[31]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation serializable() node
    	self.add_node()
    	self.vs[32]["name"] = """eq_"""
        self.vs[32]["mm__"] = """Equation"""
        #self.vs[32]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr serializable() node
    	self.add_node()
    	self.vs[33]["mm__"] = """leftExpr"""
        #self.vs[33]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr serializable() node
    	self.add_node()
    	self.vs[34]["mm__"] = """rightExpr"""
        #self.vs[34]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# has apply attribute ApplyAttribute() node
    	self.add_node()
    	self.vs[35]["mm__"] = """hasAttribute_T"""
        #self.vs[35]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'has')
    	# apply attribute ApplyAttribute() node
    	self.add_node()
    	self.vs[36]["name"] = """ApplyAttribute"""
        self.vs[36]["mm__"] = """Attribute"""
        self.vs[36]["Type"] = """'String'"""
        #self.vs[36]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply attribute equation ApplyAttribute() node
    	self.add_node()
    	self.vs[37]["name"] = """eq_"""
        self.vs[37]["mm__"] = """Equation"""
        #self.vs[37]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equation')
    	# apply attribute equation left expr ApplyAttribute() node
    	self.add_node()
    	self.vs[38]["mm__"] = """leftExpr"""
        #self.vs[38]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExpr')
    	# apply attribute equation right expr ApplyAttribute() node
    	self.add_node()
    	self.vs[39]["mm__"] = """rightExpr"""
        #self.vs[39]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExpr')
    	# apply attribute atom ApplyAttribute() node
    	self.add_node()
    	self.vs[40]["name"] = """solveRef"""
        self.vs[40]["mm__"] = """Constant"""
        self.vs[40]["Type"] = """'String'"""
        #self.vs[40]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atom40')
        
        
        # Add the edges
        self.add_edges([
    		(0,4), # matchmodel -> match_contains
    		(4,3), # match_contains -> match_class EDataType()
    		(1,6), # applymodel -> apply_contains
    		(6,5), # apply_contains -> apply_class EDataType()
    		(3,7), # match_class EDataType() -> has_match_attribute name ()
    		(7,8), #  has_match_attribute name () -> match_attribute name ()
    		(3,9), # match_class EDataType() -> has_match_attribute instanceClassName ()
    		(9,10), #  has_match_attribute instanceClassName () -> match_attribute instanceClassName ()
    		(3,11), # match_class EDataType() -> has_match_attribute instanceTypeName ()
    		(11,12), #  has_match_attribute instanceTypeName () -> match_attribute instanceTypeName ()
    		(3,13), # match_class EDataType() -> has_match_attribute serializable ()
    		(13,14), #  has_match_attribute serializable () -> match_attribute serializable ()
    		(5,15), # apply_class EDataType() -> has_apply_attribute name ()
    		(15,16), #  has_apply_attribute name () -> apply_attribute name ()
    		(17,18), #  equation of apply attribute name () -> left_expr
    		(18,16), #  left_expr -> apply_attribute name ()
    		(17,19), #  equation of apply attribute name () -> right_expr
    		(19,8), # right_expr --> term
    		(5,20), # apply_class EDataType() -> has_apply_attribute instanceClassName ()
    		(20,21), #  has_apply_attribute instanceClassName () -> apply_attribute instanceClassName ()
    		(22,23), #  equation of apply attribute instanceClassName () -> left_expr
    		(23,21), #  left_expr -> apply_attribute instanceClassName ()
    		(22,24), #  equation of apply attribute instanceClassName () -> right_expr
    		(24,10), # right_expr --> term
    		(5,25), # apply_class EDataType() -> has_apply_attribute instanceTypeName ()
    		(25,26), #  has_apply_attribute instanceTypeName () -> apply_attribute instanceTypeName ()
    		(27,28), #  equation of apply attribute instanceTypeName () -> left_expr
    		(28,26), #  left_expr -> apply_attribute instanceTypeName ()
    		(27,29), #  equation of apply attribute instanceTypeName () -> right_expr
    		(29,12), # right_expr --> term
    		(5,30), # apply_class EDataType() -> has_apply_attribute serializable ()
    		(30,31), #  has_apply_attribute serializable () -> apply_attribute serializable ()
    		(32,33), #  equation of apply attribute serializable () -> left_expr
    		(33,31), #  left_expr -> apply_attribute serializable ()
    		(32,34), #  equation of apply attribute serializable () -> right_expr
    		(34,14), # right_expr --> term
    		(5,35), # apply_class EDataType() -> has_apply_attribute ApplyAttribute ()
    		(35,36), #  has_apply_attribute ApplyAttribute () -> apply_attribute ApplyAttribute ()
    		(37,38), #  equation of apply attribute ApplyAttribute () -> left_expr
    		(38,36), #  left_expr -> apply_attribute ApplyAttribute ()
    		(37,39), #  equation of apply attribute ApplyAttribute () -> right_expr
    		(39,40), # right_expr --> term
        	(0,2), # matchmodel -> pairedwith
        	(2,1) # pairedwith -> applyModel
        ])
        
