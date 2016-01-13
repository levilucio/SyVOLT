from core.himesis import Himesis
import uuid

class HeenumlefteLiteralsSolveRefEEnumEEnumLiteralEEnumEEnumLiteral(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule eenumlefteLiteralsSolveRefEEnumEEnumLiteralEEnumEEnumLiteral.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HeenumlefteLiteralsSolveRefEEnumEEnumLiteralEEnumEEnumLiteral, self).__init__(name='HeenumlefteLiteralsSolveRefEEnumEEnumLiteralEEnumEEnumLiteral', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """eenumlefteLiteralsSolveRefEEnumEEnumLiteralEEnumEEnumLiteral"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'eenumlefteLiteralsSolveRefEEnumEEnumLiteralEEnumEEnumLiteral')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
 
        
        # match class EEnum() node
        self.add_node()

        self.vs[3]["mm__"] = """EEnum""" 
        self.vs[3]["attr1"] = """+""" 
        # match_contains node for class EEnum()
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        # match class EEnumLiteral() node
        self.add_node()

        self.vs[5]["mm__"] = """EEnumLiteral""" 
        self.vs[5]["attr1"] = """+""" 
        # match_contains node for class EEnumLiteral()
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        
        
        # apply class EEnum() node
        self.add_node()

        self.vs[7]["mm__"] = """EEnum""" 
        self.vs[7]["attr1"] = """1"""
        # apply_contains node for class EEnum()
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        # apply class EEnumLiteral() node
        self.add_node()

        self.vs[9]["mm__"] = """EEnumLiteral""" 
        self.vs[9]["attr1"] = """1"""
        # apply_contains node for class EEnumLiteral()
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        
        
        # match association EEnum--eLiterals-->EEnumLiteral node
        self.add_node()
        self.vs[11]["attr1"] = """eLiterals"""
        self.vs[11]["mm__"] = """directLink_S"""
        
        # apply association EEnum--eLiterals-->EEnumLiteral node
        self.add_node()
        self.vs[12]["attr1"] = """eLiterals"""
        self.vs[12]["mm__"] = """directLink_T"""
        
        # backward association EEnum---->EEnum node
        self.add_node()

        self.vs[13]["mm__"] = """backward_link"""
        # backward association EEnumLiteral---->EEnumLiteral node
        self.add_node()

        self.vs[14]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class EEnum()
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class EEnumLiteral()
                (1,8), # applymodel -> apply_contains
                (8,7), # apply_contains -> apply_class EEnum()
                (1,10), # applymodel -> apply_contains
                (10,9), # apply_contains -> apply_class EEnumLiteral()
                (3,11), # match_class EEnum() -> association eLiterals
                (11,5), # association eLiterals  -> match_class EEnumLiteral()
                (7,12), # apply_class EEnum() -> association eLiterals
                (12,9), # association eLiterals  -> apply_class EEnumLiteral()
                (7,13), # apply_class EEnum() -> backward_association
                (13,3), #  backward_association -> apply_class EEnum()
                (9,14), # apply_class EEnumLiteral() -> backward_association
                (14,5), #  backward_association -> apply_class EEnumLiteral()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((7,'ApplyAttribute'),('constant','solveRef')), ((9,'ApplyAttribute'),('constant','solveRef')), ]

        
