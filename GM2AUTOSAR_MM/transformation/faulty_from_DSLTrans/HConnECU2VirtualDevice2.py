from core.himesis import Himesis
import uuid

class HConnECU2VirtualDevice2(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule ConnECU2VirtualDevice2.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HConnECU2VirtualDevice2, self).__init__(name='HConnECU2VirtualDevice2', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """ConnECU2VirtualDevice2"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConnECU2VirtualDevice2')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["attr1"] = """ConnECU2VirtualDevice2"""
        
        # match class PhysicalNode() node
        self.add_node()
        
        self.vs[3]["mm__"] = """PhysicalNode""" 
        self.vs[3]["attr1"] = """+""" 
        # match class Partition() node
        self.add_node()
        
        self.vs[4]["mm__"] = """Partition""" 
        self.vs[4]["attr1"] = """+""" 
        
        
        # apply class SwcToEcuMapping() node
        self.add_node()

        self.vs[5]["mm__"] = """SwcToEcuMapping""" 
        self.vs[5]["attr1"] = """1"""
        # apply class EcuInstance() node
        self.add_node()

        self.vs[6]["mm__"] = """EcuInstance""" 
        self.vs[6]["attr1"] = """1"""
        
        
        # match association PhysicalNode--partition-->Partition node
        self.add_node()
        self.vs[7]["attr1"] = """partition"""
        self.vs[7]["mm__"] = """directLink_S"""
        
        # apply association SwcToEcuMapping--ecuInstance-->EcuInstance node
        self.add_node()
        self.vs[8]["attr1"] = """ecuInstance"""
        self.vs[8]["mm__"] = """directLink_T"""
        
        # backward association PhysicalNode---->EcuInstance node
        self.add_node()

        self.vs[9]["mm__"] = """backward_link"""
        # backward association Partition---->SwcToEcuMapping node
        self.add_node()

        self.vs[10]["mm__"] = """backward_link"""
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class PhysicalNode()
                (0,4), # matchmodel -> match_class Partition()
                (1,5), # applymodel -> -> apply_class SwcToEcuMapping()
                (1,6), # applymodel -> -> apply_class EcuInstance()
                (3,7), # match_class PhysicalNode() -> association partition
                (7,4), # association partition  -> match_class Partition()
                (5,8), # apply_class SwcToEcuMapping() -> association ecuInstance
                (8,6), # association ecuInstance  -> apply_class EcuInstance()
                (6,9), # apply_class EcuInstance() -> backward_association
                (9,3), #  backward_association -> apply_class PhysicalNode()
                (5,10), # apply_class SwcToEcuMapping() -> backward_association
                (10,4), #  backward_association -> apply_class Partition()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((5,'ApplyAttribute'),('constant','solveRef')), ((6,'ApplyAttribute'),('constant','solveRef')), ]

        
