from core.himesis import Himesis
import uuid

class HState2HProcDef(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule State2HProcDef.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HState2HProcDef, self).__init__(name='HState2HProcDef', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """State2HProcDef"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'State2HProcDef')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["rulename"] = """State2HProcDef"""
        
        # match class State() node
        self.add_node()
        self.vs[3]["name"] = """"""
        self.vs[3]["classtype"] = """State"""
        self.vs[3]["mm__"] = """State"""
        self.vs[3]["cardinality"] = """+"""
        # match_contains node for class State()
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        
        
        # apply class LocalDef() node
        self.add_node()
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """LocalDef"""
        self.vs[5]["mm__"] = """LocalDef"""
        self.vs[5]["cardinality"] = """1"""
        # apply_contains node for class LocalDef()
        self.add_node()
        self.vs[6]["mm__"] = """apply_contains"""
        # apply class ProcDef() node
        self.add_node()
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """ProcDef"""
        self.vs[7]["mm__"] = """ProcDef"""
        self.vs[7]["cardinality"] = """1"""
        # apply_contains node for class ProcDef()
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        # apply class Name() node
        self.add_node()
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """Name"""
        self.vs[9]["mm__"] = """Name"""
        self.vs[9]["cardinality"] = """1"""
        # apply_contains node for class Name()
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        # apply class Name() node
        self.add_node()
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """Name"""
        self.vs[11]["mm__"] = """Name"""
        self.vs[11]["cardinality"] = """1"""
        # apply_contains node for class Name()
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
        # apply class Listen() node
        self.add_node()
        self.vs[15]["name"] = """"""
        self.vs[15]["classtype"] = """Listen"""
        self.vs[15]["mm__"] = """Listen"""
        self.vs[15]["cardinality"] = """1"""
        # apply_contains node for class Listen()
        self.add_node()
        self.vs[16]["mm__"] = """apply_contains"""
        # apply class ListenBranch() node
        self.add_node()
        self.vs[17]["name"] = """"""
        self.vs[17]["classtype"] = """ListenBranch"""
        self.vs[17]["mm__"] = """ListenBranch"""
        self.vs[17]["cardinality"] = """1"""
        # apply_contains node for class ListenBranch()
        self.add_node()
        self.vs[18]["mm__"] = """apply_contains"""
        # apply class Null() node
        self.add_node()
        self.vs[19]["name"] = """"""
        self.vs[19]["classtype"] = """Null"""
        self.vs[19]["mm__"] = """Null"""
        self.vs[19]["cardinality"] = """1"""
        # apply_contains node for class Null()
        self.add_node()
        self.vs[20]["mm__"] = """apply_contains"""
        # apply class ListenBranch() node
        self.add_node()
        self.vs[21]["name"] = """"""
        self.vs[21]["classtype"] = """ListenBranch"""
        self.vs[21]["mm__"] = """ListenBranch"""
        self.vs[21]["cardinality"] = """1"""
        # apply_contains node for class ListenBranch()
        self.add_node()
        self.vs[22]["mm__"] = """apply_contains"""
        # apply class Seq() node
        self.add_node()
        self.vs[23]["name"] = """"""
        self.vs[23]["classtype"] = """Seq"""
        self.vs[23]["mm__"] = """Seq"""
        self.vs[23]["cardinality"] = """1"""
        # apply_contains node for class Seq()
        self.add_node()
        self.vs[24]["mm__"] = """apply_contains"""
        # apply class Trigger() node
        self.add_node()
        self.vs[25]["name"] = """"""
        self.vs[25]["classtype"] = """Trigger"""
        self.vs[25]["mm__"] = """Trigger"""
        self.vs[25]["cardinality"] = """1"""
        # apply_contains node for class Trigger()
        self.add_node()
        self.vs[26]["mm__"] = """apply_contains"""
        # apply class Listen() node
        self.add_node()
        self.vs[27]["name"] = """"""
        self.vs[27]["classtype"] = """Listen"""
        self.vs[27]["mm__"] = """Listen"""
        self.vs[27]["cardinality"] = """1"""
        # apply_contains node for class Listen()
        self.add_node()
        self.vs[28]["mm__"] = """apply_contains"""
        # apply class ListenBranch() node
        self.add_node()
        self.vs[29]["name"] = """"""
        self.vs[29]["classtype"] = """ListenBranch"""
        self.vs[29]["mm__"] = """ListenBranch"""
        self.vs[29]["cardinality"] = """1"""
        # apply_contains node for class ListenBranch()
        self.add_node()
        self.vs[30]["mm__"] = """apply_contains"""
        # apply class Trigger() node
        self.add_node()
        self.vs[31]["name"] = """"""
        self.vs[31]["classtype"] = """Trigger"""
        self.vs[31]["mm__"] = """Trigger"""
        self.vs[31]["cardinality"] = """1"""
        # apply_contains node for class Trigger()
        self.add_node()
        self.vs[32]["mm__"] = """apply_contains"""
        
        
        
        # apply association LocalDef--def-->ProcDef node
        self.add_node()
        self.vs[33]["associationType"] = """def"""
        self.vs[33]["mm__"] = """directLink_T"""
        # apply association ProcDef--channelNames-->Name node
        self.add_node()
        self.vs[34]["associationType"] = """channelNames"""
        self.vs[34]["mm__"] = """directLink_T"""
        # apply association ProcDef--channelNames-->Name node
        self.add_node()
        self.vs[35]["associationType"] = """channelNames"""
        self.vs[35]["mm__"] = """directLink_T"""
        # apply association ProcDef--channelNames-->Name node
        self.add_node()
        self.vs[36]["associationType"] = """channelNames"""
        self.vs[36]["mm__"] = """directLink_T"""
        # apply association ProcDef--p-->Listen node
        self.add_node()
        self.vs[37]["associationType"] = """p"""
        self.vs[37]["mm__"] = """directLink_T"""
        # apply association Listen--branches-->ListenBranch node
        self.add_node()
        self.vs[38]["associationType"] = """branches"""
        self.vs[38]["mm__"] = """directLink_T"""
        # apply association ListenBranch--p-->Null node
        self.add_node()
        self.vs[39]["associationType"] = """p"""
        self.vs[39]["mm__"] = """directLink_T"""
        # apply association Listen--branches-->ListenBranch node
        self.add_node()
        self.vs[40]["associationType"] = """branches"""
        self.vs[40]["mm__"] = """directLink_T"""
        # apply association ListenBranch--p-->Seq node
        self.add_node()
        self.vs[41]["associationType"] = """p"""
        self.vs[41]["mm__"] = """directLink_T"""
        # apply association Seq--p-->Trigger node
        self.add_node()
        self.vs[42]["associationType"] = """p"""
        self.vs[42]["mm__"] = """directLink_T"""
        # apply association Seq--p-->Listen node
        self.add_node()
        self.vs[43]["associationType"] = """p"""
        self.vs[43]["mm__"] = """directLink_T"""
        # apply association Listen--branches-->ListenBranch node
        self.add_node()
        self.vs[44]["associationType"] = """branches"""
        self.vs[44]["mm__"] = """directLink_T"""
        # apply association ListenBranch--p-->Trigger node
        self.add_node()
        self.vs[45]["associationType"] = """p"""
        self.vs[45]["mm__"] = """directLink_T"""
        
        # backward association State---->LocalDef node
        self.add_node()
        self.vs[46]["type"] = """ruleDef"""
        self.vs[46]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class State()
                (1,6), # applymodel -> apply_contains
                (6,5), # apply_contains -> apply_class LocalDef()
                (1,8), # applymodel -> apply_contains
                (8,7), # apply_contains -> apply_class ProcDef()
                (1,10), # applymodel -> apply_contains
                (10,9), # apply_contains -> apply_class Name()
                (1,12), # applymodel -> apply_contains
                (12,11), # apply_contains -> apply_class Name()
                (1,14), # applymodel -> apply_contains
                (14,13), # apply_contains -> apply_class Name()
                (1,16), # applymodel -> apply_contains
                (16,15), # apply_contains -> apply_class Listen()
                (1,18), # applymodel -> apply_contains
                (18,17), # apply_contains -> apply_class ListenBranch()
                (1,20), # applymodel -> apply_contains
                (20,19), # apply_contains -> apply_class Null()
                (1,22), # applymodel -> apply_contains
                (22,21), # apply_contains -> apply_class ListenBranch()
                (1,24), # applymodel -> apply_contains
                (24,23), # apply_contains -> apply_class Seq()
                (1,26), # applymodel -> apply_contains
                (26,25), # apply_contains -> apply_class Trigger()
                (1,28), # applymodel -> apply_contains
                (28,27), # apply_contains -> apply_class Listen()
                (1,30), # applymodel -> apply_contains
                (30,29), # apply_contains -> apply_class ListenBranch()
                (1,32), # applymodel -> apply_contains
                (32,31), # apply_contains -> apply_class Trigger()
                (5,33), # apply_class LocalDef() -> association def
                (33,7), # association def  -> apply_class ProcDef()
                (7,34), # apply_class ProcDef() -> association channelNames
                (34,9), # association channelNames  -> apply_class Name()
                (7,35), # apply_class ProcDef() -> association channelNames
                (35,11), # association channelNames  -> apply_class Name()
                (7,36), # apply_class ProcDef() -> association channelNames
                (36,13), # association channelNames  -> apply_class Name()
                (7,37), # apply_class ProcDef() -> association p
                (37,15), # association p  -> apply_class Listen()
                (15,38), # apply_class Listen() -> association branches
                (38,17), # association branches  -> apply_class ListenBranch()
                (17,39), # apply_class ListenBranch() -> association p
                (39,19), # association p  -> apply_class Null()
                (15,40), # apply_class Listen() -> association branches
                (40,21), # association branches  -> apply_class ListenBranch()
                (21,41), # apply_class ListenBranch() -> association p
                (41,23), # association p  -> apply_class Seq()
                (23,42), # apply_class Seq() -> association p
                (42,25), # association p  -> apply_class Trigger()
                (23,43), # apply_class Seq() -> association p
                (43,27), # association p  -> apply_class Listen()
                (27,44), # apply_class Listen() -> association branches
                (44,29), # association branches  -> apply_class ListenBranch()
                (29,45), # apply_class ListenBranch() -> association p
                (45,31), # association p  -> apply_class Trigger()
                (5,46), # apply_class LocalDef() -> backward_association
                (46,3), #  backward_association -> apply_class State()
		])
		
        # Add the equations
        self.equations = [((3,'isComposite'),('constant','true')), ((5,'__ApplyAttribute'),('constant','localdefcompstate')), ((7,'name'),('constant','H')), ((9,'literal'),('constant','exit_in')), ((11,'literal'),('constant','exack_in')), ((13,'literal'),('constant','sh_in')), ((15,'__ApplyAttribute'),('constant','listenhproc')), ((17,'channel'),('constant','sh_in')), ((21,'channel'),('constant','exit')), ((25,'channel'),('constant','exit_in')), ((29,'channel'),('constant','exack_in')), ((31,'channel'),('constant','exack')), ]
        
