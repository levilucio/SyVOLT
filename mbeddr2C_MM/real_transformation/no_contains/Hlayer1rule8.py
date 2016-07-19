from core.himesis import Himesis
import uuid

class Hlayer1rule8(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule layer1rule8.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer1rule8, self).__init__(name='Hlayer1rule8', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer1rule8"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule8')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["attr1"] = """layer1rule8"""
        
        # match class ImplementationModule(layer1rule8class0) node
        self.add_node()
        
        self.vs[3]["mm__"] = """ImplementationModule""" 
        self.vs[3]["attr1"] = """+""" 
        # match class AtomicComponent(layer1rule8class1) node
        self.add_node()
        
        self.vs[4]["mm__"] = """AtomicComponent""" 
        self.vs[4]["attr1"] = """+""" 
        
        
        # apply class ImplementationModule(layer1rule8class2) node
        self.add_node()

        self.vs[5]["mm__"] = """ImplementationModule""" 
        self.vs[5]["attr1"] = """1"""
        # apply class TypeDef(layer1rule8class3) node
        self.add_node()

        self.vs[6]["mm__"] = """TypeDef""" 
        self.vs[6]["attr1"] = """1"""
        
        
        # match association ImplementationModule--contents-->AtomicComponent node
        self.add_node()
        self.vs[7]["attr1"] = """contents"""
        self.vs[7]["mm__"] = """directLink_S"""
        
        # apply association ImplementationModule--contents-->TypeDef node
        self.add_node()
        self.vs[8]["attr1"] = """contents"""
        self.vs[8]["mm__"] = """directLink_T"""
        
        # backward association ImplementationModule---->ImplementationModule node
        self.add_node()

        self.vs[9]["mm__"] = """backward_link"""
        # backward association AtomicComponent---->TypeDef node
        self.add_node()

        self.vs[10]["mm__"] = """backward_link"""
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class ImplementationModule(layer1rule8class0)
                (0,4), # matchmodel -> match_class AtomicComponent(layer1rule8class1)
                (1,5), # applymodel -> -> apply_class ImplementationModule(layer1rule8class2)
                (1,6), # applymodel -> -> apply_class TypeDef(layer1rule8class3)
                (3,7), # match_class ImplementationModule(layer1rule8class0) -> association contents
                (7,4), # association contents  -> match_class AtomicComponent(layer1rule8class1)
                (5,8), # apply_class ImplementationModule(layer1rule8class2) -> association contents
                (8,6), # association contents  -> apply_class TypeDef(layer1rule8class3)
                (5,9), # apply_class ImplementationModule(layer1rule8class2) -> backward_association
                (9,3), #  backward_association -> apply_class ImplementationModule(layer1rule8class0)
                (6,10), # apply_class TypeDef(layer1rule8class3) -> backward_association
                (10,4), #  backward_association -> apply_class AtomicComponent(layer1rule8class1)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((5,'__ApplyAttribute'),('constant','ImplementationModule')), ((6,'__ApplyAttribute'),('constant','TypeDefComponentStruct')), ]

        
