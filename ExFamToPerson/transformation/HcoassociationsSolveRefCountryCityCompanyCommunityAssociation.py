from core.himesis import Himesis
import uuid

class HcoassociationsSolveRefCountryCityCompanyCommunityAssociation(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule coassociationsSolveRefCountryCityCompanyCommunityAssociation.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HcoassociationsSolveRefCountryCityCompanyCommunityAssociation, self).__init__(name='HcoassociationsSolveRefCountryCityCompanyCommunityAssociation', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """coassociationsSolveRefCountryCityCompanyCommunityAssociation"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'coassociationsSolveRefCountryCityCompanyCommunityAssociation')
        
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
        # match class City() node
        self.add_node()

        self.vs[5]["mm__"] = """City""" 
        self.vs[5]["attr1"] = """+""" 
        # match_contains node for class City()
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        # match class Company() node
        self.add_node()

        self.vs[7]["mm__"] = """Company""" 
        self.vs[7]["attr1"] = """+""" 
        # match_contains node for class Company()
        self.add_node()
        self.vs[8]["mm__"] = """match_contains"""
        
        
        # apply class Community() node
        self.add_node()

        self.vs[9]["mm__"] = """Community""" 
        self.vs[9]["attr1"] = """1"""
        # apply_contains node for class Community()
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        # apply class Association() node
        self.add_node()

        self.vs[11]["mm__"] = """Association""" 
        self.vs[11]["attr1"] = """1"""
        # apply_contains node for class Association()
        self.add_node()
        self.vs[12]["mm__"] = """apply_contains"""
        
        
        # match association Country--cities-->City node
        self.add_node()
        self.vs[13]["attr1"] = """cities"""
        self.vs[13]["mm__"] = """directLink_S"""
        # match association Country--companies-->Company node
        self.add_node()
        self.vs[14]["attr1"] = """companies"""
        self.vs[14]["mm__"] = """directLink_S"""
        # match association City--companies-->Company node
        self.add_node()
        self.vs[15]["attr1"] = """companies"""
        self.vs[15]["mm__"] = """directLink_S"""
        # match association Company--isIn-->City node
        self.add_node()
        self.vs[16]["attr1"] = """isIn"""
        self.vs[16]["mm__"] = """directLink_S"""
        
        # apply association Community--associations-->Association node
        self.add_node()
        self.vs[17]["attr1"] = """associations"""
        self.vs[17]["mm__"] = """directLink_T"""
        
        # backward association Country---->Community node
        self.add_node()

        self.vs[18]["mm__"] = """backward_link"""
        # backward association City---->Association node
        self.add_node()

        self.vs[19]["mm__"] = """backward_link"""
        # backward association Company---->Association node
        self.add_node()

        self.vs[20]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class Country()
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class City()
                (0,8), # matchmodel -> match_contains
                (8,7), # match_contains -> match_class Company()
                (1,10), # applymodel -> apply_contains
                (10,9), # apply_contains -> apply_class Community()
                (1,12), # applymodel -> apply_contains
                (12,11), # apply_contains -> apply_class Association()
                (3,13), # match_class Country() -> association cities
                (13,5), # association cities  -> match_class City()
                (3,14), # match_class Country() -> association companies
                (14,7), # association companies  -> match_class Company()
                (5,15), # match_class City() -> association companies
                (15,7), # association companies  -> match_class Company()
                (7,16), # match_class Company() -> association isIn
                (16,5), # association isIn  -> match_class City()
                (9,17), # apply_class Community() -> association associations
                (17,11), # association associations  -> apply_class Association()
                (9,18), # apply_class Community() -> backward_association
                (18,3), #  backward_association -> apply_class Country()
                (11,19), # apply_class Association() -> backward_association
                (19,5), #  backward_association -> apply_class City()
                (11,20), # apply_class Association() -> backward_association
                (20,7), #  backward_association -> apply_class Company()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = []

        
