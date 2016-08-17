

from core.himesis import Himesis

class HEParameter(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HEParameter.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HEParameter, self).__init__(name='HEParameter', num_nodes=48, edges=[])
        
        # Add the edges
        self.add_edges([[0, 3], [3, 6], [1, 4], [4, 7], [6, 8], [8, 37], [6, 9], [9, 38], [6, 10], [10, 39], [6, 11], [11, 40], [6, 12], [12, 41], [7, 13], [13, 42], [14, 15], [15, 42], [14, 16], [16, 37], [7, 17], [17, 43], [18, 19], [19, 43], [18, 20], [20, 38], [7, 21], [21, 44], [22, 23], [23, 44], [22, 24], [24, 39], [7, 25], [25, 45], [26, 27], [27, 45], [26, 28], [28, 40], [7, 29], [29, 46], [30, 31], [31, 46], [30, 32], [32, 41], [7, 33], [33, 47], [34, 35], [35, 47], [34, 36], [36, 5], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """EParameter"""
        self["GUID__"] = 6749339449011532152
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 2389464235591375673
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 250990042949112085
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 6290606671997222511
        self.vs[3]["mm__"] = """match_contains"""
        self.vs[3]["GUID__"] = 7314499045225206104
        self.vs[4]["mm__"] = """apply_contains"""
        self.vs[4]["GUID__"] = 3357849991328375297
        self.vs[5]["name"] = """solveRef"""
        self.vs[5]["mm__"] = """Constant"""
        self.vs[5]["Type"] = """'String'"""
        self.vs[5]["GUID__"] = 3589583033785265550
        self.vs[6]["name"] = """"""
        self.vs[6]["classtype"] = """EParameter"""
        self.vs[6]["mm__"] = """EParameter"""
        self.vs[6]["cardinality"] = """+"""
        self.vs[6]["GUID__"] = 6512613757692690304
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EParameter"""
        self.vs[7]["mm__"] = """EParameter"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = 1505375278273103288
        self.vs[8]["mm__"] = """hasAttribute_S"""
        self.vs[8]["GUID__"] = 8002350964532715122
        self.vs[9]["mm__"] = """hasAttribute_S"""
        self.vs[9]["GUID__"] = 1951662966759509545
        self.vs[10]["mm__"] = """hasAttribute_S"""
        self.vs[10]["GUID__"] = 6200879754865437769
        self.vs[11]["mm__"] = """hasAttribute_S"""
        self.vs[11]["GUID__"] = 462208901166267338
        self.vs[12]["mm__"] = """hasAttribute_S"""
        self.vs[12]["GUID__"] = 873681454819347589
        self.vs[13]["mm__"] = """hasAttribute_T"""
        self.vs[13]["GUID__"] = 1976318218803729683
        self.vs[14]["name"] = """eq_"""
        self.vs[14]["mm__"] = """Equation"""
        self.vs[14]["GUID__"] = 8628870272867206927
        self.vs[15]["mm__"] = """leftExpr"""
        self.vs[15]["GUID__"] = 2302964246764991598
        self.vs[16]["mm__"] = """rightExpr"""
        self.vs[16]["GUID__"] = 1510147556832028010
        self.vs[17]["mm__"] = """hasAttribute_T"""
        self.vs[17]["GUID__"] = 6232381532218432159
        self.vs[18]["name"] = """eq_"""
        self.vs[18]["mm__"] = """Equation"""
        self.vs[18]["GUID__"] = 582583986976853926
        self.vs[19]["mm__"] = """leftExpr"""
        self.vs[19]["GUID__"] = 4104261504720607400
        self.vs[20]["mm__"] = """rightExpr"""
        self.vs[20]["GUID__"] = 545812527443442398
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 7822561197153808864
        self.vs[22]["name"] = """eq_"""
        self.vs[22]["mm__"] = """Equation"""
        self.vs[22]["GUID__"] = 4675913010969617400
        self.vs[23]["mm__"] = """leftExpr"""
        self.vs[23]["GUID__"] = 5062619616980993221
        self.vs[24]["mm__"] = """rightExpr"""
        self.vs[24]["GUID__"] = 7677887490372492032
        self.vs[25]["mm__"] = """hasAttribute_T"""
        self.vs[25]["GUID__"] = 5683748422831995652
        self.vs[26]["name"] = """eq_"""
        self.vs[26]["mm__"] = """Equation"""
        self.vs[26]["GUID__"] = 8794342848272562112
        self.vs[27]["mm__"] = """leftExpr"""
        self.vs[27]["GUID__"] = 8189500995285429749
        self.vs[28]["mm__"] = """rightExpr"""
        self.vs[28]["GUID__"] = 4576477063667844049
        self.vs[29]["mm__"] = """hasAttribute_T"""
        self.vs[29]["GUID__"] = 1937101358016754296
        self.vs[30]["name"] = """eq_"""
        self.vs[30]["mm__"] = """Equation"""
        self.vs[30]["GUID__"] = 8527309644982611074
        self.vs[31]["mm__"] = """leftExpr"""
        self.vs[31]["GUID__"] = 7843777969931746314
        self.vs[32]["mm__"] = """rightExpr"""
        self.vs[32]["GUID__"] = 135565936956533693
        self.vs[33]["mm__"] = """hasAttribute_T"""
        self.vs[33]["GUID__"] = 98248589381725667
        self.vs[34]["name"] = """eq_"""
        self.vs[34]["mm__"] = """Equation"""
        self.vs[34]["GUID__"] = 1994442754441104548
        self.vs[35]["mm__"] = """leftExpr"""
        self.vs[35]["GUID__"] = 3931658360384580142
        self.vs[36]["mm__"] = """rightExpr"""
        self.vs[36]["GUID__"] = 1491525784184389205
        self.vs[37]["name"] = """name"""
        self.vs[37]["mm__"] = """Attribute"""
        self.vs[37]["Type"] = """'String'"""
        self.vs[37]["GUID__"] = 1882201920289648585
        self.vs[38]["name"] = """ordered"""
        self.vs[38]["mm__"] = """Attribute"""
        self.vs[38]["Type"] = """'String'"""
        self.vs[38]["GUID__"] = 8872577015130733670
        self.vs[39]["name"] = """unique"""
        self.vs[39]["mm__"] = """Attribute"""
        self.vs[39]["Type"] = """'String'"""
        self.vs[39]["GUID__"] = 77678441867874531
        self.vs[40]["name"] = """lowerBound"""
        self.vs[40]["mm__"] = """Attribute"""
        self.vs[40]["Type"] = """'String'"""
        self.vs[40]["GUID__"] = 2154082419115129983
        self.vs[41]["name"] = """upperBound"""
        self.vs[41]["mm__"] = """Attribute"""
        self.vs[41]["Type"] = """'String'"""
        self.vs[41]["GUID__"] = 3842165874713799355
        self.vs[42]["name"] = """name"""
        self.vs[42]["mm__"] = """Attribute"""
        self.vs[42]["Type"] = """'String'"""
        self.vs[42]["GUID__"] = 3585204735620009514
        self.vs[43]["name"] = """ordered"""
        self.vs[43]["mm__"] = """Attribute"""
        self.vs[43]["Type"] = """'String'"""
        self.vs[43]["GUID__"] = 6139149958935211010
        self.vs[44]["name"] = """unique"""
        self.vs[44]["mm__"] = """Attribute"""
        self.vs[44]["Type"] = """'String'"""
        self.vs[44]["GUID__"] = 5028046018944726326
        self.vs[45]["name"] = """lowerBound"""
        self.vs[45]["mm__"] = """Attribute"""
        self.vs[45]["Type"] = """'String'"""
        self.vs[45]["GUID__"] = 3311847168064451230
        self.vs[46]["name"] = """upperBound"""
        self.vs[46]["mm__"] = """Attribute"""
        self.vs[46]["Type"] = """'String'"""
        self.vs[46]["GUID__"] = 1161200393055443021
        self.vs[47]["name"] = """ApplyAttribute"""
        self.vs[47]["mm__"] = """Attribute"""
        self.vs[47]["Type"] = """'String'"""
        self.vs[47]["GUID__"] = 8339499371485609057

