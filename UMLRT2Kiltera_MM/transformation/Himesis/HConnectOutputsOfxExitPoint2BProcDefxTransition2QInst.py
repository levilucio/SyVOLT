

from core.himesis import Himesis

class HConnectOutputsOfxExitPoint2BProcDefxTransition2QInst(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HConnectOutputsOfxExitPoint2BProcDefxTransition2QInst.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HConnectOutputsOfxExitPoint2BProcDefxTransition2QInst, self).__init__(name='HConnectOutputsOfxExitPoint2BProcDefxTransition2QInst', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[8, 0], [0, 6], [7, 1], [1, 5], [15, 9], [9, 25], [16, 10], [10, 26], [7, 11], [11, 19], [5, 12], [12, 20], [3, 2], [2, 17], [2, 18], [4, 13], [13, 8], [4, 14], [14, 6], [4, 3], [15, 23], [16, 24], [17, 7], [18, 5], [5, 22], [22, 6], [23, 19], [24, 20], [7, 21], [21, 8]])
        # Set the graph attributes
        self["mm__"] = ['UMLRT2Kiltera_MM']
        self["name"] = """ConnectOutputsOfxExitPoint2BProcDefxTransition2QInst"""
        self["GUID__"] = 3287395769891270121
        
        # Set the node attributes
        self.vs[0]["associationType"] = """outgoingTransitions"""
        self.vs[0]["mm__"] = """directLink_S"""
        self.vs[0]["GUID__"] = 7107337269178138801
        self.vs[1]["associationType"] = """p"""
        self.vs[1]["mm__"] = """directLink_T"""
        self.vs[1]["GUID__"] = 1588969512102861295
        self.vs[2]["mm__"] = """ApplyModel"""
        self.vs[2]["GUID__"] = 1278892475090478914
        self.vs[3]["mm__"] = """paired_with"""
        self.vs[3]["GUID__"] = 6144896627918011069
        self.vs[4]["mm__"] = """MatchModel"""
        self.vs[4]["GUID__"] = 9133034264210581729
        self.vs[5]["name"] = """inst1"""
        self.vs[5]["classtype"] = """Inst"""
        self.vs[5]["mm__"] = """Inst"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = 8720458462339832036
        self.vs[6]["name"] = """transition1"""
        self.vs[6]["classtype"] = """Transition"""
        self.vs[6]["mm__"] = """Transition"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = 7093353581503719188
        self.vs[7]["name"] = """par1"""
        self.vs[7]["classtype"] = """Par"""
        self.vs[7]["mm__"] = """Par"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = 6456054054278398058
        self.vs[8]["name"] = """exitpoint1"""
        self.vs[8]["classtype"] = """ExitPoint"""
        self.vs[8]["mm__"] = """ExitPoint"""
        self.vs[8]["cardinality"] = """+"""
        self.vs[8]["GUID__"] = 8784447958320551310
        self.vs[9]["mm__"] = """rightExpr"""
        self.vs[9]["GUID__"] = 7198872125762678295
        self.vs[10]["mm__"] = """rightExpr"""
        self.vs[10]["GUID__"] = 8340031755255525833
        self.vs[11]["mm__"] = """hasAttribute_T"""
        self.vs[11]["GUID__"] = 8212581455348153337
        self.vs[12]["mm__"] = """hasAttribute_T"""
        self.vs[12]["GUID__"] = 195782553637393678
        self.vs[13]["mm__"] = """match_contains"""
        self.vs[13]["GUID__"] = 1811012472429481907
        self.vs[14]["mm__"] = """match_contains"""
        self.vs[14]["GUID__"] = 8168307660565605039
        self.vs[15]["name"] = """eq1"""
        self.vs[15]["mm__"] = """Equation"""
        self.vs[15]["GUID__"] = 5079826567480131082
        self.vs[16]["name"] = """eq2"""
        self.vs[16]["mm__"] = """Equation"""
        self.vs[16]["GUID__"] = 1632119297697528428
        self.vs[17]["mm__"] = """apply_contains"""
        self.vs[17]["GUID__"] = 6014174692767395440
        self.vs[18]["mm__"] = """apply_contains"""
        self.vs[18]["GUID__"] = 4097537182578875191
        self.vs[19]["name"] = """pivot"""
        self.vs[19]["mm__"] = """Attribute"""
        self.vs[19]["Type"] = """'String'"""
        self.vs[19]["GUID__"] = 1443244960555876634
        self.vs[20]["name"] = """pivot"""
        self.vs[20]["mm__"] = """Attribute"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["GUID__"] = 1408272473276621841
        self.vs[21]["type"] = """ruleDef"""
        self.vs[21]["mm__"] = """backward_link"""
        self.vs[21]["GUID__"] = 4102439250594306478
        self.vs[22]["type"] = """ruleDef"""
        self.vs[22]["mm__"] = """backward_link"""
        self.vs[22]["GUID__"] = 2784324854952829275
        self.vs[23]["mm__"] = """leftExpr"""
        self.vs[23]["GUID__"] = 4994027069063479656
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = 2663190492996055969
        self.vs[25]["name"] = """parexitpoint"""
        self.vs[25]["mm__"] = """Constant"""
        self.vs[25]["Type"] = """'String'"""
        self.vs[25]["GUID__"] = 6157466119664277789
        self.vs[26]["name"] = """instfortrans"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["GUID__"] = 4956886484288888779

