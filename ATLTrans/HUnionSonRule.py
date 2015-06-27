

from core.himesis import Himesis

class HUnionSonRule(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HUnionSonRule.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HUnionSonRule, self).__init__(name='HUnionSonRule', num_nodes=31, edges=[])
        
        # Add the edges
        self.add_edges([[0, 25], [25, 3], [0, 26], [26, 4], [0, 27], [27, 5], [1, 9], [9, 6], [1, 10], [10, 7], [4, 11], [11, 3], [3, 12], [12, 5], [7, 8], [8, 6], [7, 28], [28, 4], [6, 29], [29, 3], [6, 30], [30, 5], [6, 13], [13, 14], [15, 16], [16, 14], [15, 17], [17, 18], [7, 19], [19, 20], [21, 22], [22, 20], [21, 23], [23, 24], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """UnionSonRule"""
        self["GUID__"] = 3541520595692850211
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 3453930305046814046
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 1318986191048718560
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 8170194843506434719
        self.vs[3]["name"] = """"""
        self.vs[3]["classtype"] = """Family"""
        self.vs[3]["mm__"] = """Family"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 1418907978798279182
        self.vs[4]["name"] = """"""
        self.vs[4]["classtype"] = """HouseholdRoot"""
        self.vs[4]["mm__"] = """HouseholdRoot"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = 2239191085772265560
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """Member"""
        self.vs[5]["mm__"] = """Member"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 8690967788592859349
        self.vs[6]["name"] = """"""
        self.vs[6]["classtype"] = """Man"""
        self.vs[6]["mm__"] = """Man"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = 2573339204871057159
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """CommunityRoot"""
        self.vs[7]["mm__"] = """CommunityRoot"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = 711929094857150743
        self.vs[8]["associationType"] = """has"""
        self.vs[8]["mm__"] = """directLink_T"""
        self.vs[8]["GUID__"] = 5453410470050680048
        self.vs[9]["mm__"] = """apply_contains"""
        self.vs[9]["GUID__"] = 3001428909457494314
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 3912040371916924708
        self.vs[11]["associationType"] = """have"""
        self.vs[11]["mm__"] = """directLink_S"""
        self.vs[11]["GUID__"] = 7391253864267243754
        self.vs[12]["associationType"] = """son"""
        self.vs[12]["mm__"] = """directLink_S"""
        self.vs[12]["GUID__"] = 3689514867987605658
        self.vs[13]["mm__"] = """hasAttribute_T"""
        self.vs[13]["GUID__"] = 9140695439831940734
        self.vs[14]["name"] = """ApplyAttribute"""
        self.vs[14]["mm__"] = """Attribute"""
        self.vs[14]["Type"] = """'String'"""
        self.vs[14]["GUID__"] = 7006101416770012680
        self.vs[15]["name"] = """eq_"""
        self.vs[15]["mm__"] = """Equation"""
        self.vs[15]["GUID__"] = 5605736295905641101
        self.vs[16]["mm__"] = """leftExpr"""
        self.vs[16]["GUID__"] = 1372055130607556439
        self.vs[17]["mm__"] = """rightExpr"""
        self.vs[17]["GUID__"] = 5963265585904441397
        self.vs[18]["name"] = """famMemberSon"""
        self.vs[18]["mm__"] = """Constant"""
        self.vs[18]["Type"] = """'String'"""
        self.vs[18]["GUID__"] = 8611833123024243249
        self.vs[19]["mm__"] = """hasAttribute_T"""
        self.vs[19]["GUID__"] = 4234435244153092841
        self.vs[20]["name"] = """ApplyAttribute"""
        self.vs[20]["mm__"] = """Attribute"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["GUID__"] = 2794357604125218536
        self.vs[21]["name"] = """eq_"""
        self.vs[21]["mm__"] = """Equation"""
        self.vs[21]["GUID__"] = 5289896097703610181
        self.vs[22]["mm__"] = """leftExpr"""
        self.vs[22]["GUID__"] = 5628396505680526553
        self.vs[23]["mm__"] = """rightExpr"""
        self.vs[23]["GUID__"] = 3348166726734115110
        self.vs[24]["name"] = """root"""
        self.vs[24]["mm__"] = """Constant"""
        self.vs[24]["Type"] = """'String'"""
        self.vs[24]["GUID__"] = 6488265130118311438
        self.vs[25]["mm__"] = """match_contains"""
        self.vs[25]["GUID__"] = 8727647913454085111
        self.vs[26]["mm__"] = """match_contains"""
        self.vs[26]["GUID__"] = 3182382818369973340
        self.vs[27]["mm__"] = """match_contains"""
        self.vs[27]["GUID__"] = 5100757958105142068
        self.vs[28]["type"] = """ruleDef"""
        self.vs[28]["mm__"] = """backward_link"""
        self.vs[28]["GUID__"] = 6849360824570433929
        self.vs[29]["type"] = """ruleDef"""
        self.vs[29]["mm__"] = """backward_link"""
        self.vs[29]["GUID__"] = 7961407954274807310
        self.vs[30]["type"] = """ruleDef"""
        self.vs[30]["mm__"] = """backward_link"""
        self.vs[30]["GUID__"] = 628328046941243810

