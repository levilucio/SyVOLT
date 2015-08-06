from core.himesis import Himesis
import uuid

class Hlayer2rule1(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule layer2rule1.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer2rule1, self).__init__(name='Hlayer2rule1', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """layer2rule1"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer2rule1')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
 
        
        # match class StringType(layer2rule1class0) node
        self.add_node()
        self.vs[3]["name"] = """layer2rule1class0""" 
        self.vs[3]["classtype"] = """StringType"""
        self.vs[3]["mm__"] = """StringType"""
        self.vs[3]["cardinality"] = """+""" 
        # match_contains node for class StringType(layer2rule1class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        # match class OperationParameter(layer2rule1class1) node
        self.add_node()
        self.vs[5]["name"] = """layer2rule1class1""" 
        self.vs[5]["classtype"] = """OperationParameter"""
        self.vs[5]["mm__"] = """OperationParameter"""
        self.vs[5]["cardinality"] = """+""" 
        # match_contains node for class OperationParameter(layer2rule1class1)
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        
        
        # apply class StringType(layer2rule1class2) node
        self.add_node()
        self.vs[7]["name"] = """layer2rule1class2""" 
        self.vs[7]["classtype"] = """StringType"""
        self.vs[7]["mm__"] = """StringType"""
        self.vs[7]["cardinality"] = """1"""
        # apply_contains node for class StringType(layer2rule1class2)
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        # apply class Argument(layer2rule1class3) node
        self.add_node()
        self.vs[9]["name"] = """layer2rule1class3""" 
        self.vs[9]["classtype"] = """Argument"""
        self.vs[9]["mm__"] = """Argument"""
        self.vs[9]["cardinality"] = """1"""
        # apply_contains node for class Argument(layer2rule1class3)
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        
        
        # match association OperationParameter--type-->StringType node
        self.add_node()
        self.vs[11]["associationType"] = """type"""
        self.vs[11]["mm__"] = """directLink_S"""
        
        # apply association Argument--type-->StringType node
        self.add_node()
        self.vs[12]["associationType"] = """type"""
        self.vs[12]["mm__"] = """directLink_T"""
        
        # backward association OperationParameter---->Argument node
        self.add_node()
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class StringType(layer2rule1class0)
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class OperationParameter(layer2rule1class1)
                (1,8), # applymodel -> apply_contains
                (8,7), # apply_contains -> apply_class StringType(layer2rule1class2)
                (1,10), # applymodel -> apply_contains
                (10,9), # apply_contains -> apply_class Argument(layer2rule1class3)
                (5,11), # match_class OperationParameter(layer2rule1class1) -> association type
                (11,3), # association type  -> match_class StringType(layer2rule1class0)
                (9,12), # apply_class Argument(layer2rule1class3) -> association type
                (12,7), # association type  -> apply_class StringType(layer2rule1class2)
                (9,13), # apply_class Argument(layer2rule1class3) -> backward_association
                (13,5), #  backward_association -> apply_class OperationParameter(layer2rule1class1)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((9,'__ApplyAttribute'),('constant','ProvidedPortFunctionPrototypeArgument')), ]

        
