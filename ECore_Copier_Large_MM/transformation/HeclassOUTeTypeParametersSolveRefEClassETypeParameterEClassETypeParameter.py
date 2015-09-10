

from core.himesis import Himesis

class HeclassOUTeTypeParametersSolveRefEClassETypeParameterEClassETypeParameter(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HeclassOUTeTypeParametersSolveRefEClassETypeParameterEClassETypeParameter.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HeclassOUTeTypeParametersSolveRefEClassETypeParameterEClassETypeParameter, self).__init__(name='HeclassOUTeTypeParametersSolveRefEClassETypeParameterEClassETypeParameter', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 6], [6, 5], [0, 8], [8, 7], [1, 10], [10, 9], [1, 12], [12, 11], [5, 3], [3, 7], [9, 4], [4, 11], [9, 13], [13, 5], [11, 14], [14, 7], [9, 15], [15, 16], [17, 18], [18, 16], [17, 19], [19, 20], [11, 21], [21, 22], [23, 24], [24, 22], [23, 25], [25, 26], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """eclassOUTeTypeParametersSolveRefEClassETypeParameterEClassETypeParameter"""
        self["GUID__"] = 4980837554085539620
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 3221221609493702901
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 5255213354093735432
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 7579187497955238467
        self.vs[3]["associationType"] = """eTypeParameters"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 3797143210809728769
        self.vs[4]["associationType"] = """eTypeParameters"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 2059894066647756192
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EClass"""
        self.vs[5]["mm__"] = """EClass"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 2476145235298424552
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 6517387818988537317
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """ETypeParameter"""
        self.vs[7]["mm__"] = """ETypeParameter"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 2677381876600404388
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 4741742789901472564
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """EClass"""
        self.vs[9]["mm__"] = """EClass"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 2937922289547418547
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 6806541583567685385
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """ETypeParameter"""
        self.vs[11]["mm__"] = """ETypeParameter"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 3695756919468742507
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 8368652282273713424
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 7251527838572751270
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 1718874795098212185
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 463633291369726691
        self.vs[16]["name"] = """ApplyAttribute"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["GUID__"] = 8942183360835263515
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 6203099223234768901
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 463632989245038583
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 2377202214772442938
        self.vs[20]["name"] = """solveRef"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 5027401967891494281
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 9082442165925728583
        self.vs[22]["name"] = """ApplyAttribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["GUID__"] = 6877465800682366309
        self.vs[23]["name"] = """eq_"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = 9221157818642301811
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = 8589020415357134154
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = 2416955536262686640
        self.vs[26]["name"] = """solveRef"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 6922479532359277487

