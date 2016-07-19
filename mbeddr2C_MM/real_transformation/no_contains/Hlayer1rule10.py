from core.himesis import Himesis
import uuid

class Hlayer1rule10(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule layer1rule10.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer1rule10, self).__init__(name='Hlayer1rule10', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer1rule10"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule10')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["attr1"] = """layer1rule10"""
        
        # match class AtomicComponent(layer1rule10class0) node
        self.add_node()
        
        self.vs[3]["mm__"] = """AtomicComponent""" 
        self.vs[3]["attr1"] = """+""" 
        # match class RequiredPort(layer1rule10class1) node
        self.add_node()
        
        self.vs[4]["mm__"] = """RequiredPort""" 
        self.vs[4]["attr1"] = """+""" 
        
        
        # apply class StructDeclaration(layer1rule10class2) node
        self.add_node()

        self.vs[5]["mm__"] = """StructDeclaration""" 
        self.vs[5]["attr1"] = """1"""
        # apply class Member(layer1rule10class3) node
        self.add_node()

        self.vs[6]["mm__"] = """Member""" 
        self.vs[6]["attr1"] = """1"""
        # apply class Member(layer1rule10class4) node
        self.add_node()

        self.vs[7]["mm__"] = """Member""" 
        self.vs[7]["attr1"] = """1"""
        
        
        # match association AtomicComponent--contents-->RequiredPort node
        self.add_node()
        self.vs[8]["attr1"] = """contents"""
        self.vs[8]["mm__"] = """directLink_S"""
        
        # apply association StructDeclaration--members-->Member node
        self.add_node()
        self.vs[9]["attr1"] = """members"""
        self.vs[9]["mm__"] = """directLink_T"""
        # apply association StructDeclaration--members-->Member node
        self.add_node()
        self.vs[10]["attr1"] = """members"""
        self.vs[10]["mm__"] = """directLink_T"""
        
        # backward association AtomicComponent---->StructDeclaration node
        self.add_node()

        self.vs[11]["mm__"] = """backward_link"""
        # backward association RequiredPort---->Member node
        self.add_node()

        self.vs[12]["mm__"] = """backward_link"""
        # backward association RequiredPort---->Member node
        self.add_node()

        self.vs[13]["mm__"] = """backward_link"""
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class AtomicComponent(layer1rule10class0)
                (0,4), # matchmodel -> match_class RequiredPort(layer1rule10class1)
                (1,5), # applymodel -> -> apply_class StructDeclaration(layer1rule10class2)
                (1,6), # applymodel -> -> apply_class Member(layer1rule10class3)
                (1,7), # applymodel -> -> apply_class Member(layer1rule10class4)
                (3,8), # match_class AtomicComponent(layer1rule10class0) -> association contents
                (8,4), # association contents  -> match_class RequiredPort(layer1rule10class1)
                (5,9), # apply_class StructDeclaration(layer1rule10class2) -> association members
                (9,6), # association members  -> apply_class Member(layer1rule10class3)
                (5,10), # apply_class StructDeclaration(layer1rule10class2) -> association members
                (10,7), # association members  -> apply_class Member(layer1rule10class4)
                (5,11), # apply_class StructDeclaration(layer1rule10class2) -> backward_association
                (11,3), #  backward_association -> apply_class AtomicComponent(layer1rule10class0)
                (6,12), # apply_class Member(layer1rule10class3) -> backward_association
                (12,4), #  backward_association -> apply_class RequiredPort(layer1rule10class1)
                (7,13), # apply_class Member(layer1rule10class4) -> backward_association
                (13,4), #  backward_association -> apply_class RequiredPort(layer1rule10class1)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((5,'__ApplyAttribute'),('constant','AtomicComponentStructCData')), ((6,'__ApplyAttribute'),('constant','RequiredPort_port')), ((7,'__ApplyAttribute'),('constant','RequiredPort_ops')), ]

        
