from core.himesis import Himesis
import uuid

class Hlayer1rule4(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule layer1rule4.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer1rule4, self).__init__(name='Hlayer1rule4', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer1rule4"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule4')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["attr1"] = """layer1rule4"""
        
        # match class Operation(layer1rule4class0) node
        self.add_node()
        
        self.vs[3]["mm__"] = """Operation""" 
        self.vs[3]["attr1"] = """+""" 
        # match class OperationParameter(layer1rule4class1) node
        self.add_node()
        
        self.vs[4]["mm__"] = """OperationParameter""" 
        self.vs[4]["attr1"] = """+""" 
        # match class StringType(layer1rule4class2) node
        self.add_node()
        
        self.vs[5]["mm__"] = """StringType""" 
        self.vs[5]["attr1"] = """+""" 
        
        
        # apply class FunctionRefType(layer1rule4class3) node
        self.add_node()

        self.vs[6]["mm__"] = """FunctionRefType""" 
        self.vs[6]["attr1"] = """1"""
        # apply class StringType(layer1rule4class4) node
        self.add_node()

        self.vs[7]["mm__"] = """StringType""" 
        self.vs[7]["attr1"] = """1"""
        
        
        # match association Operation--parameters-->OperationParameter node
        self.add_node()
        self.vs[8]["attr1"] = """parameters"""
        self.vs[8]["mm__"] = """directLink_S"""
        # match association OperationParameter--type-->StringType node
        self.add_node()
        self.vs[9]["attr1"] = """type"""
        self.vs[9]["mm__"] = """directLink_S"""
        
        # apply association FunctionRefType--argTypes-->StringType node
        self.add_node()
        self.vs[10]["attr1"] = """argTypes"""
        self.vs[10]["mm__"] = """directLink_T"""
        
        # backward association StringType---->StringType node
        self.add_node()

        self.vs[11]["mm__"] = """backward_link"""
        # backward association Operation---->FunctionRefType node
        self.add_node()

        self.vs[12]["mm__"] = """backward_link"""
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class Operation(layer1rule4class0)
                (0,4), # matchmodel -> match_class OperationParameter(layer1rule4class1)
                (0,5), # matchmodel -> match_class StringType(layer1rule4class2)
                (1,6), # applymodel -> -> apply_class FunctionRefType(layer1rule4class3)
                (1,7), # applymodel -> -> apply_class StringType(layer1rule4class4)
                (3,8), # match_class Operation(layer1rule4class0) -> association parameters
                (8,4), # association parameters  -> match_class OperationParameter(layer1rule4class1)
                (4,9), # match_class OperationParameter(layer1rule4class1) -> association type
                (9,5), # association type  -> match_class StringType(layer1rule4class2)
                (6,10), # apply_class FunctionRefType(layer1rule4class3) -> association argTypes
                (10,7), # association argTypes  -> apply_class StringType(layer1rule4class4)
                (7,11), # apply_class StringType(layer1rule4class4) -> backward_association
                (11,5), #  backward_association -> apply_class StringType(layer1rule4class2)
                (6,12), # apply_class FunctionRefType(layer1rule4class3) -> backward_association
                (12,3), #  backward_association -> apply_class Operation(layer1rule4class0)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((6,'__ApplyAttribute'),('constant','FunctionRefType')), ((7,'__ApplyAttribute'),('constant','StringType')), ]

        
