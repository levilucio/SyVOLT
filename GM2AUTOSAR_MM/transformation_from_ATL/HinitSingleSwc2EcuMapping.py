

from core.himesis import Himesis

class HinitSingleSwc2EcuMapping(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HinitSingleSwc2EcuMapping.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HinitSingleSwc2EcuMapping, self).__init__(name='HinitSingleSwc2EcuMapping', num_nodes=30, edges=[])
        
        # Add the edges
        self.add_edges([[0, 24], [24, 3], [0, 25], [25, 4], [0, 26], [26, 5], [1, 7], [7, 6], [4, 10], [10, 3], [3, 11], [11, 5], [3, 8], [8, 27], [6, 12], [12, 28], [13, 14], [14, 28], [13, 15], [9, 16], [16, 18], [9, 17], [17, 27], [15, 9], [6, 19], [19, 29], [20, 21], [21, 29], [20, 22], [22, 23], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """initSingleSwc2EcuMapping"""
        self["GUID__"] = 5168264086666811050
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 5128647726025049232
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 4659226348932248912
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 3201060995201725240
        self.vs[3]["name"] = """"""
        self.vs[3]["classtype"] = """Partition"""
        self.vs[3]["mm__"] = """Partition"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 1199068320869154567
        self.vs[4]["name"] = """"""
        self.vs[4]["classtype"] = """PhysicalNode"""
        self.vs[4]["mm__"] = """PhysicalNode"""
        self.vs[4]["cardinality"] = """1"""
        self.vs[4]["GUID__"] = 6263189281480861742
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """Module"""
        self.vs[5]["mm__"] = """Module"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = 9118709775911529935
        self.vs[6]["name"] = """"""
        self.vs[6]["classtype"] = """SwcToEcuMapping"""
        self.vs[6]["mm__"] = """SwcToEcuMapping"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = 2420484494664948056
        self.vs[7]["mm__"] = """apply_contains"""
        self.vs[7]["GUID__"] = 7933960858999027477
        self.vs[8]["mm__"] = """hasAttribute_S"""
        self.vs[8]["GUID__"] = 2945961897312983034
        self.vs[9]["name"] = """Concat20"""
        self.vs[9]["mm__"] = """Concat"""
        self.vs[9]["Type"] = """'String'"""
        self.vs[9]["GUID__"] = 3170924583343735859
        self.vs[10]["associationType"] = """partition"""
        self.vs[10]["mm__"] = """directLink_S"""
        self.vs[10]["GUID__"] = 504399538094753535
        self.vs[11]["associationType"] = """module"""
        self.vs[11]["mm__"] = """directLink_S"""
        self.vs[11]["GUID__"] = 810170301705003368
        self.vs[12]["mm__"] = """hasAttribute_T"""
        self.vs[12]["GUID__"] = 95301687509202679
        self.vs[13]["name"] = """eq_"""
        self.vs[13]["mm__"] = """Equation"""
        self.vs[13]["GUID__"] = 3025236546510442525
        self.vs[14]["mm__"] = """leftExpr"""
        self.vs[14]["GUID__"] = 7491511539615629596
        self.vs[15]["mm__"] = """rightExpr"""
        self.vs[15]["GUID__"] = 1453936257435267703
        self.vs[16]["mm__"] = """hasArgs"""
        self.vs[16]["GUID__"] = 7222570128436826604
        self.vs[17]["mm__"] = """hasArgs"""
        self.vs[17]["GUID__"] = 346961681022384266
        self.vs[18]["name"] = """Swc2EcuMapping_"""
        self.vs[18]["mm__"] = """Constant"""
        self.vs[18]["Type"] = """'String'"""
        self.vs[18]["GUID__"] = 1056087720806102718
        self.vs[19]["mm__"] = """hasAttribute_T"""
        self.vs[19]["GUID__"] = 6210876364171431094
        self.vs[20]["name"] = """eq_"""
        self.vs[20]["mm__"] = """Equation"""
        self.vs[20]["GUID__"] = 8870473924811405716
        self.vs[21]["mm__"] = """leftExpr"""
        self.vs[21]["GUID__"] = 8390984963889962096
        self.vs[22]["mm__"] = """rightExpr"""
        self.vs[22]["GUID__"] = 1239941924572115749
        self.vs[23]["name"] = """solveRef"""
        self.vs[23]["mm__"] = """Constant"""
        self.vs[23]["Type"] = """'String'"""
        self.vs[23]["GUID__"] = 1473277815286855513
        self.vs[24]["mm__"] = """match_contains"""
        self.vs[24]["GUID__"] = 1236881482412626061
        self.vs[25]["mm__"] = """match_contains"""
        self.vs[25]["GUID__"] = 2654387224269528377
        self.vs[26]["mm__"] = """match_contains"""
        self.vs[26]["GUID__"] = 52992186442165343
        self.vs[27]["name"] = """name"""
        self.vs[27]["mm__"] = """Attribute"""
        self.vs[27]["Type"] = """'String'"""
        self.vs[27]["GUID__"] = 7768472211935080218
        self.vs[28]["name"] = """shortName"""
        self.vs[28]["mm__"] = """Attribute"""
        self.vs[28]["Type"] = """'String'"""
        self.vs[28]["GUID__"] = 1490596617357491644
        self.vs[29]["name"] = """ApplyAttribute"""
        self.vs[29]["mm__"] = """Attribute"""
        self.vs[29]["Type"] = """'String'"""
        self.vs[29]["GUID__"] = 1377654045688320000

