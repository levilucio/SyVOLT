

from core.himesis import Himesis

class HedatatypeOUTeAnnotationsSolveRefEDataTypeEAnnotationEDataTypeEAnnotation(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HedatatypeOUTeAnnotationsSolveRefEDataTypeEAnnotationEDataTypeEAnnotation.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HedatatypeOUTeAnnotationsSolveRefEDataTypeEAnnotationEDataTypeEAnnotation, self).__init__(name='HedatatypeOUTeAnnotationsSolveRefEDataTypeEAnnotationEDataTypeEAnnotation', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 6], [6, 5], [0, 8], [8, 7], [1, 10], [10, 9], [1, 12], [12, 11], [5, 3], [3, 7], [9, 4], [4, 11], [9, 13], [13, 5], [11, 14], [14, 7], [9, 15], [15, 16], [17, 18], [18, 16], [17, 19], [19, 20], [11, 21], [21, 22], [23, 24], [24, 22], [23, 25], [25, 26], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """edatatypeOUTeAnnotationsSolveRefEDataTypeEAnnotationEDataTypeEAnnotation"""
        self["GUID__"] = 4621012212582684501
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 1125323558302701139
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 4591956230736461287
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 7494054096709309042
        self.vs[3]["associationType"] = """eAnnotations"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 2617305970422412589
        self.vs[4]["associationType"] = """eAnnotations"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 873390849138914814
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EDataType"""
        self.vs[5]["mm__"] = """EDataType"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 2233476089664386204
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 7583684228253299642
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EAnnotation"""
        self.vs[7]["mm__"] = """EAnnotation"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 2800000065889113964
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 6129933014845074633
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """EDataType"""
        self.vs[9]["mm__"] = """EDataType"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 8864204913788416932
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 1259339854252209650
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """EAnnotation"""
        self.vs[11]["mm__"] = """EAnnotation"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 2640273625825158884
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 4214902575538887742
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 9187713284903552968
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 5476702963078555274
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 83471069109314450
        self.vs[16]["name"] = """ApplyAttribute"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["GUID__"] = 4451087131350840314
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 1845444794102645680
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 6071267204310088706
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 2926539340238923561
        self.vs[20]["name"] = """solveRef"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 731574549802545815
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 7274107881763129664
        self.vs[22]["name"] = """ApplyAttribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["GUID__"] = 2280624963661624826
        self.vs[23]["name"] = """eq_"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = 6991718596332152799
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = 9027082111210098873
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = 7027889624462267929
        self.vs[26]["name"] = """solveRef"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 8406877580895499716

