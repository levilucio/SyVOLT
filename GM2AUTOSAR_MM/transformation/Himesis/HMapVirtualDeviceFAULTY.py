

from core.himesis import Himesis

class HMapVirtualDeviceFAULTY(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HMapVirtualDeviceFAULTY.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HMapVirtualDeviceFAULTY, self).__init__(name='HMapVirtualDeviceFAULTY', num_nodes=7, edges=[])
        
        # Add the edges
        self.add_edges([[2, 0], [0, 3], [6, 1], [1, 2], [5, 4], [6, 5]])
        # Set the graph attributes
        self["mm__"] = ['GM2AUTOSAR_MM']
        self["name"] = """MapVirtualDeviceFAULTY"""
        self["GUID__"] = 8005519840508330680
        
        # Set the node attributes
        self.vs[0]["mm__"] = """apply_contains"""
        self.vs[0]["GUID__"] = 5386016800331561697
        self.vs[1]["mm__"] = """paired_with"""
        self.vs[1]["GUID__"] = 8029754531670097211
        self.vs[2]["mm__"] = """ApplyModel"""
        self.vs[2]["GUID__"] = 4123416109082120287
        self.vs[3]["mm__"] = """SwcToEcuMapping"""
        self.vs[3]["classtype"] = """SwcToEcuMapping"""
        self.vs[3]["cardinality"] = """1"""
        self.vs[3]["name"] = """stem1"""
        self.vs[3]["GUID__"] = 1639029734686706598
        self.vs[4]["mm__"] = """VirtualDevice"""
        self.vs[4]["classtype"] = """VirtualDevice"""
        self.vs[4]["cardinality"] = """1"""
        self.vs[4]["name"] = """vd1"""
        self.vs[4]["GUID__"] = 7435299057323062833
        self.vs[5]["mm__"] = """match_contains"""
        self.vs[5]["GUID__"] = 748770923641199100
        self.vs[6]["mm__"] = """MatchModel"""
        self.vs[6]["GUID__"] = 1166249380544893393

