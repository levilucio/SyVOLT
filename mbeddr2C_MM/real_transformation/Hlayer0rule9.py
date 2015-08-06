from core.himesis import Himesis
import uuid

class Hlayer0rule9(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule layer0rule9.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer0rule9, self).__init__(name='Hlayer0rule9', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """layer0rule9"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule9')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
 
        
        # match class RequiredPort(layer0rule9class0) node
        self.add_node()
        self.vs[3]["name"] = """layer0rule9class0""" 
        self.vs[3]["classtype"] = """RequiredPort"""
        self.vs[3]["mm__"] = """RequiredPort"""
        self.vs[3]["cardinality"] = """+""" 
        # match_contains node for class RequiredPort(layer0rule9class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        
        
        # apply class Member(layer0rule9class1) node
        self.add_node()
        self.vs[5]["name"] = """layer0rule9class1""" 
        self.vs[5]["classtype"] = """Member"""
        self.vs[5]["mm__"] = """Member"""
        self.vs[5]["cardinality"] = """1"""
        # apply_contains node for class Member(layer0rule9class1)
        self.add_node()
        self.vs[6]["mm__"] = """apply_contains"""
        # apply class VoidType(layer0rule9class2) node
        self.add_node()
        self.vs[7]["name"] = """layer0rule9class2""" 
        self.vs[7]["classtype"] = """VoidType"""
        self.vs[7]["mm__"] = """VoidType"""
        self.vs[7]["cardinality"] = """1"""
        # apply_contains node for class VoidType(layer0rule9class2)
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        # apply class PointerType(layer0rule9class3) node
        self.add_node()
        self.vs[9]["name"] = """layer0rule9class3""" 
        self.vs[9]["classtype"] = """PointerType"""
        self.vs[9]["mm__"] = """PointerType"""
        self.vs[9]["cardinality"] = """1"""
        # apply_contains node for class PointerType(layer0rule9class3)
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        
        
        
        # apply association Member--type-->PointerType node
        self.add_node()
        self.vs[11]["associationType"] = """type"""
        self.vs[11]["mm__"] = """directLink_T"""
        # apply association PointerType--baseType-->VoidType node
        self.add_node()
        self.vs[12]["associationType"] = """baseType"""
        self.vs[12]["mm__"] = """directLink_T"""
        
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class RequiredPort(layer0rule9class0)
                (1,6), # applymodel -> apply_contains
                (6,5), # apply_contains -> apply_class Member(layer0rule9class1)
                (1,8), # applymodel -> apply_contains
                (8,7), # apply_contains -> apply_class VoidType(layer0rule9class2)
                (1,10), # applymodel -> apply_contains
                (10,9), # apply_contains -> apply_class PointerType(layer0rule9class3)
                (5,11), # apply_class Member(layer0rule9class1) -> association type
                (11,9), # association type  -> apply_class PointerType(layer0rule9class3)
                (9,12), # apply_class PointerType(layer0rule9class3) -> association baseType
                (12,7), # association baseType  -> apply_class VoidType(layer0rule9class2)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((5,'name'),('concat',((3,'name'),('constant','__port')))), ((5,'__ApplyAttribute'),('constant','RequiredPort_port')), ]

        
