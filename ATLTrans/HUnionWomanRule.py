

from core.himesis import Himesis

class HUnionWomanRule(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HUnionWomanRule.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HUnionWomanRule, self).__init__(name='HUnionWomanRule', num_nodes=31, edges=[])
        
        # Add the edges
        self.add_edges([[0, 25], [25, 3], [0, 26], [26, 4], [0, 27], [27, 5], [1, 9], [9, 6], [1, 10], [10, 7], [3, 11], [11, 4], [4, 12], [12, 5], [6, 8], [8, 7], [6, 28], [28, 3], [7, 29], [29, 4], [7, 30], [30, 5], [6, 13], [13, 14], [15, 16], [16, 14], [15, 17], [17, 18], [7, 19], [19, 20], [21, 22], [22, 20], [21, 23], [23, 24], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """UnionWomanRule"""
        self["GUID__"] = 3281611107083547820
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 4914254676027250039
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 5624891097942681036
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 7800762523593593980
        self.vs[3]["name"] = """"""
        self.vs[3]["classtype"] = """HouseholdRoot"""
        self.vs[3]["mm__"] = """HouseholdRoot"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 585982534574199767
        self.vs[4]["name"] = """"""
        self.vs[4]["classtype"] = """Family"""
        self.vs[4]["mm__"] = """Family"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = 4637257101367727791
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """Member"""
        self.vs[5]["mm__"] = """Member"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 3916107969826430545
        self.vs[6]["name"] = """"""
        self.vs[6]["classtype"] = """CommunityRoot"""
        self.vs[6]["mm__"] = """CommunityRoot"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = 6155077297559288642
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """Woman"""
        self.vs[7]["mm__"] = """Woman"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = 7195303199388739294
        self.vs[8]["associationType"] = """has"""
        self.vs[8]["mm__"] = """directLink_T"""
        self.vs[8]["GUID__"] = 7892611213382215881
        self.vs[9]["mm__"] = """apply_contains"""
        self.vs[9]["GUID__"] = 7677735104375512856
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 2650834300085794784
        self.vs[11]["associationType"] = """have"""
        self.vs[11]["mm__"] = """directLink_S"""
        self.vs[11]["GUID__"] = 1858350827428844521
        self.vs[12]["associationType"] = """mother"""
        self.vs[12]["mm__"] = """directLink_S"""
        self.vs[12]["GUID__"] = 7954901447244577746
        self.vs[13]["mm__"] = """hasAttribute_T"""
        self.vs[13]["GUID__"] = 7358237076388814141
        self.vs[14]["name"] = """ApplyAttribute"""
        self.vs[14]["mm__"] = """Attribute"""
        self.vs[14]["Type"] = """'String'"""
        self.vs[14]["GUID__"] = 1381987048399918131
        self.vs[15]["name"] = """eq_"""
        self.vs[15]["mm__"] = """Equation"""
        self.vs[15]["GUID__"] = 8343852387498820977
        self.vs[16]["mm__"] = """leftExpr"""
        self.vs[16]["GUID__"] = 2660901015706814159
        self.vs[17]["mm__"] = """rightExpr"""
        self.vs[17]["GUID__"] = 5169784170577672011
        self.vs[18]["name"] = """root"""
        self.vs[18]["mm__"] = """Constant"""
        self.vs[18]["Type"] = """'String'"""
        self.vs[18]["GUID__"] = 773613943497985785
        self.vs[19]["mm__"] = """hasAttribute_T"""
        self.vs[19]["GUID__"] = 4170159565913736019
        self.vs[20]["name"] = """ApplyAttribute"""
        self.vs[20]["mm__"] = """Attribute"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["GUID__"] = 3532406909035749332
        self.vs[21]["name"] = """eq_"""
        self.vs[21]["mm__"] = """Equation"""
        self.vs[21]["GUID__"] = 3661068347866243032
        self.vs[22]["mm__"] = """leftExpr"""
        self.vs[22]["GUID__"] = 8747699932616658651
        self.vs[23]["mm__"] = """rightExpr"""
        self.vs[23]["GUID__"] = 4776820845973233613
        self.vs[24]["name"] = """famMemberWoman"""
        self.vs[24]["mm__"] = """Constant"""
        self.vs[24]["Type"] = """'String'"""
        self.vs[24]["GUID__"] = 4260153728275048433
        self.vs[25]["mm__"] = """match_contains"""
        self.vs[25]["GUID__"] = 4518521902494916508
        self.vs[26]["mm__"] = """match_contains"""
        self.vs[26]["GUID__"] = 4417663026164388158
        self.vs[27]["mm__"] = """match_contains"""
        self.vs[27]["GUID__"] = 5603660764304798516
        self.vs[28]["type"] = """ruleDef"""
        self.vs[28]["mm__"] = """backward_link"""
        self.vs[28]["GUID__"] = 4904731665684167272
        self.vs[29]["type"] = """ruleDef"""
        self.vs[29]["mm__"] = """backward_link"""
        self.vs[29]["GUID__"] = 7363230038642984175
        self.vs[30]["type"] = """ruleDef"""
        self.vs[30]["mm__"] = """backward_link"""
        self.vs[30]["GUID__"] = 6625591010172102342

