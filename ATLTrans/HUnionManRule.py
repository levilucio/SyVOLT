

from core.himesis import Himesis

class HUnionManRule(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HUnionManRule.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HUnionManRule, self).__init__(name='HUnionManRule', num_nodes=31, edges=[])
        
        # Add the edges
        self.add_edges([[0, 25], [25, 3], [0, 26], [26, 4], [0, 27], [27, 5], [1, 9], [9, 6], [1, 10], [10, 7], [3, 11], [11, 4], [5, 12], [12, 3], [7, 8], [8, 6], [6, 28], [28, 4], [7, 29], [29, 5], [6, 30], [30, 3], [6, 13], [13, 14], [15, 16], [16, 14], [15, 17], [17, 18], [7, 19], [19, 20], [21, 22], [22, 20], [21, 23], [23, 24], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """UnionManRule"""
        self["GUID__"] = 8436475798075113532
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 7361093160426254132
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 3867111869186057762
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 1168394164482762355
        self.vs[3]["name"] = """"""
        self.vs[3]["classtype"] = """Family"""
        self.vs[3]["mm__"] = """Family"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 7459878323988677681
        self.vs[4]["name"] = """"""
        self.vs[4]["classtype"] = """Member"""
        self.vs[4]["mm__"] = """Member"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = 8164384913322332085
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """HouseholdRoot"""
        self.vs[5]["mm__"] = """HouseholdRoot"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 847752224322527329
        self.vs[6]["name"] = """"""
        self.vs[6]["classtype"] = """Man"""
        self.vs[6]["mm__"] = """Man"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = 5192576760823095399
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """CommunityRoot"""
        self.vs[7]["mm__"] = """CommunityRoot"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = 5433294242944732357
        self.vs[8]["associationType"] = """has"""
        self.vs[8]["mm__"] = """directLink_T"""
        self.vs[8]["GUID__"] = 22605775612797215
        self.vs[9]["mm__"] = """apply_contains"""
        self.vs[9]["GUID__"] = 6942192352627504013
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 7737138140395462039
        self.vs[11]["associationType"] = """father"""
        self.vs[11]["mm__"] = """directLink_S"""
        self.vs[11]["GUID__"] = 3698231753272940381
        self.vs[12]["associationType"] = """have"""
        self.vs[12]["mm__"] = """directLink_S"""
        self.vs[12]["GUID__"] = 6868201881532527663
        self.vs[13]["mm__"] = """hasAttribute_T"""
        self.vs[13]["GUID__"] = 824110028735626235
        self.vs[14]["name"] = """ApplyAttribute"""
        self.vs[14]["mm__"] = """Attribute"""
        self.vs[14]["Type"] = """'String'"""
        self.vs[14]["GUID__"] = 346459928543351491
        self.vs[15]["name"] = """eq_"""
        self.vs[15]["mm__"] = """Equation"""
        self.vs[15]["GUID__"] = 8765660596022607244
        self.vs[16]["mm__"] = """leftExpr"""
        self.vs[16]["GUID__"] = 7279550722357884644
        self.vs[17]["mm__"] = """rightExpr"""
        self.vs[17]["GUID__"] = 5072061577104747728
        self.vs[18]["name"] = """famMemberFather"""
        self.vs[18]["mm__"] = """Constant"""
        self.vs[18]["Type"] = """'String'"""
        self.vs[18]["GUID__"] = 7742838131884166822
        self.vs[19]["mm__"] = """hasAttribute_T"""
        self.vs[19]["GUID__"] = 4069004138657746834
        self.vs[20]["name"] = """ApplyAttribute"""
        self.vs[20]["mm__"] = """Attribute"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["GUID__"] = 8642582035705828672
        self.vs[21]["name"] = """eq_"""
        self.vs[21]["mm__"] = """Equation"""
        self.vs[21]["GUID__"] = 1528931020449697813
        self.vs[22]["mm__"] = """leftExpr"""
        self.vs[22]["GUID__"] = 6432895277856872632
        self.vs[23]["mm__"] = """rightExpr"""
        self.vs[23]["GUID__"] = 6642653567991021500
        self.vs[24]["name"] = """root"""
        self.vs[24]["mm__"] = """Constant"""
        self.vs[24]["Type"] = """'String'"""
        self.vs[24]["GUID__"] = 9218026963791259828
        self.vs[25]["mm__"] = """match_contains"""
        self.vs[25]["GUID__"] = 1348004204868534342
        self.vs[26]["mm__"] = """match_contains"""
        self.vs[26]["GUID__"] = 150575170077597988
        self.vs[27]["mm__"] = """match_contains"""
        self.vs[27]["GUID__"] = 4456926317859050978
        self.vs[28]["type"] = """ruleDef"""
        self.vs[28]["mm__"] = """backward_link"""
        self.vs[28]["GUID__"] = 7559566677165040475
        self.vs[29]["type"] = """ruleDef"""
        self.vs[29]["mm__"] = """backward_link"""
        self.vs[29]["GUID__"] = 6817929537372789675
        self.vs[30]["type"] = """ruleDef"""
        self.vs[30]["mm__"] = """backward_link"""
        self.vs[30]["GUID__"] = 4119843106421743901

