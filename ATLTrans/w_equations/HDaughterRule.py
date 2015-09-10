from core.himesis import Himesis
import uuid

class HDaughterRule(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule DaughterRule.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HDaughterRule, self).__init__(name='HDaughterRule', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """DaughterRule"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'DaughterRule')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
 
        
        # match class Family() node
        self.add_node()

        self.vs[3]["mm__"] = """Family""" 
        self.vs[3]["attr1"] = """+""" 
        # match_contains node for class Family()
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        # match class Member() node
        self.add_node()

        self.vs[5]["mm__"] = """Member""" 
        self.vs[5]["attr1"] = """+""" 
        # match_contains node for class Member()
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        
        
        # apply class Woman() node
        self.add_node()

        self.vs[7]["mm__"] = """Woman""" 
        self.vs[7]["attr1"] = """1"""
        # apply_contains node for class Woman()
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        
        
        # match association Family--daughter-->Member node
        self.add_node()
        self.vs[9]["attr1"] = """daughter"""
        self.vs[9]["mm__"] = """directLink_S"""
        
        
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class Family()
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class Member()
                (1,8), # applymodel -> apply_contains
                (8,7), # apply_contains -> apply_class Woman()
                (3,9), # match_class Family() -> association daughter
                (9,5), # association daughter  -> match_class Member()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((7,'ApplyAttribute'),('constant','famMemberDaughter')), ((7,'name'),('concat',((5,'name'),(3,'name')))), ]

        
