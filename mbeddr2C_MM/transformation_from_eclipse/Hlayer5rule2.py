from core.himesis import Himesis
import uuid

class Hlayer5rule2(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule layer5rule2.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer5rule2, self).__init__(name='Hlayer5rule2', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """layer5rule2"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule2')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
 
        
        # match class InstanceConfiguration(layer5rule2class0) node
        self.add_node()

        self.vs[3]["mm__"] = """InstanceConfiguration""" 
        self.vs[3]["attr1"] = """+""" 
        # match_contains node for class InstanceConfiguration(layer5rule2class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        # match class ComponentInstance(layer5rule2class1) node
        self.add_node()

        self.vs[5]["mm__"] = """ComponentInstance""" 
        self.vs[5]["attr1"] = """+""" 
        # match_contains node for class ComponentInstance(layer5rule2class1)
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        
        
        # apply class StatementList(layer5rule2class2) node
        self.add_node()

        self.vs[7]["mm__"] = """StatementList""" 
        self.vs[7]["attr1"] = """1"""
        # apply_contains node for class StatementList(layer5rule2class2)
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        # apply class FunctionPrototype(layer5rule2class3) node
        self.add_node()

        self.vs[9]["mm__"] = """FunctionPrototype""" 
        self.vs[9]["attr1"] = """1"""
        # apply_contains node for class FunctionPrototype(layer5rule2class3)
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        # apply class ExpressionStatement(layer5rule2class4) node
        self.add_node()

        self.vs[11]["mm__"] = """ExpressionStatement""" 
        self.vs[11]["attr1"] = """1"""
        # apply_contains node for class ExpressionStatement(layer5rule2class4)
        self.add_node()
        self.vs[12]["mm__"] = """apply_contains"""
        # apply class FunctionCall(layer5rule2class5) node
        self.add_node()

        self.vs[13]["mm__"] = """FunctionCall""" 
        self.vs[13]["attr1"] = """1"""
        # apply_contains node for class FunctionCall(layer5rule2class5)
        self.add_node()
        self.vs[14]["mm__"] = """apply_contains"""
        
        
        # match association InstanceConfiguration--contents-->ComponentInstance node
        self.add_node()
        self.vs[15]["attr1"] = """contents"""
        self.vs[15]["mm__"] = """directLink_S"""
        
        # apply association StatementList--statements-->ExpressionStatement node
        self.add_node()
        self.vs[16]["attr1"] = """statements"""
        self.vs[16]["mm__"] = """directLink_T"""
        # apply association ExpressionStatement--expr-->FunctionCall node
        self.add_node()
        self.vs[17]["attr1"] = """expr"""
        self.vs[17]["mm__"] = """directLink_T"""
        # apply association FunctionCall--function-->FunctionPrototype node
        self.add_node()
        self.vs[18]["attr1"] = """function"""
        self.vs[18]["mm__"] = """directLink_T"""
        
        # backward association InstanceConfiguration---->StatementList node
        self.add_node()

        self.vs[19]["mm__"] = """backward_link"""
        # backward association ComponentInstance---->FunctionPrototype node
        self.add_node()

        self.vs[20]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class InstanceConfiguration(layer5rule2class0)
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class ComponentInstance(layer5rule2class1)
                (1,8), # applymodel -> apply_contains
                (8,7), # apply_contains -> apply_class StatementList(layer5rule2class2)
                (1,10), # applymodel -> apply_contains
                (10,9), # apply_contains -> apply_class FunctionPrototype(layer5rule2class3)
                (1,12), # applymodel -> apply_contains
                (12,11), # apply_contains -> apply_class ExpressionStatement(layer5rule2class4)
                (1,14), # applymodel -> apply_contains
                (14,13), # apply_contains -> apply_class FunctionCall(layer5rule2class5)
                (3,15), # match_class InstanceConfiguration(layer5rule2class0) -> association contents
                (15,5), # association contents  -> match_class ComponentInstance(layer5rule2class1)
                (7,16), # apply_class StatementList(layer5rule2class2) -> association statements
                (16,11), # association statements  -> apply_class ExpressionStatement(layer5rule2class4)
                (11,17), # apply_class ExpressionStatement(layer5rule2class4) -> association expr
                (17,13), # association expr  -> apply_class FunctionCall(layer5rule2class5)
                (13,18), # apply_class FunctionCall(layer5rule2class5) -> association function
                (18,9), # association function  -> apply_class FunctionPrototype(layer5rule2class3)
                (7,19), # apply_class StatementList(layer5rule2class2) -> backward_association
                (19,3), #  backward_association -> apply_class InstanceConfiguration(layer5rule2class0)
                (9,20), # apply_class FunctionPrototype(layer5rule2class3) -> backward_association
                (20,5), #  backward_association -> apply_class ComponentInstance(layer5rule2class1)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((7,'__ApplyAttribute'),('constant','InstancesInitFunctionBody')), ((9,'__ApplyAttribute'),('constant','WireFunctionPrototype')), ]

        
