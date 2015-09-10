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
 
        
        # match class Transition() node
        self.add_node()

        self.vs[3]["mm__"] = """Transition""" 
        self.vs[3]["attr1"] = """+""" 
        # match_contains node for class Transition()
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        # match class Vertex() node
        self.add_node()

        self.vs[5]["mm__"] = """Vertex""" 
        self.vs[5]["attr1"] = """+""" 
        # match_contains node for class Vertex()
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
        self.vs[9]["attr1"] = """1""" 
        # match_contains node for class State()
        self.add_node()
        self.vs[10]["mm__"] = """match_contains"""
        # match class Trigger() node
        self.add_node()

        self.vs[11]["mm__"] = """Trigger""" 
        self.vs[11]["attr1"] = """1""" 
        # match_contains node for class Trigger()
        self.add_node()
        self.vs[12]["mm__"] = """match_contains"""
        # match class Signal() node
        self.add_node()

        self.vs[13]["mm__"] = """Signal""" 
        self.vs[13]["attr1"] = """1""" 
        # match_contains node for class Signal()
        self.add_node()
        self.vs[14]["mm__"] = """match_contains"""
        # match class State() node
        self.add_node()

        self.vs[15]["mm__"] = """State""" 
        self.vs[15]["attr1"] = """+""" 
        # match_contains node for class State()
        self.add_node()
        self.vs[16]["mm__"] = """match_contains"""
        
        
        # apply class ListenBranch() node
        self.add_node()

        self.vs[17]["mm__"] = """ListenBranch""" 
        self.vs[17]["attr1"] = """1"""
        # apply_contains node for class ListenBranch()
        self.add_node()
        self.vs[18]["mm__"] = """apply_contains"""
        # apply class Seq() node
        self.add_node()

        self.vs[19]["mm__"] = """Seq""" 
        self.vs[19]["attr1"] = """1"""
        # apply_contains node for class Seq()
        self.add_node()
        self.vs[20]["mm__"] = """apply_contains"""
        # apply class Trigger() node
        self.add_node()

        self.vs[21]["mm__"] = """Trigger""" 
        self.vs[21]["attr1"] = """1"""
        # apply_contains node for class Trigger()
        self.add_node()
        self.vs[22]["mm__"] = """apply_contains"""
        # apply class Listen() node
        self.add_node()

        self.vs[23]["mm__"] = """Listen""" 
        self.vs[23]["attr1"] = """1"""
        # apply_contains node for class Listen()
        self.add_node()
        self.vs[24]["mm__"] = """apply_contains"""
        # apply class ListenBranch() node
        self.add_node()

        self.vs[25]["mm__"] = """ListenBranch""" 
        self.vs[25]["attr1"] = """1"""
        # apply_contains node for class ListenBranch()
        self.add_node()
        self.vs[26]["mm__"] = """apply_contains"""
        # apply class Inst() node
        self.add_node()

        self.vs[27]["mm__"] = """Inst""" 
        self.vs[27]["attr1"] = """1"""
        # apply_contains node for class Inst()
        self.add_node()
        self.vs[28]["mm__"] = """apply_contains"""
        # apply class Listen() node
        self.add_node()

        self.vs[29]["mm__"] = """Listen""" 
        self.vs[29]["attr1"] = """1"""
        # apply_contains node for class Listen()
        self.add_node()
        self.vs[30]["mm__"] = """apply_contains"""
        
        
        # match association Transition--src-->Vertex node
        self.add_node()
        self.vs[31]["attr1"] = """src"""
        self.vs[31]["mm__"] = """directLink_S"""
        # match association Vertex--owningStateMachine-->StateMachine node
        self.add_node()
        self.vs[32]["attr1"] = """owningStateMachine"""
        self.vs[32]["mm__"] = """directLink_S"""
        # match association StateMachine--states-->State node
        self.add_node()
        self.vs[33]["attr1"] = """states"""
        self.vs[33]["mm__"] = """directLink_S"""
        # match association Transition--triggers-->Trigger node
        self.add_node()
        self.vs[34]["attr1"] = """triggers"""
        self.vs[34]["mm__"] = """directLink_S"""
        # match association Trigger--signal-->Signal node
        self.add_node()
        self.vs[35]["attr1"] = """signal"""
        self.vs[35]["mm__"] = """directLink_S"""
        # match association State--outgoingTransitions-->Transition node
        self.add_node()
        self.vs[36]["attr1"] = """outgoingTransitions"""
        self.vs[36]["mm__"] = """directLink_S"""
        
        # apply association ListenBranch--p-->Seq node
        self.add_node()
        self.vs[37]["attr1"] = """p"""
        self.vs[37]["mm__"] = """directLink_T"""
        # apply association Seq--p-->Trigger node
        self.add_node()
        self.vs[38]["attr1"] = """p"""
        self.vs[38]["mm__"] = """directLink_T"""
        # apply association Seq--p-->Listen node
        self.add_node()
        self.vs[39]["attr1"] = """p"""
        self.vs[39]["mm__"] = """directLink_T"""
        # apply association Listen--branches-->ListenBranch node
        self.add_node()
        self.vs[40]["attr1"] = """branches"""
        self.vs[40]["mm__"] = """directLink_T"""
        # apply association ListenBranch--p-->Inst node
        self.add_node()
        self.vs[41]["attr1"] = """p"""
        self.vs[41]["mm__"] = """directLink_T"""
        # apply association Listen--branches-->ListenBranch node
        self.add_node()
        self.vs[42]["attr1"] = """branches"""
        self.vs[42]["mm__"] = """directLink_T"""
        
        # backward association Transition---->Inst node
        self.add_node()

        self.vs[43]["mm__"] = """backward_link"""
        # backward association State---->Listen node
        self.add_node()

        self.vs[44]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class Transition()
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class Vertex()
                (0,8), # matchmodel -> match_contains
                (8,7), # match_contains -> match_class StateMachine()
                (0,10), # matchmodel -> match_contains
                (10,9), # match_contains -> match_class State()
                (0,12), # matchmodel -> match_contains
                (12,11), # match_contains -> match_class Trigger()
                (0,14), # matchmodel -> match_contains
                (14,13), # match_contains -> match_class Signal()
                (0,16), # matchmodel -> match_contains
                (16,15), # match_contains -> match_class State()
                (1,18), # applymodel -> apply_contains
                (18,17), # apply_contains -> apply_class ListenBranch()
                (1,20), # applymodel -> apply_contains
                (20,19), # apply_contains -> apply_class Seq()
                (1,22), # applymodel -> apply_contains
                (22,21), # apply_contains -> apply_class Trigger()
                (1,24), # applymodel -> apply_contains
                (24,23), # apply_contains -> apply_class Listen()
                (1,26), # applymodel -> apply_contains
                (26,25), # apply_contains -> apply_class ListenBranch()
                (1,28), # applymodel -> apply_contains
                (28,27), # apply_contains -> apply_class Inst()
                (1,30), # applymodel -> apply_contains
                (30,29), # apply_contains -> apply_class Listen()
                (3,31), # match_class Transition() -> association src
                (31,5), # association src  -> match_class Vertex()
                (5,32), # match_class Vertex() -> association owningStateMachine
                (32,7), # association owningStateMachine  -> match_class StateMachine()
                (7,33), # match_class StateMachine() -> association states
                (33,9), # association states  -> match_class State()
                (3,34), # match_class Transition() -> association triggers
                (34,11), # association triggers  -> match_class Trigger()
                (11,35), # match_class Trigger() -> association signal
                (35,13), # association signal  -> match_class Signal()
                (15,36), # match_class State() -> association outgoingTransitions
                (36,3), # association outgoingTransitions  -> match_class Transition()
                (17,37), # apply_class ListenBranch() -> association p
                (37,19), # association p  -> apply_class Seq()
                (19,38), # apply_class Seq() -> association p
                (38,21), # association p  -> apply_class Trigger()
                (19,39), # apply_class Seq() -> association p
                (39,23), # association p  -> apply_class Listen()
                (23,40), # apply_class Listen() -> association branches
                (40,25), # association branches  -> apply_class ListenBranch()
                (25,41), # apply_class ListenBranch() -> association p
                (41,27), # association p  -> apply_class Inst()
                (29,42), # apply_class Listen() -> association branches
                (42,17), # association branches  -> apply_class ListenBranch()
                (27,43), # apply_class Inst() -> backward_association
                (43,3), #  backward_association -> apply_class Transition()
                (29,44), # apply_class Listen() -> backward_association
                (44,15), #  backward_association -> apply_class State()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((17,'channel'),(13,'name')), ((21,'channel'),('constant','exit_in')), ((25,'channel'),('constant','exack_in')), ((27,'__ApplyAttribute'),('constant','instfortrans')), ((29,'__ApplyAttribute'),('constant','listenhproc')), ]

        
