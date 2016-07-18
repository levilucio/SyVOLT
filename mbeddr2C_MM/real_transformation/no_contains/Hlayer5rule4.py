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
        self.vs[2]["attr1"] = """layer5rule4"""
        
        # match class TestCase(layer5rule4class0) node
        self.add_node()
        
        self.vs[3]["mm__"] = """TestCase""" 
        self.vs[3]["attr1"] = """+""" 
        # match class StatementList(layer5rule4class1) node
        self.add_node()
        
        self.vs[4]["mm__"] = """StatementList""" 
        self.vs[4]["attr1"] = """+""" 
        # match class ExpressionStatement(layer5rule4class2) node
        self.add_node()
        
        self.vs[5]["mm__"] = """ExpressionStatement""" 
        self.vs[5]["attr1"] = """+""" 
        # match class PortAdapterOpCallExpr(layer5rule4class3) node
        self.add_node()
        
        self.vs[6]["mm__"] = """PortAdapterOpCallExpr""" 
        self.vs[6]["attr1"] = """+""" 
        # match class PortAdapterRefExpr(layer5rule4class4) node
        self.add_node()
        
        self.vs[7]["mm__"] = """PortAdapterRefExpr""" 
        self.vs[7]["attr1"] = """+""" 
        # match class PortAdapter(layer5rule4class5) node
        self.add_node()
        
        self.vs[8]["mm__"] = """PortAdapter""" 
        self.vs[8]["attr1"] = """+""" 
        # match class Operation(layer5rule4class6) node
        self.add_node()
        
        self.vs[9]["mm__"] = """Operation""" 
        self.vs[9]["attr1"] = """+""" 
        # match class AdapterInstancePortRef(layer5rule4class7) node
        self.add_node()
        
        self.vs[10]["mm__"] = """AdapterInstancePortRef""" 
        self.vs[10]["attr1"] = """+""" 
        # match class ComponentInstance(layer5rule4class8) node
        self.add_node()
        
        self.vs[11]["mm__"] = """ComponentInstance""" 
        self.vs[11]["attr1"] = """+""" 
        # match class ProvidedPort(layer5rule4class9) node
        self.add_node()
        
        self.vs[12]["mm__"] = """ProvidedPort""" 
        self.vs[12]["attr1"] = """+""" 
        # match class ClientServerInterface(layer5rule4class10) node
        self.add_node()
        
        self.vs[13]["mm__"] = """ClientServerInterface""" 
        self.vs[13]["attr1"] = """+""" 
        
        
        # apply class StatementList(layer5rule4class11) node
        self.add_node()

        self.vs[14]["mm__"] = """StatementList""" 
        self.vs[14]["attr1"] = """1"""
        # apply class ExpressionStatement(layer5rule4class12) node
        self.add_node()

        self.vs[15]["mm__"] = """ExpressionStatement""" 
        self.vs[15]["attr1"] = """1"""
        # apply class FunctionCall(layer5rule4class13) node
        self.add_node()

        self.vs[16]["mm__"] = """FunctionCall""" 
        self.vs[16]["attr1"] = """1"""
        # apply class FunctionPrototype(layer5rule4class14) node
        self.add_node()

        self.vs[17]["mm__"] = """FunctionPrototype""" 
        self.vs[17]["attr1"] = """1"""
        # apply class ReferenceExpr(layer5rule4class15) node
        self.add_node()

        self.vs[18]["mm__"] = """ReferenceExpr""" 
        self.vs[18]["attr1"] = """1"""
        # apply class GlobalVarRef(layer5rule4class16) node
        self.add_node()

        self.vs[19]["mm__"] = """GlobalVarRef""" 
        self.vs[19]["attr1"] = """1"""
        # apply class GlobalVariableDeclaration(layer5rule4class17) node
        self.add_node()

        self.vs[20]["mm__"] = """GlobalVariableDeclaration""" 
        self.vs[20]["attr1"] = """1"""
        
        
        # match association TestCase--body-->StatementList node
        self.add_node()
        self.vs[21]["attr1"] = """body"""
        self.vs[21]["mm__"] = """directLink_S"""
        # match association StatementList--statements-->ExpressionStatement node
        self.add_node()
        self.vs[22]["attr1"] = """statements"""
        self.vs[22]["mm__"] = """directLink_S"""
        # match association ExpressionStatement--expr-->PortAdapterOpCallExpr node
        self.add_node()
        self.vs[23]["attr1"] = """expr"""
        self.vs[23]["mm__"] = """directLink_S"""
        # match association PortAdapterOpCallExpr--expression-->PortAdapterRefExpr node
        self.add_node()
        self.vs[24]["attr1"] = """expression"""
        self.vs[24]["mm__"] = """directLink_S"""
        # match association PortAdapterRefExpr--portAdater-->PortAdapter node
        self.add_node()
        self.vs[25]["attr1"] = """portAdater"""
        self.vs[25]["mm__"] = """directLink_S"""
        # match association PortAdapterOpCallExpr--operation-->Operation node
        self.add_node()
        self.vs[26]["attr1"] = """operation"""
        self.vs[26]["mm__"] = """directLink_S"""
        # match association PortAdapter--portRef-->AdapterInstancePortRef node
        self.add_node()
        self.vs[27]["attr1"] = """portRef"""
        self.vs[27]["mm__"] = """directLink_S"""
        # match association AdapterInstancePortRef--instance-->ComponentInstance node
        self.add_node()
        self.vs[28]["attr1"] = """instance"""
        self.vs[28]["mm__"] = """directLink_S"""
        # match association AdapterInstancePortRef--port-->ProvidedPort node
        self.add_node()
        self.vs[29]["attr1"] = """port"""
        self.vs[29]["mm__"] = """directLink_S"""
        # match association ProvidedPort--intf-->ClientServerInterface node
        self.add_node()
        self.vs[30]["attr1"] = """intf"""
        self.vs[30]["mm__"] = """directLink_S"""
        # match association ClientServerInterface--contents-->Operation node
        self.add_node()
        self.vs[31]["attr1"] = """contents"""
        self.vs[31]["mm__"] = """directLink_S"""
        
        # apply association StatementList--statements-->ExpressionStatement node
        self.add_node()
        self.vs[32]["attr1"] = """statements"""
        self.vs[32]["mm__"] = """directLink_T"""
        # apply association ExpressionStatement--expr-->FunctionCall node
        self.add_node()
        self.vs[33]["attr1"] = """expr"""
        self.vs[33]["mm__"] = """directLink_T"""
        # apply association FunctionCall--function-->FunctionPrototype node
        self.add_node()
        self.vs[34]["attr1"] = """function"""
        self.vs[34]["mm__"] = """directLink_T"""
        # apply association FunctionCall--actuals-->ReferenceExpr node
        self.add_node()
        self.vs[35]["attr1"] = """actuals"""
        self.vs[35]["mm__"] = """directLink_T"""
        # apply association ReferenceExpr--expression-->GlobalVarRef node
        self.add_node()
        self.vs[36]["attr1"] = """expression"""
        self.vs[36]["mm__"] = """directLink_T"""
        # apply association GlobalVarRef--var-->GlobalVariableDeclaration node
        self.add_node()
        self.vs[37]["attr1"] = """var"""
        self.vs[37]["mm__"] = """directLink_T"""
        
        # backward association TestCase---->StatementList node
        self.add_node()

        self.vs[38]["mm__"] = """backward_link"""
        # backward association ProvidedPort---->FunctionPrototype node
        self.add_node()

        self.vs[39]["mm__"] = """backward_link"""
        # backward association ComponentInstance---->GlobalVariableDeclaration node
        self.add_node()

        self.vs[40]["mm__"] = """backward_link"""
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class TestCase(layer5rule4class0)
                (0,4), # matchmodel -> match_class StatementList(layer5rule4class1)
                (0,5), # matchmodel -> match_class ExpressionStatement(layer5rule4class2)
                (0,6), # matchmodel -> match_class PortAdapterOpCallExpr(layer5rule4class3)
                (0,7), # matchmodel -> match_class PortAdapterRefExpr(layer5rule4class4)
                (0,8), # matchmodel -> match_class PortAdapter(layer5rule4class5)
                (0,9), # matchmodel -> match_class Operation(layer5rule4class6)
                (0,10), # matchmodel -> match_class AdapterInstancePortRef(layer5rule4class7)
                (0,11), # matchmodel -> match_class ComponentInstance(layer5rule4class8)
                (0,12), # matchmodel -> match_class ProvidedPort(layer5rule4class9)
                (0,13), # matchmodel -> match_class ClientServerInterface(layer5rule4class10)
                (1,14), # applymodel -> -> apply_class StatementList(layer5rule4class11)
                (1,15), # applymodel -> -> apply_class ExpressionStatement(layer5rule4class12)
                (1,16), # applymodel -> -> apply_class FunctionCall(layer5rule4class13)
                (1,17), # applymodel -> -> apply_class FunctionPrototype(layer5rule4class14)
                (1,18), # applymodel -> -> apply_class ReferenceExpr(layer5rule4class15)
                (1,19), # applymodel -> -> apply_class GlobalVarRef(layer5rule4class16)
                (1,20), # applymodel -> -> apply_class GlobalVariableDeclaration(layer5rule4class17)
                (3,21), # match_class TestCase(layer5rule4class0) -> association body
                (21,4), # association body  -> match_class StatementList(layer5rule4class1)
                (4,22), # match_class StatementList(layer5rule4class1) -> association statements
                (22,5), # association statements  -> match_class ExpressionStatement(layer5rule4class2)
                (5,23), # match_class ExpressionStatement(layer5rule4class2) -> association expr
                (23,6), # association expr  -> match_class PortAdapterOpCallExpr(layer5rule4class3)
                (6,24), # match_class PortAdapterOpCallExpr(layer5rule4class3) -> association expression
                (24,7), # association expression  -> match_class PortAdapterRefExpr(layer5rule4class4)
                (7,25), # match_class PortAdapterRefExpr(layer5rule4class4) -> association portAdater
                (25,8), # association portAdater  -> match_class PortAdapter(layer5rule4class5)
                (6,26), # match_class PortAdapterOpCallExpr(layer5rule4class3) -> association operation
                (26,9), # association operation  -> match_class Operation(layer5rule4class6)
                (8,27), # match_class PortAdapter(layer5rule4class5) -> association portRef
                (27,10), # association portRef  -> match_class AdapterInstancePortRef(layer5rule4class7)
                (10,28), # match_class AdapterInstancePortRef(layer5rule4class7) -> association instance
                (28,11), # association instance  -> match_class ComponentInstance(layer5rule4class8)
                (10,29), # match_class AdapterInstancePortRef(layer5rule4class7) -> association port
                (29,12), # association port  -> match_class ProvidedPort(layer5rule4class9)
                (12,30), # match_class ProvidedPort(layer5rule4class9) -> association intf
                (30,13), # association intf  -> match_class ClientServerInterface(layer5rule4class10)
                (13,31), # match_class ClientServerInterface(layer5rule4class10) -> association contents
                (31,9), # association contents  -> match_class Operation(layer5rule4class6)
                (14,32), # apply_class StatementList(layer5rule4class11) -> association statements
                (32,15), # association statements  -> apply_class ExpressionStatement(layer5rule4class12)
                (15,33), # apply_class ExpressionStatement(layer5rule4class12) -> association expr
                (33,16), # association expr  -> apply_class FunctionCall(layer5rule4class13)
                (16,34), # apply_class FunctionCall(layer5rule4class13) -> association function
                (34,17), # association function  -> apply_class FunctionPrototype(layer5rule4class14)
                (16,35), # apply_class FunctionCall(layer5rule4class13) -> association actuals
                (35,18), # association actuals  -> apply_class ReferenceExpr(layer5rule4class15)
                (18,36), # apply_class ReferenceExpr(layer5rule4class15) -> association expression
                (36,19), # association expression  -> apply_class GlobalVarRef(layer5rule4class16)
                (19,37), # apply_class GlobalVarRef(layer5rule4class16) -> association var
                (37,20), # association var  -> apply_class GlobalVariableDeclaration(layer5rule4class17)
                (14,38), # apply_class StatementList(layer5rule4class11) -> backward_association
                (38,3), #  backward_association -> apply_class TestCase(layer5rule4class0)
                (17,39), # apply_class FunctionPrototype(layer5rule4class14) -> backward_association
                (39,12), #  backward_association -> apply_class ProvidedPort(layer5rule4class9)
                (20,40), # apply_class GlobalVariableDeclaration(layer5rule4class17) -> backward_association
                (40,11), #  backward_association -> apply_class ComponentInstance(layer5rule4class8)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((14,'__ApplyAttribute'),('constant','TestCaseFunctionStatements')), ((17,'__ApplyAttribute'),('constant','ProvidedPortFunctionPrototype')), ((20,'__ApplyAttribute'),('constant','GlobalComponentInstanceDeclaration')), ]

        
