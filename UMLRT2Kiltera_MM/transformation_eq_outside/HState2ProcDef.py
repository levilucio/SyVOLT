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
        self.vs[2]["rulename"] = """State2ProcDef"""
        
        # match class State() node
        self.add_node()
        self.vs[3]["name"] = """"""
        self.vs[3]["classtype"] = """State"""
        self.vs[3]["mm__"] = """State"""
        self.vs[3]["cardinality"] = """+"""
        # match_contains node for class State()
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        
        
        # apply class ProcDef() node
        self.add_node()
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """ProcDef"""
        self.vs[5]["mm__"] = """ProcDef"""
        self.vs[5]["cardinality"] = """1"""
        # apply_contains node for class ProcDef()
        self.add_node()
        self.vs[6]["mm__"] = """apply_contains"""
        # apply class Name() node
        self.add_node()
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """Name"""
        self.vs[7]["mm__"] = """Name"""
        self.vs[7]["cardinality"] = """1"""
        # apply_contains node for class Name()
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        # apply class Name() node
        self.add_node()
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """Name"""
        self.vs[9]["mm__"] = """Name"""
        self.vs[9]["cardinality"] = """1"""
        # apply_contains node for class Name()
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        # apply class Name() node
        self.add_node()
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """Name"""
        self.vs[11]["mm__"] = """Name"""
        self.vs[11]["cardinality"] = """1"""
        # apply_contains node for class Name()
        self.add_node()
        self.vs[12]["mm__"] = """apply_contains"""
        
        
        
        # apply association ProcDef--channelNames-->Name node
        self.add_node()
        self.vs[13]["associationType"] = """channelNames"""
        self.vs[13]["mm__"] = """directLink_T"""
        # apply association ProcDef--channelNames-->Name node
        self.add_node()
        self.vs[14]["associationType"] = """channelNames"""
        self.vs[14]["mm__"] = """directLink_T"""
        # apply association ProcDef--channelNames-->Name node
        self.add_node()
        self.vs[15]["associationType"] = """channelNames"""
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
		])
		
        # Add the equations
        self["equations"] = [((5,'name'),('concat',(('constant','S'),(3,'name')))), ((5,'__ApplyAttribute'),('constant','procdef')), ((7,'literal'),('constant','exit')), ((9,'literal'),('constant','exack')), ((11,'literal'),('constant','enp')), ]
        
