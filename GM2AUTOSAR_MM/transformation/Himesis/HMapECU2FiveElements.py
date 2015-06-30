

from core.himesis import Himesis

class HMapECU2FiveElements(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HMapECU2FiveElements.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HMapECU2FiveElements, self).__init__(name='HMapECU2FiveElements', num_nodes=24, edges=[])
        
        # Add the edges
        self.add_edges([[6, 11], [11, 7], [7, 12], [12, 1], [4, 19], [19, 2], [4, 20], [20, 8], [4, 21], [21, 5], [4, 22], [22, 10], [4, 23], [23, 0], [15, 0], [18, 1], [2, 13], [2, 15], [9, 3], [3, 4], [13, 8], [8, 14], [14, 5], [16, 6], [17, 7], [9, 16], [9, 17], [9, 18]])
        # Set the graph attributes
        self["mm__"] = ['GM2AUTOSAR_MM']
        self["name"] = """MapECU2FiveElements"""
        self["GUID__"] = 2147339306453962358
        
        # Set the node attributes
        self.vs[0]["name"] = """sysmap1"""
        self.vs[0]["classtype"] = """SystemMapping"""
        self.vs[0]["mm__"] = """SystemMapping"""
        self.vs[0]["cardinality"] = """1"""
        self.vs[0]["GUID__"] = 4567748977449828162
        self.vs[1]["name"] = """dist1"""
        self.vs[1]["classtype"] = """Distributable"""
        self.vs[1]["mm__"] = """Distributable"""
        self.vs[1]["cardinality"] = """1"""
        self.vs[1]["GUID__"] = 3647799502956596013
        self.vs[2]["name"] = """sys1"""
        self.vs[2]["classtype"] = """System"""
        self.vs[2]["mm__"] = """System"""
        self.vs[2]["cardinality"] = """1"""
        self.vs[2]["GUID__"] = 5254979261160147928
        self.vs[3]["mm__"] = """paired_with"""
        self.vs[3]["GUID__"] = 6635870871354259374
        self.vs[4]["mm__"] = """ApplyModel"""
        self.vs[4]["GUID__"] = 1866261081332950229
        self.vs[5]["name"] = """composty1"""
        self.vs[5]["classtype"] = """CompositionType"""
        self.vs[5]["mm__"] = """CompositionType"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = 1502210219054176355
        self.vs[6]["name"] = """ecu1"""
        self.vs[6]["classtype"] = """ECU"""
        self.vs[6]["mm__"] = """ECU"""
        self.vs[6]["cardinality"] = """+"""
        self.vs[6]["GUID__"] = 4702738983912087693
        self.vs[7]["name"] = """vd1"""
        self.vs[7]["classtype"] = """VirtualDevice"""
        self.vs[7]["mm__"] = """VirtualDevice"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = 2065861480392376956
        self.vs[8]["name"] = """swcompos1"""
        self.vs[8]["classtype"] = """SoftwareComposition"""
        self.vs[8]["mm__"] = """SoftwareComposition"""
        self.vs[8]["cardinality"] = """1"""
        self.vs[8]["GUID__"] = 7745074910905322574
        self.vs[9]["mm__"] = """MatchModel"""
        self.vs[9]["GUID__"] = 8100248232739018895
        self.vs[10]["name"] = """ecuinst1"""
        self.vs[10]["classtype"] = """EcuInstance"""
        self.vs[10]["mm__"] = """EcuInstance"""
        self.vs[10]["cardinality"] = """1"""
        self.vs[10]["GUID__"] = 4943864269956774246
        self.vs[11]["associationType"] = """virtualDevice"""
        self.vs[11]["mm__"] = """directLink_S"""
        self.vs[11]["GUID__"] = 8456781471749532857
        self.vs[12]["associationType"] = """distributable"""
        self.vs[12]["mm__"] = """directLink_S"""
        self.vs[12]["GUID__"] = 3738965775305298515
        self.vs[13]["associationType"] = """softwareComposition"""
        self.vs[13]["mm__"] = """directLink_T"""
        self.vs[13]["GUID__"] = 9041082083727902893
        self.vs[14]["associationType"] = """softwareComposition"""
        self.vs[14]["mm__"] = """directLink_T"""
        self.vs[14]["GUID__"] = 4777483739166191684
        self.vs[15]["associationType"] = """mapping"""
        self.vs[15]["mm__"] = """directLink_T"""
        self.vs[15]["GUID__"] = 7622187477012958772
        self.vs[16]["mm__"] = """match_contains"""
        self.vs[16]["GUID__"] = 6280738099090485165
        self.vs[17]["mm__"] = """match_contains"""
        self.vs[17]["GUID__"] = 1465191925400095212
        self.vs[18]["mm__"] = """match_contains"""
        self.vs[18]["GUID__"] = 3077447033433992763
        self.vs[19]["mm__"] = """apply_contains"""
        self.vs[19]["GUID__"] = 4360952753527638391
        self.vs[20]["mm__"] = """apply_contains"""
        self.vs[20]["GUID__"] = 7983747145149585713
        self.vs[21]["mm__"] = """apply_contains"""
        self.vs[21]["GUID__"] = 8744965711990402768
        self.vs[22]["mm__"] = """apply_contains"""
        self.vs[22]["GUID__"] = 6793595975989279382
        self.vs[23]["mm__"] = """apply_contains"""
        self.vs[23]["GUID__"] = 2384115689318387697

