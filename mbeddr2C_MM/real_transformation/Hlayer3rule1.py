from core.himesis import Himesis
import uuid

class Hlayer3rule1(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule layer3rule1.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer3rule1, self).__init__(name='Hlayer3rule1', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """layer3rule1"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule1')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
 
        
        # match class ImplementationModule(layer3rule1class0) node
        self.add_node()
        self.vs[3]["name"] = """layer3rule1class0""" 
        self.vs[3]["classtype"] = """ImplementationModule"""
        self.vs[3]["mm__"] = """ImplementationModule"""
        self.vs[3]["cardinality"] = """+""" 
        # match_contains node for class ImplementationModule(layer3rule1class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        # match class InstanceConfiguration(layer3rule1class1) node
        self.add_node()
        self.vs[5]["name"] = """layer3rule1class1""" 
        self.vs[5]["classtype"] = """InstanceConfiguration"""
        self.vs[5]["mm__"] = """InstanceConfiguration"""
        self.vs[5]["cardinality"] = """+""" 
        # match_contains node for class InstanceConfiguration(layer3rule1class1)
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        
        
        # apply class ImplementationModule(layer3rule1class2) node
        self.add_node()
        self.vs[7]["name"] = """layer3rule1class2""" 
        self.vs[7]["classtype"] = """ImplementationModule"""
        self.vs[7]["mm__"] = """ImplementationModule"""
        self.vs[7]["cardinality"] = """1"""
        # apply_contains node for class ImplementationModule(layer3rule1class2)
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        # apply class FunctionPrototype(layer3rule1class3) node
        self.add_node()
        self.vs[9]["name"] = """layer3rule1class3""" 
        self.vs[9]["classtype"] = """FunctionPrototype"""
        self.vs[9]["mm__"] = """FunctionPrototype"""
        self.vs[9]["cardinality"] = """1"""
        # apply_contains node for class FunctionPrototype(layer3rule1class3)
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        # apply class VoidType(layer3rule1class4) node
        self.add_node()
        self.vs[11]["name"] = """layer3rule1class4""" 
        self.vs[11]["classtype"] = """VoidType"""
        self.vs[11]["mm__"] = """VoidType"""
        self.vs[11]["cardinality"] = """1"""
        # apply_contains node for class VoidType(layer3rule1class4)
        self.add_node()
        self.vs[12]["mm__"] = """apply_contains"""
        
        
        # match association ImplementationModule--contents-->InstanceConfiguration node
        self.add_node()
        self.vs[13]["associationType"] = """contents"""
        self.vs[13]["mm__"] = """directLink_S"""
        
        # apply association ImplementationModule--contents-->FunctionPrototype node
        self.add_node()
        self.vs[14]["associationType"] = """contents"""
        self.vs[14]["mm__"] = """directLink_T"""
        # apply association FunctionPrototype--type-->VoidType node
        self.add_node()
        self.vs[15]["associationType"] = """type"""
        self.vs[15]["mm__"] = """directLink_T"""
        
        # backward association ImplementationModule---->ImplementationModule node
        self.add_node()
        self.vs[16]["type"] = """ruleDef"""
        self.vs[16]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class ImplementationModule(layer3rule1class0)
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class InstanceConfiguration(layer3rule1class1)
                (1,8), # applymodel -> apply_contains
                (8,7), # apply_contains -> apply_class ImplementationModule(layer3rule1class2)
                (1,10), # applymodel -> apply_contains
                (10,9), # apply_contains -> apply_class FunctionPrototype(layer3rule1class3)
                (1,12), # applymodel -> apply_contains
                (12,11), # apply_contains -> apply_class VoidType(layer3rule1class4)
                (3,13), # match_class ImplementationModule(layer3rule1class0) -> association contents
                (13,5), # association contents  -> match_class InstanceConfiguration(layer3rule1class1)
                (7,14), # apply_class ImplementationModule(layer3rule1class2) -> association contents
                (14,9), # association contents  -> apply_class FunctionPrototype(layer3rule1class3)
                (9,15), # apply_class FunctionPrototype(layer3rule1class3) -> association type
                (15,11), # association type  -> apply_class VoidType(layer3rule1class4)
                (7,16), # apply_class ImplementationModule(layer3rule1class2) -> backward_association
                (16,3), #  backward_association -> apply_class ImplementationModule(layer3rule1class0)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((7,'__ApplyAttribute'),('constant','ImplementationModule')), ((9,'name'),('concat',((3,'name'),('concat',(('constant','_'),('concat',((5,'name'),('constant','__init')))))))), ((9,'__ApplyAttribute'),('constant','InstanceConfigurationInit')), ]

        
