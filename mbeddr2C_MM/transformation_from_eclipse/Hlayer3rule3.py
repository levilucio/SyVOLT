from core.himesis import Himesis
import uuid

class Hlayer3rule3(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule layer3rule3.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer3rule3, self).__init__(name='Hlayer3rule3', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """layer3rule3"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule3')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
 
        
        # match class ImplementationModule(layer3rule3class0) node
        self.add_node()

        self.vs[3]["mm__"] = """ImplementationModule""" 
        self.vs[3]["attr1"] = """+""" 
        # match_contains node for class ImplementationModule(layer3rule3class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        # match class InstanceConfiguration(layer3rule3class1) node
        self.add_node()

        self.vs[5]["mm__"] = """InstanceConfiguration""" 
        self.vs[5]["attr1"] = """+""" 
        # match_contains node for class InstanceConfiguration(layer3rule3class1)
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        # match class ComponentInstance(layer3rule3class2) node
        self.add_node()

        self.vs[7]["mm__"] = """ComponentInstance""" 
        self.vs[7]["attr1"] = """+""" 
        # match_contains node for class ComponentInstance(layer3rule3class2)
        self.add_node()
        self.vs[8]["mm__"] = """match_contains"""
        # match class AtomicComponent(layer3rule3class3) node
        self.add_node()

        self.vs[9]["mm__"] = """AtomicComponent""" 
        self.vs[9]["attr1"] = """+""" 
        # match_contains node for class AtomicComponent(layer3rule3class3)
        self.add_node()
        self.vs[10]["mm__"] = """match_contains"""
        # match class ProvidedPort(layer3rule3class4) node
        self.add_node()

        self.vs[11]["mm__"] = """ProvidedPort""" 
        self.vs[11]["attr1"] = """+""" 
        # match_contains node for class ProvidedPort(layer3rule3class4)
        self.add_node()
        self.vs[12]["mm__"] = """match_contains"""
        # match class ClientServerInterface(layer3rule3class5) node
        self.add_node()

        self.vs[13]["mm__"] = """ClientServerInterface""" 
        self.vs[13]["attr1"] = """+""" 
        # match_contains node for class ClientServerInterface(layer3rule3class5)
        self.add_node()
        self.vs[14]["mm__"] = """match_contains"""
        
        
        # apply class ImplementationModule(layer3rule3class6) node
        self.add_node()

        self.vs[15]["mm__"] = """ImplementationModule""" 
        self.vs[15]["attr1"] = """1"""
        # apply_contains node for class ImplementationModule(layer3rule3class6)
        self.add_node()
        self.vs[16]["mm__"] = """apply_contains"""
        # apply class GlobalVariableDeclaration(layer3rule3class7) node
        self.add_node()

        self.vs[17]["mm__"] = """GlobalVariableDeclaration""" 
        self.vs[17]["attr1"] = """1"""
        # apply_contains node for class GlobalVariableDeclaration(layer3rule3class7)
        self.add_node()
        self.vs[18]["mm__"] = """apply_contains"""
        # apply class TypeDef(layer3rule3class8) node
        self.add_node()

        self.vs[19]["mm__"] = """TypeDef""" 
        self.vs[19]["attr1"] = """1"""
        # apply_contains node for class TypeDef(layer3rule3class8)
        self.add_node()
        self.vs[20]["mm__"] = """apply_contains"""
        # apply class TypeDefType(layer3rule3class9) node
        self.add_node()

        self.vs[21]["mm__"] = """TypeDefType""" 
        self.vs[21]["attr1"] = """1"""
        # apply_contains node for class TypeDefType(layer3rule3class9)
        self.add_node()
        self.vs[22]["mm__"] = """apply_contains"""
        
        
        # match association ImplementationModule--contents-->InstanceConfiguration node
        self.add_node()
        self.vs[23]["attr1"] = """contents"""
        self.vs[23]["mm__"] = """directLink_S"""
        # match association InstanceConfiguration--contents-->ComponentInstance node
        self.add_node()
        self.vs[24]["attr1"] = """contents"""
        self.vs[24]["mm__"] = """directLink_S"""
        # match association ComponentInstance--component-->AtomicComponent node
        self.add_node()
        self.vs[25]["attr1"] = """component"""
        self.vs[25]["mm__"] = """directLink_S"""
        # match association AtomicComponent--contents-->ProvidedPort node
        self.add_node()
        self.vs[26]["attr1"] = """contents"""
        self.vs[26]["mm__"] = """directLink_S"""
        # match association ProvidedPort--intf-->ClientServerInterface node
        self.add_node()
        self.vs[27]["attr1"] = """intf"""
        self.vs[27]["mm__"] = """directLink_S"""
        
        # apply association ImplementationModule--contents-->GlobalVariableDeclaration node
        self.add_node()
        self.vs[28]["attr1"] = """contents"""
        self.vs[28]["mm__"] = """directLink_T"""
        # apply association GlobalVariableDeclaration--type-->TypeDefType node
        self.add_node()
        self.vs[29]["attr1"] = """type"""
        self.vs[29]["mm__"] = """directLink_T"""
        # apply association TypeDefType--typeDef-->TypeDef node
        self.add_node()
        self.vs[30]["attr1"] = """typeDef"""
        self.vs[30]["mm__"] = """directLink_T"""
        
        # backward association ImplementationModule---->ImplementationModule node
        self.add_node()

        self.vs[31]["mm__"] = """backward_link"""
        # backward association ClientServerInterface---->TypeDef node
        self.add_node()

        self.vs[32]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class ImplementationModule(layer3rule3class0)
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class InstanceConfiguration(layer3rule3class1)
                (0,8), # matchmodel -> match_contains
                (8,7), # match_contains -> match_class ComponentInstance(layer3rule3class2)
                (0,10), # matchmodel -> match_contains
                (10,9), # match_contains -> match_class AtomicComponent(layer3rule3class3)
                (0,12), # matchmodel -> match_contains
                (12,11), # match_contains -> match_class ProvidedPort(layer3rule3class4)
                (0,14), # matchmodel -> match_contains
                (14,13), # match_contains -> match_class ClientServerInterface(layer3rule3class5)
                (1,16), # applymodel -> apply_contains
                (16,15), # apply_contains -> apply_class ImplementationModule(layer3rule3class6)
                (1,18), # applymodel -> apply_contains
                (18,17), # apply_contains -> apply_class GlobalVariableDeclaration(layer3rule3class7)
                (1,20), # applymodel -> apply_contains
                (20,19), # apply_contains -> apply_class TypeDef(layer3rule3class8)
                (1,22), # applymodel -> apply_contains
                (22,21), # apply_contains -> apply_class TypeDefType(layer3rule3class9)
                (3,23), # match_class ImplementationModule(layer3rule3class0) -> association contents
                (23,5), # association contents  -> match_class InstanceConfiguration(layer3rule3class1)
                (5,24), # match_class InstanceConfiguration(layer3rule3class1) -> association contents
                (24,7), # association contents  -> match_class ComponentInstance(layer3rule3class2)
                (7,25), # match_class ComponentInstance(layer3rule3class2) -> association component
                (25,9), # association component  -> match_class AtomicComponent(layer3rule3class3)
                (9,26), # match_class AtomicComponent(layer3rule3class3) -> association contents
                (26,11), # association contents  -> match_class ProvidedPort(layer3rule3class4)
                (11,27), # match_class ProvidedPort(layer3rule3class4) -> association intf
                (27,13), # association intf  -> match_class ClientServerInterface(layer3rule3class5)
                (15,28), # apply_class ImplementationModule(layer3rule3class6) -> association contents
                (28,17), # association contents  -> apply_class GlobalVariableDeclaration(layer3rule3class7)
                (17,29), # apply_class GlobalVariableDeclaration(layer3rule3class7) -> association type
                (29,21), # association type  -> apply_class TypeDefType(layer3rule3class9)
                (21,30), # apply_class TypeDefType(layer3rule3class9) -> association typeDef
                (30,19), # association typeDef  -> apply_class TypeDef(layer3rule3class8)
                (15,31), # apply_class ImplementationModule(layer3rule3class6) -> backward_association
                (31,3), #  backward_association -> apply_class ImplementationModule(layer3rule3class0)
                (19,32), # apply_class TypeDef(layer3rule3class8) -> backward_association
                (32,13), #  backward_association -> apply_class ClientServerInterface(layer3rule3class5)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((15,'__ApplyAttribute'),('constant','ImplementationModule')), ((17,'name'),('concat',((3,'name'),('concat',(('constant','_'),('concat',((7,'name'),('concat',(('constant','_'),('concat',((13,'name'),('constant','__ops')))))))))))), ((17,'__ApplyAttribute'),('constant','GlobalVarOps')), ((19,'__ApplyAttribute'),('constant','TypeDefInterfaceStruct')), ]

        
