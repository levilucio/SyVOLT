from core.himesis import Himesis
import uuid

class Hr12(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule r12.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hr12, self).__init__(name='Hr12', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """r12"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'r12')
        
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
        # match class ExitPoint() node
        self.add_node()

        self.vs[5]["mm__"] = """ExitPoint""" 
        self.vs[5]["attr1"] = """+""" 
        # match_contains node for class ExitPoint()
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        
        
        # apply class ProcDef() node
        self.add_node()

        self.vs[7]["mm__"] = """ProcDef""" 
        self.vs[7]["attr1"] = """1"""
        # apply_contains node for class ProcDef()
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        
        
        
        
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class State()
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class ExitPoint()
                (1,8), # applymodel -> apply_contains
                (8,7), # apply_contains -> apply_class ProcDef()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = []

        
