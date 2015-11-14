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
 
        
        # match class City() node
        self.add_node()

        self.vs[3]["mm__"] = """City""" 
        self.vs[3]["attr1"] = """+""" 
        # match_contains node for class City()
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        
        
        # apply class TownHall() node
        self.add_node()

        self.vs[5]["mm__"] = """TownHall""" 
        self.vs[5]["attr1"] = """1"""
        # apply_contains node for class TownHall()
        self.add_node()
        self.vs[6]["mm__"] = """apply_contains"""
        # apply class Committee() node
        self.add_node()

        self.vs[7]["mm__"] = """Committee""" 
        self.vs[7]["attr1"] = """1"""
        # apply_contains node for class Committee()
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        
        
        
        # apply association TownHall--committee-->Committee node
        self.add_node()
        self.vs[9]["attr1"] = """committee"""
        self.vs[9]["mm__"] = """directLink_T"""
        
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class City()
                (1,6), # applymodel -> apply_contains
                (6,5), # apply_contains -> apply_class TownHall()
                (1,8), # applymodel -> apply_contains
                (8,7), # apply_contains -> apply_class Committee()
                (5,9), # apply_class TownHall() -> association committee
                (9,7), # association committee  -> apply_class Committee()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((5,'name'),('concat',((3,'name'),('constant',' TownHall')))), ((5,'ApplyAttribute'),('constant','solveRef')), ((7,'name'),('concat',((3,'name'),('constant',' TownHall Committee')))), ((7,'ApplyAttribute'),('constant','solveRef')), ]

        
