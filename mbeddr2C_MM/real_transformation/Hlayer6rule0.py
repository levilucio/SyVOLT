from core.himesis import Himesis
import cPickle as pickle
import uuid

class Hlayer6rule0(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule layer6rule0.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer6rule0, self).__init__(name='Hlayer6rule0', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        # TODO Levi, need some help here because I don't know where does 
        # this value come from.
        self["mm__"] = pickle.loads("""(lp1
S'HimesisMM'
p2
a.""")
        
        self["name"] = """layer6rule0"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer6rule0')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer6rule0matchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer6rule0applymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer6rule0pairedwith2')
        
    	# match class Function(layer6rule0class0) node
    	self.add_node()
    	self.vs[3]["name"] = """layer6rule0class0"""
        self.vs[3]["classtype"] = """Function"""
        self.vs[3]["mm__"] = """Function"""
        self.vs[3]["cardinality"] = """+"""
        #self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer6rule0class0')
    	# match_contains node for class Function(layer6rule0class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        #self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer6rule0class0matchcontains4')
        
        
    	# apply class StatementList(layer6rule0class1) node
    	self.add_node()
    	self.vs[5]["name"] = """layer6rule0class1"""
        self.vs[5]["classtype"] = """StatementList"""
        self.vs[5]["mm__"] = """StatementList"""
        self.vs[5]["cardinality"] = """1"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer6rule0class1')
    	# apply_contains node for class StatementList(layer6rule0class1)
        self.add_node()
        self.vs[6]["mm__"] = """apply_contains"""
        #self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer6rule0class1applycontains6')
    	# apply class ReturnStatement(layer6rule0class2) node
    	self.add_node()
    	self.vs[7]["name"] = """layer6rule0class2"""
        self.vs[7]["classtype"] = """ReturnStatement"""
        self.vs[7]["mm__"] = """ReturnStatement"""
        self.vs[7]["cardinality"] = """1"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer6rule0class2')
    	# apply_contains node for class ReturnStatement(layer6rule0class2)
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        #self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer6rule0class2applycontains8')
    	# apply class NumberLiteral(layer6rule0class3) node
    	self.add_node()
    	self.vs[9]["name"] = """layer6rule0class3"""
        self.vs[9]["classtype"] = """NumberLiteral"""
        self.vs[9]["mm__"] = """NumberLiteral"""
        self.vs[9]["cardinality"] = """1"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer6rule0class3')
    	# apply_contains node for class NumberLiteral(layer6rule0class3)
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        #self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer6rule0class3applycontains10')
        
        
        
    	# apply association StatementList--statements-->ReturnStatement node
    	self.add_node()
    	self.vs[11]["associationType"] = """statements"""
        self.vs[11]["mm__"] = """directLink_T"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer6rule0class1assoc11layer6rule0class2')
    	# apply association ReturnStatement--expression-->NumberLiteral node
    	self.add_node()
    	self.vs[12]["associationType"] = """expression"""
        self.vs[12]["mm__"] = """directLink_T"""
        #self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer6rule0class2assoc12layer6rule0class3')
        
    	# backward association Function---->StatementList node
    	self.add_node()
    	self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["mm__"] = """backward_link"""
        #self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer6rule0class0blink13layer6rule0class1')
        
        
    	# has match attribute name(layer6rule0class0attribute0) node
    	self.add_node()
    	self.vs[14]["mm__"] = """hasAttribute_S"""
        #self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer6rule0class0attribute0')
    	# match attribute name(layer6rule0class0attribute0) node
    	self.add_node()
    	self.vs[15]["name"] = """name"""
        self.vs[15]["mm__"] = """Attribute"""
        self.vs[15]["Type"] = """'String'"""
        #self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer6rule0class0attribute0')
    	# match attribute equation name(layer6rule0class0attribute0) node
    	self.add_node()
    	self.vs[16]["name"] = """eq_"""
        self.vs[16]["mm__"] = """Equation"""
        #self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equationlayer6rule0class0attribute0')
    	# match attribute equation left expr name(layer6rule0class0attribute0) node
    	self.add_node()
    	self.vs[17]["mm__"] = """leftExpr"""
        #self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExprlayer6rule0class0attribute0')
    	# match attribute equation right expr name(layer6rule0class0attribute0) node
    	self.add_node()
    	self.vs[18]["mm__"] = """rightExpr"""
        #self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExprlayer6rule0class0attribute0')
    	# apply attribute atom name(layer6rule0class0attribute0) node
    	self.add_node()
    	self.vs[19]["name"] = """main"""
        self.vs[19]["mm__"] = """Constant"""
        self.vs[19]["Type"] = """'String'"""
        #self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atomlayer6rule0class0attribute019')
        
        
    	# has apply attribute value(layer6rule0class3attribute0) node
    	self.add_node()
    	self.vs[20]["mm__"] = """hasAttribute_T"""
        #self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer6rule0class3attribute0')
    	# apply attribute value(layer6rule0class3attribute0) node
    	self.add_node()
    	self.vs[21]["name"] = """value"""
        self.vs[21]["mm__"] = """Attribute"""
        self.vs[21]["Type"] = """'String'"""
        #self.vs[21]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer6rule0class3attribute0')
    	# apply attribute equation value(layer6rule0class3attribute0) node
    	self.add_node()
    	self.vs[22]["name"] = """eq_"""
        self.vs[22]["mm__"] = """Equation"""
        #self.vs[22]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equationlayer6rule0class3attribute0')
    	# apply attribute equation left expr value(layer6rule0class3attribute0) node
    	self.add_node()
    	self.vs[23]["mm__"] = """leftExpr"""
        #self.vs[23]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExprlayer6rule0class3attribute0')
    	# apply attribute equation right expr value(layer6rule0class3attribute0) node
    	self.add_node()
    	self.vs[24]["mm__"] = """rightExpr"""
        #self.vs[24]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExprlayer6rule0class3attribute0')
    	# apply attribute atom value(layer6rule0class3attribute0) node
    	self.add_node()
    	self.vs[25]["name"] = """0"""
        self.vs[25]["mm__"] = """Constant"""
        self.vs[25]["Type"] = """'String'"""
        #self.vs[25]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atomlayer6rule0class3attribute025')
        
        
        # Add the edges
        self.add_edges([
    		(0,4), # matchmodel -> match_contains
    		(4,3), # match_contains -> match_class Function(layer6rule0class0)
    		(1,6), # applymodel -> apply_contains
    		(6,5), # apply_contains -> apply_class StatementList(layer6rule0class1)
    		(1,8), # applymodel -> apply_contains
    		(8,7), # apply_contains -> apply_class ReturnStatement(layer6rule0class2)
    		(1,10), # applymodel -> apply_contains
    		(10,9), # apply_contains -> apply_class NumberLiteral(layer6rule0class3)
    		(5,11), # apply_class StatementList(layer6rule0class1) -> association statements
    		(11,7), # association statements  -> apply_class ReturnStatement(layer6rule0class2)
    		(7,12), # apply_class ReturnStatement(layer6rule0class2) -> association expression
    		(12,9), # association expression  -> apply_class NumberLiteral(layer6rule0class3)
    		(5,13), # apply_class StatementList(layer6rule0class1) -> backward_association
    		(13,3), #  backward_association -> apply_class Function(layer6rule0class0)
    		(3,14), # match_class Function(layer6rule0class0) -> has_match_attribute name (layer6rule0class0attribute0)
    		(14,15), #  has_match_attribute name (layer6rule0class0attribute0) -> match_attribute name (layer6rule0class0attribute0)
	    	(16,17), #  equation of match attribute name (layer6rule0class0attribute0) -> left_expr
    		(17,15), #  left_expr -> match_attribute name (layer6rule0class0attribute0)
    		(16,18), #  equation of match attribute name (layer6rule0class0attribute0) -> right_expr
    		(18,19), # right_expr --> term
    		(9,20), # apply_class NumberLiteral(layer6rule0class3) -> has_apply_attribute value (layer6rule0class3attribute0)
    		(20,21), #  has_apply_attribute value (layer6rule0class3attribute0) -> apply_attribute value (layer6rule0class3attribute0)
    		(22,23), #  equation of apply attribute value (layer6rule0class3attribute0) -> left_expr
    		(23,21), #  left_expr -> apply_attribute value (layer6rule0class3attribute0)
    		(22,24), #  equation of apply attribute value (layer6rule0class3attribute0) -> right_expr
    		(24,25), # right_expr --> term
        	(0,2), # matchmodel -> pairedwith
        	(2,1) # pairedwith -> applyModel
        ])
        
