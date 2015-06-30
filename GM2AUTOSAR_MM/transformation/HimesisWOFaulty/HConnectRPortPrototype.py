

from core.himesis import Himesis

class HConnectRPortPrototype(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HConnectRPortPrototype.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HConnectRPortPrototype, self).__init__(name='HConnectRPortPrototype', num_nodes=23, edges=[])
        
        # Add the edges
        self.add_edges([[6, 14], [14, 7], [7, 15], [15, 0], [0, 16], [16, 8], [8, 17], [17, 9], [4, 12], [12, 5], [4, 13], [13, 11], [20, 0], [10, 1], [1, 4], [5, 2], [2, 6], [5, 3], [3, 11], [18, 6], [19, 7], [21, 8], [22, 9], [10, 18], [10, 19], [10, 20], [10, 21], [10, 22]])
        # Set the graph attributes
        self["mm__"] = ['GM2AUTOSAR_MM']
        self["name"] = """ConnectRPortPrototype"""
        self["GUID__"] = 2424417460545023563
        
        # Set the node attributes
        self.vs[0]["name"] = """dist1"""
        self.vs[0]["classtype"] = """Distributable"""
        self.vs[0]["mm__"] = """Distributable"""
        self.vs[0]["cardinality"] = """+"""
        self.vs[0]["GUID__"] = 6676462656138066710
        self.vs[1]["mm__"] = """paired_with"""
        self.vs[1]["GUID__"] = 6498801497579132202
        self.vs[2]["mm__"] = """backward_link"""
        self.vs[2]["type"] = """ruleDef"""
        self.vs[2]["GUID__"] = 5368205367157966180
        self.vs[3]["associationType"] = """port"""
        self.vs[3]["mm__"] = """directLink_T"""
        self.vs[3]["GUID__"] = 5872144690896754212
        self.vs[4]["mm__"] = """ApplyModel"""
        self.vs[4]["GUID__"] = 3284888035062290097
        self.vs[5]["name"] = """composty1"""
        self.vs[5]["classtype"] = """CompositionType"""
        self.vs[5]["mm__"] = """CompositionType"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = 5166471285633645391
        self.vs[6]["name"] = """ecu1"""
        self.vs[6]["classtype"] = """ECU"""
        self.vs[6]["mm__"] = """ECU"""
        self.vs[6]["cardinality"] = """+"""
        self.vs[6]["GUID__"] = 3545694688117630812
        self.vs[7]["name"] = """vd1"""
        self.vs[7]["classtype"] = """VirtualDevice"""
        self.vs[7]["mm__"] = """VirtualDevice"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 1013448636658168140
        self.vs[8]["name"] = """ef1"""
        self.vs[8]["classtype"] = """ExecFrame"""
        self.vs[8]["mm__"] = """ExecFrame"""
        self.vs[8]["cardinality"] = """+"""
        self.vs[8]["GUID__"] = 7634129998660161638
        self.vs[9]["name"] = """sig1"""
        self.vs[9]["classtype"] = """Signal"""
        self.vs[9]["mm__"] = """Signal"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 4675151453439690985
        self.vs[10]["mm__"] = """MatchModel"""
        self.vs[10]["GUID__"] = 701688639774110603
        self.vs[11]["name"] = """rport1"""
        self.vs[11]["classtype"] = """RPortPrototype"""
        self.vs[11]["mm__"] = """RPortPrototype"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 4497051674485038371
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 2625069938847133457
        self.vs[13]["mm__"] = """apply_contains"""
        self.vs[13]["GUID__"] = 856419492505205746
        self.vs[14]["associationType"] = """virtualDevice"""
        self.vs[14]["mm__"] = """directLink_S"""
        self.vs[14]["GUID__"] = 1147573391558879428
        self.vs[15]["associationType"] = """distributable"""
        self.vs[15]["mm__"] = """directLink_S"""
        self.vs[15]["GUID__"] = 3776301000620020478
        self.vs[16]["associationType"] = """execFrame"""
        self.vs[16]["mm__"] = """directLink_S"""
        self.vs[16]["GUID__"] = 177827066577950129
        self.vs[17]["associationType"] = """required"""
        self.vs[17]["mm__"] = """directLink_S"""
        self.vs[17]["GUID__"] = 4395425262907199665
        self.vs[18]["mm__"] = """match_contains"""
        self.vs[18]["GUID__"] = 2012049258527361465
        self.vs[19]["mm__"] = """match_contains"""
        self.vs[19]["GUID__"] = 7883514449206529979
        self.vs[20]["mm__"] = """match_contains"""
        self.vs[20]["GUID__"] = 8918211060723142490
        self.vs[21]["mm__"] = """match_contains"""
        self.vs[21]["GUID__"] = 7317970578528254062
        self.vs[22]["mm__"] = """match_contains"""
        self.vs[22]["GUID__"] = 2569291830884594154

