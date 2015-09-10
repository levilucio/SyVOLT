

from core.himesis import Himesis

class HAttribute(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HAttribute.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HAttribute, self).__init__(name='HAttribute', num_nodes=21, edges=[])
        
        # Add the edges
        self.add_edges([[0, 3], [3, 5], [1, 4], [4, 6], [5, 7], [7, 17], [5, 8], [8, 18], [6, 9], [9, 19], [10, 11], [11, 19], [10, 12], [12, 17], [6, 13], [13, 20], [14, 15], [15, 20], [14, 16], [16, 18], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """Attribute"""
        self["GUID__"] = 3574505274974929400
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 5104035967257325663
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 7643540925708423723
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 4256129064194313080
        self.vs[3]["mm__"] = """match_contains"""
        self.vs[3]["GUID__"] = 2559997404416782661
        self.vs[4]["mm__"] = """apply_contains"""
        self.vs[4]["GUID__"] = 1262223614599991890
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """ERAttribute"""
        self.vs[5]["mm__"] = """ERAttribute"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 1934107019075234055
        self.vs[6]["name"] = """"""
        self.vs[6]["classtype"] = """ERAttribute"""
        self.vs[6]["mm__"] = """ERAttribute"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = 7129763451982806896
        self.vs[7]["mm__"] = """hasAttribute_S"""
        self.vs[7]["GUID__"] = 2394947713872571055
        self.vs[8]["mm__"] = """hasAttribute_S"""
        self.vs[8]["GUID__"] = 9155488874084803864
        self.vs[9]["mm__"] = """hasAttribute_T"""
        self.vs[9]["GUID__"] = 18151062632659639
        self.vs[10]["name"] = """eq_"""
        self.vs[10]["mm__"] = """Equation"""
        self.vs[10]["GUID__"] = 1729928169667830918
        self.vs[11]["mm__"] = """leftExpr"""
        self.vs[11]["GUID__"] = 1166026851172696723
        self.vs[12]["mm__"] = """rightExpr"""
        self.vs[12]["GUID__"] = 5053900088228334809
        self.vs[13]["mm__"] = """hasAttribute_T"""
        self.vs[13]["GUID__"] = 2576866574401823727
        self.vs[14]["name"] = """eq_"""
        self.vs[14]["mm__"] = """Equation"""
        self.vs[14]["GUID__"] = 419105854984436200
        self.vs[15]["mm__"] = """leftExpr"""
        self.vs[15]["GUID__"] = 6740469636276109554
        self.vs[16]["mm__"] = """rightExpr"""
        self.vs[16]["GUID__"] = 5773097307109707444
        self.vs[17]["name"] = """name"""
        self.vs[17]["mm__"] = """Attribute"""
        self.vs[17]["Type"] = """'String'"""
        self.vs[17]["GUID__"] = 5035925018922698837
        self.vs[18]["name"] = """type"""
        self.vs[18]["mm__"] = """Attribute"""
        self.vs[18]["Type"] = """'String'"""
        self.vs[18]["GUID__"] = 1332423430691063613
        self.vs[19]["name"] = """name"""
        self.vs[19]["mm__"] = """Attribute"""
        self.vs[19]["Type"] = """'String'"""
        self.vs[19]["GUID__"] = 577421850872220812
        self.vs[20]["name"] = """type"""
        self.vs[20]["mm__"] = """Attribute"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["GUID__"] = 4873776569328851928

