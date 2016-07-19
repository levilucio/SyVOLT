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
        self.vs[2]["attr1"] = """layer1rule11"""
        
        # match class ClientServerInterface(layer1rule11class0) node
        self.add_node()
        
        self.vs[3]["mm__"] = """ClientServerInterface""" 
        self.vs[3]["attr1"] = """+""" 
        # match class RequiredPort(layer1rule11class1) node
        self.add_node()
        
        self.vs[4]["mm__"] = """RequiredPort""" 
        self.vs[4]["attr1"] = """+""" 
        
        
        # apply class TypeDef(layer1rule11class2) node
        self.add_node()

        self.vs[5]["mm__"] = """TypeDef""" 
        self.vs[5]["attr1"] = """1"""
        # apply class Member(layer1rule11class3) node
        self.add_node()

        self.vs[6]["mm__"] = """Member""" 
        self.vs[6]["attr1"] = """1"""
        # apply class PointerType(layer1rule11class4) node
        self.add_node()

        self.vs[7]["mm__"] = """PointerType""" 
        self.vs[7]["attr1"] = """1"""
        # apply class TypeDefType(layer1rule11class5) node
        self.add_node()

        self.vs[8]["mm__"] = """TypeDefType""" 
        self.vs[8]["attr1"] = """1"""
        
        
        # match association RequiredPort--intf-->ClientServerInterface node
        self.add_node()
        self.vs[9]["attr1"] = """intf"""
        self.vs[9]["mm__"] = """directLink_S"""
        
        # apply association Member--type-->PointerType node
        self.add_node()
        self.vs[10]["attr1"] = """type"""
        self.vs[10]["mm__"] = """directLink_T"""
        # apply association PointerType--baseType-->TypeDefType node
        self.add_node()
        self.vs[11]["attr1"] = """baseType"""
        self.vs[11]["mm__"] = """directLink_T"""
        # apply association TypeDefType--typeDef-->TypeDef node
        self.add_node()
        self.vs[12]["attr1"] = """typeDef"""
        self.vs[12]["mm__"] = """directLink_T"""
        
        # backward association ClientServerInterface---->TypeDef node
        self.add_node()

        self.vs[13]["mm__"] = """backward_link"""
        # backward association RequiredPort---->Member node
        self.add_node()

        self.vs[14]["mm__"] = """backward_link"""
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class ClientServerInterface(layer1rule11class0)
                (0,4), # matchmodel -> match_class RequiredPort(layer1rule11class1)
                (1,5), # applymodel -> -> apply_class TypeDef(layer1rule11class2)
                (1,6), # applymodel -> -> apply_class Member(layer1rule11class3)
                (1,7), # applymodel -> -> apply_class PointerType(layer1rule11class4)
                (1,8), # applymodel -> -> apply_class TypeDefType(layer1rule11class5)
                (4,9), # match_class RequiredPort(layer1rule11class1) -> association intf
                (9,3), # association intf  -> match_class ClientServerInterface(layer1rule11class0)
                (6,10), # apply_class Member(layer1rule11class3) -> association type
                (10,7), # association type  -> apply_class PointerType(layer1rule11class4)
                (7,11), # apply_class PointerType(layer1rule11class4) -> association baseType
                (11,8), # association baseType  -> apply_class TypeDefType(layer1rule11class5)
                (8,12), # apply_class TypeDefType(layer1rule11class5) -> association typeDef
                (12,5), # association typeDef  -> apply_class TypeDef(layer1rule11class2)
                (5,13), # apply_class TypeDef(layer1rule11class2) -> backward_association
                (13,3), #  backward_association -> apply_class ClientServerInterface(layer1rule11class0)
                (6,14), # apply_class Member(layer1rule11class3) -> backward_association
                (14,4), #  backward_association -> apply_class RequiredPort(layer1rule11class1)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((5,'__ApplyAttribute'),('constant','TypeDefInterfaceStruct')), ((6,'__ApplyAttribute'),('constant','RequiredPort_ops')), ]

        
