from core.himesis import Himesis
import uuid

class HBasicStateNoOutgoing2ProcDef(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule BasicStateNoOutgoing2ProcDef.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HBasicStateNoOutgoing2ProcDef, self).__init__(name='HBasicStateNoOutgoing2ProcDef', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """BasicStateNoOutgoing2ProcDef"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'BasicStateNoOutgoing2ProcDef')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["rulename"] = """BasicStateNoOutgoing2ProcDef"""
        
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
        # apply class Null() node
        self.add_node()
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """Null"""
        self.vs[7]["mm__"] = """Null"""
        self.vs[7]["cardinality"] = """1"""
        # apply_contains node for class Null()
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        
        
        
        # apply association ProcDef--p-->Null node
        self.add_node()
        self.vs[9]["associationType"] = """p"""
        self.vs[9]["mm__"] = """directLink_T"""
        
        # backward association State---->ProcDef node
        self.add_node()
        self.vs[10]["type"] = """ruleDef"""
        self.vs[10]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class State()
                (1,6), # applymodel -> apply_contains
                (6,5), # apply_contains -> apply_class ProcDef()
                (1,8), # applymodel -> apply_contains
                (8,7), # apply_contains -> apply_class Null()
                (5,9), # apply_class ProcDef() -> association p
                (9,7), # association p  -> apply_class Null()
                (5,10), # apply_class ProcDef() -> backward_association
                (10,3), #  backward_association -> apply_class State()
		])
		
        # Add the equations
        self["equations"] = [((3,'isComposite'),('constant','false')), ((3,'hasOutgoingTransitions'),('constant','false')), ((5,'__ApplyAttribute'),('constant','procdef')), ]
        
