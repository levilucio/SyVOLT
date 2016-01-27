from core.himesis import Himesis
import uuid

class HCityCompany2Association(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule CityCompany2Association.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HCityCompany2Association, self).__init__(name='HCityCompany2Association', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """CityCompany2Association"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'CityCompany2Association')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
 
        
        # match class City() node
        self.add_node()

        self.vs[3]["mm__"] = """City""" 
        self.vs[3]["attr1"] = """+""" 
        # match_contains node for class City()
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        # match class Company() node
        self.add_node()

        self.vs[5]["mm__"] = """Company""" 
        self.vs[5]["attr1"] = """+""" 
        # match_contains node for class Company()
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        
        
        # apply class Association() node
        self.add_node()

        self.vs[7]["mm__"] = """Association""" 
        self.vs[7]["attr1"] = """1"""
        # apply_contains node for class Association()
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        
        
        # match association City--companies-->Company node
        self.add_node()
        self.vs[9]["attr1"] = """companies"""
        self.vs[9]["mm__"] = """directLink_S"""
        # match association Company--isIn-->City node
        self.add_node()
        self.vs[10]["attr1"] = """isIn"""
        self.vs[10]["mm__"] = """directLink_S"""
        
        
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class City()
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class Company()
                (1,8), # applymodel -> apply_contains
                (8,7), # apply_contains -> apply_class Association()
                (3,9), # match_class City() -> association companies
                (9,5), # association companies  -> match_class Company()
                (5,10), # match_class Company() -> association isIn
                (10,3), # association isIn  -> match_class City()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((7,'name'),('concat',((3,'name'),(5,'name')))), ]

        
