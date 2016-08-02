from core.himesis import Himesis
import uuid

class Hlayer5rule1copy(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule layer5rule1.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer5rule1copy, self).__init__(name='Hlayer5rule1copy', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """Hlayer5rule1copy"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Hlayer5rule1copy')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["attr1"] = """layer5rule1"""
        
        # match class ComponentInstance(layer5rule1class0) node
        self.add_node()
        
        self.vs[3]["mm__"] = """ComponentInstance""" 
        self.vs[3]["attr1"] = """+""" 
        # match class AtomicComponent(layer5rule1class1) node
        self.add_node()
        
        self.vs[4]["mm__"] = """AtomicComponent""" 
        self.vs[4]["attr1"] = """+""" 
        # match class RequiredPort(layer5rule1class2) node
        self.add_node()
        
        self.vs[5]["mm__"] = """RequiredPort""" 
        self.vs[5]["attr1"] = """+""" 
        # match class InstanceConfiguration(layer5rule1class3) node
        self.add_node()
        
        self.vs[6]["mm__"] = """InstanceConfiguration""" 
        self.vs[6]["attr1"] = """+""" 
        # match class AssemblyConnector(layer5rule1class4) node
        self.add_node()
        
        self.vs[7]["mm__"] = """AssemblyConnector""" 
        self.vs[7]["attr1"] = """+""" 
        # match class InstancePortRef(layer5rule1class5) node
        self.add_node()
        
        self.vs[8]["mm__"] = """InstancePortRef""" 
        self.vs[8]["attr1"] = """+""" 
        # match class InstancePortRef(layer5rule1class6) node
        self.add_node()
        
        self.vs[9]["mm__"] = """InstancePortRef""" 
        self.vs[9]["attr1"] = """+""" 
        # match class ComponentInstance(layer5rule1class7) node
        self.add_node()
        
        self.vs[10]["mm__"] = """ComponentInstance""" 
        self.vs[10]["attr1"] = """+""" 
        # match class AtomicComponent(layer5rule1class8) node
        self.add_node()
        
        self.vs[11]["mm__"] = """AtomicComponent""" 
        self.vs[11]["attr1"] = """+""" 
        # match class ProvidedPort(layer5rule1class9) node
        self.add_node()
        
        self.vs[12]["mm__"] = """ProvidedPort""" 
        self.vs[12]["attr1"] = """+""" 
        # match class ClientServerInterface(layer5rule1class10) node
        self.add_node()
        
        self.vs[13]["mm__"] = """ClientServerInterface""" 
        self.vs[13]["attr1"] = """+""" 
        
        
        # apply class StatementList(layer5rule1class11) node
        self.add_node()

        self.vs[14]["mm__"] = """StatementList""" 
        self.vs[14]["attr1"] = """1"""
        # apply class GlobalVariableDeclaration(layer5rule1class12) node
        self.add_node()

        self.vs[15]["mm__"] = """GlobalVariableDeclaration""" 
        self.vs[15]["attr1"] = """1"""
        # apply class ExpressionStatement(layer5rule1class13) node
        self.add_node()

        self.vs[16]["mm__"] = """ExpressionStatement""" 
        self.vs[16]["attr1"] = """1"""
        # apply class AssignmentExpr(layer5rule1class14) node
        self.add_node()

        self.vs[17]["mm__"] = """AssignmentExpr""" 
        self.vs[17]["attr1"] = """1"""
        # apply class GenericDotExpression(layer5rule1class15) node
        self.add_node()

        self.vs[18]["mm__"] = """GenericDotExpression""" 
        self.vs[18]["attr1"] = """1"""
        # apply class ReferenceExpr(layer5rule1class16) node
        self.add_node()

        self.vs[19]["mm__"] = """ReferenceExpr""" 
        self.vs[19]["attr1"] = """1"""
        # apply class GlobalVarRef(layer5rule1class17) node
        self.add_node()

        self.vs[20]["mm__"] = """GlobalVarRef""" 
        self.vs[20]["attr1"] = """1"""
        # apply class GenericMemberRef(layer5rule1class18) node
        self.add_node()

        self.vs[21]["mm__"] = """GenericMemberRef""" 
        self.vs[21]["attr1"] = """1"""
        # apply class Member(layer5rule1class19) node
        self.add_node()

        self.vs[22]["mm__"] = """Member""" 
        self.vs[22]["attr1"] = """1"""
        # apply class GlobalVariableDeclaration(layer5rule1class20) node
        self.add_node()

        self.vs[23]["mm__"] = """GlobalVariableDeclaration""" 
        self.vs[23]["attr1"] = """1"""
        # apply class GlobalVarRef(layer5rule1class21) node
        self.add_node()

        self.vs[24]["mm__"] = """GlobalVarRef""" 
        self.vs[24]["attr1"] = """1"""
        # apply class ExpressionStatement(layer5rule1class22) node
        self.add_node()

        self.vs[25]["mm__"] = """ExpressionStatement""" 
        self.vs[25]["attr1"] = """1"""
        # apply class AssignmentExpr(layer5rule1class23) node
        self.add_node()

        self.vs[26]["mm__"] = """AssignmentExpr""" 
        self.vs[26]["attr1"] = """1"""
        # apply class GenericDotExpression(layer5rule1class24) node
        self.add_node()

        self.vs[27]["mm__"] = """GenericDotExpression""" 
        self.vs[27]["attr1"] = """1"""
        # apply class GlobalVarRef(layer5rule1class25) node
        self.add_node()

        self.vs[28]["mm__"] = """GlobalVarRef""" 
        self.vs[28]["attr1"] = """1"""
        # apply class GenericMemberRef(layer5rule1class26) node
        self.add_node()

        self.vs[29]["mm__"] = """GenericMemberRef""" 
        self.vs[29]["attr1"] = """1"""
        # apply class Member(layer5rule1class27) node
        self.add_node()

        self.vs[30]["mm__"] = """Member""" 
        self.vs[30]["attr1"] = """1"""
        # apply class ReferenceExpr(layer5rule1class28) node
        self.add_node()

        self.vs[31]["mm__"] = """ReferenceExpr""" 
        self.vs[31]["attr1"] = """1"""
        # apply class GlobalVarRef(layer5rule1class29) node
        self.add_node()

        self.vs[32]["mm__"] = """GlobalVarRef""" 
        self.vs[32]["attr1"] = """1"""
        # apply class GlobalVariableDeclaration(layer5rule1class30) node
        self.add_node()

        self.vs[33]["mm__"] = """GlobalVariableDeclaration""" 
        self.vs[33]["attr1"] = """1"""
        
        
        # match association ComponentInstance--component-->AtomicComponent node
        self.add_node()
        self.vs[34]["attr1"] = """component"""
        self.vs[34]["mm__"] = """directLink_S"""
        # match association AtomicComponent--contents-->RequiredPort node
        self.add_node()
        self.vs[35]["attr1"] = """contents"""
        self.vs[35]["mm__"] = """directLink_S"""
        # match association InstanceConfiguration--contents-->ComponentInstance node
        self.add_node()
        self.vs[36]["attr1"] = """contents"""
        self.vs[36]["mm__"] = """directLink_S"""
        # match association InstanceConfiguration--contents-->AssemblyConnector node
        self.add_node()
        self.vs[37]["attr1"] = """contents"""
        self.vs[37]["mm__"] = """directLink_S"""
        # match association AssemblyConnector--source-->InstancePortRef node
        self.add_node()
        self.vs[38]["attr1"] = """source"""
        self.vs[38]["mm__"] = """directLink_S"""
        # match association InstancePortRef--instance-->ComponentInstance node
        self.add_node()
        self.vs[39]["attr1"] = """instance"""
        self.vs[39]["mm__"] = """directLink_S"""
        # match association InstancePortRef--port-->RequiredPort node
        self.add_node()
        self.vs[40]["attr1"] = """port"""
        self.vs[40]["mm__"] = """directLink_S"""
        # match association InstanceConfiguration--contents-->ComponentInstance node
        self.add_node()
        self.vs[41]["attr1"] = """contents"""
        self.vs[41]["mm__"] = """directLink_S"""
        # match association InstancePortRef--instance-->ComponentInstance node
        self.add_node()
        self.vs[42]["attr1"] = """instance"""
        self.vs[42]["mm__"] = """directLink_S"""
        # match association AssemblyConnector--target-->InstancePortRef node
        self.add_node()
        self.vs[43]["attr1"] = """target"""
        self.vs[43]["mm__"] = """directLink_S"""
        # match association ComponentInstance--component-->AtomicComponent node
        self.add_node()
        self.vs[44]["attr1"] = """component"""
        self.vs[44]["mm__"] = """directLink_S"""
        # match association AtomicComponent--contents-->ProvidedPort node
        self.add_node()
        self.vs[45]["attr1"] = """contents"""
        self.vs[45]["mm__"] = """directLink_S"""
        # match association ProvidedPort--intf-->ClientServerInterface node
        self.add_node()
        self.vs[46]["attr1"] = """intf"""
        self.vs[46]["mm__"] = """directLink_S"""
        # match association RequiredPort--intf-->ClientServerInterface node
        self.add_node()
        self.vs[47]["attr1"] = """intf"""
        self.vs[47]["mm__"] = """directLink_S"""
        
        # apply association StatementList--statements-->ExpressionStatement node
        self.add_node()
        self.vs[48]["attr1"] = """statements"""
        self.vs[48]["mm__"] = """directLink_T"""
        # apply association ExpressionStatement--expr-->AssignmentExpr node
        self.add_node()
        self.vs[49]["attr1"] = """expr"""
        self.vs[49]["mm__"] = """directLink_T"""
        # apply association AssignmentExpr--left-->GenericDotExpression node
        self.add_node()
        self.vs[50]["attr1"] = """left"""
        self.vs[50]["mm__"] = """directLink_T"""
        # apply association AssignmentExpr--right-->ReferenceExpr node
        self.add_node()
        self.vs[51]["attr1"] = """right"""
        self.vs[51]["mm__"] = """directLink_T"""
        # apply association GenericDotExpression--expression-->GlobalVarRef node
        self.add_node()
        self.vs[52]["attr1"] = """expression"""
        self.vs[52]["mm__"] = """directLink_T"""
        # apply association GenericDotExpression--target-->GenericMemberRef node
        self.add_node()
        self.vs[53]["attr1"] = """target"""
        self.vs[53]["mm__"] = """directLink_T"""
        # apply association GlobalVarRef--var-->GlobalVariableDeclaration node
        self.add_node()
        self.vs[54]["attr1"] = """var"""
        self.vs[54]["mm__"] = """directLink_T"""
        # apply association GenericMemberRef--member-->Member node
        self.add_node()
        self.vs[55]["attr1"] = """member"""
        self.vs[55]["mm__"] = """directLink_T"""
        # apply association ReferenceExpr--expression-->GlobalVarRef node
        self.add_node()
        self.vs[56]["attr1"] = """expression"""
        self.vs[56]["mm__"] = """directLink_T"""
        # apply association GlobalVarRef--var-->GlobalVariableDeclaration node
        self.add_node()
        self.vs[57]["attr1"] = """var"""
        self.vs[57]["mm__"] = """directLink_T"""
        # apply association StatementList--statements-->ExpressionStatement node
        self.add_node()
        self.vs[58]["attr1"] = """statements"""
        self.vs[58]["mm__"] = """directLink_T"""
        # apply association ExpressionStatement--expr-->AssignmentExpr node
        self.add_node()
        self.vs[59]["attr1"] = """expr"""
        self.vs[59]["mm__"] = """directLink_T"""
        # apply association AssignmentExpr--left-->GenericDotExpression node
        self.add_node()
        self.vs[60]["attr1"] = """left"""
        self.vs[60]["mm__"] = """directLink_T"""
        # apply association GenericDotExpression--expression-->GlobalVarRef node
        self.add_node()
        self.vs[61]["attr1"] = """expression"""
        self.vs[61]["mm__"] = """directLink_T"""
        # apply association GlobalVarRef--var-->GlobalVariableDeclaration node
        self.add_node()
        self.vs[62]["attr1"] = """var"""
        self.vs[62]["mm__"] = """directLink_T"""
        # apply association GenericDotExpression--target-->GenericMemberRef node
        self.add_node()
        self.vs[63]["attr1"] = """target"""
        self.vs[63]["mm__"] = """directLink_T"""
        # apply association GenericMemberRef--member-->Member node
        self.add_node()
        self.vs[64]["attr1"] = """member"""
        self.vs[64]["mm__"] = """directLink_T"""
        # apply association AssignmentExpr--right-->ReferenceExpr node
        self.add_node()
        self.vs[65]["attr1"] = """right"""
        self.vs[65]["mm__"] = """directLink_T"""
        # apply association ReferenceExpr--expression-->GlobalVarRef node
        self.add_node()
        self.vs[66]["attr1"] = """expression"""
        self.vs[66]["mm__"] = """directLink_T"""
        # apply association GlobalVarRef--var-->GlobalVariableDeclaration node
        self.add_node()
        self.vs[67]["attr1"] = """var"""
        self.vs[67]["mm__"] = """directLink_T"""
        
        # backward association ComponentInstance---->StatementList node
        self.add_node()

        self.vs[68]["mm__"] = """backward_link"""
        # backward association ComponentInstance---->GlobalVariableDeclaration node
        self.add_node()

        self.vs[69]["mm__"] = """backward_link"""
        # backward association RequiredPort---->Member node
        self.add_node()

        self.vs[70]["mm__"] = """backward_link"""
        # backward association ComponentInstance---->GlobalVariableDeclaration node
        self.add_node()

        self.vs[71]["mm__"] = """backward_link"""
        # backward association RequiredPort---->Member node
        self.add_node()

        self.vs[72]["mm__"] = """backward_link"""
        # backward association ProvidedPort---->GlobalVariableDeclaration node
        self.add_node()

        self.vs[73]["mm__"] = """backward_link"""
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class ComponentInstance(layer5rule1class0)
                (0,4), # matchmodel -> match_class AtomicComponent(layer5rule1class1)
                (0,5), # matchmodel -> match_class RequiredPort(layer5rule1class2)
                (0,6), # matchmodel -> match_class InstanceConfiguration(layer5rule1class3)
                (0,7), # matchmodel -> match_class AssemblyConnector(layer5rule1class4)
                (0,8), # matchmodel -> match_class InstancePortRef(layer5rule1class5)
                (0,9), # matchmodel -> match_class InstancePortRef(layer5rule1class6)
                (0,10), # matchmodel -> match_class ComponentInstance(layer5rule1class7)
                (0,11), # matchmodel -> match_class AtomicComponent(layer5rule1class8)
                (0,12), # matchmodel -> match_class ProvidedPort(layer5rule1class9)
                (0,13), # matchmodel -> match_class ClientServerInterface(layer5rule1class10)
                (1,14), # applymodel -> -> apply_class StatementList(layer5rule1class11)
                (1,15), # applymodel -> -> apply_class GlobalVariableDeclaration(layer5rule1class12)
                (1,16), # applymodel -> -> apply_class ExpressionStatement(layer5rule1class13)
                (1,17), # applymodel -> -> apply_class AssignmentExpr(layer5rule1class14)
                (1,18), # applymodel -> -> apply_class GenericDotExpression(layer5rule1class15)
                (1,19), # applymodel -> -> apply_class ReferenceExpr(layer5rule1class16)
                (1,20), # applymodel -> -> apply_class GlobalVarRef(layer5rule1class17)
                (1,21), # applymodel -> -> apply_class GenericMemberRef(layer5rule1class18)
                (1,22), # applymodel -> -> apply_class Member(layer5rule1class19)
                (1,23), # applymodel -> -> apply_class GlobalVariableDeclaration(layer5rule1class20)
                (1,24), # applymodel -> -> apply_class GlobalVarRef(layer5rule1class21)
                (1,25), # applymodel -> -> apply_class ExpressionStatement(layer5rule1class22)
                (1,26), # applymodel -> -> apply_class AssignmentExpr(layer5rule1class23)
                (1,27), # applymodel -> -> apply_class GenericDotExpression(layer5rule1class24)
                (1,28), # applymodel -> -> apply_class GlobalVarRef(layer5rule1class25)
                (1,29), # applymodel -> -> apply_class GenericMemberRef(layer5rule1class26)
                (1,30), # applymodel -> -> apply_class Member(layer5rule1class27)
                (1,31), # applymodel -> -> apply_class ReferenceExpr(layer5rule1class28)
                (1,32), # applymodel -> -> apply_class GlobalVarRef(layer5rule1class29)
                (1,33), # applymodel -> -> apply_class GlobalVariableDeclaration(layer5rule1class30)
                (3,34), # match_class ComponentInstance(layer5rule1class0) -> association component
                (34,4), # association component  -> match_class AtomicComponent(layer5rule1class1)
                (4,35), # match_class AtomicComponent(layer5rule1class1) -> association contents
                (35,5), # association contents  -> match_class RequiredPort(layer5rule1class2)
                (6,36), # match_class InstanceConfiguration(layer5rule1class3) -> association contents
                (36,3), # association contents  -> match_class ComponentInstance(layer5rule1class0)
                (6,37), # match_class InstanceConfiguration(layer5rule1class3) -> association contents
                (37,7), # association contents  -> match_class AssemblyConnector(layer5rule1class4)
                (7,38), # match_class AssemblyConnector(layer5rule1class4) -> association source
                (38,8), # association source  -> match_class InstancePortRef(layer5rule1class5)
                (8,39), # match_class InstancePortRef(layer5rule1class5) -> association instance
                (39,3), # association instance  -> match_class ComponentInstance(layer5rule1class0)
                (8,40), # match_class InstancePortRef(layer5rule1class5) -> association port
                (40,5), # association port  -> match_class RequiredPort(layer5rule1class2)
                (6,41), # match_class InstanceConfiguration(layer5rule1class3) -> association contents
                (41,10), # association contents  -> match_class ComponentInstance(layer5rule1class7)
                (9,42), # match_class InstancePortRef(layer5rule1class6) -> association instance
                (42,10), # association instance  -> match_class ComponentInstance(layer5rule1class7)
                (7,43), # match_class AssemblyConnector(layer5rule1class4) -> association target
                (43,9), # association target  -> match_class InstancePortRef(layer5rule1class6)
                (10,44), # match_class ComponentInstance(layer5rule1class7) -> association component
                (44,11), # association component  -> match_class AtomicComponent(layer5rule1class8)
                (11,45), # match_class AtomicComponent(layer5rule1class8) -> association contents
                (45,12), # association contents  -> match_class ProvidedPort(layer5rule1class9)
                (12,46), # match_class ProvidedPort(layer5rule1class9) -> association intf
                (46,13), # association intf  -> match_class ClientServerInterface(layer5rule1class10)
                (5,47), # match_class RequiredPort(layer5rule1class2) -> association intf
                (47,13), # association intf  -> match_class ClientServerInterface(layer5rule1class10)
                (14,48), # apply_class StatementList(layer5rule1class11) -> association statements
                (48,16), # association statements  -> apply_class ExpressionStatement(layer5rule1class13)
                (16,49), # apply_class ExpressionStatement(layer5rule1class13) -> association expr
                (49,17), # association expr  -> apply_class AssignmentExpr(layer5rule1class14)
                (17,50), # apply_class AssignmentExpr(layer5rule1class14) -> association left
                (50,18), # association left  -> apply_class GenericDotExpression(layer5rule1class15)
                (17,51), # apply_class AssignmentExpr(layer5rule1class14) -> association right
                (51,19), # association right  -> apply_class ReferenceExpr(layer5rule1class16)
                (18,52), # apply_class GenericDotExpression(layer5rule1class15) -> association expression
                (52,20), # association expression  -> apply_class GlobalVarRef(layer5rule1class17)
                (18,53), # apply_class GenericDotExpression(layer5rule1class15) -> association target
                (53,21), # association target  -> apply_class GenericMemberRef(layer5rule1class18)
                (20,54), # apply_class GlobalVarRef(layer5rule1class17) -> association var
                (54,15), # association var  -> apply_class GlobalVariableDeclaration(layer5rule1class12)
                (21,55), # apply_class GenericMemberRef(layer5rule1class18) -> association member
                (55,22), # association member  -> apply_class Member(layer5rule1class19)
                (19,56), # apply_class ReferenceExpr(layer5rule1class16) -> association expression
                (56,24), # association expression  -> apply_class GlobalVarRef(layer5rule1class21)
                (24,57), # apply_class GlobalVarRef(layer5rule1class21) -> association var
                (57,23), # association var  -> apply_class GlobalVariableDeclaration(layer5rule1class20)
                (14,58), # apply_class StatementList(layer5rule1class11) -> association statements
                (58,25), # association statements  -> apply_class ExpressionStatement(layer5rule1class22)
                (25,59), # apply_class ExpressionStatement(layer5rule1class22) -> association expr
                (59,26), # association expr  -> apply_class AssignmentExpr(layer5rule1class23)
                (26,60), # apply_class AssignmentExpr(layer5rule1class23) -> association left
                (60,27), # association left  -> apply_class GenericDotExpression(layer5rule1class24)
                (27,61), # apply_class GenericDotExpression(layer5rule1class24) -> association expression
                (61,28), # association expression  -> apply_class GlobalVarRef(layer5rule1class25)
                (28,62), # apply_class GlobalVarRef(layer5rule1class25) -> association var
                (62,15), # association var  -> apply_class GlobalVariableDeclaration(layer5rule1class12)
                (27,63), # apply_class GenericDotExpression(layer5rule1class24) -> association target
                (63,29), # association target  -> apply_class GenericMemberRef(layer5rule1class26)
                (29,64), # apply_class GenericMemberRef(layer5rule1class26) -> association member
                (64,30), # association member  -> apply_class Member(layer5rule1class27)
                (26,65), # apply_class AssignmentExpr(layer5rule1class23) -> association right
                (65,31), # association right  -> apply_class ReferenceExpr(layer5rule1class28)
                (31,66), # apply_class ReferenceExpr(layer5rule1class28) -> association expression
                (66,32), # association expression  -> apply_class GlobalVarRef(layer5rule1class29)
                (32,67), # apply_class GlobalVarRef(layer5rule1class29) -> association var
                (67,33), # association var  -> apply_class GlobalVariableDeclaration(layer5rule1class30)
                (14,68), # apply_class StatementList(layer5rule1class11) -> backward_association
                (68,3), #  backward_association -> apply_class ComponentInstance(layer5rule1class0)
                (15,69), # apply_class GlobalVariableDeclaration(layer5rule1class12) -> backward_association
                (69,3), #  backward_association -> apply_class ComponentInstance(layer5rule1class0)
                (22,70), # apply_class Member(layer5rule1class19) -> backward_association
                (70,5), #  backward_association -> apply_class RequiredPort(layer5rule1class2)
                (23,71), # apply_class GlobalVariableDeclaration(layer5rule1class20) -> backward_association
                (71,10), #  backward_association -> apply_class ComponentInstance(layer5rule1class7)
                (30,72), # apply_class Member(layer5rule1class27) -> backward_association
                (72,5), #  backward_association -> apply_class RequiredPort(layer5rule1class2)
                (33,73), # apply_class GlobalVariableDeclaration(layer5rule1class30) -> backward_association
                (73,12), #  backward_association -> apply_class ProvidedPort(layer5rule1class9)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((14,'__ApplyAttribute'),('constant','WireFunctionStatements')), ((15,'__ApplyAttribute'),('constant','GlobalComponentInstanceDeclaration')), ((22,'__ApplyAttribute'),('constant','RequiredPort_port')), ((23,'__ApplyAttribute'),('constant','GlobalComponentInstanceDeclaration')), ((30,'__ApplyAttribute'),('constant','RequiredPort_ops')), ((33,'__ApplyAttribute'),('constant','GlobalVarOps')), ]

        
