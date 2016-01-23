from core.himesis import Himesis
import uuid

class HMapHierarchyOfStates2HierarchyOfProcs(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule MapHierarchyOfStates2HierarchyOfProcs.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HMapHierarchyOfStates2HierarchyOfProcs, self).__init__(name='HMapHierarchyOfStates2HierarchyOfProcs', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """MapHierarchyOfStates2HierarchyOfProcs"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'MapHierarchyOfStates2HierarchyOfProcs')
        
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
        # match class State() node
        self.add_node()

        self.vs[5]["mm__"] = """State""" 
        self.vs[5]["attr1"] = """+""" 
        # match_contains node for class State()
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        
        
        # apply class LocalDef() node
        self.add_node()

        self.vs[7]["mm__"] = """LocalDef""" 
        self.vs[7]["attr1"] = """1"""
        # apply_contains node for class LocalDef()
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        # apply class ProcDef() node
        self.add_node()

        self.vs[9]["mm__"] = """ProcDef""" 
        self.vs[9]["attr1"] = """1"""
        # apply_contains node for class ProcDef()
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        
        
        # match association State--states-->State node
        self.add_node()
        self.vs[11]["attr1"] = """states"""
        self.vs[11]["mm__"] = """directLink_S"""
        
        # apply association LocalDef--def-->ProcDef node
        self.add_node()
        self.vs[12]["attr1"] = """def"""
        self.vs[12]["mm__"] = """directLink_T"""
        
        # backward association State---->LocalDef node
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
                (6,5), # match_contains -> match_class State()
                (1,8), # applymodel -> apply_contains
                (8,7), # apply_contains -> apply_class LocalDef()
                (1,10), # applymodel -> apply_contains
                (10,9), # apply_contains -> apply_class ProcDef()
                (3,11), # match_class State() -> association states
                (11,5), # association states  -> match_class State()
                (7,12), # apply_class LocalDef() -> association def
                (12,9), # association def  -> apply_class ProcDef()
                (7,13), # apply_class LocalDef() -> backward_association
                (13,3), #  backward_association -> apply_class State()
                (9,14), # apply_class ProcDef() -> backward_association
                (14,5), #  backward_association -> apply_class State()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((7,'ApplyAttribute'),('constant','solveRef')), ]

        
