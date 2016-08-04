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
        self.vs[2]["attr1"] = """Transition2Inst"""
        
        # match class State() node
        self.add_node()
        
        self.vs[3]["mm__"] = """State""" 
        self.vs[3]["attr1"] = """+""" 
        # match class Transition() node
        self.add_node()
        
        self.vs[4]["mm__"] = """Transition""" 
        self.vs[4]["attr1"] = """+""" 
        # match class IN1() node
        self.add_node()
        
        self.vs[5]["mm__"] = """IN1""" 
        self.vs[5]["attr1"] = """1""" 
        # match class EntryPoint() node
        self.add_node()
        
        self.vs[6]["mm__"] = """EntryPoint""" 
        self.vs[6]["attr1"] = """1""" 
        # match class StateMachine() node
        self.add_node()
        
        self.vs[7]["mm__"] = """StateMachine""" 
        self.vs[7]["attr1"] = """1""" 
        
        
        # apply class Inst() node
        self.add_node()

        self.vs[8]["mm__"] = """Inst""" 
        self.vs[8]["attr1"] = """1"""
        # apply class Name() node
        self.add_node()

        self.vs[9]["mm__"] = """Name""" 
        self.vs[9]["attr1"] = """1"""
        # apply class Name() node
        self.add_node()

        self.vs[10]["mm__"] = """Name""" 
        self.vs[10]["attr1"] = """1"""
        # apply class Name() node
        self.add_node()

        self.vs[11]["mm__"] = """Name""" 
        self.vs[11]["attr1"] = """1"""
        # apply class Name() node
        self.add_node()

        self.vs[12]["mm__"] = """Name""" 
        self.vs[12]["attr1"] = """1"""
        
        
        # match association State--transitions-->Transition node
        self.add_node()
        self.vs[13]["attr1"] = """transitions"""
        self.vs[13]["mm__"] = """directLink_S"""
        # match association Transition--type-->IN1 node
        self.add_node()
        self.vs[14]["attr1"] = """type"""
        self.vs[14]["mm__"] = """directLink_S"""
        # match association Transition--dest-->EntryPoint node
        self.add_node()
        self.vs[15]["attr1"] = """dest"""
        self.vs[15]["mm__"] = """directLink_S"""
        # match association EntryPoint--owningStateMachine-->StateMachine node
        self.add_node()
        self.vs[16]["attr1"] = """owningStateMachine"""
        self.vs[16]["mm__"] = """directLink_S"""
        
        # apply association Inst--channelNames-->Name node
        self.add_node()
        self.vs[17]["attr1"] = """channelNames"""
        self.vs[17]["mm__"] = """directLink_T"""
        # apply association Inst--channelNames-->Name node
        self.add_node()
        self.vs[18]["attr1"] = """channelNames"""
        self.vs[18]["mm__"] = """directLink_T"""
        # apply association Inst--channelNames-->Name node
        self.add_node()
        self.vs[19]["attr1"] = """channelNames"""
        self.vs[19]["mm__"] = """directLink_T"""
        # apply association Inst--channelNames-->Name node
        self.add_node()
        self.vs[20]["attr1"] = """channelNames"""
        self.vs[20]["mm__"] = """directLink_T"""
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class State()
                (0,4), # matchmodel -> match_class Transition()
                (0,5), # matchmodel -> match_class IN1()
                (0,6), # matchmodel -> match_class EntryPoint()
                (0,7), # matchmodel -> match_class StateMachine()
                (1,8), # applymodel -> -> apply_class Inst()
                (1,9), # applymodel -> -> apply_class Name()
                (1,10), # applymodel -> -> apply_class Name()
                (1,11), # applymodel -> -> apply_class Name()
                (1,12), # applymodel -> -> apply_class Name()
                (3,13), # match_class State() -> association transitions
                (13,4), # association transitions  -> match_class Transition()
                (4,14), # match_class Transition() -> association type
                (14,5), # association type  -> match_class IN1()
                (4,15), # match_class Transition() -> association dest
                (15,6), # association dest  -> match_class EntryPoint()
                (6,16), # match_class EntryPoint() -> association owningStateMachine
                (16,7), # association owningStateMachine  -> match_class StateMachine()
                (8,17), # apply_class Inst() -> association channelNames
                (17,9), # association channelNames  -> apply_class Name()
                (8,18), # apply_class Inst() -> association channelNames
                (18,10), # association channelNames  -> apply_class Name()
                (8,19), # apply_class Inst() -> association channelNames
                (19,11), # association channelNames  -> apply_class Name()
                (8,20), # apply_class Inst() -> association channelNames
                (20,12), # association channelNames  -> apply_class Name()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((3,'isComposite'),('constant','true')), ((8,'name'),('concat',(('constant','S'),(7,'name')))), ((8,'__ApplyAttribute'),('constant','instForInTrans')), ((9,'literal'),('constant','exit_in')), ((10,'literal'),('constant','exack_in')), ((11,'literal'),('concat',(('constant','A'),('concat',((6,'name'),('constant','A')))))), ((12,'literal'),('constant','sh_in')), ]

        
