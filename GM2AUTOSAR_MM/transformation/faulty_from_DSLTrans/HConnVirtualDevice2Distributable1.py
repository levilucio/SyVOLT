from core.himesis import Himesis
import uuid

class HConnVirtualDevice2Distributable1(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule ConnVirtualDevice2Distributable1.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HConnVirtualDevice2Distributable1, self).__init__(name='HConnVirtualDevice2Distributable1', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """ConnVirtualDevice2Distributable1"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConnVirtualDevice2Distributable1')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["attr1"] = """ConnVirtualDevice2Distributable1"""
        
        # match class PhysicalNode() node
        self.add_node()
        
        self.vs[3]["mm__"] = """PhysicalNode""" 
        self.vs[3]["attr1"] = """+""" 
        # match class Partition() node
        self.add_node()
        
        self.vs[4]["mm__"] = """Partition""" 
        self.vs[4]["attr1"] = """+""" 
        # match class Module() node
        self.add_node()
        
        self.vs[5]["mm__"] = """Module""" 
        self.vs[5]["attr1"] = """+""" 
        
        
        # apply class CompositionType() node
        self.add_node()

        self.vs[6]["mm__"] = """CompositionType""" 
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
        
        # apply association CompositionType--component-->ComponentPrototype node
        self.add_node()
        self.vs[10]["attr1"] = """component"""
        self.vs[10]["mm__"] = """directLink_T"""
        # apply association ComponentPrototype--type-->CompositionType node
        self.add_node()
        self.vs[11]["attr1"] = """type"""
        self.vs[11]["mm__"] = """directLink_T"""
        
        # backward association PhysicalNode---->CompositionType node
        self.add_node()

        self.vs[12]["mm__"] = """backward_link"""
        # backward association Module---->ComponentPrototype node
        self.add_node()

        self.vs[13]["mm__"] = """backward_link"""
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class PhysicalNode()
                (0,4), # matchmodel -> match_class Partition()
                (0,5), # matchmodel -> match_class Module()
                (1,6), # applymodel -> -> apply_class CompositionType()
                (1,7), # applymodel -> -> apply_class ComponentPrototype()
                (3,8), # match_class PhysicalNode() -> association partition
                (8,4), # association partition  -> match_class Partition()
                (4,9), # match_class Partition() -> association module
                (9,5), # association module  -> match_class Module()
                (6,10), # apply_class CompositionType() -> association component
                (10,7), # association component  -> apply_class ComponentPrototype()
                (7,11), # apply_class ComponentPrototype() -> association type
                (11,6), # association type  -> apply_class CompositionType()
                (6,12), # apply_class CompositionType() -> backward_association
                (12,3), #  backward_association -> apply_class PhysicalNode()
                (7,13), # apply_class ComponentPrototype() -> backward_association
                (13,5), #  backward_association -> apply_class Module()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((6,'ApplyAttribute'),('constant','solveRef')), ((7,'ApplyAttribute'),('constant','solveRef')), ]

        
