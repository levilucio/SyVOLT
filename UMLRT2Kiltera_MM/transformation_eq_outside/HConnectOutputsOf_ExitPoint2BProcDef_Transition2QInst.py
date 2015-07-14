from core.himesis import Himesis
import uuid

class HConnectOutputsOf_ExitPoint2BProcDef_Transition2QInst(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule ConnectOutputsOf_ExitPoint2BProcDef_Transition2QInst.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HConnectOutputsOf_ExitPoint2BProcDef_Transition2QInst, self).__init__(name='HConnectOutputsOf_ExitPoint2BProcDef_Transition2QInst', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """ConnectOutputsOf_ExitPoint2BProcDef_Transition2QInst"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConnectOutputsOf_ExitPoint2BProcDef_Transition2QInst')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["rulename"] = """ConnectOutputsOf_ExitPoint2BProcDef_Transition2QInst"""
        
        # match class ExitPoint() node
        self.add_node()
        self.vs[3]["name"] = """"""
        self.vs[3]["classtype"] = """ExitPoint"""
        self.vs[3]["mm__"] = """ExitPoint"""
        self.vs[3]["cardinality"] = """+"""
        # match_contains node for class ExitPoint()
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        # match class Transition() node
        self.add_node()
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """Transition"""
        self.vs[5]["mm__"] = """Transition"""
        self.vs[5]["cardinality"] = """1"""
        # match_contains node for class Transition()
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        
        
        # apply class Par() node
        self.add_node()
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """Par"""
        self.vs[7]["mm__"] = """Par"""
        self.vs[7]["cardinality"] = """1"""
        # apply_contains node for class Par()
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        # apply class Inst() node
        self.add_node()
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """Inst"""
        self.vs[9]["mm__"] = """Inst"""
        self.vs[9]["cardinality"] = """1"""
        # apply_contains node for class Inst()
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        
        
        # match association ExitPoint--outgoingTransitions-->Transition node
        self.add_node()
        self.vs[11]["associationType"] = """outgoingTransitions"""
        self.vs[11]["mm__"] = """directLink_S"""
        
        # apply association Par--p-->Inst node
        self.add_node()
        self.vs[12]["associationType"] = """p"""
        self.vs[12]["mm__"] = """directLink_T"""
        
        # backward association ExitPoint---->Par node
        self.add_node()
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["mm__"] = """backward_link"""
        # backward association Transition---->Inst node
        self.add_node()
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class ExitPoint()
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class Transition()
                (1,8), # applymodel -> apply_contains
                (8,7), # apply_contains -> apply_class Par()
                (1,10), # applymodel -> apply_contains
                (10,9), # apply_contains -> apply_class Inst()
                (3,11), # match_class ExitPoint() -> association outgoingTransitions
                (11,5), # association outgoingTransitions  -> match_class Transition()
                (7,12), # apply_class Par() -> association p
                (12,9), # association p  -> apply_class Inst()
                (7,13), # apply_class Par() -> backward_association
                (13,3), #  backward_association -> apply_class ExitPoint()
                (9,14), # apply_class Inst() -> backward_association
                (14,5), #  backward_association -> apply_class Transition()
		])
		
        # Add the equations
        self.equations = [((7,'__ApplyAttribute'),('constant','parexitpoint')), ((9,'__ApplyAttribute'),('constant','instfortrans')), ]
        
