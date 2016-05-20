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
        self.vs[2]["attr1"] = """MapModule"""
        
        # match class Module() node
        self.add_node()
        
        self.vs[3]["mm__"] = """Module""" 
        self.vs[3]["attr1"] = """+""" 
        # match class Partition() node
        self.add_node()
        
        self.vs[4]["mm__"] = """Partition""" 
        self.vs[4]["attr1"] = """1""" 
        # match class PhysicalNode() node
        self.add_node()
        
        self.vs[5]["mm__"] = """PhysicalNode""" 
        self.vs[5]["attr1"] = """1""" 
        
        
        # apply class SwCompToEcuMapping_component() node
        self.add_node()

        self.vs[6]["mm__"] = """SwCompToEcuMapping_component""" 
        self.vs[6]["attr1"] = """1"""
        # apply class ComponentPrototype() node
        self.add_node()

        self.vs[7]["mm__"] = """ComponentPrototype""" 
        self.vs[7]["attr1"] = """1"""
        
        
        # match association PhysicalNode--partition-->Partition node
        self.add_node()
        self.vs[8]["attr1"] = """partition"""
        self.vs[8]["mm__"] = """directLink_S"""
        # match association Partition--module-->Module node
        self.add_node()
        self.vs[9]["attr1"] = """module"""
        self.vs[9]["mm__"] = """directLink_S"""
        
        # apply association SwCompToEcuMapping_component--componentPrototype-->ComponentPrototype node
        self.add_node()
        self.vs[10]["attr1"] = """componentPrototype"""
        self.vs[10]["mm__"] = """directLink_T"""
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class Module()
                (0,4), # matchmodel -> match_class Partition()
                (0,5), # matchmodel -> match_class PhysicalNode()
                (1,6), # applymodel -> -> apply_class SwCompToEcuMapping_component()
                (1,7), # applymodel -> -> apply_class ComponentPrototype()
                (5,8), # match_class PhysicalNode() -> association partition
                (8,4), # association partition  -> match_class Partition()
                (4,9), # match_class Partition() -> association module
                (9,3), # association module  -> match_class Module()
                (6,10), # apply_class SwCompToEcuMapping_component() -> association componentPrototype
                (10,7), # association componentPrototype  -> apply_class ComponentPrototype()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((6,'ApplyAttribute'),('constant','solveRef')), ((7,'shortName'),(3,'name')), ]

        
