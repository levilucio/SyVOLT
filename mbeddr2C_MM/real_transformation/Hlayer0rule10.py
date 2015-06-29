

from core.himesis import Himesis

class Hlayer0rule10(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model Hlayer0rule10.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer0rule10, self).__init__(name='Hlayer0rule10', num_nodes=18, edges=[])
        
        # Add the edges
        self.add_edges([[0, 4], [4, 3], [1, 6], [6, 5], [3, 7], [7, 14], [5, 8], [8, 15], [9, 10], [10, 15], [9, 11], [12, 16], [16, 14], [12, 17], [17, 13], [11, 12], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer0rule10"""
        self["GUID__"] = 1112880813506683684
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 7423792678599619490
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 1102515336735861024
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 3213483895952157920
        self.vs[3]["name"] = """layer0rule10class0"""
        self.vs[3]["classtype"] = """RequiredPort"""
        self.vs[3]["mm__"] = """RequiredPort"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 5213268961854098970
        self.vs[4]["mm__"] = """match_contains"""
        self.vs[4]["GUID__"] = 5208226872446466533
        self.vs[5]["name"] = """layer0rule10class1"""
        self.vs[5]["classtype"] = """Member"""
        self.vs[5]["mm__"] = """Member"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = 2035173993228166316
        self.vs[6]["mm__"] = """apply_contains"""
        self.vs[6]["GUID__"] = 7649264347965220105
        self.vs[7]["mm__"] = """hasAttribute_S"""
        self.vs[7]["GUID__"] = 2086100942510001471
        self.vs[8]["mm__"] = """hasAttribute_T"""
        self.vs[8]["GUID__"] = 739263039559069401
        self.vs[9]["name"] = """eq_"""
        self.vs[9]["mm__"] = """Equation"""
        self.vs[9]["GUID__"] = 7780775255565604613
        self.vs[10]["mm__"] = """leftExpr"""
        self.vs[10]["GUID__"] = 4520125192944887230
        self.vs[11]["mm__"] = """rightExpr"""
        self.vs[11]["GUID__"] = 4267907813140121414
        self.vs[12]["name"] = """Concatlayer0rule10class1attribute014"""
        self.vs[12]["mm__"] = """Concat"""
        self.vs[12]["Type"] = """'String'"""
        self.vs[12]["GUID__"] = 2374103942970538716
        self.vs[13]["name"] = """__ops"""
        self.vs[13]["mm__"] = """Constant"""
        self.vs[13]["Type"] = """'String'"""
        self.vs[13]["GUID__"] = 6365519828283943487
        self.vs[14]["name"] = """name"""
        self.vs[14]["mm__"] = """Attribute"""
        self.vs[14]["Type"] = """'String'"""
        self.vs[14]["GUID__"] = 1068109250526372317
        self.vs[15]["name"] = """name"""
        self.vs[15]["mm__"] = """Attribute"""
        self.vs[15]["Type"] = """'String'"""
        self.vs[15]["GUID__"] = 5026187277030842597
        self.vs[16]["mm__"] = """hasArgs"""
        self.vs[16]["GUID__"] = 606532459200799794
        self.vs[17]["mm__"] = """hasArgs"""
        self.vs[17]["GUID__"] = 6318917400693328389

