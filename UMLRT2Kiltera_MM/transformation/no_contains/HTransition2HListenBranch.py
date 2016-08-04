from core.himesis import Himesis
import uuid

class HTransition2HListenBranch(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule Transition2HListenBranch.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HTransition2HListenBranch, self).__init__(name='HTransition2HListenBranch', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """Transition2HListenBranch"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Transition2HListenBranch')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["attr1"] = """Transition2HListenBranch"""
        
        # match class Transition() node
        self.add_node()
        
        self.vs[3]["mm__"] = """Transition""" 
        self.vs[3]["attr1"] = """+""" 
        # match class Vertex() node
        self.add_node()
        
        self.vs[4]["mm__"] = """Vertex""" 
        self.vs[4]["attr1"] = """+""" 
        # match class StateMachine() node
        self.add_node()
        
        self.vs[5]["mm__"] = """StateMachine""" 
        self.vs[5]["attr1"] = """+""" 
        # match class State() node
        self.add_node()
        
        self.vs[6]["mm__"] = """State""" 
        self.vs[6]["attr1"] = """1""" 
        # match class Trigger() node
        self.add_node()
        
        self.vs[7]["mm__"] = """Trigger""" 
        self.vs[7]["attr1"] = """1""" 
        # match class Signal() node
        self.add_node()
        
        self.vs[8]["mm__"] = """Signal""" 
        self.vs[8]["attr1"] = """1""" 
        # match class State() node
        self.add_node()
        
        self.vs[9]["mm__"] = """State""" 
        self.vs[9]["attr1"] = """+""" 
        
        
        # apply class ListenBranch() node
        self.add_node()

        self.vs[10]["mm__"] = """ListenBranch""" 
        self.vs[10]["attr1"] = """1"""
        # apply class Seq() node
        self.add_node()

        self.vs[11]["mm__"] = """Seq""" 
        self.vs[11]["attr1"] = """1"""
        # apply class Trigger() node
        self.add_node()

        self.vs[12]["mm__"] = """Trigger""" 
        self.vs[12]["attr1"] = """1"""
        # apply class Listen() node
        self.add_node()

        self.vs[13]["mm__"] = """Listen""" 
        self.vs[13]["attr1"] = """1"""
        # apply class ListenBranch() node
        self.add_node()

        self.vs[14]["mm__"] = """ListenBranch""" 
        self.vs[14]["attr1"] = """1"""
        # apply class Inst() node
        self.add_node()

        self.vs[15]["mm__"] = """Inst""" 
        self.vs[15]["attr1"] = """1"""
        # apply class Listen() node
        self.add_node()

        self.vs[16]["mm__"] = """Listen""" 
        self.vs[16]["attr1"] = """1"""
        
        
        # match association Transition--src-->Vertex node
        self.add_node()
        self.vs[17]["attr1"] = """src"""
        self.vs[17]["mm__"] = """directLink_S"""
        # match association Vertex--owningStateMachine-->StateMachine node
        self.add_node()
        self.vs[18]["attr1"] = """owningStateMachine"""
        self.vs[18]["mm__"] = """directLink_S"""
        # match association StateMachine--states-->State node
        self.add_node()
        self.vs[19]["attr1"] = """states"""
        self.vs[19]["mm__"] = """directLink_S"""
        # match association Transition--triggers-->Trigger node
        self.add_node()
        self.vs[20]["attr1"] = """triggers"""
        self.vs[20]["mm__"] = """directLink_S"""
        # match association Trigger--signal-->Signal node
        self.add_node()
        self.vs[21]["attr1"] = """signal"""
        self.vs[21]["mm__"] = """directLink_S"""
        # match association State--outgoingTransitions-->Transition node
        self.add_node()
        self.vs[22]["attr1"] = """outgoingTransitions"""
        self.vs[22]["mm__"] = """directLink_S"""
        
        # apply association ListenBranch--p-->Seq node
        self.add_node()
        self.vs[23]["attr1"] = """p"""
        self.vs[23]["mm__"] = """directLink_T"""
        # apply association Seq--p-->Trigger node
        self.add_node()
        self.vs[24]["attr1"] = """p"""
        self.vs[24]["mm__"] = """directLink_T"""
        # apply association Seq--p-->Listen node
        self.add_node()
        self.vs[25]["attr1"] = """p"""
        self.vs[25]["mm__"] = """directLink_T"""
        # apply association Listen--branches-->ListenBranch node
        self.add_node()
        self.vs[26]["attr1"] = """branches"""
        self.vs[26]["mm__"] = """directLink_T"""
        # apply association ListenBranch--p-->Inst node
        self.add_node()
        self.vs[27]["attr1"] = """p"""
        self.vs[27]["mm__"] = """directLink_T"""
        # apply association Listen--branches-->ListenBranch node
        self.add_node()
        self.vs[28]["attr1"] = """branches"""
        self.vs[28]["mm__"] = """directLink_T"""
        
        # backward association Transition---->Inst node
        self.add_node()

        self.vs[29]["mm__"] = """backward_link"""
        # backward association State---->Listen node
        self.add_node()

        self.vs[30]["mm__"] = """backward_link"""
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class Transition()
                (0,4), # matchmodel -> match_class Vertex()
                (0,5), # matchmodel -> match_class StateMachine()
                (0,6), # matchmodel -> match_class State()
                (0,7), # matchmodel -> match_class Trigger()
                (0,8), # matchmodel -> match_class Signal()
                (0,9), # matchmodel -> match_class State()
                (1,10), # applymodel -> -> apply_class ListenBranch()
                (1,11), # applymodel -> -> apply_class Seq()
                (1,12), # applymodel -> -> apply_class Trigger()
                (1,13), # applymodel -> -> apply_class Listen()
                (1,14), # applymodel -> -> apply_class ListenBranch()
                (1,15), # applymodel -> -> apply_class Inst()
                (1,16), # applymodel -> -> apply_class Listen()
                (3,17), # match_class Transition() -> association src
                (17,4), # association src  -> match_class Vertex()
                (4,18), # match_class Vertex() -> association owningStateMachine
                (18,5), # association owningStateMachine  -> match_class StateMachine()
                (5,19), # match_class StateMachine() -> association states
                (19,6), # association states  -> match_class State()
                (3,20), # match_class Transition() -> association triggers
                (20,7), # association triggers  -> match_class Trigger()
                (7,21), # match_class Trigger() -> association signal
                (21,8), # association signal  -> match_class Signal()
                (9,22), # match_class State() -> association outgoingTransitions
                (22,3), # association outgoingTransitions  -> match_class Transition()
                (10,23), # apply_class ListenBranch() -> association p
                (23,11), # association p  -> apply_class Seq()
                (11,24), # apply_class Seq() -> association p
                (24,12), # association p  -> apply_class Trigger()
                (11,25), # apply_class Seq() -> association p
                (25,13), # association p  -> apply_class Listen()
                (13,26), # apply_class Listen() -> association branches
                (26,14), # association branches  -> apply_class ListenBranch()
                (14,27), # apply_class ListenBranch() -> association p
                (27,15), # association p  -> apply_class Inst()
                (16,28), # apply_class Listen() -> association branches
                (28,10), # association branches  -> apply_class ListenBranch()
                (15,29), # apply_class Inst() -> backward_association
                (29,3), #  backward_association -> apply_class Transition()
                (16,30), # apply_class Listen() -> backward_association
                (30,9), #  backward_association -> apply_class State()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((10,'channel'),(8,'name')), ((12,'channel'),('constant','exit_in')), ((14,'channel'),('constant','exack_in')), ((15,'__ApplyAttribute'),('constant','instfortrans')), ((16,'__ApplyAttribute'),('constant','listenhproc')), ]

        
