from core.himesis import Himesis
import uuid

class HMapPartition(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule MapPartition.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HMapPartition, self).__init__(name='HMapPartition', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """MapPartition"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'MapPartition')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
 
        
        # match class Partition() node
        self.add_node()

        self.vs[3]["mm__"] = """Partition""" 
        self.vs[3]["attr1"] = """+""" 
        # match_contains node for class Partition()
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        # match class PhysicalNode() node
        self.add_node()

        self.vs[5]["mm__"] = """PhysicalNode""" 
        self.vs[5]["attr1"] = """1""" 
        # match_contains node for class PhysicalNode()
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        # match class Module() node
        self.add_node()

        self.vs[7]["mm__"] = """Module""" 
        self.vs[7]["attr1"] = """1""" 
        # match_contains node for class Module()
        self.add_node()
        self.vs[8]["mm__"] = """match_contains"""
        
        
        # apply class SwcToEcuMapping() node
        self.add_node()

        self.vs[9]["mm__"] = """SwcToEcuMapping""" 
        self.vs[9]["attr1"] = """1"""
        # apply_contains node for class SwcToEcuMapping()
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        
        
        # match association PhysicalNode--partition-->Partition node
        self.add_node()
        self.vs[11]["attr1"] = """partition"""
        self.vs[11]["mm__"] = """directLink_S"""
        # match association Partition--module-->Module node
        self.add_node()
        self.vs[12]["attr1"] = """module"""
        self.vs[12]["mm__"] = """directLink_S"""
        
        
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class Partition()
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class PhysicalNode()
                (0,8), # matchmodel -> match_contains
                (8,7), # match_contains -> match_class Module()
                (1,10), # applymodel -> apply_contains
                (10,9), # apply_contains -> apply_class SwcToEcuMapping()
                (5,11), # match_class PhysicalNode() -> association partition
                (11,3), # association partition  -> match_class Partition()
                (3,12), # match_class Partition() -> association module
                (12,7), # association module  -> match_class Module()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((9,'shortName'),('concat',(('constant','Swc2EcuMapping_'),(3,'name')))), ]

        
