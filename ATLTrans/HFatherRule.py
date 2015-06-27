

from core.himesis import Himesis

class HFatherRule(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HFatherRule.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HFatherRule, self).__init__(name='HFatherRule', num_nodes=28, edges=[])
        
        # Add the edges
        self.add_edges([[0, 10], [10, 3], [0, 11], [11, 4], [1, 6], [6, 5], [3, 7], [7, 4], [3, 12], [12, 24], [4, 13], [13, 25], [5, 14], [14, 26], [15, 16], [16, 26], [15, 17], [17, 8], [5, 18], [18, 27], [19, 20], [20, 27], [19, 21], [9, 22], [22, 25], [9, 23], [23, 24], [21, 9], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """FatherRule"""
        self["GUID__"] = 3046486710100042329
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 9114236163715680844
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 8522774374238101600
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 6942070342480178269
        self.vs[3]["name"] = """"""
        self.vs[3]["classtype"] = """Family"""
        self.vs[3]["mm__"] = """Family"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 4951011629579273661
        self.vs[4]["name"] = """"""
        self.vs[4]["classtype"] = """Member"""
        self.vs[4]["mm__"] = """Member"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = 3917541545754202467
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """Man"""
        self.vs[5]["mm__"] = """Man"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = 6470362105032644726
        self.vs[6]["mm__"] = """apply_contains"""
        self.vs[6]["GUID__"] = 5156073703192303449
        self.vs[7]["associationType"] = """father"""
        self.vs[7]["mm__"] = """directLink_S"""
        self.vs[7]["GUID__"] = 539895013935623433
        self.vs[8]["name"] = """famMemberFather"""
        self.vs[8]["mm__"] = """Constant"""
        self.vs[8]["Type"] = """'String'"""
        self.vs[8]["GUID__"] = 1457407358008708064
        self.vs[9]["name"] = """Concat25"""
        self.vs[9]["mm__"] = """Concat"""
        self.vs[9]["Type"] = """'String'"""
        self.vs[9]["GUID__"] = 5564012802193101995
        self.vs[10]["mm__"] = """match_contains"""
        self.vs[10]["GUID__"] = 3142929046682116473
        self.vs[11]["mm__"] = """match_contains"""
        self.vs[11]["GUID__"] = 7132010249356621317
        self.vs[12]["mm__"] = """hasAttribute_S"""
        self.vs[12]["GUID__"] = 9153807583289271711
        self.vs[13]["mm__"] = """hasAttribute_S"""
        self.vs[13]["GUID__"] = 6959972757835076980
        self.vs[14]["mm__"] = """hasAttribute_T"""
        self.vs[14]["GUID__"] = 5017799400072165898
        self.vs[15]["name"] = """eq_"""
        self.vs[15]["mm__"] = """Equation"""
        self.vs[15]["GUID__"] = 6114103124580037104
        self.vs[16]["mm__"] = """leftExpr"""
        self.vs[16]["GUID__"] = 5313668312549732403
        self.vs[17]["mm__"] = """rightExpr"""
        self.vs[17]["GUID__"] = 268347621053803152
        self.vs[18]["mm__"] = """hasAttribute_T"""
        self.vs[18]["GUID__"] = 6659576290408920312
        self.vs[19]["name"] = """eq_"""
        self.vs[19]["mm__"] = """Equation"""
        self.vs[19]["GUID__"] = 4944971660908682818
        self.vs[20]["mm__"] = """leftExpr"""
        self.vs[20]["GUID__"] = 4148724306613045645
        self.vs[21]["mm__"] = """rightExpr"""
        self.vs[21]["GUID__"] = 1206203054404359755
        self.vs[22]["mm__"] = """hasArgs"""
        self.vs[22]["GUID__"] = 6401143966041444926
        self.vs[23]["mm__"] = """hasArgs"""
        self.vs[23]["GUID__"] = 835463066837585676
        self.vs[24]["name"] = """name"""
        self.vs[24]["mm__"] = """Attribute"""
        self.vs[24]["Type"] = """'String'"""
        self.vs[24]["GUID__"] = 3573636148019412751
        self.vs[25]["name"] = """name"""
        self.vs[25]["mm__"] = """Attribute"""
        self.vs[25]["Type"] = """'String'"""
        self.vs[25]["GUID__"] = 7745905441355555442
        self.vs[26]["name"] = """ApplyAttribute"""
        self.vs[26]["mm__"] = """Attribute"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["GUID__"] = 6359065544102840427
        self.vs[27]["name"] = """name"""
        self.vs[27]["mm__"] = """Attribute"""
        self.vs[27]["Type"] = """'String'"""
        self.vs[27]["GUID__"] = 8265432559275298044

