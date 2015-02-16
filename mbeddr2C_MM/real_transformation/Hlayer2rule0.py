from core.himesis import Himesis
import cPickle as pickle
import uuid

class Hlayer2rule0(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule layer2rule0.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer2rule0, self).__init__(name='Hlayer2rule0', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        # TODO Levi, need some help here because I don't know where does 
        # this value come from.
        self["mm__"] = pickle.loads("""(lp1
S'HimesisMM'
p2
a.""")
        
        self["name"] = """layer2rule0"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer2rule0')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer2rule0matchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer2rule0applymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer2rule0pairedwith2')
        
    	# match class Operation(layer2rule0class0) node
    	self.add_node()
    	self.vs[3]["name"] = """layer2rule0class0"""
        self.vs[3]["classtype"] = """Operation"""
        self.vs[3]["mm__"] = """Operation"""
        self.vs[3]["cardinality"] = """+"""
        #self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer2rule0class0')
    	# match_contains node for class Operation(layer2rule0class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        #self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer2rule0class0matchcontains4')
        
        
    	# apply class PointerType(layer2rule0class1) node
    	self.add_node()
    	self.vs[5]["name"] = """layer2rule0class1"""
        self.vs[5]["classtype"] = """PointerType"""
        self.vs[5]["mm__"] = """PointerType"""
        self.vs[5]["cardinality"] = """1"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer2rule0class1')
    	# apply_contains node for class PointerType(layer2rule0class1)
        self.add_node()
        self.vs[6]["mm__"] = """apply_contains"""
        #self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer2rule0class1applycontains6')
    	# apply class FunctionRefType(layer2rule0class2) node
    	self.add_node()
    	self.vs[7]["name"] = """layer2rule0class2"""
        self.vs[7]["classtype"] = """FunctionRefType"""
        self.vs[7]["mm__"] = """FunctionRefType"""
        self.vs[7]["cardinality"] = """1"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer2rule0class2')
    	# apply_contains node for class FunctionRefType(layer2rule0class2)
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        #self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer2rule0class2applycontains8')
        
        
        
    	# apply association FunctionRefType--argTypes-->PointerType node
    	self.add_node()
    	self.vs[9]["associationType"] = """argTypes"""
        self.vs[9]["mm__"] = """directLink_T"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer2rule0class2assoc9layer2rule0class1')
        
    	# backward association Operation---->PointerType node
    	self.add_node()
    	self.vs[10]["type"] = """ruleDef"""
        self.vs[10]["mm__"] = """backward_link"""
        #self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer2rule0class0blink10layer2rule0class1')
    	# backward association Operation---->FunctionRefType node
    	self.add_node()
    	self.vs[11]["type"] = """ruleDef"""
        self.vs[11]["mm__"] = """backward_link"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer2rule0class0blink11layer2rule0class2')
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
    		(0,4), # matchmodel -> match_contains
    		(4,3), # match_contains -> match_class Operation(layer2rule0class0)
    		(1,6), # applymodel -> apply_contains
    		(6,5), # apply_contains -> apply_class PointerType(layer2rule0class1)
    		(1,8), # applymodel -> apply_contains
    		(8,7), # apply_contains -> apply_class FunctionRefType(layer2rule0class2)
    		(7,9), # apply_class FunctionRefType(layer2rule0class2) -> association argTypes
    		(9,5), # association argTypes  -> apply_class PointerType(layer2rule0class1)
    		(5,10), # apply_class PointerType(layer2rule0class1) -> backward_association
    		(10,3), #  backward_association -> apply_class Operation(layer2rule0class0)
    		(7,11), # apply_class FunctionRefType(layer2rule0class2) -> backward_association
    		(11,3), #  backward_association -> apply_class Operation(layer2rule0class0)
        	(0,2), # matchmodel -> pairedwith
        	(2,1) # pairedwith -> applyModel
        ])
        
