

from core.himesis import Himesis

class HConnVirtualDeviceToDistributable(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HConnVirtualDeviceToDistributable.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HConnVirtualDeviceToDistributable, self).__init__(name='HConnVirtualDeviceToDistributable', num_nodes=26, edges=[])
        
        # Add the edges
        self.add_edges([[5, 10], [10, 7], [7, 11], [11, 0], [3, 18], [18, 4], [3, 19], [19, 6], [3, 20], [20, 2], [3, 21], [21, 9], [17, 0], [24, 0], [25, 0], [8, 1], [1, 3], [4, 22], [22, 5], [6, 23], [23, 7], [9, 24], [2, 25], [12, 2], [2, 13], [4, 12], [13, 4], [6, 14], [14, 9], [15, 5], [16, 7], [8, 15], [8, 16], [8, 17]])
        # Set the graph attributes
        self["mm__"] = ['GM2AUTOSAR_MM']
        self["name"] = """ConnVirtualDeviceToDistributable"""
        self["GUID__"] = 135097658287470424
        
        # Set the node attributes
        self.vs[0]["name"] = """dist1"""
        self.vs[0]["classtype"] = """Distributable"""
        self.vs[0]["mm__"] = """Distributable"""
        self.vs[0]["cardinality"] = """+"""
        self.vs[0]["GUID__"] = 2862480672044704619
        self.vs[1]["mm__"] = """paired_with"""
        self.vs[1]["GUID__"] = 5710788945859792427
        self.vs[2]["name"] = """comp1"""
        self.vs[2]["classtype"] = """ComponentPrototype"""
        self.vs[2]["mm__"] = """ComponentPrototype"""
        self.vs[2]["cardinality"] = """1"""
        self.vs[2]["GUID__"] = 3636197349575597208
        self.vs[3]["mm__"] = """ApplyModel"""
        self.vs[3]["GUID__"] = 6141391533606486357
        self.vs[4]["name"] = """composty1"""
        self.vs[4]["classtype"] = """CompositionType"""
        self.vs[4]["mm__"] = """CompositionType"""
        self.vs[4]["cardinality"] = """1"""
        self.vs[4]["GUID__"] = 838242401644170549
        self.vs[5]["name"] = """ecu1"""
        self.vs[5]["classtype"] = """ECU"""
        self.vs[5]["mm__"] = """ECU"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 4228650004782917332
        self.vs[6]["name"] = """stem1"""
        self.vs[6]["classtype"] = """SwcToEcuMapping"""
        self.vs[6]["mm__"] = """SwcToEcuMapping"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = 5456968974285826270
        self.vs[7]["name"] = """vd1"""
        self.vs[7]["classtype"] = """VirtualDevice"""
        self.vs[7]["mm__"] = """VirtualDevice"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 8802082973023328190
        self.vs[8]["mm__"] = """MatchModel"""
        self.vs[8]["GUID__"] = 6202437509517452595
        self.vs[9]["name"] = """sctemc1"""
        self.vs[9]["classtype"] = """SwCompToEcuMapping_component"""
        self.vs[9]["mm__"] = """SwCompToEcuMapping_component"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 130688503101294969
        self.vs[10]["associationType"] = """virtualDevice"""
        self.vs[10]["mm__"] = """directLink_S"""
        self.vs[10]["GUID__"] = 8671565071349472912
        self.vs[11]["associationType"] = """distributable"""
        self.vs[11]["mm__"] = """directLink_S"""
        self.vs[11]["GUID__"] = 7269097531828973692
        self.vs[12]["associationType"] = """component"""
        self.vs[12]["mm__"] = """directLink_T"""
        self.vs[12]["GUID__"] = 6137857719982676918
        self.vs[13]["associationType"] = """type"""
        self.vs[13]["mm__"] = """directLink_T"""
        self.vs[13]["GUID__"] = 7044535015204336176
        self.vs[14]["associationType"] = """component"""
        self.vs[14]["mm__"] = """directLink_T"""
        self.vs[14]["GUID__"] = 689190453953510236
        self.vs[15]["mm__"] = """match_contains"""
        self.vs[15]["GUID__"] = 4173140114751817780
        self.vs[16]["mm__"] = """match_contains"""
        self.vs[16]["GUID__"] = 4826327800464103807
        self.vs[17]["mm__"] = """match_contains"""
        self.vs[17]["GUID__"] = 3978906229413327974
        self.vs[18]["mm__"] = """apply_contains"""
        self.vs[18]["GUID__"] = 7039336363861942646
        self.vs[19]["mm__"] = """apply_contains"""
        self.vs[19]["GUID__"] = 5863666720788161526
        self.vs[20]["mm__"] = """apply_contains"""
        self.vs[20]["GUID__"] = 5428116526258338487
        self.vs[21]["mm__"] = """apply_contains"""
        self.vs[21]["GUID__"] = 752350933020849402
        self.vs[22]["mm__"] = """backward_link"""
        self.vs[22]["type"] = """ruleDef"""
        self.vs[22]["GUID__"] = 2703906540734192781
        self.vs[23]["mm__"] = """backward_link"""
        self.vs[23]["type"] = """ruleDef"""
        self.vs[23]["GUID__"] = 3547868022674227222
        self.vs[24]["mm__"] = """backward_link"""
        self.vs[24]["type"] = """ruleDef"""
        self.vs[24]["GUID__"] = 7220949292246680550
        self.vs[25]["mm__"] = """backward_link"""
        self.vs[25]["type"] = """ruleDef"""
        self.vs[25]["GUID__"] = 6660645141578877840

