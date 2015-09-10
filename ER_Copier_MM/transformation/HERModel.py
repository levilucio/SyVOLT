

from core.himesis import Himesis

class HERModel(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HERModel.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HERModel, self).__init__(name='HERModel', num_nodes=20, edges=[])
        
        # Add the edges
        self.add_edges([[0, 3], [3, 7], [1, 4], [4, 8], [7, 5], [5, 17], [8, 9], [9, 18], [10, 11], [11, 18], [10, 12], [12, 17], [8, 13], [13, 19], [14, 15], [15, 19], [14, 16], [16, 6], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """ERModel"""
        self["GUID__"] = 4171038043616414325
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 4512663400472351928
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 6244414176588088193
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 7000487000152932634
        self.vs[3]["mm__"] = """match_contains"""
        self.vs[3]["GUID__"] = 165365788856568210
        self.vs[4]["mm__"] = """apply_contains"""
        self.vs[4]["GUID__"] = 2154512863199825677
        self.vs[5]["mm__"] = """hasAttribute_S"""
        self.vs[5]["GUID__"] = 197712037214367933
        self.vs[6]["name"] = """solveRef"""
        self.vs[6]["mm__"] = """Constant"""
        self.vs[6]["Type"] = """'String'"""
        self.vs[6]["GUID__"] = 8492928095288938738
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """ERModel"""
        self.vs[7]["mm__"] = """ERModel"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 1650102309724733921
        self.vs[8]["name"] = """"""
        self.vs[8]["classtype"] = """ERModel"""
        self.vs[8]["mm__"] = """ERModel"""
        self.vs[8]["cardinality"] = """1"""
        self.vs[8]["GUID__"] = 2896827362335233277
        self.vs[9]["mm__"] = """hasAttribute_T"""
        self.vs[9]["GUID__"] = 6224962757229049194
        self.vs[10]["name"] = """eq_"""
        self.vs[10]["mm__"] = """Equation"""
        self.vs[10]["GUID__"] = 3359015630222095242
        self.vs[11]["mm__"] = """leftExpr"""
        self.vs[11]["GUID__"] = 4887102402598949145
        self.vs[12]["mm__"] = """rightExpr"""
        self.vs[12]["GUID__"] = 6671575401739768827
        self.vs[13]["mm__"] = """hasAttribute_T"""
        self.vs[13]["GUID__"] = 3412283339953997332
        self.vs[14]["name"] = """eq_"""
        self.vs[14]["mm__"] = """Equation"""
        self.vs[14]["GUID__"] = 6185635365126398523
        self.vs[15]["mm__"] = """leftExpr"""
        self.vs[15]["GUID__"] = 2933419803779705957
        self.vs[16]["mm__"] = """rightExpr"""
        self.vs[16]["GUID__"] = 342747187405875960
        self.vs[17]["name"] = """name"""
        self.vs[17]["mm__"] = """Attribute"""
        self.vs[17]["Type"] = """'String'"""
        self.vs[17]["GUID__"] = 3303680429438829040
        self.vs[18]["name"] = """name"""
        self.vs[18]["mm__"] = """Attribute"""
        self.vs[18]["Type"] = """'String'"""
        self.vs[18]["GUID__"] = 5219894342221821178
        self.vs[19]["name"] = """ApplyAttribute"""
        self.vs[19]["mm__"] = """Attribute"""
        self.vs[19]["Type"] = """'String'"""
        self.vs[19]["GUID__"] = 8456501794368173136

