from core.himesis import Himesis
import uuid

class Hlayer2rule2(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule layer2rule2.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer2rule2, self).__init__(name='Hlayer2rule2', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """layer2rule2"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer2rule2')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
 
        
        # match class VoidType(layer2rule2class0) node
        self.add_node()

        self.vs[3]["mm__"] = """VoidType""" 
        self.vs[3]["attr1"] = """+""" 
        # match_contains node for class VoidType(layer2rule2class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        # match class OperationParameter(layer2rule2class1) node
        self.add_node()

        self.vs[5]["mm__"] = """OperationParameter""" 
        self.vs[5]["attr1"] = """+""" 
        # match_contains node for class OperationParameter(layer2rule2class1)
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        
        
        # apply class VoidType(layer2rule2class2) node
        self.add_node()

        self.vs[7]["mm__"] = """VoidType""" 
        self.vs[7]["attr1"] = """1"""
        # apply_contains node for class VoidType(layer2rule2class2)
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        # apply class Argument(layer2rule2class3) node
        self.add_node()

        self.vs[9]["mm__"] = """Argument""" 
        self.vs[9]["attr1"] = """1"""
        # apply_contains node for class Argument(layer2rule2class3)
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        
        
        # match association OperationParameter--type-->VoidType node
        self.add_node()
        self.vs[11]["attr1"] = """type"""
        self.vs[11]["mm__"] = """directLink_S"""
        
        # apply association Argument--type-->VoidType node
        self.add_node()
        self.vs[12]["attr1"] = """type"""
        self.vs[12]["mm__"] = """directLink_T"""
        
        # backward association OperationParameter---->Argument node
        self.add_node()

        self.vs[13]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class VoidType(layer2rule2class0)
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class OperationParameter(layer2rule2class1)
                (1,8), # applymodel -> apply_contains
                (8,7), # apply_contains -> apply_class VoidType(layer2rule2class2)
                (1,10), # applymodel -> apply_contains
                (10,9), # apply_contains -> apply_class Argument(layer2rule2class3)
                (5,11), # match_class OperationParameter(layer2rule2class1) -> association type
                (11,3), # association type  -> match_class VoidType(layer2rule2class0)
                (9,12), # apply_class Argument(layer2rule2class3) -> association type
                (12,7), # association type  -> apply_class VoidType(layer2rule2class2)
                (9,13), # apply_class Argument(layer2rule2class3) -> backward_association
                (13,5), #  backward_association -> apply_class OperationParameter(layer2rule2class1)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((9,'__ApplyAttribute'),('constant','ProvidedPortFunctionPrototypeArgument')), ]

        
