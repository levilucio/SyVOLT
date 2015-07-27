from core.himesis import Himesis
import uuid

class Hlayer0rule11(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule layer0rule11.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer0rule11, self).__init__(name='Hlayer0rule11', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """layer0rule11"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule11')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["rulename"] = """layer0rule11"""
        
        # match class ProvidedPort(layer0rule11class0) node
        self.add_node()
        self.vs[3]["name"] = """layer0rule11class0""" 
        self.vs[3]["classtype"] = """ProvidedPort"""
        self.vs[3]["mm__"] = """ProvidedPort"""
        self.vs[3]["cardinality"] = """+""" 
        # match_contains node for class ProvidedPort(layer0rule11class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        # match class AtomicComponent(layer0rule11class1) node
        self.add_node()
        self.vs[5]["name"] = """layer0rule11class1""" 
        self.vs[5]["classtype"] = """AtomicComponent"""
        self.vs[5]["mm__"] = """AtomicComponent"""
        self.vs[5]["cardinality"] = """+""" 
        # match_contains node for class AtomicComponent(layer0rule11class1)
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        # match class ClientServerInterface(layer0rule11class2) node
        self.add_node()
        self.vs[7]["name"] = """layer0rule11class2""" 
        self.vs[7]["classtype"] = """ClientServerInterface"""
        self.vs[7]["mm__"] = """ClientServerInterface"""
        self.vs[7]["cardinality"] = """+""" 
        # match_contains node for class ClientServerInterface(layer0rule11class2)
        self.add_node()
        self.vs[8]["mm__"] = """match_contains"""
        # match class Operation(layer0rule11class3) node
        self.add_node()
        self.vs[9]["name"] = """layer0rule11class3""" 
        self.vs[9]["classtype"] = """Operation"""
        self.vs[9]["mm__"] = """Operation"""
        self.vs[9]["cardinality"] = """+""" 
        # match_contains node for class Operation(layer0rule11class3)
        self.add_node()
        self.vs[10]["mm__"] = """match_contains"""
        # match class ImplementationModule(layer0rule11class4) node
        self.add_node()
        self.vs[11]["name"] = """layer0rule11class4""" 
        self.vs[11]["classtype"] = """ImplementationModule"""
        self.vs[11]["mm__"] = """ImplementationModule"""
        self.vs[11]["cardinality"] = """+""" 
        # match_contains node for class ImplementationModule(layer0rule11class4)
        self.add_node()
        self.vs[12]["mm__"] = """match_contains"""
        
        
        # apply class FunctionPrototype(layer0rule11class5) node
        self.add_node()
        self.vs[13]["name"] = """layer0rule11class5""" 
        self.vs[13]["classtype"] = """FunctionPrototype"""
        self.vs[13]["mm__"] = """FunctionPrototype"""
        self.vs[13]["cardinality"] = """1"""
        # apply_contains node for class FunctionPrototype(layer0rule11class5)
        self.add_node()
        self.vs[14]["mm__"] = """apply_contains"""
        
        
        # match association AtomicComponent--contents-->ProvidedPort node
        self.add_node()
        self.vs[15]["associationType"] = """contents"""
        self.vs[15]["mm__"] = """directLink_S"""
        # match association ProvidedPort--intf-->ClientServerInterface node
        self.add_node()
        self.vs[16]["associationType"] = """intf"""
        self.vs[16]["mm__"] = """directLink_S"""
        # match association ClientServerInterface--contents-->Operation node
        self.add_node()
        self.vs[17]["associationType"] = """contents"""
        self.vs[17]["mm__"] = """directLink_S"""
        # match association ImplementationModule--contents-->AtomicComponent node
        self.add_node()
        self.vs[18]["associationType"] = """contents"""
        self.vs[18]["mm__"] = """directLink_S"""
        
        
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class ProvidedPort(layer0rule11class0)
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class AtomicComponent(layer0rule11class1)
                (0,8), # matchmodel -> match_contains
                (8,7), # match_contains -> match_class ClientServerInterface(layer0rule11class2)
                (0,10), # matchmodel -> match_contains
                (10,9), # match_contains -> match_class Operation(layer0rule11class3)
                (0,12), # matchmodel -> match_contains
                (12,11), # match_contains -> match_class ImplementationModule(layer0rule11class4)
                (1,14), # applymodel -> apply_contains
                (14,13), # apply_contains -> apply_class FunctionPrototype(layer0rule11class5)
                (5,15), # match_class AtomicComponent(layer0rule11class1) -> association contents
                (15,3), # association contents  -> match_class ProvidedPort(layer0rule11class0)
                (3,16), # match_class ProvidedPort(layer0rule11class0) -> association intf
                (16,7), # association intf  -> match_class ClientServerInterface(layer0rule11class2)
                (7,17), # match_class ClientServerInterface(layer0rule11class2) -> association contents
                (17,9), # association contents  -> match_class Operation(layer0rule11class3)
                (11,18), # match_class ImplementationModule(layer0rule11class4) -> association contents
                (18,5), # association contents  -> match_class AtomicComponent(layer0rule11class1)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])
		
        # Add the attribute equations
        self["equations"] = [((13,'name'),('concat',((11,'name'),('concat',(('constant','_'),('concat',((5,'name'),('concat',(('constant','_'),('concat',((3,'name'),('concat',(('constant','_'),(9,'name')))))))))))))), ((13,'__ApplyAttribute'),('constant','ProvidedPortFunctionPrototype')), ]

        
