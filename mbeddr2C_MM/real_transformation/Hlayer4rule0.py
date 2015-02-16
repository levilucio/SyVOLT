from core.himesis import Himesis
import cPickle as pickle
import uuid

class Hlayer4rule0(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule layer4rule0.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer4rule0, self).__init__(name='Hlayer4rule0', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        # TODO Levi, need some help here because I don't know where does 
        # this value come from.
        self["mm__"] = pickle.loads("""(lp1
S'HimesisMM'
p2
a.""")
        
        self["name"] = """layer4rule0"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule0')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule0matchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule0applymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule0pairedwith2')
        
    	# match class ImplementationModule(layer4rule0class0) node
    	self.add_node()
    	self.vs[3]["name"] = """layer4rule0class0"""
        self.vs[3]["classtype"] = """ImplementationModule"""
        self.vs[3]["mm__"] = """ImplementationModule"""
        self.vs[3]["cardinality"] = """+"""
        #self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule0class0')
    	# match_contains node for class ImplementationModule(layer4rule0class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        #self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule0class0matchcontains4')
    	# match class InstanceConfiguration(layer4rule0class1) node
    	self.add_node()
    	self.vs[5]["name"] = """layer4rule0class1"""
        self.vs[5]["classtype"] = """InstanceConfiguration"""
        self.vs[5]["mm__"] = """InstanceConfiguration"""
        self.vs[5]["cardinality"] = """+"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule0class1')
    	# match_contains node for class InstanceConfiguration(layer4rule0class1)
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        #self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule0class1matchcontains6')
    	# match class ComponentInstance(layer4rule0class2) node
    	self.add_node()
    	self.vs[7]["name"] = """layer4rule0class2"""
        self.vs[7]["classtype"] = """ComponentInstance"""
        self.vs[7]["mm__"] = """ComponentInstance"""
        self.vs[7]["cardinality"] = """+"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule0class2')
    	# match_contains node for class ComponentInstance(layer4rule0class2)
        self.add_node()
        self.vs[8]["mm__"] = """match_contains"""
        #self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule0class2matchcontains8')
        
        
    	# apply class ImplementationModule(layer4rule0class3) node
    	self.add_node()
    	self.vs[9]["name"] = """layer4rule0class3"""
        self.vs[9]["classtype"] = """ImplementationModule"""
        self.vs[9]["mm__"] = """ImplementationModule"""
        self.vs[9]["cardinality"] = """1"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule0class3')
    	# apply_contains node for class ImplementationModule(layer4rule0class3)
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        #self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule0class3applycontains10')
    	# apply class Function(layer4rule0class4) node
    	self.add_node()
    	self.vs[11]["name"] = """layer4rule0class4"""
        self.vs[11]["classtype"] = """Function"""
        self.vs[11]["mm__"] = """Function"""
        self.vs[11]["cardinality"] = """1"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule0class4')
    	# apply_contains node for class Function(layer4rule0class4)
        self.add_node()
        self.vs[12]["mm__"] = """apply_contains"""
        #self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule0class4applycontains12')
    	# apply class VoidType(layer4rule0class5) node
    	self.add_node()
    	self.vs[13]["name"] = """layer4rule0class5"""
        self.vs[13]["classtype"] = """VoidType"""
        self.vs[13]["mm__"] = """VoidType"""
        self.vs[13]["cardinality"] = """1"""
        #self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule0class5')
    	# apply_contains node for class VoidType(layer4rule0class5)
        self.add_node()
        self.vs[14]["mm__"] = """apply_contains"""
        #self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule0class5applycontains14')
    	# apply class StatementList(layer4rule0class6) node
    	self.add_node()
    	self.vs[15]["name"] = """layer4rule0class6"""
        self.vs[15]["classtype"] = """StatementList"""
        self.vs[15]["mm__"] = """StatementList"""
        self.vs[15]["cardinality"] = """1"""
        #self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule0class6')
    	# apply_contains node for class StatementList(layer4rule0class6)
        self.add_node()
        self.vs[16]["mm__"] = """apply_contains"""
        #self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule0class6applycontains16')
        
        
    	# match association ImplementationModule--contents-->InstanceConfiguration node
    	self.add_node()
    	self.vs[17]["associationType"] = """contents"""
        self.vs[17]["mm__"] = """directLink_S"""
        #self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule0class0assoc17layer4rule0class1')
    	# match association InstanceConfiguration--contents-->ComponentInstance node
    	self.add_node()
    	self.vs[18]["associationType"] = """contents"""
        self.vs[18]["mm__"] = """directLink_S"""
        #self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule0class1assoc18layer4rule0class2')
        
    	# apply association ImplementationModule--contents-->Function node
    	self.add_node()
    	self.vs[19]["associationType"] = """contents"""
        self.vs[19]["mm__"] = """directLink_T"""
        #self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule0class3assoc19layer4rule0class4')
    	# apply association Function--type-->VoidType node
    	self.add_node()
    	self.vs[20]["associationType"] = """type"""
        self.vs[20]["mm__"] = """directLink_T"""
        #self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule0class4assoc20layer4rule0class5')
    	# apply association Function--body-->StatementList node
    	self.add_node()
    	self.vs[21]["associationType"] = """body"""
        self.vs[21]["mm__"] = """directLink_T"""
        #self.vs[21]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule0class4assoc21layer4rule0class6')
        
    	# backward association ImplementationModule---->ImplementationModule node
    	self.add_node()
    	self.vs[22]["type"] = """ruleDef"""
        self.vs[22]["mm__"] = """backward_link"""
        #self.vs[22]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule0class0blink22layer4rule0class3')
        
        
    	# has match attribute name(layer4rule0class0attribute0) node
    	self.add_node()
    	self.vs[23]["mm__"] = """hasAttribute_S"""
        #self.vs[23]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer4rule0class0attribute0')
    	# match attribute name(layer4rule0class0attribute0) node
    	self.add_node()
    	self.vs[24]["name"] = """name"""
        self.vs[24]["mm__"] = """Attribute"""
        self.vs[24]["Type"] = """'String'"""
        #self.vs[24]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule0class0attribute0')
    	# has match attribute name(layer4rule0class1attribute0) node
    	self.add_node()
    	self.vs[25]["mm__"] = """hasAttribute_S"""
        #self.vs[25]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer4rule0class1attribute0')
    	# match attribute name(layer4rule0class1attribute0) node
    	self.add_node()
    	self.vs[26]["name"] = """name"""
        self.vs[26]["mm__"] = """Attribute"""
        self.vs[26]["Type"] = """'String'"""
        #self.vs[26]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule0class1attribute0')
    	# has match attribute name(layer4rule0class2attribute0) node
    	self.add_node()
    	self.vs[27]["mm__"] = """hasAttribute_S"""
        #self.vs[27]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer4rule0class2attribute0')
    	# match attribute name(layer4rule0class2attribute0) node
    	self.add_node()
    	self.vs[28]["name"] = """name"""
        self.vs[28]["mm__"] = """Attribute"""
        self.vs[28]["Type"] = """'String'"""
        #self.vs[28]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule0class2attribute0')
        
        
    	# has apply attribute name(layer4rule0class4attribute0) node
    	self.add_node()
    	self.vs[29]["mm__"] = """hasAttribute_T"""
        #self.vs[29]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'haslayer4rule0class4attribute0')
    	# apply attribute name(layer4rule0class4attribute0) node
    	self.add_node()
    	self.vs[30]["name"] = """name"""
        self.vs[30]["mm__"] = """Attribute"""
        self.vs[30]["Type"] = """'String'"""
        #self.vs[30]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule0class4attribute0')
    	# apply attribute equation name(layer4rule0class4attribute0) node
    	self.add_node()
    	self.vs[31]["name"] = """eq_"""
        self.vs[31]["mm__"] = """Equation"""
        #self.vs[31]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Equationlayer4rule0class4attribute0')
    	# apply attribute equation left expr name(layer4rule0class4attribute0) node
    	self.add_node()
    	self.vs[32]["mm__"] = """leftExpr"""
        #self.vs[32]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExprlayer4rule0class4attribute0')
    	# apply attribute equation right expr name(layer4rule0class4attribute0) node
    	self.add_node()
    	self.vs[33]["mm__"] = """rightExpr"""
        #self.vs[33]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExprlayer4rule0class4attribute0')
    	# attribute concat name(layer4rule0class4attribute0) node
    	self.add_node()
    	self.vs[34]["name"] = """Concatlayer4rule0class4attribute034"""
        self.vs[34]["mm__"] = """Concat"""
        self.vs[34]["Type"] = """'String'"""
        #self.vs[34]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concatlayer4rule0class4attribute034')
    	# apply attribute concat has left args name(layer4rule0class4attribute0) node
        self.add_node()
    	self.vs[35]["mm__"] = """hasArgs"""
        #self.vs[35]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgslayer4rule0class4attribute035')
    	# apply attribute concat has right args name(layer4rule0class4attribute0) node
        self.add_node()
    	self.vs[36]["mm__"] = """hasArgs"""
        #self.vs[36]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgslayer4rule0class4attribute036')
    	# attribute concat name(layer4rule0class4attribute0) node
    	self.add_node()
    	self.vs[37]["name"] = """Concatlayer4rule0class4attribute037"""
        self.vs[37]["mm__"] = """Concat"""
        self.vs[37]["Type"] = """'String'"""
        #self.vs[37]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concatlayer4rule0class4attribute037')
    	# apply attribute concat has left args name(layer4rule0class4attribute0) node
        self.add_node()
    	self.vs[38]["mm__"] = """hasArgs"""
        #self.vs[38]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgslayer4rule0class4attribute038')
    	# apply attribute concat has right args name(layer4rule0class4attribute0) node
        self.add_node()
    	self.vs[39]["mm__"] = """hasArgs"""
        #self.vs[39]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgslayer4rule0class4attribute039')
    	# apply attribute atom name(layer4rule0class4attribute0) node
    	self.add_node()
    	self.vs[40]["name"] = """_"""
        self.vs[40]["mm__"] = """Constant"""
        self.vs[40]["Type"] = """'String'"""
        #self.vs[40]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atomlayer4rule0class4attribute040')
    	# attribute concat name(layer4rule0class4attribute0) node
    	self.add_node()
    	self.vs[41]["name"] = """Concatlayer4rule0class4attribute041"""
        self.vs[41]["mm__"] = """Concat"""
        self.vs[41]["Type"] = """'String'"""
        #self.vs[41]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concatlayer4rule0class4attribute041')
    	# apply attribute concat has left args name(layer4rule0class4attribute0) node
        self.add_node()
    	self.vs[42]["mm__"] = """hasArgs"""
        #self.vs[42]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgslayer4rule0class4attribute042')
    	# apply attribute concat has right args name(layer4rule0class4attribute0) node
        self.add_node()
    	self.vs[43]["mm__"] = """hasArgs"""
        #self.vs[43]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgslayer4rule0class4attribute043')
    	# attribute concat name(layer4rule0class4attribute0) node
    	self.add_node()
    	self.vs[44]["name"] = """Concatlayer4rule0class4attribute044"""
        self.vs[44]["mm__"] = """Concat"""
        self.vs[44]["Type"] = """'String'"""
        #self.vs[44]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concatlayer4rule0class4attribute044')
    	# apply attribute concat has left args name(layer4rule0class4attribute0) node
        self.add_node()
    	self.vs[45]["mm__"] = """hasArgs"""
        #self.vs[45]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgslayer4rule0class4attribute045')
    	# apply attribute concat has right args name(layer4rule0class4attribute0) node
        self.add_node()
    	self.vs[46]["mm__"] = """hasArgs"""
        #self.vs[46]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgslayer4rule0class4attribute046')
    	# apply attribute atom name(layer4rule0class4attribute0) node
    	self.add_node()
    	self.vs[47]["name"] = """_"""
        self.vs[47]["mm__"] = """Constant"""
        self.vs[47]["Type"] = """'String'"""
        #self.vs[47]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atomlayer4rule0class4attribute047')
    	# attribute concat name(layer4rule0class4attribute0) node
    	self.add_node()
    	self.vs[48]["name"] = """Concatlayer4rule0class4attribute048"""
        self.vs[48]["mm__"] = """Concat"""
        self.vs[48]["Type"] = """'String'"""
        #self.vs[48]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Concatlayer4rule0class4attribute048')
    	# apply attribute concat has left args name(layer4rule0class4attribute0) node
        self.add_node()
    	self.vs[49]["mm__"] = """hasArgs"""
        #self.vs[49]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgslayer4rule0class4attribute049')
    	# apply attribute concat has right args name(layer4rule0class4attribute0) node
        self.add_node()
    	self.vs[50]["mm__"] = """hasArgs"""
        #self.vs[50]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasRightArgslayer4rule0class4attribute050')
    	# apply attribute atom name(layer4rule0class4attribute0) node
    	self.add_node()
    	self.vs[51]["name"] = """__wire"""
        self.vs[51]["mm__"] = """Constant"""
        self.vs[51]["Type"] = """'String'"""
        #self.vs[51]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Atomlayer4rule0class4attribute051')
        
        
        # Add the edges
        self.add_edges([
    		(0,4), # matchmodel -> match_contains
    		(4,3), # match_contains -> match_class ImplementationModule(layer4rule0class0)
    		(0,6), # matchmodel -> match_contains
    		(6,5), # match_contains -> match_class InstanceConfiguration(layer4rule0class1)
    		(0,8), # matchmodel -> match_contains
    		(8,7), # match_contains -> match_class ComponentInstance(layer4rule0class2)
    		(1,10), # applymodel -> apply_contains
    		(10,9), # apply_contains -> apply_class ImplementationModule(layer4rule0class3)
    		(1,12), # applymodel -> apply_contains
    		(12,11), # apply_contains -> apply_class Function(layer4rule0class4)
    		(1,14), # applymodel -> apply_contains
    		(14,13), # apply_contains -> apply_class VoidType(layer4rule0class5)
    		(1,16), # applymodel -> apply_contains
    		(16,15), # apply_contains -> apply_class StatementList(layer4rule0class6)
    		(3,17), # match_class ImplementationModule(layer4rule0class0) -> association contents
    		(17,5), # association contents  -> match_class InstanceConfiguration(layer4rule0class1)
    		(5,18), # match_class InstanceConfiguration(layer4rule0class1) -> association contents
    		(18,7), # association contents  -> match_class ComponentInstance(layer4rule0class2)
    		(9,19), # apply_class ImplementationModule(layer4rule0class3) -> association contents
    		(19,11), # association contents  -> apply_class Function(layer4rule0class4)
    		(11,20), # apply_class Function(layer4rule0class4) -> association type
    		(20,13), # association type  -> apply_class VoidType(layer4rule0class5)
    		(11,21), # apply_class Function(layer4rule0class4) -> association body
    		(21,15), # association body  -> apply_class StatementList(layer4rule0class6)
    		(9,22), # apply_class ImplementationModule(layer4rule0class3) -> backward_association
    		(22,3), #  backward_association -> apply_class ImplementationModule(layer4rule0class0)
    		(3,23), # match_class ImplementationModule(layer4rule0class0) -> has_match_attribute name (layer4rule0class0attribute0)
    		(23,24), #  has_match_attribute name (layer4rule0class0attribute0) -> match_attribute name (layer4rule0class0attribute0)
    		(5,25), # match_class InstanceConfiguration(layer4rule0class1) -> has_match_attribute name (layer4rule0class1attribute0)
    		(25,26), #  has_match_attribute name (layer4rule0class1attribute0) -> match_attribute name (layer4rule0class1attribute0)
    		(7,27), # match_class ComponentInstance(layer4rule0class2) -> has_match_attribute name (layer4rule0class2attribute0)
    		(27,28), #  has_match_attribute name (layer4rule0class2attribute0) -> match_attribute name (layer4rule0class2attribute0)
    		(11,29), # apply_class Function(layer4rule0class4) -> has_apply_attribute name (layer4rule0class4attribute0)
    		(29,30), #  has_apply_attribute name (layer4rule0class4attribute0) -> apply_attribute name (layer4rule0class4attribute0)
    		(31,32), #  equation of apply attribute name (layer4rule0class4attribute0) -> left_expr
    		(32,30), #  left_expr -> apply_attribute name (layer4rule0class4attribute0)
    		(31,33), #  equation of apply attribute name (layer4rule0class4attribute0) -> right_expr
    		(48,49), #  apply attribute concat name (layer4rule0class4attribute0) -> left has_args  
    		(49,28), #  left has_args -> term
    		(48,50), #  apply attribute concat name (layer4rule0class4attribute0) -> right has_args  
    		(50,51), #  right has_args -> term
    		(44,45), #  apply attribute concat name (layer4rule0class4attribute0) -> left has_args  
    		(45,47), #  left has_args -> term
    		(44,46), #  apply attribute concat name (layer4rule0class4attribute0) -> right has_args  
    		(46,48), #  right has_args -> term
    		(41,42), #  apply attribute concat name (layer4rule0class4attribute0) -> left has_args  
    		(42,26), #  left has_args -> term
    		(41,43), #  apply attribute concat name (layer4rule0class4attribute0) -> right has_args  
    		(43,44), #  right has_args -> term
    		(37,38), #  apply attribute concat name (layer4rule0class4attribute0) -> left has_args  
    		(38,40), #  left has_args -> term
    		(37,39), #  apply attribute concat name (layer4rule0class4attribute0) -> right has_args  
    		(39,41), #  right has_args -> term
    		(34,35), #  apply attribute concat name (layer4rule0class4attribute0) -> left has_args  
    		(35,24), #  left has_args -> term
    		(34,36), #  apply attribute concat name (layer4rule0class4attribute0) -> right has_args  
    		(36,37), #  right has_args -> term
    		(33,34), # right_expr --> term
        	(0,2), # matchmodel -> pairedwith
        	(2,1) # pairedwith -> applyModel
        ])
        
