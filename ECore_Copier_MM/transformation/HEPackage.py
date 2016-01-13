from core.himesis import Himesis
import uuid

class HEPackage(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule EPackage.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HEPackage, self).__init__(name='HEPackage', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """EPackage"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EPackage')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
 
        
        # match class EPackage() node
        self.add_node()

        self.vs[3]["mm__"] = """EPackage""" 
        self.vs[3]["attr1"] = """+""" 
        # match_contains node for class EPackage()
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        
        
        # apply class EPackage() node
        self.add_node()

        self.vs[5]["mm__"] = """EPackage""" 
        self.vs[5]["attr1"] = """1"""
        # apply_contains node for class EPackage()
        self.add_node()
        self.vs[6]["mm__"] = """apply_contains"""
        
        
        
        
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class EPackage()
                (1,6), # applymodel -> apply_contains
                (6,5), # apply_contains -> apply_class EPackage()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((5,'name'),(3,'name')), ((5,'nsURI'),(3,'nsURI')), ((5,'nsPrefix'),(3,'nsPrefix')), ((5,'ApplyAttribute'),('constant','solveRef')), ]

        
