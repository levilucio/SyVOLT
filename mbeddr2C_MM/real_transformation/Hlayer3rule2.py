from core.himesis import Himesis
import uuid

class Hlayer3rule2(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule layer3rule2.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer3rule2, self).__init__(name='Hlayer3rule2', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """layer3rule2"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer3rule2')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
 
        
        # match class ImplementationModule(layer3rule2class0) node
        self.add_node()

        self.vs[3]["mm__"] = """ImplementationModule""" 
        self.vs[3]["attr1"] = """+""" 
        # match_contains node for class ImplementationModule(layer3rule2class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        # match class InstanceConfiguration(layer3rule2class1) node
        self.add_node()

        self.vs[5]["mm__"] = """InstanceConfiguration""" 
        self.vs[5]["attr1"] = """+""" 
        # match_contains node for class InstanceConfiguration(layer3rule2class1)
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        # match class ComponentInstance(layer3rule2class2) node
        self.add_node()

        self.vs[7]["mm__"] = """ComponentInstance""" 
        self.vs[7]["attr1"] = """+""" 
        # match_contains node for class ComponentInstance(layer3rule2class2)
        self.add_node()
        self.vs[8]["mm__"] = """match_contains"""
        
        
        # apply class ImplementationModule(layer3rule2class3) node
        self.add_node()

        self.vs[9]["mm__"] = """ImplementationModule""" 
        self.vs[9]["attr1"] = """1"""
        # apply_contains node for class ImplementationModule(layer3rule2class3)
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        # apply class FunctionPrototype(layer3rule2class4) node
        self.add_node()

        self.vs[11]["mm__"] = """FunctionPrototype""" 
        self.vs[11]["attr1"] = """1"""
        # apply_contains node for class FunctionPrototype(layer3rule2class4)
        self.add_node()
        self.vs[12]["mm__"] = """apply_contains"""
        # apply class VoidType(layer3rule2class5) node
        self.add_node()

        self.vs[13]["mm__"] = """VoidType""" 
        self.vs[13]["attr1"] = """1"""
        # apply_contains node for class VoidType(layer3rule2class5)
        self.add_node()
        self.vs[14]["mm__"] = """apply_contains"""
        
        
        # match association ImplementationModule--contents-->InstanceConfiguration node
        self.add_node()
        self.vs[15]["attr1"] = """contents"""
        self.vs[15]["mm__"] = """directLink_S"""
        # match association InstanceConfiguration--contents-->ComponentInstance node
        self.add_node()
        self.vs[16]["attr1"] = """contents"""
        self.vs[16]["mm__"] = """directLink_S"""
        
        # apply association ImplementationModule--contents-->FunctionPrototype node
        self.add_node()
        self.vs[17]["attr1"] = """contents"""
        self.vs[17]["mm__"] = """directLink_T"""
        # apply association FunctionPrototype--type-->VoidType node
        self.add_node()
        self.vs[18]["attr1"] = """type"""
        self.vs[18]["mm__"] = """directLink_T"""
        
        # backward association ImplementationModule---->ImplementationModule node
        self.add_node()

        self.vs[19]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class ImplementationModule(layer3rule2class0)
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class InstanceConfiguration(layer3rule2class1)
                (0,8), # matchmodel -> match_contains
                (8,7), # match_contains -> match_class ComponentInstance(layer3rule2class2)
                (1,10), # applymodel -> apply_contains
                (10,9), # apply_contains -> apply_class ImplementationModule(layer3rule2class3)
                (1,12), # applymodel -> apply_contains
                (12,11), # apply_contains -> apply_class FunctionPrototype(layer3rule2class4)
                (1,14), # applymodel -> apply_contains
                (14,13), # apply_contains -> apply_class VoidType(layer3rule2class5)
                (3,15), # match_class ImplementationModule(layer3rule2class0) -> association contents
                (15,5), # association contents  -> match_class InstanceConfiguration(layer3rule2class1)
                (5,16), # match_class InstanceConfiguration(layer3rule2class1) -> association contents
                (16,7), # association contents  -> match_class ComponentInstance(layer3rule2class2)
                (9,17), # apply_class ImplementationModule(layer3rule2class3) -> association contents
                (17,11), # association contents  -> apply_class FunctionPrototype(layer3rule2class4)
                (11,18), # apply_class FunctionPrototype(layer3rule2class4) -> association type
                (18,13), # association type  -> apply_class VoidType(layer3rule2class5)
                (9,19), # apply_class ImplementationModule(layer3rule2class3) -> backward_association
                (19,3), #  backward_association -> apply_class ImplementationModule(layer3rule2class0)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((9,'__ApplyAttribute'),('constant','ImplementationModule')), ((11,'name'),('concat',((3,'name'),('concat',(('constant','_'),('concat',((5,'name'),('concat',(('constant','_'),('concat',((7,'name'),('constant','__wire')))))))))))), ((11,'__ApplyAttribute'),('constant','WireFunctionPrototype')), ]

        
