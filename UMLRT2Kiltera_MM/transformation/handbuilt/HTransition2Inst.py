from core.himesis import Himesis
import uuid

class HTransition2Inst(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule Transition2Inst.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HTransition2Inst, self).__init__(name='HTransition2Inst', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """Transition2Inst"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Transition2Inst')
        
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
        # match class IN1() node
        self.add_node()

        self.vs[7]["mm__"] = """IN1""" 
        self.vs[7]["attr1"] = """1""" 
        # match_contains node for class IN1()
        self.add_node()
        self.vs[8]["mm__"] = """match_contains"""
        # match class EntryPoint() node
        self.add_node()

        self.vs[9]["mm__"] = """EntryPoint""" 
        self.vs[9]["attr1"] = """1""" 
        # match_contains node for class EntryPoint()
        self.add_node()
        self.vs[10]["mm__"] = """match_contains"""
        # match class StateMachine() node
        self.add_node()

        self.vs[11]["mm__"] = """StateMachine""" 
        self.vs[11]["attr1"] = """1""" 
        # match_contains node for class StateMachine()
        self.add_node()
        self.vs[12]["mm__"] = """match_contains"""
        
        
        # apply class Inst() node
        self.add_node()

        self.vs[13]["mm__"] = """Inst""" 
        self.vs[13]["attr1"] = """1"""
        # apply_contains node for class Inst()
        self.add_node()
        self.vs[14]["mm__"] = """apply_contains"""
        # apply class Name() node
        self.add_node()

        self.vs[15]["mm__"] = """Name""" 
        self.vs[15]["attr1"] = """1"""
        # apply_contains node for class Name()
        self.add_node()
        self.vs[16]["mm__"] = """apply_contains"""
        # apply class Name() node
        self.add_node()

        self.vs[17]["mm__"] = """Name""" 
        self.vs[17]["attr1"] = """1"""
        # apply_contains node for class Name()
        self.add_node()
        self.vs[18]["mm__"] = """apply_contains"""
        # apply class Name() node
        self.add_node()

        self.vs[19]["mm__"] = """Name""" 
        self.vs[19]["attr1"] = """1"""
        # apply_contains node for class Name()
        self.add_node()
        self.vs[20]["mm__"] = """apply_contains"""
        # apply class Name() node
        self.add_node()

        self.vs[21]["mm__"] = """Name""" 
        self.vs[21]["attr1"] = """1"""
        # apply_contains node for class Name()
        self.add_node()
        self.vs[22]["mm__"] = """apply_contains"""
        
        
        # match association State--transitions-->Transition node
        self.add_node()
        self.vs[23]["attr1"] = """transitions"""
        self.vs[23]["mm__"] = """directLink_S"""
        # match association Transition--type-->IN1 node
        self.add_node()
        self.vs[24]["attr1"] = """type"""
        self.vs[24]["mm__"] = """directLink_S"""
        # match association Transition--dest-->EntryPoint node
        self.add_node()
        self.vs[25]["attr1"] = """dest"""
        self.vs[25]["mm__"] = """directLink_S"""
        # match association EntryPoint--owningStateMachine-->StateMachine node
        self.add_node()
        self.vs[26]["attr1"] = """owningStateMachine"""
        self.vs[26]["mm__"] = """directLink_S"""
        
        # apply association Inst--channelNames-->Name node
        self.add_node()
        self.vs[27]["attr1"] = """channelNames"""
        self.vs[27]["mm__"] = """directLink_T"""
        # apply association Inst--channelNames-->Name node
        self.add_node()
        self.vs[28]["attr1"] = """channelNames"""
        self.vs[28]["mm__"] = """directLink_T"""
        # apply association Inst--channelNames-->Name node
        self.add_node()
        self.vs[29]["attr1"] = """channelNames"""
        self.vs[29]["mm__"] = """directLink_T"""
        # apply association Inst--channelNames-->Name node
        self.add_node()
        self.vs[30]["attr1"] = """channelNames"""
        self.vs[30]["mm__"] = """directLink_T"""
        
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class State()
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class Transition()
                (0,8), # matchmodel -> match_contains
                (8,7), # match_contains -> match_class IN1()
                (0,10), # matchmodel -> match_contains
                (10,9), # match_contains -> match_class EntryPoint()
                (0,12), # matchmodel -> match_contains
                (12,11), # match_contains -> match_class StateMachine()
                (1,14), # applymodel -> apply_contains
                (14,13), # apply_contains -> apply_class Inst()
                (1,16), # applymodel -> apply_contains
                (16,15), # apply_contains -> apply_class Name()
                (1,18), # applymodel -> apply_contains
                (18,17), # apply_contains -> apply_class Name()
                (1,20), # applymodel -> apply_contains
                (20,19), # apply_contains -> apply_class Name()
                (1,22), # applymodel -> apply_contains
                (22,21), # apply_contains -> apply_class Name()
                (3,23), # match_class State() -> association transitions
                (23,5), # association transitions  -> match_class Transition()
                (5,24), # match_class Transition() -> association type
                (24,7), # association type  -> match_class IN1()
                (5,25), # match_class Transition() -> association dest
                (25,9), # association dest  -> match_class EntryPoint()
                (9,26), # match_class EntryPoint() -> association owningStateMachine
                (26,11), # association owningStateMachine  -> match_class StateMachine()
                (13,27), # apply_class Inst() -> association channelNames
                (27,15), # association channelNames  -> apply_class Name()
                (13,28), # apply_class Inst() -> association channelNames
                (28,17), # association channelNames  -> apply_class Name()
                (13,29), # apply_class Inst() -> association channelNames
                (29,19), # association channelNames  -> apply_class Name()
                (13,30), # apply_class Inst() -> association channelNames
                (30,21), # association channelNames  -> apply_class Name()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((3,'isComposite'),('constant','true')), ((13,'name'),('concat',(('constant','S'),(11,'name')))), ((13,'__ApplyAttribute'),('constant','instForInTrans')), ((15,'literal'),('constant','exit_in')), ((17,'literal'),('constant','exack_in')), ((19,'literal'),('concat',(('constant','A'),('concat',((9,'name'),('constant','A')))))), ((21,'literal'),('constant','sh_in')), ]

        
