from core.himesis import Himesis
import uuid

class HCountry2Community(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule Country2Community.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HCountry2Community, self).__init__(name='HCountry2Community', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """Country2Community"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Country2Community')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["attr1"] = """Country2Community"""
        
        # match class Country() node
        self.add_node()
        
        self.vs[3]["mm__"] = """Country""" 
        self.vs[3]["attr1"] = """+""" 
        
        
        # apply class Community() node
        self.add_node()

        self.vs[4]["mm__"] = """Community""" 
        self.vs[4]["attr1"] = """1"""
        
        
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class Country()
                (1,4), # applymodel -> -> apply_class Community()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = []

        
