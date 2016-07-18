from core.himesis import Himesis
import uuid

class Hlayer1rule1(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule layer1rule1.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer1rule1, self).__init__(name='Hlayer1rule1', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer1rule1"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule1')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["attr1"] = """layer1rule1"""
        
        # match class ClientServerInterface(layer1rule1class0) node
        self.add_node()
        
        self.vs[3]["mm__"] = """ClientServerInterface""" 
        self.vs[3]["attr1"] = """+""" 
        # match class Operation(layer1rule1class1) node
        self.add_node()
        
        self.vs[4]["mm__"] = """Operation""" 
        self.vs[4]["attr1"] = """+""" 
        
        
        # apply class StructDeclaration(layer1rule1class2) node
        self.add_node()

        self.vs[5]["mm__"] = """StructDeclaration""" 
        self.vs[5]["attr1"] = """1"""
        # apply class CFunctionPointerStructMember(layer1rule1class3) node
        self.add_node()

        self.vs[6]["mm__"] = """CFunctionPointerStructMember""" 
        self.vs[6]["attr1"] = """1"""
        
        
        # match association ClientServerInterface--contents-->Operation node
        self.add_node()
        self.vs[7]["attr1"] = """contents"""
        self.vs[7]["mm__"] = """directLink_S"""
        
        # apply association StructDeclaration--members-->CFunctionPointerStructMember node
        self.add_node()
        self.vs[8]["attr1"] = """members"""
        self.vs[8]["mm__"] = """directLink_T"""
        
        # backward association Operation---->CFunctionPointerStructMember node
        self.add_node()

        self.vs[9]["mm__"] = """backward_link"""
        # backward association ClientServerInterface---->StructDeclaration node
        self.add_node()

        self.vs[10]["mm__"] = """backward_link"""
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class ClientServerInterface(layer1rule1class0)
                (0,4), # matchmodel -> match_class Operation(layer1rule1class1)
                (1,5), # applymodel -> -> apply_class StructDeclaration(layer1rule1class2)
                (1,6), # applymodel -> -> apply_class CFunctionPointerStructMember(layer1rule1class3)
                (3,7), # match_class ClientServerInterface(layer1rule1class0) -> association contents
                (7,4), # association contents  -> match_class Operation(layer1rule1class1)
                (5,8), # apply_class StructDeclaration(layer1rule1class2) -> association members
                (8,6), # association members  -> apply_class CFunctionPointerStructMember(layer1rule1class3)
                (6,9), # apply_class CFunctionPointerStructMember(layer1rule1class3) -> backward_association
                (9,4), #  backward_association -> apply_class Operation(layer1rule1class1)
                (5,10), # apply_class StructDeclaration(layer1rule1class2) -> backward_association
                (10,3), #  backward_association -> apply_class ClientServerInterface(layer1rule1class0)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((5,'__ApplyAttribute'),('constant','ClientServerStructIData')), ((6,'__ApplyAttribute'),('constant','CFunctionPointerStructMember')), ]

        
