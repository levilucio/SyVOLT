from core.himesis import Himesis
import uuid

class Hlayer1rule15(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule layer1rule15.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer1rule15, self).__init__(name='Hlayer1rule15', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """layer1rule15"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule15')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["rulename"] = """layer1rule15"""
        
        # match class Operation(layer1rule15class0) node
        self.add_node()
        self.vs[3]["name"] = """layer1rule15class0""" 
        self.vs[3]["classtype"] = """Operation"""
        self.vs[3]["mm__"] = """Operation"""
        self.vs[3]["cardinality"] = """+""" 
        # match_contains node for class Operation(layer1rule15class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        # match class OperationParameter(layer1rule15class1) node
        self.add_node()
        self.vs[5]["name"] = """layer1rule15class1""" 
        self.vs[5]["classtype"] = """OperationParameter"""
        self.vs[5]["mm__"] = """OperationParameter"""
        self.vs[5]["cardinality"] = """+""" 
        # match_contains node for class OperationParameter(layer1rule15class1)
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        
        
        # apply class FunctionPrototype(layer1rule15class2) node
        self.add_node()
        self.vs[7]["name"] = """layer1rule15class2""" 
        self.vs[7]["classtype"] = """FunctionPrototype"""
        self.vs[7]["mm__"] = """FunctionPrototype"""
        self.vs[7]["cardinality"] = """1"""
        # apply_contains node for class FunctionPrototype(layer1rule15class2)
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        # apply class Argument(layer1rule15class3) node
        self.add_node()
        self.vs[9]["name"] = """layer1rule15class3""" 
        self.vs[9]["classtype"] = """Argument"""
        self.vs[9]["mm__"] = """Argument"""
        self.vs[9]["cardinality"] = """1"""
        # apply_contains node for class Argument(layer1rule15class3)
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        
        
        # match association Operation--parameters-->OperationParameter node
        self.add_node()
        self.vs[11]["associationType"] = """parameters"""
        self.vs[11]["mm__"] = """directLink_S"""
        
        # apply association FunctionPrototype--arguments-->Argument node
        self.add_node()
        self.vs[12]["associationType"] = """arguments"""
        self.vs[12]["mm__"] = """directLink_T"""
        
        # backward association Operation---->FunctionPrototype node
        self.add_node()
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class Operation(layer1rule15class0)
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class OperationParameter(layer1rule15class1)
                (1,8), # applymodel -> apply_contains
                (8,7), # apply_contains -> apply_class FunctionPrototype(layer1rule15class2)
                (1,10), # applymodel -> apply_contains
                (10,9), # apply_contains -> apply_class Argument(layer1rule15class3)
                (3,11), # match_class Operation(layer1rule15class0) -> association parameters
                (11,5), # association parameters  -> match_class OperationParameter(layer1rule15class1)
                (7,12), # apply_class FunctionPrototype(layer1rule15class2) -> association arguments
                (12,9), # association arguments  -> apply_class Argument(layer1rule15class3)
                (7,13), # apply_class FunctionPrototype(layer1rule15class2) -> backward_association
                (13,3), #  backward_association -> apply_class Operation(layer1rule15class0)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])
		
        # Add the attribute equations
        self["equations"] = [((7,'__ApplyAttribute'),('constant','ProvidedPortFunctionPrototype')), ((9,'__ApplyAttribute'),('constant','ProvidedPortFunctionPrototypeArgument')), ((9,'name'),(5,'name')), ]

        
