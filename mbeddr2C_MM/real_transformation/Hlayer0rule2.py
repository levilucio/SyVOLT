from core.himesis import Himesis
import uuid

class Hlayer0rule2(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule layer0rule2.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer0rule2, self).__init__(name='Hlayer0rule2', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """layer0rule2"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule2')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
 
        
        # match class Operation(layer0rule2class0) node
        self.add_node()

        self.vs[3]["mm__"] = """Operation""" 
        self.vs[3]["attr1"] = """+""" 
        # match_contains node for class Operation(layer0rule2class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        # match class ClientServerInterface(layer0rule2class1) node
        self.add_node()

        self.vs[5]["mm__"] = """ClientServerInterface""" 
        self.vs[5]["attr1"] = """+""" 
        # match_contains node for class ClientServerInterface(layer0rule2class1)
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        
        
        # apply class CFunctionPointerStructMember(layer0rule2class2) node
        self.add_node()

        self.vs[7]["mm__"] = """CFunctionPointerStructMember""" 
        self.vs[7]["attr1"] = """1"""
        # apply_contains node for class CFunctionPointerStructMember(layer0rule2class2)
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        # apply class FunctionRefType(layer0rule2class3) node
        self.add_node()

        self.vs[9]["mm__"] = """FunctionRefType""" 
        self.vs[9]["attr1"] = """1"""
        # apply_contains node for class FunctionRefType(layer0rule2class3)
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        
        
        # match association ClientServerInterface--contents-->Operation node
        self.add_node()
        self.vs[11]["attr1"] = """contents"""
        self.vs[11]["mm__"] = """directLink_S"""
        
        # apply association CFunctionPointerStructMember--type-->FunctionRefType node
        self.add_node()
        self.vs[12]["attr1"] = """type"""
        self.vs[12]["mm__"] = """directLink_T"""
        
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class Operation(layer0rule2class0)
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class ClientServerInterface(layer0rule2class1)
                (1,8), # applymodel -> apply_contains
                (8,7), # apply_contains -> apply_class CFunctionPointerStructMember(layer0rule2class2)
                (1,10), # applymodel -> apply_contains
                (10,9), # apply_contains -> apply_class FunctionRefType(layer0rule2class3)
                (5,11), # match_class ClientServerInterface(layer0rule2class1) -> association contents
                (11,3), # association contents  -> match_class Operation(layer0rule2class0)
                (7,12), # apply_class CFunctionPointerStructMember(layer0rule2class2) -> association type
                (12,9), # association type  -> apply_class FunctionRefType(layer0rule2class3)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((7,'name'),(3,'name')), ((7,'__ApplyAttribute'),('constant','CFunctionPointerStructMember')), ((9,'__ApplyAttribute'),('constant','FunctionRefType')), ]

        
