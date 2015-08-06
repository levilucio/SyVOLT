from core.himesis import Himesis
import uuid

class Hlayer0rule3(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule layer0rule3.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer0rule3, self).__init__(name='Hlayer0rule3', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """layer0rule3"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule3')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
 
        
        # match class StringType(layer0rule3class0) node
        self.add_node()
        self.vs[3]["name"] = """layer0rule3class0""" 
        self.vs[3]["classtype"] = """StringType"""
        self.vs[3]["mm__"] = """StringType"""
        self.vs[3]["cardinality"] = """+""" 
        # match_contains node for class StringType(layer0rule3class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        
        
        # apply class StringType(layer0rule3class1) node
        self.add_node()
        self.vs[5]["name"] = """layer0rule3class1""" 
        self.vs[5]["classtype"] = """StringType"""
        self.vs[5]["mm__"] = """StringType"""
        self.vs[5]["cardinality"] = """1"""
        # apply_contains node for class StringType(layer0rule3class1)
        self.add_node()
        self.vs[6]["mm__"] = """apply_contains"""
        
        
        
        
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class StringType(layer0rule3class0)
                (1,6), # applymodel -> apply_contains
                (6,5), # apply_contains -> apply_class StringType(layer0rule3class1)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((5,'__ApplyAttribute'),('constant','StringType')), ]

        
