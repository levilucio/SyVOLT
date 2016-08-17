

from core.himesis import Himesis

class HeclassOUTeSuperTypesSolveRefEClassEClassEClassEClass(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HeclassOUTeSuperTypesSolveRefEClassEClassEClassEClass.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HeclassOUTeSuperTypesSolveRefEClassEClassEClassEClass, self).__init__(name='HeclassOUTeSuperTypesSolveRefEClassEClassEClassEClass', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 5], [5, 23], [0, 6], [6, 24], [1, 7], [7, 25], [1, 8], [8, 26], [23, 3], [3, 24], [25, 4], [4, 26], [25, 9], [9, 23], [26, 10], [10, 24], [25, 11], [11, 12], [13, 14], [14, 12], [13, 15], [15, 16], [26, 17], [17, 18], [19, 20], [20, 18], [19, 21], [21, 22], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """eclassOUTeSuperTypesSolveRefEClassEClassEClassEClass"""
        self["GUID__"] = 5266663417605238221
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 8310399152648998700
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 9182450957858660757
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 6497634192737456651
        self.vs[3]["associationType"] = """eSuperTypes"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 914799402436416016
        self.vs[4]["associationType"] = """eSuperTypes"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 4394465094961421463
        self.vs[5]["mm__"] = """match_contains"""
        self.vs[5]["GUID__"] = 2280710708502683294
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 3557459296034388912
        self.vs[7]["mm__"] = """apply_contains"""
        self.vs[7]["GUID__"] = 4124792910777959280
        self.vs[8]["mm__"] = """apply_contains"""
        self.vs[8]["GUID__"] = 8572293634418021468
        self.vs[9]["type"] = """ruleDef"""
        self.vs[9]["mm__"] = """backward_link"""
        self.vs[9]["GUID__"] = 144273159719623019
        self.vs[10]["type"] = """ruleDef"""
        self.vs[10]["mm__"] = """backward_link"""
        self.vs[10]["GUID__"] = 4271644238455682563
        self.vs[11]["mm__"] = """hasAttribute_T"""
        self.vs[11]["GUID__"] = 7321911111801148570
        self.vs[12]["name"] = """ApplyAttribute"""
        self.vs[12]["mm__"] = """Attribute"""
        self.vs[12]["Type"] = """'String'"""
        self.vs[12]["GUID__"] = 3443946010865192410
        self.vs[13]["name"] = """eq_"""
        self.vs[13]["mm__"] = """Equation"""
        self.vs[13]["GUID__"] = 4853635049750493776
        self.vs[14]["mm__"] = """leftExpr"""
        self.vs[14]["GUID__"] = 826881248784973086
        self.vs[15]["mm__"] = """rightExpr"""
        self.vs[15]["GUID__"] = 628283689404054637
        self.vs[16]["name"] = """solveRef"""
        self.vs[16]["mm__"] = """Constant"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["GUID__"] = 818239423598760722
        self.vs[17]["mm__"] = """hasAttribute_T"""
        self.vs[17]["GUID__"] = 3163331830465060941
        self.vs[18]["name"] = """ApplyAttribute"""
        self.vs[18]["mm__"] = """Attribute"""
        self.vs[18]["Type"] = """'String'"""
        self.vs[18]["GUID__"] = 5591659206804292746
        self.vs[19]["name"] = """eq_"""
        self.vs[19]["mm__"] = """Equation"""
        self.vs[19]["GUID__"] = 7737434615505499245
        self.vs[20]["mm__"] = """leftExpr"""
        self.vs[20]["GUID__"] = 8982657982161911071
        self.vs[21]["mm__"] = """rightExpr"""
        self.vs[21]["GUID__"] = 3784104322224024466
        self.vs[22]["name"] = """solveRef"""
        self.vs[22]["mm__"] = """Constant"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["GUID__"] = 7108299339558779142
        self.vs[23]["name"] = """"""
        self.vs[23]["classtype"] = """EClass"""
        self.vs[23]["mm__"] = """EClass"""
        self.vs[23]["cardinality"] = """+"""
        self.vs[23]["GUID__"] = 7666680934550043600
        self.vs[24]["name"] = """"""
        self.vs[24]["classtype"] = """EClass"""
        self.vs[24]["mm__"] = """EClass"""
        self.vs[24]["cardinality"] = """+"""
        self.vs[24]["GUID__"] = 8652419556867075332
        self.vs[25]["name"] = """"""
        self.vs[25]["classtype"] = """EClass"""
        self.vs[25]["mm__"] = """EClass"""
        self.vs[25]["cardinality"] = """1"""
        self.vs[25]["GUID__"] = 5819515384437454252
        self.vs[26]["name"] = """"""
        self.vs[26]["classtype"] = """EClass"""
        self.vs[26]["mm__"] = """EClass"""
        self.vs[26]["cardinality"] = """1"""
        self.vs[26]["GUID__"] = 4220704155905046422

