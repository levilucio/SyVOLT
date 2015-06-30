

from core.himesis import Himesis

class HMapVirtualDevice(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HMapVirtualDevice.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HMapVirtualDevice, self).__init__(name='HMapVirtualDevice', num_nodes=13, edges=[])
        
        # Add the edges
        self.add_edges([[4, 8], [8, 6], [6, 9], [9, 1], [3, 0], [0, 5], [12, 1], [7, 2], [2, 3], [10, 4], [11, 6], [7, 10], [7, 11], [7, 12]])
        # Set the graph attributes
        self["mm__"] = ['GM2AUTOSAR_MM']
        self["name"] = """MapVirtualDevice"""
        self["GUID__"] = 2484633519417172183
        
        # Set the node attributes
        self.vs[0]["mm__"] = """apply_contains"""
        self.vs[0]["GUID__"] = 1785850404060999113
        self.vs[1]["name"] = """dist1"""
        self.vs[1]["classtype"] = """Distributable"""
        self.vs[1]["mm__"] = """Distributable"""
        self.vs[1]["cardinality"] = """1"""
        self.vs[1]["GUID__"] = 8007054246810890648
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 7530128715728501439
        self.vs[3]["mm__"] = """ApplyModel"""
        self.vs[3]["GUID__"] = 2358593909513726414
        self.vs[4]["name"] = """ecu1"""
        self.vs[4]["classtype"] = """ECU"""
        self.vs[4]["mm__"] = """ECU"""
        self.vs[4]["cardinality"] = """1"""
        self.vs[4]["GUID__"] = 849060461768056723
        self.vs[5]["name"] = """stem1"""
        self.vs[5]["classtype"] = """SwcToEcuMapping"""
        self.vs[5]["mm__"] = """SwcToEcuMapping"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = 3325360147623392843
        self.vs[6]["name"] = """vd1"""
        self.vs[6]["classtype"] = """VirtualDevice"""
        self.vs[6]["mm__"] = """VirtualDevice"""
        self.vs[6]["cardinality"] = """+"""
        self.vs[6]["GUID__"] = 4241478465904845763
        self.vs[7]["mm__"] = """MatchModel"""
        self.vs[7]["GUID__"] = 1700677397005973322
        self.vs[8]["associationType"] = """virtualDevice"""
        self.vs[8]["mm__"] = """directLink_S"""
        self.vs[8]["GUID__"] = 7939425885287164781
        self.vs[9]["associationType"] = """distributable"""
        self.vs[9]["mm__"] = """directLink_S"""
        self.vs[9]["GUID__"] = 8154928657642331319
        self.vs[10]["mm__"] = """match_contains"""
        self.vs[10]["GUID__"] = 3908907529107088374
        self.vs[11]["mm__"] = """match_contains"""
        self.vs[11]["GUID__"] = 1939826086976562436
        self.vs[12]["mm__"] = """match_contains"""
        self.vs[12]["GUID__"] = 420528279210624874

