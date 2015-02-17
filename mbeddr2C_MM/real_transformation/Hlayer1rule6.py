from core.himesis import Himesis
import cPickle as pickle
import uuid

class Hlayer1rule6(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule layer1rule6.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer1rule6, self).__init__(name='Hlayer1rule6', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        # TODO Levi, need some help here because I don't know where does 
        # this value come from.
        self["mm__"] = pickle.loads("""(lp1
S'HimesisMM'
p2
a.""")
        
        self["name"] = """layer1rule6"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule6')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule6matchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule6applymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule6pairedwith2')
        
    	# match class ClientServerInterface(layer1rule6class0) node
    	self.add_node()
    	self.vs[3]["name"] = """layer1rule6class0"""
        self.vs[3]["classtype"] = """ClientServerInterface"""
        self.vs[3]["mm__"] = """ClientServerInterface"""
        self.vs[3]["cardinality"] = """+"""
        #self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule6class0')
    	# match_contains node for class ClientServerInterface(layer1rule6class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        #self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule6class0matchcontains4')
        
        
    	# apply class StructDeclaration(layer1rule6class1) node
    	self.add_node()
    	self.vs[5]["name"] = """layer1rule6class1"""
        self.vs[5]["classtype"] = """StructDeclaration"""
        self.vs[5]["mm__"] = """StructDeclaration"""
        self.vs[5]["cardinality"] = """1"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule6class1')
    	# apply_contains node for class StructDeclaration(layer1rule6class1)
        self.add_node()
        self.vs[6]["mm__"] = """apply_contains"""
        #self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule6class1applycontains6')
    	# apply class StructType(layer1rule6class2) node
    	self.add_node()
    	self.vs[7]["name"] = """layer1rule6class2"""
        self.vs[7]["classtype"] = """StructType"""
        self.vs[7]["mm__"] = """StructType"""
        self.vs[7]["cardinality"] = """1"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule6class2')
    	# apply_contains node for class StructType(layer1rule6class2)
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        #self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule6class2applycontains8')
        
        
        
    	# apply association StructType--struct-->StructDeclaration node
    	self.add_node()
    	self.vs[9]["associationType"] = """struct"""
        self.vs[9]["mm__"] = """directLink_T"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule6class2assoc9layer1rule6class1')
        
    	# backward association ClientServerInterface---->StructType node
    	self.add_node()
    	self.vs[10]["type"] = """ruleDef"""
        self.vs[10]["mm__"] = """backward_link"""
        #self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule6class0blink10layer1rule6class2')
    	# backward association ClientServerInterface---->StructDeclaration node
    	self.add_node()
    	self.vs[11]["type"] = """ruleDef"""
        self.vs[11]["mm__"] = """backward_link"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule6class0blink11layer1rule6class1')
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
    		(0,4), # matchmodel -> match_contains
    		(4,3), # match_contains -> match_class ClientServerInterface(layer1rule6class0)
    		(1,6), # applymodel -> apply_contains
    		(6,5), # apply_contains -> apply_class StructDeclaration(layer1rule6class1)
    		(1,8), # applymodel -> apply_contains
    		(8,7), # apply_contains -> apply_class StructType(layer1rule6class2)
    		(7,9), # apply_class StructType(layer1rule6class2) -> association struct
    		(9,5), # association struct  -> apply_class StructDeclaration(layer1rule6class1)
    		(7,10), # apply_class StructType(layer1rule6class2) -> backward_association
    		(10,3), #  backward_association -> apply_class ClientServerInterface(layer1rule6class0)
    		(5,11), # apply_class StructDeclaration(layer1rule6class1) -> backward_association
    		(11,3), #  backward_association -> apply_class ClientServerInterface(layer1rule6class0)
        	(0,2), # matchmodel -> pairedwith
        	(2,1) # pairedwith -> applyModel
        ])
        