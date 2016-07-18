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
        self.vs[2]["attr1"] = """coassociationsSolveRefCountryCityCompanyCommunityAssociation"""
        
        # match class Country() node
        self.add_node()
        
        self.vs[3]["mm__"] = """Country""" 
        self.vs[3]["attr1"] = """+""" 
        # match class City() node
        self.add_node()
        
        self.vs[4]["mm__"] = """City""" 
        self.vs[4]["attr1"] = """+""" 
        # match class Company() node
        self.add_node()
        
        self.vs[5]["mm__"] = """Company""" 
        self.vs[5]["attr1"] = """+""" 
        
        
        # apply class Community() node
        self.add_node()

        self.vs[6]["mm__"] = """Community""" 
        self.vs[6]["attr1"] = """1"""
        # apply class Association() node
        self.add_node()

        self.vs[7]["mm__"] = """Association""" 
        self.vs[7]["attr1"] = """1"""
        
        
        # match association Country--cities-->City node
        self.add_node()
        self.vs[8]["attr1"] = """cities"""
        self.vs[8]["mm__"] = """directLink_S"""
        # match association Country--companies-->Company node
        self.add_node()
        self.vs[9]["attr1"] = """companies"""
        self.vs[9]["mm__"] = """directLink_S"""
        # match association City--companies-->Company node
        self.add_node()
        self.vs[10]["attr1"] = """companies"""
        self.vs[10]["mm__"] = """directLink_S"""
        # match association Company--isIn-->City node
        self.add_node()
        self.vs[11]["attr1"] = """isIn"""
        self.vs[11]["mm__"] = """directLink_S"""
        
        # apply association Community--associations-->Association node
        self.add_node()
        self.vs[12]["attr1"] = """associations"""
        self.vs[12]["mm__"] = """directLink_T"""
        
        # backward association Country---->Community node
        self.add_node()

        self.vs[13]["mm__"] = """backward_link"""
        # backward association City---->Association node
        self.add_node()

        self.vs[14]["mm__"] = """backward_link"""
        # backward association Company---->Association node
        self.add_node()

        self.vs[15]["mm__"] = """backward_link"""
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class Country()
                (0,4), # matchmodel -> match_class City()
                (0,5), # matchmodel -> match_class Company()
                (1,6), # applymodel -> -> apply_class Community()
                (1,7), # applymodel -> -> apply_class Association()
                (3,8), # match_class Country() -> association cities
                (8,4), # association cities  -> match_class City()
                (3,9), # match_class Country() -> association companies
                (9,5), # association companies  -> match_class Company()
                (4,10), # match_class City() -> association companies
                (10,5), # association companies  -> match_class Company()
                (5,11), # match_class Company() -> association isIn
                (11,4), # association isIn  -> match_class City()
                (6,12), # apply_class Community() -> association associations
                (12,7), # association associations  -> apply_class Association()
                (6,13), # apply_class Community() -> backward_association
                (13,3), #  backward_association -> apply_class Country()
                (7,14), # apply_class Association() -> backward_association
                (14,4), #  backward_association -> apply_class City()
                (7,15), # apply_class Association() -> backward_association
                (15,5), #  backward_association -> apply_class Company()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = []

        
