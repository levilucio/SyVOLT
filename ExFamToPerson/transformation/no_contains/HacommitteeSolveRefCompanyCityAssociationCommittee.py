from core.himesis import Himesis
import uuid

class HacommitteeSolveRefCompanyCityAssociationCommittee(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule acommitteeSolveRefCompanyCityAssociationCommittee.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HacommitteeSolveRefCompanyCityAssociationCommittee, self).__init__(name='HacommitteeSolveRefCompanyCityAssociationCommittee', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """acommitteeSolveRefCompanyCityAssociationCommittee"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'acommitteeSolveRefCompanyCityAssociationCommittee')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["attr1"] = """acommitteeSolveRefCompanyCityAssociationCommittee"""
        
        # match class Company() node
        self.add_node()
        
        self.vs[3]["mm__"] = """Company""" 
        self.vs[3]["attr1"] = """+""" 
        # match class City() node
        self.add_node()
        
        self.vs[4]["mm__"] = """City""" 
        self.vs[4]["attr1"] = """+""" 
        
        
        # apply class Association() node
        self.add_node()

        self.vs[5]["mm__"] = """Association""" 
        self.vs[5]["attr1"] = """1"""
        # apply class Committee() node
        self.add_node()

        self.vs[6]["mm__"] = """Committee""" 
        self.vs[6]["attr1"] = """1"""
        
        
        # match association Company--isIn-->City node
        self.add_node()
        self.vs[7]["attr1"] = """isIn"""
        self.vs[7]["mm__"] = """directLink_S"""
        # match association City--companies-->Company node
        self.add_node()
        self.vs[8]["attr1"] = """companies"""
        self.vs[8]["mm__"] = """directLink_S"""
        
        # apply association Association--committee-->Committee node
        self.add_node()
        self.vs[9]["attr1"] = """committee"""
        self.vs[9]["mm__"] = """directLink_T"""
        
        # backward association Company---->Association node
        self.add_node()

        self.vs[10]["mm__"] = """backward_link"""
        # backward association City---->Association node
        self.add_node()

        self.vs[11]["mm__"] = """backward_link"""
        # backward association City---->Committee node
        self.add_node()

        self.vs[12]["mm__"] = """backward_link"""
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class Company()
                (0,4), # matchmodel -> match_class City()
                (1,5), # applymodel -> -> apply_class Association()
                (1,6), # applymodel -> -> apply_class Committee()
                (3,7), # match_class Company() -> association isIn
                (7,4), # association isIn  -> match_class City()
                (4,8), # match_class City() -> association companies
                (8,3), # association companies  -> match_class Company()
                (5,9), # apply_class Association() -> association committee
                (9,6), # association committee  -> apply_class Committee()
                (5,10), # apply_class Association() -> backward_association
                (10,3), #  backward_association -> apply_class Company()
                (5,11), # apply_class Association() -> backward_association
                (11,4), #  backward_association -> apply_class City()
                (6,12), # apply_class Committee() -> backward_association
                (12,4), #  backward_association -> apply_class City()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = []

        
