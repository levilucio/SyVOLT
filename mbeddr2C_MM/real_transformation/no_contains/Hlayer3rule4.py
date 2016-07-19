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
        self.vs[2]["attr1"] = """layer3rule4"""
        
        # match class ImplementationModule(layer3rule4class0) node
        self.add_node()
        
        self.vs[3]["mm__"] = """ImplementationModule""" 
        self.vs[3]["attr1"] = """+""" 
        # match class InstanceConfiguration(layer3rule4class1) node
        self.add_node()
        
        self.vs[4]["mm__"] = """InstanceConfiguration""" 
        self.vs[4]["attr1"] = """+""" 
        # match class ComponentInstance(layer3rule4class2) node
        self.add_node()
        
        self.vs[5]["mm__"] = """ComponentInstance""" 
        self.vs[5]["attr1"] = """+""" 
        # match class AtomicComponent(layer3rule4class3) node
        self.add_node()
        
        self.vs[6]["mm__"] = """AtomicComponent""" 
        self.vs[6]["attr1"] = """+""" 
        
        
        # apply class ImplementationModule(layer3rule4class4) node
        self.add_node()

        self.vs[7]["mm__"] = """ImplementationModule""" 
        self.vs[7]["attr1"] = """1"""
        # apply class GlobalVariableDeclaration(layer3rule4class5) node
        self.add_node()

        self.vs[8]["mm__"] = """GlobalVariableDeclaration""" 
        self.vs[8]["attr1"] = """1"""
        # apply class TypeDef(layer3rule4class6) node
        self.add_node()

        self.vs[9]["mm__"] = """TypeDef""" 
        self.vs[9]["attr1"] = """1"""
        # apply class TypeDefType(layer3rule4class7) node
        self.add_node()

        self.vs[10]["mm__"] = """TypeDefType""" 
        self.vs[10]["attr1"] = """1"""
        
        
        # match association ImplementationModule--contents-->InstanceConfiguration node
        self.add_node()
        self.vs[11]["attr1"] = """contents"""
        self.vs[11]["mm__"] = """directLink_S"""
        # match association InstanceConfiguration--contents-->ComponentInstance node
        self.add_node()
        self.vs[12]["attr1"] = """contents"""
        self.vs[12]["mm__"] = """directLink_S"""
        # match association ComponentInstance--component-->AtomicComponent node
        self.add_node()
        self.vs[13]["attr1"] = """component"""
        self.vs[13]["mm__"] = """directLink_S"""
        
        # apply association ImplementationModule--contents-->GlobalVariableDeclaration node
        self.add_node()
        self.vs[14]["attr1"] = """contents"""
        self.vs[14]["mm__"] = """directLink_T"""
        # apply association GlobalVariableDeclaration--type-->TypeDefType node
        self.add_node()
        self.vs[15]["attr1"] = """type"""
        self.vs[15]["mm__"] = """directLink_T"""
        # apply association TypeDefType--typeDef-->TypeDef node
        self.add_node()
        self.vs[16]["attr1"] = """typeDef"""
        self.vs[16]["mm__"] = """directLink_T"""
        
        # backward association ImplementationModule---->ImplementationModule node
        self.add_node()

        self.vs[17]["mm__"] = """backward_link"""
        # backward association AtomicComponent---->TypeDef node
        self.add_node()

        self.vs[18]["mm__"] = """backward_link"""
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class ImplementationModule(layer3rule4class0)
                (0,4), # matchmodel -> match_class InstanceConfiguration(layer3rule4class1)
                (0,5), # matchmodel -> match_class ComponentInstance(layer3rule4class2)
                (0,6), # matchmodel -> match_class AtomicComponent(layer3rule4class3)
                (1,7), # applymodel -> -> apply_class ImplementationModule(layer3rule4class4)
                (1,8), # applymodel -> -> apply_class GlobalVariableDeclaration(layer3rule4class5)
                (1,9), # applymodel -> -> apply_class TypeDef(layer3rule4class6)
                (1,10), # applymodel -> -> apply_class TypeDefType(layer3rule4class7)
                (3,11), # match_class ImplementationModule(layer3rule4class0) -> association contents
                (11,4), # association contents  -> match_class InstanceConfiguration(layer3rule4class1)
                (4,12), # match_class InstanceConfiguration(layer3rule4class1) -> association contents
                (12,5), # association contents  -> match_class ComponentInstance(layer3rule4class2)
                (5,13), # match_class ComponentInstance(layer3rule4class2) -> association component
                (13,6), # association component  -> match_class AtomicComponent(layer3rule4class3)
                (7,14), # apply_class ImplementationModule(layer3rule4class4) -> association contents
                (14,8), # association contents  -> apply_class GlobalVariableDeclaration(layer3rule4class5)
                (8,15), # apply_class GlobalVariableDeclaration(layer3rule4class5) -> association type
                (15,10), # association type  -> apply_class TypeDefType(layer3rule4class7)
                (10,16), # apply_class TypeDefType(layer3rule4class7) -> association typeDef
                (16,9), # association typeDef  -> apply_class TypeDef(layer3rule4class6)
                (7,17), # apply_class ImplementationModule(layer3rule4class4) -> backward_association
                (17,3), #  backward_association -> apply_class ImplementationModule(layer3rule4class0)
                (9,18), # apply_class TypeDef(layer3rule4class6) -> backward_association
                (18,6), #  backward_association -> apply_class AtomicComponent(layer3rule4class3)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((7,'__ApplyAttribute'),('constant','ImplementationModule')), ((8,'name'),('concat',((3,'name'),('concat',(('constant','_'),('concat',((4,'name'),('concat',(('constant','_'),('concat',((5,'name'),('constant','__instance')))))))))))), ((8,'__ApplyAttribute'),('constant','GlobalComponentInstanceDeclaration')), ((9,'__ApplyAttribute'),('constant','TypeDefComponentStruct')), ]

        
