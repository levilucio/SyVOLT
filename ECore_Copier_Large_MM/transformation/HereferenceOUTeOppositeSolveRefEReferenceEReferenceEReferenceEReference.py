

from core.himesis import Himesis

class HereferenceOUTeOppositeSolveRefEReferenceEReferenceEReferenceEReference(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HereferenceOUTeOppositeSolveRefEReferenceEReferenceEReferenceEReference.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HereferenceOUTeOppositeSolveRefEReferenceEReferenceEReferenceEReference, self).__init__(name='HereferenceOUTeOppositeSolveRefEReferenceEReferenceEReferenceEReference', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 5], [5, 23], [0, 6], [6, 24], [1, 7], [7, 25], [1, 8], [8, 26], [23, 3], [3, 24], [25, 4], [4, 26], [25, 9], [9, 23], [26, 10], [10, 24], [25, 11], [11, 12], [13, 14], [14, 12], [13, 15], [15, 16], [26, 17], [17, 18], [19, 20], [20, 18], [19, 21], [21, 22], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """ereferenceOUTeOppositeSolveRefEReferenceEReferenceEReferenceEReference"""
        self["GUID__"] = 2451552413745361105
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 1837447993315956507
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 1986431090386050598
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 8633168053155733558
        self.vs[3]["associationType"] = """eOpposite"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 4213906265256877012
        self.vs[4]["associationType"] = """eOpposite"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 6355777157765875769
        self.vs[5]["mm__"] = """match_contains"""
        self.vs[5]["GUID__"] = 8507921989916365936
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 8765896690482811779
        self.vs[7]["mm__"] = """apply_contains"""
        self.vs[7]["GUID__"] = 1756326056661489658
        self.vs[8]["mm__"] = """apply_contains"""
        self.vs[8]["GUID__"] = 8351968437955909123
        self.vs[9]["type"] = """ruleDef"""
        self.vs[9]["mm__"] = """backward_link"""
        self.vs[9]["GUID__"] = 2705791796664067460
        self.vs[10]["type"] = """ruleDef"""
        self.vs[10]["mm__"] = """backward_link"""
        self.vs[10]["GUID__"] = 4743030536654178119
        self.vs[11]["mm__"] = """hasAttribute_T"""
        self.vs[11]["GUID__"] = 3507015829727038313
        self.vs[12]["name"] = """ApplyAttribute"""
        self.vs[12]["mm__"] = """Attribute"""
        self.vs[12]["Type"] = """'String'"""
        self.vs[12]["GUID__"] = 5825105247432555064
        self.vs[13]["name"] = """eq_"""
        self.vs[13]["mm__"] = """Equation"""
        self.vs[13]["GUID__"] = 305725488706338772
        self.vs[14]["mm__"] = """leftExpr"""
        self.vs[14]["GUID__"] = 9054587624744604393
        self.vs[15]["mm__"] = """rightExpr"""
        self.vs[15]["GUID__"] = 8340045429772277895
        self.vs[16]["name"] = """solveRef"""
        self.vs[16]["mm__"] = """Constant"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["GUID__"] = 2458726599193782503
        self.vs[17]["mm__"] = """hasAttribute_T"""
        self.vs[17]["GUID__"] = 2983746116981615828
        self.vs[18]["name"] = """ApplyAttribute"""
        self.vs[18]["mm__"] = """Attribute"""
        self.vs[18]["Type"] = """'String'"""
        self.vs[18]["GUID__"] = 2919711487513172229
        self.vs[19]["name"] = """eq_"""
        self.vs[19]["mm__"] = """Equation"""
        self.vs[19]["GUID__"] = 4791857147731652395
        self.vs[20]["mm__"] = """leftExpr"""
        self.vs[20]["GUID__"] = 3507373084969415749
        self.vs[21]["mm__"] = """rightExpr"""
        self.vs[21]["GUID__"] = 8942599703773623034
        self.vs[22]["name"] = """solveRef"""
        self.vs[22]["mm__"] = """Constant"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["GUID__"] = 3510903869130054768
        self.vs[23]["name"] = """"""
        self.vs[23]["classtype"] = """EReference"""
        self.vs[23]["mm__"] = """EReference"""
        self.vs[23]["cardinality"] = """+"""
        self.vs[23]["GUID__"] = 6440169305873853142
        self.vs[24]["name"] = """"""
        self.vs[24]["classtype"] = """EReference"""
        self.vs[24]["mm__"] = """EReference"""
        self.vs[24]["cardinality"] = """+"""
        self.vs[24]["GUID__"] = 209835955097807820
        self.vs[25]["name"] = """"""
        self.vs[25]["classtype"] = """EReference"""
        self.vs[25]["mm__"] = """EReference"""
        self.vs[25]["cardinality"] = """1"""
        self.vs[25]["GUID__"] = 6011167772335322370
        self.vs[26]["name"] = """"""
        self.vs[26]["classtype"] = """EReference"""
        self.vs[26]["mm__"] = """EReference"""
        self.vs[26]["cardinality"] = """1"""
        self.vs[26]["GUID__"] = 7024827212816660626

