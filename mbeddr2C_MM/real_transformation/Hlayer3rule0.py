from core.himesis import Himesis
import uuid

class Hlayer3rule0(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule layer3rule0.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer3rule0, self).__init__(name='Hlayer3rule0', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """layer3rule0"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule0')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["rulename"] = """layer3rule0"""
        
        # match class ImplementationModule(layer3rule0class0) node
        self.add_node()
        self.vs[3]["name"] = """layer3rule0class0""" 
        self.vs[3]["classtype"] = """ImplementationModule"""
        self.vs[3]["mm__"] = """ImplementationModule"""
        self.vs[3]["cardinality"] = """+""" 
        # match_contains node for class ImplementationModule(layer3rule0class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        # match class Function(layer3rule0class1) node
        self.add_node()
        self.vs[5]["name"] = """layer3rule0class1""" 
        self.vs[5]["classtype"] = """Function"""
        self.vs[5]["mm__"] = """Function"""
        self.vs[5]["cardinality"] = """+""" 
        # match_contains node for class Function(layer3rule0class1)
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        # match class Int32Type(layer3rule0class2) node
        self.add_node()
        self.vs[7]["name"] = """layer3rule0class2""" 
        self.vs[7]["classtype"] = """Int32Type"""
        self.vs[7]["mm__"] = """Int32Type"""
        self.vs[7]["cardinality"] = """+""" 
        # match_contains node for class Int32Type(layer3rule0class2)
        self.add_node()
        self.vs[8]["mm__"] = """match_contains"""
        
        
        # apply class ImplementationModule(layer3rule0class3) node
        self.add_node()
        self.vs[9]["name"] = """layer3rule0class3""" 
        self.vs[9]["classtype"] = """ImplementationModule"""
        self.vs[9]["mm__"] = """ImplementationModule"""
        self.vs[9]["cardinality"] = """1"""
        # apply_contains node for class ImplementationModule(layer3rule0class3)
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        # apply class FunctionPrototype(layer3rule0class4) node
        self.add_node()
        self.vs[11]["name"] = """layer3rule0class4""" 
        self.vs[11]["classtype"] = """FunctionPrototype"""
        self.vs[11]["mm__"] = """FunctionPrototype"""
        self.vs[11]["cardinality"] = """1"""
        # apply_contains node for class FunctionPrototype(layer3rule0class4)
        self.add_node()
        self.vs[12]["mm__"] = """apply_contains"""
        # apply class VoidType(layer3rule0class5) node
        self.add_node()
        self.vs[13]["name"] = """layer3rule0class5""" 
        self.vs[13]["classtype"] = """VoidType"""
        self.vs[13]["mm__"] = """VoidType"""
        self.vs[13]["cardinality"] = """1"""
        # apply_contains node for class VoidType(layer3rule0class5)
        self.add_node()
        self.vs[14]["mm__"] = """apply_contains"""
        
        
        # match association ImplementationModule--contents-->Function node
        self.add_node()
        self.vs[15]["associationType"] = """contents"""
        self.vs[15]["mm__"] = """directLink_S"""
        # match association Function--type-->Int32Type node
        self.add_node()
        self.vs[16]["associationType"] = """type"""
        self.vs[16]["mm__"] = """directLink_S"""
        
        # apply association ImplementationModule--contents-->FunctionPrototype node
        self.add_node()
        self.vs[17]["associationType"] = """contents"""
        self.vs[17]["mm__"] = """directLink_T"""
        # apply association FunctionPrototype--type-->VoidType node
        self.add_node()
        self.vs[18]["associationType"] = """type"""
        self.vs[18]["mm__"] = """directLink_T"""
        
        # backward association ImplementationModule---->ImplementationModule node
        self.add_node()
        self.vs[19]["type"] = """ruleDef"""
        self.vs[19]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class ImplementationModule(layer3rule0class0)
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class Function(layer3rule0class1)
                (0,8), # matchmodel -> match_contains
                (8,7), # match_contains -> match_class Int32Type(layer3rule0class2)
                (1,10), # applymodel -> apply_contains
                (10,9), # apply_contains -> apply_class ImplementationModule(layer3rule0class3)
                (1,12), # applymodel -> apply_contains
                (12,11), # apply_contains -> apply_class FunctionPrototype(layer3rule0class4)
                (1,14), # applymodel -> apply_contains
                (14,13), # apply_contains -> apply_class VoidType(layer3rule0class5)
                (3,15), # match_class ImplementationModule(layer3rule0class0) -> association contents
                (15,5), # association contents  -> match_class Function(layer3rule0class1)
                (5,16), # match_class Function(layer3rule0class1) -> association type
                (16,7), # association type  -> match_class Int32Type(layer3rule0class2)
                (9,17), # apply_class ImplementationModule(layer3rule0class3) -> association contents
                (17,11), # association contents  -> apply_class FunctionPrototype(layer3rule0class4)
                (11,18), # apply_class FunctionPrototype(layer3rule0class4) -> association type
                (18,13), # association type  -> apply_class VoidType(layer3rule0class5)
                (9,19), # apply_class ImplementationModule(layer3rule0class3) -> backward_association
                (19,3), #  backward_association -> apply_class ImplementationModule(layer3rule0class0)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])
		
        # Add the attribute equations
        self["equations"] = [((5,'name'),('constant','main')), ((9,'__ApplyAttribute'),('constant','ImplementationModule')), ((11,'name'),('concat',((3,'name'),('constant','_blockexpr_main_2')))), ((11,'__ApplyAttribute'),('constant','Main2Prototype')), ]

        
