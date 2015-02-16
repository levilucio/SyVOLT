from core.himesis import Himesis
import cPickle as pickle
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
        # TODO Levi, need some help here because I don't know where does 
        # this value come from.
        self["mm__"] = pickle.loads("""(lp1
S'HimesisMM'
p2
a.""")
        
        self["name"] = """layer5rule1"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1matchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1applymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1pairedwith2')
        
    	# match class ComponentInstance(layer5rule1class0) node
    	self.add_node()
    	self.vs[3]["name"] = """layer5rule1class0"""
        self.vs[3]["classtype"] = """ComponentInstance"""
        self.vs[3]["mm__"] = """ComponentInstance"""
        self.vs[3]["cardinality"] = """+"""
        #self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class0')
    	# match_contains node for class ComponentInstance(layer5rule1class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        #self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class0matchcontains4')
    	# match class AtomicComponent(layer5rule1class1) node
    	self.add_node()
    	self.vs[5]["name"] = """layer5rule1class1"""
        self.vs[5]["classtype"] = """AtomicComponent"""
        self.vs[5]["mm__"] = """AtomicComponent"""
        self.vs[5]["cardinality"] = """+"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class1')
    	# match_contains node for class AtomicComponent(layer5rule1class1)
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        #self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class1matchcontains6')
    	# match class RequiredPort(layer5rule1class2) node
    	self.add_node()
    	self.vs[7]["name"] = """layer5rule1class2"""
        self.vs[7]["classtype"] = """RequiredPort"""
        self.vs[7]["mm__"] = """RequiredPort"""
        self.vs[7]["cardinality"] = """+"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class2')
    	# match_contains node for class RequiredPort(layer5rule1class2)
        self.add_node()
        self.vs[8]["mm__"] = """match_contains"""
        #self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class2matchcontains8')
    	# match class InstanceConfiguration(layer5rule1class3) node
    	self.add_node()
    	self.vs[9]["name"] = """layer5rule1class3"""
        self.vs[9]["classtype"] = """InstanceConfiguration"""
        self.vs[9]["mm__"] = """InstanceConfiguration"""
        self.vs[9]["cardinality"] = """+"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class3')
    	# match_contains node for class InstanceConfiguration(layer5rule1class3)
        self.add_node()
        self.vs[10]["mm__"] = """match_contains"""
        #self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class3matchcontains10')
    	# match class AssemblyConnector(layer5rule1class4) node
    	self.add_node()
    	self.vs[11]["name"] = """layer5rule1class4"""
        self.vs[11]["classtype"] = """AssemblyConnector"""
        self.vs[11]["mm__"] = """AssemblyConnector"""
        self.vs[11]["cardinality"] = """+"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class4')
    	# match_contains node for class AssemblyConnector(layer5rule1class4)
        self.add_node()
        self.vs[12]["mm__"] = """match_contains"""
        #self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class4matchcontains12')
    	# match class InstancePortRef(layer5rule1class5) node
    	self.add_node()
    	self.vs[13]["name"] = """layer5rule1class5"""
        self.vs[13]["classtype"] = """InstancePortRef"""
        self.vs[13]["mm__"] = """InstancePortRef"""
        self.vs[13]["cardinality"] = """+"""
        #self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class5')
    	# match_contains node for class InstancePortRef(layer5rule1class5)
        self.add_node()
        self.vs[14]["mm__"] = """match_contains"""
        #self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class5matchcontains14')
    	# match class InstancePortRef(layer5rule1class6) node
    	self.add_node()
    	self.vs[15]["name"] = """layer5rule1class6"""
        self.vs[15]["classtype"] = """InstancePortRef"""
        self.vs[15]["mm__"] = """InstancePortRef"""
        self.vs[15]["cardinality"] = """+"""
        #self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class6')
    	# match_contains node for class InstancePortRef(layer5rule1class6)
        self.add_node()
        self.vs[16]["mm__"] = """match_contains"""
        #self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class6matchcontains16')
    	# match class ComponentInstance(layer5rule1class7) node
    	self.add_node()
    	self.vs[17]["name"] = """layer5rule1class7"""
        self.vs[17]["classtype"] = """ComponentInstance"""
        self.vs[17]["mm__"] = """ComponentInstance"""
        self.vs[17]["cardinality"] = """+"""
        #self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class7')
    	# match_contains node for class ComponentInstance(layer5rule1class7)
        self.add_node()
        self.vs[18]["mm__"] = """match_contains"""
        #self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class7matchcontains18')
    	# match class AtomicComponent(layer5rule1class8) node
    	self.add_node()
    	self.vs[19]["name"] = """layer5rule1class8"""
        self.vs[19]["classtype"] = """AtomicComponent"""
        self.vs[19]["mm__"] = """AtomicComponent"""
        self.vs[19]["cardinality"] = """+"""
        #self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class8')
    	# match_contains node for class AtomicComponent(layer5rule1class8)
        self.add_node()
        self.vs[20]["mm__"] = """match_contains"""
        #self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class8matchcontains20')
    	# match class ProvidedPort(layer5rule1class9) node
    	self.add_node()
    	self.vs[21]["name"] = """layer5rule1class9"""
        self.vs[21]["classtype"] = """ProvidedPort"""
        self.vs[21]["mm__"] = """ProvidedPort"""
        self.vs[21]["cardinality"] = """+"""
        #self.vs[21]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class9')
    	# match_contains node for class ProvidedPort(layer5rule1class9)
        self.add_node()
        self.vs[22]["mm__"] = """match_contains"""
        #self.vs[22]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class9matchcontains22')
    	# match class ClientServerInterface(layer5rule1class10) node
    	self.add_node()
    	self.vs[23]["name"] = """layer5rule1class10"""
        self.vs[23]["classtype"] = """ClientServerInterface"""
        self.vs[23]["mm__"] = """ClientServerInterface"""
        self.vs[23]["cardinality"] = """+"""
        #self.vs[23]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class10')
    	# match_contains node for class ClientServerInterface(layer5rule1class10)
        self.add_node()
        self.vs[24]["mm__"] = """match_contains"""
        #self.vs[24]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class10matchcontains24')
        
        
    	# apply class StatementList(layer5rule1class11) node
    	self.add_node()
    	self.vs[25]["name"] = """layer5rule1class11"""
        self.vs[25]["classtype"] = """StatementList"""
        self.vs[25]["mm__"] = """StatementList"""
        self.vs[25]["cardinality"] = """1"""
        #self.vs[25]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class11')
    	# apply_contains node for class StatementList(layer5rule1class11)
        self.add_node()
        self.vs[26]["mm__"] = """apply_contains"""
        #self.vs[26]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class11applycontains26')
    	# apply class GlobalVariableDeclaration(layer5rule1class12) node
    	self.add_node()
    	self.vs[27]["name"] = """layer5rule1class12"""
        self.vs[27]["classtype"] = """GlobalVariableDeclaration"""
        self.vs[27]["mm__"] = """GlobalVariableDeclaration"""
        self.vs[27]["cardinality"] = """1"""
        #self.vs[27]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class12')
    	# apply_contains node for class GlobalVariableDeclaration(layer5rule1class12)
        self.add_node()
        self.vs[28]["mm__"] = """apply_contains"""
        #self.vs[28]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class12applycontains28')
    	# apply class ExpressionStatement(layer5rule1class13) node
    	self.add_node()
    	self.vs[29]["name"] = """layer5rule1class13"""
        self.vs[29]["classtype"] = """ExpressionStatement"""
        self.vs[29]["mm__"] = """ExpressionStatement"""
        self.vs[29]["cardinality"] = """1"""
        #self.vs[29]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class13')
    	# apply_contains node for class ExpressionStatement(layer5rule1class13)
        self.add_node()
        self.vs[30]["mm__"] = """apply_contains"""
        #self.vs[30]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class13applycontains30')
    	# apply class AssignmentExpr(layer5rule1class14) node
    	self.add_node()
    	self.vs[31]["name"] = """layer5rule1class14"""
        self.vs[31]["classtype"] = """AssignmentExpr"""
        self.vs[31]["mm__"] = """AssignmentExpr"""
        self.vs[31]["cardinality"] = """1"""
        #self.vs[31]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class14')
    	# apply_contains node for class AssignmentExpr(layer5rule1class14)
        self.add_node()
        self.vs[32]["mm__"] = """apply_contains"""
        #self.vs[32]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class14applycontains32')
    	# apply class GenericDotExpression(layer5rule1class15) node
    	self.add_node()
    	self.vs[33]["name"] = """layer5rule1class15"""
        self.vs[33]["classtype"] = """GenericDotExpression"""
        self.vs[33]["mm__"] = """GenericDotExpression"""
        self.vs[33]["cardinality"] = """1"""
        #self.vs[33]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class15')
    	# apply_contains node for class GenericDotExpression(layer5rule1class15)
        self.add_node()
        self.vs[34]["mm__"] = """apply_contains"""
        #self.vs[34]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class15applycontains34')
    	# apply class ReferenceExpr(layer5rule1class16) node
    	self.add_node()
    	self.vs[35]["name"] = """layer5rule1class16"""
        self.vs[35]["classtype"] = """ReferenceExpr"""
        self.vs[35]["mm__"] = """ReferenceExpr"""
        self.vs[35]["cardinality"] = """1"""
        #self.vs[35]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class16')
    	# apply_contains node for class ReferenceExpr(layer5rule1class16)
        self.add_node()
        self.vs[36]["mm__"] = """apply_contains"""
        #self.vs[36]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class16applycontains36')
    	# apply class GlobalVarRef(layer5rule1class17) node
    	self.add_node()
    	self.vs[37]["name"] = """layer5rule1class17"""
        self.vs[37]["classtype"] = """GlobalVarRef"""
        self.vs[37]["mm__"] = """GlobalVarRef"""
        self.vs[37]["cardinality"] = """1"""
        #self.vs[37]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class17')
    	# apply_contains node for class GlobalVarRef(layer5rule1class17)
        self.add_node()
        self.vs[38]["mm__"] = """apply_contains"""
        #self.vs[38]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class17applycontains38')
    	# apply class GenericMemberRef(layer5rule1class18) node
    	self.add_node()
    	self.vs[39]["name"] = """layer5rule1class18"""
        self.vs[39]["classtype"] = """GenericMemberRef"""
        self.vs[39]["mm__"] = """GenericMemberRef"""
        self.vs[39]["cardinality"] = """1"""
        #self.vs[39]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class18')
    	# apply_contains node for class GenericMemberRef(layer5rule1class18)
        self.add_node()
        self.vs[40]["mm__"] = """apply_contains"""
        #self.vs[40]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class18applycontains40')
    	# apply class Member(layer5rule1class19) node
    	self.add_node()
    	self.vs[41]["name"] = """layer5rule1class19"""
        self.vs[41]["classtype"] = """Member"""
        self.vs[41]["mm__"] = """Member"""
        self.vs[41]["cardinality"] = """1"""
        #self.vs[41]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class19')
    	# apply_contains node for class Member(layer5rule1class19)
        self.add_node()
        self.vs[42]["mm__"] = """apply_contains"""
        #self.vs[42]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class19applycontains42')
    	# apply class GlobalVariableDeclaration(layer5rule1class20) node
    	self.add_node()
    	self.vs[43]["name"] = """layer5rule1class20"""
        self.vs[43]["classtype"] = """GlobalVariableDeclaration"""
        self.vs[43]["mm__"] = """GlobalVariableDeclaration"""
        self.vs[43]["cardinality"] = """1"""
        #self.vs[43]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class20')
    	# apply_contains node for class GlobalVariableDeclaration(layer5rule1class20)
        self.add_node()
        self.vs[44]["mm__"] = """apply_contains"""
        #self.vs[44]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class20applycontains44')
    	# apply class GlobalVarRef(layer5rule1class21) node
    	self.add_node()
    	self.vs[45]["name"] = """layer5rule1class21"""
        self.vs[45]["classtype"] = """GlobalVarRef"""
        self.vs[45]["mm__"] = """GlobalVarRef"""
        self.vs[45]["cardinality"] = """1"""
        #self.vs[45]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class21')
    	# apply_contains node for class GlobalVarRef(layer5rule1class21)
        self.add_node()
        self.vs[46]["mm__"] = """apply_contains"""
        #self.vs[46]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class21applycontains46')
    	# apply class ExpressionStatement(layer5rule1class22) node
    	self.add_node()
    	self.vs[47]["name"] = """layer5rule1class22"""
        self.vs[47]["classtype"] = """ExpressionStatement"""
        self.vs[47]["mm__"] = """ExpressionStatement"""
        self.vs[47]["cardinality"] = """1"""
        #self.vs[47]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class22')
    	# apply_contains node for class ExpressionStatement(layer5rule1class22)
        self.add_node()
        self.vs[48]["mm__"] = """apply_contains"""
        #self.vs[48]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class22applycontains48')
    	# apply class AssignmentExpr(layer5rule1class23) node
    	self.add_node()
    	self.vs[49]["name"] = """layer5rule1class23"""
        self.vs[49]["classtype"] = """AssignmentExpr"""
        self.vs[49]["mm__"] = """AssignmentExpr"""
        self.vs[49]["cardinality"] = """1"""
        #self.vs[49]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class23')
    	# apply_contains node for class AssignmentExpr(layer5rule1class23)
        self.add_node()
        self.vs[50]["mm__"] = """apply_contains"""
        #self.vs[50]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class23applycontains50')
    	# apply class GenericDotExpression(layer5rule1class24) node
    	self.add_node()
    	self.vs[51]["name"] = """layer5rule1class24"""
        self.vs[51]["classtype"] = """GenericDotExpression"""
        self.vs[51]["mm__"] = """GenericDotExpression"""
        self.vs[51]["cardinality"] = """1"""
        #self.vs[51]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class24')
    	# apply_contains node for class GenericDotExpression(layer5rule1class24)
        self.add_node()
        self.vs[52]["mm__"] = """apply_contains"""
        #self.vs[52]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class24applycontains52')
    	# apply class GlobalVarRef(layer5rule1class25) node
    	self.add_node()
    	self.vs[53]["name"] = """layer5rule1class25"""
        self.vs[53]["classtype"] = """GlobalVarRef"""
        self.vs[53]["mm__"] = """GlobalVarRef"""
        self.vs[53]["cardinality"] = """1"""
        #self.vs[53]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class25')
    	# apply_contains node for class GlobalVarRef(layer5rule1class25)
        self.add_node()
        self.vs[54]["mm__"] = """apply_contains"""
        #self.vs[54]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class25applycontains54')
    	# apply class GenericMemberRef(layer5rule1class26) node
    	self.add_node()
    	self.vs[55]["name"] = """layer5rule1class26"""
        self.vs[55]["classtype"] = """GenericMemberRef"""
        self.vs[55]["mm__"] = """GenericMemberRef"""
        self.vs[55]["cardinality"] = """1"""
        #self.vs[55]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class26')
    	# apply_contains node for class GenericMemberRef(layer5rule1class26)
        self.add_node()
        self.vs[56]["mm__"] = """apply_contains"""
        #self.vs[56]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class26applycontains56')
    	# apply class Member(layer5rule1class27) node
    	self.add_node()
    	self.vs[57]["name"] = """layer5rule1class27"""
        self.vs[57]["classtype"] = """Member"""
        self.vs[57]["mm__"] = """Member"""
        self.vs[57]["cardinality"] = """1"""
        #self.vs[57]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class27')
    	# apply_contains node for class Member(layer5rule1class27)
        self.add_node()
        self.vs[58]["mm__"] = """apply_contains"""
        #self.vs[58]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class27applycontains58')
    	# apply class ReferenceExpr(layer5rule1class28) node
    	self.add_node()
    	self.vs[59]["name"] = """layer5rule1class28"""
        self.vs[59]["classtype"] = """ReferenceExpr"""
        self.vs[59]["mm__"] = """ReferenceExpr"""
        self.vs[59]["cardinality"] = """1"""
        #self.vs[59]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class28')
    	# apply_contains node for class ReferenceExpr(layer5rule1class28)
        self.add_node()
        self.vs[60]["mm__"] = """apply_contains"""
        #self.vs[60]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class28applycontains60')
    	# apply class GlobalVarRef(layer5rule1class29) node
    	self.add_node()
    	self.vs[61]["name"] = """layer5rule1class29"""
        self.vs[61]["classtype"] = """GlobalVarRef"""
        self.vs[61]["mm__"] = """GlobalVarRef"""
        self.vs[61]["cardinality"] = """1"""
        #self.vs[61]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class29')
    	# apply_contains node for class GlobalVarRef(layer5rule1class29)
        self.add_node()
        self.vs[62]["mm__"] = """apply_contains"""
        #self.vs[62]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class29applycontains62')
    	# apply class GlobalVariableDeclaration(layer5rule1class30) node
    	self.add_node()
    	self.vs[63]["name"] = """layer5rule1class30"""
        self.vs[63]["classtype"] = """GlobalVariableDeclaration"""
        self.vs[63]["mm__"] = """GlobalVariableDeclaration"""
        self.vs[63]["cardinality"] = """1"""
        #self.vs[63]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class30')
    	# apply_contains node for class GlobalVariableDeclaration(layer5rule1class30)
        self.add_node()
        self.vs[64]["mm__"] = """apply_contains"""
        #self.vs[64]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class30applycontains64')
        
        
    	# match association ComponentInstance--component-->AtomicComponent node
    	self.add_node()
    	self.vs[65]["associationType"] = """component"""
        self.vs[65]["mm__"] = """directLink_S"""
        #self.vs[65]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class0assoc65layer5rule1class1')
    	# match association AtomicComponent--contents-->RequiredPort node
    	self.add_node()
    	self.vs[66]["associationType"] = """contents"""
        self.vs[66]["mm__"] = """directLink_S"""
        #self.vs[66]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class1assoc66layer5rule1class2')
    	# match association InstanceConfiguration--contents-->ComponentInstance node
    	self.add_node()
    	self.vs[67]["associationType"] = """contents"""
        self.vs[67]["mm__"] = """directLink_S"""
        #self.vs[67]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class3assoc67layer5rule1class0')
    	# match association InstanceConfiguration--contents-->AssemblyConnector node
    	self.add_node()
    	self.vs[68]["associationType"] = """contents"""
        self.vs[68]["mm__"] = """directLink_S"""
        #self.vs[68]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class3assoc68layer5rule1class4')
    	# match association AssemblyConnector--source-->InstancePortRef node
    	self.add_node()
    	self.vs[69]["associationType"] = """source"""
        self.vs[69]["mm__"] = """directLink_S"""
        #self.vs[69]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class4assoc69layer5rule1class5')
    	# match association InstancePortRef--instance-->ComponentInstance node
    	self.add_node()
    	self.vs[70]["associationType"] = """instance"""
        self.vs[70]["mm__"] = """directLink_S"""
        #self.vs[70]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class5assoc70layer5rule1class0')
    	# match association InstancePortRef--port-->RequiredPort node
    	self.add_node()
    	self.vs[71]["associationType"] = """port"""
        self.vs[71]["mm__"] = """directLink_S"""
        #self.vs[71]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class5assoc71layer5rule1class2')
    	# match association InstanceConfiguration--contents-->ComponentInstance node
    	self.add_node()
    	self.vs[72]["associationType"] = """contents"""
        self.vs[72]["mm__"] = """directLink_S"""
        #self.vs[72]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class3assoc72layer5rule1class7')
    	# match association InstancePortRef--instance-->ComponentInstance node
    	self.add_node()
    	self.vs[73]["associationType"] = """instance"""
        self.vs[73]["mm__"] = """directLink_S"""
        #self.vs[73]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class6assoc73layer5rule1class7')
    	# match association AssemblyConnector--target-->InstancePortRef node
    	self.add_node()
    	self.vs[74]["associationType"] = """target"""
        self.vs[74]["mm__"] = """directLink_S"""
        #self.vs[74]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class4assoc74layer5rule1class6')
    	# match association ComponentInstance--component-->AtomicComponent node
    	self.add_node()
    	self.vs[75]["associationType"] = """component"""
        self.vs[75]["mm__"] = """directLink_S"""
        #self.vs[75]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class7assoc75layer5rule1class8')
    	# match association AtomicComponent--contents-->ProvidedPort node
    	self.add_node()
    	self.vs[76]["associationType"] = """contents"""
        self.vs[76]["mm__"] = """directLink_S"""
        #self.vs[76]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class8assoc76layer5rule1class9')
    	# match association ProvidedPort--intf-->ClientServerInterface node
    	self.add_node()
    	self.vs[77]["associationType"] = """intf"""
        self.vs[77]["mm__"] = """directLink_S"""
        #self.vs[77]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class9assoc77layer5rule1class10')
    	# match association RequiredPort--intf-->ClientServerInterface node
    	self.add_node()
    	self.vs[78]["associationType"] = """intf"""
        self.vs[78]["mm__"] = """directLink_S"""
        #self.vs[78]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class2assoc78layer5rule1class10')
        
    	# apply association StatementList--statements-->ExpressionStatement node
    	self.add_node()
    	self.vs[79]["associationType"] = """statements"""
        self.vs[79]["mm__"] = """directLink_T"""
        #self.vs[79]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class11assoc79layer5rule1class13')
    	# apply association ExpressionStatement--expr-->AssignmentExpr node
    	self.add_node()
    	self.vs[80]["associationType"] = """expr"""
        self.vs[80]["mm__"] = """directLink_T"""
        #self.vs[80]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class13assoc80layer5rule1class14')
    	# apply association AssignmentExpr--left-->GenericDotExpression node
    	self.add_node()
    	self.vs[81]["associationType"] = """left"""
        self.vs[81]["mm__"] = """directLink_T"""
        #self.vs[81]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class14assoc81layer5rule1class15')
    	# apply association AssignmentExpr--right-->ReferenceExpr node
    	self.add_node()
    	self.vs[82]["associationType"] = """right"""
        self.vs[82]["mm__"] = """directLink_T"""
        #self.vs[82]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class14assoc82layer5rule1class16')
    	# apply association GenericDotExpression--expression-->GlobalVarRef node
    	self.add_node()
    	self.vs[83]["associationType"] = """expression"""
        self.vs[83]["mm__"] = """directLink_T"""
        #self.vs[83]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class15assoc83layer5rule1class17')
    	# apply association GenericDotExpression--target-->GenericMemberRef node
    	self.add_node()
    	self.vs[84]["associationType"] = """target"""
        self.vs[84]["mm__"] = """directLink_T"""
        #self.vs[84]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class15assoc84layer5rule1class18')
    	# apply association GlobalVarRef--var-->GlobalVariableDeclaration node
    	self.add_node()
    	self.vs[85]["associationType"] = """var"""
        self.vs[85]["mm__"] = """directLink_T"""
        #self.vs[85]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class17assoc85layer5rule1class12')
    	# apply association GenericMemberRef--member-->Member node
    	self.add_node()
    	self.vs[86]["associationType"] = """member"""
        self.vs[86]["mm__"] = """directLink_T"""
        #self.vs[86]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class18assoc86layer5rule1class19')
    	# apply association ReferenceExpr--expression-->GlobalVarRef node
    	self.add_node()
    	self.vs[87]["associationType"] = """expression"""
        self.vs[87]["mm__"] = """directLink_T"""
        #self.vs[87]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class16assoc87layer5rule1class21')
    	# apply association GlobalVarRef--var-->GlobalVariableDeclaration node
    	self.add_node()
    	self.vs[88]["associationType"] = """var"""
        self.vs[88]["mm__"] = """directLink_T"""
        #self.vs[88]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class21assoc88layer5rule1class20')
    	# apply association StatementList--statements-->ExpressionStatement node
    	self.add_node()
    	self.vs[89]["associationType"] = """statements"""
        self.vs[89]["mm__"] = """directLink_T"""
        #self.vs[89]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class11assoc89layer5rule1class22')
    	# apply association ExpressionStatement--expr-->AssignmentExpr node
    	self.add_node()
    	self.vs[90]["associationType"] = """expr"""
        self.vs[90]["mm__"] = """directLink_T"""
        #self.vs[90]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class22assoc90layer5rule1class23')
    	# apply association AssignmentExpr--left-->GenericDotExpression node
    	self.add_node()
    	self.vs[91]["associationType"] = """left"""
        self.vs[91]["mm__"] = """directLink_T"""
        #self.vs[91]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class23assoc91layer5rule1class24')
    	# apply association GenericDotExpression--expression-->GlobalVarRef node
    	self.add_node()
    	self.vs[92]["associationType"] = """expression"""
        self.vs[92]["mm__"] = """directLink_T"""
        #self.vs[92]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class24assoc92layer5rule1class25')
    	# apply association GlobalVarRef--var-->GlobalVariableDeclaration node
    	self.add_node()
    	self.vs[93]["associationType"] = """var"""
        self.vs[93]["mm__"] = """directLink_T"""
        #self.vs[93]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class25assoc93layer5rule1class12')
    	# apply association GenericDotExpression--target-->GenericMemberRef node
    	self.add_node()
    	self.vs[94]["associationType"] = """target"""
        self.vs[94]["mm__"] = """directLink_T"""
        #self.vs[94]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class24assoc94layer5rule1class26')
    	# apply association GenericMemberRef--member-->Member node
    	self.add_node()
    	self.vs[95]["associationType"] = """member"""
        self.vs[95]["mm__"] = """directLink_T"""
        #self.vs[95]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class26assoc95layer5rule1class27')
    	# apply association AssignmentExpr--right-->ReferenceExpr node
    	self.add_node()
    	self.vs[96]["associationType"] = """right"""
        self.vs[96]["mm__"] = """directLink_T"""
        #self.vs[96]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class23assoc96layer5rule1class28')
    	# apply association ReferenceExpr--expression-->GlobalVarRef node
    	self.add_node()
    	self.vs[97]["associationType"] = """expression"""
        self.vs[97]["mm__"] = """directLink_T"""
        #self.vs[97]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class28assoc97layer5rule1class29')
    	# apply association GlobalVarRef--var-->GlobalVariableDeclaration node
    	self.add_node()
    	self.vs[98]["associationType"] = """var"""
        self.vs[98]["mm__"] = """directLink_T"""
        #self.vs[98]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class29assoc98layer5rule1class30')
        
    	# backward association ComponentInstance---->StatementList node
    	self.add_node()
    	self.vs[99]["type"] = """ruleDef"""
        self.vs[99]["mm__"] = """backward_link"""
        #self.vs[99]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class0blink99layer5rule1class11')
    	# backward association ComponentInstance---->GlobalVariableDeclaration node
    	self.add_node()
    	self.vs[100]["type"] = """ruleDef"""
        self.vs[100]["mm__"] = """backward_link"""
        #self.vs[100]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class0blink100layer5rule1class12')
    	# backward association RequiredPort---->Member node
    	self.add_node()
    	self.vs[101]["type"] = """ruleDef"""
        self.vs[101]["mm__"] = """backward_link"""
        #self.vs[101]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class2blink101layer5rule1class19')
    	# backward association ComponentInstance---->GlobalVariableDeclaration node
    	self.add_node()
    	self.vs[102]["type"] = """ruleDef"""
        self.vs[102]["mm__"] = """backward_link"""
        #self.vs[102]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class7blink102layer5rule1class20')
    	# backward association RequiredPort---->Member node
    	self.add_node()
    	self.vs[103]["type"] = """ruleDef"""
        self.vs[103]["mm__"] = """backward_link"""
        #self.vs[103]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class2blink103layer5rule1class27')
    	# backward association ProvidedPort---->GlobalVariableDeclaration node
    	self.add_node()
    	self.vs[104]["type"] = """ruleDef"""
        self.vs[104]["mm__"] = """backward_link"""
        #self.vs[104]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule1class9blink104layer5rule1class30')
        
        
        
        
        
        
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
        
