from core.himesis import Himesis
import uuid

class Hlayer0rule6(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule layer0rule6.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer0rule6, self).__init__(name='Hlayer0rule6', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """layer0rule6"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule6')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
 
        
        # match class ClientServerInterface(layer0rule6class0) node
        self.add_node()

        self.vs[3]["mm__"] = """ClientServerInterface""" 
        self.vs[3]["attr1"] = """+""" 
        # match_contains node for class ClientServerInterface(layer0rule6class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        # match class ImplementationModule(layer0rule6class1) node
        self.add_node()

        self.vs[5]["mm__"] = """ImplementationModule""" 
        self.vs[5]["attr1"] = """+""" 
        # match_contains node for class ImplementationModule(layer0rule6class1)
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        
        
        # apply class TypeDef(layer0rule6class2) node
        self.add_node()

        self.vs[7]["mm__"] = """TypeDef""" 
        self.vs[7]["attr1"] = """1"""
        # apply_contains node for class TypeDef(layer0rule6class2)
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        # apply class StructType(layer0rule6class3) node
        self.add_node()

        self.vs[9]["mm__"] = """StructType""" 
        self.vs[9]["attr1"] = """1"""
        # apply_contains node for class StructType(layer0rule6class3)
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        
        
        # match association ImplementationModule--contents-->ClientServerInterface node
        self.add_node()
        self.vs[11]["attr1"] = """contents"""
        self.vs[11]["mm__"] = """directLink_S"""
        
        # apply association TypeDef--original-->StructType node
        self.add_node()
        self.vs[12]["attr1"] = """original"""
        self.vs[12]["mm__"] = """directLink_T"""
        
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class ClientServerInterface(layer0rule6class0)
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class ImplementationModule(layer0rule6class1)
                (1,8), # applymodel -> apply_contains
                (8,7), # apply_contains -> apply_class TypeDef(layer0rule6class2)
                (1,10), # applymodel -> apply_contains
                (10,9), # apply_contains -> apply_class StructType(layer0rule6class3)
                (5,11), # match_class ImplementationModule(layer0rule6class1) -> association contents
                (11,3), # association contents  -> match_class ClientServerInterface(layer0rule6class0)
                (7,12), # apply_class TypeDef(layer0rule6class2) -> association original
                (12,9), # association original  -> apply_class StructType(layer0rule6class3)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((7,'name'),('concat',((5,'name'),('concat',(('constant','_'),('concat',((3,'name'),('concat',(('constant','__'),('constant','idata_t')))))))))), ((7,'__ApplyAttribute'),('constant','TypeDefInterfaceStruct')), ((9,'__ApplyAttribute'),('constant','TypeDefInterfaceStructType')), ]

        
