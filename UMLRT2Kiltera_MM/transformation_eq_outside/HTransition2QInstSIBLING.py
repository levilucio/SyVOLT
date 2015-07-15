from core.himesis import Himesis
import uuid

class HTransition2QInstSIBLING(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule Transition2QInstSIBLING.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HTransition2QInstSIBLING, self).__init__(name='HTransition2QInstSIBLING', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """Transition2QInstSIBLING"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'Transition2QInstSIBLING')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["rulename"] = """Transition2QInstSIBLING"""
        
        # match class Transition() node
        self.add_node()
        self.vs[3]["name"] = """"""
        self.vs[3]["classtype"] = """Transition"""
        self.vs[3]["mm__"] = """Transition"""
        self.vs[3]["cardinality"] = """+"""
        # match_contains node for class Transition()
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        # match class Vertex() node
        self.add_node()
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """Vertex"""
        self.vs[5]["mm__"] = """Vertex"""
        self.vs[5]["cardinality"] = """1"""
        # match_contains node for class Vertex()
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        # match class SIBLING0() node
        self.add_node()
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """SIBLING0"""
        self.vs[7]["mm__"] = """SIBLING0"""
        self.vs[7]["cardinality"] = """1"""
        # match_contains node for class SIBLING0()
        self.add_node()
        self.vs[8]["mm__"] = """match_contains"""
        # match class StateMachine() node
        self.add_node()
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """StateMachine"""
        self.vs[9]["mm__"] = """StateMachine"""
        self.vs[9]["cardinality"] = """1"""
        # match_contains node for class StateMachine()
        self.add_node()
        self.vs[10]["mm__"] = """match_contains"""
        
        
        # apply class Inst() node
        self.add_node()
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """Inst"""
        self.vs[11]["mm__"] = """Inst"""
        self.vs[11]["cardinality"] = """1"""
        # apply_contains node for class Inst()
        self.add_node()
        self.vs[12]["mm__"] = """apply_contains"""
        # apply class Name() node
        self.add_node()
        self.vs[13]["name"] = """"""
        self.vs[13]["classtype"] = """Name"""
        self.vs[13]["mm__"] = """Name"""
        self.vs[13]["cardinality"] = """1"""
        # apply_contains node for class Name()
        self.add_node()
        self.vs[14]["mm__"] = """apply_contains"""
        # apply class Name() node
        self.add_node()
        self.vs[15]["name"] = """"""
        self.vs[15]["classtype"] = """Name"""
        self.vs[15]["mm__"] = """Name"""
        self.vs[15]["cardinality"] = """1"""
        # apply_contains node for class Name()
        self.add_node()
        self.vs[16]["mm__"] = """apply_contains"""
        # apply class Name() node
        self.add_node()
        self.vs[17]["name"] = """"""
        self.vs[17]["classtype"] = """Name"""
        self.vs[17]["mm__"] = """Name"""
        self.vs[17]["cardinality"] = """1"""
        # apply_contains node for class Name()
        self.add_node()
        self.vs[18]["mm__"] = """apply_contains"""
        # apply class Name() node
        self.add_node()
        self.vs[19]["name"] = """"""
        self.vs[19]["classtype"] = """Name"""
        self.vs[19]["mm__"] = """Name"""
        self.vs[19]["cardinality"] = """1"""
        # apply_contains node for class Name()
        self.add_node()
        self.vs[20]["mm__"] = """apply_contains"""
        
        
        # match association Transition--dest-->Vertex node
        self.add_node()
        self.vs[21]["associationType"] = """dest"""
        self.vs[21]["mm__"] = """directLink_S"""
        # match association Transition--type-->SIBLING0 node
        self.add_node()
        self.vs[22]["associationType"] = """type"""
        self.vs[22]["mm__"] = """directLink_S"""
        # match association Vertex--owningStateMachine-->StateMachine node
        self.add_node()
        self.vs[23]["associationType"] = """owningStateMachine"""
        self.vs[23]["mm__"] = """directLink_S"""
        
        # apply association Inst--channelNames-->Name node
        self.add_node()
        self.vs[24]["associationType"] = """channelNames"""
        self.vs[24]["mm__"] = """directLink_T"""
        # apply association Inst--channelNames-->Name node
        self.add_node()
        self.vs[25]["associationType"] = """channelNames"""
        self.vs[25]["mm__"] = """directLink_T"""
        # apply association Inst--channelNames-->Name node
        self.add_node()
        self.vs[26]["associationType"] = """channelNames"""
        self.vs[26]["mm__"] = """directLink_T"""
        # apply association Inst--channelNames-->Name node
        self.add_node()
        self.vs[27]["associationType"] = """channelNames"""
        self.vs[27]["mm__"] = """directLink_T"""
        
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class Transition()
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class Vertex()
                (0,8), # matchmodel -> match_contains
                (8,7), # match_contains -> match_class SIBLING0()
                (0,10), # matchmodel -> match_contains
                (10,9), # match_contains -> match_class StateMachine()
                (1,12), # applymodel -> apply_contains
                (12,11), # apply_contains -> apply_class Inst()
                (1,14), # applymodel -> apply_contains
                (14,13), # apply_contains -> apply_class Name()
                (1,16), # applymodel -> apply_contains
                (16,15), # apply_contains -> apply_class Name()
                (1,18), # applymodel -> apply_contains
                (18,17), # apply_contains -> apply_class Name()
                (1,20), # applymodel -> apply_contains
                (20,19), # apply_contains -> apply_class Name()
                (3,21), # match_class Transition() -> association dest
                (21,5), # association dest  -> match_class Vertex()
                (3,22), # match_class Transition() -> association type
                (22,7), # association type  -> match_class SIBLING0()
                (5,23), # match_class Vertex() -> association owningStateMachine
                (23,9), # association owningStateMachine  -> match_class StateMachine()
                (11,24), # apply_class Inst() -> association channelNames
                (24,17), # association channelNames  -> apply_class Name()
                (11,25), # apply_class Inst() -> association channelNames
                (25,13), # association channelNames  -> apply_class Name()
                (11,26), # apply_class Inst() -> association channelNames
                (26,15), # association channelNames  -> apply_class Name()
                (11,27), # apply_class Inst() -> association channelNames
                (27,19), # association channelNames  -> apply_class Name()
		])
		
        # Add the equations
        self["equations"] = [((11,'name'),('concat',(('constant','S'),(9,'name')))), ((11,'__ApplyAttribute'),('constant','instfortrans')), ((13,'literal'),('constant','exack')), ((15,'literal'),('concat',(('constant','A'),('concat',((5,'name'),('constant','A')))))), ((17,'literal'),('constant','exit')), ((19,'literal'),('constant','sh')), ]
        
