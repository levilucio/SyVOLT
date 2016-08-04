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
        self.vs[2]["attr1"] = """RuleConnect2RootElement"""
        
        # match class RootElement() node
        self.add_node()
        
        self.vs[3]["mm__"] = """RootElement""" 
        self.vs[3]["attr1"] = """+""" 
        # match class TopLevelElement() node
        self.add_node()
        
        self.vs[4]["mm__"] = """TopLevelElement""" 
        self.vs[4]["attr1"] = """+""" 
        
        
        # apply class RootElement() node
        self.add_node()

        self.vs[5]["mm__"] = """RootElement""" 
        self.vs[5]["attr1"] = """1"""
        # apply class TopLevelElement() node
        self.add_node()

        self.vs[6]["mm__"] = """TopLevelElement""" 
        self.vs[6]["attr1"] = """1"""
        
        
        # match association RootElement--contains-->TopLevelElement node
        self.add_node()
        self.vs[7]["attr1"] = """contains"""
        self.vs[7]["mm__"] = """directLink_S"""
        
        # apply association RootElement--contains-->TopLevelElement node
        self.add_node()
        self.vs[8]["attr1"] = """contains"""
        self.vs[8]["mm__"] = """directLink_T"""
        
        # backward association RootElement---->RootElement node
        self.add_node()

        self.vs[9]["mm__"] = """backward_link"""
        # backward association TopLevelElement---->TopLevelElement node
        self.add_node()

        self.vs[10]["mm__"] = """backward_link"""
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class RootElement()
                (0,4), # matchmodel -> match_class TopLevelElement()
                (1,5), # applymodel -> -> apply_class RootElement()
                (1,6), # applymodel -> -> apply_class TopLevelElement()
                (3,7), # match_class RootElement() -> association contains
                (7,4), # association contains  -> match_class TopLevelElement()
                (5,8), # apply_class RootElement() -> association contains
                (8,6), # association contains  -> apply_class TopLevelElement()
                (5,9), # apply_class RootElement() -> backward_association
                (9,3), #  backward_association -> apply_class RootElement()
                (6,10), # apply_class TopLevelElement() -> backward_association
                (10,4), #  backward_association -> apply_class TopLevelElement()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = []

        
