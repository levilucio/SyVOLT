

from core.himesis import Himesis

class HSonRule(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HSonRule.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HSonRule, self).__init__(name='HSonRule', num_nodes=28, edges=[])
        
        # Add the edges
        self.add_edges([[0, 10], [10, 3], [0, 11], [11, 4], [1, 6], [6, 5], [3, 7], [7, 4], [3, 12], [12, 24], [4, 13], [13, 25], [5, 14], [14, 26], [15, 16], [16, 26], [15, 17], [17, 8], [5, 18], [18, 27], [19, 20], [20, 27], [19, 21], [9, 22], [22, 25], [9, 23], [23, 24], [21, 9], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """SonRule"""
        self["GUID__"] = 3039647828217524972
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 4387398855359802277
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 1010999523399142191
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 1513796799329542433
        self.vs[3]["name"] = """"""
        self.vs[3]["classtype"] = """Family"""
        self.vs[3]["mm__"] = """Family"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 8411433876122097588
        self.vs[4]["name"] = """"""
        self.vs[4]["classtype"] = """Member"""
        self.vs[4]["mm__"] = """Member"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = 5376184230535463541
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """Man"""
        self.vs[5]["mm__"] = """Man"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = 2388843785280708893
        self.vs[6]["mm__"] = """apply_contains"""
        self.vs[6]["GUID__"] = 8810495245538604576
        self.vs[7]["associationType"] = """son"""
        self.vs[7]["mm__"] = """directLink_S"""
        self.vs[7]["GUID__"] = 3346357146859763280
        self.vs[8]["name"] = """famMemberSon"""
        self.vs[8]["mm__"] = """Constant"""
        self.vs[8]["Type"] = """'String'"""
        self.vs[8]["GUID__"] = 7706026663443862840
        self.vs[9]["name"] = """Concat25"""
        self.vs[9]["mm__"] = """Concat"""
        self.vs[9]["Type"] = """'String'"""
        self.vs[9]["GUID__"] = 742575365998845892
        self.vs[10]["mm__"] = """match_contains"""
        self.vs[10]["GUID__"] = 853924834475186777
        self.vs[11]["mm__"] = """match_contains"""
        self.vs[11]["GUID__"] = 5343271659194224138
        self.vs[12]["mm__"] = """hasAttribute_S"""
        self.vs[12]["GUID__"] = 2126931811494093964
        self.vs[13]["mm__"] = """hasAttribute_S"""
        self.vs[13]["GUID__"] = 2568319350267622732
        self.vs[14]["mm__"] = """hasAttribute_T"""
        self.vs[14]["GUID__"] = 4549423802382374847
        self.vs[15]["name"] = """eq_"""
        self.vs[15]["mm__"] = """Equation"""
        self.vs[15]["GUID__"] = 260053866910969917
        self.vs[16]["mm__"] = """leftExpr"""
        self.vs[16]["GUID__"] = 3456395307768909849
        self.vs[17]["mm__"] = """rightExpr"""
        self.vs[17]["GUID__"] = 3451442329020561555
        self.vs[18]["mm__"] = """hasAttribute_T"""
        self.vs[18]["GUID__"] = 8273976418257853154
        self.vs[19]["name"] = """eq_"""
        self.vs[19]["mm__"] = """Equation"""
        self.vs[19]["GUID__"] = 1445421282527341893
        self.vs[20]["mm__"] = """leftExpr"""
        self.vs[20]["GUID__"] = 7961867480570503888
        self.vs[21]["mm__"] = """rightExpr"""
        self.vs[21]["GUID__"] = 8184027611603921928
        self.vs[22]["mm__"] = """hasArgs"""
        self.vs[22]["GUID__"] = 3982384146589424629
        self.vs[23]["mm__"] = """hasArgs"""
        self.vs[23]["GUID__"] = 7537758993450157138
        self.vs[24]["name"] = """name"""
        self.vs[24]["mm__"] = """Attribute"""
        self.vs[24]["Type"] = """'String'"""
        self.vs[24]["GUID__"] = 3836068309322480661
        self.vs[25]["name"] = """name"""
        self.vs[25]["mm__"] = """Attribute"""
        self.vs[25]["Type"] = """'String'"""
        self.vs[25]["GUID__"] = 2947790368669924734
        self.vs[26]["name"] = """ApplyAttribute"""
        self.vs[26]["mm__"] = """Attribute"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["GUID__"] = 171585887475678757
        self.vs[27]["name"] = """name"""
        self.vs[27]["mm__"] = """Attribute"""
        self.vs[27]["Type"] = """'String'"""
        self.vs[27]["GUID__"] = 4294649902681024711

