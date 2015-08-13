from core.himesis import Himesis
import uuid

class Hr22(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule r22.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hr22, self).__init__(name='Hr22', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """r22"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'r22')
        
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
        # match class Transition() node
        self.add_node()

        self.vs[5]["mm__"] = """Transition""" 
        self.vs[5]["attr1"] = """+""" 
        # match_contains node for class Transition()
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        
        
        # apply class Listen() node
        self.add_node()

        self.vs[7]["mm__"] = """Listen""" 
        self.vs[7]["attr1"] = """1"""
        # apply_contains node for class Listen()
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        # apply class ProcDef() node
        self.add_node()

        self.vs[9]["mm__"] = """ProcDef""" 
        self.vs[9]["attr1"] = """1"""
        # apply_contains node for class ProcDef()
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        
        
        # match association State--relMatch-->Transition node
        self.add_node()
        self.vs[11]["attr1"] = """relMatch"""
        self.vs[11]["mm__"] = """directLink_S"""
        
        # apply association ProcDef--relApply2-->Listen node
        self.add_node()
        self.vs[12]["attr1"] = """relApply2"""
        self.vs[12]["mm__"] = """directLink_T"""
        
        # backward association Transition---->ProcDef node
        self.add_node()

        self.vs[13]["mm__"] = """backward_link"""
        # backward association State---->ProcDef node
        self.add_node()

        self.vs[14]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class State()
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class Transition()
                (1,8), # applymodel -> apply_contains
                (8,7), # apply_contains -> apply_class Listen()
                (1,10), # applymodel -> apply_contains
                (10,9), # apply_contains -> apply_class ProcDef()
                (3,11), # match_class State() -> association relMatch
                (11,5), # association relMatch  -> match_class Transition()
                (9,12), # apply_class ProcDef() -> association relApply2
                (12,7), # association relApply2  -> apply_class Listen()
                (9,13), # apply_class ProcDef() -> backward_association
                (13,5), #  backward_association -> apply_class Transition()
                (9,14), # apply_class ProcDef() -> backward_association
                (14,3), #  backward_association -> apply_class State()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = []

        
