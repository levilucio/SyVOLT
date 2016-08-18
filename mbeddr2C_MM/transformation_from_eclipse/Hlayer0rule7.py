from core.himesis import Himesis
import uuid

class Hlayer0rule7(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule layer0rule7.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer0rule7, self).__init__(name='Hlayer0rule7', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """layer0rule7"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule7')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
 
        
        # match class AtomicComponent(layer0rule7class0) node
        self.add_node()

        self.vs[3]["mm__"] = """AtomicComponent""" 
        self.vs[3]["attr1"] = """+""" 
        # match_contains node for class AtomicComponent(layer0rule7class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        # match class ImplementationModule(layer0rule7class1) node
        self.add_node()

        self.vs[5]["mm__"] = """ImplementationModule""" 
        self.vs[5]["attr1"] = """+""" 
        # match_contains node for class ImplementationModule(layer0rule7class1)
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        
        
        # apply class StructDeclaration(layer0rule7class2) node
        self.add_node()

        self.vs[7]["mm__"] = """StructDeclaration""" 
        self.vs[7]["attr1"] = """1"""
        # apply_contains node for class StructDeclaration(layer0rule7class2)
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        # apply class Member(layer0rule7class3) node
        self.add_node()

        self.vs[9]["mm__"] = """Member""" 
        self.vs[9]["attr1"] = """1"""
        # apply_contains node for class Member(layer0rule7class3)
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        # apply class Int32Type(layer0rule7class4) node
        self.add_node()

        self.vs[11]["mm__"] = """Int32Type""" 
        self.vs[11]["attr1"] = """1"""
        # apply_contains node for class Int32Type(layer0rule7class4)
        self.add_node()
        self.vs[12]["mm__"] = """apply_contains"""
        
        
        # match association ImplementationModule--contents-->AtomicComponent node
        self.add_node()
        self.vs[13]["attr1"] = """contents"""
        self.vs[13]["mm__"] = """directLink_S"""
        
        # apply association StructDeclaration--members-->Member node
        self.add_node()
        self.vs[14]["attr1"] = """members"""
        self.vs[14]["mm__"] = """directLink_T"""
        # apply association Member--type-->Int32Type node
        self.add_node()
        self.vs[15]["attr1"] = """type"""
        self.vs[15]["mm__"] = """directLink_T"""
        
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class AtomicComponent(layer0rule7class0)
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class ImplementationModule(layer0rule7class1)
                (1,8), # applymodel -> apply_contains
                (8,7), # apply_contains -> apply_class StructDeclaration(layer0rule7class2)
                (1,10), # applymodel -> apply_contains
                (10,9), # apply_contains -> apply_class Member(layer0rule7class3)
                (1,12), # applymodel -> apply_contains
                (12,11), # apply_contains -> apply_class Int32Type(layer0rule7class4)
                (5,13), # match_class ImplementationModule(layer0rule7class1) -> association contents
                (13,3), # association contents  -> match_class AtomicComponent(layer0rule7class0)
                (7,14), # apply_class StructDeclaration(layer0rule7class2) -> association members
                (14,9), # association members  -> apply_class Member(layer0rule7class3)
                (9,15), # apply_class Member(layer0rule7class3) -> association type
                (15,11), # association type  -> apply_class Int32Type(layer0rule7class4)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((7,'name'),('concat',((5,'name'),('concat',(('constant','_'),('concat',((3,'name'),('concat',(('constant','__'),('constant','cdata')))))))))), ((7,'__ApplyAttribute'),('constant','AtomicComponentStructCData')), ((9,'name'),('constant','aMemberSoTheStructIsNotEmpty')), ]

        
