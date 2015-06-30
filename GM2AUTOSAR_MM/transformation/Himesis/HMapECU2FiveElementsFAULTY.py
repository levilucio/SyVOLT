

from core.himesis import Himesis

class HMapECU2FiveElementsFAULTY(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HMapECU2FiveElementsFAULTY.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HMapECU2FiveElementsFAULTY, self).__init__(name='HMapECU2FiveElementsFAULTY', num_nodes=18, edges=[])
        
        # Add the edges
        self.add_edges([[3, 13], [13, 1], [3, 14], [14, 7], [3, 15], [15, 4], [3, 16], [16, 9], [3, 17], [17, 0], [12, 0], [1, 10], [1, 12], [8, 2], [2, 3], [10, 7], [7, 11], [11, 4], [6, 5], [8, 6]])
        # Set the graph attributes
        self["mm__"] = ['GM2AUTOSAR_MM']
        self["name"] = """MapECU2FiveElementsFAULTY"""
        self["GUID__"] = 1370983784953746808
        
        # Set the node attributes
        self.vs[0]["name"] = """sysmap1"""
        self.vs[0]["classtype"] = """SystemMapping"""
        self.vs[0]["mm__"] = """SystemMapping"""
        self.vs[0]["cardinality"] = """1"""
        self.vs[0]["GUID__"] = 4729855653097473264
        self.vs[1]["name"] = """sys1"""
        self.vs[1]["classtype"] = """System"""
        self.vs[1]["mm__"] = """System"""
        self.vs[1]["cardinality"] = """1"""
        self.vs[1]["GUID__"] = 5825247562669085812
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 8094237773989128308
        self.vs[3]["mm__"] = """ApplyModel"""
        self.vs[3]["GUID__"] = 127426216693010650
        self.vs[4]["name"] = """composty1"""
        self.vs[4]["classtype"] = """CompositionType"""
        self.vs[4]["mm__"] = """CompositionType"""
        self.vs[4]["cardinality"] = """1"""
        self.vs[4]["GUID__"] = 5576273705316842200
        self.vs[5]["name"] = """ecu1"""
        self.vs[5]["classtype"] = """ECU"""
        self.vs[5]["mm__"] = """ECU"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 3049641880927187477
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 3892844601252709963
        self.vs[7]["name"] = """swcompos1"""
        self.vs[7]["classtype"] = """SoftwareComposition"""
        self.vs[7]["mm__"] = """SoftwareComposition"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = 9213888064198775845
        self.vs[8]["mm__"] = """MatchModel"""
        self.vs[8]["GUID__"] = 6576111308160699301
        self.vs[9]["name"] = """ecuinst1"""
        self.vs[9]["classtype"] = """EcuInstance"""
        self.vs[9]["mm__"] = """EcuInstance"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 7565367178625784374
        self.vs[10]["associationType"] = """softwareComposition"""
        self.vs[10]["mm__"] = """directLink_T"""
        self.vs[10]["GUID__"] = 6200958728069336385
        self.vs[11]["associationType"] = """softwareComposition"""
        self.vs[11]["mm__"] = """directLink_T"""
        self.vs[11]["GUID__"] = 6567857024148404544
        self.vs[12]["associationType"] = """mapping"""
        self.vs[12]["mm__"] = """directLink_T"""
        self.vs[12]["GUID__"] = 6631495548778434902
        self.vs[13]["mm__"] = """apply_contains"""
        self.vs[13]["GUID__"] = 2999671672166792371
        self.vs[14]["mm__"] = """apply_contains"""
        self.vs[14]["GUID__"] = 6364404330144297248
        self.vs[15]["mm__"] = """apply_contains"""
        self.vs[15]["GUID__"] = 1319675010330445561
        self.vs[16]["mm__"] = """apply_contains"""
        self.vs[16]["GUID__"] = 4568883190377934303
        self.vs[17]["mm__"] = """apply_contains"""
        self.vs[17]["GUID__"] = 375384320178947629

