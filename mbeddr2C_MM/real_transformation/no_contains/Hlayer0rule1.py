from core.himesis import Himesis
import uuid

class Hlayer0rule1(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule layer0rule1.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer0rule1, self).__init__(name='Hlayer0rule1', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer0rule1"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule1')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["attr1"] = """layer0rule1"""
        
        # match class ClientServerInterface(layer0rule1class0) node
        self.add_node()
        
        self.vs[3]["mm__"] = """ClientServerInterface""" 
        self.vs[3]["attr1"] = """+""" 
        # match class ImplementationModule(layer0rule1class1) node
        self.add_node()
        
        self.vs[4]["mm__"] = """ImplementationModule""" 
        self.vs[4]["attr1"] = """+""" 
        
        
        # apply class StructDeclaration(layer0rule1class2) node
        self.add_node()

        self.vs[5]["mm__"] = """StructDeclaration""" 
        self.vs[5]["attr1"] = """1"""
        
        
        # match association ImplementationModule--contents-->ClientServerInterface node
        self.add_node()
        self.vs[6]["attr1"] = """contents"""
        self.vs[6]["mm__"] = """directLink_S"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class ClientServerInterface(layer0rule1class0)
                (0,4), # matchmodel -> match_class ImplementationModule(layer0rule1class1)
                (1,5), # applymodel -> -> apply_class StructDeclaration(layer0rule1class2)
                (4,6), # match_class ImplementationModule(layer0rule1class1) -> association contents
                (6,3), # association contents  -> match_class ClientServerInterface(layer0rule1class0)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((5,'name'),('concat',((4,'name'),('concat',(('constant','_'),('concat',((3,'name'),('concat',(('constant','__'),('constant','idata')))))))))), ((5,'__ApplyAttribute'),('constant','ClientServerStructIData')), ]

        
