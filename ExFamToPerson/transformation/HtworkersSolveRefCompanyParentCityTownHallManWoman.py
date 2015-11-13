from core.himesis import Himesis
import uuid

class HtworkersSolveRefCompanyParentCityTownHallManWoman(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule tworkersSolveRefCompanyParentCityTownHallManWoman.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HtworkersSolveRefCompanyParentCityTownHallManWoman, self).__init__(name='HtworkersSolveRefCompanyParentCityTownHallManWoman', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """tworkersSolveRefCompanyParentCityTownHallManWoman"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'tworkersSolveRefCompanyParentCityTownHallManWoman')
        
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
        # match class Parent() node
        self.add_node()

        self.vs[5]["mm__"] = """Parent""" 
        self.vs[5]["attr1"] = """+""" 
        # match_contains node for class Parent()
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        # match class City() node
        self.add_node()

        self.vs[7]["mm__"] = """City""" 
        self.vs[7]["attr1"] = """+""" 
        # match_contains node for class City()
        self.add_node()
        self.vs[8]["mm__"] = """match_contains"""
        
        
        # apply class TownHall() node
        self.add_node()

        self.vs[9]["mm__"] = """TownHall""" 
        self.vs[9]["attr1"] = """1"""
        # apply_contains node for class TownHall()
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        # apply class Man() node
        self.add_node()

        self.vs[11]["mm__"] = """Man""" 
        self.vs[11]["attr1"] = """1"""
        # apply_contains node for class Man()
        self.add_node()
        self.vs[12]["mm__"] = """apply_contains"""
        # apply class Woman() node
        self.add_node()

        self.vs[13]["mm__"] = """Woman""" 
        self.vs[13]["attr1"] = """1"""
        # apply_contains node for class Woman()
        self.add_node()
        self.vs[14]["mm__"] = """apply_contains"""
        
        
        # match association Company--employees-->Parent node
        self.add_node()
        self.vs[15]["attr1"] = """employees"""
        self.vs[15]["mm__"] = """directLink_S"""
        # match association Parent--livesIn-->City node
        self.add_node()
        self.vs[16]["attr1"] = """livesIn"""
        self.vs[16]["mm__"] = """directLink_S"""
        # match association City--companies-->Company node
        self.add_node()
        self.vs[17]["attr1"] = """companies"""
        self.vs[17]["mm__"] = """directLink_S"""
        
        # apply association TownHall--workers-->Man node
        self.add_node()
        self.vs[18]["attr1"] = """workers"""
        self.vs[18]["mm__"] = """directLink_T"""
        # apply association TownHall--workers-->Woman node
        self.add_node()
        self.vs[19]["attr1"] = """workers"""
        self.vs[19]["mm__"] = """directLink_T"""
        
        # backward association Parent---->Man node
        self.add_node()

        self.vs[20]["mm__"] = """backward_link"""
        # backward association Parent---->Woman node
        self.add_node()

        self.vs[21]["mm__"] = """backward_link"""
        # backward association City---->TownHall node
        self.add_node()

        self.vs[22]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class Company()
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class Parent()
                (0,8), # matchmodel -> match_contains
                (8,7), # match_contains -> match_class City()
                (1,10), # applymodel -> apply_contains
                (10,9), # apply_contains -> apply_class TownHall()
                (1,12), # applymodel -> apply_contains
                (12,11), # apply_contains -> apply_class Man()
                (1,14), # applymodel -> apply_contains
                (14,13), # apply_contains -> apply_class Woman()
                (3,15), # match_class Company() -> association employees
                (15,5), # association employees  -> match_class Parent()
                (5,16), # match_class Parent() -> association livesIn
                (16,7), # association livesIn  -> match_class City()
                (7,17), # match_class City() -> association companies
                (17,3), # association companies  -> match_class Company()
                (9,18), # apply_class TownHall() -> association workers
                (18,11), # association workers  -> apply_class Man()
                (9,19), # apply_class TownHall() -> association workers
                (19,13), # association workers  -> apply_class Woman()
                (11,20), # apply_class Man() -> backward_association
                (20,5), #  backward_association -> apply_class Parent()
                (13,21), # apply_class Woman() -> backward_association
                (21,5), #  backward_association -> apply_class Parent()
                (9,22), # apply_class TownHall() -> backward_association
                (22,7), #  backward_association -> apply_class City()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((9,'ApplyAttribute'),('constant','solveRef')), ((11,'ApplyAttribute'),('constant','solveRef')), ((13,'ApplyAttribute'),('constant','solveRef')), ]

        
