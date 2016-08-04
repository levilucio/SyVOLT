from core.himesis import Himesis
import uuid

class HBasicState2ProcDef(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule BasicState2ProcDef.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HBasicState2ProcDef, self).__init__(name='HBasicState2ProcDef', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """BasicState2ProcDef"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'BasicState2ProcDef')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["attr1"] = """BasicState2ProcDef"""
        
        # match class State() node
        self.add_node()
        
        self.vs[3]["mm__"] = """State""" 
        self.vs[3]["attr1"] = """+""" 
        
        
        # apply class ProcDef() node
        self.add_node()

        self.vs[4]["mm__"] = """ProcDef""" 
        self.vs[4]["attr1"] = """1"""
        # apply class Listen() node
        self.add_node()

        self.vs[5]["mm__"] = """Listen""" 
        self.vs[5]["attr1"] = """1"""
        # apply class ListenBranch() node
        self.add_node()

        self.vs[6]["mm__"] = """ListenBranch""" 
        self.vs[6]["attr1"] = """1"""
        # apply class Trigger() node
        self.add_node()

        self.vs[7]["mm__"] = """Trigger""" 
        self.vs[7]["attr1"] = """1"""
        
        
        
        # apply association ProcDef--p-->Listen node
        self.add_node()
        self.vs[8]["attr1"] = """p"""
        self.vs[8]["mm__"] = """directLink_T"""
        # apply association Listen--branches-->ListenBranch node
        self.add_node()
        self.vs[9]["attr1"] = """branches"""
        self.vs[9]["mm__"] = """directLink_T"""
        # apply association ListenBranch--p-->Trigger node
        self.add_node()
        self.vs[10]["attr1"] = """p"""
        self.vs[10]["mm__"] = """directLink_T"""
        
        # backward association State---->ProcDef node
        self.add_node()

        self.vs[11]["mm__"] = """backward_link"""
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class State()
                (1,4), # applymodel -> -> apply_class ProcDef()
                (1,5), # applymodel -> -> apply_class Listen()
                (1,6), # applymodel -> -> apply_class ListenBranch()
                (1,7), # applymodel -> -> apply_class Trigger()
                (4,8), # apply_class ProcDef() -> association p
                (8,5), # association p  -> apply_class Listen()
                (5,9), # apply_class Listen() -> association branches
                (9,6), # association branches  -> apply_class ListenBranch()
                (6,10), # apply_class ListenBranch() -> association p
                (10,7), # association p  -> apply_class Trigger()
                (4,11), # apply_class ProcDef() -> backward_association
                (11,3), #  backward_association -> apply_class State()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((3,'isComposite'),('constant','false')), ((3,'hasOutgoingTransitions'),('constant','true')), ((6,'channel'),('constant','exit')), ((7,'channel'),('constant','exack')), ]

        
