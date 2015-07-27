from core.himesis import Himesis
import uuid

class Hlayer2rule3(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule layer2rule3.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer2rule3, self).__init__(name='Hlayer2rule3', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """layer2rule3"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer2rule3')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["rulename"] = """layer2rule3"""
        
        # match class Operation(layer2rule3class0) node
        self.add_node()
        self.vs[3]["name"] = """layer2rule3class0""" 
        self.vs[3]["classtype"] = """Operation"""
        self.vs[3]["mm__"] = """Operation"""
        self.vs[3]["cardinality"] = """+""" 
        # match_contains node for class Operation(layer2rule3class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        
        
        # apply class FunctionPrototype(layer2rule3class1) node
        self.add_node()
        self.vs[5]["name"] = """layer2rule3class1""" 
        self.vs[5]["classtype"] = """FunctionPrototype"""
        self.vs[5]["mm__"] = """FunctionPrototype"""
        self.vs[5]["cardinality"] = """1"""
        # apply_contains node for class FunctionPrototype(layer2rule3class1)
        self.add_node()
        self.vs[6]["mm__"] = """apply_contains"""
        # apply class Argument(layer2rule3class2) node
        self.add_node()
        self.vs[7]["name"] = """layer2rule3class2""" 
        self.vs[7]["classtype"] = """Argument"""
        self.vs[7]["mm__"] = """Argument"""
        self.vs[7]["cardinality"] = """1"""
        # apply_contains node for class Argument(layer2rule3class2)
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        # apply class VoidType(layer2rule3class3) node
        self.add_node()
        self.vs[9]["name"] = """layer2rule3class3""" 
        self.vs[9]["classtype"] = """VoidType"""
        self.vs[9]["mm__"] = """VoidType"""
        self.vs[9]["cardinality"] = """1"""
        # apply_contains node for class VoidType(layer2rule3class3)
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        # apply class PointerType(layer2rule3class4) node
        self.add_node()
        self.vs[11]["name"] = """layer2rule3class4""" 
        self.vs[11]["classtype"] = """PointerType"""
        self.vs[11]["mm__"] = """PointerType"""
        self.vs[11]["cardinality"] = """1"""
        # apply_contains node for class PointerType(layer2rule3class4)
        self.add_node()
        self.vs[12]["mm__"] = """apply_contains"""
        
        
        
        # apply association FunctionPrototype--arguments-->Argument node
        self.add_node()
        self.vs[13]["associationType"] = """arguments"""
        self.vs[13]["mm__"] = """directLink_T"""
        # apply association Argument--type-->PointerType node
        self.add_node()
        self.vs[14]["associationType"] = """type"""
        self.vs[14]["mm__"] = """directLink_T"""
        # apply association PointerType--baseType-->VoidType node
        self.add_node()
        self.vs[15]["associationType"] = """baseType"""
        self.vs[15]["mm__"] = """directLink_T"""
        
        # backward association Operation---->FunctionPrototype node
        self.add_node()
        self.vs[16]["type"] = """ruleDef"""
        self.vs[16]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class Operation(layer2rule3class0)
                (1,6), # applymodel -> apply_contains
                (6,5), # apply_contains -> apply_class FunctionPrototype(layer2rule3class1)
                (1,8), # applymodel -> apply_contains
                (8,7), # apply_contains -> apply_class Argument(layer2rule3class2)
                (1,10), # applymodel -> apply_contains
                (10,9), # apply_contains -> apply_class VoidType(layer2rule3class3)
                (1,12), # applymodel -> apply_contains
                (12,11), # apply_contains -> apply_class PointerType(layer2rule3class4)
                (5,13), # apply_class FunctionPrototype(layer2rule3class1) -> association arguments
                (13,7), # association arguments  -> apply_class Argument(layer2rule3class2)
                (7,14), # apply_class Argument(layer2rule3class2) -> association type
                (14,11), # association type  -> apply_class PointerType(layer2rule3class4)
                (11,15), # apply_class PointerType(layer2rule3class4) -> association baseType
                (15,9), # association baseType  -> apply_class VoidType(layer2rule3class3)
                (5,16), # apply_class FunctionPrototype(layer2rule3class1) -> backward_association
                (16,3), #  backward_association -> apply_class Operation(layer2rule3class0)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])
		
        # Add the attribute equations
        self["equations"] = [((5,'__ApplyAttribute'),('constant','ProvidedPortFunctionPrototype')), ((7,'__ApplyAttribute'),('constant','ProvidedPortFunctionPrototypeInstanceArgument')), ((7,'name'),('constant','___id')), ]

        
