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
        self.vs[2]["attr1"] = """layer5rule2"""
        
        # match class InstanceConfiguration(layer5rule2class0) node
        self.add_node()
        
        self.vs[3]["mm__"] = """InstanceConfiguration""" 
        self.vs[3]["attr1"] = """+""" 
        # match class ComponentInstance(layer5rule2class1) node
        self.add_node()
        
        self.vs[4]["mm__"] = """ComponentInstance""" 
        self.vs[4]["attr1"] = """+""" 
        
        
        # apply class StatementList(layer5rule2class2) node
        self.add_node()

        self.vs[5]["mm__"] = """StatementList""" 
        self.vs[5]["attr1"] = """1"""
        # apply class FunctionPrototype(layer5rule2class3) node
        self.add_node()

        self.vs[6]["mm__"] = """FunctionPrototype""" 
        self.vs[6]["attr1"] = """1"""
        # apply class ExpressionStatement(layer5rule2class4) node
        self.add_node()

        self.vs[7]["mm__"] = """ExpressionStatement""" 
        self.vs[7]["attr1"] = """1"""
        # apply class FunctionCall(layer5rule2class5) node
        self.add_node()

        self.vs[8]["mm__"] = """FunctionCall""" 
        self.vs[8]["attr1"] = """1"""
        
        
        # match association InstanceConfiguration--contents-->ComponentInstance node
        self.add_node()
        self.vs[9]["attr1"] = """contents"""
        self.vs[9]["mm__"] = """directLink_S"""
        
        # apply association StatementList--statements-->ExpressionStatement node
        self.add_node()
        self.vs[10]["attr1"] = """statements"""
        self.vs[10]["mm__"] = """directLink_T"""
        # apply association ExpressionStatement--expr-->FunctionCall node
        self.add_node()
        self.vs[11]["attr1"] = """expr"""
        self.vs[11]["mm__"] = """directLink_T"""
        # apply association FunctionCall--function-->FunctionPrototype node
        self.add_node()
        self.vs[12]["attr1"] = """function"""
        self.vs[12]["mm__"] = """directLink_T"""
        
        # backward association InstanceConfiguration---->StatementList node
        self.add_node()

        self.vs[13]["mm__"] = """backward_link"""
        # backward association ComponentInstance---->FunctionPrototype node
        self.add_node()

        self.vs[14]["mm__"] = """backward_link"""
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class InstanceConfiguration(layer5rule2class0)
                (0,4), # matchmodel -> match_class ComponentInstance(layer5rule2class1)
                (1,5), # applymodel -> -> apply_class StatementList(layer5rule2class2)
                (1,6), # applymodel -> -> apply_class FunctionPrototype(layer5rule2class3)
                (1,7), # applymodel -> -> apply_class ExpressionStatement(layer5rule2class4)
                (1,8), # applymodel -> -> apply_class FunctionCall(layer5rule2class5)
                (3,9), # match_class InstanceConfiguration(layer5rule2class0) -> association contents
                (9,4), # association contents  -> match_class ComponentInstance(layer5rule2class1)
                (5,10), # apply_class StatementList(layer5rule2class2) -> association statements
                (10,7), # association statements  -> apply_class ExpressionStatement(layer5rule2class4)
                (7,11), # apply_class ExpressionStatement(layer5rule2class4) -> association expr
                (11,8), # association expr  -> apply_class FunctionCall(layer5rule2class5)
                (8,12), # apply_class FunctionCall(layer5rule2class5) -> association function
                (12,6), # association function  -> apply_class FunctionPrototype(layer5rule2class3)
                (5,13), # apply_class StatementList(layer5rule2class2) -> backward_association
                (13,3), #  backward_association -> apply_class InstanceConfiguration(layer5rule2class0)
                (6,14), # apply_class FunctionPrototype(layer5rule2class3) -> backward_association
                (14,4), #  backward_association -> apply_class ComponentInstance(layer5rule2class1)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((5,'__ApplyAttribute'),('constant','InstancesInitFunctionBody')), ((6,'__ApplyAttribute'),('constant','WireFunctionPrototype')), ]

        
