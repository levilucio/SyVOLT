from core.himesis import Himesis
import cPickle as pickle
import uuid

class Hlayer1rule1(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule layer1rule1.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer1rule1, self).__init__(name='Hlayer1rule1', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        # TODO Levi, need some help here because I don't know where does 
        # this value come from.
        self["mm__"] = pickle.loads("""(lp1
S'HimesisMM'
p2
a.""")
        
        self["name"] = """layer1rule1"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule1')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule1matchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule1applymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule1pairedwith2')
        
    	# match class ClientServerInterface(layer1rule1class0) node
    	self.add_node()
    	self.vs[3]["name"] = """layer1rule1class0"""
        self.vs[3]["classtype"] = """ClientServerInterface"""
        self.vs[3]["mm__"] = """ClientServerInterface"""
        self.vs[3]["cardinality"] = """+"""
        #self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule1class0')
    	# match_contains node for class ClientServerInterface(layer1rule1class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        #self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule1class0matchcontains4')
    	# match class Operation(layer1rule1class1) node
    	self.add_node()
    	self.vs[5]["name"] = """layer1rule1class1"""
        self.vs[5]["classtype"] = """Operation"""
        self.vs[5]["mm__"] = """Operation"""
        self.vs[5]["cardinality"] = """+"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule1class1')
    	# match_contains node for class Operation(layer1rule1class1)
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        #self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule1class1matchcontains6')
        
        
    	# apply class StructDeclaration(layer1rule1class2) node
    	self.add_node()
    	self.vs[7]["name"] = """layer1rule1class2"""
        self.vs[7]["classtype"] = """StructDeclaration"""
        self.vs[7]["mm__"] = """StructDeclaration"""
        self.vs[7]["cardinality"] = """1"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule1class2')
    	# apply_contains node for class StructDeclaration(layer1rule1class2)
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        #self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule1class2applycontains8')
    	# apply class CFunctionPointerStructMember(layer1rule1class3) node
    	self.add_node()
    	self.vs[9]["name"] = """layer1rule1class3"""
        self.vs[9]["classtype"] = """CFunctionPointerStructMember"""
        self.vs[9]["mm__"] = """CFunctionPointerStructMember"""
        self.vs[9]["cardinality"] = """1"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule1class3')
    	# apply_contains node for class CFunctionPointerStructMember(layer1rule1class3)
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        #self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule1class3applycontains10')
        
        
    	# match association ClientServerInterface--contents-->Operation node
    	self.add_node()
    	self.vs[11]["associationType"] = """contents"""
        self.vs[11]["mm__"] = """directLink_S"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule1class0assoc11layer1rule1class1')
        
    	# apply association StructDeclaration--members-->CFunctionPointerStructMember node
    	self.add_node()
    	self.vs[12]["associationType"] = """members"""
        self.vs[12]["mm__"] = """directLink_T"""
        #self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule1class2assoc12layer1rule1class3')
        
    	# backward association Operation---->CFunctionPointerStructMember node
    	self.add_node()
    	self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["mm__"] = """backward_link"""
        #self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule1class1blink13layer1rule1class3')
    	# backward association ClientServerInterface---->StructDeclaration node
    	self.add_node()
    	self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["mm__"] = """backward_link"""
        #self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule1class0blink14layer1rule1class2')
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
    		(0,4), # matchmodel -> match_contains
    		(4,3), # match_contains -> match_class ClientServerInterface(layer1rule1class0)
    		(0,6), # matchmodel -> match_contains
    		(6,5), # match_contains -> match_class Operation(layer1rule1class1)
    		(1,8), # applymodel -> apply_contains
    		(8,7), # apply_contains -> apply_class StructDeclaration(layer1rule1class2)
    		(1,10), # applymodel -> apply_contains
    		(10,9), # apply_contains -> apply_class CFunctionPointerStructMember(layer1rule1class3)
    		(3,11), # match_class ClientServerInterface(layer1rule1class0) -> association contents
    		(11,5), # association contents  -> match_class Operation(layer1rule1class1)
    		(7,12), # apply_class StructDeclaration(layer1rule1class2) -> association members
    		(12,9), # association members  -> apply_class CFunctionPointerStructMember(layer1rule1class3)
    		(9,13), # apply_class CFunctionPointerStructMember(layer1rule1class3) -> backward_association
    		(13,5), #  backward_association -> apply_class Operation(layer1rule1class1)
    		(7,14), # apply_class StructDeclaration(layer1rule1class2) -> backward_association
    		(14,3), #  backward_association -> apply_class ClientServerInterface(layer1rule1class0)
        	(0,2), # matchmodel -> pairedwith
        	(2,1) # pairedwith -> applyModel
        ])
        
