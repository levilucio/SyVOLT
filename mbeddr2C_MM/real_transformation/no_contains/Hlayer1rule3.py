from core.himesis import Himesis
import uuid

class Hlayer1rule3(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule layer1rule3.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer1rule3, self).__init__(name='Hlayer1rule3', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer1rule3"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule3')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["attr1"] = """layer1rule3"""
        
        # match class Operation(layer1rule3class0) node
        self.add_node()
        
        self.vs[3]["mm__"] = """Operation""" 
        self.vs[3]["attr1"] = """+""" 
        # match class StringType(layer1rule3class1) node
        self.add_node()
        
        self.vs[4]["mm__"] = """StringType""" 
        self.vs[4]["attr1"] = """+""" 
        
        
        # apply class FunctionRefType(layer1rule3class2) node
        self.add_node()

        self.vs[5]["mm__"] = """FunctionRefType""" 
        self.vs[5]["attr1"] = """1"""
        # apply class StringType(layer1rule3class3) node
        self.add_node()

        self.vs[6]["mm__"] = """StringType""" 
        self.vs[6]["attr1"] = """1"""
        
        
        # match association Operation--type-->StringType node
        self.add_node()
        self.vs[7]["attr1"] = """type"""
        self.vs[7]["mm__"] = """directLink_S"""
        
        # apply association FunctionRefType--returnType-->StringType node
        self.add_node()
        self.vs[8]["attr1"] = """returnType"""
        self.vs[8]["mm__"] = """directLink_T"""
        
        # backward association StringType---->StringType node
        self.add_node()

        self.vs[9]["mm__"] = """backward_link"""
        # backward association Operation---->FunctionRefType node
        self.add_node()

        self.vs[10]["mm__"] = """backward_link"""
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class Operation(layer1rule3class0)
                (0,4), # matchmodel -> match_class StringType(layer1rule3class1)
                (1,5), # applymodel -> -> apply_class FunctionRefType(layer1rule3class2)
                (1,6), # applymodel -> -> apply_class StringType(layer1rule3class3)
                (3,7), # match_class Operation(layer1rule3class0) -> association type
                (7,4), # association type  -> match_class StringType(layer1rule3class1)
                (5,8), # apply_class FunctionRefType(layer1rule3class2) -> association returnType
                (8,6), # association returnType  -> apply_class StringType(layer1rule3class3)
                (6,9), # apply_class StringType(layer1rule3class3) -> backward_association
                (9,4), #  backward_association -> apply_class StringType(layer1rule3class1)
                (5,10), # apply_class FunctionRefType(layer1rule3class2) -> backward_association
                (10,3), #  backward_association -> apply_class Operation(layer1rule3class0)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((5,'__ApplyAttribute'),('constant','FunctionRefType')), ((6,'__ApplyAttribute'),('constant','StringType')), ]

        
