from core.himesis import Himesis
import uuid

class HUnionSonRule(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule UnionSonRule.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HUnionSonRule, self).__init__(name='HUnionSonRule', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """UnionSonRule"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'UnionSonRule')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["rulename"] = """UnionSonRule"""
        
        # match class Family() node
        self.add_node()
        self.vs[3]["name"] = """"""
        self.vs[3]["classtype"] = """Family"""
        self.vs[3]["mm__"] = """Family"""
        self.vs[3]["cardinality"] = """+"""
        # match_contains node for class Family()
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        # match class HouseholdRoot() node
        self.add_node()
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """HouseholdRoot"""
        self.vs[5]["mm__"] = """HouseholdRoot"""
        self.vs[5]["cardinality"] = """+"""
        # match_contains node for class HouseholdRoot()
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        # match class Member() node
        self.add_node()
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """Member"""
        self.vs[7]["mm__"] = """Member"""
        self.vs[7]["cardinality"] = """+"""
        # match_contains node for class Member()
        self.add_node()
        self.vs[8]["mm__"] = """match_contains"""
        
        
        # apply class Man() node
        self.add_node()
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """Man"""
        self.vs[9]["mm__"] = """Man"""
        self.vs[9]["cardinality"] = """1"""
        # apply_contains node for class Man()
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        # apply class CommunityRoot() node
        self.add_node()
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """CommunityRoot"""
        self.vs[11]["mm__"] = """CommunityRoot"""
        self.vs[11]["cardinality"] = """1"""
        # apply_contains node for class CommunityRoot()
        self.add_node()
        self.vs[12]["mm__"] = """apply_contains"""
        
        
        # match association HouseholdRoot--have-->Family node
        self.add_node()
        self.vs[13]["associationType"] = """have"""
        self.vs[13]["mm__"] = """directLink_S"""
        # match association Family--son-->Member node
        self.add_node()
        self.vs[14]["associationType"] = """son"""
        self.vs[14]["mm__"] = """directLink_S"""
        
        # apply association CommunityRoot--has-->Man node
        self.add_node()
        self.vs[15]["associationType"] = """has"""
        self.vs[15]["mm__"] = """directLink_T"""
        
        # backward association HouseholdRoot---->CommunityRoot node
        self.add_node()
        self.vs[16]["type"] = """ruleDef"""
        self.vs[16]["mm__"] = """backward_link"""
        # backward association Family---->Man node
        self.add_node()
        self.vs[17]["type"] = """ruleDef"""
        self.vs[17]["mm__"] = """backward_link"""
        # backward association Member---->Man node
        self.add_node()
        self.vs[18]["type"] = """ruleDef"""
        self.vs[18]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class Family()
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class HouseholdRoot()
                (0,8), # matchmodel -> match_contains
                (8,7), # match_contains -> match_class Member()
                (1,10), # applymodel -> apply_contains
                (10,9), # apply_contains -> apply_class Man()
                (1,12), # applymodel -> apply_contains
                (12,11), # apply_contains -> apply_class CommunityRoot()
                (5,13), # match_class HouseholdRoot() -> association have
                (13,3), # association have  -> match_class Family()
                (3,14), # match_class Family() -> association son
                (14,7), # association son  -> match_class Member()
                (11,15), # apply_class CommunityRoot() -> association has
                (15,9), # association has  -> apply_class Man()
                (11,16), # apply_class CommunityRoot() -> backward_association
                (16,5), #  backward_association -> apply_class HouseholdRoot()
                (9,17), # apply_class Man() -> backward_association
                (17,3), #  backward_association -> apply_class Family()
                (9,18), # apply_class Man() -> backward_association
                (18,7), #  backward_association -> apply_class Member()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])
		
        # Add the equations
        self["equations"] = [((9,'ApplyAttribute'),('constant','famMemberSon')), ((11,'ApplyAttribute'),('constant','root')), ]

        
