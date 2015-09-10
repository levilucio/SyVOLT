from core.himesis import Himesis
import uuid

class Hlayer2rule0(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule layer2rule0.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer2rule0, self).__init__(name='Hlayer2rule0', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """layer2rule0"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer2rule0')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
 
        
        # match class Operation(layer2rule0class0) node
        self.add_node()

        self.vs[3]["mm__"] = """Operation""" 
        self.vs[3]["attr1"] = """+""" 
        # match_contains node for class Operation(layer2rule0class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        
        
        # apply class PointerType(layer2rule0class1) node
        self.add_node()

        self.vs[5]["mm__"] = """PointerType""" 
        self.vs[5]["attr1"] = """1"""
        # apply_contains node for class PointerType(layer2rule0class1)
        self.add_node()
        self.vs[6]["mm__"] = """apply_contains"""
        # apply class FunctionRefType(layer2rule0class2) node
        self.add_node()

        self.vs[7]["mm__"] = """FunctionRefType""" 
        self.vs[7]["attr1"] = """1"""
        # apply_contains node for class FunctionRefType(layer2rule0class2)
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        
        
        
        # apply association FunctionRefType--argTypes-->PointerType node
        self.add_node()
        self.vs[9]["attr1"] = """argTypes"""
        self.vs[9]["mm__"] = """directLink_T"""
        
        # backward association Operation---->PointerType node
        self.add_node()

        self.vs[10]["mm__"] = """backward_link"""
        # backward association Operation---->FunctionRefType node
        self.add_node()

        self.vs[11]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class Operation(layer2rule0class0)
                (1,6), # applymodel -> apply_contains
                (6,5), # apply_contains -> apply_class PointerType(layer2rule0class1)
                (1,8), # applymodel -> apply_contains
                (8,7), # apply_contains -> apply_class FunctionRefType(layer2rule0class2)
                (7,9), # apply_class FunctionRefType(layer2rule0class2) -> association argTypes
                (9,5), # association argTypes  -> apply_class PointerType(layer2rule0class1)
                (5,10), # apply_class PointerType(layer2rule0class1) -> backward_association
                (10,3), #  backward_association -> apply_class Operation(layer2rule0class0)
                (7,11), # apply_class FunctionRefType(layer2rule0class2) -> backward_association
                (11,3), #  backward_association -> apply_class Operation(layer2rule0class0)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((5,'__ApplyAttribute'),('constant','InstancePointer')), ((7,'__ApplyAttribute'),('constant','FunctionRefType')), ]

        
