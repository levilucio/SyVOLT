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
        self.vs[2]["attr1"] = """layer1rule12"""
        
        # match class ImplementationModule(layer1rule12class0) node
        self.add_node()
        
        self.vs[3]["mm__"] = """ImplementationModule""" 
        self.vs[3]["attr1"] = """+""" 
        # match class AtomicComponent(layer1rule12class4) node
        self.add_node()
        
        self.vs[4]["mm__"] = """AtomicComponent""" 
        self.vs[4]["attr1"] = """+""" 
        # match class ProvidedPort(layer1rule12class5) node
        self.add_node()
        
        self.vs[5]["mm__"] = """ProvidedPort""" 
        self.vs[5]["attr1"] = """+""" 
        # match class ClientServerInterface(layer1rule12class6) node
        self.add_node()
        
        self.vs[6]["mm__"] = """ClientServerInterface""" 
        self.vs[6]["attr1"] = """+""" 
        # match class Operation(layer1rule12class7) node
        self.add_node()
        
        self.vs[7]["mm__"] = """Operation""" 
        self.vs[7]["attr1"] = """+""" 
        
        
        # apply class ImplementationModule(layer1rule12class1) node
        self.add_node()

        self.vs[8]["mm__"] = """ImplementationModule""" 
        self.vs[8]["attr1"] = """1"""
        # apply class FunctionPrototype(layer1rule12class2) node
        self.add_node()

        self.vs[9]["mm__"] = """FunctionPrototype""" 
        self.vs[9]["attr1"] = """1"""
        
        
        # match association ImplementationModule--contents-->AtomicComponent node
        self.add_node()
        self.vs[10]["attr1"] = """contents"""
        self.vs[10]["mm__"] = """directLink_S"""
        # match association AtomicComponent--contents-->ProvidedPort node
        self.add_node()
        self.vs[11]["attr1"] = """contents"""
        self.vs[11]["mm__"] = """directLink_S"""
        # match association ProvidedPort--intf-->ClientServerInterface node
        self.add_node()
        self.vs[12]["attr1"] = """intf"""
        self.vs[12]["mm__"] = """directLink_S"""
        # match association ClientServerInterface--contents-->Operation node
        self.add_node()
        self.vs[13]["attr1"] = """contents"""
        self.vs[13]["mm__"] = """directLink_S"""
        
        # apply association ImplementationModule--contents-->FunctionPrototype node
        self.add_node()
        self.vs[14]["attr1"] = """contents"""
        self.vs[14]["mm__"] = """directLink_T"""
        
        # backward association ImplementationModule---->ImplementationModule node
        self.add_node()

        self.vs[15]["mm__"] = """backward_link"""
        # backward association Operation---->FunctionPrototype node
        self.add_node()

        self.vs[16]["mm__"] = """backward_link"""
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class ImplementationModule(layer1rule12class0)
                (0,4), # matchmodel -> match_class AtomicComponent(layer1rule12class4)
                (0,5), # matchmodel -> match_class ProvidedPort(layer1rule12class5)
                (0,6), # matchmodel -> match_class ClientServerInterface(layer1rule12class6)
                (0,7), # matchmodel -> match_class Operation(layer1rule12class7)
                (1,8), # applymodel -> -> apply_class ImplementationModule(layer1rule12class1)
                (1,9), # applymodel -> -> apply_class FunctionPrototype(layer1rule12class2)
                (3,10), # match_class ImplementationModule(layer1rule12class0) -> association contents
                (10,4), # association contents  -> match_class AtomicComponent(layer1rule12class4)
                (4,11), # match_class AtomicComponent(layer1rule12class4) -> association contents
                (11,5), # association contents  -> match_class ProvidedPort(layer1rule12class5)
                (5,12), # match_class ProvidedPort(layer1rule12class5) -> association intf
                (12,6), # association intf  -> match_class ClientServerInterface(layer1rule12class6)
                (6,13), # match_class ClientServerInterface(layer1rule12class6) -> association contents
                (13,7), # association contents  -> match_class Operation(layer1rule12class7)
                (8,14), # apply_class ImplementationModule(layer1rule12class1) -> association contents
                (14,9), # association contents  -> apply_class FunctionPrototype(layer1rule12class2)
                (8,15), # apply_class ImplementationModule(layer1rule12class1) -> backward_association
                (15,3), #  backward_association -> apply_class ImplementationModule(layer1rule12class0)
                (9,16), # apply_class FunctionPrototype(layer1rule12class2) -> backward_association
                (16,7), #  backward_association -> apply_class Operation(layer1rule12class7)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((8,'__ApplyAttribute'),('constant','ImplementationModule')), ((9,'__ApplyAttribute'),('constant','ProvidedPortFunctionPrototype')), ]

        
