from core.himesis import Himesis
import uuid

class HConnectOutputsOfExitPoint2BProcDefTransition2QInst(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule ConnectOutputsOfExitPoint2BProcDefTransition2QInst.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HConnectOutputsOfExitPoint2BProcDefTransition2QInst, self).__init__(name='HConnectOutputsOfExitPoint2BProcDefTransition2QInst', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """ConnectOutputsOfExitPoint2BProcDefTransition2QInst"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConnectOutputsOfExitPoint2BProcDefTransition2QInst')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["attr1"] = """ConnectOutputsOfExitPoint2BProcDefTransition2QInst"""
        
        # match class ExitPoint() node
        self.add_node()
        
        self.vs[3]["mm__"] = """ExitPoint""" 
        self.vs[3]["attr1"] = """+""" 
        # match class Transition() node
        self.add_node()
        
        self.vs[4]["mm__"] = """Transition""" 
        self.vs[4]["attr1"] = """1""" 
        
        
        # apply class Par() node
        self.add_node()

        self.vs[5]["mm__"] = """Par""" 
        self.vs[5]["attr1"] = """1"""
        # apply class Inst() node
        self.add_node()

        self.vs[6]["mm__"] = """Inst""" 
        self.vs[6]["attr1"] = """1"""
        
        
        # match association ExitPoint--outgoingTransitions-->Transition node
        self.add_node()
        self.vs[7]["attr1"] = """outgoingTransitions"""
        self.vs[7]["mm__"] = """directLink_S"""
        
        # apply association Par--p-->Inst node
        self.add_node()
        self.vs[8]["attr1"] = """p"""
        self.vs[8]["mm__"] = """directLink_T"""
        
        # backward association ExitPoint---->Par node
        self.add_node()

        self.vs[9]["mm__"] = """backward_link"""
        # backward association Transition---->Inst node
        self.add_node()

        self.vs[10]["mm__"] = """backward_link"""
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class ExitPoint()
                (0,4), # matchmodel -> match_class Transition()
                (1,5), # applymodel -> -> apply_class Par()
                (1,6), # applymodel -> -> apply_class Inst()
                (3,7), # match_class ExitPoint() -> association outgoingTransitions
                (7,4), # association outgoingTransitions  -> match_class Transition()
                (5,8), # apply_class Par() -> association p
                (8,6), # association p  -> apply_class Inst()
                (5,9), # apply_class Par() -> backward_association
                (9,3), #  backward_association -> apply_class ExitPoint()
                (6,10), # apply_class Inst() -> backward_association
                (10,4), #  backward_association -> apply_class Transition()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = []

        
