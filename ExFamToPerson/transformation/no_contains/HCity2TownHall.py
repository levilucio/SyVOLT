from core.himesis import Himesis
import uuid

class HCity2TownHall(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule City2TownHall.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HCity2TownHall, self).__init__(name='HCity2TownHall', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """City2TownHall"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'City2TownHall')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["attr1"] = """City2TownHall"""
        
        # match class City() node
        self.add_node()
        
        self.vs[3]["mm__"] = """City""" 
        self.vs[3]["attr1"] = """+""" 
        
        
        # apply class TownHall() node
        self.add_node()

        self.vs[4]["mm__"] = """TownHall""" 
        self.vs[4]["attr1"] = """1"""
        # apply class Committee() node
        self.add_node()

        self.vs[5]["mm__"] = """Committee""" 
        self.vs[5]["attr1"] = """1"""
        
        
        
        # apply association TownHall--committee-->Committee node
        self.add_node()
        self.vs[6]["attr1"] = """committee"""
        self.vs[6]["mm__"] = """directLink_T"""
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class City()
                (1,4), # applymodel -> -> apply_class TownHall()
                (1,5), # applymodel -> -> apply_class Committee()
                (4,6), # apply_class TownHall() -> association committee
                (6,5), # association committee  -> apply_class Committee()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((4,'name'),('concat',((3,'name'),('constant',' TownHall')))), ((5,'name'),('concat',((3,'name'),('constant',' TownHall Committee')))), ]

        
