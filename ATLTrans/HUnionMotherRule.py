

from core.himesis import Himesis

class HUnionMotherRule(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HUnionMotherRule.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HUnionMotherRule, self).__init__(name='HUnionMotherRule', num_nodes=31, edges=[])
        
        # Add the edges
        self.add_edges([[0, 25], [25, 3], [0, 26], [26, 4], [0, 27], [27, 5], [1, 9], [9, 6], [1, 10], [10, 7], [3, 11], [11, 4], [4, 12], [12, 5], [6, 8], [8, 7], [6, 28], [28, 3], [7, 29], [29, 4], [7, 30], [30, 5], [6, 13], [13, 14], [15, 16], [16, 14], [15, 17], [17, 18], [7, 19], [19, 20], [21, 22], [22, 20], [21, 23], [23, 24], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """UnionMotherRule"""
        self["GUID__"] = 4706084632775029163
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 3710893763608157629
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 7355300863617039118
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 5623564694034587704
        self.vs[3]["name"] = """"""
        self.vs[3]["classtype"] = """HouseholdRoot"""
        self.vs[3]["mm__"] = """HouseholdRoot"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 4972392594947355466
        self.vs[4]["name"] = """"""
        self.vs[4]["classtype"] = """Family"""
        self.vs[4]["mm__"] = """Family"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = 1583262658088707459
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """Member"""
        self.vs[5]["mm__"] = """Member"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 4369856629168046829
        self.vs[6]["name"] = """"""
        self.vs[6]["classtype"] = """CommunityRoot"""
        self.vs[6]["mm__"] = """CommunityRoot"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = 5562763637798329565
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """Woman"""
        self.vs[7]["mm__"] = """Woman"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = 1218194295918650953
        self.vs[8]["associationType"] = """has"""
        self.vs[8]["mm__"] = """directLink_T"""
        self.vs[8]["GUID__"] = 8731646616672057564
        self.vs[9]["mm__"] = """apply_contains"""
        self.vs[9]["GUID__"] = 6909460221414622075
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 4807835722553328126
        self.vs[11]["associationType"] = """have"""
        self.vs[11]["mm__"] = """directLink_S"""
        self.vs[11]["GUID__"] = 71411737742832168
        self.vs[12]["associationType"] = """mother"""
        self.vs[12]["mm__"] = """directLink_S"""
        self.vs[12]["GUID__"] = 1113564736266834885
        self.vs[13]["mm__"] = """hasAttribute_T"""
        self.vs[13]["GUID__"] = 2074923851841654110
        self.vs[14]["name"] = """ApplyAttribute"""
        self.vs[14]["mm__"] = """Attribute"""
        self.vs[14]["Type"] = """'String'"""
        self.vs[14]["GUID__"] = 7670518150916608072
        self.vs[15]["name"] = """eq_"""
        self.vs[15]["mm__"] = """Equation"""
        self.vs[15]["GUID__"] = 5036057395007379296
        self.vs[16]["mm__"] = """leftExpr"""
        self.vs[16]["GUID__"] = 4970763585356815083
        self.vs[17]["mm__"] = """rightExpr"""
        self.vs[17]["GUID__"] = 3225467870896464360
        self.vs[18]["name"] = """root"""
        self.vs[18]["mm__"] = """Constant"""
        self.vs[18]["Type"] = """'String'"""
        self.vs[18]["GUID__"] = 7399213886664652206
        self.vs[19]["mm__"] = """hasAttribute_T"""
        self.vs[19]["GUID__"] = 2400348631948796166
        self.vs[20]["name"] = """ApplyAttribute"""
        self.vs[20]["mm__"] = """Attribute"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["GUID__"] = 7794102789817828866
        self.vs[21]["name"] = """eq_"""
        self.vs[21]["mm__"] = """Equation"""
        self.vs[21]["GUID__"] = 7535327743787767692
        self.vs[22]["mm__"] = """leftExpr"""
        self.vs[22]["GUID__"] = 3927385275696813827
        self.vs[23]["mm__"] = """rightExpr"""
        self.vs[23]["GUID__"] = 2042564041842537083
        self.vs[24]["name"] = """famMemberMother"""
        self.vs[24]["mm__"] = """Constant"""
        self.vs[24]["Type"] = """'String'"""
        self.vs[24]["GUID__"] = 7521218716902315824
        self.vs[25]["mm__"] = """match_contains"""
        self.vs[25]["GUID__"] = 8349246915840883195
        self.vs[26]["mm__"] = """match_contains"""
        self.vs[26]["GUID__"] = 7524838804051234116
        self.vs[27]["mm__"] = """match_contains"""
        self.vs[27]["GUID__"] = 6776191552991307184
        self.vs[28]["type"] = """ruleDef"""
        self.vs[28]["mm__"] = """backward_link"""
        self.vs[28]["GUID__"] = 1841349857312859565
        self.vs[29]["type"] = """ruleDef"""
        self.vs[29]["mm__"] = """backward_link"""
        self.vs[29]["GUID__"] = 3499451108614629983
        self.vs[30]["type"] = """ruleDef"""
        self.vs[30]["mm__"] = """backward_link"""
        self.vs[30]["GUID__"] = 2693561506228849547

