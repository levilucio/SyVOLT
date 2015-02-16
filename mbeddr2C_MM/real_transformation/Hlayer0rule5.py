from core.himesis import Himesis
import cPickle as pickle
import uuid

class Hlayer0rule5(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule layer0rule5.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer0rule5, self).__init__(name='Hlayer0rule5', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        # TODO Levi, need some help here because I don't know where does 
        # this value come from.
        self["mm__"] = pickle.loads("""(lp1
S'HimesisMM'
p2
a.""")
        
        self["name"] = """layer0rule5"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule5')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule5matchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule5applymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule5pairedwith2')
        
    	# match class Operation(layer0rule5class0) node
    	self.add_node()
    	self.vs[3]["name"] = """layer0rule5class0"""
        self.vs[3]["classtype"] = """Operation"""
        self.vs[3]["mm__"] = """Operation"""
        self.vs[3]["cardinality"] = """+"""
        #self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule5class0')
    	# match_contains node for class Operation(layer0rule5class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        #self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule5class0matchcontains4')
    	# match class ClientServerInterface(layer0rule5class1) node
    	self.add_node()
    	self.vs[5]["name"] = """layer0rule5class1"""
        self.vs[5]["classtype"] = """ClientServerInterface"""
        self.vs[5]["mm__"] = """ClientServerInterface"""
        self.vs[5]["cardinality"] = """+"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule5class1')
    	# match_contains node for class ClientServerInterface(layer0rule5class1)
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        #self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule5class1matchcontains6')
        
        
    	# apply class PointerType(layer0rule5class2) node
    	self.add_node()
    	self.vs[7]["name"] = """layer0rule5class2"""
        self.vs[7]["classtype"] = """PointerType"""
        self.vs[7]["mm__"] = """PointerType"""
        self.vs[7]["cardinality"] = """1"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule5class2')
    	# apply_contains node for class PointerType(layer0rule5class2)
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        #self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule5class2applycontains8')
    	# apply class VoidType(layer0rule5class3) node
    	self.add_node()
    	self.vs[9]["name"] = """layer0rule5class3"""
        self.vs[9]["classtype"] = """VoidType"""
        self.vs[9]["mm__"] = """VoidType"""
        self.vs[9]["cardinality"] = """1"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule5class3')
    	# apply_contains node for class VoidType(layer0rule5class3)
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        #self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule5class3applycontains10')
        
        
    	# match association ClientServerInterface--contents-->Operation node
    	self.add_node()
    	self.vs[11]["associationType"] = """contents"""
        self.vs[11]["mm__"] = """directLink_S"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule5class1assoc11layer0rule5class0')
        
    	# apply association PointerType--baseType-->VoidType node
    	self.add_node()
    	self.vs[12]["associationType"] = """baseType"""
        self.vs[12]["mm__"] = """directLink_T"""
        #self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer0rule5class2assoc12layer0rule5class3')
        
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
    		(0,4), # matchmodel -> match_contains
    		(4,3), # match_contains -> match_class Operation(layer0rule5class0)
    		(0,6), # matchmodel -> match_contains
    		(6,5), # match_contains -> match_class ClientServerInterface(layer0rule5class1)
    		(1,8), # applymodel -> apply_contains
    		(8,7), # apply_contains -> apply_class PointerType(layer0rule5class2)
    		(1,10), # applymodel -> apply_contains
    		(10,9), # apply_contains -> apply_class VoidType(layer0rule5class3)
    		(5,11), # match_class ClientServerInterface(layer0rule5class1) -> association contents
    		(11,3), # association contents  -> match_class Operation(layer0rule5class0)
    		(7,12), # apply_class PointerType(layer0rule5class2) -> association baseType
    		(12,9), # association baseType  -> apply_class VoidType(layer0rule5class3)
        	(0,2), # matchmodel -> pairedwith
        	(2,1) # pairedwith -> applyModel
        ])
        
