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
        self.vs[2]["attr1"] = """MapPartition"""
        
        # match class Partition() node
        self.add_node()
        
        self.vs[3]["mm__"] = """Partition""" 
        self.vs[3]["attr1"] = """+""" 
        # match class PhysicalNode() node
        self.add_node()
        
        self.vs[4]["mm__"] = """PhysicalNode""" 
        self.vs[4]["attr1"] = """1""" 
        
        
        # apply class SwcToEcuMapping() node
        self.add_node()

        self.vs[5]["mm__"] = """SwcToEcuMapping""" 
        self.vs[5]["attr1"] = """1"""
        
        
        # match association PhysicalNode--partition-->Partition node
        self.add_node()
        self.vs[6]["attr1"] = """partition"""
        self.vs[6]["mm__"] = """directLink_S"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class Partition()
                (0,4), # matchmodel -> match_class PhysicalNode()
                (1,5), # applymodel -> -> apply_class SwcToEcuMapping()
                (4,6), # match_class PhysicalNode() -> association partition
                (6,3), # association partition  -> match_class Partition()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((5,'shortName'),('concat',(('constant','Swc2EcuMapping_'),(3,'name')))), ]

        
