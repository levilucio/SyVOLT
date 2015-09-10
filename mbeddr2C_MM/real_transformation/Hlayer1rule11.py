from core.himesis import Himesis
import uuid

class Hlayer1rule11(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule layer1rule11.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer1rule11, self).__init__(name='Hlayer1rule11', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """layer1rule11"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule11')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
 
        
        # match class ClientServerInterface(layer1rule11class0) node
        self.add_node()

        self.vs[3]["mm__"] = """ClientServerInterface""" 
        self.vs[3]["attr1"] = """+""" 
        # match_contains node for class ClientServerInterface(layer1rule11class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        # match class RequiredPort(layer1rule11class1) node
        self.add_node()

        self.vs[5]["mm__"] = """RequiredPort""" 
        self.vs[5]["attr1"] = """+""" 
        # match_contains node for class RequiredPort(layer1rule11class1)
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        
        
        # apply class TypeDef(layer1rule11class2) node
        self.add_node()

        self.vs[7]["mm__"] = """TypeDef""" 
        self.vs[7]["attr1"] = """1"""
        # apply_contains node for class TypeDef(layer1rule11class2)
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        # apply class Member(layer1rule11class3) node
        self.add_node()

        self.vs[9]["mm__"] = """Member""" 
        self.vs[9]["attr1"] = """1"""
        # apply_contains node for class Member(layer1rule11class3)
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        # apply class PointerType(layer1rule11class4) node
        self.add_node()

        self.vs[11]["mm__"] = """PointerType""" 
        self.vs[11]["attr1"] = """1"""
        # apply_contains node for class PointerType(layer1rule11class4)
        self.add_node()
        self.vs[12]["mm__"] = """apply_contains"""
        # apply class TypeDefType(layer1rule11class5) node
        self.add_node()

        self.vs[13]["mm__"] = """TypeDefType""" 
        self.vs[13]["attr1"] = """1"""
        # apply_contains node for class TypeDefType(layer1rule11class5)
        self.add_node()
        self.vs[14]["mm__"] = """apply_contains"""
        
        
        # match association RequiredPort--intf-->ClientServerInterface node
        self.add_node()
        self.vs[15]["attr1"] = """intf"""
        self.vs[15]["mm__"] = """directLink_S"""
        
        # apply association Member--type-->PointerType node
        self.add_node()
        self.vs[16]["attr1"] = """type"""
        self.vs[16]["mm__"] = """directLink_T"""
        # apply association PointerType--baseType-->TypeDefType node
        self.add_node()
        self.vs[17]["attr1"] = """baseType"""
        self.vs[17]["mm__"] = """directLink_T"""
        # apply association TypeDefType--typeDef-->TypeDef node
        self.add_node()
        self.vs[18]["attr1"] = """typeDef"""
        self.vs[18]["mm__"] = """directLink_T"""
        
        # backward association ClientServerInterface---->TypeDef node
        self.add_node()

        self.vs[19]["mm__"] = """backward_link"""
        # backward association RequiredPort---->Member node
        self.add_node()

        self.vs[20]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class ClientServerInterface(layer1rule11class0)
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class RequiredPort(layer1rule11class1)
                (1,8), # applymodel -> apply_contains
                (8,7), # apply_contains -> apply_class TypeDef(layer1rule11class2)
                (1,10), # applymodel -> apply_contains
                (10,9), # apply_contains -> apply_class Member(layer1rule11class3)
                (1,12), # applymodel -> apply_contains
                (12,11), # apply_contains -> apply_class PointerType(layer1rule11class4)
                (1,14), # applymodel -> apply_contains
                (14,13), # apply_contains -> apply_class TypeDefType(layer1rule11class5)
                (5,15), # match_class RequiredPort(layer1rule11class1) -> association intf
                (15,3), # association intf  -> match_class ClientServerInterface(layer1rule11class0)
                (9,16), # apply_class Member(layer1rule11class3) -> association type
                (16,11), # association type  -> apply_class PointerType(layer1rule11class4)
                (11,17), # apply_class PointerType(layer1rule11class4) -> association baseType
                (17,13), # association baseType  -> apply_class TypeDefType(layer1rule11class5)
                (13,18), # apply_class TypeDefType(layer1rule11class5) -> association typeDef
                (18,7), # association typeDef  -> apply_class TypeDef(layer1rule11class2)
                (7,19), # apply_class TypeDef(layer1rule11class2) -> backward_association
                (19,3), #  backward_association -> apply_class ClientServerInterface(layer1rule11class0)
                (9,20), # apply_class Member(layer1rule11class3) -> backward_association
                (20,5), #  backward_association -> apply_class RequiredPort(layer1rule11class1)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((7,'__ApplyAttribute'),('constant','TypeDefInterfaceStruct')), ((9,'__ApplyAttribute'),('constant','RequiredPort_ops')), ]

        
