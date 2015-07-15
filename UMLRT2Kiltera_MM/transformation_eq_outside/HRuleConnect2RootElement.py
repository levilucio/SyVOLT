from core.himesis import Himesis
import uuid

class HRuleConnect2RootElement(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule RuleConnect2RootElement.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HRuleConnect2RootElement, self).__init__(name='HRuleConnect2RootElement', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """RuleConnect2RootElement"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'RuleConnect2RootElement')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["rulename"] = """RuleConnect2RootElement"""
        
        # match class RootElement() node
        self.add_node()
        self.vs[3]["name"] = """"""
        self.vs[3]["classtype"] = """RootElement"""
        self.vs[3]["mm__"] = """RootElement"""
        self.vs[3]["cardinality"] = """+"""
        # match_contains node for class RootElement()
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        # match class State() node
        self.add_node()
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """State"""
        self.vs[5]["mm__"] = """State"""
        self.vs[5]["cardinality"] = """+"""
        # match_contains node for class State()
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        
        
        # apply class RootElement() node
        self.add_node()
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """RootElement"""
        self.vs[7]["mm__"] = """RootElement"""
        self.vs[7]["cardinality"] = """1"""
        # apply_contains node for class RootElement()
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        # apply class ProcDef() node
        self.add_node()
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """ProcDef"""
        self.vs[9]["mm__"] = """ProcDef"""
        self.vs[9]["cardinality"] = """1"""
        # apply_contains node for class ProcDef()
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        
        
        # match association RootElement--state-->State node
        self.add_node()
        self.vs[11]["associationType"] = """state"""
        self.vs[11]["mm__"] = """directLink_S"""
        
        # apply association RootElement--procDef-->ProcDef node
        self.add_node()
        self.vs[12]["associationType"] = """procDef"""
        self.vs[12]["mm__"] = """directLink_T"""
        
        # backward association RootElement---->RootElement node
        self.add_node()
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["mm__"] = """backward_link"""
        # backward association State---->ProcDef node
        self.add_node()
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class RootElement()
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class State()
                (1,8), # applymodel -> apply_contains
                (8,7), # apply_contains -> apply_class RootElement()
                (1,10), # applymodel -> apply_contains
                (10,9), # apply_contains -> apply_class ProcDef()
                (3,11), # match_class RootElement() -> association state
                (11,5), # association state  -> match_class State()
                (7,12), # apply_class RootElement() -> association procDef
                (12,9), # association procDef  -> apply_class ProcDef()
                (7,13), # apply_class RootElement() -> backward_association
                (13,3), #  backward_association -> apply_class RootElement()
                (9,14), # apply_class ProcDef() -> backward_association
                (14,5), #  backward_association -> apply_class State()
		])
		
        # Add the equations
        self["equations"] = [((7,'__ApplyAttribute'),('constant','root')), ((9,'__ApplyAttribute'),('constant','procdef')), ]
        
