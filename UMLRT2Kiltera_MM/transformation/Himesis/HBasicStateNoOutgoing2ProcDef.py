

from core.himesis import Himesis

class HBasicStateNoOutgoing2ProcDef(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HBasicStateNoOutgoing2ProcDef.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HBasicStateNoOutgoing2ProcDef, self).__init__(name='HBasicStateNoOutgoing2ProcDef', num_nodes=29, edges=[])
        
        # Add the edges
        self.add_edges([[8, 0], [0, 7], [18, 14], [14, 27], [17, 15], [15, 26], [19, 16], [16, 28], [8, 1], [1, 22], [5, 2], [2, 12], [2, 13], [6, 3], [3, 4], [4, 10], [10, 20], [4, 11], [11, 21], [9, 4], [6, 5], [17, 23], [18, 24], [19, 25], [13, 7], [12, 8], [8, 9], [23, 20], [24, 21], [25, 22]])
        # Set the graph attributes
        self["mm__"] = ['UMLRT2Kiltera_MM']
        self["name"] = """BasicStateNoOutgoing2ProcDef"""
        self["GUID__"] = 6099964635145944144
        
        # Set the node attributes
        self.vs[0]["associationType"] = """p"""
        self.vs[0]["mm__"] = """directLink_T"""
        self.vs[0]["GUID__"] = 8594045057616115267
        self.vs[1]["mm__"] = """hasAttribute_T"""
        self.vs[1]["GUID__"] = 2652801976527318279
        self.vs[2]["mm__"] = """ApplyModel"""
        self.vs[2]["GUID__"] = 2246186575130914086
        self.vs[3]["mm__"] = """match_contains"""
        self.vs[3]["GUID__"] = 2837358535469550779
        self.vs[4]["name"] = """state1"""
        self.vs[4]["classtype"] = """State"""
        self.vs[4]["mm__"] = """State"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = 7415144559275781691
        self.vs[5]["mm__"] = """paired_with"""
        self.vs[5]["GUID__"] = 6910257610741535439
        self.vs[6]["mm__"] = """MatchModel"""
        self.vs[6]["GUID__"] = 5384204831269294915
        self.vs[7]["name"] = """null1"""
        self.vs[7]["classtype"] = """Null"""
        self.vs[7]["mm__"] = """Null"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = 8726334918046482046
        self.vs[8]["name"] = """procdef1"""
        self.vs[8]["classtype"] = """ProcDef"""
        self.vs[8]["mm__"] = """ProcDef"""
        self.vs[8]["cardinality"] = """1"""
        self.vs[8]["GUID__"] = 3867775458825975895
        self.vs[9]["mm__"] = """backward_link"""
        self.vs[9]["type"] = """ruleDef"""
        self.vs[9]["GUID__"] = 1565499112901273858
        self.vs[10]["mm__"] = """hasAttribute_S"""
        self.vs[10]["GUID__"] = 5419670648108149462
        self.vs[11]["mm__"] = """hasAttribute_S"""
        self.vs[11]["GUID__"] = 6302259747763698082
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 5225940711097184717
        self.vs[13]["mm__"] = """apply_contains"""
        self.vs[13]["GUID__"] = 6461955502429471902
        self.vs[14]["mm__"] = """rightExpr"""
        self.vs[14]["GUID__"] = 5682278460184926931
        self.vs[15]["mm__"] = """rightExpr"""
        self.vs[15]["GUID__"] = 6826874363091670959
        self.vs[16]["mm__"] = """rightExpr"""
        self.vs[16]["GUID__"] = 4017585897012792283
        self.vs[17]["name"] = """eq1"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 3169458542573725647
        self.vs[18]["name"] = """eq2"""
        self.vs[18]["mm__"] = """Equation"""
        self.vs[18]["GUID__"] = 3703076769387195771
        self.vs[19]["name"] = """eq3"""
        self.vs[19]["mm__"] = """Equation"""
        self.vs[19]["GUID__"] = 520701530960340312
        self.vs[20]["name"] = """isComposite"""
        self.vs[20]["Type"] = """'Bool'"""
        self.vs[20]["mm__"] = """Attribute"""
        self.vs[20]["GUID__"] = 1242959223121352013
        self.vs[21]["name"] = """hasOutgoingTransitions"""
        self.vs[21]["Type"] = """'Bool'"""
        self.vs[21]["mm__"] = """Attribute"""
        self.vs[21]["GUID__"] = 5362055990772679204
        self.vs[22]["name"] = """pivot"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["GUID__"] = 2915674714696930349
        self.vs[23]["mm__"] = """leftExpr"""
        self.vs[23]["GUID__"] = 4494441341044070787
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = 1296198394194057184
        self.vs[25]["mm__"] = """leftExpr"""
        self.vs[25]["GUID__"] = 7661029515234221783
        self.vs[26]["name"] = """false"""
        self.vs[26]["Type"] = """'Bool'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 8184327863903859887
        self.vs[27]["name"] = """false"""
        self.vs[27]["Type"] = """'Bool'"""
        self.vs[27]["mm__"] = """Constant"""
        self.vs[27]["GUID__"] = 2898597903183493500
        self.vs[28]["name"] = """procdef"""
        self.vs[28]["Type"] = """'String'"""
        self.vs[28]["mm__"] = """Constant"""
        self.vs[28]["GUID__"] = 4678187015003537421

