from core.himesis import Himesis
import uuid

class HcotownHallsSolveRefCountryCityCommunityTownHall(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule cotownHallsSolveRefCountryCityCommunityTownHall.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HcotownHallsSolveRefCountryCityCommunityTownHall, self).__init__(name='HcotownHallsSolveRefCountryCityCommunityTownHall', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """cotownHallsSolveRefCountryCityCommunityTownHall"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'cotownHallsSolveRefCountryCityCommunityTownHall')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["attr1"] = """cotownHallsSolveRefCountryCityCommunityTownHall"""
        
        # match class Country() node
        self.add_node()
        
        self.vs[3]["mm__"] = """Country""" 
        self.vs[3]["attr1"] = """+""" 
        # match class City() node
        self.add_node()
        
        self.vs[4]["mm__"] = """City""" 
        self.vs[4]["attr1"] = """+""" 
        
        
        # apply class Community() node
        self.add_node()

        self.vs[5]["mm__"] = """Community""" 
        self.vs[5]["attr1"] = """1"""
        # apply class TownHall() node
        self.add_node()

        self.vs[6]["mm__"] = """TownHall""" 
        self.vs[6]["attr1"] = """1"""
        
        
        # match association Country--cities-->City node
        self.add_node()
        self.vs[7]["attr1"] = """cities"""
        self.vs[7]["mm__"] = """directLink_S"""
        
        # apply association Community--townHalls-->TownHall node
        self.add_node()
        self.vs[8]["attr1"] = """townHalls"""
        self.vs[8]["mm__"] = """directLink_T"""
        
        # backward association Country---->Community node
        self.add_node()

        self.vs[9]["mm__"] = """backward_link"""
        # backward association City---->TownHall node
        self.add_node()

        self.vs[10]["mm__"] = """backward_link"""
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class Country()
                (0,4), # matchmodel -> match_class City()
                (1,5), # applymodel -> -> apply_class Community()
                (1,6), # applymodel -> -> apply_class TownHall()
                (3,7), # match_class Country() -> association cities
                (7,4), # association cities  -> match_class City()
                (5,8), # apply_class Community() -> association townHalls
                (8,6), # association townHalls  -> apply_class TownHall()
                (5,9), # apply_class Community() -> backward_association
                (9,3), #  backward_association -> apply_class Country()
                (6,10), # apply_class TownHall() -> backward_association
                (10,4), #  backward_association -> apply_class City()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = []

        
