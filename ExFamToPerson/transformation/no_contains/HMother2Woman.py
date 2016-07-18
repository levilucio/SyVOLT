from core.himesis import Himesis
import uuid

class HMother2Woman(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule Mother2Woman.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HMother2Woman, self).__init__(name='HMother2Woman', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """Mother2Woman"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Mother2Woman')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["attr1"] = """Mother2Woman"""
        
        # match class Parent() node
        self.add_node()
        
        self.vs[3]["mm__"] = """Parent""" 
        self.vs[3]["attr1"] = """+""" 
        # match class Family() node
        self.add_node()
        
        self.vs[4]["mm__"] = """Family""" 
        self.vs[4]["attr1"] = """1""" 
        
        
        # apply class Woman() node
        self.add_node()

        self.vs[5]["mm__"] = """Woman""" 
        self.vs[5]["attr1"] = """1"""
        
        
        # match association Parent--family-->Family node
        self.add_node()
        self.vs[6]["attr1"] = """family"""
        self.vs[6]["mm__"] = """directLink_S"""
        # match association Family--mothers-->Parent node
        self.add_node()
        self.vs[7]["attr1"] = """mothers"""
        self.vs[7]["mm__"] = """directLink_S"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class Parent()
                (0,4), # matchmodel -> match_class Family()
                (1,5), # applymodel -> -> apply_class Woman()
                (3,6), # match_class Parent() -> association family
                (6,4), # association family  -> match_class Family()
                (4,7), # match_class Family() -> association mothers
                (7,3), # association mothers  -> match_class Parent()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((5,'fullName'),('concat',((3,'firstName'),(4,'lastName')))), ]

        
