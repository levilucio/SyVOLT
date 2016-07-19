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
        self.vs[2]["attr1"] = """layer1rule15"""
        
        # match class Operation(layer1rule15class0) node
        self.add_node()
        
        self.vs[3]["mm__"] = """Operation""" 
        self.vs[3]["attr1"] = """+""" 
        # match class OperationParameter(layer1rule15class1) node
        self.add_node()
        
        self.vs[4]["mm__"] = """OperationParameter""" 
        self.vs[4]["attr1"] = """+""" 
        
        
        # apply class FunctionPrototype(layer1rule15class2) node
        self.add_node()

        self.vs[5]["mm__"] = """FunctionPrototype""" 
        self.vs[5]["attr1"] = """1"""
        # apply class Argument(layer1rule15class3) node
        self.add_node()

        self.vs[6]["mm__"] = """Argument""" 
        self.vs[6]["attr1"] = """1"""
        
        
        # match association Operation--parameters-->OperationParameter node
        self.add_node()
        self.vs[7]["attr1"] = """parameters"""
        self.vs[7]["mm__"] = """directLink_S"""
        
        # apply association FunctionPrototype--arguments-->Argument node
        self.add_node()
        self.vs[8]["attr1"] = """arguments"""
        self.vs[8]["mm__"] = """directLink_T"""
        
        # backward association Operation---->FunctionPrototype node
        self.add_node()

        self.vs[9]["mm__"] = """backward_link"""
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class Operation(layer1rule15class0)
                (0,4), # matchmodel -> match_class OperationParameter(layer1rule15class1)
                (1,5), # applymodel -> -> apply_class FunctionPrototype(layer1rule15class2)
                (1,6), # applymodel -> -> apply_class Argument(layer1rule15class3)
                (3,7), # match_class Operation(layer1rule15class0) -> association parameters
                (7,4), # association parameters  -> match_class OperationParameter(layer1rule15class1)
                (5,8), # apply_class FunctionPrototype(layer1rule15class2) -> association arguments
                (8,6), # association arguments  -> apply_class Argument(layer1rule15class3)
                (5,9), # apply_class FunctionPrototype(layer1rule15class2) -> backward_association
                (9,3), #  backward_association -> apply_class Operation(layer1rule15class0)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((5,'__ApplyAttribute'),('constant','ProvidedPortFunctionPrototype')), ((6,'__ApplyAttribute'),('constant','ProvidedPortFunctionPrototypeArgument')), ((6,'name'),(4,'name')), ]

        
