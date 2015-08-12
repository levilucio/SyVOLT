from core.himesis import Himesis
import uuid

class HUnionDaughterRule(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule UnionDaughterRule.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HUnionDaughterRule, self).__init__(name='HUnionDaughterRule', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """UnionDaughterRule"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'UnionDaughterRule')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
 
        
        # match class HouseholdRoot() node
        self.add_node()

        self.vs[3]["mm__"] = """HouseholdRoot""" 
        self.vs[3]["attr1"] = """+""" 
        # match_contains node for class HouseholdRoot()
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        # match class Member() node
        self.add_node()

        self.vs[5]["mm__"] = """Member""" 
        self.vs[5]["attr1"] = """+""" 
        # match_contains node for class Member()
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        # match class Family() node
        self.add_node()

        self.vs[7]["mm__"] = """Family""" 
        self.vs[7]["attr1"] = """+""" 
        # match_contains node for class Family()
        self.add_node()
        self.vs[8]["mm__"] = """match_contains"""
        
        
        # apply class CommunityRoot() node
        self.add_node()

        self.vs[9]["mm__"] = """CommunityRoot""" 
        self.vs[9]["attr1"] = """1"""
        # apply_contains node for class CommunityRoot()
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        # apply class Woman() node
        self.add_node()

        self.vs[11]["mm__"] = """Woman""" 
        self.vs[11]["attr1"] = """1"""
        # apply_contains node for class Woman()
        self.add_node()
        self.vs[12]["mm__"] = """apply_contains"""
        
        
        # match association HouseholdRoot--have-->Family node
        self.add_node()
        self.vs[13]["attr1"] = """have"""
        self.vs[13]["mm__"] = """directLink_S"""
        # match association Family--daughter-->Member node
        self.add_node()
        self.vs[14]["attr1"] = """daughter"""
        self.vs[14]["mm__"] = """directLink_S"""
        
        # apply association CommunityRoot--has-->Woman node
        self.add_node()
        self.vs[15]["attr1"] = """has"""
        self.vs[15]["mm__"] = """directLink_T"""
        
        # backward association HouseholdRoot---->CommunityRoot node
        self.add_node()

        self.vs[16]["mm__"] = """backward_link"""
        # backward association Family---->Woman node
        self.add_node()

        self.vs[17]["mm__"] = """backward_link"""
        # backward association Member---->Woman node
        self.add_node()

        self.vs[18]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class HouseholdRoot()
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class Member()
                (0,8), # matchmodel -> match_contains
                (8,7), # match_contains -> match_class Family()
                (1,10), # applymodel -> apply_contains
                (10,9), # apply_contains -> apply_class CommunityRoot()
                (1,12), # applymodel -> apply_contains
                (12,11), # apply_contains -> apply_class Woman()
                (3,13), # match_class HouseholdRoot() -> association have
                (13,7), # association have  -> match_class Family()
                (7,14), # match_class Family() -> association daughter
                (14,5), # association daughter  -> match_class Member()
                (9,15), # apply_class CommunityRoot() -> association has
                (15,11), # association has  -> apply_class Woman()
                (9,16), # apply_class CommunityRoot() -> backward_association
                (16,3), #  backward_association -> apply_class HouseholdRoot()
                (11,17), # apply_class Woman() -> backward_association
                (17,7), #  backward_association -> apply_class Family()
                (11,18), # apply_class Woman() -> backward_association
                (18,5), #  backward_association -> apply_class Member()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((9,'ApplyAttribute'),('constant','root')), ((11,'ApplyAttribute'),('constant','famMemberDaughter')), ]

        
