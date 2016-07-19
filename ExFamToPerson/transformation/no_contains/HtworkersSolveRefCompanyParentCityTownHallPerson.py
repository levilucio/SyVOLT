from core.himesis import Himesis
import uuid

class HtworkersSolveRefCompanyParentCityTownHallPerson(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule tworkersSolveRefCompanyParentCityTownHallPerson.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HtworkersSolveRefCompanyParentCityTownHallPerson, self).__init__(name='HtworkersSolveRefCompanyParentCityTownHallPerson', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """tworkersSolveRefCompanyParentCityTownHallPerson"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'tworkersSolveRefCompanyParentCityTownHallPerson')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["attr1"] = """tworkersSolveRefCompanyParentCityTownHallPerson"""
        
        # match class Company() node
        self.add_node()
        
        self.vs[3]["mm__"] = """Company""" 
        self.vs[3]["attr1"] = """+""" 
        # match class Parent() node
        self.add_node()
        
        self.vs[4]["mm__"] = """Parent""" 
        self.vs[4]["attr1"] = """+""" 
        # match class City() node
        self.add_node()
        
        self.vs[5]["mm__"] = """City""" 
        self.vs[5]["attr1"] = """+""" 
        
        
        # apply class TownHall() node
        self.add_node()

        self.vs[6]["mm__"] = """TownHall""" 
        self.vs[6]["attr1"] = """1"""
        # apply class Person() node
        self.add_node()

        self.vs[7]["mm__"] = """Person""" 
        self.vs[7]["attr1"] = """1"""
        
        
        # match association Company--employees-->Parent node
        self.add_node()
        self.vs[8]["attr1"] = """employees"""
        self.vs[8]["mm__"] = """directLink_S"""
        # match association Parent--livesIn-->City node
        self.add_node()
        self.vs[9]["attr1"] = """livesIn"""
        self.vs[9]["mm__"] = """directLink_S"""
        # match association City--companies-->Company node
        self.add_node()
        self.vs[10]["attr1"] = """companies"""
        self.vs[10]["mm__"] = """directLink_S"""
        # match association Company--isIn-->City node
        self.add_node()
        self.vs[11]["attr1"] = """isIn"""
        self.vs[11]["mm__"] = """directLink_S"""
        
        # apply association TownHall--workers-->Person node
        self.add_node()
        self.vs[12]["attr1"] = """workers"""
        self.vs[12]["mm__"] = """directLink_T"""
        
        # backward association Parent---->Person node
        self.add_node()

        self.vs[13]["mm__"] = """backward_link"""
        # backward association City---->TownHall node
        self.add_node()

        self.vs[14]["mm__"] = """backward_link"""
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class Company()
                (0,4), # matchmodel -> match_class Parent()
                (0,5), # matchmodel -> match_class City()
                (1,6), # applymodel -> -> apply_class TownHall()
                (1,7), # applymodel -> -> apply_class Person()
                (3,8), # match_class Company() -> association employees
                (8,4), # association employees  -> match_class Parent()
                (4,9), # match_class Parent() -> association livesIn
                (9,5), # association livesIn  -> match_class City()
                (5,10), # match_class City() -> association companies
                (10,3), # association companies  -> match_class Company()
                (3,11), # match_class Company() -> association isIn
                (11,5), # association isIn  -> match_class City()
                (6,12), # apply_class TownHall() -> association workers
                (12,7), # association workers  -> apply_class Person()
                (7,13), # apply_class Person() -> backward_association
                (13,4), #  backward_association -> apply_class Parent()
                (6,14), # apply_class TownHall() -> backward_association
                (14,5), #  backward_association -> apply_class City()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = []

        
