

from core.himesis import Himesis

class HDaughterRule(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HDaughterRule.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HDaughterRule, self).__init__(name='HDaughterRule', num_nodes=28, edges=[])
        
        # Add the edges
        self.add_edges([[0, 10], [10, 3], [0, 11], [11, 4], [1, 6], [6, 5], [3, 7], [7, 4], [3, 12], [12, 24], [4, 13], [13, 25], [5, 14], [14, 26], [15, 16], [16, 26], [15, 17], [17, 8], [5, 18], [18, 27], [19, 20], [20, 27], [19, 21], [9, 22], [22, 25], [9, 23], [23, 24], [21, 9], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """DaughterRule"""
        self["GUID__"] = 306755394590966201
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 2725239882200584502
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 8616720206745858884
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 4098526761131590297
        self.vs[3]["name"] = """"""
        self.vs[3]["classtype"] = """Family"""
        self.vs[3]["mm__"] = """Family"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 8573595960349593540
        self.vs[4]["name"] = """"""
        self.vs[4]["classtype"] = """Member"""
        self.vs[4]["mm__"] = """Member"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = 1592359773121052988
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """Woman"""
        self.vs[5]["mm__"] = """Woman"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = 3530720354649252604
        self.vs[6]["mm__"] = """apply_contains"""
        self.vs[6]["GUID__"] = 4682375168839824505
        self.vs[7]["associationType"] = """daughter"""
        self.vs[7]["mm__"] = """directLink_S"""
        self.vs[7]["GUID__"] = 8429373444608293950
        self.vs[8]["name"] = """famMemberDaughter"""
        self.vs[8]["mm__"] = """Constant"""
        self.vs[8]["Type"] = """'String'"""
        self.vs[8]["GUID__"] = 7998833896010568914
        self.vs[9]["name"] = """Concat25"""
        self.vs[9]["mm__"] = """Concat"""
        self.vs[9]["Type"] = """'String'"""
        self.vs[9]["GUID__"] = 4922917558625280260
        self.vs[10]["mm__"] = """match_contains"""
        self.vs[10]["GUID__"] = 3977085272551649725
        self.vs[11]["mm__"] = """match_contains"""
        self.vs[11]["GUID__"] = 7039778024377921446
        self.vs[12]["mm__"] = """hasAttribute_S"""
        self.vs[12]["GUID__"] = 3833274542832345473
        self.vs[13]["mm__"] = """hasAttribute_S"""
        self.vs[13]["GUID__"] = 7530934858318907454
        self.vs[14]["mm__"] = """hasAttribute_T"""
        self.vs[14]["GUID__"] = 2849606153526278272
        self.vs[15]["name"] = """eq_"""
        self.vs[15]["mm__"] = """Equation"""
        self.vs[15]["GUID__"] = 7216855437790478687
        self.vs[16]["mm__"] = """leftExpr"""
        self.vs[16]["GUID__"] = 2364750759307347128
        self.vs[17]["mm__"] = """rightExpr"""
        self.vs[17]["GUID__"] = 8954353876030319879
        self.vs[18]["mm__"] = """hasAttribute_T"""
        self.vs[18]["GUID__"] = 7034849043195804176
        self.vs[19]["name"] = """eq_"""
        self.vs[19]["mm__"] = """Equation"""
        self.vs[19]["GUID__"] = 8395319763293697
        self.vs[20]["mm__"] = """leftExpr"""
        self.vs[20]["GUID__"] = 371323844071842194
        self.vs[21]["mm__"] = """rightExpr"""
        self.vs[21]["GUID__"] = 1622536558985102301
        self.vs[22]["mm__"] = """hasArgs"""
        self.vs[22]["GUID__"] = 7866213531810988047
        self.vs[23]["mm__"] = """hasArgs"""
        self.vs[23]["GUID__"] = 4034022507457492018
        self.vs[24]["name"] = """name"""
        self.vs[24]["mm__"] = """Attribute"""
        self.vs[24]["Type"] = """'String'"""
        self.vs[24]["GUID__"] = 7846379032656459107
        self.vs[25]["name"] = """name"""
        self.vs[25]["mm__"] = """Attribute"""
        self.vs[25]["Type"] = """'String'"""
        self.vs[25]["GUID__"] = 2409331435281152825
        self.vs[26]["name"] = """ApplyAttribute"""
        self.vs[26]["mm__"] = """Attribute"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["GUID__"] = 4460774008228854855
        self.vs[27]["name"] = """name"""
        self.vs[27]["mm__"] = """Attribute"""
        self.vs[27]["Type"] = """'String'"""
        self.vs[27]["GUID__"] = 6235159657510095909

