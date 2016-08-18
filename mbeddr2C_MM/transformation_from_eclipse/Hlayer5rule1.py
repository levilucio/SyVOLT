from core.himesis import Himesis
import uuid

class Hlayer5rule1(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule layer5rule1.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer5rule1, self).__init__(name='Hlayer5rule1', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """layer5rule1"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
 
        
        # match class ComponentInstance(layer5rule1class0) node
        self.add_node()

        self.vs[3]["mm__"] = """ComponentInstance""" 
        self.vs[3]["attr1"] = """+""" 
        # match_contains node for class ComponentInstance(layer5rule1class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        # match class AtomicComponent(layer5rule1class1) node
        self.add_node()

        self.vs[5]["mm__"] = """AtomicComponent""" 
        self.vs[5]["attr1"] = """+""" 
        # match_contains node for class AtomicComponent(layer5rule1class1)
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        # match class RequiredPort(layer5rule1class2) node
        self.add_node()

        self.vs[7]["mm__"] = """RequiredPort""" 
        self.vs[7]["attr1"] = """+""" 
        # match_contains node for class RequiredPort(layer5rule1class2)
        self.add_node()
        self.vs[8]["mm__"] = """match_contains"""
        # match class InstanceConfiguration(layer5rule1class3) node
        self.add_node()

        self.vs[9]["mm__"] = """InstanceConfiguration""" 
        self.vs[9]["attr1"] = """+""" 
        # match_contains node for class InstanceConfiguration(layer5rule1class3)
        self.add_node()
        self.vs[10]["mm__"] = """match_contains"""
        # match class AssemblyConnector(layer5rule1class4) node
        self.add_node()

        self.vs[11]["mm__"] = """AssemblyConnector""" 
        self.vs[11]["attr1"] = """+""" 
        # match_contains node for class AssemblyConnector(layer5rule1class4)
        self.add_node()
        self.vs[12]["mm__"] = """match_contains"""
        # match class InstancePortRef(layer5rule1class5) node
        self.add_node()

        self.vs[13]["mm__"] = """InstancePortRef""" 
        self.vs[13]["attr1"] = """+""" 
        # match_contains node for class InstancePortRef(layer5rule1class5)
        self.add_node()
        self.vs[14]["mm__"] = """match_contains"""
        # match class InstancePortRef(layer5rule1class6) node
        self.add_node()

        self.vs[15]["mm__"] = """InstancePortRef""" 
        self.vs[15]["attr1"] = """+""" 
        # match_contains node for class InstancePortRef(layer5rule1class6)
        self.add_node()
        self.vs[16]["mm__"] = """match_contains"""
        # match class ComponentInstance(layer5rule1class7) node
        self.add_node()

        self.vs[17]["mm__"] = """ComponentInstance""" 
        self.vs[17]["attr1"] = """+""" 
        # match_contains node for class ComponentInstance(layer5rule1class7)
        self.add_node()
        self.vs[18]["mm__"] = """match_contains"""
        # match class AtomicComponent(layer5rule1class8) node
        self.add_node()

        self.vs[19]["mm__"] = """AtomicComponent""" 
        self.vs[19]["attr1"] = """+""" 
        # match_contains node for class AtomicComponent(layer5rule1class8)
        self.add_node()
        self.vs[20]["mm__"] = """match_contains"""
        # match class ProvidedPort(layer5rule1class9) node
        self.add_node()

        self.vs[21]["mm__"] = """ProvidedPort""" 
        self.vs[21]["attr1"] = """+""" 
        # match_contains node for class ProvidedPort(layer5rule1class9)
        self.add_node()
        self.vs[22]["mm__"] = """match_contains"""
        # match class ClientServerInterface(layer5rule1class10) node
        self.add_node()

        self.vs[23]["mm__"] = """ClientServerInterface""" 
        self.vs[23]["attr1"] = """+""" 
        # match_contains node for class ClientServerInterface(layer5rule1class10)
        self.add_node()
        self.vs[24]["mm__"] = """match_contains"""
        
        
        # apply class StatementList(layer5rule1class11) node
        self.add_node()

        self.vs[25]["mm__"] = """StatementList""" 
        self.vs[25]["attr1"] = """1"""
        # apply_contains node for class StatementList(layer5rule1class11)
        self.add_node()
        self.vs[26]["mm__"] = """apply_contains"""
        # apply class GlobalVariableDeclaration(layer5rule1class12) node
        self.add_node()

        self.vs[27]["mm__"] = """GlobalVariableDeclaration""" 
        self.vs[27]["attr1"] = """1"""
        # apply_contains node for class GlobalVariableDeclaration(layer5rule1class12)
        self.add_node()
        self.vs[28]["mm__"] = """apply_contains"""
        # apply class ExpressionStatement(layer5rule1class13) node
        self.add_node()

        self.vs[29]["mm__"] = """ExpressionStatement""" 
        self.vs[29]["attr1"] = """1"""
        # apply_contains node for class ExpressionStatement(layer5rule1class13)
        self.add_node()
        self.vs[30]["mm__"] = """apply_contains"""
        # apply class AssignmentExpr(layer5rule1class14) node
        self.add_node()

        self.vs[31]["mm__"] = """AssignmentExpr""" 
        self.vs[31]["attr1"] = """1"""
        # apply_contains node for class AssignmentExpr(layer5rule1class14)
        self.add_node()
        self.vs[32]["mm__"] = """apply_contains"""
        # apply class GenericDotExpression(layer5rule1class15) node
        self.add_node()

        self.vs[33]["mm__"] = """GenericDotExpression""" 
        self.vs[33]["attr1"] = """1"""
        # apply_contains node for class GenericDotExpression(layer5rule1class15)
        self.add_node()
        self.vs[34]["mm__"] = """apply_contains"""
        # apply class ReferenceExpr(layer5rule1class16) node
        self.add_node()

        self.vs[35]["mm__"] = """ReferenceExpr""" 
        self.vs[35]["attr1"] = """1"""
        # apply_contains node for class ReferenceExpr(layer5rule1class16)
        self.add_node()
        self.vs[36]["mm__"] = """apply_contains"""
        # apply class GlobalVarRef(layer5rule1class17) node
        self.add_node()

        self.vs[37]["mm__"] = """GlobalVarRef""" 
        self.vs[37]["attr1"] = """1"""
        # apply_contains node for class GlobalVarRef(layer5rule1class17)
        self.add_node()
        self.vs[38]["mm__"] = """apply_contains"""
        # apply class GenericMemberRef(layer5rule1class18) node
        self.add_node()

        self.vs[39]["mm__"] = """GenericMemberRef""" 
        self.vs[39]["attr1"] = """1"""
        # apply_contains node for class GenericMemberRef(layer5rule1class18)
        self.add_node()
        self.vs[40]["mm__"] = """apply_contains"""
        # apply class Member(layer5rule1class19) node
        self.add_node()

        self.vs[41]["mm__"] = """Member""" 
        self.vs[41]["attr1"] = """1"""
        # apply_contains node for class Member(layer5rule1class19)
        self.add_node()
        self.vs[42]["mm__"] = """apply_contains"""
        # apply class GlobalVariableDeclaration(layer5rule1class20) node
        self.add_node()

        self.vs[43]["mm__"] = """GlobalVariableDeclaration""" 
        self.vs[43]["attr1"] = """1"""
        # apply_contains node for class GlobalVariableDeclaration(layer5rule1class20)
        self.add_node()
        self.vs[44]["mm__"] = """apply_contains"""
        # apply class GlobalVarRef(layer5rule1class21) node
        self.add_node()

        self.vs[45]["mm__"] = """GlobalVarRef""" 
        self.vs[45]["attr1"] = """1"""
        # apply_contains node for class GlobalVarRef(layer5rule1class21)
        self.add_node()
        self.vs[46]["mm__"] = """apply_contains"""
        # apply class ExpressionStatement(layer5rule1class22) node
        self.add_node()

        self.vs[47]["mm__"] = """ExpressionStatement""" 
        self.vs[47]["attr1"] = """1"""
        # apply_contains node for class ExpressionStatement(layer5rule1class22)
        self.add_node()
        self.vs[48]["mm__"] = """apply_contains"""
        # apply class AssignmentExpr(layer5rule1class23) node
        self.add_node()

        self.vs[49]["mm__"] = """AssignmentExpr""" 
        self.vs[49]["attr1"] = """1"""
        # apply_contains node for class AssignmentExpr(layer5rule1class23)
        self.add_node()
        self.vs[50]["mm__"] = """apply_contains"""
        # apply class GenericDotExpression(layer5rule1class24) node
        self.add_node()

        self.vs[51]["mm__"] = """GenericDotExpression""" 
        self.vs[51]["attr1"] = """1"""
        # apply_contains node for class GenericDotExpression(layer5rule1class24)
        self.add_node()
        self.vs[52]["mm__"] = """apply_contains"""
        # apply class GlobalVarRef(layer5rule1class25) node
        self.add_node()

        self.vs[53]["mm__"] = """GlobalVarRef""" 
        self.vs[53]["attr1"] = """1"""
        # apply_contains node for class GlobalVarRef(layer5rule1class25)
        self.add_node()
        self.vs[54]["mm__"] = """apply_contains"""
        # apply class GenericMemberRef(layer5rule1class26) node
        self.add_node()

        self.vs[55]["mm__"] = """GenericMemberRef""" 
        self.vs[55]["attr1"] = """1"""
        # apply_contains node for class GenericMemberRef(layer5rule1class26)
        self.add_node()
        self.vs[56]["mm__"] = """apply_contains"""
        # apply class Member(layer5rule1class27) node
        self.add_node()

        self.vs[57]["mm__"] = """Member""" 
        self.vs[57]["attr1"] = """1"""
        # apply_contains node for class Member(layer5rule1class27)
        self.add_node()
        self.vs[58]["mm__"] = """apply_contains"""
        # apply class ReferenceExpr(layer5rule1class28) node
        self.add_node()

        self.vs[59]["mm__"] = """ReferenceExpr""" 
        self.vs[59]["attr1"] = """1"""
        # apply_contains node for class ReferenceExpr(layer5rule1class28)
        self.add_node()
        self.vs[60]["mm__"] = """apply_contains"""
        # apply class GlobalVarRef(layer5rule1class29) node
        self.add_node()

        self.vs[61]["mm__"] = """GlobalVarRef""" 
        self.vs[61]["attr1"] = """1"""
        # apply_contains node for class GlobalVarRef(layer5rule1class29)
        self.add_node()
        self.vs[62]["mm__"] = """apply_contains"""
        # apply class GlobalVariableDeclaration(layer5rule1class30) node
        self.add_node()

        self.vs[63]["mm__"] = """GlobalVariableDeclaration""" 
        self.vs[63]["attr1"] = """1"""
        # apply_contains node for class GlobalVariableDeclaration(layer5rule1class30)
        self.add_node()
        self.vs[64]["mm__"] = """apply_contains"""
        
        
        # match association ComponentInstance--component-->AtomicComponent node
        self.add_node()
        self.vs[65]["attr1"] = """component"""
        self.vs[65]["mm__"] = """directLink_S"""
        # match association AtomicComponent--contents-->RequiredPort node
        self.add_node()
        self.vs[66]["attr1"] = """contents"""
        self.vs[66]["mm__"] = """directLink_S"""
        # match association InstanceConfiguration--contents-->ComponentInstance node
        self.add_node()
        self.vs[67]["attr1"] = """contents"""
        self.vs[67]["mm__"] = """directLink_S"""
        # match association InstanceConfiguration--contents-->AssemblyConnector node
        self.add_node()
        self.vs[68]["attr1"] = """contents"""
        self.vs[68]["mm__"] = """directLink_S"""
        # match association AssemblyConnector--source-->InstancePortRef node
        self.add_node()
        self.vs[69]["attr1"] = """source"""
        self.vs[69]["mm__"] = """directLink_S"""
        # match association InstancePortRef--instance-->ComponentInstance node
        self.add_node()
        self.vs[70]["attr1"] = """instance"""
        self.vs[70]["mm__"] = """directLink_S"""
        # match association InstancePortRef--port-->RequiredPort node
        self.add_node()
        self.vs[71]["attr1"] = """port"""
        self.vs[71]["mm__"] = """directLink_S"""
        # match association InstanceConfiguration--contents-->ComponentInstance node
        self.add_node()
        self.vs[72]["attr1"] = """contents"""
        self.vs[72]["mm__"] = """directLink_S"""
        # match association InstancePortRef--instance-->ComponentInstance node
        self.add_node()
        self.vs[73]["attr1"] = """instance"""
        self.vs[73]["mm__"] = """directLink_S"""
        # match association AssemblyConnector--target-->InstancePortRef node
        self.add_node()
        self.vs[74]["attr1"] = """target"""
        self.vs[74]["mm__"] = """directLink_S"""
        # match association ComponentInstance--component-->AtomicComponent node
        self.add_node()
        self.vs[75]["attr1"] = """component"""
        self.vs[75]["mm__"] = """directLink_S"""
        # match association AtomicComponent--contents-->ProvidedPort node
        self.add_node()
        self.vs[76]["attr1"] = """contents"""
        self.vs[76]["mm__"] = """directLink_S"""
        # match association ProvidedPort--intf-->ClientServerInterface node
        self.add_node()
        self.vs[77]["attr1"] = """intf"""
        self.vs[77]["mm__"] = """directLink_S"""
        # match association RequiredPort--intf-->ClientServerInterface node
        self.add_node()
        self.vs[78]["attr1"] = """intf"""
        self.vs[78]["mm__"] = """directLink_S"""
        
        # apply association StatementList--statements-->ExpressionStatement node
        self.add_node()
        self.vs[79]["attr1"] = """statements"""
        self.vs[79]["mm__"] = """directLink_T"""
        # apply association ExpressionStatement--expr-->AssignmentExpr node
        self.add_node()
        self.vs[80]["attr1"] = """expr"""
        self.vs[80]["mm__"] = """directLink_T"""
        # apply association AssignmentExpr--left-->GenericDotExpression node
        self.add_node()
        self.vs[81]["attr1"] = """left"""
        self.vs[81]["mm__"] = """directLink_T"""
        # apply association AssignmentExpr--right-->ReferenceExpr node
        self.add_node()
        self.vs[82]["attr1"] = """right"""
        self.vs[82]["mm__"] = """directLink_T"""
        # apply association GenericDotExpression--expression-->GlobalVarRef node
        self.add_node()
        self.vs[83]["attr1"] = """expression"""
        self.vs[83]["mm__"] = """directLink_T"""
        # apply association GenericDotExpression--target-->GenericMemberRef node
        self.add_node()
        self.vs[84]["attr1"] = """target"""
        self.vs[84]["mm__"] = """directLink_T"""
        # apply association GlobalVarRef--var-->GlobalVariableDeclaration node
        self.add_node()
        self.vs[85]["attr1"] = """var"""
        self.vs[85]["mm__"] = """directLink_T"""
        # apply association GenericMemberRef--member-->Member node
        self.add_node()
        self.vs[86]["attr1"] = """member"""
        self.vs[86]["mm__"] = """directLink_T"""
        # apply association ReferenceExpr--expression-->GlobalVarRef node
        self.add_node()
        self.vs[87]["attr1"] = """expression"""
        self.vs[87]["mm__"] = """directLink_T"""
        # apply association GlobalVarRef--var-->GlobalVariableDeclaration node
        self.add_node()
        self.vs[88]["attr1"] = """var"""
        self.vs[88]["mm__"] = """directLink_T"""
        # apply association StatementList--statements-->ExpressionStatement node
        self.add_node()
        self.vs[89]["attr1"] = """statements"""
        self.vs[89]["mm__"] = """directLink_T"""
        # apply association ExpressionStatement--expr-->AssignmentExpr node
        self.add_node()
        self.vs[90]["attr1"] = """expr"""
        self.vs[90]["mm__"] = """directLink_T"""
        # apply association AssignmentExpr--left-->GenericDotExpression node
        self.add_node()
        self.vs[91]["attr1"] = """left"""
        self.vs[91]["mm__"] = """directLink_T"""
        # apply association GenericDotExpression--expression-->GlobalVarRef node
        self.add_node()
        self.vs[92]["attr1"] = """expression"""
        self.vs[92]["mm__"] = """directLink_T"""
        # apply association GlobalVarRef--var-->GlobalVariableDeclaration node
        self.add_node()
        self.vs[93]["attr1"] = """var"""
        self.vs[93]["mm__"] = """directLink_T"""
        # apply association GenericDotExpression--target-->GenericMemberRef node
        self.add_node()
        self.vs[94]["attr1"] = """target"""
        self.vs[94]["mm__"] = """directLink_T"""
        # apply association GenericMemberRef--member-->Member node
        self.add_node()
        self.vs[95]["attr1"] = """member"""
        self.vs[95]["mm__"] = """directLink_T"""
        # apply association AssignmentExpr--right-->ReferenceExpr node
        self.add_node()
        self.vs[96]["attr1"] = """right"""
        self.vs[96]["mm__"] = """directLink_T"""
        # apply association ReferenceExpr--expression-->GlobalVarRef node
        self.add_node()
        self.vs[97]["attr1"] = """expression"""
        self.vs[97]["mm__"] = """directLink_T"""
        # apply association GlobalVarRef--var-->GlobalVariableDeclaration node
        self.add_node()
        self.vs[98]["attr1"] = """var"""
        self.vs[98]["mm__"] = """directLink_T"""
        
        # backward association ComponentInstance---->StatementList node
        self.add_node()

        self.vs[99]["mm__"] = """backward_link"""
        # backward association ComponentInstance---->GlobalVariableDeclaration node
        self.add_node()

        self.vs[100]["mm__"] = """backward_link"""
        # backward association RequiredPort---->Member node
        self.add_node()

        self.vs[101]["mm__"] = """backward_link"""
        # backward association ComponentInstance---->GlobalVariableDeclaration node
        self.add_node()

        self.vs[102]["mm__"] = """backward_link"""
        # backward association RequiredPort---->Member node
        self.add_node()

        self.vs[103]["mm__"] = """backward_link"""
        # backward association ProvidedPort---->GlobalVariableDeclaration node
        self.add_node()

        self.vs[104]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class ComponentInstance(layer5rule1class0)
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class AtomicComponent(layer5rule1class1)
                (0,8), # matchmodel -> match_contains
                (8,7), # match_contains -> match_class RequiredPort(layer5rule1class2)
                (0,10), # matchmodel -> match_contains
                (10,9), # match_contains -> match_class InstanceConfiguration(layer5rule1class3)
                (0,12), # matchmodel -> match_contains
                (12,11), # match_contains -> match_class AssemblyConnector(layer5rule1class4)
                (0,14), # matchmodel -> match_contains
                (14,13), # match_contains -> match_class InstancePortRef(layer5rule1class5)
                (0,16), # matchmodel -> match_contains
                (16,15), # match_contains -> match_class InstancePortRef(layer5rule1class6)
                (0,18), # matchmodel -> match_contains
                (18,17), # match_contains -> match_class ComponentInstance(layer5rule1class7)
                (0,20), # matchmodel -> match_contains
                (20,19), # match_contains -> match_class AtomicComponent(layer5rule1class8)
                (0,22), # matchmodel -> match_contains
                (22,21), # match_contains -> match_class ProvidedPort(layer5rule1class9)
                (0,24), # matchmodel -> match_contains
                (24,23), # match_contains -> match_class ClientServerInterface(layer5rule1class10)
                (1,26), # applymodel -> apply_contains
                (26,25), # apply_contains -> apply_class StatementList(layer5rule1class11)
                (1,28), # applymodel -> apply_contains
                (28,27), # apply_contains -> apply_class GlobalVariableDeclaration(layer5rule1class12)
                (1,30), # applymodel -> apply_contains
                (30,29), # apply_contains -> apply_class ExpressionStatement(layer5rule1class13)
                (1,32), # applymodel -> apply_contains
                (32,31), # apply_contains -> apply_class AssignmentExpr(layer5rule1class14)
                (1,34), # applymodel -> apply_contains
                (34,33), # apply_contains -> apply_class GenericDotExpression(layer5rule1class15)
                (1,36), # applymodel -> apply_contains
                (36,35), # apply_contains -> apply_class ReferenceExpr(layer5rule1class16)
                (1,38), # applymodel -> apply_contains
                (38,37), # apply_contains -> apply_class GlobalVarRef(layer5rule1class17)
                (1,40), # applymodel -> apply_contains
                (40,39), # apply_contains -> apply_class GenericMemberRef(layer5rule1class18)
                (1,42), # applymodel -> apply_contains
                (42,41), # apply_contains -> apply_class Member(layer5rule1class19)
                (1,44), # applymodel -> apply_contains
                (44,43), # apply_contains -> apply_class GlobalVariableDeclaration(layer5rule1class20)
                (1,46), # applymodel -> apply_contains
                (46,45), # apply_contains -> apply_class GlobalVarRef(layer5rule1class21)
                (1,48), # applymodel -> apply_contains
                (48,47), # apply_contains -> apply_class ExpressionStatement(layer5rule1class22)
                (1,50), # applymodel -> apply_contains
                (50,49), # apply_contains -> apply_class AssignmentExpr(layer5rule1class23)
                (1,52), # applymodel -> apply_contains
                (52,51), # apply_contains -> apply_class GenericDotExpression(layer5rule1class24)
                (1,54), # applymodel -> apply_contains
                (54,53), # apply_contains -> apply_class GlobalVarRef(layer5rule1class25)
                (1,56), # applymodel -> apply_contains
                (56,55), # apply_contains -> apply_class GenericMemberRef(layer5rule1class26)
                (1,58), # applymodel -> apply_contains
                (58,57), # apply_contains -> apply_class Member(layer5rule1class27)
                (1,60), # applymodel -> apply_contains
                (60,59), # apply_contains -> apply_class ReferenceExpr(layer5rule1class28)
                (1,62), # applymodel -> apply_contains
                (62,61), # apply_contains -> apply_class GlobalVarRef(layer5rule1class29)
                (1,64), # applymodel -> apply_contains
                (64,63), # apply_contains -> apply_class GlobalVariableDeclaration(layer5rule1class30)
                (3,65), # match_class ComponentInstance(layer5rule1class0) -> association component
                (65,5), # association component  -> match_class AtomicComponent(layer5rule1class1)
                (5,66), # match_class AtomicComponent(layer5rule1class1) -> association contents
                (66,7), # association contents  -> match_class RequiredPort(layer5rule1class2)
                (9,67), # match_class InstanceConfiguration(layer5rule1class3) -> association contents
                (67,3), # association contents  -> match_class ComponentInstance(layer5rule1class0)
                (9,68), # match_class InstanceConfiguration(layer5rule1class3) -> association contents
                (68,11), # association contents  -> match_class AssemblyConnector(layer5rule1class4)
                (11,69), # match_class AssemblyConnector(layer5rule1class4) -> association source
                (69,13), # association source  -> match_class InstancePortRef(layer5rule1class5)
                (13,70), # match_class InstancePortRef(layer5rule1class5) -> association instance
                (70,3), # association instance  -> match_class ComponentInstance(layer5rule1class0)
                (13,71), # match_class InstancePortRef(layer5rule1class5) -> association port
                (71,7), # association port  -> match_class RequiredPort(layer5rule1class2)
                (9,72), # match_class InstanceConfiguration(layer5rule1class3) -> association contents
                (72,17), # association contents  -> match_class ComponentInstance(layer5rule1class7)
                (15,73), # match_class InstancePortRef(layer5rule1class6) -> association instance
                (73,17), # association instance  -> match_class ComponentInstance(layer5rule1class7)
                (11,74), # match_class AssemblyConnector(layer5rule1class4) -> association target
                (74,15), # association target  -> match_class InstancePortRef(layer5rule1class6)
                (17,75), # match_class ComponentInstance(layer5rule1class7) -> association component
                (75,19), # association component  -> match_class AtomicComponent(layer5rule1class8)
                (19,76), # match_class AtomicComponent(layer5rule1class8) -> association contents
                (76,21), # association contents  -> match_class ProvidedPort(layer5rule1class9)
                (21,77), # match_class ProvidedPort(layer5rule1class9) -> association intf
                (77,23), # association intf  -> match_class ClientServerInterface(layer5rule1class10)
                (7,78), # match_class RequiredPort(layer5rule1class2) -> association intf
                (78,23), # association intf  -> match_class ClientServerInterface(layer5rule1class10)
                (25,79), # apply_class StatementList(layer5rule1class11) -> association statements
                (79,29), # association statements  -> apply_class ExpressionStatement(layer5rule1class13)
                (29,80), # apply_class ExpressionStatement(layer5rule1class13) -> association expr
                (80,31), # association expr  -> apply_class AssignmentExpr(layer5rule1class14)
                (31,81), # apply_class AssignmentExpr(layer5rule1class14) -> association left
                (81,33), # association left  -> apply_class GenericDotExpression(layer5rule1class15)
                (31,82), # apply_class AssignmentExpr(layer5rule1class14) -> association right
                (82,35), # association right  -> apply_class ReferenceExpr(layer5rule1class16)
                (33,83), # apply_class GenericDotExpression(layer5rule1class15) -> association expression
                (83,37), # association expression  -> apply_class GlobalVarRef(layer5rule1class17)
                (33,84), # apply_class GenericDotExpression(layer5rule1class15) -> association target
                (84,39), # association target  -> apply_class GenericMemberRef(layer5rule1class18)
                (37,85), # apply_class GlobalVarRef(layer5rule1class17) -> association var
                (85,27), # association var  -> apply_class GlobalVariableDeclaration(layer5rule1class12)
                (39,86), # apply_class GenericMemberRef(layer5rule1class18) -> association member
                (86,41), # association member  -> apply_class Member(layer5rule1class19)
                (35,87), # apply_class ReferenceExpr(layer5rule1class16) -> association expression
                (87,45), # association expression  -> apply_class GlobalVarRef(layer5rule1class21)
                (45,88), # apply_class GlobalVarRef(layer5rule1class21) -> association var
                (88,43), # association var  -> apply_class GlobalVariableDeclaration(layer5rule1class20)
                (25,89), # apply_class StatementList(layer5rule1class11) -> association statements
                (89,47), # association statements  -> apply_class ExpressionStatement(layer5rule1class22)
                (47,90), # apply_class ExpressionStatement(layer5rule1class22) -> association expr
                (90,49), # association expr  -> apply_class AssignmentExpr(layer5rule1class23)
                (49,91), # apply_class AssignmentExpr(layer5rule1class23) -> association left
                (91,51), # association left  -> apply_class GenericDotExpression(layer5rule1class24)
                (51,92), # apply_class GenericDotExpression(layer5rule1class24) -> association expression
                (92,53), # association expression  -> apply_class GlobalVarRef(layer5rule1class25)
                (53,93), # apply_class GlobalVarRef(layer5rule1class25) -> association var
                (93,27), # association var  -> apply_class GlobalVariableDeclaration(layer5rule1class12)
                (51,94), # apply_class GenericDotExpression(layer5rule1class24) -> association target
                (94,55), # association target  -> apply_class GenericMemberRef(layer5rule1class26)
                (55,95), # apply_class GenericMemberRef(layer5rule1class26) -> association member
                (95,57), # association member  -> apply_class Member(layer5rule1class27)
                (49,96), # apply_class AssignmentExpr(layer5rule1class23) -> association right
                (96,59), # association right  -> apply_class ReferenceExpr(layer5rule1class28)
                (59,97), # apply_class ReferenceExpr(layer5rule1class28) -> association expression
                (97,61), # association expression  -> apply_class GlobalVarRef(layer5rule1class29)
                (61,98), # apply_class GlobalVarRef(layer5rule1class29) -> association var
                (98,63), # association var  -> apply_class GlobalVariableDeclaration(layer5rule1class30)
                (25,99), # apply_class StatementList(layer5rule1class11) -> backward_association
                (99,3), #  backward_association -> apply_class ComponentInstance(layer5rule1class0)
                (27,100), # apply_class GlobalVariableDeclaration(layer5rule1class12) -> backward_association
                (100,3), #  backward_association -> apply_class ComponentInstance(layer5rule1class0)
                (41,101), # apply_class Member(layer5rule1class19) -> backward_association
                (101,7), #  backward_association -> apply_class RequiredPort(layer5rule1class2)
                (43,102), # apply_class GlobalVariableDeclaration(layer5rule1class20) -> backward_association
                (102,17), #  backward_association -> apply_class ComponentInstance(layer5rule1class7)
                (57,103), # apply_class Member(layer5rule1class27) -> backward_association
                (103,7), #  backward_association -> apply_class RequiredPort(layer5rule1class2)
                (63,104), # apply_class GlobalVariableDeclaration(layer5rule1class30) -> backward_association
                (104,21), #  backward_association -> apply_class ProvidedPort(layer5rule1class9)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((25,'__ApplyAttribute'),('constant','WireFunctionStatements')), ((27,'__ApplyAttribute'),('constant','GlobalComponentInstanceDeclaration')), ((41,'__ApplyAttribute'),('constant','RequiredPort_port')), ((43,'__ApplyAttribute'),('constant','GlobalComponentInstanceDeclaration')), ((57,'__ApplyAttribute'),('constant','RequiredPort_ops')), ((63,'__ApplyAttribute'),('constant','GlobalVarOps')), ]

        
