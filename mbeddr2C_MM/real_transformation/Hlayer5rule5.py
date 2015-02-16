from core.himesis import Himesis
import cPickle as pickle
import uuid

class Hlayer5rule5(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule layer5rule5.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer5rule5, self).__init__(name='Hlayer5rule5', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        # TODO Levi, need some help here because I don't know where does 
        # this value come from.
        self["mm__"] = pickle.loads("""(lp1
S'HimesisMM'
p2
a.""")
        
        self["name"] = """layer5rule5"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule5')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule5matchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule5applymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule5pairedwith2')
        
    	# match class StatementList(layer5rule5class0) node
    	self.add_node()
    	self.vs[3]["name"] = """layer5rule5class0"""
        self.vs[3]["classtype"] = """StatementList"""
        self.vs[3]["mm__"] = """StatementList"""
        self.vs[3]["cardinality"] = """+"""
        #self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule5class0')
    	# match_contains node for class StatementList(layer5rule5class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        #self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule5class0matchcontains4')
    	# match class ReturnStatement(layer5rule5class1) node
    	self.add_node()
    	self.vs[5]["name"] = """layer5rule5class1"""
        self.vs[5]["classtype"] = """ReturnStatement"""
        self.vs[5]["mm__"] = """ReturnStatement"""
        self.vs[5]["cardinality"] = """+"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule5class1')
    	# match_contains node for class ReturnStatement(layer5rule5class1)
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        #self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule5class1matchcontains6')
    	# match class ExecuteTestExpression(layer5rule5class2) node
    	self.add_node()
    	self.vs[7]["name"] = """layer5rule5class2"""
        self.vs[7]["classtype"] = """ExecuteTestExpression"""
        self.vs[7]["mm__"] = """ExecuteTestExpression"""
        self.vs[7]["cardinality"] = """+"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule5class2')
    	# match_contains node for class ExecuteTestExpression(layer5rule5class2)
        self.add_node()
        self.vs[8]["mm__"] = """match_contains"""
        #self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule5class2matchcontains8')
    	# match class Function(layer5rule5class3) node
    	self.add_node()
    	self.vs[9]["name"] = """layer5rule5class3"""
        self.vs[9]["classtype"] = """Function"""
        self.vs[9]["mm__"] = """Function"""
        self.vs[9]["cardinality"] = """+"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule5class3')
    	# match_contains node for class Function(layer5rule5class3)
        self.add_node()
        self.vs[10]["mm__"] = """match_contains"""
        #self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule5class3matchcontains10')
    	# match class TestCaseRef(layer5rule5class4) node
    	self.add_node()
    	self.vs[11]["name"] = """layer5rule5class4"""
        self.vs[11]["classtype"] = """TestCaseRef"""
        self.vs[11]["mm__"] = """TestCaseRef"""
        self.vs[11]["cardinality"] = """+"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule5class4')
    	# match_contains node for class TestCaseRef(layer5rule5class4)
        self.add_node()
        self.vs[12]["mm__"] = """match_contains"""
        #self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule5class4matchcontains12')
    	# match class TestCase(layer5rule5class5) node
    	self.add_node()
    	self.vs[13]["name"] = """layer5rule5class5"""
        self.vs[13]["classtype"] = """TestCase"""
        self.vs[13]["mm__"] = """TestCase"""
        self.vs[13]["cardinality"] = """+"""
        #self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule5class5')
    	# match_contains node for class TestCase(layer5rule5class5)
        self.add_node()
        self.vs[14]["mm__"] = """match_contains"""
        #self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule5class5matchcontains14')
        
        
    	# apply class StatementList(layer5rule5class6) node
    	self.add_node()
    	self.vs[15]["name"] = """layer5rule5class6"""
        self.vs[15]["classtype"] = """StatementList"""
        self.vs[15]["mm__"] = """StatementList"""
        self.vs[15]["cardinality"] = """1"""
        #self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule5class6')
    	# apply_contains node for class StatementList(layer5rule5class6)
        self.add_node()
        self.vs[16]["mm__"] = """apply_contains"""
        #self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule5class6applycontains16')
    	# apply class ExpressionStatement(layer5rule5class7) node
    	self.add_node()
    	self.vs[17]["name"] = """layer5rule5class7"""
        self.vs[17]["classtype"] = """ExpressionStatement"""
        self.vs[17]["mm__"] = """ExpressionStatement"""
        self.vs[17]["cardinality"] = """1"""
        #self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule5class7')
    	# apply_contains node for class ExpressionStatement(layer5rule5class7)
        self.add_node()
        self.vs[18]["mm__"] = """apply_contains"""
        #self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule5class7applycontains18')
    	# apply class FunctionCall(layer5rule5class8) node
    	self.add_node()
    	self.vs[19]["name"] = """layer5rule5class8"""
        self.vs[19]["classtype"] = """FunctionCall"""
        self.vs[19]["mm__"] = """FunctionCall"""
        self.vs[19]["cardinality"] = """1"""
        #self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule5class8')
    	# apply_contains node for class FunctionCall(layer5rule5class8)
        self.add_node()
        self.vs[20]["mm__"] = """apply_contains"""
        #self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule5class8applycontains20')
    	# apply class FunctionPrototype(layer5rule5class9) node
    	self.add_node()
    	self.vs[21]["name"] = """layer5rule5class9"""
        self.vs[21]["classtype"] = """FunctionPrototype"""
        self.vs[21]["mm__"] = """FunctionPrototype"""
        self.vs[21]["cardinality"] = """1"""
        #self.vs[21]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule5class9')
    	# apply_contains node for class FunctionPrototype(layer5rule5class9)
        self.add_node()
        self.vs[22]["mm__"] = """apply_contains"""
        #self.vs[22]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule5class9applycontains22')
        
        
    	# match association Function--body-->StatementList node
    	self.add_node()
    	self.vs[23]["associationType"] = """body"""
        self.vs[23]["mm__"] = """directLink_S"""
        #self.vs[23]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule5class3assoc23layer5rule5class0')
    	# match association StatementList--statements-->ReturnStatement node
    	self.add_node()
    	self.vs[24]["associationType"] = """statements"""
        self.vs[24]["mm__"] = """directLink_S"""
        #self.vs[24]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule5class0assoc24layer5rule5class1')
    	# match association ReturnStatement--expression-->ExecuteTestExpression node
    	self.add_node()
    	self.vs[25]["associationType"] = """expression"""
        self.vs[25]["mm__"] = """directLink_S"""
        #self.vs[25]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule5class1assoc25layer5rule5class2')
    	# match association ExecuteTestExpression--tests-->TestCaseRef node
    	self.add_node()
    	self.vs[26]["associationType"] = """tests"""
        self.vs[26]["mm__"] = """directLink_S"""
        #self.vs[26]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule5class2assoc26layer5rule5class4')
    	# match association TestCaseRef--testcase-->TestCase node
    	self.add_node()
    	self.vs[27]["associationType"] = """testcase"""
        self.vs[27]["mm__"] = """directLink_S"""
        #self.vs[27]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule5class4assoc27layer5rule5class5')
        
    	# apply association StatementList--statements-->ExpressionStatement node
    	self.add_node()
    	self.vs[28]["associationType"] = """statements"""
        self.vs[28]["mm__"] = """directLink_T"""
        #self.vs[28]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule5class6assoc28layer5rule5class7')
    	# apply association ExpressionStatement--expr-->FunctionCall node
    	self.add_node()
    	self.vs[29]["associationType"] = """expr"""
        self.vs[29]["mm__"] = """directLink_T"""
        #self.vs[29]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule5class7assoc29layer5rule5class8')
    	# apply association FunctionCall--function-->FunctionPrototype node
    	self.add_node()
    	self.vs[30]["associationType"] = """function"""
        self.vs[30]["mm__"] = """directLink_T"""
        #self.vs[30]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule5class8assoc30layer5rule5class9')
        
    	# backward association Function---->StatementList node
    	self.add_node()
    	self.vs[31]["type"] = """ruleDef"""
        self.vs[31]["mm__"] = """backward_link"""
        #self.vs[31]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule5class3blink31layer5rule5class6')
    	# backward association TestCase---->FunctionPrototype node
    	self.add_node()
    	self.vs[32]["type"] = """ruleDef"""
        self.vs[32]["mm__"] = """backward_link"""
        #self.vs[32]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule5class5blink32layer5rule5class9')
        
        
    	# has match attribute name(layer5rule5class3attribute0) node
    	self.add_node()
    	self.vs[33]["mm__"] = """hasAttribute_S"""
        #self.vs[33]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer5rule5class3attribute0')
    	# match attribute name(layer5rule5class3attribute0) node
    	self.add_node()
    	self.vs[34]["name"] = """name"""
        self.vs[34]["mm__"] = """Attribute"""
        self.vs[34]["Type"] = """'String'"""
        #self.vs[34]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule5class3attribute0')
    	# match attribute equation name(layer5rule5class3attribute0) node
    	self.add_node()
    	self.vs[35]["name"] = """eq_"""
        self.vs[35]["mm__"] = """Equation"""
        #self.vs[35]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equationlayer5rule5class3attribute0')
    	# match attribute equation left expr name(layer5rule5class3attribute0) node
    	self.add_node()
    	self.vs[36]["mm__"] = """leftExpr"""
        #self.vs[36]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExprlayer5rule5class3attribute0')
    	# match attribute equation right expr name(layer5rule5class3attribute0) node
    	self.add_node()
    	self.vs[37]["mm__"] = """rightExpr"""
        #self.vs[37]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExprlayer5rule5class3attribute0')
    	# apply attribute atom name(layer5rule5class3attribute0) node
    	self.add_node()
    	self.vs[38]["name"] = """main"""
        self.vs[38]["mm__"] = """Constant"""
        self.vs[38]["Type"] = """'String'"""
        #self.vs[38]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atomlayer5rule5class3attribute038')
        
        
        
        
        # Add the edges
        self.add_edges([
    		(0,4), # matchmodel -> match_contains
    		(4,3), # match_contains -> match_class StatementList(layer5rule5class0)
    		(0,6), # matchmodel -> match_contains
    		(6,5), # match_contains -> match_class ReturnStatement(layer5rule5class1)
    		(0,8), # matchmodel -> match_contains
    		(8,7), # match_contains -> match_class ExecuteTestExpression(layer5rule5class2)
    		(0,10), # matchmodel -> match_contains
    		(10,9), # match_contains -> match_class Function(layer5rule5class3)
    		(0,12), # matchmodel -> match_contains
    		(12,11), # match_contains -> match_class TestCaseRef(layer5rule5class4)
    		(0,14), # matchmodel -> match_contains
    		(14,13), # match_contains -> match_class TestCase(layer5rule5class5)
    		(1,16), # applymodel -> apply_contains
    		(16,15), # apply_contains -> apply_class StatementList(layer5rule5class6)
    		(1,18), # applymodel -> apply_contains
    		(18,17), # apply_contains -> apply_class ExpressionStatement(layer5rule5class7)
    		(1,20), # applymodel -> apply_contains
    		(20,19), # apply_contains -> apply_class FunctionCall(layer5rule5class8)
    		(1,22), # applymodel -> apply_contains
    		(22,21), # apply_contains -> apply_class FunctionPrototype(layer5rule5class9)
    		(9,23), # match_class Function(layer5rule5class3) -> association body
    		(23,3), # association body  -> match_class StatementList(layer5rule5class0)
    		(3,24), # match_class StatementList(layer5rule5class0) -> association statements
    		(24,5), # association statements  -> match_class ReturnStatement(layer5rule5class1)
    		(5,25), # match_class ReturnStatement(layer5rule5class1) -> association expression
    		(25,7), # association expression  -> match_class ExecuteTestExpression(layer5rule5class2)
    		(7,26), # match_class ExecuteTestExpression(layer5rule5class2) -> association tests
    		(26,11), # association tests  -> match_class TestCaseRef(layer5rule5class4)
    		(11,27), # match_class TestCaseRef(layer5rule5class4) -> association testcase
    		(27,13), # association testcase  -> match_class TestCase(layer5rule5class5)
    		(15,28), # apply_class StatementList(layer5rule5class6) -> association statements
    		(28,17), # association statements  -> apply_class ExpressionStatement(layer5rule5class7)
    		(17,29), # apply_class ExpressionStatement(layer5rule5class7) -> association expr
    		(29,19), # association expr  -> apply_class FunctionCall(layer5rule5class8)
    		(19,30), # apply_class FunctionCall(layer5rule5class8) -> association function
    		(30,21), # association function  -> apply_class FunctionPrototype(layer5rule5class9)
    		(15,31), # apply_class StatementList(layer5rule5class6) -> backward_association
    		(31,9), #  backward_association -> apply_class Function(layer5rule5class3)
    		(21,32), # apply_class FunctionPrototype(layer5rule5class9) -> backward_association
    		(32,13), #  backward_association -> apply_class TestCase(layer5rule5class5)
    		(9,33), # match_class Function(layer5rule5class3) -> has_match_attribute name (layer5rule5class3attribute0)
    		(33,34), #  has_match_attribute name (layer5rule5class3attribute0) -> match_attribute name (layer5rule5class3attribute0)
	    	(35,36), #  equation of match attribute name (layer5rule5class3attribute0) -> left_expr
    		(36,34), #  left_expr -> match_attribute name (layer5rule5class3attribute0)
    		(35,37), #  equation of match attribute name (layer5rule5class3attribute0) -> right_expr
    		(37,38), # right_expr --> term
        	(0,2), # matchmodel -> pairedwith
        	(2,1) # pairedwith -> applyModel
        ])
        
