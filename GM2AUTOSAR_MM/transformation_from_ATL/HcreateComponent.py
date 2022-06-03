from core.himesis import Himesis
import uuid

class HcreateComponent(Himesis):
    def __init__(self, *args, **kwargs):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule createComponent.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HcreateComponent, self).__init__(name='HcreateComponent', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """createComponent"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'createComponent')
        
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
        
        
        # apply class SwCompToEcuMapping_component() node
        self.add_node()

        self.vs[5]["mm__"] = """SwCompToEcuMapping_component""" 
        self.vs[5]["attr1"] = """1"""
        # apply_contains node for class SwCompToEcuMapping_component()
        self.add_node()
        self.vs[6]["mm__"] = """apply_contains"""
        # apply class ComponentPrototype() node
        self.add_node()

        self.vs[7]["mm__"] = """ComponentPrototype""" 
        self.vs[7]["attr1"] = """1"""
        # apply_contains node for class ComponentPrototype()
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        
        
        
        # apply association SwCompToEcuMapping_component--componentPrototype-->ComponentPrototype node
        self.add_node()
        self.vs[9]["attr1"] = """componentPrototype"""
        self.vs[9]["mm__"] = """directLink_T"""
        
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class Module()
                (1,6), # applymodel -> apply_contains
                (6,5), # apply_contains -> apply_class SwCompToEcuMapping_component()
                (1,8), # applymodel -> apply_contains
                (8,7), # apply_contains -> apply_class ComponentPrototype()
                (5,9), # apply_class SwCompToEcuMapping_component() -> association componentPrototype
                (9,7), # association componentPrototype  -> apply_class ComponentPrototype()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((5,'ApplyAttribute'),('constant','solveRef')), ((7,'shortName'),(3,'name')), ((7,'ApplyAttribute'),('constant','solveRef')), ]

        
