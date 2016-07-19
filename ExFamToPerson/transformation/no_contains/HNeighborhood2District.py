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
        self.vs[2]["attr1"] = """Neighborhood2District"""
        
        # match class Neighborhood() node
        self.add_node()
        
        self.vs[3]["mm__"] = """Neighborhood""" 
        self.vs[3]["attr1"] = """+""" 
        # match class Family() node
        self.add_node()
        
        self.vs[4]["mm__"] = """Family""" 
        self.vs[4]["attr1"] = """1""" 
        
        
        # apply class District() node
        self.add_node()

        self.vs[5]["mm__"] = """District""" 
        self.vs[5]["attr1"] = """1"""
        
        
        # match association Family--registeredIn-->Neighborhood node
        self.add_node()
        self.vs[6]["attr1"] = """registeredIn"""
        self.vs[6]["mm__"] = """directLink_S"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class Neighborhood()
                (0,4), # matchmodel -> match_class Family()
                (1,5), # applymodel -> -> apply_class District()
                (4,6), # match_class Family() -> association registeredIn
                (6,3), # association registeredIn  -> match_class Neighborhood()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((5,'name'),(3,'name')), ]

        
