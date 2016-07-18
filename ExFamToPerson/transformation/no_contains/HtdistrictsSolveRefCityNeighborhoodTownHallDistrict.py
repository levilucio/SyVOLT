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
        self.vs[2]["attr1"] = """tdistrictsSolveRefCityNeighborhoodTownHallDistrict"""
        
        # match class City() node
        self.add_node()
        
        self.vs[3]["mm__"] = """City""" 
        self.vs[3]["attr1"] = """+""" 
        # match class Neighborhood() node
        self.add_node()
        
        self.vs[4]["mm__"] = """Neighborhood""" 
        self.vs[4]["attr1"] = """+""" 
        
        
        # apply class TownHall() node
        self.add_node()

        self.vs[5]["mm__"] = """TownHall""" 
        self.vs[5]["attr1"] = """1"""
        # apply class District() node
        self.add_node()

        self.vs[6]["mm__"] = """District""" 
        self.vs[6]["attr1"] = """1"""
        
        
        # match association City--neighborhoods-->Neighborhood node
        self.add_node()
        self.vs[7]["attr1"] = """neighborhoods"""
        self.vs[7]["mm__"] = """directLink_S"""
        
        # apply association TownHall--districts-->District node
        self.add_node()
        self.vs[8]["attr1"] = """districts"""
        self.vs[8]["mm__"] = """directLink_T"""
        
        # backward association City---->TownHall node
        self.add_node()

        self.vs[9]["mm__"] = """backward_link"""
        # backward association Neighborhood---->District node
        self.add_node()

        self.vs[10]["mm__"] = """backward_link"""
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class City()
                (0,4), # matchmodel -> match_class Neighborhood()
                (1,5), # applymodel -> -> apply_class TownHall()
                (1,6), # applymodel -> -> apply_class District()
                (3,7), # match_class City() -> association neighborhoods
                (7,4), # association neighborhoods  -> match_class Neighborhood()
                (5,8), # apply_class TownHall() -> association districts
                (8,6), # association districts  -> apply_class District()
                (5,9), # apply_class TownHall() -> backward_association
                (9,3), #  backward_association -> apply_class City()
                (6,10), # apply_class District() -> backward_association
                (10,4), #  backward_association -> apply_class Neighborhood()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = []

        
