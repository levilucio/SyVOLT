

from core.himesis import Himesis

class Hlayer2rule3(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model Hlayer2rule3.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer2rule3, self).__init__(name='Hlayer2rule3', num_nodes=23, edges=[])
        
        # Add the edges
        self.add_edges([[0, 4], [4, 3], [1, 19], [19, 5], [1, 20], [20, 6], [1, 21], [21, 7], [1, 22], [22, 8], [5, 16], [16, 6], [6, 17], [17, 8], [8, 18], [18, 7], [5, 9], [9, 3], [6, 10], [10, 11], [12, 13], [13, 11], [12, 14], [14, 15], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer2rule3"""
        self["GUID__"] = 4637945904383774303
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 2722756593853352484
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 1013849627189021725
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 8413803253966254999
        self.vs[3]["name"] = """layer2rule3class0"""
        self.vs[3]["classtype"] = """Operation"""
        self.vs[3]["mm__"] = """Operation"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 1207997187523094632
        self.vs[4]["mm__"] = """match_contains"""
        self.vs[4]["GUID__"] = 4917711570519103633
        self.vs[5]["name"] = """layer2rule3class1"""
        self.vs[5]["classtype"] = """FunctionPrototype"""
        self.vs[5]["mm__"] = """FunctionPrototype"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = 9173864775111770243
        self.vs[6]["name"] = """layer2rule3class2"""
        self.vs[6]["classtype"] = """Argument"""
        self.vs[6]["mm__"] = """Argument"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = 7341613491075203199
        self.vs[7]["name"] = """layer2rule3class3"""
        self.vs[7]["classtype"] = """VoidType"""
        self.vs[7]["mm__"] = """VoidType"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = 508952319817315846
        self.vs[8]["name"] = """layer2rule3class4"""
        self.vs[8]["classtype"] = """PointerType"""
        self.vs[8]["mm__"] = """PointerType"""
        self.vs[8]["cardinality"] = """1"""
        self.vs[8]["GUID__"] = 2419395145946036857
        self.vs[9]["mm__"] = """backward_link"""
        self.vs[9]["type"] = """ruleDef"""
        self.vs[9]["GUID__"] = 6387957987029705645
        self.vs[10]["mm__"] = """hasAttribute_T"""
        self.vs[10]["GUID__"] = 386573058362580273
        self.vs[11]["name"] = """name"""
        self.vs[11]["Type"] = """'String'"""
        self.vs[11]["mm__"] = """Attribute"""
        self.vs[11]["GUID__"] = 712121863921185990
        self.vs[12]["name"] = """eq_"""
        self.vs[12]["mm__"] = """Equation"""
        self.vs[12]["GUID__"] = 8962889850243038012
        self.vs[13]["mm__"] = """leftExpr"""
        self.vs[13]["GUID__"] = 4208311454626272085
        self.vs[14]["mm__"] = """rightExpr"""
        self.vs[14]["GUID__"] = 7313284592522891722
        self.vs[15]["name"] = """___id"""
        self.vs[15]["Type"] = """'String'"""
        self.vs[15]["mm__"] = """Constant"""
        self.vs[15]["GUID__"] = 2844627039439998809
        self.vs[16]["associationType"] = """arguments"""
        self.vs[16]["mm__"] = """directLink_T"""
        self.vs[16]["GUID__"] = 906217124029377795
        self.vs[17]["associationType"] = """type"""
        self.vs[17]["mm__"] = """directLink_T"""
        self.vs[17]["GUID__"] = 132787124080875692
        self.vs[18]["associationType"] = """baseType"""
        self.vs[18]["mm__"] = """directLink_T"""
        self.vs[18]["GUID__"] = 7667416149086845668
        self.vs[19]["mm__"] = """apply_contains"""
        self.vs[19]["GUID__"] = 4238429953270425920
        self.vs[20]["mm__"] = """apply_contains"""
        self.vs[20]["GUID__"] = 2905279285986731952
        self.vs[21]["mm__"] = """apply_contains"""
        self.vs[21]["GUID__"] = 5684227321751160987
        self.vs[22]["mm__"] = """apply_contains"""
        self.vs[22]["GUID__"] = 2075710133492129307

