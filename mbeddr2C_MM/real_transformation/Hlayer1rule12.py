from core.himesis import Himesis
import uuid

class Hlayer1rule12(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule layer1rule12.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer1rule12, self).__init__(name='Hlayer1rule12', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """layer1rule12"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule12')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
 
        
        # match class ImplementationModule(layer1rule12class0) node
        self.add_node()

        self.vs[3]["mm__"] = """ImplementationModule""" 
        self.vs[3]["attr1"] = """+""" 
        # match_contains node for class ImplementationModule(layer1rule12class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        
        
        # apply class ImplementationModule(layer1rule12class1) node
        self.add_node()

        self.vs[5]["mm__"] = """ImplementationModule""" 
        self.vs[5]["attr1"] = """1"""
        # apply_contains node for class ImplementationModule(layer1rule12class1)
        self.add_node()
        self.vs[6]["mm__"] = """apply_contains"""
        # apply class FunctionPrototype(layer1rule12class2) node
        self.add_node()

        self.vs[7]["mm__"] = """FunctionPrototype""" 
        self.vs[7]["attr1"] = """1"""
        # apply_contains node for class FunctionPrototype(layer1rule12class2)
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        
        
        
        # apply association ImplementationModule--contents-->FunctionPrototype node
        self.add_node()
        self.vs[9]["attr1"] = """contents"""
        self.vs[9]["mm__"] = """directLink_T"""
        
        # backward association ImplementationModule---->ImplementationModule node
        self.add_node()

        self.vs[10]["mm__"] = """backward_link"""
        # backward association ImplementationModule---->FunctionPrototype node
        self.add_node()

        self.vs[11]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class ImplementationModule(layer1rule12class0)
                (1,6), # applymodel -> apply_contains
                (6,5), # apply_contains -> apply_class ImplementationModule(layer1rule12class1)
                (1,8), # applymodel -> apply_contains
                (8,7), # apply_contains -> apply_class FunctionPrototype(layer1rule12class2)
                (5,9), # apply_class ImplementationModule(layer1rule12class1) -> association contents
                (9,7), # association contents  -> apply_class FunctionPrototype(layer1rule12class2)
                (5,10), # apply_class ImplementationModule(layer1rule12class1) -> backward_association
                (10,3), #  backward_association -> apply_class ImplementationModule(layer1rule12class0)
                (7,11), # apply_class FunctionPrototype(layer1rule12class2) -> backward_association
                (11,3), #  backward_association -> apply_class ImplementationModule(layer1rule12class0)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((5,'__ApplyAttribute'),('constant','ImplementationModule')), ((7,'__ApplyAttribute'),('constant','ProvidedPortFunctionPrototype')), ]

        
