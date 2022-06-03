from core.himesis import Himesis
import uuid

class HinitSysTemp(Himesis):
    def __init__(self, *args, **kwargs):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule initSysTemp.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HinitSysTemp, self).__init__(name='HinitSysTemp', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """initSysTemp"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'initSysTemp')
        
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
        self.vs[5]["attr1"] = """1""" 
        # match_contains node for class Partition()
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        # match class Module() node
        self.add_node()

        self.vs[7]["mm__"] = """Module""" 
        self.vs[7]["attr1"] = """1""" 
        # match_contains node for class Module()
        self.add_node()
        self.vs[8]["mm__"] = """match_contains"""
        
        
        # apply class SystemMapping() node
        self.add_node()

        self.vs[9]["mm__"] = """SystemMapping""" 
        self.vs[9]["attr1"] = """1"""
        # apply_contains node for class SystemMapping()
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        # apply class System() node
        self.add_node()

        self.vs[11]["mm__"] = """System""" 
        self.vs[11]["attr1"] = """1"""
        # apply_contains node for class System()
        self.add_node()
        self.vs[12]["mm__"] = """apply_contains"""
        # apply class SoftwareComposition() node
        self.add_node()

        self.vs[13]["mm__"] = """SoftwareComposition""" 
        self.vs[13]["attr1"] = """1"""
        # apply_contains node for class SoftwareComposition()
        self.add_node()
        self.vs[14]["mm__"] = """apply_contains"""
        # apply class CompositionType() node
        self.add_node()

        self.vs[15]["mm__"] = """CompositionType""" 
        self.vs[15]["attr1"] = """1"""
        # apply_contains node for class CompositionType()
        self.add_node()
        self.vs[16]["mm__"] = """apply_contains"""
        # apply class EcuInstance() node
        self.add_node()

        self.vs[17]["mm__"] = """EcuInstance""" 
        self.vs[17]["attr1"] = """1"""
        # apply_contains node for class EcuInstance()
        self.add_node()
        self.vs[18]["mm__"] = """apply_contains"""
        
        
        # match association PhysicalNode--partition-->Partition node
        self.add_node()
        self.vs[19]["attr1"] = """partition"""
        self.vs[19]["mm__"] = """directLink_S"""
        # match association Partition--module-->Module node
        self.add_node()
        self.vs[20]["attr1"] = """module"""
        self.vs[20]["mm__"] = """directLink_S"""
        
        # apply association System--mapping-->SystemMapping node
        self.add_node()
        self.vs[21]["attr1"] = """mapping"""
        self.vs[21]["mm__"] = """directLink_T"""
        # apply association System--softwareComposition-->SoftwareComposition node
        self.add_node()
        self.vs[22]["attr1"] = """softwareComposition"""
        self.vs[22]["mm__"] = """directLink_T"""
        # apply association SoftwareComposition--softwareComposition-->CompositionType node
        self.add_node()
        self.vs[23]["attr1"] = """softwareComposition"""
        self.vs[23]["mm__"] = """directLink_T"""
        
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class PhysicalNode()
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class Partition()
                (0,8), # matchmodel -> match_contains
                (8,7), # match_contains -> match_class Module()
                (1,10), # applymodel -> apply_contains
                (10,9), # apply_contains -> apply_class SystemMapping()
                (1,12), # applymodel -> apply_contains
                (12,11), # apply_contains -> apply_class System()
                (1,14), # applymodel -> apply_contains
                (14,13), # apply_contains -> apply_class SoftwareComposition()
                (1,16), # applymodel -> apply_contains
                (16,15), # apply_contains -> apply_class CompositionType()
                (1,18), # applymodel -> apply_contains
                (18,17), # apply_contains -> apply_class EcuInstance()
                (3,19), # match_class PhysicalNode() -> association partition
                (19,5), # association partition  -> match_class Partition()
                (5,20), # match_class Partition() -> association module
                (20,7), # association module  -> match_class Module()
                (11,21), # apply_class System() -> association mapping
                (21,9), # association mapping  -> apply_class SystemMapping()
                (11,22), # apply_class System() -> association softwareComposition
                (22,13), # association softwareComposition  -> apply_class SoftwareComposition()
                (13,23), # apply_class SoftwareComposition() -> association softwareComposition
                (23,15), # association softwareComposition  -> apply_class CompositionType()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((9,'shortName'),('concat',(('constant','SysMapping_'),(3,'name')))), ((9,'ApplyAttribute'),('constant','solveRef')), ((11,'shortName'),('concat',(('constant','SysTemplate_'),(3,'name')))), ((11,'ApplyAttribute'),('constant','solveRef')), ((13,'shortName'),('concat',(('constant','SoftwareComposition_'),(3,'name')))), ((13,'ApplyAttribute'),('constant','solveRef')), ((15,'shortName'),('concat',(('constant','CompositionType_'),(3,'name')))), ((15,'ApplyAttribute'),('constant','solveRef')), ((17,'shortName'),('concat',(('constant','EcuInstance_'),(3,'name')))), ]

        
