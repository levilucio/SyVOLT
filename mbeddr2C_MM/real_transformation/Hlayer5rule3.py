from core.himesis import Himesis
import uuid

class Hlayer5rule3(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule layer5rule3.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer5rule3, self).__init__(name='Hlayer5rule3', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """layer5rule3"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule3')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
 
        
        # match class TestCase(layer5rule3class0) node
        self.add_node()

        self.vs[3]["mm__"] = """TestCase""" 
        self.vs[3]["attr1"] = """+""" 
        # match_contains node for class TestCase(layer5rule3class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        # match class StatementList(layer5rule3class1) node
        self.add_node()

        self.vs[5]["mm__"] = """StatementList""" 
        self.vs[5]["attr1"] = """+""" 
        # match_contains node for class StatementList(layer5rule3class1)
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        # match class InitializeConfiguration(layer5rule3class2) node
        self.add_node()

        self.vs[7]["mm__"] = """InitializeConfiguration""" 
        self.vs[7]["attr1"] = """+""" 
        # match_contains node for class InitializeConfiguration(layer5rule3class2)
        self.add_node()
        self.vs[8]["mm__"] = """match_contains"""
        # match class InstanceConfiguration(layer5rule3class3) node
        self.add_node()

        self.vs[9]["mm__"] = """InstanceConfiguration""" 
        self.vs[9]["attr1"] = """+""" 
        # match_contains node for class InstanceConfiguration(layer5rule3class3)
        self.add_node()
        self.vs[10]["mm__"] = """match_contains"""
        
        
        # apply class StatementList(layer5rule3class4) node
        self.add_node()

        self.vs[11]["mm__"] = """StatementList""" 
        self.vs[11]["attr1"] = """1"""
        # apply_contains node for class StatementList(layer5rule3class4)
        self.add_node()
        self.vs[12]["mm__"] = """apply_contains"""
        # apply class ExpressionStatement(layer5rule3class5) node
        self.add_node()

        self.vs[13]["mm__"] = """ExpressionStatement""" 
        self.vs[13]["attr1"] = """1"""
        # apply_contains node for class ExpressionStatement(layer5rule3class5)
        self.add_node()
        self.vs[14]["mm__"] = """apply_contains"""
        # apply class FunctionCall(layer5rule3class6) node
        self.add_node()

        self.vs[15]["mm__"] = """FunctionCall""" 
        self.vs[15]["attr1"] = """1"""
        # apply_contains node for class FunctionCall(layer5rule3class6)
        self.add_node()
        self.vs[16]["mm__"] = """apply_contains"""
        # apply class FunctionPrototype(layer5rule3class7) node
        self.add_node()

        self.vs[17]["mm__"] = """FunctionPrototype""" 
        self.vs[17]["attr1"] = """1"""
        # apply_contains node for class FunctionPrototype(layer5rule3class7)
        self.add_node()
        self.vs[18]["mm__"] = """apply_contains"""
        
        
        # match association TestCase--body-->StatementList node
        self.add_node()
        self.vs[19]["attr1"] = """body"""
        self.vs[19]["mm__"] = """directLink_S"""
        # match association StatementList--statements-->InitializeConfiguration node
        self.add_node()
        self.vs[20]["attr1"] = """statements"""
        self.vs[20]["mm__"] = """directLink_S"""
        # match association InitializeConfiguration--config-->InstanceConfiguration node
        self.add_node()
        self.vs[21]["attr1"] = """config"""
        self.vs[21]["mm__"] = """directLink_S"""
        
        # apply association StatementList--statements-->ExpressionStatement node
        self.add_node()
        self.vs[22]["attr1"] = """statements"""
        self.vs[22]["mm__"] = """directLink_T"""
        # apply association ExpressionStatement--expr-->FunctionCall node
        self.add_node()
        self.vs[23]["attr1"] = """expr"""
        self.vs[23]["mm__"] = """directLink_T"""
        # apply association FunctionCall--function-->FunctionPrototype node
        self.add_node()
        self.vs[24]["attr1"] = """function"""
        self.vs[24]["mm__"] = """directLink_T"""
        
        # backward association TestCase---->StatementList node
        self.add_node()

        self.vs[25]["mm__"] = """backward_link"""
        # backward association InstanceConfiguration---->FunctionPrototype node
        self.add_node()

        self.vs[26]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class TestCase(layer5rule3class0)
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class StatementList(layer5rule3class1)
                (0,8), # matchmodel -> match_contains
                (8,7), # match_contains -> match_class InitializeConfiguration(layer5rule3class2)
                (0,10), # matchmodel -> match_contains
                (10,9), # match_contains -> match_class InstanceConfiguration(layer5rule3class3)
                (1,12), # applymodel -> apply_contains
                (12,11), # apply_contains -> apply_class StatementList(layer5rule3class4)
                (1,14), # applymodel -> apply_contains
                (14,13), # apply_contains -> apply_class ExpressionStatement(layer5rule3class5)
                (1,16), # applymodel -> apply_contains
                (16,15), # apply_contains -> apply_class FunctionCall(layer5rule3class6)
                (1,18), # applymodel -> apply_contains
                (18,17), # apply_contains -> apply_class FunctionPrototype(layer5rule3class7)
                (3,19), # match_class TestCase(layer5rule3class0) -> association body
                (19,5), # association body  -> match_class StatementList(layer5rule3class1)
                (5,20), # match_class StatementList(layer5rule3class1) -> association statements
                (20,7), # association statements  -> match_class InitializeConfiguration(layer5rule3class2)
                (7,21), # match_class InitializeConfiguration(layer5rule3class2) -> association config
                (21,9), # association config  -> match_class InstanceConfiguration(layer5rule3class3)
                (11,22), # apply_class StatementList(layer5rule3class4) -> association statements
                (22,13), # association statements  -> apply_class ExpressionStatement(layer5rule3class5)
                (13,23), # apply_class ExpressionStatement(layer5rule3class5) -> association expr
                (23,15), # association expr  -> apply_class FunctionCall(layer5rule3class6)
                (15,24), # apply_class FunctionCall(layer5rule3class6) -> association function
                (24,17), # association function  -> apply_class FunctionPrototype(layer5rule3class7)
                (11,25), # apply_class StatementList(layer5rule3class4) -> backward_association
                (25,3), #  backward_association -> apply_class TestCase(layer5rule3class0)
                (17,26), # apply_class FunctionPrototype(layer5rule3class7) -> backward_association
                (26,9), #  backward_association -> apply_class InstanceConfiguration(layer5rule3class3)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((11,'__ApplyAttribute'),('constant','TestCaseFunctionStatements')), ((17,'__ApplyAttribute'),('constant','InstanceConfigurationInit')), ]

        
