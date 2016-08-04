from core.himesis import Himesis
import uuid

class HConnectOPState2CProcDefTransition2InstotherInTransitions(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule ConnectOPState2CProcDefTransition2InstotherInTransitions.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HConnectOPState2CProcDefTransition2InstotherInTransitions, self).__init__(name='HConnectOPState2CProcDefTransition2InstotherInTransitions', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """ConnectOPState2CProcDefTransition2InstotherInTransitions"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConnectOPState2CProcDefTransition2InstotherInTransitions')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["attr1"] = """ConnectOPState2CProcDefTransition2InstotherInTransitions"""
        
        # match class Transition() node
        self.add_node()
        
        self.vs[3]["mm__"] = """Transition""" 
        self.vs[3]["attr1"] = """+""" 
        # match class IN1() node
        self.add_node()
        
        self.vs[4]["mm__"] = """IN1""" 
        self.vs[4]["attr1"] = """+""" 
        # match class State() node
        self.add_node()
        
        self.vs[5]["mm__"] = """State""" 
        self.vs[5]["attr1"] = """+""" 
        # match class Vertex() node
        self.add_node()
        
        self.vs[6]["mm__"] = """Vertex""" 
        self.vs[6]["attr1"] = """+""" 
        
        
        # apply class ConditionSet() node
        self.add_node()

        self.vs[7]["mm__"] = """ConditionSet""" 
        self.vs[7]["attr1"] = """1"""
        # apply class ConditionBranch() node
        self.add_node()

        self.vs[8]["mm__"] = """ConditionBranch""" 
        self.vs[8]["attr1"] = """1"""
        # apply class Expr() node
        self.add_node()

        self.vs[9]["mm__"] = """Expr""" 
        self.vs[9]["attr1"] = """1"""
        # apply class Inst() node
        self.add_node()

        self.vs[10]["mm__"] = """Inst""" 
        self.vs[10]["attr1"] = """1"""
        
        
        # match association State--transitions-->Transition node
        self.add_node()
        self.vs[11]["attr1"] = """transitions"""
        self.vs[11]["mm__"] = """directLink_S"""
        # match association Transition--type-->IN1 node
        self.add_node()
        self.vs[12]["attr1"] = """type"""
        self.vs[12]["mm__"] = """directLink_S"""
        # match association Transition--src-->Vertex node
        self.add_node()
        self.vs[13]["attr1"] = """src"""
        self.vs[13]["mm__"] = """directLink_S"""
        
        # apply association ConditionSet--branches-->ConditionBranch node
        self.add_node()
        self.vs[14]["attr1"] = """branches"""
        self.vs[14]["mm__"] = """directLink_T"""
        # apply association ConditionBranch--if-->Expr node
        self.add_node()
        self.vs[15]["attr1"] = """if"""
        self.vs[15]["mm__"] = """directLink_T"""
        # apply association ConditionBranch--then-->Inst node
        self.add_node()
        self.vs[16]["attr1"] = """then"""
        self.vs[16]["mm__"] = """directLink_T"""
        
        # backward association State---->ConditionSet node
        self.add_node()

        self.vs[17]["mm__"] = """backward_link"""
        # backward association Transition---->Inst node
        self.add_node()

        self.vs[18]["mm__"] = """backward_link"""
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class Transition()
                (0,4), # matchmodel -> match_class IN1()
                (0,5), # matchmodel -> match_class State()
                (0,6), # matchmodel -> match_class Vertex()
                (1,7), # applymodel -> -> apply_class ConditionSet()
                (1,8), # applymodel -> -> apply_class ConditionBranch()
                (1,9), # applymodel -> -> apply_class Expr()
                (1,10), # applymodel -> -> apply_class Inst()
                (5,11), # match_class State() -> association transitions
                (11,3), # association transitions  -> match_class Transition()
                (3,12), # match_class Transition() -> association type
                (12,4), # association type  -> match_class IN1()
                (3,13), # match_class Transition() -> association src
                (13,6), # association src  -> match_class Vertex()
                (7,14), # apply_class ConditionSet() -> association branches
                (14,8), # association branches  -> apply_class ConditionBranch()
                (8,15), # apply_class ConditionBranch() -> association if
                (15,9), # association if  -> apply_class Expr()
                (8,16), # apply_class ConditionBranch() -> association then
                (16,10), # association then  -> apply_class Inst()
                (7,17), # apply_class ConditionSet() -> backward_association
                (17,5), #  backward_association -> apply_class State()
                (10,18), # apply_class Inst() -> backward_association
                (18,3), #  backward_association -> apply_class Transition()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((5,'isComposite'),('constant','true')), ((7,'__ApplyAttribute'),('constant','condsetcompstate')), ((9,'literal'),('concat',(('constant','enp=A'),('concat',((6,'name'),('constant','A')))))), ((10,'__ApplyAttribute'),('constant','instForInTrans')), ]

        
