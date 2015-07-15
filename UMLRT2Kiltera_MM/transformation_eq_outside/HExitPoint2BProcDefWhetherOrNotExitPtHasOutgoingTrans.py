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
        self.vs[2]["rulename"] = """ExitPoint2BProcDefWhetherOrNotExitPtHasOutgoingTrans"""
        
        # match class State() node
        self.add_node()
        self.vs[3]["name"] = """"""
        self.vs[3]["classtype"] = """State"""
        self.vs[3]["mm__"] = """State"""
        self.vs[3]["cardinality"] = """+"""
        # match_contains node for class State()
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        # match class ExitPoint() node
        self.add_node()
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """ExitPoint"""
        self.vs[5]["mm__"] = """ExitPoint"""
        self.vs[5]["cardinality"] = """+"""
        # match_contains node for class ExitPoint()
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        
        
        # apply class LocalDef() node
        self.add_node()
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """LocalDef"""
        self.vs[7]["mm__"] = """LocalDef"""
        self.vs[7]["cardinality"] = """1"""
        # apply_contains node for class LocalDef()
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        # apply class ProcDef() node
        self.add_node()
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """ProcDef"""
        self.vs[9]["mm__"] = """ProcDef"""
        self.vs[9]["cardinality"] = """1"""
        # apply_contains node for class ProcDef()
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
        # apply class Par() node
        self.add_node()
        self.vs[13]["name"] = """"""
        self.vs[13]["classtype"] = """Par"""
        self.vs[13]["mm__"] = """Par"""
        self.vs[13]["cardinality"] = """1"""
        # apply_contains node for class Par()
        self.add_node()
        self.vs[14]["mm__"] = """apply_contains"""
        # apply class Trigger() node
        self.add_node()
        self.vs[15]["name"] = """"""
        self.vs[15]["classtype"] = """Trigger"""
        self.vs[15]["mm__"] = """Trigger"""
        self.vs[15]["cardinality"] = """1"""
        # apply_contains node for class Trigger()
        self.add_node()
        self.vs[16]["mm__"] = """apply_contains"""
        
        
        # match association State--exitPoints-->ExitPoint node
        self.add_node()
        self.vs[17]["associationType"] = """exitPoints"""
        self.vs[17]["mm__"] = """directLink_S"""
        
        # apply association LocalDef--def-->ProcDef node
        self.add_node()
        self.vs[18]["associationType"] = """def"""
        self.vs[18]["mm__"] = """directLink_T"""
        # apply association ProcDef--channelNames-->Name node
        self.add_node()
        self.vs[19]["associationType"] = """channelNames"""
        self.vs[19]["mm__"] = """directLink_T"""
        # apply association ProcDef--p-->Par node
        self.add_node()
        self.vs[20]["associationType"] = """p"""
        self.vs[20]["mm__"] = """directLink_T"""
        # apply association Par--p-->Trigger node
        self.add_node()
        self.vs[21]["associationType"] = """p"""
        self.vs[21]["mm__"] = """directLink_T"""
        
        # backward association State---->LocalDef node
        self.add_node()
        self.vs[22]["type"] = """ruleDef"""
        self.vs[22]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class State()
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class ExitPoint()
                (1,8), # applymodel -> apply_contains
                (8,7), # apply_contains -> apply_class LocalDef()
                (1,10), # applymodel -> apply_contains
                (10,9), # apply_contains -> apply_class ProcDef()
                (1,12), # applymodel -> apply_contains
                (12,11), # apply_contains -> apply_class Name()
                (1,14), # applymodel -> apply_contains
                (14,13), # apply_contains -> apply_class Par()
                (1,16), # applymodel -> apply_contains
                (16,15), # apply_contains -> apply_class Trigger()
                (3,17), # match_class State() -> association exitPoints
                (17,5), # association exitPoints  -> match_class ExitPoint()
                (7,18), # apply_class LocalDef() -> association def
                (18,9), # association def  -> apply_class ProcDef()
                (9,19), # apply_class ProcDef() -> association channelNames
                (19,11), # association channelNames  -> apply_class Name()
                (9,20), # apply_class ProcDef() -> association p
                (20,13), # association p  -> apply_class Par()
                (13,21), # apply_class Par() -> association p
                (21,15), # association p  -> apply_class Trigger()
                (7,22), # apply_class LocalDef() -> backward_association
                (22,3), #  backward_association -> apply_class State()
		])
		
        # Add the equations
        self["equations"] = [((3,'isComposite'),('constant','true')), ((7,'__ApplyAttribute'),('constant','localdefcompstate')), ((9,'name'),('concat',(('constant','B'),(5,'name')))), ((11,'literal'),('constant','sh_in')), ((13,'__ApplyAttribute'),('constant','parexitpoint')), ((15,'channel'),('constant','sh_in')), ]
        
