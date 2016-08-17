

from core.himesis import Himesis

class HegenerictypeOUTeTypeParameterSolveRefEGenericTypeETypeParameterEGenericTypeETypeParameter(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HegenerictypeOUTeTypeParameterSolveRefEGenericTypeETypeParameterEGenericTypeETypeParameter.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HegenerictypeOUTeTypeParameterSolveRefEGenericTypeETypeParameterEGenericTypeETypeParameter, self).__init__(name='HegenerictypeOUTeTypeParameterSolveRefEGenericTypeETypeParameterEGenericTypeETypeParameter', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 6], [6, 5], [0, 8], [8, 7], [1, 10], [10, 9], [1, 12], [12, 11], [5, 3], [3, 7], [9, 4], [4, 11], [9, 13], [13, 5], [11, 14], [14, 7], [9, 15], [15, 16], [17, 18], [18, 16], [17, 19], [19, 20], [11, 21], [21, 22], [23, 24], [24, 22], [23, 25], [25, 26], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """egenerictypeOUTeTypeParameterSolveRefEGenericTypeETypeParameterEGenericTypeETypeParameter"""
        self["GUID__"] = 3492546649439225433
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 5907659047720036810
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 3719470430130905409
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 3990462057368438053
        self.vs[3]["associationType"] = """eTypeParameter"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 746267155135325045
        self.vs[4]["associationType"] = """eTypeParameter"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 6186380539237883845
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EGenericType"""
        self.vs[5]["mm__"] = """EGenericType"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 5486628047845415703
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 8204732700677152177
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """ETypeParameter"""
        self.vs[7]["mm__"] = """ETypeParameter"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 6930693053915705600
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 302078109197280635
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """EGenericType"""
        self.vs[9]["mm__"] = """EGenericType"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 6147199067087785776
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 6893441259242268422
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """ETypeParameter"""
        self.vs[11]["mm__"] = """ETypeParameter"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 8718054510888290171
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 477188564673035988
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 9023399932573025547
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 8614154460454261054
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 4728879788570827872
        self.vs[16]["name"] = """ApplyAttribute"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["GUID__"] = 5551185175798037560
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 5197631395138731918
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 4173697382383789036
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 80962360642045462
        self.vs[20]["name"] = """solveRef"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 7099699324517530437
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 4167088575306557696
        self.vs[22]["name"] = """ApplyAttribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["GUID__"] = 2612564187091127020
        self.vs[23]["name"] = """eq_"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = 7319751974809234946
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = 4807699843892918482
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = 287446676864508388
        self.vs[26]["name"] = """solveRef"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 3073616392749094118

