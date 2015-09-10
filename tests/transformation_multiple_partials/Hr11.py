from core.himesis import Himesis
import uuid

class Hr11(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule r11.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hr11, self).__init__(name='Hr11', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """r11"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'r11')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
 
        
        # match class Transition() node
        self.add_node()

        self.vs[3]["mm__"] = """Transition""" 
        self.vs[3]["attr1"] = """+""" 
        # match_contains node for class Transition()
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        # match class State() node
        self.add_node()

        self.vs[5]["mm__"] = """State""" 
        self.vs[5]["attr1"] = """+""" 
        # match_contains node for class State()
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        # match class StateMachine() node
        self.add_node()

        self.vs[7]["mm__"] = """StateMachine""" 
        self.vs[7]["attr1"] = """+""" 
        # match_contains node for class StateMachine()
        self.add_node()
        self.vs[8]["mm__"] = """match_contains"""
        # match class State() node
        self.add_node()

        self.vs[9]["mm__"] = """State""" 
        self.vs[9]["attr1"] = """+""" 
        # match_contains node for class State()
        self.add_node()
        self.vs[10]["mm__"] = """match_contains"""
        # match class State() node
        self.add_node()

        self.vs[11]["mm__"] = """State""" 
        self.vs[11]["attr1"] = """+""" 
        # match_contains node for class State()
        self.add_node()
        self.vs[12]["mm__"] = """match_contains"""
        
        
        # apply class ProcDef() node
        self.add_node()

        self.vs[13]["mm__"] = """ProcDef""" 
        self.vs[13]["attr1"] = """1"""
        # apply_contains node for class ProcDef()
        self.add_node()
        self.vs[14]["mm__"] = """apply_contains"""
        
        
        # match association State--relMatch-->Transition node
        self.add_node()
        self.vs[15]["attr1"] = """relMatch"""
        self.vs[15]["mm__"] = """directLink_S"""
        
        
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class Transition()
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class State()
                (0,8), # matchmodel -> match_contains
                (8,7), # match_contains -> match_class StateMachine()
                (0,10), # matchmodel -> match_contains
                (10,9), # match_contains -> match_class State()
                (0,12), # matchmodel -> match_contains
                (12,11), # match_contains -> match_class State()
                (1,14), # applymodel -> apply_contains
                (14,13), # apply_contains -> apply_class ProcDef()
                (5,15), # match_class State() -> association relMatch
                (15,3), # association relMatch  -> match_class Transition()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = []

        
