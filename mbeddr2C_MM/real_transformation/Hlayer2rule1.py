from core.himesis import Himesis
import cPickle as pickle
import uuid

class Hlayer2rule1(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule layer2rule1.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer2rule1, self).__init__(name='Hlayer2rule1', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        # TODO Levi, need some help here because I don't know where does 
        # this value come from.
        self["mm__"] = pickle.loads("""(lp1
S'HimesisMM'
p2
a.""")
        
        self["name"] = """layer2rule1"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer2rule1')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer2rule1matchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer2rule1applymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer2rule1pairedwith2')
        
    	# match class StringType(layer2rule1class0) node
    	self.add_node()
    	self.vs[3]["name"] = """layer2rule1class0"""
        self.vs[3]["classtype"] = """StringType"""
        self.vs[3]["mm__"] = """StringType"""
        self.vs[3]["cardinality"] = """+"""
        #self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer2rule1class0')
    	# match_contains node for class StringType(layer2rule1class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        #self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer2rule1class0matchcontains4')
    	# match class OperationParameter(layer2rule1class1) node
    	self.add_node()
    	self.vs[5]["name"] = """layer2rule1class1"""
        self.vs[5]["classtype"] = """OperationParameter"""
        self.vs[5]["mm__"] = """OperationParameter"""
        self.vs[5]["cardinality"] = """+"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer2rule1class1')
    	# match_contains node for class OperationParameter(layer2rule1class1)
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        #self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer2rule1class1matchcontains6')
        
        
    	# apply class StringType(layer2rule1class2) node
    	self.add_node()
    	self.vs[7]["name"] = """layer2rule1class2"""
        self.vs[7]["classtype"] = """StringType"""
        self.vs[7]["mm__"] = """StringType"""
        self.vs[7]["cardinality"] = """1"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer2rule1class2')
    	# apply_contains node for class StringType(layer2rule1class2)
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        #self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer2rule1class2applycontains8')
    	# apply class Argument(layer2rule1class3) node
    	self.add_node()
    	self.vs[9]["name"] = """layer2rule1class3"""
        self.vs[9]["classtype"] = """Argument"""
        self.vs[9]["mm__"] = """Argument"""
        self.vs[9]["cardinality"] = """1"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer2rule1class3')
    	# apply_contains node for class Argument(layer2rule1class3)
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        #self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer2rule1class3applycontains10')
        
        
    	# match association OperationParameter--type-->StringType node
    	self.add_node()
    	self.vs[11]["associationType"] = """type"""
        self.vs[11]["mm__"] = """directLink_S"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer2rule1class1assoc11layer2rule1class0')
        
    	# apply association Argument--type-->StringType node
    	self.add_node()
    	self.vs[12]["associationType"] = """type"""
        self.vs[12]["mm__"] = """directLink_T"""
        #self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer2rule1class3assoc12layer2rule1class2')
        
    	# backward association OperationParameter---->Argument node
    	self.add_node()
    	self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["mm__"] = """backward_link"""
        #self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer2rule1class1blink13layer2rule1class3')
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
    		(0,4), # matchmodel -> match_contains
    		(4,3), # match_contains -> match_class StringType(layer2rule1class0)
    		(0,6), # matchmodel -> match_contains
    		(6,5), # match_contains -> match_class OperationParameter(layer2rule1class1)
    		(1,8), # applymodel -> apply_contains
    		(8,7), # apply_contains -> apply_class StringType(layer2rule1class2)
    		(1,10), # applymodel -> apply_contains
    		(10,9), # apply_contains -> apply_class Argument(layer2rule1class3)
    		(5,11), # match_class OperationParameter(layer2rule1class1) -> association type
    		(11,3), # association type  -> match_class StringType(layer2rule1class0)
    		(9,12), # apply_class Argument(layer2rule1class3) -> association type
    		(12,7), # association type  -> apply_class StringType(layer2rule1class2)
    		(9,13), # apply_class Argument(layer2rule1class3) -> backward_association
    		(13,5), #  backward_association -> apply_class OperationParameter(layer2rule1class1)
        	(0,2), # matchmodel -> pairedwith
        	(2,1) # pairedwith -> applyModel
        ])
        
