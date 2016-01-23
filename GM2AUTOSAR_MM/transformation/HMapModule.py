from core.himesis import Himesis
import uuid

class HMapModule(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule MapModule.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HMapModule, self).__init__(name='HMapModule', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """MapModule"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'MapModule')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
 
        
        # match class Module() node
        self.add_node()

        self.vs[3]["mm__"] = """Module""" 
        self.vs[3]["attr1"] = """+""" 
        # match_contains node for class Module()
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        # match class Partition() node
        self.add_node()

        self.vs[5]["mm__"] = """Partition""" 
        self.vs[5]["attr1"] = """1""" 
        # match_contains node for class Partition()
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        # match class PhysicalNode() node
        self.add_node()

        self.vs[7]["mm__"] = """PhysicalNode""" 
        self.vs[7]["attr1"] = """1""" 
        # match_contains node for class PhysicalNode()
        self.add_node()
        self.vs[8]["mm__"] = """match_contains"""
        
        
        # apply class SwCompToEcuMapping_component() node
        self.add_node()

        self.vs[9]["mm__"] = """SwCompToEcuMapping_component""" 
        self.vs[9]["attr1"] = """1"""
        # apply_contains node for class SwCompToEcuMapping_component()
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        # apply class ComponentPrototype() node
        self.add_node()

        self.vs[11]["mm__"] = """ComponentPrototype""" 
        self.vs[11]["attr1"] = """1"""
        # apply_contains node for class ComponentPrototype()
        self.add_node()
        self.vs[12]["mm__"] = """apply_contains"""
        
        
        # match association PhysicalNode--partition-->Partition node
        self.add_node()
        self.vs[13]["attr1"] = """partition"""
        self.vs[13]["mm__"] = """directLink_S"""
        # match association Partition--module-->Module node
        self.add_node()
        self.vs[14]["attr1"] = """module"""
        self.vs[14]["mm__"] = """directLink_S"""
        
        # apply association SwCompToEcuMapping_component--componentPrototype-->ComponentPrototype node
        self.add_node()
        self.vs[15]["attr1"] = """componentPrototype"""
        self.vs[15]["mm__"] = """directLink_T"""
        
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class Module()
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class Partition()
                (0,8), # matchmodel -> match_contains
                (8,7), # match_contains -> match_class PhysicalNode()
                (1,10), # applymodel -> apply_contains
                (10,9), # apply_contains -> apply_class SwCompToEcuMapping_component()
                (1,12), # applymodel -> apply_contains
                (12,11), # apply_contains -> apply_class ComponentPrototype()
                (7,13), # match_class PhysicalNode() -> association partition
                (13,5), # association partition  -> match_class Partition()
                (5,14), # match_class Partition() -> association module
                (14,3), # association module  -> match_class Module()
                (9,15), # apply_class SwCompToEcuMapping_component() -> association componentPrototype
                (15,11), # association componentPrototype  -> apply_class ComponentPrototype()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((9,'ApplyAttribute'),('constant','solveRef')), ((11,'shortName'),(3,'name')), ]

        
