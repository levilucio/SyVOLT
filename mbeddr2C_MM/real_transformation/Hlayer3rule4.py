from core.himesis import Himesis
import uuid

class Hlayer3rule4(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule layer3rule4.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer3rule4, self).__init__(name='Hlayer3rule4', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """layer3rule4"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule4')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
 
        
        # match class ImplementationModule(layer3rule4class0) node
        self.add_node()

        self.vs[3]["mm__"] = """ImplementationModule""" 
        self.vs[3]["attr1"] = """+""" 
        # match_contains node for class ImplementationModule(layer3rule4class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        # match class InstanceConfiguration(layer3rule4class1) node
        self.add_node()

        self.vs[5]["mm__"] = """InstanceConfiguration""" 
        self.vs[5]["attr1"] = """+""" 
        # match_contains node for class InstanceConfiguration(layer3rule4class1)
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        # match class ComponentInstance(layer3rule4class2) node
        self.add_node()

        self.vs[7]["mm__"] = """ComponentInstance""" 
        self.vs[7]["attr1"] = """+""" 
        # match_contains node for class ComponentInstance(layer3rule4class2)
        self.add_node()
        self.vs[8]["mm__"] = """match_contains"""
        # match class AtomicComponent(layer3rule4class3) node
        self.add_node()

        self.vs[9]["mm__"] = """AtomicComponent""" 
        self.vs[9]["attr1"] = """+""" 
        # match_contains node for class AtomicComponent(layer3rule4class3)
        self.add_node()
        self.vs[10]["mm__"] = """match_contains"""
        
        
        # apply class ImplementationModule(layer3rule4class4) node
        self.add_node()

        self.vs[11]["mm__"] = """ImplementationModule""" 
        self.vs[11]["attr1"] = """1"""
        # apply_contains node for class ImplementationModule(layer3rule4class4)
        self.add_node()
        self.vs[12]["mm__"] = """apply_contains"""
        # apply class GlobalVariableDeclaration(layer3rule4class5) node
        self.add_node()

        self.vs[13]["mm__"] = """GlobalVariableDeclaration""" 
        self.vs[13]["attr1"] = """1"""
        # apply_contains node for class GlobalVariableDeclaration(layer3rule4class5)
        self.add_node()
        self.vs[14]["mm__"] = """apply_contains"""
        # apply class TypeDef(layer3rule4class6) node
        self.add_node()

        self.vs[15]["mm__"] = """TypeDef""" 
        self.vs[15]["attr1"] = """1"""
        # apply_contains node for class TypeDef(layer3rule4class6)
        self.add_node()
        self.vs[16]["mm__"] = """apply_contains"""
        # apply class TypeDefType(layer3rule4class7) node
        self.add_node()

        self.vs[17]["mm__"] = """TypeDefType""" 
        self.vs[17]["attr1"] = """1"""
        # apply_contains node for class TypeDefType(layer3rule4class7)
        self.add_node()
        self.vs[18]["mm__"] = """apply_contains"""
        
        
        # match association ImplementationModule--contents-->InstanceConfiguration node
        self.add_node()
        self.vs[19]["attr1"] = """contents"""
        self.vs[19]["mm__"] = """directLink_S"""
        # match association InstanceConfiguration--contents-->ComponentInstance node
        self.add_node()
        self.vs[20]["attr1"] = """contents"""
        self.vs[20]["mm__"] = """directLink_S"""
        # match association ComponentInstance--component-->AtomicComponent node
        self.add_node()
        self.vs[21]["attr1"] = """component"""
        self.vs[21]["mm__"] = """directLink_S"""
        
        # apply association ImplementationModule--contents-->GlobalVariableDeclaration node
        self.add_node()
        self.vs[22]["attr1"] = """contents"""
        self.vs[22]["mm__"] = """directLink_T"""
        # apply association GlobalVariableDeclaration--type-->TypeDefType node
        self.add_node()
        self.vs[23]["attr1"] = """type"""
        self.vs[23]["mm__"] = """directLink_T"""
        # apply association TypeDefType--typeDef-->TypeDef node
        self.add_node()
        self.vs[24]["attr1"] = """typeDef"""
        self.vs[24]["mm__"] = """directLink_T"""
        
        # backward association ImplementationModule---->ImplementationModule node
        self.add_node()

        self.vs[25]["mm__"] = """backward_link"""
        # backward association AtomicComponent---->TypeDef node
        self.add_node()

        self.vs[26]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class ImplementationModule(layer3rule4class0)
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class InstanceConfiguration(layer3rule4class1)
                (0,8), # matchmodel -> match_contains
                (8,7), # match_contains -> match_class ComponentInstance(layer3rule4class2)
                (0,10), # matchmodel -> match_contains
                (10,9), # match_contains -> match_class AtomicComponent(layer3rule4class3)
                (1,12), # applymodel -> apply_contains
                (12,11), # apply_contains -> apply_class ImplementationModule(layer3rule4class4)
                (1,14), # applymodel -> apply_contains
                (14,13), # apply_contains -> apply_class GlobalVariableDeclaration(layer3rule4class5)
                (1,16), # applymodel -> apply_contains
                (16,15), # apply_contains -> apply_class TypeDef(layer3rule4class6)
                (1,18), # applymodel -> apply_contains
                (18,17), # apply_contains -> apply_class TypeDefType(layer3rule4class7)
                (3,19), # match_class ImplementationModule(layer3rule4class0) -> association contents
                (19,5), # association contents  -> match_class InstanceConfiguration(layer3rule4class1)
                (5,20), # match_class InstanceConfiguration(layer3rule4class1) -> association contents
                (20,7), # association contents  -> match_class ComponentInstance(layer3rule4class2)
                (7,21), # match_class ComponentInstance(layer3rule4class2) -> association component
                (21,9), # association component  -> match_class AtomicComponent(layer3rule4class3)
                (11,22), # apply_class ImplementationModule(layer3rule4class4) -> association contents
                (22,13), # association contents  -> apply_class GlobalVariableDeclaration(layer3rule4class5)
                (13,23), # apply_class GlobalVariableDeclaration(layer3rule4class5) -> association type
                (23,17), # association type  -> apply_class TypeDefType(layer3rule4class7)
                (17,24), # apply_class TypeDefType(layer3rule4class7) -> association typeDef
                (24,15), # association typeDef  -> apply_class TypeDef(layer3rule4class6)
                (11,25), # apply_class ImplementationModule(layer3rule4class4) -> backward_association
                (25,3), #  backward_association -> apply_class ImplementationModule(layer3rule4class0)
                (15,26), # apply_class TypeDef(layer3rule4class6) -> backward_association
                (26,9), #  backward_association -> apply_class AtomicComponent(layer3rule4class3)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((11,'__ApplyAttribute'),('constant','ImplementationModule')), ((13,'name'),('concat',((3,'name'),('concat',(('constant','_'),('concat',((5,'name'),('concat',(('constant','_'),('concat',((7,'name'),('constant','__instance')))))))))))), ((13,'__ApplyAttribute'),('constant','GlobalComponentInstanceDeclaration')), ((15,'__ApplyAttribute'),('constant','TypeDefComponentStruct')), ]

        
