from core.himesis import Himesis
import uuid

class HcotownHallsSolveRefCountryCityCommunityTownHall(Himesis):
    def __init__(self, *args, **kwargs):

    
    
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
        
        
        # apply class Community() node
        self.add_node()

        self.vs[7]["mm__"] = """Community""" 
        self.vs[7]["attr1"] = """1"""
        # apply_contains node for class Community()
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        # apply class TownHall() node
        self.add_node()

        self.vs[9]["mm__"] = """TownHall""" 
        self.vs[9]["attr1"] = """1"""
        # apply_contains node for class TownHall()
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        
        
        # match association Country--cities-->City node
        self.add_node()
        self.vs[11]["attr1"] = """cities"""
        self.vs[11]["mm__"] = """directLink_S"""
        
        # apply association Community--townHalls-->TownHall node
        self.add_node()
        self.vs[12]["attr1"] = """townHalls"""
        self.vs[12]["mm__"] = """directLink_T"""
        
        # backward association Country---->Community node
        self.add_node()

        self.vs[13]["mm__"] = """backward_link"""
        # backward association City---->TownHall node
        self.add_node()

        self.vs[14]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class Country()
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class City()
                (1,8), # applymodel -> apply_contains
                (8,7), # apply_contains -> apply_class Community()
                (1,10), # applymodel -> apply_contains
                (10,9), # apply_contains -> apply_class TownHall()
                (3,11), # match_class Country() -> association cities
                (11,5), # association cities  -> match_class City()
                (7,12), # apply_class Community() -> association townHalls
                (12,9), # association townHalls  -> apply_class TownHall()
                (7,13), # apply_class Community() -> backward_association
                (13,3), #  backward_association -> apply_class Country()
                (9,14), # apply_class TownHall() -> backward_association
                (14,5), #  backward_association -> apply_class City()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = []

        
