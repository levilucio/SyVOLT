from core.himesis import Himesis
import uuid

class Hlayer4rule3(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule layer4rule3.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer4rule3, self).__init__(name='Hlayer4rule3', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """layer4rule3"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule3')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
 
        
        # match class ImplementationModule(layer4rule3class0) node
        self.add_node()

        self.vs[3]["mm__"] = """ImplementationModule""" 
        self.vs[3]["attr1"] = """+""" 
        # match_contains node for class ImplementationModule(layer4rule3class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        # match class Function(layer4rule3class1) node
        self.add_node()

        self.vs[5]["mm__"] = """Function""" 
        self.vs[5]["attr1"] = """+""" 
        # match_contains node for class Function(layer4rule3class1)
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        # match class Int32Type(layer4rule3class2) node
        self.add_node()

        self.vs[7]["mm__"] = """Int32Type""" 
        self.vs[7]["attr1"] = """+""" 
        # match_contains node for class Int32Type(layer4rule3class2)
        self.add_node()
        self.vs[8]["mm__"] = """match_contains"""
        
        
        # apply class ImplementationModule(layer4rule3class3) node
        self.add_node()

        self.vs[9]["mm__"] = """ImplementationModule""" 
        self.vs[9]["attr1"] = """1"""
        # apply_contains node for class ImplementationModule(layer4rule3class3)
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        # apply class Function(layer4rule3class4) node
        self.add_node()

        self.vs[11]["mm__"] = """Function""" 
        self.vs[11]["attr1"] = """1"""
        # apply_contains node for class Function(layer4rule3class4)
        self.add_node()
        self.vs[12]["mm__"] = """apply_contains"""
        # apply class VoidType(layer4rule3class5) node
        self.add_node()

        self.vs[13]["mm__"] = """VoidType""" 
        self.vs[13]["attr1"] = """1"""
        # apply_contains node for class VoidType(layer4rule3class5)
        self.add_node()
        self.vs[14]["mm__"] = """apply_contains"""
        # apply class StatementList(layer4rule3class6) node
        self.add_node()

        self.vs[15]["mm__"] = """StatementList""" 
        self.vs[15]["attr1"] = """1"""
        # apply_contains node for class StatementList(layer4rule3class6)
        self.add_node()
        self.vs[16]["mm__"] = """apply_contains"""
        # apply class Function(layer4rule3class7) node
        self.add_node()

        self.vs[17]["mm__"] = """Function""" 
        self.vs[17]["attr1"] = """1"""
        # apply_contains node for class Function(layer4rule3class7)
        self.add_node()
        self.vs[18]["mm__"] = """apply_contains"""
        # apply class StatementList(layer4rule3class8) node
        self.add_node()

        self.vs[19]["mm__"] = """StatementList""" 
        self.vs[19]["attr1"] = """1"""
        # apply_contains node for class StatementList(layer4rule3class8)
        self.add_node()
        self.vs[20]["mm__"] = """apply_contains"""
        # apply class Int32Type(layer4rule3class9) node
        self.add_node()

        self.vs[21]["mm__"] = """Int32Type""" 
        self.vs[21]["attr1"] = """1"""
        # apply_contains node for class Int32Type(layer4rule3class9)
        self.add_node()
        self.vs[22]["mm__"] = """apply_contains"""
        # apply class ExpressionStatement(layer4rule3class10) node
        self.add_node()

        self.vs[23]["mm__"] = """ExpressionStatement""" 
        self.vs[23]["attr1"] = """1"""
        # apply_contains node for class ExpressionStatement(layer4rule3class10)
        self.add_node()
        self.vs[24]["mm__"] = """apply_contains"""
        # apply class FunctionCall(layer4rule3class11) node
        self.add_node()

        self.vs[25]["mm__"] = """FunctionCall""" 
        self.vs[25]["attr1"] = """1"""
        # apply_contains node for class FunctionCall(layer4rule3class11)
        self.add_node()
        self.vs[26]["mm__"] = """apply_contains"""
        # apply class FunctionPrototype(layer4rule3class12) node
        self.add_node()

        self.vs[27]["mm__"] = """FunctionPrototype""" 
        self.vs[27]["attr1"] = """1"""
        # apply_contains node for class FunctionPrototype(layer4rule3class12)
        self.add_node()
        self.vs[28]["mm__"] = """apply_contains"""
        
        
        # match association ImplementationModule--contents-->Function node
        self.add_node()
        self.vs[29]["attr1"] = """contents"""
        self.vs[29]["mm__"] = """directLink_S"""
        # match association Function--type-->Int32Type node
        self.add_node()
        self.vs[30]["attr1"] = """type"""
        self.vs[30]["mm__"] = """directLink_S"""
        
        # apply association ImplementationModule--contents-->Function node
        self.add_node()
        self.vs[31]["attr1"] = """contents"""
        self.vs[31]["mm__"] = """directLink_T"""
        # apply association Function--type-->VoidType node
        self.add_node()
        self.vs[32]["attr1"] = """type"""
        self.vs[32]["mm__"] = """directLink_T"""
        # apply association Function--body-->StatementList node
        self.add_node()
        self.vs[33]["attr1"] = """body"""
        self.vs[33]["mm__"] = """directLink_T"""
        # apply association ImplementationModule--contents-->Function node
        self.add_node()
        self.vs[34]["attr1"] = """contents"""
        self.vs[34]["mm__"] = """directLink_T"""
        # apply association Function--type-->Int32Type node
        self.add_node()
        self.vs[35]["attr1"] = """type"""
        self.vs[35]["mm__"] = """directLink_T"""
        # apply association Function--body-->StatementList node
        self.add_node()
        self.vs[36]["attr1"] = """body"""
        self.vs[36]["mm__"] = """directLink_T"""
        # apply association StatementList--statements-->ExpressionStatement node
        self.add_node()
        self.vs[37]["attr1"] = """statements"""
        self.vs[37]["mm__"] = """directLink_T"""
        # apply association ExpressionStatement--expr-->FunctionCall node
        self.add_node()
        self.vs[38]["attr1"] = """expr"""
        self.vs[38]["mm__"] = """directLink_T"""
        # apply association FunctionCall--function-->FunctionPrototype node
        self.add_node()
        self.vs[39]["attr1"] = """function"""
        self.vs[39]["mm__"] = """directLink_T"""
        
        # backward association ImplementationModule---->ImplementationModule node
        self.add_node()

        self.vs[40]["mm__"] = """backward_link"""
        # backward association Function---->FunctionPrototype node
        self.add_node()

        self.vs[41]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class ImplementationModule(layer4rule3class0)
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class Function(layer4rule3class1)
                (0,8), # matchmodel -> match_contains
                (8,7), # match_contains -> match_class Int32Type(layer4rule3class2)
                (1,10), # applymodel -> apply_contains
                (10,9), # apply_contains -> apply_class ImplementationModule(layer4rule3class3)
                (1,12), # applymodel -> apply_contains
                (12,11), # apply_contains -> apply_class Function(layer4rule3class4)
                (1,14), # applymodel -> apply_contains
                (14,13), # apply_contains -> apply_class VoidType(layer4rule3class5)
                (1,16), # applymodel -> apply_contains
                (16,15), # apply_contains -> apply_class StatementList(layer4rule3class6)
                (1,18), # applymodel -> apply_contains
                (18,17), # apply_contains -> apply_class Function(layer4rule3class7)
                (1,20), # applymodel -> apply_contains
                (20,19), # apply_contains -> apply_class StatementList(layer4rule3class8)
                (1,22), # applymodel -> apply_contains
                (22,21), # apply_contains -> apply_class Int32Type(layer4rule3class9)
                (1,24), # applymodel -> apply_contains
                (24,23), # apply_contains -> apply_class ExpressionStatement(layer4rule3class10)
                (1,26), # applymodel -> apply_contains
                (26,25), # apply_contains -> apply_class FunctionCall(layer4rule3class11)
                (1,28), # applymodel -> apply_contains
                (28,27), # apply_contains -> apply_class FunctionPrototype(layer4rule3class12)
                (3,29), # match_class ImplementationModule(layer4rule3class0) -> association contents
                (29,5), # association contents  -> match_class Function(layer4rule3class1)
                (5,30), # match_class Function(layer4rule3class1) -> association type
                (30,7), # association type  -> match_class Int32Type(layer4rule3class2)
                (9,31), # apply_class ImplementationModule(layer4rule3class3) -> association contents
                (31,11), # association contents  -> apply_class Function(layer4rule3class4)
                (11,32), # apply_class Function(layer4rule3class4) -> association type
                (32,13), # association type  -> apply_class VoidType(layer4rule3class5)
                (11,33), # apply_class Function(layer4rule3class4) -> association body
                (33,15), # association body  -> apply_class StatementList(layer4rule3class6)
                (9,34), # apply_class ImplementationModule(layer4rule3class3) -> association contents
                (34,17), # association contents  -> apply_class Function(layer4rule3class7)
                (17,35), # apply_class Function(layer4rule3class7) -> association type
                (35,21), # association type  -> apply_class Int32Type(layer4rule3class9)
                (17,36), # apply_class Function(layer4rule3class7) -> association body
                (36,19), # association body  -> apply_class StatementList(layer4rule3class8)
                (19,37), # apply_class StatementList(layer4rule3class8) -> association statements
                (37,23), # association statements  -> apply_class ExpressionStatement(layer4rule3class10)
                (23,38), # apply_class ExpressionStatement(layer4rule3class10) -> association expr
                (38,25), # association expr  -> apply_class FunctionCall(layer4rule3class11)
                (25,39), # apply_class FunctionCall(layer4rule3class11) -> association function
                (39,27), # association function  -> apply_class FunctionPrototype(layer4rule3class12)
                (9,40), # apply_class ImplementationModule(layer4rule3class3) -> backward_association
                (40,3), #  backward_association -> apply_class ImplementationModule(layer4rule3class0)
                (27,41), # apply_class FunctionPrototype(layer4rule3class12) -> backward_association
                (41,5), #  backward_association -> apply_class Function(layer4rule3class1)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((5,'name'),('constant','main')), ((9,'__ApplyAttribute'),('constant','ImplementationModule')), ((11,'name'),('concat',((3,'name'),('constant','_blockexpr_main_2')))), ((15,'__ApplyAttribute'),('constant','Main2Body')), ((17,'name'),('constant','main')), ((19,'__ApplyAttribute'),('constant','MainBody')), ((27,'__ApplyAttribute'),('constant','Main2Prototype')), ]

        
