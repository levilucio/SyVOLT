from core.himesis import Himesis
import cPickle as pickle
import uuid

class HBuildCommunity(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the DSLTrans rule BuildCommunity.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HBuildCommunity, self).__init__(name='HBuildCommunity', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        # TODO Levi, need some help here because I don't know where does 
        # this value come from.
        self["mm__"] = pickle.loads("""(lp1
S'HimesisMM'
p2
a.""")
        
        self["name"] = """BuildCommunity"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'BuildCommunity')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        #self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'BuildCommunitymatchmodel0')
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        #self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'BuildCommunityapplymodel1')
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        #self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'BuildCommunitypairedwith2')
        
    	# match class HouseholdRoot() node
    	self.add_node()
    	self.vs[3]["name"] = """"""
        self.vs[3]["classtype"] = """HouseholdRoot"""
        self.vs[3]["mm__"] = """HouseholdRoot"""
        self.vs[3]["cardinality"] = """+"""
        #self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# match_contains node for class HouseholdRoot()
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        #self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'matchcontains4')
    	# match class Member() node
    	self.add_node()
    	self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """Member"""
        self.vs[5]["mm__"] = """Member"""
        self.vs[5]["cardinality"] = """+"""
        #self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# match_contains node for class Member()
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        #self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'matchcontains6')
        
        
    	# apply class CommunityRoot() node
    	self.add_node()
    	self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """CommunityRoot"""
        self.vs[7]["mm__"] = """CommunityRoot"""
        self.vs[7]["cardinality"] = """1"""
        #self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply_contains node for class CommunityRoot()
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        #self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains8')
    	# apply class Person() node
    	self.add_node()
    	self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """Person"""
        self.vs[9]["mm__"] = """Person"""
        self.vs[9]["cardinality"] = """1"""
        #self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
    	# apply_contains node for class Person()
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        #self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'applycontains10')
        
        
    	# match association HouseholdRoot---->Member node
    	self.add_node()
    	self.vs[11]["associationType"] = """"""
        self.vs[11]["mm__"] = """directLink_S"""
        #self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc11')
        
    	# apply association CommunityRoot--has-->Person node
    	self.add_node()
    	self.vs[12]["associationType"] = """has"""
        self.vs[12]["mm__"] = """directLink_T"""
        #self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc12')
        
    	# backward association HouseholdRoot---->CommunityRoot node
    	self.add_node()
    	self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["mm__"] = """backward_link"""
        #self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'blink13')
    	# backward association Member---->Person node
    	self.add_node()
    	self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["mm__"] = """backward_link"""
        #self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'blink14')
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
    		(0,4), # matchmodel -> match_contains
    		(4,3), # match_contains -> match_class HouseholdRoot()
    		(0,6), # matchmodel -> match_contains
    		(6,5), # match_contains -> match_class Member()
    		(1,8), # applymodel -> apply_contains
    		(8,7), # apply_contains -> apply_class CommunityRoot()
    		(1,10), # applymodel -> apply_contains
    		(10,9), # apply_contains -> apply_class Person()
    		(3,11), # match_class HouseholdRoot() -> association 
    		(11,5), # association   -> match_class Member()
    		(7,12), # apply_class CommunityRoot() -> association has
    		(12,9), # association has  -> apply_class Person()
    		(7,13), # apply_class CommunityRoot() -> backward_association
    		(13,3), #  backward_association -> apply_class HouseholdRoot()
    		(9,14), # apply_class Person() -> backward_association
    		(14,5), #  backward_association -> apply_class Member()
        	(0,2), # matchmodel -> pairedwith
        	(2,1) # pairedwith -> applyModel
        ])
        
