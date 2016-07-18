from core.himesis import Himesis
import uuid

class HdfacilitiesSolveRefNeighborhoodSchoolServiceChildDistrictSpecialFacilityPerson(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule dfacilitiesSolveRefNeighborhoodSchoolServiceChildDistrictSpecialFacilityPerson.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HdfacilitiesSolveRefNeighborhoodSchoolServiceChildDistrictSpecialFacilityPerson, self).__init__(name='HdfacilitiesSolveRefNeighborhoodSchoolServiceChildDistrictSpecialFacilityPerson', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """dfacilitiesSolveRefNeighborhoodSchoolServiceChildDistrictSpecialFacilityPerson"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'dfacilitiesSolveRefNeighborhoodSchoolServiceChildDistrictSpecialFacilityPerson')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["attr1"] = """dfacilitiesSolveRefNeighborhoodSchoolServiceChildDistrictSpecialFacilityPerson"""
        
        # match class Neighborhood() node
        self.add_node()
        
        self.vs[3]["mm__"] = """Neighborhood""" 
        self.vs[3]["attr1"] = """+""" 
        # match class School() node
        self.add_node()
        
        self.vs[4]["mm__"] = """School""" 
        self.vs[4]["attr1"] = """+""" 
        # match class Service() node
        self.add_node()
        
        self.vs[5]["mm__"] = """Service""" 
        self.vs[5]["attr1"] = """1""" 
        # match class Child() node
        self.add_node()
        
        self.vs[6]["mm__"] = """Child""" 
        self.vs[6]["attr1"] = """+""" 
        
        
        # apply class District() node
        self.add_node()

        self.vs[7]["mm__"] = """District""" 
        self.vs[7]["attr1"] = """1"""
        # apply class SpecialFacility() node
        self.add_node()

        self.vs[8]["mm__"] = """SpecialFacility""" 
        self.vs[8]["attr1"] = """1"""
        # apply class Person() node
        self.add_node()

        self.vs[9]["mm__"] = """Person""" 
        self.vs[9]["attr1"] = """1"""
        
        
        # match association Neighborhood--schools-->School node
        self.add_node()
        self.vs[10]["attr1"] = """schools"""
        self.vs[10]["mm__"] = """directLink_S"""
        # match association School--special-->Service node
        self.add_node()
        self.vs[11]["attr1"] = """special"""
        self.vs[11]["mm__"] = """directLink_S"""
        # match association School--students-->Child node
        self.add_node()
        self.vs[12]["attr1"] = """students"""
        self.vs[12]["mm__"] = """directLink_S"""
        # match association Child--goesTo-->School node
        self.add_node()
        self.vs[13]["attr1"] = """goesTo"""
        self.vs[13]["mm__"] = """directLink_S"""
        
        # apply association District--facilities-->SpecialFacility node
        self.add_node()
        self.vs[14]["attr1"] = """facilities"""
        self.vs[14]["mm__"] = """directLink_T"""
        # apply association SpecialFacility--members-->Person node
        self.add_node()
        self.vs[15]["attr1"] = """members"""
        self.vs[15]["mm__"] = """directLink_T"""
        
        # backward association Neighborhood---->District node
        self.add_node()

        self.vs[16]["mm__"] = """backward_link"""
        # backward association Child---->Person node
        self.add_node()

        self.vs[17]["mm__"] = """backward_link"""
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class Neighborhood()
                (0,4), # matchmodel -> match_class School()
                (0,5), # matchmodel -> match_class Service()
                (0,6), # matchmodel -> match_class Child()
                (1,7), # applymodel -> -> apply_class District()
                (1,8), # applymodel -> -> apply_class SpecialFacility()
                (1,9), # applymodel -> -> apply_class Person()
                (3,10), # match_class Neighborhood() -> association schools
                (10,4), # association schools  -> match_class School()
                (4,11), # match_class School() -> association special
                (11,5), # association special  -> match_class Service()
                (4,12), # match_class School() -> association students
                (12,6), # association students  -> match_class Child()
                (6,13), # match_class Child() -> association goesTo
                (13,4), # association goesTo  -> match_class School()
                (7,14), # apply_class District() -> association facilities
                (14,8), # association facilities  -> apply_class SpecialFacility()
                (8,15), # apply_class SpecialFacility() -> association members
                (15,9), # association members  -> apply_class Person()
                (7,16), # apply_class District() -> backward_association
                (16,3), #  backward_association -> apply_class Neighborhood()
                (9,17), # apply_class Person() -> backward_association
                (17,6), #  backward_association -> apply_class Child()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((8,'name'),('concat',(('constant','Special Facility Service for school '),(4,'name')))), ]

        
