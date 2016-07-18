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
        self.vs[2]["attr1"] = """layer5rule3"""
        
        # match class TestCase(layer5rule3class0) node
        self.add_node()
        
        self.vs[3]["mm__"] = """TestCase""" 
        self.vs[3]["attr1"] = """+""" 
        # match class StatementList(layer5rule3class1) node
        self.add_node()
        
        self.vs[4]["mm__"] = """StatementList""" 
        self.vs[4]["attr1"] = """+""" 
        # match class InitializeConfiguration(layer5rule3class2) node
        self.add_node()
        
        self.vs[5]["mm__"] = """InitializeConfiguration""" 
        self.vs[5]["attr1"] = """+""" 
        # match class InstanceConfiguration(layer5rule3class3) node
        self.add_node()
        
        self.vs[6]["mm__"] = """InstanceConfiguration""" 
        self.vs[6]["attr1"] = """+""" 
        
        
        # apply class StatementList(layer5rule3class4) node
        self.add_node()

        self.vs[7]["mm__"] = """StatementList""" 
        self.vs[7]["attr1"] = """1"""
        # apply class ExpressionStatement(layer5rule3class5) node
        self.add_node()

        self.vs[8]["mm__"] = """ExpressionStatement""" 
        self.vs[8]["attr1"] = """1"""
        # apply class FunctionCall(layer5rule3class6) node
        self.add_node()

        self.vs[9]["mm__"] = """FunctionCall""" 
        self.vs[9]["attr1"] = """1"""
        # apply class FunctionPrototype(layer5rule3class7) node
        self.add_node()

        self.vs[10]["mm__"] = """FunctionPrototype""" 
        self.vs[10]["attr1"] = """1"""
        
        
        # match association TestCase--body-->StatementList node
        self.add_node()
        self.vs[11]["attr1"] = """body"""
        self.vs[11]["mm__"] = """directLink_S"""
        # match association StatementList--statements-->InitializeConfiguration node
        self.add_node()
        self.vs[12]["attr1"] = """statements"""
        self.vs[12]["mm__"] = """directLink_S"""
        # match association InitializeConfiguration--config-->InstanceConfiguration node
        self.add_node()
        self.vs[13]["attr1"] = """config"""
        self.vs[13]["mm__"] = """directLink_S"""
        
        # apply association StatementList--statements-->ExpressionStatement node
        self.add_node()
        self.vs[14]["attr1"] = """statements"""
        self.vs[14]["mm__"] = """directLink_T"""
        # apply association ExpressionStatement--expr-->FunctionCall node
        self.add_node()
        self.vs[15]["attr1"] = """expr"""
        self.vs[15]["mm__"] = """directLink_T"""
        # apply association FunctionCall--function-->FunctionPrototype node
        self.add_node()
        self.vs[16]["attr1"] = """function"""
        self.vs[16]["mm__"] = """directLink_T"""
        
        # backward association TestCase---->StatementList node
        self.add_node()

        self.vs[17]["mm__"] = """backward_link"""
        # backward association InstanceConfiguration---->FunctionPrototype node
        self.add_node()

        self.vs[18]["mm__"] = """backward_link"""
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class TestCase(layer5rule3class0)
                (0,4), # matchmodel -> match_class StatementList(layer5rule3class1)
                (0,5), # matchmodel -> match_class InitializeConfiguration(layer5rule3class2)
                (0,6), # matchmodel -> match_class InstanceConfiguration(layer5rule3class3)
                (1,7), # applymodel -> -> apply_class StatementList(layer5rule3class4)
                (1,8), # applymodel -> -> apply_class ExpressionStatement(layer5rule3class5)
                (1,9), # applymodel -> -> apply_class FunctionCall(layer5rule3class6)
                (1,10), # applymodel -> -> apply_class FunctionPrototype(layer5rule3class7)
                (3,11), # match_class TestCase(layer5rule3class0) -> association body
                (11,4), # association body  -> match_class StatementList(layer5rule3class1)
                (4,12), # match_class StatementList(layer5rule3class1) -> association statements
                (12,5), # association statements  -> match_class InitializeConfiguration(layer5rule3class2)
                (5,13), # match_class InitializeConfiguration(layer5rule3class2) -> association config
                (13,6), # association config  -> match_class InstanceConfiguration(layer5rule3class3)
                (7,14), # apply_class StatementList(layer5rule3class4) -> association statements
                (14,8), # association statements  -> apply_class ExpressionStatement(layer5rule3class5)
                (8,15), # apply_class ExpressionStatement(layer5rule3class5) -> association expr
                (15,9), # association expr  -> apply_class FunctionCall(layer5rule3class6)
                (9,16), # apply_class FunctionCall(layer5rule3class6) -> association function
                (16,10), # association function  -> apply_class FunctionPrototype(layer5rule3class7)
                (7,17), # apply_class StatementList(layer5rule3class4) -> backward_association
                (17,3), #  backward_association -> apply_class TestCase(layer5rule3class0)
                (10,18), # apply_class FunctionPrototype(layer5rule3class7) -> backward_association
                (18,6), #  backward_association -> apply_class InstanceConfiguration(layer5rule3class3)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((7,'__ApplyAttribute'),('constant','TestCaseFunctionStatements')), ((10,'__ApplyAttribute'),('constant','InstanceConfigurationInit')), ]

        
