from core.himesis import Himesis
import cPickle as pickle
import uuid

class Hlayer5rule2(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule layer5rule2.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer5rule2, self).__init__(name='Hlayer5rule2', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        # TODO Levi, need some help here because I don't know where does 
        # this value come from.
        self["mm__"] = pickle.loads("""(lp1
S'HimesisMM'
p2
a.""")
        
        self["name"] = """layer5rule2"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule2')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule2matchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule2applymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule2pairedwith2')
        
    	# match class InstanceConfiguration(layer5rule2class0) node
    	self.add_node()
    	self.vs[3]["name"] = """layer5rule2class0"""
        self.vs[3]["classtype"] = """InstanceConfiguration"""
        self.vs[3]["mm__"] = """InstanceConfiguration"""
        self.vs[3]["cardinality"] = """+"""
        #self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule2class0')
    	# match_contains node for class InstanceConfiguration(layer5rule2class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        #self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule2class0matchcontains4')
    	# match class ComponentInstance(layer5rule2class1) node
    	self.add_node()
    	self.vs[5]["name"] = """layer5rule2class1"""
        self.vs[5]["classtype"] = """ComponentInstance"""
        self.vs[5]["mm__"] = """ComponentInstance"""
        self.vs[5]["cardinality"] = """+"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule2class1')
    	# match_contains node for class ComponentInstance(layer5rule2class1)
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        #self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule2class1matchcontains6')
        
        
    	# apply class StatementList(layer5rule2class2) node
    	self.add_node()
    	self.vs[7]["name"] = """layer5rule2class2"""
        self.vs[7]["classtype"] = """StatementList"""
        self.vs[7]["mm__"] = """StatementList"""
        self.vs[7]["cardinality"] = """1"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule2class2')
    	# apply_contains node for class StatementList(layer5rule2class2)
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        #self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule2class2applycontains8')
    	# apply class FunctionPrototype(layer5rule2class3) node
    	self.add_node()
    	self.vs[9]["name"] = """layer5rule2class3"""
        self.vs[9]["classtype"] = """FunctionPrototype"""
        self.vs[9]["mm__"] = """FunctionPrototype"""
        self.vs[9]["cardinality"] = """1"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule2class3')
    	# apply_contains node for class FunctionPrototype(layer5rule2class3)
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        #self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule2class3applycontains10')
    	# apply class ExpressionStatement(layer5rule2class4) node
    	self.add_node()
    	self.vs[11]["name"] = """layer5rule2class4"""
        self.vs[11]["classtype"] = """ExpressionStatement"""
        self.vs[11]["mm__"] = """ExpressionStatement"""
        self.vs[11]["cardinality"] = """1"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule2class4')
    	# apply_contains node for class ExpressionStatement(layer5rule2class4)
        self.add_node()
        self.vs[12]["mm__"] = """apply_contains"""
        #self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule2class4applycontains12')
    	# apply class FunctionCall(layer5rule2class5) node
    	self.add_node()
    	self.vs[13]["name"] = """layer5rule2class5"""
        self.vs[13]["classtype"] = """FunctionCall"""
        self.vs[13]["mm__"] = """FunctionCall"""
        self.vs[13]["cardinality"] = """1"""
        #self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule2class5')
    	# apply_contains node for class FunctionCall(layer5rule2class5)
        self.add_node()
        self.vs[14]["mm__"] = """apply_contains"""
        #self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule2class5applycontains14')
        
        
    	# match association InstanceConfiguration--contents-->ComponentInstance node
    	self.add_node()
    	self.vs[15]["associationType"] = """contents"""
        self.vs[15]["mm__"] = """directLink_S"""
        #self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule2class0assoc15layer5rule2class1')
        
    	# apply association StatementList--statements-->ExpressionStatement node
    	self.add_node()
    	self.vs[16]["associationType"] = """statements"""
        self.vs[16]["mm__"] = """directLink_T"""
        #self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule2class2assoc16layer5rule2class4')
    	# apply association ExpressionStatement--expr-->FunctionCall node
    	self.add_node()
    	self.vs[17]["associationType"] = """expr"""
        self.vs[17]["mm__"] = """directLink_T"""
        #self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule2class4assoc17layer5rule2class5')
    	# apply association FunctionCall--function-->FunctionPrototype node
    	self.add_node()
    	self.vs[18]["associationType"] = """function"""
        self.vs[18]["mm__"] = """directLink_T"""
        #self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule2class5assoc18layer5rule2class3')
        
    	# backward association InstanceConfiguration---->StatementList node
    	self.add_node()
    	self.vs[19]["type"] = """ruleDef"""
        self.vs[19]["mm__"] = """backward_link"""
        #self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule2class0blink19layer5rule2class2')
    	# backward association ComponentInstance---->FunctionPrototype node
    	self.add_node()
    	self.vs[20]["type"] = """ruleDef"""
        self.vs[20]["mm__"] = """backward_link"""
        #self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer5rule2class1blink20layer5rule2class3')
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
    		(0,4), # matchmodel -> match_contains
    		(4,3), # match_contains -> match_class InstanceConfiguration(layer5rule2class0)
    		(0,6), # matchmodel -> match_contains
    		(6,5), # match_contains -> match_class ComponentInstance(layer5rule2class1)
    		(1,8), # applymodel -> apply_contains
    		(8,7), # apply_contains -> apply_class StatementList(layer5rule2class2)
    		(1,10), # applymodel -> apply_contains
    		(10,9), # apply_contains -> apply_class FunctionPrototype(layer5rule2class3)
    		(1,12), # applymodel -> apply_contains
    		(12,11), # apply_contains -> apply_class ExpressionStatement(layer5rule2class4)
    		(1,14), # applymodel -> apply_contains
    		(14,13), # apply_contains -> apply_class FunctionCall(layer5rule2class5)
    		(3,15), # match_class InstanceConfiguration(layer5rule2class0) -> association contents
    		(15,5), # association contents  -> match_class ComponentInstance(layer5rule2class1)
    		(7,16), # apply_class StatementList(layer5rule2class2) -> association statements
    		(16,11), # association statements  -> apply_class ExpressionStatement(layer5rule2class4)
    		(11,17), # apply_class ExpressionStatement(layer5rule2class4) -> association expr
    		(17,13), # association expr  -> apply_class FunctionCall(layer5rule2class5)
    		(13,18), # apply_class FunctionCall(layer5rule2class5) -> association function
    		(18,9), # association function  -> apply_class FunctionPrototype(layer5rule2class3)
    		(7,19), # apply_class StatementList(layer5rule2class2) -> backward_association
    		(19,3), #  backward_association -> apply_class InstanceConfiguration(layer5rule2class0)
    		(9,20), # apply_class FunctionPrototype(layer5rule2class3) -> backward_association
    		(20,5), #  backward_association -> apply_class ComponentInstance(layer5rule2class1)
        	(0,2), # matchmodel -> pairedwith
        	(2,1) # pairedwith -> applyModel
        ])
        
