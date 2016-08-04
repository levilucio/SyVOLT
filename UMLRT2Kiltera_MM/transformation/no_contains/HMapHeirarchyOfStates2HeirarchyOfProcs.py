from core.himesis import Himesis
import uuid

class HMapHeirarchyOfStates2HeirarchyOfProcs(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule MapHeirarchyOfStates2HeirarchyOfProcs.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HMapHeirarchyOfStates2HeirarchyOfProcs, self).__init__(name='HMapHeirarchyOfStates2HeirarchyOfProcs', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """MapHeirarchyOfStates2HeirarchyOfProcs"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'MapHeirarchyOfStates2HeirarchyOfProcs')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["attr1"] = """MapHeirarchyOfStates2HeirarchyOfProcs"""
        
        # match class State() node
        self.add_node()
        
        self.vs[3]["mm__"] = """State""" 
        self.vs[3]["attr1"] = """+""" 
        # match class State() node
        self.add_node()
        
        self.vs[4]["mm__"] = """State""" 
        self.vs[4]["attr1"] = """+""" 
        
        
        # apply class LocalDef() node
        self.add_node()

        self.vs[5]["mm__"] = """LocalDef""" 
        self.vs[5]["attr1"] = """1"""
        # apply class ProcDef() node
        self.add_node()

        self.vs[6]["mm__"] = """ProcDef""" 
        self.vs[6]["attr1"] = """1"""
        
        
        # match association State--states-->State node
        self.add_node()
        self.vs[7]["attr1"] = """states"""
        self.vs[7]["mm__"] = """directLink_S"""
        
        # apply association LocalDef--def-->ProcDef node
        self.add_node()
        self.vs[8]["attr1"] = """def"""
        self.vs[8]["mm__"] = """directLink_T"""
        
        # backward association State---->LocalDef node
        self.add_node()

        self.vs[9]["mm__"] = """backward_link"""
        # backward association State---->ProcDef node
        self.add_node()

        self.vs[10]["mm__"] = """backward_link"""
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class State()
                (0,4), # matchmodel -> match_class State()
                (1,5), # applymodel -> -> apply_class LocalDef()
                (1,6), # applymodel -> -> apply_class ProcDef()
                (3,7), # match_class State() -> association states
                (7,4), # association states  -> match_class State()
                (5,8), # apply_class LocalDef() -> association def
                (8,6), # association def  -> apply_class ProcDef()
                (5,9), # apply_class LocalDef() -> backward_association
                (9,3), #  backward_association -> apply_class State()
                (6,10), # apply_class ProcDef() -> backward_association
                (10,4), #  backward_association -> apply_class State()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((3,'isComposite'),('constant','true')), ]

        
