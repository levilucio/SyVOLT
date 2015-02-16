from core.himesis import Himesis
import cPickle as pickle
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
        # TODO Levi, need some help here because I don't know where does 
        # this value come from.
        self["mm__"] = pickle.loads("""(lp1
S'HimesisMM'
p2
a.""")
        
        self["name"] = """layer4rule3"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule3')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule3matchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule3applymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule3pairedwith2')
        
    	# match class ImplementationModule(layer4rule3class0) node
    	self.add_node()
    	self.vs[3]["name"] = """layer4rule3class0"""
        self.vs[3]["classtype"] = """ImplementationModule"""
        self.vs[3]["mm__"] = """ImplementationModule"""
        self.vs[3]["cardinality"] = """+"""
        #self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule3class0')
    	# match_contains node for class ImplementationModule(layer4rule3class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        #self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule3class0matchcontains4')
    	# match class Function(layer4rule3class1) node
    	self.add_node()
    	self.vs[5]["name"] = """layer4rule3class1"""
        self.vs[5]["classtype"] = """Function"""
        self.vs[5]["mm__"] = """Function"""
        self.vs[5]["cardinality"] = """+"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule3class1')
    	# match_contains node for class Function(layer4rule3class1)
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        #self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule3class1matchcontains6')
    	# match class Int32Type(layer4rule3class2) node
    	self.add_node()
    	self.vs[7]["name"] = """layer4rule3class2"""
        self.vs[7]["classtype"] = """Int32Type"""
        self.vs[7]["mm__"] = """Int32Type"""
        self.vs[7]["cardinality"] = """+"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule3class2')
    	# match_contains node for class Int32Type(layer4rule3class2)
        self.add_node()
        self.vs[8]["mm__"] = """match_contains"""
        #self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule3class2matchcontains8')
        
        
    	# apply class ImplementationModule(layer4rule3class3) node
    	self.add_node()
    	self.vs[9]["name"] = """layer4rule3class3"""
        self.vs[9]["classtype"] = """ImplementationModule"""
        self.vs[9]["mm__"] = """ImplementationModule"""
        self.vs[9]["cardinality"] = """1"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule3class3')
    	# apply_contains node for class ImplementationModule(layer4rule3class3)
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        #self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule3class3applycontains10')
    	# apply class Function(layer4rule3class4) node
    	self.add_node()
    	self.vs[11]["name"] = """layer4rule3class4"""
        self.vs[11]["classtype"] = """Function"""
        self.vs[11]["mm__"] = """Function"""
        self.vs[11]["cardinality"] = """1"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule3class4')
    	# apply_contains node for class Function(layer4rule3class4)
        self.add_node()
        self.vs[12]["mm__"] = """apply_contains"""
        #self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule3class4applycontains12')
    	# apply class VoidType(layer4rule3class5) node
    	self.add_node()
    	self.vs[13]["name"] = """layer4rule3class5"""
        self.vs[13]["classtype"] = """VoidType"""
        self.vs[13]["mm__"] = """VoidType"""
        self.vs[13]["cardinality"] = """1"""
        #self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule3class5')
    	# apply_contains node for class VoidType(layer4rule3class5)
        self.add_node()
        self.vs[14]["mm__"] = """apply_contains"""
        #self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule3class5applycontains14')
    	# apply class StatementList(layer4rule3class6) node
    	self.add_node()
    	self.vs[15]["name"] = """layer4rule3class6"""
        self.vs[15]["classtype"] = """StatementList"""
        self.vs[15]["mm__"] = """StatementList"""
        self.vs[15]["cardinality"] = """1"""
        #self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule3class6')
    	# apply_contains node for class StatementList(layer4rule3class6)
        self.add_node()
        self.vs[16]["mm__"] = """apply_contains"""
        #self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule3class6applycontains16')
    	# apply class Function(layer4rule3class7) node
    	self.add_node()
    	self.vs[17]["name"] = """layer4rule3class7"""
        self.vs[17]["classtype"] = """Function"""
        self.vs[17]["mm__"] = """Function"""
        self.vs[17]["cardinality"] = """1"""
        #self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule3class7')
    	# apply_contains node for class Function(layer4rule3class7)
        self.add_node()
        self.vs[18]["mm__"] = """apply_contains"""
        #self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule3class7applycontains18')
    	# apply class StatementList(layer4rule3class8) node
    	self.add_node()
    	self.vs[19]["name"] = """layer4rule3class8"""
        self.vs[19]["classtype"] = """StatementList"""
        self.vs[19]["mm__"] = """StatementList"""
        self.vs[19]["cardinality"] = """1"""
        #self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule3class8')
    	# apply_contains node for class StatementList(layer4rule3class8)
        self.add_node()
        self.vs[20]["mm__"] = """apply_contains"""
        #self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule3class8applycontains20')
    	# apply class Int32Type(layer4rule3class9) node
    	self.add_node()
    	self.vs[21]["name"] = """layer4rule3class9"""
        self.vs[21]["classtype"] = """Int32Type"""
        self.vs[21]["mm__"] = """Int32Type"""
        self.vs[21]["cardinality"] = """1"""
        #self.vs[21]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule3class9')
    	# apply_contains node for class Int32Type(layer4rule3class9)
        self.add_node()
        self.vs[22]["mm__"] = """apply_contains"""
        #self.vs[22]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule3class9applycontains22')
    	# apply class ExpressionStatement(layer4rule3class10) node
    	self.add_node()
    	self.vs[23]["name"] = """layer4rule3class10"""
        self.vs[23]["classtype"] = """ExpressionStatement"""
        self.vs[23]["mm__"] = """ExpressionStatement"""
        self.vs[23]["cardinality"] = """1"""
        #self.vs[23]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule3class10')
    	# apply_contains node for class ExpressionStatement(layer4rule3class10)
        self.add_node()
        self.vs[24]["mm__"] = """apply_contains"""
        #self.vs[24]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule3class10applycontains24')
    	# apply class FunctionCall(layer4rule3class11) node
    	self.add_node()
    	self.vs[25]["name"] = """layer4rule3class11"""
        self.vs[25]["classtype"] = """FunctionCall"""
        self.vs[25]["mm__"] = """FunctionCall"""
        self.vs[25]["cardinality"] = """1"""
        #self.vs[25]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule3class11')
    	# apply_contains node for class FunctionCall(layer4rule3class11)
        self.add_node()
        self.vs[26]["mm__"] = """apply_contains"""
        #self.vs[26]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule3class11applycontains26')
    	# apply class FunctionPrototype(layer4rule3class12) node
    	self.add_node()
    	self.vs[27]["name"] = """layer4rule3class12"""
        self.vs[27]["classtype"] = """FunctionPrototype"""
        self.vs[27]["mm__"] = """FunctionPrototype"""
        self.vs[27]["cardinality"] = """1"""
        #self.vs[27]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule3class12')
    	# apply_contains node for class FunctionPrototype(layer4rule3class12)
        self.add_node()
        self.vs[28]["mm__"] = """apply_contains"""
        #self.vs[28]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule3class12applycontains28')
        
        
    	# match association ImplementationModule--contents-->Function node
    	self.add_node()
    	self.vs[29]["associationType"] = """contents"""
        self.vs[29]["mm__"] = """directLink_S"""
        #self.vs[29]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule3class0assoc29layer4rule3class1')
    	# match association Function--type-->Int32Type node
    	self.add_node()
    	self.vs[30]["associationType"] = """type"""
        self.vs[30]["mm__"] = """directLink_S"""
        #self.vs[30]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule3class1assoc30layer4rule3class2')
        
    	# apply association ImplementationModule--contents-->Function node
    	self.add_node()
    	self.vs[31]["associationType"] = """contents"""
        self.vs[31]["mm__"] = """directLink_T"""
        #self.vs[31]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule3class3assoc31layer4rule3class4')
    	# apply association Function--type-->VoidType node
    	self.add_node()
    	self.vs[32]["associationType"] = """type"""
        self.vs[32]["mm__"] = """directLink_T"""
        #self.vs[32]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule3class4assoc32layer4rule3class5')
    	# apply association Function--body-->StatementList node
    	self.add_node()
    	self.vs[33]["associationType"] = """body"""
        self.vs[33]["mm__"] = """directLink_T"""
        #self.vs[33]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule3class4assoc33layer4rule3class6')
    	# apply association ImplementationModule--contents-->Function node
    	self.add_node()
    	self.vs[34]["associationType"] = """contents"""
        self.vs[34]["mm__"] = """directLink_T"""
        #self.vs[34]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule3class3assoc34layer4rule3class7')
    	# apply association Function--type-->Int32Type node
    	self.add_node()
    	self.vs[35]["associationType"] = """type"""
        self.vs[35]["mm__"] = """directLink_T"""
        #self.vs[35]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule3class7assoc35layer4rule3class9')
    	# apply association Function--body-->StatementList node
    	self.add_node()
    	self.vs[36]["associationType"] = """body"""
        self.vs[36]["mm__"] = """directLink_T"""
        #self.vs[36]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule3class7assoc36layer4rule3class8')
    	# apply association StatementList--statements-->ExpressionStatement node
    	self.add_node()
    	self.vs[37]["associationType"] = """statements"""
        self.vs[37]["mm__"] = """directLink_T"""
        #self.vs[37]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule3class8assoc37layer4rule3class10')
    	# apply association ExpressionStatement--expr-->FunctionCall node
    	self.add_node()
    	self.vs[38]["associationType"] = """expr"""
        self.vs[38]["mm__"] = """directLink_T"""
        #self.vs[38]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule3class10assoc38layer4rule3class11')
    	# apply association FunctionCall--function-->FunctionPrototype node
    	self.add_node()
    	self.vs[39]["associationType"] = """function"""
        self.vs[39]["mm__"] = """directLink_T"""
        #self.vs[39]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule3class11assoc39layer4rule3class12')
        
    	# backward association ImplementationModule---->ImplementationModule node
    	self.add_node()
    	self.vs[40]["type"] = """ruleDef"""
        self.vs[40]["mm__"] = """backward_link"""
        #self.vs[40]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule3class0blink40layer4rule3class3')
    	# backward association Function---->FunctionPrototype node
    	self.add_node()
    	self.vs[41]["type"] = """ruleDef"""
        self.vs[41]["mm__"] = """backward_link"""
        #self.vs[41]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule3class1blink41layer4rule3class12')
        
        
    	# has match attribute name(layer4rule3class0attribute0) node
    	self.add_node()
    	self.vs[42]["mm__"] = """hasAttribute_S"""
        #self.vs[42]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer4rule3class0attribute0')
    	# match attribute name(layer4rule3class0attribute0) node
    	self.add_node()
    	self.vs[43]["name"] = """name"""
        self.vs[43]["mm__"] = """Attribute"""
        self.vs[43]["Type"] = """'String'"""
        #self.vs[43]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule3class0attribute0')
    	# has match attribute name(layer4rule3class1attribute0) node
    	self.add_node()
    	self.vs[44]["mm__"] = """hasAttribute_S"""
        #self.vs[44]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer4rule3class1attribute0')
    	# match attribute name(layer4rule3class1attribute0) node
    	self.add_node()
    	self.vs[45]["name"] = """name"""
        self.vs[45]["mm__"] = """Attribute"""
        self.vs[45]["Type"] = """'String'"""
        #self.vs[45]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule3class1attribute0')
    	# match attribute equation name(layer4rule3class1attribute0) node
    	self.add_node()
    	self.vs[46]["name"] = """eq_"""
        self.vs[46]["mm__"] = """Equation"""
        #self.vs[46]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equationlayer4rule3class1attribute0')
    	# match attribute equation left expr name(layer4rule3class1attribute0) node
    	self.add_node()
    	self.vs[47]["mm__"] = """leftExpr"""
        #self.vs[47]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExprlayer4rule3class1attribute0')
    	# match attribute equation right expr name(layer4rule3class1attribute0) node
    	self.add_node()
    	self.vs[48]["mm__"] = """rightExpr"""
        #self.vs[48]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExprlayer4rule3class1attribute0')
    	# apply attribute atom name(layer4rule3class1attribute0) node
    	self.add_node()
    	self.vs[49]["name"] = """main"""
        self.vs[49]["mm__"] = """Constant"""
        self.vs[49]["Type"] = """'String'"""
        #self.vs[49]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atomlayer4rule3class1attribute049')
        
        
    	# has apply attribute name(layer4rule3class4attribute0) node
    	self.add_node()
    	self.vs[50]["mm__"] = """hasAttribute_T"""
        #self.vs[50]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer4rule3class4attribute0')
    	# apply attribute name(layer4rule3class4attribute0) node
    	self.add_node()
    	self.vs[51]["name"] = """name"""
        self.vs[51]["mm__"] = """Attribute"""
        self.vs[51]["Type"] = """'String'"""
        #self.vs[51]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule3class4attribute0')
    	# apply attribute equation name(layer4rule3class4attribute0) node
    	self.add_node()
    	self.vs[52]["name"] = """eq_"""
        self.vs[52]["mm__"] = """Equation"""
        #self.vs[52]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equationlayer4rule3class4attribute0')
    	# apply attribute equation left expr name(layer4rule3class4attribute0) node
    	self.add_node()
    	self.vs[53]["mm__"] = """leftExpr"""
        #self.vs[53]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExprlayer4rule3class4attribute0')
    	# apply attribute equation right expr name(layer4rule3class4attribute0) node
    	self.add_node()
    	self.vs[54]["mm__"] = """rightExpr"""
        #self.vs[54]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExprlayer4rule3class4attribute0')
    	# attribute concat name(layer4rule3class4attribute0) node
    	self.add_node()
    	self.vs[55]["name"] = """Concatlayer4rule3class4attribute055"""
        self.vs[55]["mm__"] = """Concat"""
        self.vs[55]["Type"] = """'String'"""
        #self.vs[55]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concatlayer4rule3class4attribute055')
    	# apply attribute concat has left args name(layer4rule3class4attribute0) node
        self.add_node()
    	self.vs[56]["mm__"] = """hasArgs"""
        #self.vs[56]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgslayer4rule3class4attribute056')
    	# apply attribute concat has right args name(layer4rule3class4attribute0) node
        self.add_node()
    	self.vs[57]["mm__"] = """hasArgs"""
        #self.vs[57]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgslayer4rule3class4attribute057')
    	# apply attribute atom name(layer4rule3class4attribute0) node
    	self.add_node()
    	self.vs[58]["name"] = """_blockexpr_main_2"""
        self.vs[58]["mm__"] = """Constant"""
        self.vs[58]["Type"] = """'String'"""
        #self.vs[58]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atomlayer4rule3class4attribute058')
    	# has apply attribute name(layer4rule3class7attribute0) node
    	self.add_node()
    	self.vs[59]["mm__"] = """hasAttribute_T"""
        #self.vs[59]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer4rule3class7attribute0')
    	# apply attribute name(layer4rule3class7attribute0) node
    	self.add_node()
    	self.vs[60]["name"] = """name"""
        self.vs[60]["mm__"] = """Attribute"""
        self.vs[60]["Type"] = """'String'"""
        #self.vs[60]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule3class7attribute0')
    	# apply attribute equation name(layer4rule3class7attribute0) node
    	self.add_node()
    	self.vs[61]["name"] = """eq_"""
        self.vs[61]["mm__"] = """Equation"""
        #self.vs[61]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equationlayer4rule3class7attribute0')
    	# apply attribute equation left expr name(layer4rule3class7attribute0) node
    	self.add_node()
    	self.vs[62]["mm__"] = """leftExpr"""
        #self.vs[62]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExprlayer4rule3class7attribute0')
    	# apply attribute equation right expr name(layer4rule3class7attribute0) node
    	self.add_node()
    	self.vs[63]["mm__"] = """rightExpr"""
        #self.vs[63]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExprlayer4rule3class7attribute0')
    	# apply attribute atom name(layer4rule3class7attribute0) node
    	self.add_node()
    	self.vs[64]["name"] = """main"""
        self.vs[64]["mm__"] = """Constant"""
        self.vs[64]["Type"] = """'String'"""
        #self.vs[64]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atomlayer4rule3class7attribute064')
        
        
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
    		(3,42), # match_class ImplementationModule(layer4rule3class0) -> has_match_attribute name (layer4rule3class0attribute0)
    		(42,43), #  has_match_attribute name (layer4rule3class0attribute0) -> match_attribute name (layer4rule3class0attribute0)
    		(5,44), # match_class Function(layer4rule3class1) -> has_match_attribute name (layer4rule3class1attribute0)
    		(44,45), #  has_match_attribute name (layer4rule3class1attribute0) -> match_attribute name (layer4rule3class1attribute0)
	    	(46,47), #  equation of match attribute name (layer4rule3class1attribute0) -> left_expr
    		(47,45), #  left_expr -> match_attribute name (layer4rule3class1attribute0)
    		(46,48), #  equation of match attribute name (layer4rule3class1attribute0) -> right_expr
    		(48,49), # right_expr --> term
    		(11,50), # apply_class Function(layer4rule3class4) -> has_apply_attribute name (layer4rule3class4attribute0)
    		(50,51), #  has_apply_attribute name (layer4rule3class4attribute0) -> apply_attribute name (layer4rule3class4attribute0)
    		(52,53), #  equation of apply attribute name (layer4rule3class4attribute0) -> left_expr
    		(53,51), #  left_expr -> apply_attribute name (layer4rule3class4attribute0)
    		(52,54), #  equation of apply attribute name (layer4rule3class4attribute0) -> right_expr
    		(55,56), #  apply attribute concat name (layer4rule3class4attribute0) -> left has_args  
    		(56,43), #  left has_args -> term
    		(55,57), #  apply attribute concat name (layer4rule3class4attribute0) -> right has_args  
    		(57,58), #  right has_args -> term
    		(54,55), # right_expr --> term
    		(17,59), # apply_class Function(layer4rule3class7) -> has_apply_attribute name (layer4rule3class7attribute0)
    		(59,60), #  has_apply_attribute name (layer4rule3class7attribute0) -> apply_attribute name (layer4rule3class7attribute0)
    		(61,62), #  equation of apply attribute name (layer4rule3class7attribute0) -> left_expr
    		(62,60), #  left_expr -> apply_attribute name (layer4rule3class7attribute0)
    		(61,63), #  equation of apply attribute name (layer4rule3class7attribute0) -> right_expr
    		(63,64), # right_expr --> term
        	(0,2), # matchmodel -> pairedwith
        	(2,1) # pairedwith -> applyModel
        ])
        
