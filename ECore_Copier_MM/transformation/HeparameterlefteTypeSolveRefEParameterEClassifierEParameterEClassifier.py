from core.himesis import Himesis
import uuid

class HeparameterlefteTypeSolveRefEParameterEClassifierEParameterEClassifier(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule eparameterlefteTypeSolveRefEParameterEClassifierEParameterEClassifier.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HeparameterlefteTypeSolveRefEParameterEClassifierEParameterEClassifier, self).__init__(name='HeparameterlefteTypeSolveRefEParameterEClassifierEParameterEClassifier', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """eparameterlefteTypeSolveRefEParameterEClassifierEParameterEClassifier"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'eparameterlefteTypeSolveRefEParameterEClassifierEParameterEClassifier')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
 
        
        # match class EParameter() node
        self.add_node()

        self.vs[3]["mm__"] = """EParameter""" 
        self.vs[3]["attr1"] = """+""" 
        # match_contains node for class EParameter()
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        # match class EClassifier() node
        self.add_node()

        self.vs[5]["mm__"] = """EClassifier""" 
        self.vs[5]["attr1"] = """+""" 
        # match_contains node for class EClassifier()
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        
        
        # apply class EParameter() node
        self.add_node()

        self.vs[7]["mm__"] = """EParameter""" 
        self.vs[7]["attr1"] = """1"""
        # apply_contains node for class EParameter()
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        # apply class EClassifier() node
        self.add_node()

        self.vs[9]["mm__"] = """EClassifier""" 
        self.vs[9]["attr1"] = """1"""
        # apply_contains node for class EClassifier()
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        
        
        # match association EParameter--eType-->EClassifier node
        self.add_node()
        self.vs[11]["attr1"] = """eType"""
        self.vs[11]["mm__"] = """directLink_S"""
        
        # apply association EParameter--eType-->EClassifier node
        self.add_node()
        self.vs[12]["attr1"] = """eType"""
        self.vs[12]["mm__"] = """directLink_T"""
        
        # backward association EParameter---->EParameter node
        self.add_node()

        self.vs[13]["mm__"] = """backward_link"""
        # backward association EClassifier---->EClassifier node
        self.add_node()

        self.vs[14]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class EParameter()
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class EClassifier()
                (1,8), # applymodel -> apply_contains
                (8,7), # apply_contains -> apply_class EParameter()
                (1,10), # applymodel -> apply_contains
                (10,9), # apply_contains -> apply_class EClassifier()
                (3,11), # match_class EParameter() -> association eType
                (11,5), # association eType  -> match_class EClassifier()
                (7,12), # apply_class EParameter() -> association eType
                (12,9), # association eType  -> apply_class EClassifier()
                (7,13), # apply_class EParameter() -> backward_association
                (13,3), #  backward_association -> apply_class EParameter()
                (9,14), # apply_class EClassifier() -> backward_association
                (14,5), #  backward_association -> apply_class EClassifier()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((7,'ApplyAttribute'),('constant','solveRef')), ((9,'ApplyAttribute'),('constant','solveRef')), ]

        
