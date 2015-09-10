

from core.himesis import Himesis

class HConnectPPortPrototype(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HConnectPPortPrototype.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HConnectPPortPrototype, self).__init__(name='HConnectPPortPrototype', num_nodes=23, edges=[])
        
        # Add the edges
        self.add_edges([[7, 14], [14, 8], [8, 15], [15, 0], [0, 16], [16, 9], [9, 17], [17, 10], [5, 12], [12, 6], [5, 13], [13, 2], [20, 0], [11, 1], [1, 5], [4, 2], [6, 3], [3, 7], [6, 4], [18, 7], [19, 8], [21, 9], [22, 10], [11, 18], [11, 19], [11, 20], [11, 21], [11, 22]])
        # Set the graph attributes
        self["mm__"] = ['GM2AUTOSAR_MM']
        self["name"] = """ConnectPPortPrototype"""
        self["GUID__"] = 1562621071471362973
        
        # Set the node attributes
        self.vs[0]["name"] = """dist1"""
        self.vs[0]["classtype"] = """Distributable"""
        self.vs[0]["mm__"] = """Distributable"""
        self.vs[0]["cardinality"] = """+"""
        self.vs[0]["GUID__"] = 2805661591027829336
        self.vs[1]["mm__"] = """paired_with"""
        self.vs[1]["GUID__"] = 8863177386347215029
        self.vs[2]["name"] = """pport1"""
        self.vs[2]["classtype"] = """PPortPrototype"""
        self.vs[2]["mm__"] = """PPortPrototype"""
        self.vs[2]["cardinality"] = """1"""
        self.vs[2]["GUID__"] = 4102788401699745998
        self.vs[3]["mm__"] = """backward_link"""
        self.vs[3]["type"] = """ruleDef"""
        self.vs[3]["GUID__"] = 4335583735424708590
        self.vs[4]["associationType"] = """port"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 7669116264446592621
        self.vs[5]["mm__"] = """ApplyModel"""
        self.vs[5]["GUID__"] = 6413372078753091690
        self.vs[6]["name"] = """composty1"""
        self.vs[6]["classtype"] = """CompositionType"""
        self.vs[6]["mm__"] = """CompositionType"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = 6365009100213953372
        self.vs[7]["name"] = """ecu1"""
        self.vs[7]["classtype"] = """ECU"""
        self.vs[7]["mm__"] = """ECU"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 3399033183180354834
        self.vs[8]["name"] = """vd1"""
        self.vs[8]["classtype"] = """VirtualDevice"""
        self.vs[8]["mm__"] = """VirtualDevice"""
        self.vs[8]["cardinality"] = """+"""
        self.vs[8]["GUID__"] = 593836466990247151
        self.vs[9]["name"] = """ef1"""
        self.vs[9]["classtype"] = """ExecFrame"""
        self.vs[9]["mm__"] = """ExecFrame"""
        self.vs[9]["cardinality"] = """+"""
        self.vs[9]["GUID__"] = 5455788689310147981
        self.vs[10]["name"] = """s1"""
        self.vs[10]["classtype"] = """Signal"""
        self.vs[10]["mm__"] = """Signal"""
        self.vs[10]["cardinality"] = """1"""
        self.vs[10]["GUID__"] = 2493494501069684108
        self.vs[11]["mm__"] = """MatchModel"""
        self.vs[11]["GUID__"] = 2477369891443646645
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 2275782568304269224
        self.vs[13]["mm__"] = """apply_contains"""
        self.vs[13]["GUID__"] = 6996065539879767197
        self.vs[14]["associationType"] = """virtualDevice"""
        self.vs[14]["mm__"] = """directLink_S"""
        self.vs[14]["GUID__"] = 7153328745846913467
        self.vs[15]["associationType"] = """distributable"""
        self.vs[15]["mm__"] = """directLink_S"""
        self.vs[15]["GUID__"] = 3736996048619959738
        self.vs[16]["associationType"] = """execFrame"""
        self.vs[16]["mm__"] = """directLink_S"""
        self.vs[16]["GUID__"] = 685322813054001943
        self.vs[17]["associationType"] = """provided"""
        self.vs[17]["mm__"] = """directLink_S"""
        self.vs[17]["GUID__"] = 1605612247120144129
        self.vs[18]["mm__"] = """match_contains"""
        self.vs[18]["GUID__"] = 7304435388089323345
        self.vs[19]["mm__"] = """match_contains"""
        self.vs[19]["GUID__"] = 6451991209205647529
        self.vs[20]["mm__"] = """match_contains"""
        self.vs[20]["GUID__"] = 7645037041235934245
        self.vs[21]["mm__"] = """match_contains"""
        self.vs[21]["GUID__"] = 7681395510273011915
        self.vs[22]["mm__"] = """match_contains"""
        self.vs[22]["GUID__"] = 4628069674672443444

