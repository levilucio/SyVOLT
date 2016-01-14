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
        # match class Trigger() node
        self.add_node()

        self.vs[7]["mm__"] = """Trigger""" 
        self.vs[7]["attr1"] = """1""" 
        # match_contains node for class Trigger()
        self.add_node()
        self.vs[8]["mm__"] = """match_contains"""
        # match class Signal() node
        self.add_node()

        self.vs[9]["mm__"] = """Signal""" 
        self.vs[9]["attr1"] = """1""" 
        # match_contains node for class Signal()
        self.add_node()
        self.vs[10]["mm__"] = """match_contains"""
        
        
        # apply class Listen() node
        self.add_node()

        self.vs[11]["mm__"] = """Listen""" 
        self.vs[11]["attr1"] = """1"""
        # apply_contains node for class Listen()
        self.add_node()
        self.vs[12]["mm__"] = """apply_contains"""
        # apply class ListenBranch() node
        self.add_node()

        self.vs[13]["mm__"] = """ListenBranch""" 
        self.vs[13]["attr1"] = """1"""
        # apply_contains node for class ListenBranch()
        self.add_node()
        self.vs[14]["mm__"] = """apply_contains"""
        # apply class Inst() node
        self.add_node()

        self.vs[15]["mm__"] = """Inst""" 
        self.vs[15]["attr1"] = """1"""
        # apply_contains node for class Inst()
        self.add_node()
        self.vs[16]["mm__"] = """apply_contains"""
        
        
        # match association State--outgoingTransitions-->Transition node
        self.add_node()
        self.vs[17]["attr1"] = """outgoingTransitions"""
        self.vs[17]["mm__"] = """directLink_S"""
        # match association Transition--triggers-->Trigger node
        self.add_node()
        self.vs[18]["attr1"] = """triggers"""
        self.vs[18]["mm__"] = """directLink_S"""
        # match association Trigger--signal-->Signal node
        self.add_node()
        self.vs[19]["attr1"] = """signal"""
        self.vs[19]["mm__"] = """directLink_S"""
        
        # apply association Listen--branches-->ListenBranch node
        self.add_node()
        self.vs[20]["attr1"] = """branches"""
        self.vs[20]["mm__"] = """directLink_T"""
        # apply association ListenBranch--p-->Inst node
        self.add_node()
        self.vs[21]["attr1"] = """p"""
        self.vs[21]["mm__"] = """directLink_T"""
        
        # backward association State---->Listen node
        self.add_node()

        self.vs[22]["mm__"] = """backward_link"""
        # backward association Transition---->Inst node
        self.add_node()

        self.vs[23]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class State()
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class Transition()
                (0,8), # matchmodel -> match_contains
                (8,7), # match_contains -> match_class Trigger()
                (0,10), # matchmodel -> match_contains
                (10,9), # match_contains -> match_class Signal()
                (1,12), # applymodel -> apply_contains
                (12,11), # apply_contains -> apply_class Listen()
                (1,14), # applymodel -> apply_contains
                (14,13), # apply_contains -> apply_class ListenBranch()
                (1,16), # applymodel -> apply_contains
                (16,15), # apply_contains -> apply_class Inst()
                (3,17), # match_class State() -> association outgoingTransitions
                (17,5), # association outgoingTransitions  -> match_class Transition()
                (5,18), # match_class Transition() -> association triggers
                (18,7), # association triggers  -> match_class Trigger()
                (7,19), # match_class Trigger() -> association signal
                (19,9), # association signal  -> match_class Signal()
                (11,20), # apply_class Listen() -> association branches
                (20,13), # association branches  -> apply_class ListenBranch()
                (13,21), # apply_class ListenBranch() -> association p
                (21,15), # association p  -> apply_class Inst()
                (11,22), # apply_class Listen() -> backward_association
                (22,3), #  backward_association -> apply_class State()
                (15,23), # apply_class Inst() -> backward_association
                (23,5), #  backward_association -> apply_class Transition()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((3,'isComposite'),('constant','false')), ((3,'hasOutgoingTransitions'),('constant','true')), ((11,'ApplyAttribute'),('constant','solveRef')), ((13,'channel'),(9,'name')), ((15,'ApplyAttribute'),('constant','solveRef')), ]

        
