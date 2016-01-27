from core.himesis import Himesis
import uuid

class HcopersonsSolveRefCountryFamilyChildCommunityMan(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule copersonsSolveRefCountryFamilyChildCommunityMan.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HcopersonsSolveRefCountryFamilyChildCommunityMan, self).__init__(name='HcopersonsSolveRefCountryFamilyChildCommunityMan', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """copersonsSolveRefCountryFamilyChildCommunityMan"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'copersonsSolveRefCountryFamilyChildCommunityMan')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
 
        
        # match class Country() node
        self.add_node()

        self.vs[3]["mm__"] = """Country""" 
        self.vs[3]["attr1"] = """+""" 
        # match_contains node for class Country()
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        # match class Family() node
        self.add_node()

        self.vs[5]["mm__"] = """Family""" 
        self.vs[5]["attr1"] = """+""" 
        # match_contains node for class Family()
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        # match class Child() node
        self.add_node()

        self.vs[7]["mm__"] = """Child""" 
        self.vs[7]["attr1"] = """+""" 
        # match_contains node for class Child()
        self.add_node()
        self.vs[8]["mm__"] = """match_contains"""
        
        
        # apply class Community() node
        self.add_node()

        self.vs[9]["mm__"] = """Community""" 
        self.vs[9]["attr1"] = """1"""
        # apply_contains node for class Community()
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        # apply class Man() node
        self.add_node()

        self.vs[11]["mm__"] = """Man""" 
        self.vs[11]["attr1"] = """1"""
        # apply_contains node for class Man()
        self.add_node()
        self.vs[12]["mm__"] = """apply_contains"""
        
        
        # match association Country--families-->Family node
        self.add_node()
        self.vs[13]["attr1"] = """families"""
        self.vs[13]["mm__"] = """directLink_S"""
        # match association Family--sons-->Child node
        self.add_node()
        self.vs[14]["attr1"] = """sons"""
        self.vs[14]["mm__"] = """directLink_S"""
        
        # apply association Community--persons-->Man node
        self.add_node()
        self.vs[15]["attr1"] = """persons"""
        self.vs[15]["mm__"] = """directLink_T"""
        
        # backward association Country---->Community node
        self.add_node()

        self.vs[16]["mm__"] = """backward_link"""
        # backward association Child---->Man node
        self.add_node()

        self.vs[17]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class Country()
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class Family()
                (0,8), # matchmodel -> match_contains
                (8,7), # match_contains -> match_class Child()
                (1,10), # applymodel -> apply_contains
                (10,9), # apply_contains -> apply_class Community()
                (1,12), # applymodel -> apply_contains
                (12,11), # apply_contains -> apply_class Man()
                (3,13), # match_class Country() -> association families
                (13,5), # association families  -> match_class Family()
                (5,14), # match_class Family() -> association sons
                (14,7), # association sons  -> match_class Child()
                (9,15), # apply_class Community() -> association persons
                (15,11), # association persons  -> apply_class Man()
                (9,16), # apply_class Community() -> backward_association
                (16,3), #  backward_association -> apply_class Country()
                (11,17), # apply_class Man() -> backward_association
                (17,7), #  backward_association -> apply_class Child()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = []

        
