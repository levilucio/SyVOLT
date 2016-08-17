

from core.himesis import Himesis

class HeenumOUTeTypeParametersSolveRefEEnumETypeParameterEEnumETypeParameter(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HeenumOUTeTypeParametersSolveRefEEnumETypeParameterEEnumETypeParameter.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HeenumOUTeTypeParametersSolveRefEEnumETypeParameterEEnumETypeParameter, self).__init__(name='HeenumOUTeTypeParametersSolveRefEEnumETypeParameterEEnumETypeParameter', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 6], [6, 5], [0, 8], [8, 7], [1, 10], [10, 9], [1, 12], [12, 11], [5, 3], [3, 7], [9, 4], [4, 11], [9, 13], [13, 5], [11, 14], [14, 7], [9, 15], [15, 16], [17, 18], [18, 16], [17, 19], [19, 20], [11, 21], [21, 22], [23, 24], [24, 22], [23, 25], [25, 26], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """eenumOUTeTypeParametersSolveRefEEnumETypeParameterEEnumETypeParameter"""
        self["GUID__"] = 3334778672714496912
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 4524610659727406673
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 9164069540088195085
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 9021965217247316988
        self.vs[3]["associationType"] = """eTypeParameters"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 5258888278357664891
        self.vs[4]["associationType"] = """eTypeParameters"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 2180316725247168530
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EEnum"""
        self.vs[5]["mm__"] = """EEnum"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 8750381820517428404
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 6858823818850952416
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """ETypeParameter"""
        self.vs[7]["mm__"] = """ETypeParameter"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 911283980934982667
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 4420680797569194702
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """EEnum"""
        self.vs[9]["mm__"] = """EEnum"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 2453414914404641979
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 3114003177596377678
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """ETypeParameter"""
        self.vs[11]["mm__"] = """ETypeParameter"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 182593432828846129
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 4464026095448781562
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 6435882578697119268
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 3130760012301744638
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 9187204814175013182
        self.vs[16]["name"] = """ApplyAttribute"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["GUID__"] = 3750252437799372208
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 2720774683907295253
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 5164673934357456979
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 1475607937500741265
        self.vs[20]["name"] = """solveRef"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 7387640284267525481
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 4878808574458095866
        self.vs[22]["name"] = """ApplyAttribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["GUID__"] = 5581145539621995825
        self.vs[23]["name"] = """eq_"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = 5449836593936650961
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = 8998949088213307027
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = 3163770550209726065
        self.vs[26]["name"] = """solveRef"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 447058606870982587

