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
 
        
        # match class Company() node
        self.add_node()

        self.vs[3]["mm__"] = """Company""" 
        self.vs[3]["attr1"] = """+""" 
        # match_contains node for class Company()
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        # match class City() node
        self.add_node()

        self.vs[5]["mm__"] = """City""" 
        self.vs[5]["attr1"] = """+""" 
        # match_contains node for class City()
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        
        
        # apply class Association() node
        self.add_node()

        self.vs[7]["mm__"] = """Association""" 
        self.vs[7]["attr1"] = """1"""
        # apply_contains node for class Association()
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        # apply class Committee() node
        self.add_node()

        self.vs[9]["mm__"] = """Committee""" 
        self.vs[9]["attr1"] = """1"""
        # apply_contains node for class Committee()
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        
        
        # match association Company--isIn-->City node
        self.add_node()
        self.vs[11]["attr1"] = """isIn"""
        self.vs[11]["mm__"] = """directLink_S"""
        
        # apply association Association--committee-->Committee node
        self.add_node()
        self.vs[12]["attr1"] = """committee"""
        self.vs[12]["mm__"] = """directLink_T"""
        
        # backward association Company---->Association node
        self.add_node()

        self.vs[13]["mm__"] = """backward_link"""
        # backward association City---->Association node
        self.add_node()

        self.vs[14]["mm__"] = """backward_link"""
        # backward association City---->Committee node
        self.add_node()

        self.vs[15]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class Company()
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class City()
                (1,8), # applymodel -> apply_contains
                (8,7), # apply_contains -> apply_class Association()
                (1,10), # applymodel -> apply_contains
                (10,9), # apply_contains -> apply_class Committee()
                (3,11), # match_class Company() -> association isIn
                (11,5), # association isIn  -> match_class City()
                (7,12), # apply_class Association() -> association committee
                (12,9), # association committee  -> apply_class Committee()
                (7,13), # apply_class Association() -> backward_association
                (13,3), #  backward_association -> apply_class Company()
                (7,14), # apply_class Association() -> backward_association
                (14,5), #  backward_association -> apply_class City()
                (9,15), # apply_class Committee() -> backward_association
                (15,5), #  backward_association -> apply_class City()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((7,'ApplyAttribute'),('constant','solveRef')), ((9,'ApplyAttribute'),('constant','solveRef')), ]

        
