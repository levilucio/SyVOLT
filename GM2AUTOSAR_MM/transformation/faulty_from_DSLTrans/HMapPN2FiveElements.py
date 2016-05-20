from core.himesis import Himesis
import uuid

class HMapPN2FiveElements(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule MapPN2FiveElements.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HMapPN2FiveElements, self).__init__(name='HMapPN2FiveElements', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """MapPN2FiveElements"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'MapPN2FiveElements')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["attr1"] = """MapPN2FiveElements"""
        
        # match class PhysicalNode() node
        self.add_node()
        
        self.vs[3]["mm__"] = """PhysicalNode""" 
        self.vs[3]["attr1"] = """+""" 
        
        
        # apply class SystemMapping() node
        self.add_node()

        self.vs[4]["mm__"] = """SystemMapping""" 
        self.vs[4]["attr1"] = """1"""
        # apply class System() node
        self.add_node()

        self.vs[5]["mm__"] = """System""" 
        self.vs[5]["attr1"] = """1"""
        # apply class SoftwareComposition() node
        self.add_node()

        self.vs[6]["mm__"] = """SoftwareComposition""" 
        self.vs[6]["attr1"] = """1"""
        # apply class CompositionType() node
        self.add_node()

        self.vs[7]["mm__"] = """CompositionType""" 
        self.vs[7]["attr1"] = """1"""
        # apply class EcuInstance() node
        self.add_node()

        self.vs[8]["mm__"] = """EcuInstance""" 
        self.vs[8]["attr1"] = """1"""
        
        
        
        # apply association System--mapping-->SystemMapping node
        self.add_node()
        self.vs[9]["attr1"] = """mapping"""
        self.vs[9]["mm__"] = """directLink_T"""
        # apply association System--softwareComposition-->SoftwareComposition node
        self.add_node()
        self.vs[10]["attr1"] = """softwareComposition"""
        self.vs[10]["mm__"] = """directLink_T"""
        # apply association SoftwareComposition--softwareComposition-->CompositionType node
        self.add_node()
        self.vs[11]["attr1"] = """softwareComposition"""
        self.vs[11]["mm__"] = """directLink_T"""
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class PhysicalNode()
                (1,4), # applymodel -> -> apply_class SystemMapping()
                (1,5), # applymodel -> -> apply_class System()
                (1,6), # applymodel -> -> apply_class SoftwareComposition()
                (1,7), # applymodel -> -> apply_class CompositionType()
                (1,8), # applymodel -> -> apply_class EcuInstance()
                (5,9), # apply_class System() -> association mapping
                (9,4), # association mapping  -> apply_class SystemMapping()
                (5,10), # apply_class System() -> association softwareComposition
                (10,6), # association softwareComposition  -> apply_class SoftwareComposition()
                (6,11), # apply_class SoftwareComposition() -> association softwareComposition
                (11,7), # association softwareComposition  -> apply_class CompositionType()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((4,'shortName'),('concat',(('constant','SysMapping_'),(3,'name')))), ((5,'shortName'),('concat',(('constant','SysTemplate_'),(3,'name')))), ((6,'shortName'),('concat',(('constant','SoftwareComposition_'),(3,'name')))), ((7,'shortName'),('concat',(('constant','CompositionType_'),(3,'name')))), ((8,'shortName'),('concat',(('constant','EcuInstance_'),(3,'name')))), ]

        
