from core.himesis import Himesis
import uuid

class HState2CProcDef(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule State2CProcDef.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HState2CProcDef, self).__init__(name='HState2CProcDef', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """State2CProcDef"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'State2CProcDef')
        
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
        self.vs[5]["attr1"] = """1""" 
        # match_contains node for class Transition()
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        # match class EntryPoint() node
        self.add_node()

        self.vs[7]["mm__"] = """EntryPoint""" 
        self.vs[7]["attr1"] = """1""" 
        # match_contains node for class EntryPoint()
        self.add_node()
        self.vs[8]["mm__"] = """match_contains"""
        # match class StateMachine() node
        self.add_node()

        self.vs[9]["mm__"] = """StateMachine""" 
        self.vs[9]["attr1"] = """1""" 
        # match_contains node for class StateMachine()
        self.add_node()
        self.vs[10]["mm__"] = """match_contains"""
        
        
        # apply class LocalDef() node
        self.add_node()

        self.vs[11]["mm__"] = """LocalDef""" 
        self.vs[11]["attr1"] = """1"""
        # apply_contains node for class LocalDef()
        self.add_node()
        self.vs[12]["mm__"] = """apply_contains"""
        # apply class ProcDef() node
        self.add_node()

        self.vs[13]["mm__"] = """ProcDef""" 
        self.vs[13]["attr1"] = """1"""
        # apply_contains node for class ProcDef()
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
        # apply class ConditionSet() node
        self.add_node()

        self.vs[23]["mm__"] = """ConditionSet""" 
        self.vs[23]["attr1"] = """1"""
        # apply_contains node for class ConditionSet()
        self.add_node()
        self.vs[24]["mm__"] = """apply_contains"""
        # apply class Inst() node
        self.add_node()

        self.vs[25]["mm__"] = """Inst""" 
        self.vs[25]["attr1"] = """1"""
        # apply_contains node for class Inst()
        self.add_node()
        self.vs[26]["mm__"] = """apply_contains"""
        # apply class Name() node
        self.add_node()

        self.vs[27]["mm__"] = """Name""" 
        self.vs[27]["attr1"] = """1"""
        # apply_contains node for class Name()
        self.add_node()
        self.vs[28]["mm__"] = """apply_contains"""
        # apply class Name() node
        self.add_node()

        self.vs[29]["mm__"] = """Name""" 
        self.vs[29]["attr1"] = """1"""
        # apply_contains node for class Name()
        self.add_node()
        self.vs[30]["mm__"] = """apply_contains"""
        # apply class Name() node
        self.add_node()

        self.vs[31]["mm__"] = """Name""" 
        self.vs[31]["attr1"] = """1"""
        # apply_contains node for class Name()
        self.add_node()
        self.vs[32]["mm__"] = """apply_contains"""
        # apply class Name() node
        self.add_node()

        self.vs[33]["mm__"] = """Name""" 
        self.vs[33]["attr1"] = """1"""
        # apply_contains node for class Name()
        self.add_node()
        self.vs[34]["mm__"] = """apply_contains"""
        
        
        # match association State--initialTransition-->Transition node
        self.add_node()
        self.vs[35]["attr1"] = """initialTransition"""
        self.vs[35]["mm__"] = """directLink_S"""
        # match association Transition--dest-->EntryPoint node
        self.add_node()
        self.vs[36]["attr1"] = """dest"""
        self.vs[36]["mm__"] = """directLink_S"""
        # match association EntryPoint--owningStateMachine-->StateMachine node
        self.add_node()
        self.vs[37]["attr1"] = """owningStateMachine"""
        self.vs[37]["mm__"] = """directLink_S"""
        
        # apply association LocalDef--def-->ProcDef node
        self.add_node()
        self.vs[38]["attr1"] = """def"""
        self.vs[38]["mm__"] = """directLink_T"""
        # apply association ProcDef--channelNames-->Name node
        self.add_node()
        self.vs[39]["attr1"] = """channelNames"""
        self.vs[39]["mm__"] = """directLink_T"""
        # apply association ProcDef--channelNames-->Name node
        self.add_node()
        self.vs[40]["attr1"] = """channelNames"""
        self.vs[40]["mm__"] = """directLink_T"""
        # apply association ProcDef--channelNames-->Name node
        self.add_node()
        self.vs[41]["attr1"] = """channelNames"""
        self.vs[41]["mm__"] = """directLink_T"""
        # apply association ProcDef--channelNames-->Name node
        self.add_node()
        self.vs[42]["attr1"] = """channelNames"""
        self.vs[42]["mm__"] = """directLink_T"""
        # apply association ProcDef--p-->ConditionSet node
        self.add_node()
        self.vs[43]["attr1"] = """p"""
        self.vs[43]["mm__"] = """directLink_T"""
        # apply association ConditionSet--alternative-->Inst node
        self.add_node()
        self.vs[44]["attr1"] = """alternative"""
        self.vs[44]["mm__"] = """directLink_T"""
        # apply association Inst--channelNames-->Name node
        self.add_node()
        self.vs[45]["attr1"] = """channelNames"""
        self.vs[45]["mm__"] = """directLink_T"""
        # apply association Inst--channelNames-->Name node
        self.add_node()
        self.vs[46]["attr1"] = """channelNames"""
        self.vs[46]["mm__"] = """directLink_T"""
        # apply association Inst--channelNames-->Name node
        self.add_node()
        self.vs[47]["attr1"] = """channelNames"""
        self.vs[47]["mm__"] = """directLink_T"""
        # apply association Inst--channelNames-->Name node
        self.add_node()
        self.vs[48]["attr1"] = """channelNames"""
        self.vs[48]["mm__"] = """directLink_T"""
        
        # backward association State---->LocalDef node
        self.add_node()

        self.vs[49]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class State()
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class Transition()
                (0,8), # matchmodel -> match_contains
                (8,7), # match_contains -> match_class EntryPoint()
                (0,10), # matchmodel -> match_contains
                (10,9), # match_contains -> match_class StateMachine()
                (1,12), # applymodel -> apply_contains
                (12,11), # apply_contains -> apply_class LocalDef()
                (1,14), # applymodel -> apply_contains
                (14,13), # apply_contains -> apply_class ProcDef()
                (1,16), # applymodel -> apply_contains
                (16,15), # apply_contains -> apply_class Name()
                (1,18), # applymodel -> apply_contains
                (18,17), # apply_contains -> apply_class Name()
                (1,20), # applymodel -> apply_contains
                (20,19), # apply_contains -> apply_class Name()
                (1,22), # applymodel -> apply_contains
                (22,21), # apply_contains -> apply_class Name()
                (1,24), # applymodel -> apply_contains
                (24,23), # apply_contains -> apply_class ConditionSet()
                (1,26), # applymodel -> apply_contains
                (26,25), # apply_contains -> apply_class Inst()
                (1,28), # applymodel -> apply_contains
                (28,27), # apply_contains -> apply_class Name()
                (1,30), # applymodel -> apply_contains
                (30,29), # apply_contains -> apply_class Name()
                (1,32), # applymodel -> apply_contains
                (32,31), # apply_contains -> apply_class Name()
                (1,34), # applymodel -> apply_contains
                (34,33), # apply_contains -> apply_class Name()
                (3,35), # match_class State() -> association initialTransition
                (35,5), # association initialTransition  -> match_class Transition()
                (5,36), # match_class Transition() -> association dest
                (36,7), # association dest  -> match_class EntryPoint()
                (7,37), # match_class EntryPoint() -> association owningStateMachine
                (37,9), # association owningStateMachine  -> match_class StateMachine()
                (11,38), # apply_class LocalDef() -> association def
                (38,13), # association def  -> apply_class ProcDef()
                (13,39), # apply_class ProcDef() -> association channelNames
                (39,15), # association channelNames  -> apply_class Name()
                (13,40), # apply_class ProcDef() -> association channelNames
                (40,17), # association channelNames  -> apply_class Name()
                (13,41), # apply_class ProcDef() -> association channelNames
                (41,19), # association channelNames  -> apply_class Name()
                (13,42), # apply_class ProcDef() -> association channelNames
                (42,21), # association channelNames  -> apply_class Name()
                (13,43), # apply_class ProcDef() -> association p
                (43,23), # association p  -> apply_class ConditionSet()
                (23,44), # apply_class ConditionSet() -> association alternative
                (44,25), # association alternative  -> apply_class Inst()
                (25,45), # apply_class Inst() -> association channelNames
                (45,27), # association channelNames  -> apply_class Name()
                (25,46), # apply_class Inst() -> association channelNames
                (46,29), # association channelNames  -> apply_class Name()
                (25,47), # apply_class Inst() -> association channelNames
                (47,31), # association channelNames  -> apply_class Name()
                (25,48), # apply_class Inst() -> association channelNames
                (48,33), # association channelNames  -> apply_class Name()
                (11,49), # apply_class LocalDef() -> backward_association
                (49,3), #  backward_association -> apply_class State()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((3,'isComposite'),('constant','true')), ((11,'__ApplyAttribute'),('constant','localdefcompstate')), ((13,'name'),('constant','C')), ((15,'literal'),('constant','exit')), ((17,'literal'),('constant','exack')), ((19,'literal'),('constant','enp')), ((21,'literal'),('constant','sh')), ((23,'__ApplyAttribute'),('constant','condsetcompstate')), ((25,'name'),('concat',(('constant','S'),(9,'name')))), ((27,'literal'),('constant','exit_in')), ((29,'literal'),('constant','exack_in')), ((31,'literal'),('concat',(('constant','A'),('concat',((7,'name'),('constant','A')))))), ((33,'literal'),('constant','sh_in')), ]

        
