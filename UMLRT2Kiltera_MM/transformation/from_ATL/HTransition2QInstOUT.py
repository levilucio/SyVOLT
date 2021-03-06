from core.himesis import Himesis
import uuid

class HTransition2QInstOUT(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule Transition2QInstOUT.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HTransition2QInstOUT, self).__init__(name='HTransition2QInstOUT', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """Transition2QInstOUT"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Transition2QInstOUT')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
 
        
        # match class Transition() node
        self.add_node()

        self.vs[3]["mm__"] = """Transition""" 
        self.vs[3]["attr1"] = """+""" 
        # match_contains node for class Transition()
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        # match class Vertex() node
        self.add_node()

        self.vs[5]["mm__"] = """Vertex""" 
        self.vs[5]["attr1"] = """1""" 
        # match_contains node for class Vertex()
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        # match class OUT2() node
        self.add_node()

        self.vs[7]["mm__"] = """OUT2""" 
        self.vs[7]["attr1"] = """1""" 
        # match_contains node for class OUT2()
        self.add_node()
        self.vs[8]["mm__"] = """match_contains"""
        # match class StateMachine() node
        self.add_node()

        self.vs[9]["mm__"] = """StateMachine""" 
        self.vs[9]["attr1"] = """1""" 
        # match_contains node for class StateMachine()
        self.add_node()
        self.vs[10]["mm__"] = """match_contains"""
        
        
        # apply class Inst() node
        self.add_node()

        self.vs[11]["mm__"] = """Inst""" 
        self.vs[11]["attr1"] = """1"""
        # apply_contains node for class Inst()
        self.add_node()
        self.vs[12]["mm__"] = """apply_contains"""
        # apply class Name() node
        self.add_node()

        self.vs[13]["mm__"] = """Name""" 
        self.vs[13]["attr1"] = """1"""
        # apply_contains node for class Name()
        self.add_node()
        self.vs[14]["mm__"] = """apply_contains"""
        
        
        # match association Transition--type-->OUT2 node
        self.add_node()
        self.vs[15]["attr1"] = """type"""
        self.vs[15]["mm__"] = """directLink_S"""
        # match association Transition--owningStateMachine-->StateMachine node
        self.add_node()
        self.vs[16]["attr1"] = """owningStateMachine"""
        self.vs[16]["mm__"] = """directLink_S"""
        # match association StateMachine--exitPoints-->Vertex node
        self.add_node()
        self.vs[17]["attr1"] = """exitPoints"""
        self.vs[17]["mm__"] = """directLink_S"""
        # match association Transition--dest-->Vertex node
        self.add_node()
        self.vs[18]["attr1"] = """dest"""
        self.vs[18]["mm__"] = """directLink_S"""
        
        # apply association Inst--channelNames-->Name node
        self.add_node()
        self.vs[19]["attr1"] = """channelNames"""
        self.vs[19]["mm__"] = """directLink_T"""
        
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class Transition()
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class Vertex()
                (0,8), # matchmodel -> match_contains
                (8,7), # match_contains -> match_class OUT2()
                (0,10), # matchmodel -> match_contains
                (10,9), # match_contains -> match_class StateMachine()
                (1,12), # applymodel -> apply_contains
                (12,11), # apply_contains -> apply_class Inst()
                (1,14), # applymodel -> apply_contains
                (14,13), # apply_contains -> apply_class Name()
                (3,15), # match_class Transition() -> association type
                (15,7), # association type  -> match_class OUT2()
                (3,16), # match_class Transition() -> association owningStateMachine
                (16,9), # association owningStateMachine  -> match_class StateMachine()
                (9,17), # match_class StateMachine() -> association exitPoints
                (17,5), # association exitPoints  -> match_class Vertex()
                (3,18), # match_class Transition() -> association dest
                (18,5), # association dest  -> match_class Vertex()
                (11,19), # apply_class Inst() -> association channelNames
                (19,13), # association channelNames  -> apply_class Name()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((11,'name'),('concat',(('constant','B'),(5,'name')))), ((11,'ApplyAttribute'),('constant','solveRef')), ((13,'literal'),('constant','sh')), ]

        
