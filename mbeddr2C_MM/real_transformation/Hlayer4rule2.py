from core.himesis import Himesis
import cPickle as pickle
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
        # TODO Levi, need some help here because I don't know where does 
        # this value come from.
        self["mm__"] = pickle.loads("""(lp1
S'HimesisMM'
p2
a.""")
        
        self["name"] = """layer4rule2"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule2')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule2matchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule2applymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule2pairedwith2')
        
    	# match class ImplementationModule(layer4rule2class0) node
    	self.add_node()
    	self.vs[3]["name"] = """layer4rule2class0"""
        self.vs[3]["classtype"] = """ImplementationModule"""
        self.vs[3]["mm__"] = """ImplementationModule"""
        self.vs[3]["cardinality"] = """+"""
        #self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule2class0')
    	# match_contains node for class ImplementationModule(layer4rule2class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        #self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule2class0matchcontains4')
    	# match class TestCase(layer4rule2class1) node
    	self.add_node()
    	self.vs[5]["name"] = """layer4rule2class1"""
        self.vs[5]["classtype"] = """TestCase"""
        self.vs[5]["mm__"] = """TestCase"""
        self.vs[5]["cardinality"] = """+"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule2class1')
    	# match_contains node for class TestCase(layer4rule2class1)
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        #self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule2class1matchcontains6')
        
        
    	# apply class ImplementationModule(layer4rule2class2) node
    	self.add_node()
    	self.vs[7]["name"] = """layer4rule2class2"""
        self.vs[7]["classtype"] = """ImplementationModule"""
        self.vs[7]["mm__"] = """ImplementationModule"""
        self.vs[7]["cardinality"] = """1"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule2class2')
    	# apply_contains node for class ImplementationModule(layer4rule2class2)
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        #self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule2class2applycontains8')
    	# apply class Function(layer4rule2class3) node
    	self.add_node()
    	self.vs[9]["name"] = """layer4rule2class3"""
        self.vs[9]["classtype"] = """Function"""
        self.vs[9]["mm__"] = """Function"""
        self.vs[9]["cardinality"] = """1"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule2class3')
    	# apply_contains node for class Function(layer4rule2class3)
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        #self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule2class3applycontains10')
    	# apply class VoidType(layer4rule2class4) node
    	self.add_node()
    	self.vs[11]["name"] = """layer4rule2class4"""
        self.vs[11]["classtype"] = """VoidType"""
        self.vs[11]["mm__"] = """VoidType"""
        self.vs[11]["cardinality"] = """1"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule2class4')
    	# apply_contains node for class VoidType(layer4rule2class4)
        self.add_node()
        self.vs[12]["mm__"] = """apply_contains"""
        #self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule2class4applycontains12')
    	# apply class StatementList(layer4rule2class5) node
    	self.add_node()
    	self.vs[13]["name"] = """layer4rule2class5"""
        self.vs[13]["classtype"] = """StatementList"""
        self.vs[13]["mm__"] = """StatementList"""
        self.vs[13]["cardinality"] = """1"""
        #self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule2class5')
    	# apply_contains node for class StatementList(layer4rule2class5)
        self.add_node()
        self.vs[14]["mm__"] = """apply_contains"""
        #self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule2class5applycontains14')
        
        
    	# match association ImplementationModule--contents-->TestCase node
    	self.add_node()
    	self.vs[15]["associationType"] = """contents"""
        self.vs[15]["mm__"] = """directLink_S"""
        #self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule2class0assoc15layer4rule2class1')
        
    	# apply association ImplementationModule--contents-->Function node
    	self.add_node()
    	self.vs[16]["associationType"] = """contents"""
        self.vs[16]["mm__"] = """directLink_T"""
        #self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule2class2assoc16layer4rule2class3')
    	# apply association Function--type-->VoidType node
    	self.add_node()
    	self.vs[17]["associationType"] = """type"""
        self.vs[17]["mm__"] = """directLink_T"""
        #self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule2class3assoc17layer4rule2class4')
    	# apply association Function--body-->StatementList node
    	self.add_node()
    	self.vs[18]["associationType"] = """body"""
        self.vs[18]["mm__"] = """directLink_T"""
        #self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule2class3assoc18layer4rule2class5')
        
    	# backward association ImplementationModule---->ImplementationModule node
    	self.add_node()
    	self.vs[19]["type"] = """ruleDef"""
        self.vs[19]["mm__"] = """backward_link"""
        #self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule2class0blink19layer4rule2class2')
        
        
    	# has match attribute name(layer4rule2class0attribute0) node
    	self.add_node()
    	self.vs[20]["mm__"] = """hasAttribute_S"""
        #self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer4rule2class0attribute0')
    	# match attribute name(layer4rule2class0attribute0) node
    	self.add_node()
    	self.vs[21]["name"] = """name"""
        self.vs[21]["mm__"] = """Attribute"""
        self.vs[21]["Type"] = """'String'"""
        #self.vs[21]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule2class0attribute0')
    	# has match attribute name(layer4rule2class1attribute0) node
    	self.add_node()
    	self.vs[22]["mm__"] = """hasAttribute_S"""
        #self.vs[22]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer4rule2class1attribute0')
    	# match attribute name(layer4rule2class1attribute0) node
    	self.add_node()
    	self.vs[23]["name"] = """name"""
        self.vs[23]["mm__"] = """Attribute"""
        self.vs[23]["Type"] = """'String'"""
        #self.vs[23]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule2class1attribute0')
        
        
    	# has apply attribute name(layer4rule2class3attribute0) node
    	self.add_node()
    	self.vs[24]["mm__"] = """hasAttribute_T"""
        #self.vs[24]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer4rule2class3attribute0')
    	# apply attribute name(layer4rule2class3attribute0) node
    	self.add_node()
    	self.vs[25]["name"] = """name"""
        self.vs[25]["mm__"] = """Attribute"""
        self.vs[25]["Type"] = """'String'"""
        #self.vs[25]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule2class3attribute0')
    	# apply attribute equation name(layer4rule2class3attribute0) node
    	self.add_node()
    	self.vs[26]["name"] = """eq_"""
        self.vs[26]["mm__"] = """Equation"""
        #self.vs[26]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equationlayer4rule2class3attribute0')
    	# apply attribute equation left expr name(layer4rule2class3attribute0) node
    	self.add_node()
    	self.vs[27]["mm__"] = """leftExpr"""
        #self.vs[27]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExprlayer4rule2class3attribute0')
    	# apply attribute equation right expr name(layer4rule2class3attribute0) node
    	self.add_node()
    	self.vs[28]["mm__"] = """rightExpr"""
        #self.vs[28]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExprlayer4rule2class3attribute0')
    	# attribute concat name(layer4rule2class3attribute0) node
    	self.add_node()
    	self.vs[29]["name"] = """Concatlayer4rule2class3attribute029"""
        self.vs[29]["mm__"] = """Concat"""
        self.vs[29]["Type"] = """'String'"""
        #self.vs[29]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concatlayer4rule2class3attribute029')
    	# apply attribute concat has left args name(layer4rule2class3attribute0) node
        self.add_node()
    	self.vs[30]["mm__"] = """hasArgs"""
        #self.vs[30]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgslayer4rule2class3attribute030')
    	# apply attribute concat has right args name(layer4rule2class3attribute0) node
        self.add_node()
    	self.vs[31]["mm__"] = """hasArgs"""
        #self.vs[31]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgslayer4rule2class3attribute031')
    	# attribute concat name(layer4rule2class3attribute0) node
    	self.add_node()
    	self.vs[32]["name"] = """Concatlayer4rule2class3attribute032"""
        self.vs[32]["mm__"] = """Concat"""
        self.vs[32]["Type"] = """'String'"""
        #self.vs[32]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concatlayer4rule2class3attribute032')
    	# apply attribute concat has left args name(layer4rule2class3attribute0) node
        self.add_node()
    	self.vs[33]["mm__"] = """hasArgs"""
        #self.vs[33]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgslayer4rule2class3attribute033')
    	# apply attribute concat has right args name(layer4rule2class3attribute0) node
        self.add_node()
    	self.vs[34]["mm__"] = """hasArgs"""
        #self.vs[34]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgslayer4rule2class3attribute034')
    	# apply attribute atom name(layer4rule2class3attribute0) node
    	self.add_node()
    	self.vs[35]["name"] = """_"""
        self.vs[35]["mm__"] = """Constant"""
        self.vs[35]["Type"] = """'String'"""
        #self.vs[35]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atomlayer4rule2class3attribute035')
        
        
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
    		(3,20), # match_class ImplementationModule(layer4rule2class0) -> has_match_attribute name (layer4rule2class0attribute0)
    		(20,21), #  has_match_attribute name (layer4rule2class0attribute0) -> match_attribute name (layer4rule2class0attribute0)
    		(5,22), # match_class TestCase(layer4rule2class1) -> has_match_attribute name (layer4rule2class1attribute0)
    		(22,23), #  has_match_attribute name (layer4rule2class1attribute0) -> match_attribute name (layer4rule2class1attribute0)
    		(9,24), # apply_class Function(layer4rule2class3) -> has_apply_attribute name (layer4rule2class3attribute0)
    		(24,25), #  has_apply_attribute name (layer4rule2class3attribute0) -> apply_attribute name (layer4rule2class3attribute0)
    		(26,27), #  equation of apply attribute name (layer4rule2class3attribute0) -> left_expr
    		(27,25), #  left_expr -> apply_attribute name (layer4rule2class3attribute0)
    		(26,28), #  equation of apply attribute name (layer4rule2class3attribute0) -> right_expr
    		(32,33), #  apply attribute concat name (layer4rule2class3attribute0) -> left has_args  
    		(33,35), #  left has_args -> term
    		(32,34), #  apply attribute concat name (layer4rule2class3attribute0) -> right has_args  
    		(34,23), #  right has_args -> term
    		(29,30), #  apply attribute concat name (layer4rule2class3attribute0) -> left has_args  
    		(30,21), #  left has_args -> term
    		(29,31), #  apply attribute concat name (layer4rule2class3attribute0) -> right has_args  
    		(31,32), #  right has_args -> term
    		(28,29), # right_expr --> term
        	(0,2), # matchmodel -> pairedwith
        	(2,1) # pairedwith -> applyModel
        ])
        
