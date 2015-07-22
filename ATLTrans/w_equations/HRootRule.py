from core.himesis import Himesis
import uuid

class HRootRule(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule RootRule.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HRootRule, self).__init__(name='HRootRule', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """RootRule"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'RootRule')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["rulename"] = """RootRule"""
        
        # match class HouseholdRoot() node
        self.add_node()
        self.vs[3]["name"] = """"""
        self.vs[3]["classtype"] = """HouseholdRoot"""
        self.vs[3]["mm__"] = """HouseholdRoot"""
        self.vs[3]["cardinality"] = """+"""
        # match_contains node for class HouseholdRoot()
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        
        
        # apply class CommunityRoot() node
        self.add_node()
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """CommunityRoot"""
        self.vs[5]["mm__"] = """CommunityRoot"""
        self.vs[5]["cardinality"] = """1"""
        # apply_contains node for class CommunityRoot()
        self.add_node()
        self.vs[6]["mm__"] = """apply_contains"""
        
        
        
        
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class HouseholdRoot()
                (1,6), # applymodel -> apply_contains
                (6,5), # apply_contains -> apply_class CommunityRoot()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])
		
        # Add the equations
        self["equations"] = [((5,'ApplyAttribute'),('constant','root')), ]

        
