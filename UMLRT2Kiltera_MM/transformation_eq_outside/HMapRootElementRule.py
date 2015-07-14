from core.himesis import Himesis
import uuid

class HMapRootElementRule(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule MapRootElementRule.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HMapRootElementRule, self).__init__(name='HMapRootElementRule', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """MapRootElementRule"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'MapRootElementRule')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["rulename"] = """MapRootElementRule"""
        
        # match class RootElement() node
        self.add_node()
        self.vs[3]["name"] = """"""
        self.vs[3]["classtype"] = """RootElement"""
        self.vs[3]["mm__"] = """RootElement"""
        self.vs[3]["cardinality"] = """+"""
        # match_contains node for class RootElement()
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        
        
        # apply class RootElement() node
        self.add_node()
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """RootElement"""
        self.vs[5]["mm__"] = """RootElement"""
        self.vs[5]["cardinality"] = """1"""
        # apply_contains node for class RootElement()
        self.add_node()
        self.vs[6]["mm__"] = """apply_contains"""
        
        
        
        
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class RootElement()
                (1,6), # applymodel -> apply_contains
                (6,5), # apply_contains -> apply_class RootElement()
		])
		
        # Add the equations
        self.equations = [((5,'__ApplyAttribute'),('constant','root')), ]
        
