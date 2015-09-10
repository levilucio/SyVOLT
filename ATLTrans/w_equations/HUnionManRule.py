from core.himesis import Himesis
import uuid

class HUnionManRule(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule UnionManRule.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HUnionManRule, self).__init__(name='HUnionManRule', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """UnionManRule"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'UnionManRule')
        
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
        # match class HouseholdRoot() node
        self.add_node()

        self.vs[7]["mm__"] = """HouseholdRoot""" 
        self.vs[7]["attr1"] = """+""" 
        # match_contains node for class HouseholdRoot()
        self.add_node()
        self.vs[8]["mm__"] = """match_contains"""
        
        
        # apply class Man() node
        self.add_node()

        self.vs[9]["mm__"] = """Man""" 
        self.vs[9]["attr1"] = """1"""
        # apply_contains node for class Man()
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        # apply class CommunityRoot() node
        self.add_node()

        self.vs[11]["mm__"] = """CommunityRoot""" 
        self.vs[11]["attr1"] = """1"""
        # apply_contains node for class CommunityRoot()
        self.add_node()
        self.vs[12]["mm__"] = """apply_contains"""
        
        
        # match association Family--father-->Member node
        self.add_node()
        self.vs[13]["attr1"] = """father"""
        self.vs[13]["mm__"] = """directLink_S"""
        # match association HouseholdRoot--have-->Family node
        self.add_node()
        self.vs[14]["attr1"] = """have"""
        self.vs[14]["mm__"] = """directLink_S"""
        
        # apply association CommunityRoot--has-->Man node
        self.add_node()
        self.vs[15]["attr1"] = """has"""
        self.vs[15]["mm__"] = """directLink_T"""
        
        # backward association Member---->Man node
        self.add_node()

        self.vs[16]["mm__"] = """backward_link"""
        # backward association HouseholdRoot---->CommunityRoot node
        self.add_node()

        self.vs[17]["mm__"] = """backward_link"""
        # backward association Family---->Man node
        self.add_node()

        self.vs[18]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class Family()
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class Member()
                (0,8), # matchmodel -> match_contains
                (8,7), # match_contains -> match_class HouseholdRoot()
                (1,10), # applymodel -> apply_contains
                (10,9), # apply_contains -> apply_class Man()
                (1,12), # applymodel -> apply_contains
                (12,11), # apply_contains -> apply_class CommunityRoot()
                (3,13), # match_class Family() -> association father
                (13,5), # association father  -> match_class Member()
                (7,14), # match_class HouseholdRoot() -> association have
                (14,3), # association have  -> match_class Family()
                (11,15), # apply_class CommunityRoot() -> association has
                (15,9), # association has  -> apply_class Man()
                (9,16), # apply_class Man() -> backward_association
                (16,5), #  backward_association -> apply_class Member()
                (11,17), # apply_class CommunityRoot() -> backward_association
                (17,7), #  backward_association -> apply_class HouseholdRoot()
                (9,18), # apply_class Man() -> backward_association
                (18,3), #  backward_association -> apply_class Family()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((9,'ApplyAttribute'),('constant','famMemberFather')), ((11,'ApplyAttribute'),('constant','root')), ]

        
