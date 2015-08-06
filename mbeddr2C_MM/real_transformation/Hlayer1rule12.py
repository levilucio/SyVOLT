from core.himesis import Himesis
import uuid

class Hlayer1rule12(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule layer1rule12.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer1rule12, self).__init__(name='Hlayer1rule12', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """layer1rule12"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule12')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["rulename"] = """layer1rule12"""
        
        # match class ImplementationModule(layer1rule12class0) node
        self.add_node()
        self.vs[3]["name"] = """layer1rule12class0""" 
        self.vs[3]["classtype"] = """ImplementationModule"""
        self.vs[3]["mm__"] = """ImplementationModule"""
        self.vs[3]["cardinality"] = """+""" 
        # match_contains node for class ImplementationModule(layer1rule12class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        # match class AtomicComponent(layer1rule12class4) node
        self.add_node()
        self.vs[5]["name"] = """layer1rule12class4""" 
        self.vs[5]["classtype"] = """AtomicComponent"""
        self.vs[5]["mm__"] = """AtomicComponent"""
        self.vs[5]["cardinality"] = """+""" 
        # match_contains node for class AtomicComponent(layer1rule12class4)
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        # match class ProvidedPort(layer1rule12class5) node
        self.add_node()
        self.vs[7]["name"] = """layer1rule12class5""" 
        self.vs[7]["classtype"] = """ProvidedPort"""
        self.vs[7]["mm__"] = """ProvidedPort"""
        self.vs[7]["cardinality"] = """+""" 
        # match_contains node for class ProvidedPort(layer1rule12class5)
        self.add_node()
        self.vs[8]["mm__"] = """match_contains"""
        # match class ClientServerInterface(layer1rule12class6) node
        self.add_node()
        self.vs[9]["name"] = """layer1rule12class6""" 
        self.vs[9]["classtype"] = """ClientServerInterface"""
        self.vs[9]["mm__"] = """ClientServerInterface"""
        self.vs[9]["cardinality"] = """+""" 
        # match_contains node for class ClientServerInterface(layer1rule12class6)
        self.add_node()
        self.vs[10]["mm__"] = """match_contains"""
        # match class Operation(layer1rule12class7) node
        self.add_node()
        self.vs[11]["name"] = """layer1rule12class7""" 
        self.vs[11]["classtype"] = """Operation"""
        self.vs[11]["mm__"] = """Operation"""
        self.vs[11]["cardinality"] = """+""" 
        # match_contains node for class Operation(layer1rule12class7)
        self.add_node()
        self.vs[12]["mm__"] = """match_contains"""
        
        
        # apply class ImplementationModule(layer1rule12class1) node
        self.add_node()
        self.vs[13]["name"] = """layer1rule12class1""" 
        self.vs[13]["classtype"] = """ImplementationModule"""
        self.vs[13]["mm__"] = """ImplementationModule"""
        self.vs[13]["cardinality"] = """1"""
        # apply_contains node for class ImplementationModule(layer1rule12class1)
        self.add_node()
        self.vs[14]["mm__"] = """apply_contains"""
        # apply class FunctionPrototype(layer1rule12class2) node
        self.add_node()
        self.vs[15]["name"] = """layer1rule12class2""" 
        self.vs[15]["classtype"] = """FunctionPrototype"""
        self.vs[15]["mm__"] = """FunctionPrototype"""
        self.vs[15]["cardinality"] = """1"""
        # apply_contains node for class FunctionPrototype(layer1rule12class2)
        self.add_node()
        self.vs[16]["mm__"] = """apply_contains"""
        
        
        # match association ImplementationModule--contents-->AtomicComponent node
        self.add_node()
        self.vs[17]["associationType"] = """contents"""
        self.vs[17]["mm__"] = """directLink_S"""
        # match association AtomicComponent--contents-->ProvidedPort node
        self.add_node()
        self.vs[18]["associationType"] = """contents"""
        self.vs[18]["mm__"] = """directLink_S"""
        # match association ProvidedPort--intf-->ClientServerInterface node
        self.add_node()
        self.vs[19]["associationType"] = """intf"""
        self.vs[19]["mm__"] = """directLink_S"""
        # match association ClientServerInterface--contents-->Operation node
        self.add_node()
        self.vs[20]["associationType"] = """contents"""
        self.vs[20]["mm__"] = """directLink_S"""
        
        # apply association ImplementationModule--contents-->FunctionPrototype node
        self.add_node()
        self.vs[21]["associationType"] = """contents"""
        self.vs[21]["mm__"] = """directLink_T"""
        
        # backward association ImplementationModule---->ImplementationModule node
        self.add_node()
        self.vs[22]["type"] = """ruleDef"""
        self.vs[22]["mm__"] = """backward_link"""
        # backward association Operation---->FunctionPrototype node
        self.add_node()
        self.vs[23]["type"] = """ruleDef"""
        self.vs[23]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class ImplementationModule(layer1rule12class0)
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class AtomicComponent(layer1rule12class4)
                (0,8), # matchmodel -> match_contains
                (8,7), # match_contains -> match_class ProvidedPort(layer1rule12class5)
                (0,10), # matchmodel -> match_contains
                (10,9), # match_contains -> match_class ClientServerInterface(layer1rule12class6)
                (0,12), # matchmodel -> match_contains
                (12,11), # match_contains -> match_class Operation(layer1rule12class7)
                (1,14), # applymodel -> apply_contains
                (14,13), # apply_contains -> apply_class ImplementationModule(layer1rule12class1)
                (1,16), # applymodel -> apply_contains
                (16,15), # apply_contains -> apply_class FunctionPrototype(layer1rule12class2)
                (3,17), # match_class ImplementationModule(layer1rule12class0) -> association contents
                (17,5), # association contents  -> match_class AtomicComponent(layer1rule12class4)
                (5,18), # match_class AtomicComponent(layer1rule12class4) -> association contents
                (18,7), # association contents  -> match_class ProvidedPort(layer1rule12class5)
                (7,19), # match_class ProvidedPort(layer1rule12class5) -> association intf
                (19,9), # association intf  -> match_class ClientServerInterface(layer1rule12class6)
                (9,20), # match_class ClientServerInterface(layer1rule12class6) -> association contents
                (20,11), # association contents  -> match_class Operation(layer1rule12class7)
                (13,21), # apply_class ImplementationModule(layer1rule12class1) -> association contents
                (21,15), # association contents  -> apply_class FunctionPrototype(layer1rule12class2)
                (13,22), # apply_class ImplementationModule(layer1rule12class1) -> backward_association
                (22,3), #  backward_association -> apply_class ImplementationModule(layer1rule12class0)
                (15,23), # apply_class FunctionPrototype(layer1rule12class2) -> backward_association
                (23,11), #  backward_association -> apply_class Operation(layer1rule12class7)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])
		
        # Add the attribute equations
        self["equations"] = [((13,'__ApplyAttribute'),('constant','ImplementationModule')), ((15,'__ApplyAttribute'),('constant','ProvidedPortFunctionPrototype')), ]

        
