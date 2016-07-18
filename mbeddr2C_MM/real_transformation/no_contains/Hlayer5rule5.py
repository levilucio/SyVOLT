from core.himesis import Himesis
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
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer5rule5"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule5')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["attr1"] = """layer5rule5"""
        
        # match class StatementList(layer5rule5class0) node
        self.add_node()
        
        self.vs[3]["mm__"] = """StatementList""" 
        self.vs[3]["attr1"] = """+""" 
        # match class ReturnStatement(layer5rule5class1) node
        self.add_node()
        
        self.vs[4]["mm__"] = """ReturnStatement""" 
        self.vs[4]["attr1"] = """+""" 
        # match class ExecuteTestExpression(layer5rule5class2) node
        self.add_node()
        
        self.vs[5]["mm__"] = """ExecuteTestExpression""" 
        self.vs[5]["attr1"] = """+""" 
        # match class Function(layer5rule5class3) node
        self.add_node()
        
        self.vs[6]["mm__"] = """Function""" 
        self.vs[6]["attr1"] = """+""" 
        # match class TestCaseRef(layer5rule5class4) node
        self.add_node()
        
        self.vs[7]["mm__"] = """TestCaseRef""" 
        self.vs[7]["attr1"] = """+""" 
        # match class TestCase(layer5rule5class5) node
        self.add_node()
        
        self.vs[8]["mm__"] = """TestCase""" 
        self.vs[8]["attr1"] = """+""" 
        
        
        # apply class StatementList(layer5rule5class6) node
        self.add_node()

        self.vs[9]["mm__"] = """StatementList""" 
        self.vs[9]["attr1"] = """1"""
        # apply class ExpressionStatement(layer5rule5class7) node
        self.add_node()

        self.vs[10]["mm__"] = """ExpressionStatement""" 
        self.vs[10]["attr1"] = """1"""
        # apply class FunctionCall(layer5rule5class8) node
        self.add_node()

        self.vs[11]["mm__"] = """FunctionCall""" 
        self.vs[11]["attr1"] = """1"""
        # apply class FunctionPrototype(layer5rule5class9) node
        self.add_node()

        self.vs[12]["mm__"] = """FunctionPrototype""" 
        self.vs[12]["attr1"] = """1"""
        
        
        # match association Function--body-->StatementList node
        self.add_node()
        self.vs[13]["attr1"] = """body"""
        self.vs[13]["mm__"] = """directLink_S"""
        # match association StatementList--statements-->ReturnStatement node
        self.add_node()
        self.vs[14]["attr1"] = """statements"""
        self.vs[14]["mm__"] = """directLink_S"""
        # match association ReturnStatement--expression-->ExecuteTestExpression node
        self.add_node()
        self.vs[15]["attr1"] = """expression"""
        self.vs[15]["mm__"] = """directLink_S"""
        # match association ExecuteTestExpression--tests-->TestCaseRef node
        self.add_node()
        self.vs[16]["attr1"] = """tests"""
        self.vs[16]["mm__"] = """directLink_S"""
        # match association TestCaseRef--testcase-->TestCase node
        self.add_node()
        self.vs[17]["attr1"] = """testcase"""
        self.vs[17]["mm__"] = """directLink_S"""
        
        # apply association StatementList--statements-->ExpressionStatement node
        self.add_node()
        self.vs[18]["attr1"] = """statements"""
        self.vs[18]["mm__"] = """directLink_T"""
        # apply association ExpressionStatement--expr-->FunctionCall node
        self.add_node()
        self.vs[19]["attr1"] = """expr"""
        self.vs[19]["mm__"] = """directLink_T"""
        # apply association FunctionCall--function-->FunctionPrototype node
        self.add_node()
        self.vs[20]["attr1"] = """function"""
        self.vs[20]["mm__"] = """directLink_T"""
        
        # backward association Function---->StatementList node
        self.add_node()

        self.vs[21]["mm__"] = """backward_link"""
        # backward association TestCase---->FunctionPrototype node
        self.add_node()

        self.vs[22]["mm__"] = """backward_link"""
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class StatementList(layer5rule5class0)
                (0,4), # matchmodel -> match_class ReturnStatement(layer5rule5class1)
                (0,5), # matchmodel -> match_class ExecuteTestExpression(layer5rule5class2)
                (0,6), # matchmodel -> match_class Function(layer5rule5class3)
                (0,7), # matchmodel -> match_class TestCaseRef(layer5rule5class4)
                (0,8), # matchmodel -> match_class TestCase(layer5rule5class5)
                (1,9), # applymodel -> -> apply_class StatementList(layer5rule5class6)
                (1,10), # applymodel -> -> apply_class ExpressionStatement(layer5rule5class7)
                (1,11), # applymodel -> -> apply_class FunctionCall(layer5rule5class8)
                (1,12), # applymodel -> -> apply_class FunctionPrototype(layer5rule5class9)
                (6,13), # match_class Function(layer5rule5class3) -> association body
                (13,3), # association body  -> match_class StatementList(layer5rule5class0)
                (3,14), # match_class StatementList(layer5rule5class0) -> association statements
                (14,4), # association statements  -> match_class ReturnStatement(layer5rule5class1)
                (4,15), # match_class ReturnStatement(layer5rule5class1) -> association expression
                (15,5), # association expression  -> match_class ExecuteTestExpression(layer5rule5class2)
                (5,16), # match_class ExecuteTestExpression(layer5rule5class2) -> association tests
                (16,7), # association tests  -> match_class TestCaseRef(layer5rule5class4)
                (7,17), # match_class TestCaseRef(layer5rule5class4) -> association testcase
                (17,8), # association testcase  -> match_class TestCase(layer5rule5class5)
                (9,18), # apply_class StatementList(layer5rule5class6) -> association statements
                (18,10), # association statements  -> apply_class ExpressionStatement(layer5rule5class7)
                (10,19), # apply_class ExpressionStatement(layer5rule5class7) -> association expr
                (19,11), # association expr  -> apply_class FunctionCall(layer5rule5class8)
                (11,20), # apply_class FunctionCall(layer5rule5class8) -> association function
                (20,12), # association function  -> apply_class FunctionPrototype(layer5rule5class9)
                (9,21), # apply_class StatementList(layer5rule5class6) -> backward_association
                (21,6), #  backward_association -> apply_class Function(layer5rule5class3)
                (12,22), # apply_class FunctionPrototype(layer5rule5class9) -> backward_association
                (22,8), #  backward_association -> apply_class TestCase(layer5rule5class5)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((6,'name'),('constant','main')), ((9,'__ApplyAttribute'),('constant','Main2Body')), ((12,'__ApplyAttribute'),('constant','TestCasePrototype')), ]

        
