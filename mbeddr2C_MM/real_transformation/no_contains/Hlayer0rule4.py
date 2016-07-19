from core.himesis import Himesis
import uuid

class Hlayer0rule4(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule layer0rule4.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer0rule4, self).__init__(name='Hlayer0rule4', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer0rule4"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule4')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["attr1"] = """layer0rule4"""
        
        # match class VoidType(layer0rule4class0) node
        self.add_node()
        
        self.vs[3]["mm__"] = """VoidType""" 
        self.vs[3]["attr1"] = """+""" 
        
        
        # apply class VoidType(layer0rule4class1) node
        self.add_node()

        self.vs[4]["mm__"] = """VoidType""" 
        self.vs[4]["attr1"] = """1"""
        
        
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class VoidType(layer0rule4class0)
                (1,4), # applymodel -> -> apply_class VoidType(layer0rule4class1)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((4,'__ApplyAttribute'),('constant','VoidType')), ]

        
