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
 
        
        # match class AtomicComponent(layer1rule9class0) node
        self.add_node()
        self.vs[3]["name"] = """layer1rule9class0""" 
        self.vs[3]["classtype"] = """AtomicComponent"""
        self.vs[3]["mm__"] = """AtomicComponent"""
        self.vs[3]["cardinality"] = """+""" 
        # match_contains node for class AtomicComponent(layer1rule9class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        # match class ImplementationModule(layer1rule9class5) node
        self.add_node()
        self.vs[5]["name"] = """layer1rule9class5""" 
        self.vs[5]["classtype"] = """ImplementationModule"""
        self.vs[5]["mm__"] = """ImplementationModule"""
        self.vs[5]["cardinality"] = """+""" 
        # match_contains node for class ImplementationModule(layer1rule9class5)
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        
        
        # apply class StructDeclaration(layer1rule9class1) node
        self.add_node()
        self.vs[7]["name"] = """layer1rule9class1""" 
        self.vs[7]["classtype"] = """StructDeclaration"""
        self.vs[7]["mm__"] = """StructDeclaration"""
        self.vs[7]["cardinality"] = """1"""
        # apply_contains node for class StructDeclaration(layer1rule9class1)
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        # apply class StructType(layer1rule9class2) node
        self.add_node()
        self.vs[9]["name"] = """layer1rule9class2""" 
        self.vs[9]["classtype"] = """StructType"""
        self.vs[9]["mm__"] = """StructType"""
        self.vs[9]["cardinality"] = """1"""
        # apply_contains node for class StructType(layer1rule9class2)
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        
        
        # match association ImplementationModule--contents-->AtomicComponent node
        self.add_node()
        self.vs[11]["associationType"] = """contents"""
        self.vs[11]["mm__"] = """directLink_S"""
        
        # apply association StructType--struct-->StructDeclaration node
        self.add_node()
        self.vs[12]["associationType"] = """struct"""
        self.vs[12]["mm__"] = """directLink_T"""
        
        # backward association ImplementationModule---->StructType node
        self.add_node()
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["mm__"] = """backward_link"""
        # backward association AtomicComponent---->StructDeclaration node
        self.add_node()
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class AtomicComponent(layer1rule9class0)
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class ImplementationModule(layer1rule9class5)
                (1,8), # applymodel -> apply_contains
                (8,7), # apply_contains -> apply_class StructDeclaration(layer1rule9class1)
                (1,10), # applymodel -> apply_contains
                (10,9), # apply_contains -> apply_class StructType(layer1rule9class2)
                (5,11), # match_class ImplementationModule(layer1rule9class5) -> association contents
                (11,3), # association contents  -> match_class AtomicComponent(layer1rule9class0)
                (9,12), # apply_class StructType(layer1rule9class2) -> association struct
                (12,7), # association struct  -> apply_class StructDeclaration(layer1rule9class1)
                (9,13), # apply_class StructType(layer1rule9class2) -> backward_association
                (13,5), #  backward_association -> apply_class ImplementationModule(layer1rule9class5)
                (7,14), # apply_class StructDeclaration(layer1rule9class1) -> backward_association
                (14,3), #  backward_association -> apply_class AtomicComponent(layer1rule9class0)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((7,'__ApplyAttribute'),('constant','AtomicComponentStructCData')), ((9,'__ApplyAttribute'),('constant','TypeComponentStructType')), ]

        
