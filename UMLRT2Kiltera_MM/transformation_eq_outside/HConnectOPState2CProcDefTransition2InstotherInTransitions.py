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
        self.vs[2]["rulename"] = """ConnectOPState2CProcDefTransition2InstotherInTransitions"""
        
        # match class Transition() node
        self.add_node()
        self.vs[3]["name"] = """"""
        self.vs[3]["classtype"] = """Transition"""
        self.vs[3]["mm__"] = """Transition"""
        self.vs[3]["cardinality"] = """+"""
        # match_contains node for class Transition()
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        # match class IN1() node
        self.add_node()
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """IN1"""
        self.vs[5]["mm__"] = """IN1"""
        self.vs[5]["cardinality"] = """+"""
        # match_contains node for class IN1()
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        # match class State() node
        self.add_node()
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """State"""
        self.vs[7]["mm__"] = """State"""
        self.vs[7]["cardinality"] = """+"""
        # match_contains node for class State()
        self.add_node()
        self.vs[8]["mm__"] = """match_contains"""
        # match class Vertex() node
        self.add_node()
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """Vertex"""
        self.vs[9]["mm__"] = """Vertex"""
        self.vs[9]["cardinality"] = """+"""
        # match_contains node for class Vertex()
        self.add_node()
        self.vs[10]["mm__"] = """match_contains"""
        
        
        # apply class ConditionSet() node
        self.add_node()
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """ConditionSet"""
        self.vs[11]["mm__"] = """ConditionSet"""
        self.vs[11]["cardinality"] = """1"""
        # apply_contains node for class ConditionSet()
        self.add_node()
        self.vs[12]["mm__"] = """apply_contains"""
        # apply class ConditionBranch() node
        self.add_node()
        self.vs[13]["name"] = """"""
        self.vs[13]["classtype"] = """ConditionBranch"""
        self.vs[13]["mm__"] = """ConditionBranch"""
        self.vs[13]["cardinality"] = """1"""
        # apply_contains node for class ConditionBranch()
        self.add_node()
        self.vs[14]["mm__"] = """apply_contains"""
        # apply class Expr() node
        self.add_node()
        self.vs[15]["name"] = """"""
        self.vs[15]["classtype"] = """Expr"""
        self.vs[15]["mm__"] = """Expr"""
        self.vs[15]["cardinality"] = """1"""
        # apply_contains node for class Expr()
        self.add_node()
        self.vs[16]["mm__"] = """apply_contains"""
        # apply class Inst() node
        self.add_node()
        self.vs[17]["name"] = """"""
        self.vs[17]["classtype"] = """Inst"""
        self.vs[17]["mm__"] = """Inst"""
        self.vs[17]["cardinality"] = """1"""
        # apply_contains node for class Inst()
        self.add_node()
        self.vs[18]["mm__"] = """apply_contains"""
        
        
        # match association State--transitions-->Transition node
        self.add_node()
        self.vs[19]["associationType"] = """transitions"""
        self.vs[19]["mm__"] = """directLink_S"""
        # match association Transition--type-->IN1 node
        self.add_node()
        self.vs[20]["associationType"] = """type"""
        self.vs[20]["mm__"] = """directLink_S"""
        # match association Transition--src-->Vertex node
        self.add_node()
        self.vs[21]["associationType"] = """src"""
        self.vs[21]["mm__"] = """directLink_S"""
        
        # apply association ConditionSet--branches-->ConditionBranch node
        self.add_node()
        self.vs[22]["associationType"] = """branches"""
        self.vs[22]["mm__"] = """directLink_T"""
        # apply association ConditionBranch--if-->Expr node
        self.add_node()
        self.vs[23]["associationType"] = """if"""
        self.vs[23]["mm__"] = """directLink_T"""
        # apply association ConditionBranch--then-->Inst node
        self.add_node()
        self.vs[24]["associationType"] = """then"""
        self.vs[24]["mm__"] = """directLink_T"""
        
        # backward association State---->ConditionSet node
        self.add_node()
        self.vs[25]["type"] = """ruleDef"""
        self.vs[25]["mm__"] = """backward_link"""
        # backward association Transition---->Inst node
        self.add_node()
        self.vs[26]["type"] = """ruleDef"""
        self.vs[26]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class Transition()
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class IN1()
                (0,8), # matchmodel -> match_contains
                (8,7), # match_contains -> match_class State()
                (0,10), # matchmodel -> match_contains
                (10,9), # match_contains -> match_class Vertex()
                (1,12), # applymodel -> apply_contains
                (12,11), # apply_contains -> apply_class ConditionSet()
                (1,14), # applymodel -> apply_contains
                (14,13), # apply_contains -> apply_class ConditionBranch()
                (1,16), # applymodel -> apply_contains
                (16,15), # apply_contains -> apply_class Expr()
                (1,18), # applymodel -> apply_contains
                (18,17), # apply_contains -> apply_class Inst()
                (7,19), # match_class State() -> association transitions
                (19,3), # association transitions  -> match_class Transition()
                (3,20), # match_class Transition() -> association type
                (20,5), # association type  -> match_class IN1()
                (3,21), # match_class Transition() -> association src
                (21,9), # association src  -> match_class Vertex()
                (11,22), # apply_class ConditionSet() -> association branches
                (22,13), # association branches  -> apply_class ConditionBranch()
                (13,23), # apply_class ConditionBranch() -> association if
                (23,15), # association if  -> apply_class Expr()
                (13,24), # apply_class ConditionBranch() -> association then
                (24,17), # association then  -> apply_class Inst()
                (11,25), # apply_class ConditionSet() -> backward_association
                (25,7), #  backward_association -> apply_class State()
                (17,26), # apply_class Inst() -> backward_association
                (26,3), #  backward_association -> apply_class Transition()
		])
		
        # Add the equations
        self["equations"] = [((7,'isComposite'),('constant','true')), ((11,'__ApplyAttribute'),('constant','condsetcompstate')), ((15,'literal'),('concat',(('constant','enp=A'),('concat',((9,'name'),('constant','A')))))), ((17,'__ApplyAttribute'),('constant','instForInTrans')), ]
        
