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
 
        
        # match class ClientServerInterface(layer0rule1class0) node
        self.add_node()
        self.vs[3]["name"] = """layer0rule1class0""" 
        self.vs[3]["classtype"] = """ClientServerInterface"""
        self.vs[3]["mm__"] = """ClientServerInterface"""
        self.vs[3]["cardinality"] = """+""" 
        # match_contains node for class ClientServerInterface(layer0rule1class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        # match class ImplementationModule(layer0rule1class1) node
        self.add_node()
        self.vs[5]["name"] = """layer0rule1class1""" 
        self.vs[5]["classtype"] = """ImplementationModule"""
        self.vs[5]["mm__"] = """ImplementationModule"""
        self.vs[5]["cardinality"] = """+""" 
        # match_contains node for class ImplementationModule(layer0rule1class1)
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        
        
        # apply class StructDeclaration(layer0rule1class2) node
        self.add_node()
        self.vs[7]["name"] = """layer0rule1class2""" 
        self.vs[7]["classtype"] = """StructDeclaration"""
        self.vs[7]["mm__"] = """StructDeclaration"""
        self.vs[7]["cardinality"] = """1"""
        # apply_contains node for class StructDeclaration(layer0rule1class2)
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        
        
        # match association ImplementationModule--contents-->ClientServerInterface node
        self.add_node()
        self.vs[9]["associationType"] = """contents"""
        self.vs[9]["mm__"] = """directLink_S"""
        
        
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class ClientServerInterface(layer0rule1class0)
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class ImplementationModule(layer0rule1class1)
                (1,8), # applymodel -> apply_contains
                (8,7), # apply_contains -> apply_class StructDeclaration(layer0rule1class2)
                (5,9), # match_class ImplementationModule(layer0rule1class1) -> association contents
                (9,3), # association contents  -> match_class ClientServerInterface(layer0rule1class0)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((7,'name'),('concat',((5,'name'),('concat',(('constant','_'),('concat',((3,'name'),('concat',(('constant','__'),('constant','idata')))))))))), ((7,'__ApplyAttribute'),('constant','ClientServerStructIData')), ]

        
