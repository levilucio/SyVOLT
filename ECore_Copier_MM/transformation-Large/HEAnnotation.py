

from core.himesis import Himesis

class HEAnnotation(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HEAnnotation.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HEAnnotation, self).__init__(name='HEAnnotation', num_nodes=20, edges=[])
        
        # Add the edges
        self.add_edges([[0, 3], [3, 7], [1, 4], [4, 8], [7, 5], [5, 17], [8, 9], [9, 18], [10, 11], [11, 18], [10, 12], [12, 17], [8, 13], [13, 19], [14, 15], [15, 19], [14, 16], [16, 6], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """EAnnotation"""
        self["GUID__"] = 6697731823979103442
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 168692645805990523
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 5830811278114996678
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 5256861059255873175
        self.vs[3]["mm__"] = """match_contains"""
        self.vs[3]["GUID__"] = 1165910890986252639
        self.vs[4]["mm__"] = """apply_contains"""
        self.vs[4]["GUID__"] = 6979891316244176140
        self.vs[5]["mm__"] = """hasAttribute_S"""
        self.vs[5]["GUID__"] = 3069357429564592392
        self.vs[6]["name"] = """solveRef"""
        self.vs[6]["mm__"] = """Constant"""
        self.vs[6]["Type"] = """'String'"""
        self.vs[6]["GUID__"] = 2237892257879373516
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EAnnotation"""
        self.vs[7]["mm__"] = """EAnnotation"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 7084962301544149314
        self.vs[8]["name"] = """"""
        self.vs[8]["classtype"] = """EAnnotation"""
        self.vs[8]["mm__"] = """EAnnotation"""
        self.vs[8]["cardinality"] = """1"""
        self.vs[8]["GUID__"] = 605742560760152402
        self.vs[9]["mm__"] = """hasAttribute_T"""
        self.vs[9]["GUID__"] = 8134745298837795213
        self.vs[10]["name"] = """eq_"""
        self.vs[10]["mm__"] = """Equation"""
        self.vs[10]["GUID__"] = 7416403277377419537
        self.vs[11]["mm__"] = """leftExpr"""
        self.vs[11]["GUID__"] = 691823568592882284
        self.vs[12]["mm__"] = """rightExpr"""
        self.vs[12]["GUID__"] = 389417283762578698
        self.vs[13]["mm__"] = """hasAttribute_T"""
        self.vs[13]["GUID__"] = 353168228091083336
        self.vs[14]["name"] = """eq_"""
        self.vs[14]["mm__"] = """Equation"""
        self.vs[14]["GUID__"] = 6885283560705834929
        self.vs[15]["mm__"] = """leftExpr"""
        self.vs[15]["GUID__"] = 6966445725346417383
        self.vs[16]["mm__"] = """rightExpr"""
        self.vs[16]["GUID__"] = 5665946486398541130
        self.vs[17]["name"] = """source"""
        self.vs[17]["mm__"] = """Attribute"""
        self.vs[17]["Type"] = """'String'"""
        self.vs[17]["GUID__"] = 6471315062122959780
        self.vs[18]["name"] = """source"""
        self.vs[18]["mm__"] = """Attribute"""
        self.vs[18]["Type"] = """'String'"""
        self.vs[18]["GUID__"] = 6633000110047329372
        self.vs[19]["name"] = """ApplyAttribute"""
        self.vs[19]["mm__"] = """Attribute"""
        self.vs[19]["Type"] = """'String'"""
        self.vs[19]["GUID__"] = 5250110802796542316

