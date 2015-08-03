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
        self.vs[2]["rulename"] = """layer2rule0"""
        
        # match class Operation(layer2rule0class0) node
        self.add_node()
        self.vs[3]["name"] = """layer2rule0class0""" 
        self.vs[3]["classtype"] = """Operation"""
        self.vs[3]["mm__"] = """Operation"""
        self.vs[3]["cardinality"] = """+""" 
        # match_contains node for class Operation(layer2rule0class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        # match class ClientServerInterface() node
        self.add_node()
        self.vs[5]["name"] = """""" 
        self.vs[5]["classtype"] = """ClientServerInterface"""
        self.vs[5]["mm__"] = """ClientServerInterface"""
        self.vs[5]["cardinality"] = """+""" 
        # match_contains node for class ClientServerInterface()
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        
        
        # apply class PointerType(layer2rule0class1) node
        self.add_node()
        self.vs[7]["name"] = """layer2rule0class1""" 
        self.vs[7]["classtype"] = """PointerType"""
        self.vs[7]["mm__"] = """PointerType"""
        self.vs[7]["cardinality"] = """1"""
        # apply_contains node for class PointerType(layer2rule0class1)
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        # apply class FunctionRefType(layer2rule0class2) node
        self.add_node()
        self.vs[9]["name"] = """layer2rule0class2""" 
        self.vs[9]["classtype"] = """FunctionRefType"""
        self.vs[9]["mm__"] = """FunctionRefType"""
        self.vs[9]["cardinality"] = """1"""
        # apply_contains node for class FunctionRefType(layer2rule0class2)
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        
        
        # match association ClientServerInterface--contents-->Operation node
        self.add_node()
        self.vs[11]["associationType"] = """contents"""
        self.vs[11]["mm__"] = """directLink_S"""
        
        # apply association FunctionRefType--argTypes-->PointerType node
        self.add_node()
        self.vs[12]["associationType"] = """argTypes"""
        self.vs[12]["mm__"] = """directLink_T"""
        
        # backward association Operation---->PointerType node
        self.add_node()
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["mm__"] = """backward_link"""
        # backward association ClientServerInterface---->FunctionRefType node
        self.add_node()
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class Operation(layer2rule0class0)
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class ClientServerInterface()
                (1,8), # applymodel -> apply_contains
                (8,7), # apply_contains -> apply_class PointerType(layer2rule0class1)
                (1,10), # applymodel -> apply_contains
                (10,9), # apply_contains -> apply_class FunctionRefType(layer2rule0class2)
                (5,11), # match_class ClientServerInterface() -> association contents
                (11,3), # association contents  -> match_class Operation(layer2rule0class0)
                (9,12), # apply_class FunctionRefType(layer2rule0class2) -> association argTypes
                (12,7), # association argTypes  -> apply_class PointerType(layer2rule0class1)
                (7,13), # apply_class PointerType(layer2rule0class1) -> backward_association
                (13,3), #  backward_association -> apply_class Operation(layer2rule0class0)
                (9,14), # apply_class FunctionRefType(layer2rule0class2) -> backward_association
                (14,5), #  backward_association -> apply_class ClientServerInterface()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])
		
        # Add the attribute equations
        self["equations"] = [((7,'__ApplyAttribute'),('constant','InstancePointer')), ((9,'__ApplyAttribute'),('constant','FunctionRefType')), ]

        
