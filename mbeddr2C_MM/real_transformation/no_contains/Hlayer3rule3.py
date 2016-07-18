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
        self.vs[2]["attr1"] = """layer3rule3"""
        
        # match class ImplementationModule(layer3rule3class0) node
        self.add_node()
        
        self.vs[3]["mm__"] = """ImplementationModule""" 
        self.vs[3]["attr1"] = """+""" 
        # match class InstanceConfiguration(layer3rule3class1) node
        self.add_node()
        
        self.vs[4]["mm__"] = """InstanceConfiguration""" 
        self.vs[4]["attr1"] = """+""" 
        # match class ComponentInstance(layer3rule3class2) node
        self.add_node()
        
        self.vs[5]["mm__"] = """ComponentInstance""" 
        self.vs[5]["attr1"] = """+""" 
        # match class AtomicComponent(layer3rule3class3) node
        self.add_node()
        
        self.vs[6]["mm__"] = """AtomicComponent""" 
        self.vs[6]["attr1"] = """+""" 
        # match class ProvidedPort(layer3rule3class4) node
        self.add_node()
        
        self.vs[7]["mm__"] = """ProvidedPort""" 
        self.vs[7]["attr1"] = """+""" 
        # match class ClientServerInterface(layer3rule3class5) node
        self.add_node()
        
        self.vs[8]["mm__"] = """ClientServerInterface""" 
        self.vs[8]["attr1"] = """+""" 
        
        
        # apply class ImplementationModule(layer3rule3class6) node
        self.add_node()

        self.vs[9]["mm__"] = """ImplementationModule""" 
        self.vs[9]["attr1"] = """1"""
        # apply class GlobalVariableDeclaration(layer3rule3class7) node
        self.add_node()

        self.vs[10]["mm__"] = """GlobalVariableDeclaration""" 
        self.vs[10]["attr1"] = """1"""
        # apply class TypeDef(layer3rule3class8) node
        self.add_node()

        self.vs[11]["mm__"] = """TypeDef""" 
        self.vs[11]["attr1"] = """1"""
        # apply class TypeDefType(layer3rule3class9) node
        self.add_node()

        self.vs[12]["mm__"] = """TypeDefType""" 
        self.vs[12]["attr1"] = """1"""
        
        
        # match association ImplementationModule--contents-->InstanceConfiguration node
        self.add_node()
        self.vs[13]["attr1"] = """contents"""
        self.vs[13]["mm__"] = """directLink_S"""
        # match association InstanceConfiguration--contents-->ComponentInstance node
        self.add_node()
        self.vs[14]["attr1"] = """contents"""
        self.vs[14]["mm__"] = """directLink_S"""
        # match association ComponentInstance--component-->AtomicComponent node
        self.add_node()
        self.vs[15]["attr1"] = """component"""
        self.vs[15]["mm__"] = """directLink_S"""
        # match association AtomicComponent--contents-->ProvidedPort node
        self.add_node()
        self.vs[16]["attr1"] = """contents"""
        self.vs[16]["mm__"] = """directLink_S"""
        # match association ProvidedPort--intf-->ClientServerInterface node
        self.add_node()
        self.vs[17]["attr1"] = """intf"""
        self.vs[17]["mm__"] = """directLink_S"""
        
        # apply association ImplementationModule--contents-->GlobalVariableDeclaration node
        self.add_node()
        self.vs[18]["attr1"] = """contents"""
        self.vs[18]["mm__"] = """directLink_T"""
        # apply association GlobalVariableDeclaration--type-->TypeDefType node
        self.add_node()
        self.vs[19]["attr1"] = """type"""
        self.vs[19]["mm__"] = """directLink_T"""
        # apply association TypeDefType--typeDef-->TypeDef node
        self.add_node()
        self.vs[20]["attr1"] = """typeDef"""
        self.vs[20]["mm__"] = """directLink_T"""
        
        # backward association ImplementationModule---->ImplementationModule node
        self.add_node()

        self.vs[21]["mm__"] = """backward_link"""
        # backward association ClientServerInterface---->TypeDef node
        self.add_node()

        self.vs[22]["mm__"] = """backward_link"""
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class ImplementationModule(layer3rule3class0)
                (0,4), # matchmodel -> match_class InstanceConfiguration(layer3rule3class1)
                (0,5), # matchmodel -> match_class ComponentInstance(layer3rule3class2)
                (0,6), # matchmodel -> match_class AtomicComponent(layer3rule3class3)
                (0,7), # matchmodel -> match_class ProvidedPort(layer3rule3class4)
                (0,8), # matchmodel -> match_class ClientServerInterface(layer3rule3class5)
                (1,9), # applymodel -> -> apply_class ImplementationModule(layer3rule3class6)
                (1,10), # applymodel -> -> apply_class GlobalVariableDeclaration(layer3rule3class7)
                (1,11), # applymodel -> -> apply_class TypeDef(layer3rule3class8)
                (1,12), # applymodel -> -> apply_class TypeDefType(layer3rule3class9)
                (3,13), # match_class ImplementationModule(layer3rule3class0) -> association contents
                (13,4), # association contents  -> match_class InstanceConfiguration(layer3rule3class1)
                (4,14), # match_class InstanceConfiguration(layer3rule3class1) -> association contents
                (14,5), # association contents  -> match_class ComponentInstance(layer3rule3class2)
                (5,15), # match_class ComponentInstance(layer3rule3class2) -> association component
                (15,6), # association component  -> match_class AtomicComponent(layer3rule3class3)
                (6,16), # match_class AtomicComponent(layer3rule3class3) -> association contents
                (16,7), # association contents  -> match_class ProvidedPort(layer3rule3class4)
                (7,17), # match_class ProvidedPort(layer3rule3class4) -> association intf
                (17,8), # association intf  -> match_class ClientServerInterface(layer3rule3class5)
                (9,18), # apply_class ImplementationModule(layer3rule3class6) -> association contents
                (18,10), # association contents  -> apply_class GlobalVariableDeclaration(layer3rule3class7)
                (10,19), # apply_class GlobalVariableDeclaration(layer3rule3class7) -> association type
                (19,12), # association type  -> apply_class TypeDefType(layer3rule3class9)
                (12,20), # apply_class TypeDefType(layer3rule3class9) -> association typeDef
                (20,11), # association typeDef  -> apply_class TypeDef(layer3rule3class8)
                (9,21), # apply_class ImplementationModule(layer3rule3class6) -> backward_association
                (21,3), #  backward_association -> apply_class ImplementationModule(layer3rule3class0)
                (11,22), # apply_class TypeDef(layer3rule3class8) -> backward_association
                (22,8), #  backward_association -> apply_class ClientServerInterface(layer3rule3class5)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((9,'__ApplyAttribute'),('constant','ImplementationModule')), ((10,'name'),('concat',((3,'name'),('concat',(('constant','_'),('concat',((5,'name'),('concat',(('constant','_'),('concat',((8,'name'),('constant','__ops')))))))))))), ((10,'__ApplyAttribute'),('constant','GlobalVarOps')), ((11,'__ApplyAttribute'),('constant','TypeDefInterfaceStruct')), ]

        
