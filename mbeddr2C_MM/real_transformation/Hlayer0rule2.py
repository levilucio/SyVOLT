from core.himesis import Himesis
import uuid

class Hlayer0rule2(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule layer0rule2.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer0rule2, self).__init__(name='Hlayer0rule2', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """layer0rule2"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule2')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
 
        
        # match class Operation(layer0rule2class0) node
        self.add_node()

        self.vs[3]["mm__"] = """Operation""" 
        self.vs[3]["attr1"] = """+""" 
        # match_contains node for class Operation(layer0rule2class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        
        
        # apply class CFunctionPointerStructMember(layer0rule2class2) node
        self.add_node()

        self.vs[5]["mm__"] = """CFunctionPointerStructMember""" 
        self.vs[5]["attr1"] = """1"""
        # apply_contains node for class CFunctionPointerStructMember(layer0rule2class2)
        self.add_node()
        self.vs[6]["mm__"] = """apply_contains"""
        # apply class FunctionRefType(layer0rule2class3) node
        self.add_node()

        self.vs[7]["mm__"] = """FunctionRefType""" 
        self.vs[7]["attr1"] = """1"""
        # apply_contains node for class FunctionRefType(layer0rule2class3)
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        # apply class PointerType(layer0rule5class2) node
        self.add_node()

        self.vs[9]["mm__"] = """PointerType""" 
        self.vs[9]["attr1"] = """1"""
        # apply_contains node for class PointerType(layer0rule5class2)
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        # apply class VoidType(layer0rule5class3) node
        self.add_node()

        self.vs[11]["mm__"] = """VoidType""" 
        self.vs[11]["attr1"] = """1"""
        # apply_contains node for class VoidType(layer0rule5class3)
        self.add_node()
        self.vs[12]["mm__"] = """apply_contains"""
        
        
        
        # apply association CFunctionPointerStructMember--type-->FunctionRefType node
        self.add_node()
        self.vs[13]["attr1"] = """type"""
        self.vs[13]["mm__"] = """directLink_T"""
        # apply association FunctionRefType--argTypes-->PointerType node
        self.add_node()
        self.vs[14]["attr1"] = """argTypes"""
        self.vs[14]["mm__"] = """directLink_T"""
        # apply association PointerType--baseType-->VoidType node
        self.add_node()
        self.vs[15]["attr1"] = """baseType"""
        self.vs[15]["mm__"] = """directLink_T"""
        
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class Operation(layer0rule2class0)
                (1,6), # applymodel -> apply_contains
                (6,5), # apply_contains -> apply_class CFunctionPointerStructMember(layer0rule2class2)
                (1,8), # applymodel -> apply_contains
                (8,7), # apply_contains -> apply_class FunctionRefType(layer0rule2class3)
                (1,10), # applymodel -> apply_contains
                (10,9), # apply_contains -> apply_class PointerType(layer0rule5class2)
                (1,12), # applymodel -> apply_contains
                (12,11), # apply_contains -> apply_class VoidType(layer0rule5class3)
                (5,13), # apply_class CFunctionPointerStructMember(layer0rule2class2) -> association type
                (13,7), # association type  -> apply_class FunctionRefType(layer0rule2class3)
                (7,14), # apply_class FunctionRefType(layer0rule2class3) -> association argTypes
                (14,9), # association argTypes  -> apply_class PointerType(layer0rule5class2)
                (9,15), # apply_class PointerType(layer0rule5class2) -> association baseType
                (15,11), # association baseType  -> apply_class VoidType(layer0rule5class3)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((5,'name'),(3,'name')), ((5,'__ApplyAttribute'),('constant','CFunctionPointerStructMember')), ((7,'__ApplyAttribute'),('constant','FunctionRefType')), ((9,'__ApplyAttribute'),('constant','InstancePointer')), ]

        
