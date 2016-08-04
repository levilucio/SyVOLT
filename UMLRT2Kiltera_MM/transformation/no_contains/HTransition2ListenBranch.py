from core.himesis import Himesis
import uuid

class HTransition2ListenBranch(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule Transition2ListenBranch.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HTransition2ListenBranch, self).__init__(name='HTransition2ListenBranch', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """Transition2ListenBranch"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Transition2ListenBranch')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["attr1"] = """Transition2ListenBranch"""
        
        # match class State() node
        self.add_node()
        
        self.vs[3]["mm__"] = """State""" 
        self.vs[3]["attr1"] = """+""" 
        # match class Transition() node
        self.add_node()
        
        self.vs[4]["mm__"] = """Transition""" 
        self.vs[4]["attr1"] = """+""" 
        # match class Trigger() node
        self.add_node()
        
        self.vs[5]["mm__"] = """Trigger""" 
        self.vs[5]["attr1"] = """1""" 
        # match class Signal() node
        self.add_node()
        
        self.vs[6]["mm__"] = """Signal""" 
        self.vs[6]["attr1"] = """1""" 
        
        
        # apply class Listen() node
        self.add_node()

        self.vs[7]["mm__"] = """Listen""" 
        self.vs[7]["attr1"] = """1"""
        # apply class ListenBranch() node
        self.add_node()

        self.vs[8]["mm__"] = """ListenBranch""" 
        self.vs[8]["attr1"] = """1"""
        # apply class Inst() node
        self.add_node()

        self.vs[9]["mm__"] = """Inst""" 
        self.vs[9]["attr1"] = """1"""
        
        
        # match association State--outgoingTransitions-->Transition node
        self.add_node()
        self.vs[10]["attr1"] = """outgoingTransitions"""
        self.vs[10]["mm__"] = """directLink_S"""
        # match association Transition--triggers-->Trigger node
        self.add_node()
        self.vs[11]["attr1"] = """triggers"""
        self.vs[11]["mm__"] = """directLink_S"""
        # match association Trigger--signal-->Signal node
        self.add_node()
        self.vs[12]["attr1"] = """signal"""
        self.vs[12]["mm__"] = """directLink_S"""
        
        # apply association Listen--branches-->ListenBranch node
        self.add_node()
        self.vs[13]["attr1"] = """branches"""
        self.vs[13]["mm__"] = """directLink_T"""
        # apply association ListenBranch--p-->Inst node
        self.add_node()
        self.vs[14]["attr1"] = """p"""
        self.vs[14]["mm__"] = """directLink_T"""
        
        # backward association State---->Listen node
        self.add_node()

        self.vs[15]["mm__"] = """backward_link"""
        # backward association Transition---->Inst node
        self.add_node()

        self.vs[16]["mm__"] = """backward_link"""
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class State()
                (0,4), # matchmodel -> match_class Transition()
                (0,5), # matchmodel -> match_class Trigger()
                (0,6), # matchmodel -> match_class Signal()
                (1,7), # applymodel -> -> apply_class Listen()
                (1,8), # applymodel -> -> apply_class ListenBranch()
                (1,9), # applymodel -> -> apply_class Inst()
                (3,10), # match_class State() -> association outgoingTransitions
                (10,4), # association outgoingTransitions  -> match_class Transition()
                (4,11), # match_class Transition() -> association triggers
                (11,5), # association triggers  -> match_class Trigger()
                (5,12), # match_class Trigger() -> association signal
                (12,6), # association signal  -> match_class Signal()
                (7,13), # apply_class Listen() -> association branches
                (13,8), # association branches  -> apply_class ListenBranch()
                (8,14), # apply_class ListenBranch() -> association p
                (14,9), # association p  -> apply_class Inst()
                (7,15), # apply_class Listen() -> backward_association
                (15,3), #  backward_association -> apply_class State()
                (9,16), # apply_class Inst() -> backward_association
                (16,4), #  backward_association -> apply_class Transition()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((3,'isComposite'),('constant','false')), ((3,'hasOutgoingTransitions'),('constant','true')), ((8,'channel'),(6,'name')), ]

        
