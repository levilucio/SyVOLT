

from core.himesis import Himesis

class HeparameterOUTeAnnotationsSolveRefEParameterEAnnotationEParameterEAnnotation(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HeparameterOUTeAnnotationsSolveRefEParameterEAnnotationEParameterEAnnotation.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HeparameterOUTeAnnotationsSolveRefEParameterEAnnotationEParameterEAnnotation, self).__init__(name='HeparameterOUTeAnnotationsSolveRefEParameterEAnnotationEParameterEAnnotation', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 6], [6, 5], [0, 8], [8, 7], [1, 10], [10, 9], [1, 12], [12, 11], [5, 3], [3, 7], [9, 4], [4, 11], [9, 13], [13, 5], [11, 14], [14, 7], [9, 15], [15, 16], [17, 18], [18, 16], [17, 19], [19, 20], [11, 21], [21, 22], [23, 24], [24, 22], [23, 25], [25, 26], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """eparameterOUTeAnnotationsSolveRefEParameterEAnnotationEParameterEAnnotation"""
        self["GUID__"] = 1430544255663804267
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 2668911686373056438
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 8715068711506004479
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 3214911711228266273
        self.vs[3]["associationType"] = """eAnnotations"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 8923391237000135008
        self.vs[4]["associationType"] = """eAnnotations"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 5640018753527910213
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EParameter"""
        self.vs[5]["mm__"] = """EParameter"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 316787059944078797
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 9179725539689520026
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EAnnotation"""
        self.vs[7]["mm__"] = """EAnnotation"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 6232084353876037851
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 3585298135366505438
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """EParameter"""
        self.vs[9]["mm__"] = """EParameter"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 4236374234964774932
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 3873390392098880510
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """EAnnotation"""
        self.vs[11]["mm__"] = """EAnnotation"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 5708241351129604936
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 5620772368014585966
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 3015974766966580466
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 2644590606068467225
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 5018154874021548218
        self.vs[16]["name"] = """ApplyAttribute"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["GUID__"] = 5637605795679981987
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 7587114062342180276
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 3511086125847815811
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 1741471255862328860
        self.vs[20]["name"] = """solveRef"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 1947862666677329573
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 8126603078268598036
        self.vs[22]["name"] = """ApplyAttribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["GUID__"] = 8659962513258102212
        self.vs[23]["name"] = """eq_"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = 1651524110289751399
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = 2474842311935853251
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = 5183941945598666911
        self.vs[26]["name"] = """solveRef"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 3551348147948254648

