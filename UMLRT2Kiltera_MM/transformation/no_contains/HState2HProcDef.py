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
        self.vs[2]["attr1"] = """State2HProcDef"""
        
        # match class State() node
        self.add_node()
        
        self.vs[3]["mm__"] = """State""" 
        self.vs[3]["attr1"] = """+""" 
        
        
        # apply class LocalDef() node
        self.add_node()

        self.vs[4]["mm__"] = """LocalDef""" 
        self.vs[4]["attr1"] = """1"""
        # apply class ProcDef() node
        self.add_node()

        self.vs[5]["mm__"] = """ProcDef""" 
        self.vs[5]["attr1"] = """1"""
        # apply class Name() node
        self.add_node()

        self.vs[6]["mm__"] = """Name""" 
        self.vs[6]["attr1"] = """1"""
        # apply class Name() node
        self.add_node()

        self.vs[7]["mm__"] = """Name""" 
        self.vs[7]["attr1"] = """1"""
        # apply class Name() node
        self.add_node()

        self.vs[8]["mm__"] = """Name""" 
        self.vs[8]["attr1"] = """1"""
        # apply class Listen() node
        self.add_node()

        self.vs[9]["mm__"] = """Listen""" 
        self.vs[9]["attr1"] = """1"""
        # apply class ListenBranch() node
        self.add_node()

        self.vs[10]["mm__"] = """ListenBranch""" 
        self.vs[10]["attr1"] = """1"""
        # apply class Null() node
        self.add_node()

        self.vs[11]["mm__"] = """Null""" 
        self.vs[11]["attr1"] = """1"""
        # apply class ListenBranch() node
        self.add_node()

        self.vs[12]["mm__"] = """ListenBranch""" 
        self.vs[12]["attr1"] = """1"""
        # apply class Seq() node
        self.add_node()

        self.vs[13]["mm__"] = """Seq""" 
        self.vs[13]["attr1"] = """1"""
        # apply class Trigger() node
        self.add_node()

        self.vs[14]["mm__"] = """Trigger""" 
        self.vs[14]["attr1"] = """1"""
        # apply class Listen() node
        self.add_node()

        self.vs[15]["mm__"] = """Listen""" 
        self.vs[15]["attr1"] = """1"""
        # apply class ListenBranch() node
        self.add_node()

        self.vs[16]["mm__"] = """ListenBranch""" 
        self.vs[16]["attr1"] = """1"""
        # apply class Trigger() node
        self.add_node()

        self.vs[17]["mm__"] = """Trigger""" 
        self.vs[17]["attr1"] = """1"""
        
        
        
        # apply association LocalDef--def-->ProcDef node
        self.add_node()
        self.vs[18]["attr1"] = """def"""
        self.vs[18]["mm__"] = """directLink_T"""
        # apply association ProcDef--channelNames-->Name node
        self.add_node()
        self.vs[19]["attr1"] = """channelNames"""
        self.vs[19]["mm__"] = """directLink_T"""
        # apply association ProcDef--channelNames-->Name node
        self.add_node()
        self.vs[20]["attr1"] = """channelNames"""
        self.vs[20]["mm__"] = """directLink_T"""
        # apply association ProcDef--channelNames-->Name node
        self.add_node()
        self.vs[21]["attr1"] = """channelNames"""
        self.vs[21]["mm__"] = """directLink_T"""
        # apply association ProcDef--p-->Listen node
        self.add_node()
        self.vs[22]["attr1"] = """p"""
        self.vs[22]["mm__"] = """directLink_T"""
        # apply association Listen--branches-->ListenBranch node
        self.add_node()
        self.vs[23]["attr1"] = """branches"""
        self.vs[23]["mm__"] = """directLink_T"""
        # apply association ListenBranch--p-->Null node
        self.add_node()
        self.vs[24]["attr1"] = """p"""
        self.vs[24]["mm__"] = """directLink_T"""
        # apply association Listen--branches-->ListenBranch node
        self.add_node()
        self.vs[25]["attr1"] = """branches"""
        self.vs[25]["mm__"] = """directLink_T"""
        # apply association ListenBranch--p-->Seq node
        self.add_node()
        self.vs[26]["attr1"] = """p"""
        self.vs[26]["mm__"] = """directLink_T"""
        # apply association Seq--p-->Trigger node
        self.add_node()
        self.vs[27]["attr1"] = """p"""
        self.vs[27]["mm__"] = """directLink_T"""
        # apply association Seq--p-->Listen node
        self.add_node()
        self.vs[28]["attr1"] = """p"""
        self.vs[28]["mm__"] = """directLink_T"""
        # apply association Listen--branches-->ListenBranch node
        self.add_node()
        self.vs[29]["attr1"] = """branches"""
        self.vs[29]["mm__"] = """directLink_T"""
        # apply association ListenBranch--p-->Trigger node
        self.add_node()
        self.vs[30]["attr1"] = """p"""
        self.vs[30]["mm__"] = """directLink_T"""
        
        # backward association State---->LocalDef node
        self.add_node()

        self.vs[31]["mm__"] = """backward_link"""
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class State()
                (1,4), # applymodel -> -> apply_class LocalDef()
                (1,5), # applymodel -> -> apply_class ProcDef()
                (1,6), # applymodel -> -> apply_class Name()
                (1,7), # applymodel -> -> apply_class Name()
                (1,8), # applymodel -> -> apply_class Name()
                (1,9), # applymodel -> -> apply_class Listen()
                (1,10), # applymodel -> -> apply_class ListenBranch()
                (1,11), # applymodel -> -> apply_class Null()
                (1,12), # applymodel -> -> apply_class ListenBranch()
                (1,13), # applymodel -> -> apply_class Seq()
                (1,14), # applymodel -> -> apply_class Trigger()
                (1,15), # applymodel -> -> apply_class Listen()
                (1,16), # applymodel -> -> apply_class ListenBranch()
                (1,17), # applymodel -> -> apply_class Trigger()
                (4,18), # apply_class LocalDef() -> association def
                (18,5), # association def  -> apply_class ProcDef()
                (5,19), # apply_class ProcDef() -> association channelNames
                (19,6), # association channelNames  -> apply_class Name()
                (5,20), # apply_class ProcDef() -> association channelNames
                (20,7), # association channelNames  -> apply_class Name()
                (5,21), # apply_class ProcDef() -> association channelNames
                (21,8), # association channelNames  -> apply_class Name()
                (5,22), # apply_class ProcDef() -> association p
                (22,9), # association p  -> apply_class Listen()
                (9,23), # apply_class Listen() -> association branches
                (23,10), # association branches  -> apply_class ListenBranch()
                (10,24), # apply_class ListenBranch() -> association p
                (24,11), # association p  -> apply_class Null()
                (9,25), # apply_class Listen() -> association branches
                (25,12), # association branches  -> apply_class ListenBranch()
                (12,26), # apply_class ListenBranch() -> association p
                (26,13), # association p  -> apply_class Seq()
                (13,27), # apply_class Seq() -> association p
                (27,14), # association p  -> apply_class Trigger()
                (13,28), # apply_class Seq() -> association p
                (28,15), # association p  -> apply_class Listen()
                (15,29), # apply_class Listen() -> association branches
                (29,16), # association branches  -> apply_class ListenBranch()
                (16,30), # apply_class ListenBranch() -> association p
                (30,17), # association p  -> apply_class Trigger()
                (4,31), # apply_class LocalDef() -> backward_association
                (31,3), #  backward_association -> apply_class State()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((3,'isComposite'),('constant','true')), ((5,'name'),('constant','H')), ((6,'literal'),('constant','exit_in')), ((7,'literal'),('constant','exack_in')), ((8,'literal'),('constant','sh_in')), ((10,'channel'),('constant','sh_in')), ((12,'channel'),('constant','exit')), ((14,'channel'),('constant','exit_in')), ((16,'channel'),('constant','exack_in')), ((17,'channel'),('constant','exack')), ]

        
