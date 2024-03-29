from core.himesis import Himesis
import uuid

class HmappingcomponentSolveRefPartitionModuleSwcToEcuMappingSwCompToEcuMappingcomponent(Himesis):
    def __init__(self, *args, **kwargs):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule mappingcomponentSolveRefPartitionModuleSwcToEcuMappingSwCompToEcuMappingcomponent.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HmappingcomponentSolveRefPartitionModuleSwcToEcuMappingSwCompToEcuMappingcomponent, self).__init__(name='HmappingcomponentSolveRefPartitionModuleSwcToEcuMappingSwCompToEcuMappingcomponent', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """mappingcomponentSolveRefPartitionModuleSwcToEcuMappingSwCompToEcuMappingcomponent"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'mappingcomponentSolveRefPartitionModuleSwcToEcuMappingSwCompToEcuMappingcomponent')
        
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
        # match class Module() node
        self.add_node()

        self.vs[5]["mm__"] = """Module""" 
        self.vs[5]["attr1"] = """+""" 
        # match_contains node for class Module()
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        
        
        # apply class SwcToEcuMapping() node
        self.add_node()

        self.vs[7]["mm__"] = """SwcToEcuMapping""" 
        self.vs[7]["attr1"] = """1"""
        # apply_contains node for class SwcToEcuMapping()
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        # apply class SwCompToEcuMapping_component() node
        self.add_node()

        self.vs[9]["mm__"] = """SwCompToEcuMapping_component""" 
        self.vs[9]["attr1"] = """1"""
        # apply_contains node for class SwCompToEcuMapping_component()
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        
        
        # match association Partition--module-->Module node
        self.add_node()
        self.vs[11]["attr1"] = """module"""
        self.vs[11]["mm__"] = """directLink_S"""
        
        # apply association SwcToEcuMapping--component-->SwCompToEcuMapping_component node
        self.add_node()
        self.vs[12]["attr1"] = """component"""
        self.vs[12]["mm__"] = """directLink_T"""
        
        # backward association Partition---->SwcToEcuMapping node
        self.add_node()

        self.vs[13]["mm__"] = """backward_link"""
        # backward association Module---->SwCompToEcuMapping_component node
        self.add_node()

        self.vs[14]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class Partition()
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class Module()
                (1,8), # applymodel -> apply_contains
                (8,7), # apply_contains -> apply_class SwcToEcuMapping()
                (1,10), # applymodel -> apply_contains
                (10,9), # apply_contains -> apply_class SwCompToEcuMapping_component()
                (3,11), # match_class Partition() -> association module
                (11,5), # association module  -> match_class Module()
                (7,12), # apply_class SwcToEcuMapping() -> association component
                (12,9), # association component  -> apply_class SwCompToEcuMapping_component()
                (7,13), # apply_class SwcToEcuMapping() -> backward_association
                (13,3), #  backward_association -> apply_class Partition()
                (9,14), # apply_class SwCompToEcuMapping_component() -> backward_association
                (14,5), #  backward_association -> apply_class Module()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((7,'ApplyAttribute'),('constant','solveRef')), ((9,'ApplyAttribute'),('constant','solveRef')), ]

        
