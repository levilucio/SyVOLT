from core.himesis import Himesis
import uuid

class HState2ProcDefcopy(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule State2ProcDef.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HState2ProcDefcopy, self).__init__(name='HState2ProcDefcopy', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """State2ProcDefcopy"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'State2ProcDefcopy')
        
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
        
        
        # apply class ProcDef() node
        self.add_node()

        self.vs[5]["mm__"] = """ProcDef""" 
        self.vs[5]["attr1"] = """1"""
        # apply_contains node for class ProcDef()
        self.add_node()
        self.vs[6]["mm__"] = """apply_contains"""
        # apply class Name() node
        self.add_node()

        self.vs[7]["mm__"] = """Name""" 
        self.vs[7]["attr1"] = """1"""
        # apply_contains node for class Name()
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        # apply class Name() node
        self.add_node()

        self.vs[9]["mm__"] = """Name""" 
        self.vs[9]["attr1"] = """1"""
        # apply_contains node for class Name()
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        # apply class Name() node
        self.add_node()

        self.vs[11]["mm__"] = """Name""" 
        self.vs[11]["attr1"] = """1"""
        # apply_contains node for class Name()
        self.add_node()
        self.vs[12]["mm__"] = """apply_contains"""
        
        
        
        # apply association ProcDef--channelNames-->Name node
        self.add_node()
        self.vs[13]["attr1"] = """channelNames"""
        self.vs[13]["mm__"] = """directLink_T"""
        # apply association ProcDef--channelNames-->Name node
        self.add_node()
        self.vs[14]["attr1"] = """channelNames"""
        self.vs[14]["mm__"] = """directLink_T"""
        # apply association ProcDef--channelNames-->Name node
        self.add_node()
        self.vs[15]["attr1"] = """channelNames"""
        self.vs[15]["mm__"] = """directLink_T"""
        
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class State()
                (1,6), # applymodel -> apply_contains
                (6,5), # apply_contains -> apply_class ProcDef()
                (1,8), # applymodel -> apply_contains
                (8,7), # apply_contains -> apply_class Name()
                (1,10), # applymodel -> apply_contains
                (10,9), # apply_contains -> apply_class Name()
                (1,12), # applymodel -> apply_contains
                (12,11), # apply_contains -> apply_class Name()
                (5,13), # apply_class ProcDef() -> association channelNames
                (13,7), # association channelNames  -> apply_class Name()
                (5,14), # apply_class ProcDef() -> association channelNames
                (14,9), # association channelNames  -> apply_class Name()
                (5,15), # apply_class ProcDef() -> association channelNames
                (15,11), # association channelNames  -> apply_class Name()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((5,'name'),('concat',(('constant','S'),(3,'name')))), ((5,'ApplyAttribute'),('constant','solveRef')), ((7,'literal'),('constant','enp')), ((9,'literal'),('constant','exit')), ((11,'literal'),('constant','exack')), ]

        
