from core.himesis import Himesis
import uuid

class HeclasslefteStructuralFeaturesSolveRefEClassEStructuralFeatureEClassEStructuralFeature(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule eclasslefteStructuralFeaturesSolveRefEClassEStructuralFeatureEClassEStructuralFeature.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HeclasslefteStructuralFeaturesSolveRefEClassEStructuralFeatureEClassEStructuralFeature, self).__init__(name='HeclasslefteStructuralFeaturesSolveRefEClassEStructuralFeatureEClassEStructuralFeature', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """eclasslefteStructuralFeaturesSolveRefEClassEStructuralFeatureEClassEStructuralFeature"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'eclasslefteStructuralFeaturesSolveRefEClassEStructuralFeatureEClassEStructuralFeature')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
 
        
        # match class EClass() node
        self.add_node()

        self.vs[3]["mm__"] = """EClass""" 
        self.vs[3]["attr1"] = """+""" 
        # match_contains node for class EClass()
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        # match class EStructuralFeature() node
        self.add_node()

        self.vs[5]["mm__"] = """EStructuralFeature""" 
        self.vs[5]["attr1"] = """+""" 
        # match_contains node for class EStructuralFeature()
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        
        
        # apply class EClass() node
        self.add_node()

        self.vs[7]["mm__"] = """EClass""" 
        self.vs[7]["attr1"] = """1"""
        # apply_contains node for class EClass()
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        # apply class EStructuralFeature() node
        self.add_node()

        self.vs[9]["mm__"] = """EStructuralFeature""" 
        self.vs[9]["attr1"] = """1"""
        # apply_contains node for class EStructuralFeature()
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        
        
        # match association EClass--eStructuralFeatures-->EStructuralFeature node
        self.add_node()
        self.vs[11]["attr1"] = """eStructuralFeatures"""
        self.vs[11]["mm__"] = """directLink_S"""
        
        # apply association EClass--eStructuralFeatures-->EStructuralFeature node
        self.add_node()
        self.vs[12]["attr1"] = """eStructuralFeatures"""
        self.vs[12]["mm__"] = """directLink_T"""
        
        # backward association EClass---->EClass node
        self.add_node()

        self.vs[13]["mm__"] = """backward_link"""
        # backward association EStructuralFeature---->EStructuralFeature node
        self.add_node()

        self.vs[14]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class EClass()
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class EStructuralFeature()
                (1,8), # applymodel -> apply_contains
                (8,7), # apply_contains -> apply_class EClass()
                (1,10), # applymodel -> apply_contains
                (10,9), # apply_contains -> apply_class EStructuralFeature()
                (3,11), # match_class EClass() -> association eStructuralFeatures
                (11,5), # association eStructuralFeatures  -> match_class EStructuralFeature()
                (7,12), # apply_class EClass() -> association eStructuralFeatures
                (12,9), # association eStructuralFeatures  -> apply_class EStructuralFeature()
                (7,13), # apply_class EClass() -> backward_association
                (13,3), #  backward_association -> apply_class EClass()
                (9,14), # apply_class EStructuralFeature() -> backward_association
                (14,5), #  backward_association -> apply_class EStructuralFeature()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((7,'ApplyAttribute'),('constant','solveRef')), ((9,'ApplyAttribute'),('constant','solveRef')), ]

        
