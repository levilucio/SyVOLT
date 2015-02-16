from core.himesis import Himesis
import cPickle as pickle
import uuid

class Hlayer1rule4(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule layer1rule4.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer1rule4, self).__init__(name='Hlayer1rule4', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        # TODO Levi, need some help here because I don't know where does 
        # this value come from.
        self["mm__"] = pickle.loads("""(lp1
S'HimesisMM'
p2
a.""")
        
        self["name"] = """layer1rule4"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule4')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule4matchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule4applymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule4pairedwith2')
        
    	# match class Operation(layer1rule4class0) node
    	self.add_node()
    	self.vs[3]["name"] = """layer1rule4class0"""
        self.vs[3]["classtype"] = """Operation"""
        self.vs[3]["mm__"] = """Operation"""
        self.vs[3]["cardinality"] = """+"""
        #self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule4class0')
    	# match_contains node for class Operation(layer1rule4class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        #self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule4class0matchcontains4')
    	# match class OperationParameter(layer1rule4class1) node
    	self.add_node()
    	self.vs[5]["name"] = """layer1rule4class1"""
        self.vs[5]["classtype"] = """OperationParameter"""
        self.vs[5]["mm__"] = """OperationParameter"""
        self.vs[5]["cardinality"] = """+"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule4class1')
    	# match_contains node for class OperationParameter(layer1rule4class1)
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        #self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule4class1matchcontains6')
    	# match class StringType(layer1rule4class2) node
    	self.add_node()
    	self.vs[7]["name"] = """layer1rule4class2"""
        self.vs[7]["classtype"] = """StringType"""
        self.vs[7]["mm__"] = """StringType"""
        self.vs[7]["cardinality"] = """+"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule4class2')
    	# match_contains node for class StringType(layer1rule4class2)
        self.add_node()
        self.vs[8]["mm__"] = """match_contains"""
        #self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule4class2matchcontains8')
        
        
    	# apply class FunctionRefType(layer1rule4class3) node
    	self.add_node()
    	self.vs[9]["name"] = """layer1rule4class3"""
        self.vs[9]["classtype"] = """FunctionRefType"""
        self.vs[9]["mm__"] = """FunctionRefType"""
        self.vs[9]["cardinality"] = """1"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule4class3')
    	# apply_contains node for class FunctionRefType(layer1rule4class3)
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        #self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule4class3applycontains10')
    	# apply class StringType(layer1rule4class4) node
    	self.add_node()
    	self.vs[11]["name"] = """layer1rule4class4"""
        self.vs[11]["classtype"] = """StringType"""
        self.vs[11]["mm__"] = """StringType"""
        self.vs[11]["cardinality"] = """1"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule4class4')
    	# apply_contains node for class StringType(layer1rule4class4)
        self.add_node()
        self.vs[12]["mm__"] = """apply_contains"""
        #self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule4class4applycontains12')
        
        
    	# match association Operation--parameters-->OperationParameter node
    	self.add_node()
    	self.vs[13]["associationType"] = """parameters"""
        self.vs[13]["mm__"] = """directLink_S"""
        #self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule4class0assoc13layer1rule4class1')
    	# match association OperationParameter--type-->StringType node
    	self.add_node()
    	self.vs[14]["associationType"] = """type"""
        self.vs[14]["mm__"] = """directLink_S"""
        #self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule4class1assoc14layer1rule4class2')
        
    	# apply association FunctionRefType--argTypes-->StringType node
    	self.add_node()
    	self.vs[15]["associationType"] = """argTypes"""
        self.vs[15]["mm__"] = """directLink_T"""
        #self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule4class3assoc15layer1rule4class4')
        
    	# backward association StringType---->StringType node
    	self.add_node()
    	self.vs[16]["type"] = """ruleDef"""
        self.vs[16]["mm__"] = """backward_link"""
        #self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule4class2blink16layer1rule4class4')
    	# backward association Operation---->FunctionRefType node
    	self.add_node()
    	self.vs[17]["type"] = """ruleDef"""
        self.vs[17]["mm__"] = """backward_link"""
        #self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule4class0blink17layer1rule4class3')
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
    		(0,4), # matchmodel -> match_contains
    		(4,3), # match_contains -> match_class Operation(layer1rule4class0)
    		(0,6), # matchmodel -> match_contains
    		(6,5), # match_contains -> match_class OperationParameter(layer1rule4class1)
    		(0,8), # matchmodel -> match_contains
    		(8,7), # match_contains -> match_class StringType(layer1rule4class2)
    		(1,10), # applymodel -> apply_contains
    		(10,9), # apply_contains -> apply_class FunctionRefType(layer1rule4class3)
    		(1,12), # applymodel -> apply_contains
    		(12,11), # apply_contains -> apply_class StringType(layer1rule4class4)
    		(3,13), # match_class Operation(layer1rule4class0) -> association parameters
    		(13,5), # association parameters  -> match_class OperationParameter(layer1rule4class1)
    		(5,14), # match_class OperationParameter(layer1rule4class1) -> association type
    		(14,7), # association type  -> match_class StringType(layer1rule4class2)
    		(9,15), # apply_class FunctionRefType(layer1rule4class3) -> association argTypes
    		(15,11), # association argTypes  -> apply_class StringType(layer1rule4class4)
    		(11,16), # apply_class StringType(layer1rule4class4) -> backward_association
    		(16,7), #  backward_association -> apply_class StringType(layer1rule4class2)
    		(9,17), # apply_class FunctionRefType(layer1rule4class3) -> backward_association
    		(17,3), #  backward_association -> apply_class Operation(layer1rule4class0)
        	(0,2), # matchmodel -> pairedwith
        	(2,1) # pairedwith -> applyModel
        ])
        
