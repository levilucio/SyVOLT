from core.himesis import Himesis
import uuid

class Hlayer1rule7(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule layer1rule7.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer1rule7, self).__init__(name='Hlayer1rule7', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """layer1rule7"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule7')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
 
        
        # match class ImplementationModule(layer1rule7class0) node
        self.add_node()

        self.vs[3]["mm__"] = """ImplementationModule""" 
        self.vs[3]["attr1"] = """+""" 
        # match_contains node for class ImplementationModule(layer1rule7class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        # match class AtomicComponent(layer1rule7class1) node
        self.add_node()

        self.vs[5]["mm__"] = """AtomicComponent""" 
        self.vs[5]["attr1"] = """+""" 
        # match_contains node for class AtomicComponent(layer1rule7class1)
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        
        
        # apply class ImplementationModule(layer1rule7class2) node
        self.add_node()

        self.vs[7]["mm__"] = """ImplementationModule""" 
        self.vs[7]["attr1"] = """1"""
        # apply_contains node for class ImplementationModule(layer1rule7class2)
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        # apply class StructDeclaration(layer1rule7class3) node
        self.add_node()

        self.vs[9]["mm__"] = """StructDeclaration""" 
        self.vs[9]["attr1"] = """1"""
        # apply_contains node for class StructDeclaration(layer1rule7class3)
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        
        
        # match association ImplementationModule--contents-->AtomicComponent node
        self.add_node()
        self.vs[11]["attr1"] = """contents"""
        self.vs[11]["mm__"] = """directLink_S"""
        
        # apply association ImplementationModule--contents-->StructDeclaration node
        self.add_node()
        self.vs[12]["attr1"] = """contents"""
        self.vs[12]["mm__"] = """directLink_T"""
        
        # backward association ImplementationModule---->ImplementationModule node
        self.add_node()

        self.vs[13]["mm__"] = """backward_link"""
        # backward association AtomicComponent---->StructDeclaration node
        self.add_node()

        self.vs[14]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class ImplementationModule(layer1rule7class0)
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class AtomicComponent(layer1rule7class1)
                (1,8), # applymodel -> apply_contains
                (8,7), # apply_contains -> apply_class ImplementationModule(layer1rule7class2)
                (1,10), # applymodel -> apply_contains
                (10,9), # apply_contains -> apply_class StructDeclaration(layer1rule7class3)
                (3,11), # match_class ImplementationModule(layer1rule7class0) -> association contents
                (11,5), # association contents  -> match_class AtomicComponent(layer1rule7class1)
                (7,12), # apply_class ImplementationModule(layer1rule7class2) -> association contents
                (12,9), # association contents  -> apply_class StructDeclaration(layer1rule7class3)
                (7,13), # apply_class ImplementationModule(layer1rule7class2) -> backward_association
                (13,3), #  backward_association -> apply_class ImplementationModule(layer1rule7class0)
                (9,14), # apply_class StructDeclaration(layer1rule7class3) -> backward_association
                (14,5), #  backward_association -> apply_class AtomicComponent(layer1rule7class1)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((7,'__ApplyAttribute'),('constant','ImplementationModule')), ((9,'__ApplyAttribute'),('constant','AtomicComponentStructCData')), ]

        
