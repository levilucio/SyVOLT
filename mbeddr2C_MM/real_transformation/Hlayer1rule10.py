from core.himesis import Himesis
import cPickle as pickle
import uuid

class Hlayer1rule10(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule layer1rule10.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer1rule10, self).__init__(name='Hlayer1rule10', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        # TODO Levi, need some help here because I don't know where does 
        # this value come from.
        self["mm__"] = pickle.loads("""(lp1
S'HimesisMM'
p2
a.""")
        
        self["name"] = """layer1rule10"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule10')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule10matchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule10applymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule10pairedwith2')
        
    	# match class AtomicComponent(layer1rule10class0) node
    	self.add_node()
    	self.vs[3]["name"] = """layer1rule10class0"""
        self.vs[3]["classtype"] = """AtomicComponent"""
        self.vs[3]["mm__"] = """AtomicComponent"""
        self.vs[3]["cardinality"] = """+"""
        #self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule10class0')
    	# match_contains node for class AtomicComponent(layer1rule10class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        #self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule10class0matchcontains4')
    	# match class RequiredPort(layer1rule10class1) node
    	self.add_node()
    	self.vs[5]["name"] = """layer1rule10class1"""
        self.vs[5]["classtype"] = """RequiredPort"""
        self.vs[5]["mm__"] = """RequiredPort"""
        self.vs[5]["cardinality"] = """+"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule10class1')
    	# match_contains node for class RequiredPort(layer1rule10class1)
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        #self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule10class1matchcontains6')
        
        
    	# apply class StructDeclaration(layer1rule10class2) node
    	self.add_node()
    	self.vs[7]["name"] = """layer1rule10class2"""
        self.vs[7]["classtype"] = """StructDeclaration"""
        self.vs[7]["mm__"] = """StructDeclaration"""
        self.vs[7]["cardinality"] = """1"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule10class2')
    	# apply_contains node for class StructDeclaration(layer1rule10class2)
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        #self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule10class2applycontains8')
    	# apply class Member(layer1rule10class3) node
    	self.add_node()
    	self.vs[9]["name"] = """layer1rule10class3"""
        self.vs[9]["classtype"] = """Member"""
        self.vs[9]["mm__"] = """Member"""
        self.vs[9]["cardinality"] = """1"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule10class3')
    	# apply_contains node for class Member(layer1rule10class3)
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        #self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule10class3applycontains10')
    	# apply class Member(layer1rule10class4) node
    	self.add_node()
    	self.vs[11]["name"] = """layer1rule10class4"""
        self.vs[11]["classtype"] = """Member"""
        self.vs[11]["mm__"] = """Member"""
        self.vs[11]["cardinality"] = """1"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule10class4')
    	# apply_contains node for class Member(layer1rule10class4)
        self.add_node()
        self.vs[12]["mm__"] = """apply_contains"""
        #self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule10class4applycontains12')
        
        
    	# match association AtomicComponent--contents-->RequiredPort node
    	self.add_node()
    	self.vs[13]["associationType"] = """contents"""
        self.vs[13]["mm__"] = """directLink_S"""
        #self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule10class0assoc13layer1rule10class1')
        
    	# apply association StructDeclaration--members-->Member node
    	self.add_node()
    	self.vs[14]["associationType"] = """members"""
        self.vs[14]["mm__"] = """directLink_T"""
        #self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule10class2assoc14layer1rule10class3')
    	# apply association StructDeclaration--members-->Member node
    	self.add_node()
    	self.vs[15]["associationType"] = """members"""
        self.vs[15]["mm__"] = """directLink_T"""
        #self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule10class2assoc15layer1rule10class4')
        
    	# backward association AtomicComponent---->StructDeclaration node
    	self.add_node()
    	self.vs[16]["type"] = """ruleDef"""
        self.vs[16]["mm__"] = """backward_link"""
        #self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule10class0blink16layer1rule10class2')
    	# backward association RequiredPort---->Member node
    	self.add_node()
    	self.vs[17]["type"] = """ruleDef"""
        self.vs[17]["mm__"] = """backward_link"""
        #self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule10class1blink17layer1rule10class3')
    	# backward association RequiredPort---->Member node
    	self.add_node()
    	self.vs[18]["type"] = """ruleDef"""
        self.vs[18]["mm__"] = """backward_link"""
        #self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule10class1blink18layer1rule10class4')
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
    		(0,4), # matchmodel -> match_contains
    		(4,3), # match_contains -> match_class AtomicComponent(layer1rule10class0)
    		(0,6), # matchmodel -> match_contains
    		(6,5), # match_contains -> match_class RequiredPort(layer1rule10class1)
    		(1,8), # applymodel -> apply_contains
    		(8,7), # apply_contains -> apply_class StructDeclaration(layer1rule10class2)
    		(1,10), # applymodel -> apply_contains
    		(10,9), # apply_contains -> apply_class Member(layer1rule10class3)
    		(1,12), # applymodel -> apply_contains
    		(12,11), # apply_contains -> apply_class Member(layer1rule10class4)
    		(3,13), # match_class AtomicComponent(layer1rule10class0) -> association contents
    		(13,5), # association contents  -> match_class RequiredPort(layer1rule10class1)
    		(7,14), # apply_class StructDeclaration(layer1rule10class2) -> association members
    		(14,9), # association members  -> apply_class Member(layer1rule10class3)
    		(7,15), # apply_class StructDeclaration(layer1rule10class2) -> association members
    		(15,11), # association members  -> apply_class Member(layer1rule10class4)
    		(7,16), # apply_class StructDeclaration(layer1rule10class2) -> backward_association
    		(16,3), #  backward_association -> apply_class AtomicComponent(layer1rule10class0)
    		(9,17), # apply_class Member(layer1rule10class3) -> backward_association
    		(17,5), #  backward_association -> apply_class RequiredPort(layer1rule10class1)
    		(11,18), # apply_class Member(layer1rule10class4) -> backward_association
    		(18,5), #  backward_association -> apply_class RequiredPort(layer1rule10class1)
        	(0,2), # matchmodel -> pairedwith
        	(2,1) # pairedwith -> applyModel
        ])
        
