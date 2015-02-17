from core.himesis import Himesis
import cPickle as pickle
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
        # TODO Levi, need some help here because I don't know where does 
        # this value come from.
        self["mm__"] = pickle.loads("""(lp1
S'HimesisMM'
p2
a.""")
        
        self["name"] = """layer5rule0"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0matchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0applymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0pairedwith2')
        
    	# match class ComponentInstance(layer5rule0class0) node
    	self.add_node()
    	self.vs[3]["name"] = """layer5rule0class0"""
        self.vs[3]["classtype"] = """ComponentInstance"""
        self.vs[3]["mm__"] = """ComponentInstance"""
        self.vs[3]["cardinality"] = """+"""
        #self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0class0')
    	# match_contains node for class ComponentInstance(layer5rule0class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        #self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0class0matchcontains4')
    	# match class AtomicComponent(layer5rule0class1) node
    	self.add_node()
    	self.vs[5]["name"] = """layer5rule0class1"""
        self.vs[5]["classtype"] = """AtomicComponent"""
        self.vs[5]["mm__"] = """AtomicComponent"""
        self.vs[5]["cardinality"] = """+"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0class1')
    	# match_contains node for class AtomicComponent(layer5rule0class1)
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        #self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0class1matchcontains6')
    	# match class ProvidedPort(layer5rule0class2) node
    	self.add_node()
    	self.vs[7]["name"] = """layer5rule0class2"""
        self.vs[7]["classtype"] = """ProvidedPort"""
        self.vs[7]["mm__"] = """ProvidedPort"""
        self.vs[7]["cardinality"] = """+"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0class2')
    	# match_contains node for class ProvidedPort(layer5rule0class2)
        self.add_node()
        self.vs[8]["mm__"] = """match_contains"""
        #self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0class2matchcontains8')
    	# match class ClientServerInterface(layer5rule0class3) node
    	self.add_node()
    	self.vs[9]["name"] = """layer5rule0class3"""
        self.vs[9]["classtype"] = """ClientServerInterface"""
        self.vs[9]["mm__"] = """ClientServerInterface"""
        self.vs[9]["cardinality"] = """+"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0class3')
    	# match_contains node for class ClientServerInterface(layer5rule0class3)
        self.add_node()
        self.vs[10]["mm__"] = """match_contains"""
        #self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0class3matchcontains10')
    	# match class Operation(layer5rule0class4) node
    	self.add_node()
    	self.vs[11]["name"] = """layer5rule0class4"""
        self.vs[11]["classtype"] = """Operation"""
        self.vs[11]["mm__"] = """Operation"""
        self.vs[11]["cardinality"] = """+"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0class4')
    	# match_contains node for class Operation(layer5rule0class4)
        self.add_node()
        self.vs[12]["mm__"] = """match_contains"""
        #self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0class4matchcontains12')
        
        
    	# apply class StatementList(layer5rule0class5) node
    	self.add_node()
    	self.vs[13]["name"] = """layer5rule0class5"""
        self.vs[13]["classtype"] = """StatementList"""
        self.vs[13]["mm__"] = """StatementList"""
        self.vs[13]["cardinality"] = """1"""
        #self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0class5')
    	# apply_contains node for class StatementList(layer5rule0class5)
        self.add_node()
        self.vs[14]["mm__"] = """apply_contains"""
        #self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0class5applycontains14')
    	# apply class GlobalVariableDeclaration(layer5rule0class6) node
    	self.add_node()
    	self.vs[15]["name"] = """layer5rule0class6"""
        self.vs[15]["classtype"] = """GlobalVariableDeclaration"""
        self.vs[15]["mm__"] = """GlobalVariableDeclaration"""
        self.vs[15]["cardinality"] = """1"""
        #self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0class6')
    	# apply_contains node for class GlobalVariableDeclaration(layer5rule0class6)
        self.add_node()
        self.vs[16]["mm__"] = """apply_contains"""
        #self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0class6applycontains16')
    	# apply class ExpressionStatement(layer5rule0class7) node
    	self.add_node()
    	self.vs[17]["name"] = """layer5rule0class7"""
        self.vs[17]["classtype"] = """ExpressionStatement"""
        self.vs[17]["mm__"] = """ExpressionStatement"""
        self.vs[17]["cardinality"] = """1"""
        #self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0class7')
    	# apply_contains node for class ExpressionStatement(layer5rule0class7)
        self.add_node()
        self.vs[18]["mm__"] = """apply_contains"""
        #self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0class7applycontains18')
    	# apply class AssignmentExpr(layer5rule0class8) node
    	self.add_node()
    	self.vs[19]["name"] = """layer5rule0class8"""
        self.vs[19]["classtype"] = """AssignmentExpr"""
        self.vs[19]["mm__"] = """AssignmentExpr"""
        self.vs[19]["cardinality"] = """1"""
        #self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0class8')
    	# apply_contains node for class AssignmentExpr(layer5rule0class8)
        self.add_node()
        self.vs[20]["mm__"] = """apply_contains"""
        #self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0class8applycontains20')
    	# apply class GenericDotExpression(layer5rule0class9) node
    	self.add_node()
    	self.vs[21]["name"] = """layer5rule0class9"""
        self.vs[21]["classtype"] = """GenericDotExpression"""
        self.vs[21]["mm__"] = """GenericDotExpression"""
        self.vs[21]["cardinality"] = """1"""
        #self.vs[21]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0class9')
    	# apply_contains node for class GenericDotExpression(layer5rule0class9)
        self.add_node()
        self.vs[22]["mm__"] = """apply_contains"""
        #self.vs[22]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0class9applycontains22')
    	# apply class ReferenceExpr(layer5rule0class10) node
    	self.add_node()
    	self.vs[23]["name"] = """layer5rule0class10"""
        self.vs[23]["classtype"] = """ReferenceExpr"""
        self.vs[23]["mm__"] = """ReferenceExpr"""
        self.vs[23]["cardinality"] = """1"""
        #self.vs[23]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0class10')
    	# apply_contains node for class ReferenceExpr(layer5rule0class10)
        self.add_node()
        self.vs[24]["mm__"] = """apply_contains"""
        #self.vs[24]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0class10applycontains24')
    	# apply class GlobalVarRef(layer5rule0class11) node
    	self.add_node()
    	self.vs[25]["name"] = """layer5rule0class11"""
        self.vs[25]["classtype"] = """GlobalVarRef"""
        self.vs[25]["mm__"] = """GlobalVarRef"""
        self.vs[25]["cardinality"] = """1"""
        #self.vs[25]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0class11')
    	# apply_contains node for class GlobalVarRef(layer5rule0class11)
        self.add_node()
        self.vs[26]["mm__"] = """apply_contains"""
        #self.vs[26]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0class11applycontains26')
    	# apply class GenericMemberRef(layer5rule0class12) node
    	self.add_node()
    	self.vs[27]["name"] = """layer5rule0class12"""
        self.vs[27]["classtype"] = """GenericMemberRef"""
        self.vs[27]["mm__"] = """GenericMemberRef"""
        self.vs[27]["cardinality"] = """1"""
        #self.vs[27]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0class12')
    	# apply_contains node for class GenericMemberRef(layer5rule0class12)
        self.add_node()
        self.vs[28]["mm__"] = """apply_contains"""
        #self.vs[28]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0class12applycontains28')
    	# apply class CFunctionPointerStructMember(layer5rule0class13) node
    	self.add_node()
    	self.vs[29]["name"] = """layer5rule0class13"""
        self.vs[29]["classtype"] = """CFunctionPointerStructMember"""
        self.vs[29]["mm__"] = """CFunctionPointerStructMember"""
        self.vs[29]["cardinality"] = """1"""
        #self.vs[29]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0class13')
    	# apply_contains node for class CFunctionPointerStructMember(layer5rule0class13)
        self.add_node()
        self.vs[30]["mm__"] = """apply_contains"""
        #self.vs[30]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0class13applycontains30')
    	# apply class FunctionPrototype(layer5rule0class14) node
    	self.add_node()
    	self.vs[31]["name"] = """layer5rule0class14"""
        self.vs[31]["classtype"] = """FunctionPrototype"""
        self.vs[31]["mm__"] = """FunctionPrototype"""
        self.vs[31]["cardinality"] = """1"""
        #self.vs[31]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0class14')
    	# apply_contains node for class FunctionPrototype(layer5rule0class14)
        self.add_node()
        self.vs[32]["mm__"] = """apply_contains"""
        #self.vs[32]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0class14applycontains32')
    	# apply class FunctionRefExpr(layer5rule0class15) node
    	self.add_node()
    	self.vs[33]["name"] = """layer5rule0class15"""
        self.vs[33]["classtype"] = """FunctionRefExpr"""
        self.vs[33]["mm__"] = """FunctionRefExpr"""
        self.vs[33]["cardinality"] = """1"""
        #self.vs[33]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0class15')
    	# apply_contains node for class FunctionRefExpr(layer5rule0class15)
        self.add_node()
        self.vs[34]["mm__"] = """apply_contains"""
        #self.vs[34]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0class15applycontains34')
        
        
    	# match association ComponentInstance--component-->AtomicComponent node
    	self.add_node()
    	self.vs[35]["associationType"] = """component"""
        self.vs[35]["mm__"] = """directLink_S"""
        #self.vs[35]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0class0assoc35layer5rule0class1')
    	# match association AtomicComponent--contents-->ProvidedPort node
    	self.add_node()
    	self.vs[36]["associationType"] = """contents"""
        self.vs[36]["mm__"] = """directLink_S"""
        #self.vs[36]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0class1assoc36layer5rule0class2')
    	# match association ProvidedPort--intf-->ClientServerInterface node
    	self.add_node()
    	self.vs[37]["associationType"] = """intf"""
        self.vs[37]["mm__"] = """directLink_S"""
        #self.vs[37]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0class2assoc37layer5rule0class3')
    	# match association ClientServerInterface--contents-->Operation node
    	self.add_node()
    	self.vs[38]["associationType"] = """contents"""
        self.vs[38]["mm__"] = """directLink_S"""
        #self.vs[38]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0class3assoc38layer5rule0class4')
        
    	# apply association StatementList--statements-->ExpressionStatement node
    	self.add_node()
    	self.vs[39]["associationType"] = """statements"""
        self.vs[39]["mm__"] = """directLink_T"""
        #self.vs[39]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0class5assoc39layer5rule0class7')
    	# apply association ExpressionStatement--expr-->AssignmentExpr node
    	self.add_node()
    	self.vs[40]["associationType"] = """expr"""
        self.vs[40]["mm__"] = """directLink_T"""
        #self.vs[40]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0class7assoc40layer5rule0class8')
    	# apply association AssignmentExpr--left-->GenericDotExpression node
    	self.add_node()
    	self.vs[41]["associationType"] = """left"""
        self.vs[41]["mm__"] = """directLink_T"""
        #self.vs[41]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0class8assoc41layer5rule0class9')
    	# apply association AssignmentExpr--right-->ReferenceExpr node
    	self.add_node()
    	self.vs[42]["associationType"] = """right"""
        self.vs[42]["mm__"] = """directLink_T"""
        #self.vs[42]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0class8assoc42layer5rule0class10')
    	# apply association GenericDotExpression--expression-->GlobalVarRef node
    	self.add_node()
    	self.vs[43]["associationType"] = """expression"""
        self.vs[43]["mm__"] = """directLink_T"""
        #self.vs[43]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0class9assoc43layer5rule0class11')
    	# apply association GenericDotExpression--target-->GenericMemberRef node
    	self.add_node()
    	self.vs[44]["associationType"] = """target"""
        self.vs[44]["mm__"] = """directLink_T"""
        #self.vs[44]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0class9assoc44layer5rule0class12')
    	# apply association GlobalVarRef--var-->GlobalVariableDeclaration node
    	self.add_node()
    	self.vs[45]["associationType"] = """var"""
        self.vs[45]["mm__"] = """directLink_T"""
        #self.vs[45]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0class11assoc45layer5rule0class6')
    	# apply association GenericMemberRef--member-->CFunctionPointerStructMember node
    	self.add_node()
    	self.vs[46]["associationType"] = """member"""
        self.vs[46]["mm__"] = """directLink_T"""
        #self.vs[46]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0class12assoc46layer5rule0class13')
    	# apply association ReferenceExpr--expression-->FunctionRefExpr node
    	self.add_node()
    	self.vs[47]["associationType"] = """expression"""
        self.vs[47]["mm__"] = """directLink_T"""
        #self.vs[47]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0class10assoc47layer5rule0class15')
    	# apply association FunctionRefExpr--function-->FunctionPrototype node
    	self.add_node()
    	self.vs[48]["associationType"] = """function"""
        self.vs[48]["mm__"] = """directLink_T"""
        #self.vs[48]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0class15assoc48layer5rule0class14')
        
    	# backward association ComponentInstance---->StatementList node
    	self.add_node()
    	self.vs[49]["type"] = """ruleDef"""
        self.vs[49]["mm__"] = """backward_link"""
        #self.vs[49]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0class0blink49layer5rule0class5')
    	# backward association ProvidedPort---->GlobalVariableDeclaration node
    	self.add_node()
    	self.vs[50]["type"] = """ruleDef"""
        self.vs[50]["mm__"] = """backward_link"""
        #self.vs[50]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0class2blink50layer5rule0class6')
    	# backward association Operation---->CFunctionPointerStructMember node
    	self.add_node()
    	self.vs[51]["type"] = """ruleDef"""
        self.vs[51]["mm__"] = """backward_link"""
        #self.vs[51]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0class4blink51layer5rule0class13')
    	# backward association ProvidedPort---->FunctionPrototype node
    	self.add_node()
    	self.vs[52]["type"] = """ruleDef"""
        self.vs[52]["mm__"] = """backward_link"""
        #self.vs[52]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule0class2blink52layer5rule0class14')
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
    		(0,4), # matchmodel -> match_contains
    		(4,3), # match_contains -> match_class ComponentInstance(layer5rule0class0)
    		(0,6), # matchmodel -> match_contains
    		(6,5), # match_contains -> match_class AtomicComponent(layer5rule0class1)
    		(0,8), # matchmodel -> match_contains
    		(8,7), # match_contains -> match_class ProvidedPort(layer5rule0class2)
    		(0,10), # matchmodel -> match_contains
    		(10,9), # match_contains -> match_class ClientServerInterface(layer5rule0class3)
    		(0,12), # matchmodel -> match_contains
    		(12,11), # match_contains -> match_class Operation(layer5rule0class4)
    		(1,14), # applymodel -> apply_contains
    		(14,13), # apply_contains -> apply_class StatementList(layer5rule0class5)
    		(1,16), # applymodel -> apply_contains
    		(16,15), # apply_contains -> apply_class GlobalVariableDeclaration(layer5rule0class6)
    		(1,18), # applymodel -> apply_contains
    		(18,17), # apply_contains -> apply_class ExpressionStatement(layer5rule0class7)
    		(1,20), # applymodel -> apply_contains
    		(20,19), # apply_contains -> apply_class AssignmentExpr(layer5rule0class8)
    		(1,22), # applymodel -> apply_contains
    		(22,21), # apply_contains -> apply_class GenericDotExpression(layer5rule0class9)
    		(1,24), # applymodel -> apply_contains
    		(24,23), # apply_contains -> apply_class ReferenceExpr(layer5rule0class10)
    		(1,26), # applymodel -> apply_contains
    		(26,25), # apply_contains -> apply_class GlobalVarRef(layer5rule0class11)
    		(1,28), # applymodel -> apply_contains
    		(28,27), # apply_contains -> apply_class GenericMemberRef(layer5rule0class12)
    		(1,30), # applymodel -> apply_contains
    		(30,29), # apply_contains -> apply_class CFunctionPointerStructMember(layer5rule0class13)
    		(1,32), # applymodel -> apply_contains
    		(32,31), # apply_contains -> apply_class FunctionPrototype(layer5rule0class14)
    		(1,34), # applymodel -> apply_contains
    		(34,33), # apply_contains -> apply_class FunctionRefExpr(layer5rule0class15)
    		(3,35), # match_class ComponentInstance(layer5rule0class0) -> association component
    		(35,5), # association component  -> match_class AtomicComponent(layer5rule0class1)
    		(5,36), # match_class AtomicComponent(layer5rule0class1) -> association contents
    		(36,7), # association contents  -> match_class ProvidedPort(layer5rule0class2)
    		(7,37), # match_class ProvidedPort(layer5rule0class2) -> association intf
    		(37,9), # association intf  -> match_class ClientServerInterface(layer5rule0class3)
    		(9,38), # match_class ClientServerInterface(layer5rule0class3) -> association contents
    		(38,11), # association contents  -> match_class Operation(layer5rule0class4)
    		(13,39), # apply_class StatementList(layer5rule0class5) -> association statements
    		(39,17), # association statements  -> apply_class ExpressionStatement(layer5rule0class7)
    		(17,40), # apply_class ExpressionStatement(layer5rule0class7) -> association expr
    		(40,19), # association expr  -> apply_class AssignmentExpr(layer5rule0class8)
    		(19,41), # apply_class AssignmentExpr(layer5rule0class8) -> association left
    		(41,21), # association left  -> apply_class GenericDotExpression(layer5rule0class9)
    		(19,42), # apply_class AssignmentExpr(layer5rule0class8) -> association right
    		(42,23), # association right  -> apply_class ReferenceExpr(layer5rule0class10)
    		(21,43), # apply_class GenericDotExpression(layer5rule0class9) -> association expression
    		(43,25), # association expression  -> apply_class GlobalVarRef(layer5rule0class11)
    		(21,44), # apply_class GenericDotExpression(layer5rule0class9) -> association target
    		(44,27), # association target  -> apply_class GenericMemberRef(layer5rule0class12)
    		(25,45), # apply_class GlobalVarRef(layer5rule0class11) -> association var
    		(45,15), # association var  -> apply_class GlobalVariableDeclaration(layer5rule0class6)
    		(27,46), # apply_class GenericMemberRef(layer5rule0class12) -> association member
    		(46,29), # association member  -> apply_class CFunctionPointerStructMember(layer5rule0class13)
    		(23,47), # apply_class ReferenceExpr(layer5rule0class10) -> association expression
    		(47,33), # association expression  -> apply_class FunctionRefExpr(layer5rule0class15)
    		(33,48), # apply_class FunctionRefExpr(layer5rule0class15) -> association function
    		(48,31), # association function  -> apply_class FunctionPrototype(layer5rule0class14)
    		(13,49), # apply_class StatementList(layer5rule0class5) -> backward_association
    		(49,3), #  backward_association -> apply_class ComponentInstance(layer5rule0class0)
    		(15,50), # apply_class GlobalVariableDeclaration(layer5rule0class6) -> backward_association
    		(50,7), #  backward_association -> apply_class ProvidedPort(layer5rule0class2)
    		(29,51), # apply_class CFunctionPointerStructMember(layer5rule0class13) -> backward_association
    		(51,11), #  backward_association -> apply_class Operation(layer5rule0class4)
    		(31,52), # apply_class FunctionPrototype(layer5rule0class14) -> backward_association
    		(52,7), #  backward_association -> apply_class ProvidedPort(layer5rule0class2)
        	(0,2), # matchmodel -> pairedwith
        	(2,1) # pairedwith -> applyModel
        ])
        