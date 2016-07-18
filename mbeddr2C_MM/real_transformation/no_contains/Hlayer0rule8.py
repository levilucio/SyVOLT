from core.himesis import Himesis
import uuid

class Hlayer0rule8(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule layer0rule8.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer0rule8, self).__init__(name='Hlayer0rule8', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer0rule8"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule8')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["attr1"] = """layer0rule8"""
        
        # match class AtomicComponent(layer0rule8class0) node
        self.add_node()
        
        self.vs[3]["mm__"] = """AtomicComponent""" 
        self.vs[3]["attr1"] = """+""" 
        # match class ImplementationModule(layer0rule8class1) node
        self.add_node()
        
        self.vs[4]["mm__"] = """ImplementationModule""" 
        self.vs[4]["attr1"] = """+""" 
        
        
        # apply class TypeDef(layer0rule8class2) node
        self.add_node()

        self.vs[5]["mm__"] = """TypeDef""" 
        self.vs[5]["attr1"] = """1"""
        # apply class StructType(layer0rule8class3) node
        self.add_node()

        self.vs[6]["mm__"] = """StructType""" 
        self.vs[6]["attr1"] = """1"""
        
        
        # match association ImplementationModule--contents-->AtomicComponent node
        self.add_node()
        self.vs[7]["attr1"] = """contents"""
        self.vs[7]["mm__"] = """directLink_S"""
        
        # apply association TypeDef--original-->StructType node
        self.add_node()
        self.vs[8]["attr1"] = """original"""
        self.vs[8]["mm__"] = """directLink_T"""
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class AtomicComponent(layer0rule8class0)
                (0,4), # matchmodel -> match_class ImplementationModule(layer0rule8class1)
                (1,5), # applymodel -> -> apply_class TypeDef(layer0rule8class2)
                (1,6), # applymodel -> -> apply_class StructType(layer0rule8class3)
                (4,7), # match_class ImplementationModule(layer0rule8class1) -> association contents
                (7,3), # association contents  -> match_class AtomicComponent(layer0rule8class0)
                (5,8), # apply_class TypeDef(layer0rule8class2) -> association original
                (8,6), # association original  -> apply_class StructType(layer0rule8class3)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((5,'name'),('concat',((4,'name'),('concat',(('constant','_'),('concat',((3,'name'),('concat',(('constant','__'),('constant','cdata_t')))))))))), ((5,'__ApplyAttribute'),('constant','TypeDefComponentStruct')), ((6,'__ApplyAttribute'),('constant','TypeComponentStructType')), ]

        
