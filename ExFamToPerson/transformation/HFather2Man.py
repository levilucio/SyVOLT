from core.himesis import Himesis
import uuid

class HFather2Man(Himesis):
    def __init__(self, *args, **kwargs):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule Father2Man.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HFather2Man, self).__init__(name='HFather2Man', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """Father2Man"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Father2Man')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
 
        
        # match class Parent() node
        self.add_node()

        self.vs[3]["mm__"] = """Parent""" 
        self.vs[3]["attr1"] = """+""" 
        # match_contains node for class Parent()
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        # match class Family() node
        self.add_node()

        self.vs[5]["mm__"] = """Family""" 
        self.vs[5]["attr1"] = """1""" 
        # match_contains node for class Family()
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        
        
        # apply class Man() node
        self.add_node()

        self.vs[7]["mm__"] = """Man""" 
        self.vs[7]["attr1"] = """1"""
        # apply_contains node for class Man()
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        
        
        # match association Parent--family-->Family node
        self.add_node()
        self.vs[9]["attr1"] = """family"""
        self.vs[9]["mm__"] = """directLink_S"""
        # match association Family--fathers-->Parent node
        self.add_node()
        self.vs[10]["attr1"] = """fathers"""
        self.vs[10]["mm__"] = """directLink_S"""
        
        
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class Parent()
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class Family()
                (1,8), # applymodel -> apply_contains
                (8,7), # apply_contains -> apply_class Man()
                (3,9), # match_class Parent() -> association family
                (9,5), # association family  -> match_class Family()
                (5,10), # match_class Family() -> association fathers
                (10,3), # association fathers  -> match_class Parent()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((7,'fullName'),('concat',((3,'firstName'),(5,'lastName')))), ]

        
