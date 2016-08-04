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
        self.vs[2]["attr1"] = """Transition2QInstOUT"""
        
        # match class Transition() node
        self.add_node()
        
        self.vs[3]["mm__"] = """Transition""" 
        self.vs[3]["attr1"] = """+""" 
        # match class OUT2() node
        self.add_node()
        
        self.vs[4]["mm__"] = """OUT2""" 
        self.vs[4]["attr1"] = """1""" 
        # match class StateMachine() node
        self.add_node()
        
        self.vs[5]["mm__"] = """StateMachine""" 
        self.vs[5]["attr1"] = """1""" 
        # match class Vertex() node
        self.add_node()
        
        self.vs[6]["mm__"] = """Vertex""" 
        self.vs[6]["attr1"] = """1""" 
        
        
        # apply class Inst() node
        self.add_node()

        self.vs[7]["mm__"] = """Inst""" 
        self.vs[7]["attr1"] = """1"""
        # apply class Name() node
        self.add_node()

        self.vs[8]["mm__"] = """Name""" 
        self.vs[8]["attr1"] = """1"""
        
        
        # match association Transition--type-->OUT2 node
        self.add_node()
        self.vs[9]["attr1"] = """type"""
        self.vs[9]["mm__"] = """directLink_S"""
        # match association Transition--owningStateMachine-->StateMachine node
        self.add_node()
        self.vs[10]["attr1"] = """owningStateMachine"""
        self.vs[10]["mm__"] = """directLink_S"""
        # match association StateMachine--exitPoints-->Vertex node
        self.add_node()
        self.vs[11]["attr1"] = """exitPoints"""
        self.vs[11]["mm__"] = """directLink_S"""
        # match association Transition--dest-->Vertex node
        self.add_node()
        self.vs[12]["attr1"] = """dest"""
        self.vs[12]["mm__"] = """directLink_S"""
        
        # apply association Inst--channelNames-->Name node
        self.add_node()
        self.vs[13]["attr1"] = """channelNames"""
        self.vs[13]["mm__"] = """directLink_T"""
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class Transition()
                (0,4), # matchmodel -> match_class OUT2()
                (0,5), # matchmodel -> match_class StateMachine()
                (0,6), # matchmodel -> match_class Vertex()
                (1,7), # applymodel -> -> apply_class Inst()
                (1,8), # applymodel -> -> apply_class Name()
                (3,9), # match_class Transition() -> association type
                (9,4), # association type  -> match_class OUT2()
                (3,10), # match_class Transition() -> association owningStateMachine
                (10,5), # association owningStateMachine  -> match_class StateMachine()
                (5,11), # match_class StateMachine() -> association exitPoints
                (11,6), # association exitPoints  -> match_class Vertex()
                (3,12), # match_class Transition() -> association dest
                (12,6), # association dest  -> match_class Vertex()
                (7,13), # apply_class Inst() -> association channelNames
                (13,8), # association channelNames  -> apply_class Name()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((7,'name'),('concat',(('constant','B'),(6,'name')))), ((7,'__ApplyAttribute'),('constant','instfortrans')), ((8,'literal'),('constant','sh')), ]

        
