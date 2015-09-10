

from core.himesis import Himesis

class HEPackage(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HEPackage.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HEPackage, self).__init__(name='HEPackage', num_nodes=34, edges=[])
        
        # Add the edges
        self.add_edges([[0, 3], [3, 6], [1, 4], [4, 7], [6, 8], [8, 27], [6, 9], [9, 28], [6, 10], [10, 29], [7, 11], [11, 30], [12, 13], [13, 30], [12, 14], [14, 27], [7, 15], [15, 31], [16, 17], [17, 31], [16, 18], [18, 28], [7, 19], [19, 32], [20, 21], [21, 32], [20, 22], [22, 29], [7, 23], [23, 33], [24, 25], [25, 33], [24, 26], [26, 5], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """EPackage"""
        self["GUID__"] = 6888822680342846797
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 3517412697458314336
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 3186413579539041091
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 6476100577738804613
        self.vs[3]["mm__"] = """match_contains"""
        self.vs[3]["GUID__"] = 3108433068016932573
        self.vs[4]["mm__"] = """apply_contains"""
        self.vs[4]["GUID__"] = 1331050117633534585
        self.vs[5]["name"] = """solveRef"""
        self.vs[5]["mm__"] = """Constant"""
        self.vs[5]["Type"] = """'String'"""
        self.vs[5]["GUID__"] = 6091063594200501714
        self.vs[6]["name"] = """"""
        self.vs[6]["classtype"] = """EPackage"""
        self.vs[6]["mm__"] = """EPackage"""
        self.vs[6]["cardinality"] = """+"""
        self.vs[6]["GUID__"] = 8338023376054774990
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EPackage"""
        self.vs[7]["mm__"] = """EPackage"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = 1452107385957573597
        self.vs[8]["mm__"] = """hasAttribute_S"""
        self.vs[8]["GUID__"] = 3044732396533900113
        self.vs[9]["mm__"] = """hasAttribute_S"""
        self.vs[9]["GUID__"] = 2913571135357330251
        self.vs[10]["mm__"] = """hasAttribute_S"""
        self.vs[10]["GUID__"] = 6803714943214165866
        self.vs[11]["mm__"] = """hasAttribute_T"""
        self.vs[11]["GUID__"] = 572844058759577333
        self.vs[12]["name"] = """eq_"""
        self.vs[12]["mm__"] = """Equation"""
        self.vs[12]["GUID__"] = 3357186504973573609
        self.vs[13]["mm__"] = """leftExpr"""
        self.vs[13]["GUID__"] = 3034960711553384608
        self.vs[14]["mm__"] = """rightExpr"""
        self.vs[14]["GUID__"] = 8940016448657622528
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 7035773818032358671
        self.vs[16]["name"] = """eq_"""
        self.vs[16]["mm__"] = """Equation"""
        self.vs[16]["GUID__"] = 1368874326590068683
        self.vs[17]["mm__"] = """leftExpr"""
        self.vs[17]["GUID__"] = 7646796461784648190
        self.vs[18]["mm__"] = """rightExpr"""
        self.vs[18]["GUID__"] = 3161394166614360641
        self.vs[19]["mm__"] = """hasAttribute_T"""
        self.vs[19]["GUID__"] = 3219234762051799602
        self.vs[20]["name"] = """eq_"""
        self.vs[20]["mm__"] = """Equation"""
        self.vs[20]["GUID__"] = 7987153131241042724
        self.vs[21]["mm__"] = """leftExpr"""
        self.vs[21]["GUID__"] = 3083337975352280811
        self.vs[22]["mm__"] = """rightExpr"""
        self.vs[22]["GUID__"] = 7356064383553619536
        self.vs[23]["mm__"] = """hasAttribute_T"""
        self.vs[23]["GUID__"] = 2657150075195379058
        self.vs[24]["name"] = """eq_"""
        self.vs[24]["mm__"] = """Equation"""
        self.vs[24]["GUID__"] = 2039720199746807627
        self.vs[25]["mm__"] = """leftExpr"""
        self.vs[25]["GUID__"] = 8169088090653972376
        self.vs[26]["mm__"] = """rightExpr"""
        self.vs[26]["GUID__"] = 3516728569955184806
        self.vs[27]["name"] = """name"""
        self.vs[27]["mm__"] = """Attribute"""
        self.vs[27]["Type"] = """'String'"""
        self.vs[27]["GUID__"] = 1326441149213831506
        self.vs[28]["name"] = """nsURI"""
        self.vs[28]["mm__"] = """Attribute"""
        self.vs[28]["Type"] = """'String'"""
        self.vs[28]["GUID__"] = 406368508873391586
        self.vs[29]["name"] = """nsPrefix"""
        self.vs[29]["mm__"] = """Attribute"""
        self.vs[29]["Type"] = """'String'"""
        self.vs[29]["GUID__"] = 4210224422474428787
        self.vs[30]["name"] = """name"""
        self.vs[30]["mm__"] = """Attribute"""
        self.vs[30]["Type"] = """'String'"""
        self.vs[30]["GUID__"] = 7718102509364427797
        self.vs[31]["name"] = """nsURI"""
        self.vs[31]["mm__"] = """Attribute"""
        self.vs[31]["Type"] = """'String'"""
        self.vs[31]["GUID__"] = 5404822765233180206
        self.vs[32]["name"] = """nsPrefix"""
        self.vs[32]["mm__"] = """Attribute"""
        self.vs[32]["Type"] = """'String'"""
        self.vs[32]["GUID__"] = 5889459929432192735
        self.vs[33]["name"] = """ApplyAttribute"""
        self.vs[33]["mm__"] = """Attribute"""
        self.vs[33]["Type"] = """'String'"""
        self.vs[33]["GUID__"] = 8559664442328114764

