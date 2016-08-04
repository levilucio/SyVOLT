from core.himesis import Himesis
import uuid

class HExitPoint2BProcDefWhetherOrNotExitPtHasOutgoingTrans(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule ExitPoint2BProcDefWhetherOrNotExitPtHasOutgoingTrans.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HExitPoint2BProcDefWhetherOrNotExitPtHasOutgoingTrans, self).__init__(name='HExitPoint2BProcDefWhetherOrNotExitPtHasOutgoingTrans', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """ExitPoint2BProcDefWhetherOrNotExitPtHasOutgoingTrans"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ExitPoint2BProcDefWhetherOrNotExitPtHasOutgoingTrans')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["attr1"] = """ExitPoint2BProcDefWhetherOrNotExitPtHasOutgoingTrans"""
        
        # match class State() node
        self.add_node()
        
        self.vs[3]["mm__"] = """State""" 
        self.vs[3]["attr1"] = """+""" 
        # match class ExitPoint() node
        self.add_node()
        
        self.vs[4]["mm__"] = """ExitPoint""" 
        self.vs[4]["attr1"] = """+""" 
        
        
        # apply class LocalDef() node
        self.add_node()

        self.vs[5]["mm__"] = """LocalDef""" 
        self.vs[5]["attr1"] = """1"""
        # apply class ProcDef() node
        self.add_node()

        self.vs[6]["mm__"] = """ProcDef""" 
        self.vs[6]["attr1"] = """1"""
        # apply class Name() node
        self.add_node()

        self.vs[7]["mm__"] = """Name""" 
        self.vs[7]["attr1"] = """1"""
        # apply class Par() node
        self.add_node()

        self.vs[8]["mm__"] = """Par""" 
        self.vs[8]["attr1"] = """1"""
        # apply class Trigger() node
        self.add_node()

        self.vs[9]["mm__"] = """Trigger""" 
        self.vs[9]["attr1"] = """1"""
        
        
        # match association State--exitPoints-->ExitPoint node
        self.add_node()
        self.vs[10]["attr1"] = """exitPoints"""
        self.vs[10]["mm__"] = """directLink_S"""
        
        # apply association LocalDef--def-->ProcDef node
        self.add_node()
        self.vs[11]["attr1"] = """def"""
        self.vs[11]["mm__"] = """directLink_T"""
        # apply association ProcDef--channelNames-->Name node
        self.add_node()
        self.vs[12]["attr1"] = """channelNames"""
        self.vs[12]["mm__"] = """directLink_T"""
        # apply association ProcDef--p-->Par node
        self.add_node()
        self.vs[13]["attr1"] = """p"""
        self.vs[13]["mm__"] = """directLink_T"""
        # apply association Par--p-->Trigger node
        self.add_node()
        self.vs[14]["attr1"] = """p"""
        self.vs[14]["mm__"] = """directLink_T"""
        
        # backward association State---->LocalDef node
        self.add_node()

        self.vs[15]["mm__"] = """backward_link"""
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class State()
                (0,4), # matchmodel -> match_class ExitPoint()
                (1,5), # applymodel -> -> apply_class LocalDef()
                (1,6), # applymodel -> -> apply_class ProcDef()
                (1,7), # applymodel -> -> apply_class Name()
                (1,8), # applymodel -> -> apply_class Par()
                (1,9), # applymodel -> -> apply_class Trigger()
                (3,10), # match_class State() -> association exitPoints
                (10,4), # association exitPoints  -> match_class ExitPoint()
                (5,11), # apply_class LocalDef() -> association def
                (11,6), # association def  -> apply_class ProcDef()
                (6,12), # apply_class ProcDef() -> association channelNames
                (12,7), # association channelNames  -> apply_class Name()
                (6,13), # apply_class ProcDef() -> association p
                (13,8), # association p  -> apply_class Par()
                (8,14), # apply_class Par() -> association p
                (14,9), # association p  -> apply_class Trigger()
                (5,15), # apply_class LocalDef() -> backward_association
                (15,3), #  backward_association -> apply_class State()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((3,'isComposite'),('constant','true')), ((6,'name'),('concat',(('constant','B'),(4,'name')))), ((7,'literal'),('constant','sh_in')), ((8,'__ApplyAttribute'),('constant','parexitpoint')), ((9,'channel'),('constant','sh_in')), ]

        
