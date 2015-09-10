

from core.himesis import Himesis

class HedatatypeOUTeTypeParametersSolveRefEDataTypeETypeParameterEDataTypeETypeParameter(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HedatatypeOUTeTypeParametersSolveRefEDataTypeETypeParameterEDataTypeETypeParameter.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HedatatypeOUTeTypeParametersSolveRefEDataTypeETypeParameterEDataTypeETypeParameter, self).__init__(name='HedatatypeOUTeTypeParametersSolveRefEDataTypeETypeParameterEDataTypeETypeParameter', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 6], [6, 5], [0, 8], [8, 7], [1, 10], [10, 9], [1, 12], [12, 11], [5, 3], [3, 7], [9, 4], [4, 11], [9, 13], [13, 5], [11, 14], [14, 7], [9, 15], [15, 16], [17, 18], [18, 16], [17, 19], [19, 20], [11, 21], [21, 22], [23, 24], [24, 22], [23, 25], [25, 26], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """edatatypeOUTeTypeParametersSolveRefEDataTypeETypeParameterEDataTypeETypeParameter"""
        self["GUID__"] = 9216841814768560592
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 3637022504002522765
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 1514275467067869021
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 387758662155257229
        self.vs[3]["associationType"] = """eTypeParameters"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 1669556237675087642
        self.vs[4]["associationType"] = """eTypeParameters"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 4958789637966985052
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EDataType"""
        self.vs[5]["mm__"] = """EDataType"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 7946454087607733146
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 9133726544621315770
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """ETypeParameter"""
        self.vs[7]["mm__"] = """ETypeParameter"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 5699861857151727609
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 692320901114489271
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """EDataType"""
        self.vs[9]["mm__"] = """EDataType"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 4202295646997420412
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 8014872872051247219
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """ETypeParameter"""
        self.vs[11]["mm__"] = """ETypeParameter"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 148510130415220409
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 4086749586668436150
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 2522122892873632696
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 1738429017737622910
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 7600919830493987630
        self.vs[16]["name"] = """ApplyAttribute"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["GUID__"] = 4539691374496413222
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 4559282058929906499
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 4043718801088784330
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 7869078365520097302
        self.vs[20]["name"] = """solveRef"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 3623399056145213035
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 3246759103643529052
        self.vs[22]["name"] = """ApplyAttribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["GUID__"] = 9116843035793812053
        self.vs[23]["name"] = """eq_"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = 7608039033500036356
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = 6760875346500065688
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = 9016330942781717447
        self.vs[26]["name"] = """solveRef"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 5651025117334024887

