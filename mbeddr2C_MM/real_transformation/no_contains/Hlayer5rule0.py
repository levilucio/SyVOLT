from core.himesis import Himesis
import uuid

class Hlayer5rule0(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule layer5rule0.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer5rule0, self).__init__(name='Hlayer5rule0', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer5rule0"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["attr1"] = """layer5rule0"""
        
        # match class ComponentInstance(layer5rule0class0) node
        self.add_node()
        
        self.vs[3]["mm__"] = """ComponentInstance""" 
        self.vs[3]["attr1"] = """+""" 
        # match class AtomicComponent(layer5rule0class1) node
        self.add_node()
        
        self.vs[4]["mm__"] = """AtomicComponent""" 
        self.vs[4]["attr1"] = """+""" 
        # match class ProvidedPort(layer5rule0class2) node
        self.add_node()
        
        self.vs[5]["mm__"] = """ProvidedPort""" 
        self.vs[5]["attr1"] = """+""" 
        # match class ClientServerInterface(layer5rule0class3) node
        self.add_node()
        
        self.vs[6]["mm__"] = """ClientServerInterface""" 
        self.vs[6]["attr1"] = """+""" 
        # match class Operation(layer5rule0class4) node
        self.add_node()
        
        self.vs[7]["mm__"] = """Operation""" 
        self.vs[7]["attr1"] = """+""" 
        
        
        # apply class StatementList(layer5rule0class5) node
        self.add_node()

        self.vs[8]["mm__"] = """StatementList""" 
        self.vs[8]["attr1"] = """1"""
        # apply class GlobalVariableDeclaration(layer5rule0class6) node
        self.add_node()

        self.vs[9]["mm__"] = """GlobalVariableDeclaration""" 
        self.vs[9]["attr1"] = """1"""
        # apply class ExpressionStatement(layer5rule0class7) node
        self.add_node()

        self.vs[10]["mm__"] = """ExpressionStatement""" 
        self.vs[10]["attr1"] = """1"""
        # apply class AssignmentExpr(layer5rule0class8) node
        self.add_node()

        self.vs[11]["mm__"] = """AssignmentExpr""" 
        self.vs[11]["attr1"] = """1"""
        # apply class GenericDotExpression(layer5rule0class9) node
        self.add_node()

        self.vs[12]["mm__"] = """GenericDotExpression""" 
        self.vs[12]["attr1"] = """1"""
        # apply class ReferenceExpr(layer5rule0class10) node
        self.add_node()

        self.vs[13]["mm__"] = """ReferenceExpr""" 
        self.vs[13]["attr1"] = """1"""
        # apply class GlobalVarRef(layer5rule0class11) node
        self.add_node()

        self.vs[14]["mm__"] = """GlobalVarRef""" 
        self.vs[14]["attr1"] = """1"""
        # apply class GenericMemberRef(layer5rule0class12) node
        self.add_node()

        self.vs[15]["mm__"] = """GenericMemberRef""" 
        self.vs[15]["attr1"] = """1"""
        # apply class CFunctionPointerStructMember(layer5rule0class13) node
        self.add_node()

        self.vs[16]["mm__"] = """CFunctionPointerStructMember""" 
        self.vs[16]["attr1"] = """1"""
        # apply class FunctionPrototype(layer5rule0class14) node
        self.add_node()

        self.vs[17]["mm__"] = """FunctionPrototype""" 
        self.vs[17]["attr1"] = """1"""
        # apply class FunctionRefExpr(layer5rule0class15) node
        self.add_node()

        self.vs[18]["mm__"] = """FunctionRefExpr""" 
        self.vs[18]["attr1"] = """1"""
        
        
        # match association ComponentInstance--component-->AtomicComponent node
        self.add_node()
        self.vs[19]["attr1"] = """component"""
        self.vs[19]["mm__"] = """directLink_S"""
        # match association AtomicComponent--contents-->ProvidedPort node
        self.add_node()
        self.vs[20]["attr1"] = """contents"""
        self.vs[20]["mm__"] = """directLink_S"""
        # match association ProvidedPort--intf-->ClientServerInterface node
        self.add_node()
        self.vs[21]["attr1"] = """intf"""
        self.vs[21]["mm__"] = """directLink_S"""
        # match association ClientServerInterface--contents-->Operation node
        self.add_node()
        self.vs[22]["attr1"] = """contents"""
        self.vs[22]["mm__"] = """directLink_S"""
        
        # apply association StatementList--statements-->ExpressionStatement node
        self.add_node()
        self.vs[23]["attr1"] = """statements"""
        self.vs[23]["mm__"] = """directLink_T"""
        # apply association ExpressionStatement--expr-->AssignmentExpr node
        self.add_node()
        self.vs[24]["attr1"] = """expr"""
        self.vs[24]["mm__"] = """directLink_T"""
        # apply association AssignmentExpr--left-->GenericDotExpression node
        self.add_node()
        self.vs[25]["attr1"] = """left"""
        self.vs[25]["mm__"] = """directLink_T"""
        # apply association AssignmentExpr--right-->ReferenceExpr node
        self.add_node()
        self.vs[26]["attr1"] = """right"""
        self.vs[26]["mm__"] = """directLink_T"""
        # apply association GenericDotExpression--expression-->GlobalVarRef node
        self.add_node()
        self.vs[27]["attr1"] = """expression"""
        self.vs[27]["mm__"] = """directLink_T"""
        # apply association GenericDotExpression--target-->GenericMemberRef node
        self.add_node()
        self.vs[28]["attr1"] = """target"""
        self.vs[28]["mm__"] = """directLink_T"""
        # apply association GlobalVarRef--var-->GlobalVariableDeclaration node
        self.add_node()
        self.vs[29]["attr1"] = """var"""
        self.vs[29]["mm__"] = """directLink_T"""
        # apply association GenericMemberRef--member-->CFunctionPointerStructMember node
        self.add_node()
        self.vs[30]["attr1"] = """member"""
        self.vs[30]["mm__"] = """directLink_T"""
        # apply association ReferenceExpr--expression-->FunctionRefExpr node
        self.add_node()
        self.vs[31]["attr1"] = """expression"""
        self.vs[31]["mm__"] = """directLink_T"""
        # apply association FunctionRefExpr--function-->FunctionPrototype node
        self.add_node()
        self.vs[32]["attr1"] = """function"""
        self.vs[32]["mm__"] = """directLink_T"""
        
        # backward association ComponentInstance---->StatementList node
        self.add_node()

        self.vs[33]["mm__"] = """backward_link"""
        # backward association ProvidedPort---->GlobalVariableDeclaration node
        self.add_node()

        self.vs[34]["mm__"] = """backward_link"""
        # backward association Operation---->CFunctionPointerStructMember node
        self.add_node()

        self.vs[35]["mm__"] = """backward_link"""
        # backward association ProvidedPort---->FunctionPrototype node
        self.add_node()

        self.vs[36]["mm__"] = """backward_link"""
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class ComponentInstance(layer5rule0class0)
                (0,4), # matchmodel -> match_class AtomicComponent(layer5rule0class1)
                (0,5), # matchmodel -> match_class ProvidedPort(layer5rule0class2)
                (0,6), # matchmodel -> match_class ClientServerInterface(layer5rule0class3)
                (0,7), # matchmodel -> match_class Operation(layer5rule0class4)
                (1,8), # applymodel -> -> apply_class StatementList(layer5rule0class5)
                (1,9), # applymodel -> -> apply_class GlobalVariableDeclaration(layer5rule0class6)
                (1,10), # applymodel -> -> apply_class ExpressionStatement(layer5rule0class7)
                (1,11), # applymodel -> -> apply_class AssignmentExpr(layer5rule0class8)
                (1,12), # applymodel -> -> apply_class GenericDotExpression(layer5rule0class9)
                (1,13), # applymodel -> -> apply_class ReferenceExpr(layer5rule0class10)
                (1,14), # applymodel -> -> apply_class GlobalVarRef(layer5rule0class11)
                (1,15), # applymodel -> -> apply_class GenericMemberRef(layer5rule0class12)
                (1,16), # applymodel -> -> apply_class CFunctionPointerStructMember(layer5rule0class13)
                (1,17), # applymodel -> -> apply_class FunctionPrototype(layer5rule0class14)
                (1,18), # applymodel -> -> apply_class FunctionRefExpr(layer5rule0class15)
                (3,19), # match_class ComponentInstance(layer5rule0class0) -> association component
                (19,4), # association component  -> match_class AtomicComponent(layer5rule0class1)
                (4,20), # match_class AtomicComponent(layer5rule0class1) -> association contents
                (20,5), # association contents  -> match_class ProvidedPort(layer5rule0class2)
                (5,21), # match_class ProvidedPort(layer5rule0class2) -> association intf
                (21,6), # association intf  -> match_class ClientServerInterface(layer5rule0class3)
                (6,22), # match_class ClientServerInterface(layer5rule0class3) -> association contents
                (22,7), # association contents  -> match_class Operation(layer5rule0class4)
                (8,23), # apply_class StatementList(layer5rule0class5) -> association statements
                (23,10), # association statements  -> apply_class ExpressionStatement(layer5rule0class7)
                (10,24), # apply_class ExpressionStatement(layer5rule0class7) -> association expr
                (24,11), # association expr  -> apply_class AssignmentExpr(layer5rule0class8)
                (11,25), # apply_class AssignmentExpr(layer5rule0class8) -> association left
                (25,12), # association left  -> apply_class GenericDotExpression(layer5rule0class9)
                (11,26), # apply_class AssignmentExpr(layer5rule0class8) -> association right
                (26,13), # association right  -> apply_class ReferenceExpr(layer5rule0class10)
                (12,27), # apply_class GenericDotExpression(layer5rule0class9) -> association expression
                (27,14), # association expression  -> apply_class GlobalVarRef(layer5rule0class11)
                (12,28), # apply_class GenericDotExpression(layer5rule0class9) -> association target
                (28,15), # association target  -> apply_class GenericMemberRef(layer5rule0class12)
                (14,29), # apply_class GlobalVarRef(layer5rule0class11) -> association var
                (29,9), # association var  -> apply_class GlobalVariableDeclaration(layer5rule0class6)
                (15,30), # apply_class GenericMemberRef(layer5rule0class12) -> association member
                (30,16), # association member  -> apply_class CFunctionPointerStructMember(layer5rule0class13)
                (13,31), # apply_class ReferenceExpr(layer5rule0class10) -> association expression
                (31,18), # association expression  -> apply_class FunctionRefExpr(layer5rule0class15)
                (18,32), # apply_class FunctionRefExpr(layer5rule0class15) -> association function
                (32,17), # association function  -> apply_class FunctionPrototype(layer5rule0class14)
                (8,33), # apply_class StatementList(layer5rule0class5) -> backward_association
                (33,3), #  backward_association -> apply_class ComponentInstance(layer5rule0class0)
                (9,34), # apply_class GlobalVariableDeclaration(layer5rule0class6) -> backward_association
                (34,5), #  backward_association -> apply_class ProvidedPort(layer5rule0class2)
                (16,35), # apply_class CFunctionPointerStructMember(layer5rule0class13) -> backward_association
                (35,7), #  backward_association -> apply_class Operation(layer5rule0class4)
                (17,36), # apply_class FunctionPrototype(layer5rule0class14) -> backward_association
                (36,5), #  backward_association -> apply_class ProvidedPort(layer5rule0class2)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((8,'__ApplyAttribute'),('constant','WireFunctionStatements')), ((9,'__ApplyAttribute'),('constant','GlobalVarOps')), ((16,'__ApplyAttribute'),('constant','CFunctionPointerStructMember')), ((17,'__ApplyAttribute'),('constant','ProvidedPortFunctionPrototype')), ]

        
