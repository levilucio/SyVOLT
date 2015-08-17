from core.himesis import Himesis
import uuid

class Hr7(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule r7.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hr7, self).__init__(name='Hr7', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """r7"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'r7')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
 
        
        # match class State() node
        self.add_node()

        self.vs[3]["mm__"] = """State""" 
        self.vs[3]["attr1"] = """+""" 
        # match_contains node for class State()
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        
        
        # apply class ProcDef() node
        self.add_node()

        self.vs[5]["mm__"] = """ProcDef""" 
        self.vs[5]["attr1"] = """1"""
        # apply_contains node for class ProcDef()
        self.add_node()
        self.vs[6]["mm__"] = """apply_contains"""
        # apply class Listen() node
        self.add_node()

        self.vs[7]["mm__"] = """Listen""" 
        self.vs[7]["attr1"] = """1"""
        # apply_contains node for class Listen()
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        
        
        
        # apply association ProcDef--relApply2-->Listen node
        self.add_node()
        self.vs[9]["attr1"] = """relApply2"""
        self.vs[9]["mm__"] = """directLink_T"""
        
        # backward association State---->ProcDef node
        self.add_node()

        self.vs[10]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class State()
                (1,6), # applymodel -> apply_contains
                (6,5), # apply_contains -> apply_class ProcDef()
                (1,8), # applymodel -> apply_contains
                (8,7), # apply_contains -> apply_class Listen()
                (5,9), # apply_class ProcDef() -> association relApply2
                (9,7), # association relApply2  -> apply_class Listen()
                (5,10), # apply_class ProcDef() -> backward_association
                (10,3), #  backward_association -> apply_class State()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = []

        
