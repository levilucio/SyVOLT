from core.himesis import Himesis
import uuid

class HNeighborhood2District(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule Neighborhood2District.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HNeighborhood2District, self).__init__(name='HNeighborhood2District', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """Neighborhood2District"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Neighborhood2District')
        
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
        # match class Family() node
        self.add_node()

        self.vs[5]["mm__"] = """Family""" 
        self.vs[5]["attr1"] = """1""" 
        # match_contains node for class Family()
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        
        
        # apply class District() node
        self.add_node()

        self.vs[7]["mm__"] = """District""" 
        self.vs[7]["attr1"] = """1"""
        # apply_contains node for class District()
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        
        
        # match association Family--registeredIn-->Neighborhood node
        self.add_node()
        self.vs[9]["attr1"] = """registeredIn"""
        self.vs[9]["mm__"] = """directLink_S"""
        
        
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class Neighborhood()
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class Family()
                (1,8), # applymodel -> apply_contains
                (8,7), # apply_contains -> apply_class District()
                (5,9), # match_class Family() -> association registeredIn
                (9,3), # association registeredIn  -> match_class Neighborhood()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((7,'name'),(3,'name')), ]

        
