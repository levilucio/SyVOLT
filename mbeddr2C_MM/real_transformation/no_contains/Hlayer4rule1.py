from core.himesis import Himesis
import uuid

class Hlayer4rule1(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule layer4rule1.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer4rule1, self).__init__(name='Hlayer4rule1', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer4rule1"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule1')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["attr1"] = """layer4rule1"""
        
        # match class ImplementationModule(layer4rule1class0) node
        self.add_node()
        
        self.vs[3]["mm__"] = """ImplementationModule""" 
        self.vs[3]["attr1"] = """+""" 
        # match class InstanceConfiguration(layer4rule1class1) node
        self.add_node()
        
        self.vs[4]["mm__"] = """InstanceConfiguration""" 
        self.vs[4]["attr1"] = """+""" 
        
        
        # apply class ImplementationModule(layer4rule1class2) node
        self.add_node()

        self.vs[5]["mm__"] = """ImplementationModule""" 
        self.vs[5]["attr1"] = """1"""
        # apply class Function(layer4rule1class3) node
        self.add_node()

        self.vs[6]["mm__"] = """Function""" 
        self.vs[6]["attr1"] = """1"""
        # apply class StatementList(layer4rule1class4) node
        self.add_node()

        self.vs[7]["mm__"] = """StatementList""" 
        self.vs[7]["attr1"] = """1"""
        
        
        # match association ImplementationModule--contents-->InstanceConfiguration node
        self.add_node()
        self.vs[8]["attr1"] = """contents"""
        self.vs[8]["mm__"] = """directLink_S"""
        
        # apply association ImplementationModule--contents-->Function node
        self.add_node()
        self.vs[9]["attr1"] = """contents"""
        self.vs[9]["mm__"] = """directLink_T"""
        # apply association Function--body-->StatementList node
        self.add_node()
        self.vs[10]["attr1"] = """body"""
        self.vs[10]["mm__"] = """directLink_T"""
        
        # backward association ImplementationModule---->ImplementationModule node
        self.add_node()

        self.vs[11]["mm__"] = """backward_link"""
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class ImplementationModule(layer4rule1class0)
                (0,4), # matchmodel -> match_class InstanceConfiguration(layer4rule1class1)
                (1,5), # applymodel -> -> apply_class ImplementationModule(layer4rule1class2)
                (1,6), # applymodel -> -> apply_class Function(layer4rule1class3)
                (1,7), # applymodel -> -> apply_class StatementList(layer4rule1class4)
                (3,8), # match_class ImplementationModule(layer4rule1class0) -> association contents
                (8,4), # association contents  -> match_class InstanceConfiguration(layer4rule1class1)
                (5,9), # apply_class ImplementationModule(layer4rule1class2) -> association contents
                (9,6), # association contents  -> apply_class Function(layer4rule1class3)
                (6,10), # apply_class Function(layer4rule1class3) -> association body
                (10,7), # association body  -> apply_class StatementList(layer4rule1class4)
                (5,11), # apply_class ImplementationModule(layer4rule1class2) -> backward_association
                (11,3), #  backward_association -> apply_class ImplementationModule(layer4rule1class0)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((5,'__ApplyAttribute'),('constant','ImplementationModule')), ((6,'name'),('concat',((3,'name'),('concat',(('constant','_'),('concat',((4,'name'),('constant','__init')))))))), ((7,'__ApplyAttribute'),('constant','InstancesInitFunctionBody')), ]

        
