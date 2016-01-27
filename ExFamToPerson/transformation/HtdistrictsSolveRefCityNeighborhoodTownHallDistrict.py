from core.himesis import Himesis
import uuid

class HtdistrictsSolveRefCityNeighborhoodTownHallDistrict(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule tdistrictsSolveRefCityNeighborhoodTownHallDistrict.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HtdistrictsSolveRefCityNeighborhoodTownHallDistrict, self).__init__(name='HtdistrictsSolveRefCityNeighborhoodTownHallDistrict', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """tdistrictsSolveRefCityNeighborhoodTownHallDistrict"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'tdistrictsSolveRefCityNeighborhoodTownHallDistrict')
        
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
        # match class Neighborhood() node
        self.add_node()

        self.vs[5]["mm__"] = """Neighborhood""" 
        self.vs[5]["attr1"] = """+""" 
        # match_contains node for class Neighborhood()
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        
        
        # apply class TownHall() node
        self.add_node()

        self.vs[7]["mm__"] = """TownHall""" 
        self.vs[7]["attr1"] = """1"""
        # apply_contains node for class TownHall()
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        # apply class District() node
        self.add_node()

        self.vs[9]["mm__"] = """District""" 
        self.vs[9]["attr1"] = """1"""
        # apply_contains node for class District()
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        
        
        # match association City--neighborhoods-->Neighborhood node
        self.add_node()
        self.vs[11]["attr1"] = """neighborhoods"""
        self.vs[11]["mm__"] = """directLink_S"""
        
        # apply association TownHall--districts-->District node
        self.add_node()
        self.vs[12]["attr1"] = """districts"""
        self.vs[12]["mm__"] = """directLink_T"""
        
        # backward association City---->TownHall node
        self.add_node()

        self.vs[13]["mm__"] = """backward_link"""
        # backward association Neighborhood---->District node
        self.add_node()

        self.vs[14]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class City()
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class Neighborhood()
                (1,8), # applymodel -> apply_contains
                (8,7), # apply_contains -> apply_class TownHall()
                (1,10), # applymodel -> apply_contains
                (10,9), # apply_contains -> apply_class District()
                (3,11), # match_class City() -> association neighborhoods
                (11,5), # association neighborhoods  -> match_class Neighborhood()
                (7,12), # apply_class TownHall() -> association districts
                (12,9), # association districts  -> apply_class District()
                (7,13), # apply_class TownHall() -> backward_association
                (13,3), #  backward_association -> apply_class City()
                (9,14), # apply_class District() -> backward_association
                (14,5), #  backward_association -> apply_class Neighborhood()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = []

        
