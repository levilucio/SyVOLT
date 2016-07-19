from core.himesis import Himesis
import uuid

class Hlayer4rule2(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule layer4rule2.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer4rule2, self).__init__(name='Hlayer4rule2', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer4rule2"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule2')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["attr1"] = """layer4rule2"""
        
        # match class ImplementationModule(layer4rule2class0) node
        self.add_node()
        
        self.vs[3]["mm__"] = """ImplementationModule""" 
        self.vs[3]["attr1"] = """+""" 
        # match class TestCase(layer4rule2class1) node
        self.add_node()
        
        self.vs[4]["mm__"] = """TestCase""" 
        self.vs[4]["attr1"] = """+""" 
        
        
        # apply class ImplementationModule(layer4rule2class2) node
        self.add_node()

        self.vs[5]["mm__"] = """ImplementationModule""" 
        self.vs[5]["attr1"] = """1"""
        # apply class Function(layer4rule2class3) node
        self.add_node()

        self.vs[6]["mm__"] = """Function""" 
        self.vs[6]["attr1"] = """1"""
        # apply class VoidType(layer4rule2class4) node
        self.add_node()

        self.vs[7]["mm__"] = """VoidType""" 
        self.vs[7]["attr1"] = """1"""
        # apply class StatementList(layer4rule2class5) node
        self.add_node()

        self.vs[8]["mm__"] = """StatementList""" 
        self.vs[8]["attr1"] = """1"""
        
        
        # match association ImplementationModule--contents-->TestCase node
        self.add_node()
        self.vs[9]["attr1"] = """contents"""
        self.vs[9]["mm__"] = """directLink_S"""
        
        # apply association ImplementationModule--contents-->Function node
        self.add_node()
        self.vs[10]["attr1"] = """contents"""
        self.vs[10]["mm__"] = """directLink_T"""
        # apply association Function--type-->VoidType node
        self.add_node()
        self.vs[11]["attr1"] = """type"""
        self.vs[11]["mm__"] = """directLink_T"""
        # apply association Function--body-->StatementList node
        self.add_node()
        self.vs[12]["attr1"] = """body"""
        self.vs[12]["mm__"] = """directLink_T"""
        
        # backward association ImplementationModule---->ImplementationModule node
        self.add_node()

        self.vs[13]["mm__"] = """backward_link"""
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class ImplementationModule(layer4rule2class0)
                (0,4), # matchmodel -> match_class TestCase(layer4rule2class1)
                (1,5), # applymodel -> -> apply_class ImplementationModule(layer4rule2class2)
                (1,6), # applymodel -> -> apply_class Function(layer4rule2class3)
                (1,7), # applymodel -> -> apply_class VoidType(layer4rule2class4)
                (1,8), # applymodel -> -> apply_class StatementList(layer4rule2class5)
                (3,9), # match_class ImplementationModule(layer4rule2class0) -> association contents
                (9,4), # association contents  -> match_class TestCase(layer4rule2class1)
                (5,10), # apply_class ImplementationModule(layer4rule2class2) -> association contents
                (10,6), # association contents  -> apply_class Function(layer4rule2class3)
                (6,11), # apply_class Function(layer4rule2class3) -> association type
                (11,7), # association type  -> apply_class VoidType(layer4rule2class4)
                (6,12), # apply_class Function(layer4rule2class3) -> association body
                (12,8), # association body  -> apply_class StatementList(layer4rule2class5)
                (5,13), # apply_class ImplementationModule(layer4rule2class2) -> backward_association
                (13,3), #  backward_association -> apply_class ImplementationModule(layer4rule2class0)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((5,'__ApplyAttribute'),('constant','ImplementationModule')), ((6,'name'),('concat',((3,'name'),('concat',(('constant','_'),(4,'name')))))), ((8,'__ApplyAttribute'),('constant','TestCaseFunctionStatements')), ]

        
