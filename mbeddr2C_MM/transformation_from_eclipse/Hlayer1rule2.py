from core.himesis import Himesis
import uuid

class Hlayer1rule2(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule layer1rule2.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer1rule2, self).__init__(name='Hlayer1rule2', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """layer1rule2"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule2')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
 
        
        # match class Operation(layer1rule2class0) node
        self.add_node()

        self.vs[3]["mm__"] = """Operation""" 
        self.vs[3]["attr1"] = """+""" 
        # match_contains node for class Operation(layer1rule2class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        # match class VoidType(layer1rule2class1) node
        self.add_node()

        self.vs[5]["mm__"] = """VoidType""" 
        self.vs[5]["attr1"] = """+""" 
        # match_contains node for class VoidType(layer1rule2class1)
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        
        
        # apply class FunctionRefType(layer1rule2class2) node
        self.add_node()

        self.vs[7]["mm__"] = """FunctionRefType""" 
        self.vs[7]["attr1"] = """1"""
        # apply_contains node for class FunctionRefType(layer1rule2class2)
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        # apply class VoidType(layer1rule2class3) node
        self.add_node()

        self.vs[9]["mm__"] = """VoidType""" 
        self.vs[9]["attr1"] = """1"""
        # apply_contains node for class VoidType(layer1rule2class3)
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        
        
        # match association Operation--type-->VoidType node
        self.add_node()
        self.vs[11]["attr1"] = """type"""
        self.vs[11]["mm__"] = """directLink_S"""
        
        # apply association FunctionRefType--returnType-->VoidType node
        self.add_node()
        self.vs[12]["attr1"] = """returnType"""
        self.vs[12]["mm__"] = """directLink_T"""
        
        # backward association VoidType---->VoidType node
        self.add_node()

        self.vs[13]["mm__"] = """backward_link"""
        # backward association Operation---->FunctionRefType node
        self.add_node()

        self.vs[14]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class Operation(layer1rule2class0)
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class VoidType(layer1rule2class1)
                (1,8), # applymodel -> apply_contains
                (8,7), # apply_contains -> apply_class FunctionRefType(layer1rule2class2)
                (1,10), # applymodel -> apply_contains
                (10,9), # apply_contains -> apply_class VoidType(layer1rule2class3)
                (3,11), # match_class Operation(layer1rule2class0) -> association type
                (11,5), # association type  -> match_class VoidType(layer1rule2class1)
                (7,12), # apply_class FunctionRefType(layer1rule2class2) -> association returnType
                (12,9), # association returnType  -> apply_class VoidType(layer1rule2class3)
                (9,13), # apply_class VoidType(layer1rule2class3) -> backward_association
                (13,5), #  backward_association -> apply_class VoidType(layer1rule2class1)
                (7,14), # apply_class FunctionRefType(layer1rule2class2) -> backward_association
                (14,3), #  backward_association -> apply_class Operation(layer1rule2class0)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((7,'__ApplyAttribute'),('constant','FunctionRefType')), ((9,'__ApplyAttribute'),('constant','VoidType')), ]

        
