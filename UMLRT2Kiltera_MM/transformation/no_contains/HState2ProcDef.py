from core.himesis import Himesis
import uuid

class HState2ProcDef(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule State2ProcDef.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HState2ProcDef, self).__init__(name='HState2ProcDef', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """State2ProcDef"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'State2ProcDef')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["attr1"] = """State2ProcDef"""
        
        # match class State() node
        self.add_node()
        
        self.vs[3]["mm__"] = """State""" 
        self.vs[3]["attr1"] = """+""" 
        
        
        # apply class ProcDef() node
        self.add_node()

        self.vs[4]["mm__"] = """ProcDef""" 
        self.vs[4]["attr1"] = """1"""
        # apply class Name() node
        self.add_node()

        self.vs[5]["mm__"] = """Name""" 
        self.vs[5]["attr1"] = """1"""
        
        
        
        # apply association ProcDef--channelNames-->Name node
        self.add_node()
        self.vs[6]["attr1"] = """channelNames"""
        self.vs[6]["mm__"] = """directLink_T"""
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class State()
                (1,4), # applymodel -> -> apply_class ProcDef()
                (1,5), # applymodel -> -> apply_class Name()
                (4,6), # apply_class ProcDef() -> association channelNames
                (6,5), # association channelNames  -> apply_class Name()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((4,'name'),('concat',(('constant','S'),(3,'name')))), ((5,'literal'),('constant','exack')), ]

        
