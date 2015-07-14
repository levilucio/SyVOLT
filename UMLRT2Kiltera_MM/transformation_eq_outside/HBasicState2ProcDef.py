from core.himesis import Himesis
import uuid

class HBasicState2ProcDef(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule BasicState2ProcDef.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HBasicState2ProcDef, self).__init__(name='HBasicState2ProcDef', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """BasicState2ProcDef"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'BasicState2ProcDef')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["rulename"] = """BasicState2ProcDef"""
        
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
        # apply class Listen() node
        self.add_node()
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """Listen"""
        self.vs[7]["mm__"] = """Listen"""
        self.vs[7]["cardinality"] = """1"""
        # apply_contains node for class Listen()
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        # apply class ListenBranch() node
        self.add_node()
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """ListenBranch"""
        self.vs[9]["mm__"] = """ListenBranch"""
        self.vs[9]["cardinality"] = """1"""
        # apply_contains node for class ListenBranch()
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        # apply class Trigger() node
        self.add_node()
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """Trigger"""
        self.vs[11]["mm__"] = """Trigger"""
        self.vs[11]["cardinality"] = """1"""
        # apply_contains node for class Trigger()
        self.add_node()
        self.vs[12]["mm__"] = """apply_contains"""
        
        
        
        # apply association ProcDef--p-->Listen node
        self.add_node()
        self.vs[13]["associationType"] = """p"""
        self.vs[13]["mm__"] = """directLink_T"""
        # apply association Listen--branches-->ListenBranch node
        self.add_node()
        self.vs[14]["associationType"] = """branches"""
        self.vs[14]["mm__"] = """directLink_T"""
        # apply association ListenBranch--p-->Trigger node
        self.add_node()
        self.vs[15]["associationType"] = """p"""
        self.vs[15]["mm__"] = """directLink_T"""
        
        # backward association State---->ProcDef node
        self.add_node()
        self.vs[16]["type"] = """ruleDef"""
        self.vs[16]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class State()
                (1,6), # applymodel -> apply_contains
                (6,5), # apply_contains -> apply_class ProcDef()
                (1,8), # applymodel -> apply_contains
                (8,7), # apply_contains -> apply_class Listen()
                (1,10), # applymodel -> apply_contains
                (10,9), # apply_contains -> apply_class ListenBranch()
                (1,12), # applymodel -> apply_contains
                (12,11), # apply_contains -> apply_class Trigger()
                (5,13), # apply_class ProcDef() -> association p
                (13,7), # association p  -> apply_class Listen()
                (7,14), # apply_class Listen() -> association branches
                (14,9), # association branches  -> apply_class ListenBranch()
                (9,15), # apply_class ListenBranch() -> association p
                (15,11), # association p  -> apply_class Trigger()
                (5,16), # apply_class ProcDef() -> backward_association
                (16,3), #  backward_association -> apply_class State()
		])
		
        # Add the equations
        self.equations = [((3,'isComposite'),('constant','false')), ((3,'hasOutgoingTransitions'),('constant','true')), ((5,'__ApplyAttribute'),('constant','procdef')), ((7,'__ApplyAttribute'),('constant','listensimplestate')), ((9,'channel'),('constant','exit')), ((11,'channel'),('constant','exack')), ]
        
