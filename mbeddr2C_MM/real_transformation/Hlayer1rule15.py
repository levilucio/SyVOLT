

from core.himesis import Himesis

class Hlayer1rule15(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model Hlayer1rule15.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer1rule15, self).__init__(name='Hlayer1rule15', num_nodes=21, edges=[])
        
        # Add the edges
        self.add_edges([[0, 15], [15, 3], [0, 16], [16, 4], [1, 17], [17, 5], [1, 18], [18, 6], [3, 7], [7, 4], [5, 8], [8, 6], [5, 9], [9, 3], [4, 10], [10, 19], [6, 11], [11, 20], [12, 13], [13, 20], [12, 14], [14, 19], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer1rule15"""
        self["GUID__"] = 5833695245272397084
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 8497881080306540479
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 5501565034149421512
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 5351890165137368349
        self.vs[3]["name"] = """layer1rule15class0"""
        self.vs[3]["classtype"] = """Operation"""
        self.vs[3]["mm__"] = """Operation"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 4209533875175092258
        self.vs[4]["name"] = """layer1rule15class1"""
        self.vs[4]["classtype"] = """OperationParameter"""
        self.vs[4]["mm__"] = """OperationParameter"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = 2816671611960763280
        self.vs[5]["name"] = """layer1rule15class2"""
        self.vs[5]["classtype"] = """FunctionPrototype"""
        self.vs[5]["mm__"] = """FunctionPrototype"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = 2734494824449964834
        self.vs[6]["name"] = """layer1rule15class3"""
        self.vs[6]["classtype"] = """Argument"""
        self.vs[6]["mm__"] = """Argument"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = 1190368752397605361
        self.vs[7]["associationType"] = """parameters"""
        self.vs[7]["mm__"] = """directLink_S"""
        self.vs[7]["GUID__"] = 6314728360822866861
        self.vs[8]["associationType"] = """arguments"""
        self.vs[8]["mm__"] = """directLink_T"""
        self.vs[8]["GUID__"] = 8467501585031204007
        self.vs[9]["mm__"] = """backward_link"""
        self.vs[9]["type"] = """ruleDef"""
        self.vs[9]["GUID__"] = 7593115955066445785
        self.vs[10]["mm__"] = """hasAttribute_S"""
        self.vs[10]["GUID__"] = 7985704361338085998
        self.vs[11]["mm__"] = """hasAttribute_T"""
        self.vs[11]["GUID__"] = 6022600269466944916
        self.vs[12]["name"] = """eq_"""
        self.vs[12]["mm__"] = """Equation"""
        self.vs[12]["GUID__"] = 1802349741206373201
        self.vs[13]["mm__"] = """leftExpr"""
        self.vs[13]["GUID__"] = 4975627067141688093
        self.vs[14]["mm__"] = """rightExpr"""
        self.vs[14]["GUID__"] = 8585843324653273910
        self.vs[15]["mm__"] = """match_contains"""
        self.vs[15]["GUID__"] = 591944198280363351
        self.vs[16]["mm__"] = """match_contains"""
        self.vs[16]["GUID__"] = 6560485443459882865
        self.vs[17]["mm__"] = """apply_contains"""
        self.vs[17]["GUID__"] = 5956949623461686382
        self.vs[18]["mm__"] = """apply_contains"""
        self.vs[18]["GUID__"] = 940271315307648286
        self.vs[19]["name"] = """name"""
        self.vs[19]["Type"] = """'String'"""
        self.vs[19]["mm__"] = """Attribute"""
        self.vs[19]["GUID__"] = 4977958049569073249
        self.vs[20]["name"] = """name"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Attribute"""
        self.vs[20]["GUID__"] = 4941131681774736615

