

from core.himesis import Himesis

class Hlayer6rule0(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model Hlayer6rule0.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer6rule0, self).__init__(name='Hlayer6rule0', num_nodes=26, edges=[])
        
        # Add the edges
        self.add_edges([[0, 4], [4, 3], [1, 23], [23, 5], [1, 24], [24, 6], [1, 25], [25, 7], [5, 11], [11, 6], [6, 12], [12, 7], [5, 8], [8, 3], [3, 9], [9, 13], [14, 15], [15, 13], [14, 16], [16, 17], [7, 10], [10, 18], [19, 20], [20, 18], [19, 21], [21, 22], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer6rule0"""
        self["GUID__"] = 4742881250491757415
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 8913756710997827952
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 8141130301424162428
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 7102975926221893374
        self.vs[3]["name"] = """layer6rule0class0"""
        self.vs[3]["classtype"] = """Function"""
        self.vs[3]["mm__"] = """Function"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 8070423525201397135
        self.vs[4]["mm__"] = """match_contains"""
        self.vs[4]["GUID__"] = 3766320682131898614
        self.vs[5]["name"] = """layer6rule0class1"""
        self.vs[5]["classtype"] = """StatementList"""
        self.vs[5]["mm__"] = """StatementList"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = 8622993792684050174
        self.vs[6]["name"] = """layer6rule0class2"""
        self.vs[6]["classtype"] = """ReturnStatement"""
        self.vs[6]["mm__"] = """ReturnStatement"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = 60497089321267614
        self.vs[7]["name"] = """layer6rule0class3"""
        self.vs[7]["classtype"] = """NumberLiteral"""
        self.vs[7]["mm__"] = """NumberLiteral"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = 4192339963595577604
        self.vs[8]["mm__"] = """backward_link"""
        self.vs[8]["type"] = """ruleDef"""
        self.vs[8]["GUID__"] = 691606937114722652
        self.vs[9]["mm__"] = """hasAttribute_S"""
        self.vs[9]["GUID__"] = 1557668424049220695
        self.vs[10]["mm__"] = """hasAttribute_T"""
        self.vs[10]["GUID__"] = 8594762424697191571
        self.vs[11]["associationType"] = """statements"""
        self.vs[11]["mm__"] = """directLink_T"""
        self.vs[11]["GUID__"] = 2581719534993134996
        self.vs[12]["associationType"] = """expression"""
        self.vs[12]["mm__"] = """directLink_T"""
        self.vs[12]["GUID__"] = 5468144608942662350
        self.vs[13]["name"] = """name"""
        self.vs[13]["Type"] = """'String'"""
        self.vs[13]["mm__"] = """Attribute"""
        self.vs[13]["GUID__"] = 413760503883965707
        self.vs[14]["name"] = """eq_"""
        self.vs[14]["mm__"] = """Equation"""
        self.vs[14]["GUID__"] = 261069058361656586
        self.vs[15]["mm__"] = """leftExpr"""
        self.vs[15]["GUID__"] = 4010517801495114442
        self.vs[16]["mm__"] = """rightExpr"""
        self.vs[16]["GUID__"] = 3519919389822264149
        self.vs[17]["name"] = """main"""
        self.vs[17]["Type"] = """'String'"""
        self.vs[17]["mm__"] = """Constant"""
        self.vs[17]["GUID__"] = 5899391971910405709
        self.vs[18]["name"] = """value"""
        self.vs[18]["Type"] = """'String'"""
        self.vs[18]["mm__"] = """Attribute"""
        self.vs[18]["GUID__"] = 6268476598094073121
        self.vs[19]["name"] = """eq_"""
        self.vs[19]["mm__"] = """Equation"""
        self.vs[19]["GUID__"] = 6984569345570355427
        self.vs[20]["mm__"] = """leftExpr"""
        self.vs[20]["GUID__"] = 2468658321521535478
        self.vs[21]["mm__"] = """rightExpr"""
        self.vs[21]["GUID__"] = 3487495463545566518
        self.vs[22]["name"] = """0"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Constant"""
        self.vs[22]["GUID__"] = 3192682210103633066
        self.vs[23]["mm__"] = """apply_contains"""
        self.vs[23]["GUID__"] = 3857838723711657802
        self.vs[24]["mm__"] = """apply_contains"""
        self.vs[24]["GUID__"] = 2801003604541839694
        self.vs[25]["mm__"] = """apply_contains"""
        self.vs[25]["GUID__"] = 5651103082857088639

