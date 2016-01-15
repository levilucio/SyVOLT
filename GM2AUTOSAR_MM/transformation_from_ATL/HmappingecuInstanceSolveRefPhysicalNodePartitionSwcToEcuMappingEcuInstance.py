from core.himesis import Himesis
import uuid

class HmappingecuInstanceSolveRefPhysicalNodePartitionSwcToEcuMappingEcuInstance(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule mappingecuInstanceSolveRefPhysicalNodePartitionSwcToEcuMappingEcuInstance.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HmappingecuInstanceSolveRefPhysicalNodePartitionSwcToEcuMappingEcuInstance, self).__init__(name='HmappingecuInstanceSolveRefPhysicalNodePartitionSwcToEcuMappingEcuInstance', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """mappingecuInstanceSolveRefPhysicalNodePartitionSwcToEcuMappingEcuInstance"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'mappingecuInstanceSolveRefPhysicalNodePartitionSwcToEcuMappingEcuInstance')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
 
        
        # match class PhysicalNode() node
        self.add_node()

        self.vs[3]["mm__"] = """PhysicalNode""" 
        self.vs[3]["attr1"] = """+""" 
        # match_contains node for class PhysicalNode()
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        # match class Partition() node
        self.add_node()

        self.vs[5]["mm__"] = """Partition""" 
        self.vs[5]["attr1"] = """+""" 
        # match_contains node for class Partition()
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        
        
        # apply class SwcToEcuMapping() node
        self.add_node()

        self.vs[7]["mm__"] = """SwcToEcuMapping""" 
        self.vs[7]["attr1"] = """1"""
        # apply_contains node for class SwcToEcuMapping()
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        # apply class EcuInstance() node
        self.add_node()

        self.vs[9]["mm__"] = """EcuInstance""" 
        self.vs[9]["attr1"] = """1"""
        # apply_contains node for class EcuInstance()
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        
        
        # match association PhysicalNode--partition-->Partition node
        self.add_node()
        self.vs[11]["attr1"] = """partition"""
        self.vs[11]["mm__"] = """directLink_S"""
        
        # apply association SwcToEcuMapping--ecuInstance-->EcuInstance node
        self.add_node()
        self.vs[12]["attr1"] = """ecuInstance"""
        self.vs[12]["mm__"] = """directLink_T"""
        
        # backward association PhysicalNode---->EcuInstance node
        self.add_node()

        self.vs[13]["mm__"] = """backward_link"""
        # backward association Partition---->SwcToEcuMapping node
        self.add_node()

        self.vs[14]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class PhysicalNode()
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class Partition()
                (1,8), # applymodel -> apply_contains
                (8,7), # apply_contains -> apply_class SwcToEcuMapping()
                (1,10), # applymodel -> apply_contains
                (10,9), # apply_contains -> apply_class EcuInstance()
                (3,11), # match_class PhysicalNode() -> association partition
                (11,5), # association partition  -> match_class Partition()
                (7,12), # apply_class SwcToEcuMapping() -> association ecuInstance
                (12,9), # association ecuInstance  -> apply_class EcuInstance()
                (9,13), # apply_class EcuInstance() -> backward_association
                (13,3), #  backward_association -> apply_class PhysicalNode()
                (7,14), # apply_class SwcToEcuMapping() -> backward_association
                (14,5), #  backward_association -> apply_class Partition()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((7,'ApplyAttribute'),('constant','solveRef')), ((9,'ApplyAttribute'),('constant','solveRef')), ]

        
