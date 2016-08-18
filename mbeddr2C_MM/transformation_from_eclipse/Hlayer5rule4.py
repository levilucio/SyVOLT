from core.himesis import Himesis
import uuid

class Hlayer5rule4(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule layer5rule4.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer5rule4, self).__init__(name='Hlayer5rule4', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """layer5rule4"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule4')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
 
        
        # match class TestCase(layer5rule4class0) node
        self.add_node()

        self.vs[3]["mm__"] = """TestCase""" 
        self.vs[3]["attr1"] = """+""" 
        # match_contains node for class TestCase(layer5rule4class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        # match class StatementList(layer5rule4class1) node
        self.add_node()

        self.vs[5]["mm__"] = """StatementList""" 
        self.vs[5]["attr1"] = """+""" 
        # match_contains node for class StatementList(layer5rule4class1)
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        # match class ExpressionStatement(layer5rule4class2) node
        self.add_node()

        self.vs[7]["mm__"] = """ExpressionStatement""" 
        self.vs[7]["attr1"] = """+""" 
        # match_contains node for class ExpressionStatement(layer5rule4class2)
        self.add_node()
        self.vs[8]["mm__"] = """match_contains"""
        # match class PortAdapterOpCallExpr(layer5rule4class3) node
        self.add_node()

        self.vs[9]["mm__"] = """PortAdapterOpCallExpr""" 
        self.vs[9]["attr1"] = """+""" 
        # match_contains node for class PortAdapterOpCallExpr(layer5rule4class3)
        self.add_node()
        self.vs[10]["mm__"] = """match_contains"""
        # match class PortAdapterRefExpr(layer5rule4class4) node
        self.add_node()

        self.vs[11]["mm__"] = """PortAdapterRefExpr""" 
        self.vs[11]["attr1"] = """+""" 
        # match_contains node for class PortAdapterRefExpr(layer5rule4class4)
        self.add_node()
        self.vs[12]["mm__"] = """match_contains"""
        # match class PortAdapter(layer5rule4class5) node
        self.add_node()

        self.vs[13]["mm__"] = """PortAdapter""" 
        self.vs[13]["attr1"] = """+""" 
        # match_contains node for class PortAdapter(layer5rule4class5)
        self.add_node()
        self.vs[14]["mm__"] = """match_contains"""
        # match class Operation(layer5rule4class6) node
        self.add_node()

        self.vs[15]["mm__"] = """Operation""" 
        self.vs[15]["attr1"] = """+""" 
        # match_contains node for class Operation(layer5rule4class6)
        self.add_node()
        self.vs[16]["mm__"] = """match_contains"""
        # match class AdapterInstancePortRef(layer5rule4class7) node
        self.add_node()

        self.vs[17]["mm__"] = """AdapterInstancePortRef""" 
        self.vs[17]["attr1"] = """+""" 
        # match_contains node for class AdapterInstancePortRef(layer5rule4class7)
        self.add_node()
        self.vs[18]["mm__"] = """match_contains"""
        # match class ComponentInstance(layer5rule4class8) node
        self.add_node()

        self.vs[19]["mm__"] = """ComponentInstance""" 
        self.vs[19]["attr1"] = """+""" 
        # match_contains node for class ComponentInstance(layer5rule4class8)
        self.add_node()
        self.vs[20]["mm__"] = """match_contains"""
        # match class ProvidedPort(layer5rule4class9) node
        self.add_node()

        self.vs[21]["mm__"] = """ProvidedPort""" 
        self.vs[21]["attr1"] = """+""" 
        # match_contains node for class ProvidedPort(layer5rule4class9)
        self.add_node()
        self.vs[22]["mm__"] = """match_contains"""
        # match class ClientServerInterface(layer5rule4class10) node
        self.add_node()

        self.vs[23]["mm__"] = """ClientServerInterface""" 
        self.vs[23]["attr1"] = """+""" 
        # match_contains node for class ClientServerInterface(layer5rule4class10)
        self.add_node()
        self.vs[24]["mm__"] = """match_contains"""
        
        
        # apply class StatementList(layer5rule4class11) node
        self.add_node()

        self.vs[25]["mm__"] = """StatementList""" 
        self.vs[25]["attr1"] = """1"""
        # apply_contains node for class StatementList(layer5rule4class11)
        self.add_node()
        self.vs[26]["mm__"] = """apply_contains"""
        # apply class ExpressionStatement(layer5rule4class12) node
        self.add_node()

        self.vs[27]["mm__"] = """ExpressionStatement""" 
        self.vs[27]["attr1"] = """1"""
        # apply_contains node for class ExpressionStatement(layer5rule4class12)
        self.add_node()
        self.vs[28]["mm__"] = """apply_contains"""
        # apply class FunctionCall(layer5rule4class13) node
        self.add_node()

        self.vs[29]["mm__"] = """FunctionCall""" 
        self.vs[29]["attr1"] = """1"""
        # apply_contains node for class FunctionCall(layer5rule4class13)
        self.add_node()
        self.vs[30]["mm__"] = """apply_contains"""
        # apply class FunctionPrototype(layer5rule4class14) node
        self.add_node()

        self.vs[31]["mm__"] = """FunctionPrototype""" 
        self.vs[31]["attr1"] = """1"""
        # apply_contains node for class FunctionPrototype(layer5rule4class14)
        self.add_node()
        self.vs[32]["mm__"] = """apply_contains"""
        # apply class ReferenceExpr(layer5rule4class15) node
        self.add_node()

        self.vs[33]["mm__"] = """ReferenceExpr""" 
        self.vs[33]["attr1"] = """1"""
        # apply_contains node for class ReferenceExpr(layer5rule4class15)
        self.add_node()
        self.vs[34]["mm__"] = """apply_contains"""
        # apply class GlobalVarRef(layer5rule4class16) node
        self.add_node()

        self.vs[35]["mm__"] = """GlobalVarRef""" 
        self.vs[35]["attr1"] = """1"""
        # apply_contains node for class GlobalVarRef(layer5rule4class16)
        self.add_node()
        self.vs[36]["mm__"] = """apply_contains"""
        # apply class GlobalVariableDeclaration(layer5rule4class17) node
        self.add_node()

        self.vs[37]["mm__"] = """GlobalVariableDeclaration""" 
        self.vs[37]["attr1"] = """1"""
        # apply_contains node for class GlobalVariableDeclaration(layer5rule4class17)
        self.add_node()
        self.vs[38]["mm__"] = """apply_contains"""
        
        
        # match association TestCase--body-->StatementList node
        self.add_node()
        self.vs[39]["attr1"] = """body"""
        self.vs[39]["mm__"] = """directLink_S"""
        # match association StatementList--statements-->ExpressionStatement node
        self.add_node()
        self.vs[40]["attr1"] = """statements"""
        self.vs[40]["mm__"] = """directLink_S"""
        # match association ExpressionStatement--expr-->PortAdapterOpCallExpr node
        self.add_node()
        self.vs[41]["attr1"] = """expr"""
        self.vs[41]["mm__"] = """directLink_S"""
        # match association PortAdapterOpCallExpr--expression-->PortAdapterRefExpr node
        self.add_node()
        self.vs[42]["attr1"] = """expression"""
        self.vs[42]["mm__"] = """directLink_S"""
        # match association PortAdapterRefExpr--portAdater-->PortAdapter node
        self.add_node()
        self.vs[43]["attr1"] = """portAdater"""
        self.vs[43]["mm__"] = """directLink_S"""
        # match association PortAdapterOpCallExpr--operation-->Operation node
        self.add_node()
        self.vs[44]["attr1"] = """operation"""
        self.vs[44]["mm__"] = """directLink_S"""
        # match association PortAdapter--portRef-->AdapterInstancePortRef node
        self.add_node()
        self.vs[45]["attr1"] = """portRef"""
        self.vs[45]["mm__"] = """directLink_S"""
        # match association AdapterInstancePortRef--instance-->ComponentInstance node
        self.add_node()
        self.vs[46]["attr1"] = """instance"""
        self.vs[46]["mm__"] = """directLink_S"""
        # match association AdapterInstancePortRef--port-->ProvidedPort node
        self.add_node()
        self.vs[47]["attr1"] = """port"""
        self.vs[47]["mm__"] = """directLink_S"""
        # match association ProvidedPort--intf-->ClientServerInterface node
        self.add_node()
        self.vs[48]["attr1"] = """intf"""
        self.vs[48]["mm__"] = """directLink_S"""
        # match association ClientServerInterface--contents-->Operation node
        self.add_node()
        self.vs[49]["attr1"] = """contents"""
        self.vs[49]["mm__"] = """directLink_S"""
        
        # apply association StatementList--statements-->ExpressionStatement node
        self.add_node()
        self.vs[50]["attr1"] = """statements"""
        self.vs[50]["mm__"] = """directLink_T"""
        # apply association ExpressionStatement--expr-->FunctionCall node
        self.add_node()
        self.vs[51]["attr1"] = """expr"""
        self.vs[51]["mm__"] = """directLink_T"""
        # apply association FunctionCall--function-->FunctionPrototype node
        self.add_node()
        self.vs[52]["attr1"] = """function"""
        self.vs[52]["mm__"] = """directLink_T"""
        # apply association FunctionCall--actuals-->ReferenceExpr node
        self.add_node()
        self.vs[53]["attr1"] = """actuals"""
        self.vs[53]["mm__"] = """directLink_T"""
        # apply association ReferenceExpr--expression-->GlobalVarRef node
        self.add_node()
        self.vs[54]["attr1"] = """expression"""
        self.vs[54]["mm__"] = """directLink_T"""
        # apply association GlobalVarRef--var-->GlobalVariableDeclaration node
        self.add_node()
        self.vs[55]["attr1"] = """var"""
        self.vs[55]["mm__"] = """directLink_T"""
        
        # backward association TestCase---->StatementList node
        self.add_node()

        self.vs[56]["mm__"] = """backward_link"""
        # backward association ProvidedPort---->FunctionPrototype node
        self.add_node()

        self.vs[57]["mm__"] = """backward_link"""
        # backward association ComponentInstance---->GlobalVariableDeclaration node
        self.add_node()

        self.vs[58]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class TestCase(layer5rule4class0)
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class StatementList(layer5rule4class1)
                (0,8), # matchmodel -> match_contains
                (8,7), # match_contains -> match_class ExpressionStatement(layer5rule4class2)
                (0,10), # matchmodel -> match_contains
                (10,9), # match_contains -> match_class PortAdapterOpCallExpr(layer5rule4class3)
                (0,12), # matchmodel -> match_contains
                (12,11), # match_contains -> match_class PortAdapterRefExpr(layer5rule4class4)
                (0,14), # matchmodel -> match_contains
                (14,13), # match_contains -> match_class PortAdapter(layer5rule4class5)
                (0,16), # matchmodel -> match_contains
                (16,15), # match_contains -> match_class Operation(layer5rule4class6)
                (0,18), # matchmodel -> match_contains
                (18,17), # match_contains -> match_class AdapterInstancePortRef(layer5rule4class7)
                (0,20), # matchmodel -> match_contains
                (20,19), # match_contains -> match_class ComponentInstance(layer5rule4class8)
                (0,22), # matchmodel -> match_contains
                (22,21), # match_contains -> match_class ProvidedPort(layer5rule4class9)
                (0,24), # matchmodel -> match_contains
                (24,23), # match_contains -> match_class ClientServerInterface(layer5rule4class10)
                (1,26), # applymodel -> apply_contains
                (26,25), # apply_contains -> apply_class StatementList(layer5rule4class11)
                (1,28), # applymodel -> apply_contains
                (28,27), # apply_contains -> apply_class ExpressionStatement(layer5rule4class12)
                (1,30), # applymodel -> apply_contains
                (30,29), # apply_contains -> apply_class FunctionCall(layer5rule4class13)
                (1,32), # applymodel -> apply_contains
                (32,31), # apply_contains -> apply_class FunctionPrototype(layer5rule4class14)
                (1,34), # applymodel -> apply_contains
                (34,33), # apply_contains -> apply_class ReferenceExpr(layer5rule4class15)
                (1,36), # applymodel -> apply_contains
                (36,35), # apply_contains -> apply_class GlobalVarRef(layer5rule4class16)
                (1,38), # applymodel -> apply_contains
                (38,37), # apply_contains -> apply_class GlobalVariableDeclaration(layer5rule4class17)
                (3,39), # match_class TestCase(layer5rule4class0) -> association body
                (39,5), # association body  -> match_class StatementList(layer5rule4class1)
                (5,40), # match_class StatementList(layer5rule4class1) -> association statements
                (40,7), # association statements  -> match_class ExpressionStatement(layer5rule4class2)
                (7,41), # match_class ExpressionStatement(layer5rule4class2) -> association expr
                (41,9), # association expr  -> match_class PortAdapterOpCallExpr(layer5rule4class3)
                (9,42), # match_class PortAdapterOpCallExpr(layer5rule4class3) -> association expression
                (42,11), # association expression  -> match_class PortAdapterRefExpr(layer5rule4class4)
                (11,43), # match_class PortAdapterRefExpr(layer5rule4class4) -> association portAdater
                (43,13), # association portAdater  -> match_class PortAdapter(layer5rule4class5)
                (9,44), # match_class PortAdapterOpCallExpr(layer5rule4class3) -> association operation
                (44,15), # association operation  -> match_class Operation(layer5rule4class6)
                (13,45), # match_class PortAdapter(layer5rule4class5) -> association portRef
                (45,17), # association portRef  -> match_class AdapterInstancePortRef(layer5rule4class7)
                (17,46), # match_class AdapterInstancePortRef(layer5rule4class7) -> association instance
                (46,19), # association instance  -> match_class ComponentInstance(layer5rule4class8)
                (17,47), # match_class AdapterInstancePortRef(layer5rule4class7) -> association port
                (47,21), # association port  -> match_class ProvidedPort(layer5rule4class9)
                (21,48), # match_class ProvidedPort(layer5rule4class9) -> association intf
                (48,23), # association intf  -> match_class ClientServerInterface(layer5rule4class10)
                (23,49), # match_class ClientServerInterface(layer5rule4class10) -> association contents
                (49,15), # association contents  -> match_class Operation(layer5rule4class6)
                (25,50), # apply_class StatementList(layer5rule4class11) -> association statements
                (50,27), # association statements  -> apply_class ExpressionStatement(layer5rule4class12)
                (27,51), # apply_class ExpressionStatement(layer5rule4class12) -> association expr
                (51,29), # association expr  -> apply_class FunctionCall(layer5rule4class13)
                (29,52), # apply_class FunctionCall(layer5rule4class13) -> association function
                (52,31), # association function  -> apply_class FunctionPrototype(layer5rule4class14)
                (29,53), # apply_class FunctionCall(layer5rule4class13) -> association actuals
                (53,33), # association actuals  -> apply_class ReferenceExpr(layer5rule4class15)
                (33,54), # apply_class ReferenceExpr(layer5rule4class15) -> association expression
                (54,35), # association expression  -> apply_class GlobalVarRef(layer5rule4class16)
                (35,55), # apply_class GlobalVarRef(layer5rule4class16) -> association var
                (55,37), # association var  -> apply_class GlobalVariableDeclaration(layer5rule4class17)
                (25,56), # apply_class StatementList(layer5rule4class11) -> backward_association
                (56,3), #  backward_association -> apply_class TestCase(layer5rule4class0)
                (31,57), # apply_class FunctionPrototype(layer5rule4class14) -> backward_association
                (57,21), #  backward_association -> apply_class ProvidedPort(layer5rule4class9)
                (37,58), # apply_class GlobalVariableDeclaration(layer5rule4class17) -> backward_association
                (58,19), #  backward_association -> apply_class ComponentInstance(layer5rule4class8)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((25,'__ApplyAttribute'),('constant','TestCaseFunctionStatements')), ((31,'__ApplyAttribute'),('constant','ProvidedPortFunctionPrototype')), ((37,'__ApplyAttribute'),('constant','GlobalComponentInstanceDeclaration')), ]

        
