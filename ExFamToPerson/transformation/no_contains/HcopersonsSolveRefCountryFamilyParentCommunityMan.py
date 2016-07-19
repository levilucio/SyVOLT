from core.himesis import Himesis
import uuid

class HcopersonsSolveRefCountryFamilyParentCommunityMan(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule copersonsSolveRefCountryFamilyParentCommunityMan.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HcopersonsSolveRefCountryFamilyParentCommunityMan, self).__init__(name='HcopersonsSolveRefCountryFamilyParentCommunityMan', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """copersonsSolveRefCountryFamilyParentCommunityMan"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'copersonsSolveRefCountryFamilyParentCommunityMan')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["attr1"] = """copersonsSolveRefCountryFamilyParentCommunityMan"""
        
        # match class Country() node
        self.add_node()
        
        self.vs[3]["mm__"] = """Country""" 
        self.vs[3]["attr1"] = """+""" 
        # match class Family() node
        self.add_node()
        
        self.vs[4]["mm__"] = """Family""" 
        self.vs[4]["attr1"] = """+""" 
        # match class Parent() node
        self.add_node()
        
        self.vs[5]["mm__"] = """Parent""" 
        self.vs[5]["attr1"] = """+""" 
        
        
        # apply class Community() node
        self.add_node()

        self.vs[6]["mm__"] = """Community""" 
        self.vs[6]["attr1"] = """1"""
        # apply class Man() node
        self.add_node()

        self.vs[7]["mm__"] = """Man""" 
        self.vs[7]["attr1"] = """1"""
        
        
        # match association Country--families-->Family node
        self.add_node()
        self.vs[8]["attr1"] = """families"""
        self.vs[8]["mm__"] = """directLink_S"""
        # match association Family--fathers-->Parent node
        self.add_node()
        self.vs[9]["attr1"] = """fathers"""
        self.vs[9]["mm__"] = """directLink_S"""
        
        # apply association Community--persons-->Man node
        self.add_node()
        self.vs[10]["attr1"] = """persons"""
        self.vs[10]["mm__"] = """directLink_T"""
        
        # backward association Country---->Community node
        self.add_node()

        self.vs[11]["mm__"] = """backward_link"""
        # backward association Parent---->Man node
        self.add_node()

        self.vs[12]["mm__"] = """backward_link"""
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class Country()
                (0,4), # matchmodel -> match_class Family()
                (0,5), # matchmodel -> match_class Parent()
                (1,6), # applymodel -> -> apply_class Community()
                (1,7), # applymodel -> -> apply_class Man()
                (3,8), # match_class Country() -> association families
                (8,4), # association families  -> match_class Family()
                (4,9), # match_class Family() -> association fathers
                (9,5), # association fathers  -> match_class Parent()
                (6,10), # apply_class Community() -> association persons
                (10,7), # association persons  -> apply_class Man()
                (6,11), # apply_class Community() -> backward_association
                (11,3), #  backward_association -> apply_class Country()
                (7,12), # apply_class Man() -> backward_association
                (12,5), #  backward_association -> apply_class Parent()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = []

        
