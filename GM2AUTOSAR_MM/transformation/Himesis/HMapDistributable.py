

from core.himesis import Himesis

class HMapDistributable(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HMapDistributable.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HMapDistributable, self).__init__(name='HMapDistributable', num_nodes=16, edges=[])
        
        # Add the edges
        self.add_edges([[5, 9], [9, 6], [6, 10], [10, 0], [4, 11], [11, 8], [4, 12], [12, 2], [15, 0], [7, 1], [1, 4], [3, 2], [8, 3], [13, 5], [14, 6], [7, 13], [7, 14], [7, 15]])
        # Set the graph attributes
        self["mm__"] = ['GM2AUTOSAR_MM']
        self["name"] = """MapDistributable"""
        self["GUID__"] = 4088813473587741739
        
        # Set the node attributes
        self.vs[0]["name"] = """dist1"""
        self.vs[0]["classtype"] = """Distributable"""
        self.vs[0]["mm__"] = """Distributable"""
        self.vs[0]["cardinality"] = """+"""
        self.vs[0]["GUID__"] = 323366918691558831
        self.vs[1]["mm__"] = """paired_with"""
        self.vs[1]["GUID__"] = 8946885519094067000
        self.vs[2]["name"] = """comp1"""
        self.vs[2]["classtype"] = """ComponentPrototype"""
        self.vs[2]["mm__"] = """ComponentPrototype"""
        self.vs[2]["cardinality"] = """1"""
        self.vs[2]["GUID__"] = 4766758106158606329
        self.vs[3]["associationType"] = """componentPrototype"""
        self.vs[3]["mm__"] = """directLink_T"""
        self.vs[3]["GUID__"] = 9095811788322207131
        self.vs[4]["mm__"] = """ApplyModel"""
        self.vs[4]["GUID__"] = 2690799472485879894
        self.vs[5]["name"] = """ecu1"""
        self.vs[5]["classtype"] = """ECU"""
        self.vs[5]["mm__"] = """ECU"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = 7234414424121682329
        self.vs[6]["name"] = """vd1"""
        self.vs[6]["classtype"] = """VirtualDevice"""
        self.vs[6]["mm__"] = """VirtualDevice"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = 3736480196596533372
        self.vs[7]["mm__"] = """MatchModel"""
        self.vs[7]["GUID__"] = 9098274017854249582
        self.vs[8]["name"] = """sctemc1"""
        self.vs[8]["classtype"] = """SwCompToEcuMapping_component"""
        self.vs[8]["mm__"] = """SwCompToEcuMapping_component"""
        self.vs[8]["cardinality"] = """1"""
        self.vs[8]["GUID__"] = 3076827786974758511
        self.vs[9]["associationType"] = """virtualDevice"""
        self.vs[9]["mm__"] = """directLink_S"""
        self.vs[9]["GUID__"] = 8664921369541242794
        self.vs[10]["associationType"] = """distributable"""
        self.vs[10]["mm__"] = """directLink_S"""
        self.vs[10]["GUID__"] = 5495065921484171932
        self.vs[11]["mm__"] = """apply_contains"""
        self.vs[11]["GUID__"] = 8599505507245221716
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 6393231501703334170
        self.vs[13]["mm__"] = """match_contains"""
        self.vs[13]["GUID__"] = 5963963149875453797
        self.vs[14]["mm__"] = """match_contains"""
        self.vs[14]["GUID__"] = 1726375435581392112
        self.vs[15]["mm__"] = """match_contains"""
        self.vs[15]["GUID__"] = 3385780651888584839

