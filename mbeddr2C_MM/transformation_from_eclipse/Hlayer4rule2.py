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
 
        
        # match class ImplementationModule(layer4rule2class0) node
        self.add_node()

        self.vs[3]["mm__"] = """ImplementationModule""" 
        self.vs[3]["attr1"] = """+""" 
        # match_contains node for class ImplementationModule(layer4rule2class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        # match class TestCase(layer4rule2class1) node
        self.add_node()

        self.vs[5]["mm__"] = """TestCase""" 
        self.vs[5]["attr1"] = """+""" 
        # match_contains node for class TestCase(layer4rule2class1)
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        
        
        # apply class ImplementationModule(layer4rule2class2) node
        self.add_node()

        self.vs[7]["mm__"] = """ImplementationModule""" 
        self.vs[7]["attr1"] = """1"""
        # apply_contains node for class ImplementationModule(layer4rule2class2)
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        # apply class Function(layer4rule2class3) node
        self.add_node()

        self.vs[9]["mm__"] = """Function""" 
        self.vs[9]["attr1"] = """1"""
        # apply_contains node for class Function(layer4rule2class3)
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        # apply class VoidType(layer4rule2class4) node
        self.add_node()

        self.vs[11]["mm__"] = """VoidType""" 
        self.vs[11]["attr1"] = """1"""
        # apply_contains node for class VoidType(layer4rule2class4)
        self.add_node()
        self.vs[12]["mm__"] = """apply_contains"""
        # apply class StatementList(layer4rule2class5) node
        self.add_node()

        self.vs[13]["mm__"] = """StatementList""" 
        self.vs[13]["attr1"] = """1"""
        # apply_contains node for class StatementList(layer4rule2class5)
        self.add_node()
        self.vs[14]["mm__"] = """apply_contains"""
        
        
        # match association ImplementationModule--contents-->TestCase node
        self.add_node()
        self.vs[15]["attr1"] = """contents"""
        self.vs[15]["mm__"] = """directLink_S"""
        
        # apply association ImplementationModule--contents-->Function node
        self.add_node()
        self.vs[16]["attr1"] = """contents"""
        self.vs[16]["mm__"] = """directLink_T"""
        # apply association Function--type-->VoidType node
        self.add_node()
        self.vs[17]["attr1"] = """type"""
        self.vs[17]["mm__"] = """directLink_T"""
        # apply association Function--body-->StatementList node
        self.add_node()
        self.vs[18]["attr1"] = """body"""
        self.vs[18]["mm__"] = """directLink_T"""
        
        # backward association ImplementationModule---->ImplementationModule node
        self.add_node()

        self.vs[19]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class ImplementationModule(layer4rule2class0)
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class TestCase(layer4rule2class1)
                (1,8), # applymodel -> apply_contains
                (8,7), # apply_contains -> apply_class ImplementationModule(layer4rule2class2)
                (1,10), # applymodel -> apply_contains
                (10,9), # apply_contains -> apply_class Function(layer4rule2class3)
                (1,12), # applymodel -> apply_contains
                (12,11), # apply_contains -> apply_class VoidType(layer4rule2class4)
                (1,14), # applymodel -> apply_contains
                (14,13), # apply_contains -> apply_class StatementList(layer4rule2class5)
                (3,15), # match_class ImplementationModule(layer4rule2class0) -> association contents
                (15,5), # association contents  -> match_class TestCase(layer4rule2class1)
                (7,16), # apply_class ImplementationModule(layer4rule2class2) -> association contents
                (16,9), # association contents  -> apply_class Function(layer4rule2class3)
                (9,17), # apply_class Function(layer4rule2class3) -> association type
                (17,11), # association type  -> apply_class VoidType(layer4rule2class4)
                (9,18), # apply_class Function(layer4rule2class3) -> association body
                (18,13), # association body  -> apply_class StatementList(layer4rule2class5)
                (7,19), # apply_class ImplementationModule(layer4rule2class2) -> backward_association
                (19,3), #  backward_association -> apply_class ImplementationModule(layer4rule2class0)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((7,'__ApplyAttribute'),('constant','ImplementationModule')), ((9,'name'),('concat',((3,'name'),('concat',(('constant','_'),(5,'name')))))), ((13,'__ApplyAttribute'),('constant','TestCaseFunctionStatements')), ]

        
