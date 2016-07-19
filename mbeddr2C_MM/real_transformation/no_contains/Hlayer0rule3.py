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
        self.vs[2]["attr1"] = """layer0rule3"""
        
        # match class StringType(layer0rule3class0) node
        self.add_node()
        
        self.vs[3]["mm__"] = """StringType""" 
        self.vs[3]["attr1"] = """+""" 
        
        
        # apply class StringType(layer0rule3class1) node
        self.add_node()

        self.vs[4]["mm__"] = """StringType""" 
        self.vs[4]["attr1"] = """1"""
        
        
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class StringType(layer0rule3class0)
                (1,4), # applymodel -> -> apply_class StringType(layer0rule3class1)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((4,'__ApplyAttribute'),('constant','StringType')), ]

        
