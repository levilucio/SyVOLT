from core.himesis import Himesis
import uuid

class Hlayer1rule9(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule layer1rule9.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer1rule9, self).__init__(name='Hlayer1rule9', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer1rule9"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule9')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["attr1"] = """layer1rule9"""
        
        # match class AtomicComponent(layer1rule9class0) node
        self.add_node()
        
        self.vs[3]["mm__"] = """AtomicComponent""" 
        self.vs[3]["attr1"] = """+""" 
        # match class ImplementationModule(layer1rule9class5) node
        self.add_node()
        
        self.vs[4]["mm__"] = """ImplementationModule""" 
        self.vs[4]["attr1"] = """+""" 
        
        
        # apply class StructDeclaration(layer1rule9class1) node
        self.add_node()

        self.vs[5]["mm__"] = """StructDeclaration""" 
        self.vs[5]["attr1"] = """1"""
        # apply class StructType(layer1rule9class2) node
        self.add_node()

        self.vs[6]["mm__"] = """StructType""" 
        self.vs[6]["attr1"] = """1"""
        
        
        # match association ImplementationModule--contents-->AtomicComponent node
        self.add_node()
        self.vs[7]["attr1"] = """contents"""
        self.vs[7]["mm__"] = """directLink_S"""
        
        # apply association StructType--struct-->StructDeclaration node
        self.add_node()
        self.vs[8]["attr1"] = """struct"""
        self.vs[8]["mm__"] = """directLink_T"""
        
        # backward association ImplementationModule---->StructType node
        self.add_node()

        self.vs[9]["mm__"] = """backward_link"""
        # backward association AtomicComponent---->StructDeclaration node
        self.add_node()

        self.vs[10]["mm__"] = """backward_link"""
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class AtomicComponent(layer1rule9class0)
                (0,4), # matchmodel -> match_class ImplementationModule(layer1rule9class5)
                (1,5), # applymodel -> -> apply_class StructDeclaration(layer1rule9class1)
                (1,6), # applymodel -> -> apply_class StructType(layer1rule9class2)
                (4,7), # match_class ImplementationModule(layer1rule9class5) -> association contents
                (7,3), # association contents  -> match_class AtomicComponent(layer1rule9class0)
                (6,8), # apply_class StructType(layer1rule9class2) -> association struct
                (8,5), # association struct  -> apply_class StructDeclaration(layer1rule9class1)
                (6,9), # apply_class StructType(layer1rule9class2) -> backward_association
                (9,4), #  backward_association -> apply_class ImplementationModule(layer1rule9class5)
                (5,10), # apply_class StructDeclaration(layer1rule9class1) -> backward_association
                (10,3), #  backward_association -> apply_class AtomicComponent(layer1rule9class0)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((5,'__ApplyAttribute'),('constant','AtomicComponentStructCData')), ((6,'__ApplyAttribute'),('constant','TypeComponentStructType')), ]

        
