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
        self.vs[2]["attr1"] = """layer3rule2"""
        
        # match class ImplementationModule(layer3rule2class0) node
        self.add_node()
        
        self.vs[3]["mm__"] = """ImplementationModule""" 
        self.vs[3]["attr1"] = """+""" 
        # match class InstanceConfiguration(layer3rule2class1) node
        self.add_node()
        
        self.vs[4]["mm__"] = """InstanceConfiguration""" 
        self.vs[4]["attr1"] = """+""" 
        # match class ComponentInstance(layer3rule2class2) node
        self.add_node()
        
        self.vs[5]["mm__"] = """ComponentInstance""" 
        self.vs[5]["attr1"] = """+""" 
        
        
        # apply class ImplementationModule(layer3rule2class3) node
        self.add_node()

        self.vs[6]["mm__"] = """ImplementationModule""" 
        self.vs[6]["attr1"] = """1"""
        # apply class FunctionPrototype(layer3rule2class4) node
        self.add_node()

        self.vs[7]["mm__"] = """FunctionPrototype""" 
        self.vs[7]["attr1"] = """1"""
        # apply class VoidType(layer3rule2class5) node
        self.add_node()

        self.vs[8]["mm__"] = """VoidType""" 
        self.vs[8]["attr1"] = """1"""
        
        
        # match association ImplementationModule--contents-->InstanceConfiguration node
        self.add_node()
        self.vs[9]["attr1"] = """contents"""
        self.vs[9]["mm__"] = """directLink_S"""
        # match association InstanceConfiguration--contents-->ComponentInstance node
        self.add_node()
        self.vs[10]["attr1"] = """contents"""
        self.vs[10]["mm__"] = """directLink_S"""
        
        # apply association ImplementationModule--contents-->FunctionPrototype node
        self.add_node()
        self.vs[11]["attr1"] = """contents"""
        self.vs[11]["mm__"] = """directLink_T"""
        # apply association FunctionPrototype--type-->VoidType node
        self.add_node()
        self.vs[12]["attr1"] = """type"""
        self.vs[12]["mm__"] = """directLink_T"""
        
        # backward association ImplementationModule---->ImplementationModule node
        self.add_node()

        self.vs[13]["mm__"] = """backward_link"""
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class ImplementationModule(layer3rule2class0)
                (0,4), # matchmodel -> match_class InstanceConfiguration(layer3rule2class1)
                (0,5), # matchmodel -> match_class ComponentInstance(layer3rule2class2)
                (1,6), # applymodel -> -> apply_class ImplementationModule(layer3rule2class3)
                (1,7), # applymodel -> -> apply_class FunctionPrototype(layer3rule2class4)
                (1,8), # applymodel -> -> apply_class VoidType(layer3rule2class5)
                (3,9), # match_class ImplementationModule(layer3rule2class0) -> association contents
                (9,4), # association contents  -> match_class InstanceConfiguration(layer3rule2class1)
                (4,10), # match_class InstanceConfiguration(layer3rule2class1) -> association contents
                (10,5), # association contents  -> match_class ComponentInstance(layer3rule2class2)
                (6,11), # apply_class ImplementationModule(layer3rule2class3) -> association contents
                (11,7), # association contents  -> apply_class FunctionPrototype(layer3rule2class4)
                (7,12), # apply_class FunctionPrototype(layer3rule2class4) -> association type
                (12,8), # association type  -> apply_class VoidType(layer3rule2class5)
                (6,13), # apply_class ImplementationModule(layer3rule2class3) -> backward_association
                (13,3), #  backward_association -> apply_class ImplementationModule(layer3rule2class0)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((6,'__ApplyAttribute'),('constant','ImplementationModule')), ((7,'name'),('concat',((3,'name'),('concat',(('constant','_'),('concat',((4,'name'),('concat',(('constant','_'),('concat',((5,'name'),('constant','__wire')))))))))))), ((7,'__ApplyAttribute'),('constant','WireFunctionPrototype')), ]

        
