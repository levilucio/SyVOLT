from core.himesis import Himesis
import uuid

class HdfacilitiesSolveRefNeighborhoodSchoolServiceChildDistrictOrdinaryFacilityPerson(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule dfacilitiesSolveRefNeighborhoodSchoolServiceChildDistrictOrdinaryFacilityPerson.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HdfacilitiesSolveRefNeighborhoodSchoolServiceChildDistrictOrdinaryFacilityPerson, self).__init__(name='HdfacilitiesSolveRefNeighborhoodSchoolServiceChildDistrictOrdinaryFacilityPerson', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """dfacilitiesSolveRefNeighborhoodSchoolServiceChildDistrictOrdinaryFacilityPerson"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'dfacilitiesSolveRefNeighborhoodSchoolServiceChildDistrictOrdinaryFacilityPerson')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
 
        
        # match class Neighborhood() node
        self.add_node()

        self.vs[3]["mm__"] = """Neighborhood""" 
        self.vs[3]["attr1"] = """+""" 
        # match_contains node for class Neighborhood()
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        # match class School() node
        self.add_node()

        self.vs[5]["mm__"] = """School""" 
        self.vs[5]["attr1"] = """+""" 
        # match_contains node for class School()
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        # match class Service() node
        self.add_node()

        self.vs[7]["mm__"] = """Service""" 
        self.vs[7]["attr1"] = """1""" 
        # match_contains node for class Service()
        self.add_node()
        self.vs[8]["mm__"] = """match_contains"""
        # match class Child() node
        self.add_node()

        self.vs[9]["mm__"] = """Child""" 
        self.vs[9]["attr1"] = """+""" 
        # match_contains node for class Child()
        self.add_node()
        self.vs[10]["mm__"] = """match_contains"""
        
        
        # apply class District() node
        self.add_node()

        self.vs[11]["mm__"] = """District""" 
        self.vs[11]["attr1"] = """1"""
        # apply_contains node for class District()
        self.add_node()
        self.vs[12]["mm__"] = """apply_contains"""
        # apply class OrdinaryFacility() node
        self.add_node()

        self.vs[13]["mm__"] = """OrdinaryFacility""" 
        self.vs[13]["attr1"] = """1"""
        # apply_contains node for class OrdinaryFacility()
        self.add_node()
        self.vs[14]["mm__"] = """apply_contains"""
        # apply class Person() node
        self.add_node()

        self.vs[15]["mm__"] = """Person""" 
        self.vs[15]["attr1"] = """1"""
        # apply_contains node for class Person()
        self.add_node()
        self.vs[16]["mm__"] = """apply_contains"""
        
        
        # match association Neighborhood--schools-->School node
        self.add_node()
        self.vs[17]["attr1"] = """schools"""
        self.vs[17]["mm__"] = """directLink_S"""
        # match association School--ordinary-->Service node
        self.add_node()
        self.vs[18]["attr1"] = """ordinary"""
        self.vs[18]["mm__"] = """directLink_S"""
        # match association School--students-->Child node
        self.add_node()
        self.vs[19]["attr1"] = """students"""
        self.vs[19]["mm__"] = """directLink_S"""
        # match association Child--goesTo-->School node
        self.add_node()
        self.vs[20]["attr1"] = """goesTo"""
        self.vs[20]["mm__"] = """directLink_S"""
        
        # apply association District--facilities-->OrdinaryFacility node
        self.add_node()
        self.vs[21]["attr1"] = """facilities"""
        self.vs[21]["mm__"] = """directLink_T"""
        # apply association OrdinaryFacility--members-->Person node
        self.add_node()
        self.vs[22]["attr1"] = """members"""
        self.vs[22]["mm__"] = """directLink_T"""
        
        # backward association Neighborhood---->District node
        self.add_node()

        self.vs[23]["mm__"] = """backward_link"""
        # backward association Child---->Person node
        self.add_node()

        self.vs[24]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class Neighborhood()
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class School()
                (0,8), # matchmodel -> match_contains
                (8,7), # match_contains -> match_class Service()
                (0,10), # matchmodel -> match_contains
                (10,9), # match_contains -> match_class Child()
                (1,12), # applymodel -> apply_contains
                (12,11), # apply_contains -> apply_class District()
                (1,14), # applymodel -> apply_contains
                (14,13), # apply_contains -> apply_class OrdinaryFacility()
                (1,16), # applymodel -> apply_contains
                (16,15), # apply_contains -> apply_class Person()
                (3,17), # match_class Neighborhood() -> association schools
                (17,5), # association schools  -> match_class School()
                (5,18), # match_class School() -> association ordinary
                (18,7), # association ordinary  -> match_class Service()
                (5,19), # match_class School() -> association students
                (19,9), # association students  -> match_class Child()
                (9,20), # match_class Child() -> association goesTo
                (20,5), # association goesTo  -> match_class School()
                (11,21), # apply_class District() -> association facilities
                (21,13), # association facilities  -> apply_class OrdinaryFacility()
                (13,22), # apply_class OrdinaryFacility() -> association members
                (22,15), # association members  -> apply_class Person()
                (11,23), # apply_class District() -> backward_association
                (23,3), #  backward_association -> apply_class Neighborhood()
                (15,24), # apply_class Person() -> backward_association
                (24,9), #  backward_association -> apply_class Child()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((11,'ApplyAttribute'),('constant','solveRef')), ((13,'name'),('concat',(('constant','Ordinary Facility Service for school '),(5,'name')))), ((13,'ApplyAttribute'),('constant','solveRef')), ((15,'ApplyAttribute'),('constant','solveRef')), ]

        
