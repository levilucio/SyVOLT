from core.himesis import Himesis
import cPickle as pickle
import uuid

class Hlayer1rule11(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule layer1rule11.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer1rule11, self).__init__(name='Hlayer1rule11', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        # TODO Levi, need some help here because I don't know where does 
        # this value come from.
        self["mm__"] = pickle.loads("""(lp1
S'HimesisMM'
p2
a.""")
        
        self["name"] = """layer1rule11"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule11')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule11matchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule11applymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule11pairedwith2')
        
    	# match class ClientServerInterface(layer1rule11class0) node
    	self.add_node()
    	self.vs[3]["name"] = """layer1rule11class0"""
        self.vs[3]["classtype"] = """ClientServerInterface"""
        self.vs[3]["mm__"] = """ClientServerInterface"""
        self.vs[3]["cardinality"] = """+"""
        #self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule11class0')
    	# match_contains node for class ClientServerInterface(layer1rule11class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        #self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule11class0matchcontains4')
    	# match class RequiredPort(layer1rule11class1) node
    	self.add_node()
    	self.vs[5]["name"] = """layer1rule11class1"""
        self.vs[5]["classtype"] = """RequiredPort"""
        self.vs[5]["mm__"] = """RequiredPort"""
        self.vs[5]["cardinality"] = """+"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule11class1')
    	# match_contains node for class RequiredPort(layer1rule11class1)
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        #self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule11class1matchcontains6')
        
        
    	# apply class TypeDef(layer1rule11class2) node
    	self.add_node()
    	self.vs[7]["name"] = """layer1rule11class2"""
        self.vs[7]["classtype"] = """TypeDef"""
        self.vs[7]["mm__"] = """TypeDef"""
        self.vs[7]["cardinality"] = """1"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule11class2')
    	# apply_contains node for class TypeDef(layer1rule11class2)
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        #self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule11class2applycontains8')
    	# apply class Member(layer1rule11class3) node
    	self.add_node()
    	self.vs[9]["name"] = """layer1rule11class3"""
        self.vs[9]["classtype"] = """Member"""
        self.vs[9]["mm__"] = """Member"""
        self.vs[9]["cardinality"] = """1"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule11class3')
    	# apply_contains node for class Member(layer1rule11class3)
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        #self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule11class3applycontains10')
    	# apply class PointerType(layer1rule11class4) node
    	self.add_node()
    	self.vs[11]["name"] = """layer1rule11class4"""
        self.vs[11]["classtype"] = """PointerType"""
        self.vs[11]["mm__"] = """PointerType"""
        self.vs[11]["cardinality"] = """1"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule11class4')
    	# apply_contains node for class PointerType(layer1rule11class4)
        self.add_node()
        self.vs[12]["mm__"] = """apply_contains"""
        #self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule11class4applycontains12')
    	# apply class TypeDefType(layer1rule11class5) node
    	self.add_node()
    	self.vs[13]["name"] = """layer1rule11class5"""
        self.vs[13]["classtype"] = """TypeDefType"""
        self.vs[13]["mm__"] = """TypeDefType"""
        self.vs[13]["cardinality"] = """1"""
        #self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule11class5')
    	# apply_contains node for class TypeDefType(layer1rule11class5)
        self.add_node()
        self.vs[14]["mm__"] = """apply_contains"""
        #self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule11class5applycontains14')
        
        
    	# match association RequiredPort--intf-->ClientServerInterface node
    	self.add_node()
    	self.vs[15]["associationType"] = """intf"""
        self.vs[15]["mm__"] = """directLink_S"""
        #self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule11class1assoc15layer1rule11class0')
        
    	# apply association Member--type-->PointerType node
    	self.add_node()
    	self.vs[16]["associationType"] = """type"""
        self.vs[16]["mm__"] = """directLink_T"""
        #self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule11class3assoc16layer1rule11class4')
    	# apply association PointerType--baseType-->TypeDefType node
    	self.add_node()
    	self.vs[17]["associationType"] = """baseType"""
        self.vs[17]["mm__"] = """directLink_T"""
        #self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule11class4assoc17layer1rule11class5')
    	# apply association TypeDefType--typeDef-->TypeDef node
    	self.add_node()
    	self.vs[18]["associationType"] = """typeDef"""
        self.vs[18]["mm__"] = """directLink_T"""
        #self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule11class5assoc18layer1rule11class2')
        
    	# backward association ClientServerInterface---->TypeDef node
    	self.add_node()
    	self.vs[19]["type"] = """ruleDef"""
        self.vs[19]["mm__"] = """backward_link"""
        #self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule11class0blink19layer1rule11class2')
    	# backward association RequiredPort---->Member node
    	self.add_node()
    	self.vs[20]["type"] = """ruleDef"""
        self.vs[20]["mm__"] = """backward_link"""
        #self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer1rule11class1blink20layer1rule11class3')
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
    		(0,4), # matchmodel -> match_contains
    		(4,3), # match_contains -> match_class ClientServerInterface(layer1rule11class0)
    		(0,6), # matchmodel -> match_contains
    		(6,5), # match_contains -> match_class RequiredPort(layer1rule11class1)
    		(1,8), # applymodel -> apply_contains
    		(8,7), # apply_contains -> apply_class TypeDef(layer1rule11class2)
    		(1,10), # applymodel -> apply_contains
    		(10,9), # apply_contains -> apply_class Member(layer1rule11class3)
    		(1,12), # applymodel -> apply_contains
    		(12,11), # apply_contains -> apply_class PointerType(layer1rule11class4)
    		(1,14), # applymodel -> apply_contains
    		(14,13), # apply_contains -> apply_class TypeDefType(layer1rule11class5)
    		(5,15), # match_class RequiredPort(layer1rule11class1) -> association intf
    		(15,3), # association intf  -> match_class ClientServerInterface(layer1rule11class0)
    		(9,16), # apply_class Member(layer1rule11class3) -> association type
    		(16,11), # association type  -> apply_class PointerType(layer1rule11class4)
    		(11,17), # apply_class PointerType(layer1rule11class4) -> association baseType
    		(17,13), # association baseType  -> apply_class TypeDefType(layer1rule11class5)
    		(13,18), # apply_class TypeDefType(layer1rule11class5) -> association typeDef
    		(18,7), # association typeDef  -> apply_class TypeDef(layer1rule11class2)
    		(7,19), # apply_class TypeDef(layer1rule11class2) -> backward_association
    		(19,3), #  backward_association -> apply_class ClientServerInterface(layer1rule11class0)
    		(9,20), # apply_class Member(layer1rule11class3) -> backward_association
    		(20,5), #  backward_association -> apply_class RequiredPort(layer1rule11class1)
        	(0,2), # matchmodel -> pairedwith
        	(2,1) # pairedwith -> applyModel
        ])
        
