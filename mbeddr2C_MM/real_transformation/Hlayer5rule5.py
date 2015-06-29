

from core.himesis import Himesis

class Hlayer5rule5(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model Hlayer5rule5.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer5rule5, self).__init__(name='Hlayer5rule5', num_nodes=39, edges=[])
        
        # Add the edges
        self.add_edges([[0, 33], [33, 17], [0, 34], [34, 3], [0, 35], [35, 4], [0, 36], [36, 5], [0, 37], [37, 6], [0, 38], [38, 7], [1, 24], [24, 18], [1, 25], [25, 8], [1, 26], [26, 9], [1, 27], [27, 10], [5, 28], [28, 17], [17, 29], [29, 3], [3, 30], [30, 4], [4, 31], [31, 6], [6, 32], [32, 7], [18, 21], [21, 8], [8, 22], [22, 9], [9, 23], [23, 10], [18, 19], [19, 5], [10, 20], [20, 7], [5, 11], [11, 12], [13, 14], [14, 12], [13, 15], [15, 16], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer5rule5"""
        self["GUID__"] = 873918934989132844
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 478660089037522727
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 4012428690845927965
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 445901609008456168
        self.vs[3]["name"] = """layer5rule5class1"""
        self.vs[3]["classtype"] = """ReturnStatement"""
        self.vs[3]["mm__"] = """ReturnStatement"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 4244048652318320202
        self.vs[4]["name"] = """layer5rule5class2"""
        self.vs[4]["classtype"] = """ExecuteTestExpression"""
        self.vs[4]["mm__"] = """ExecuteTestExpression"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = 6377712599575632639
        self.vs[5]["name"] = """layer5rule5class3"""
        self.vs[5]["classtype"] = """Function"""
        self.vs[5]["mm__"] = """Function"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 9119019302152291301
        self.vs[6]["name"] = """layer5rule5class4"""
        self.vs[6]["classtype"] = """TestCaseRef"""
        self.vs[6]["mm__"] = """TestCaseRef"""
        self.vs[6]["cardinality"] = """+"""
        self.vs[6]["GUID__"] = 7469778976760759634
        self.vs[7]["name"] = """layer5rule5class5"""
        self.vs[7]["classtype"] = """TestCase"""
        self.vs[7]["mm__"] = """TestCase"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 8439416226538690250
        self.vs[8]["name"] = """layer5rule5class7"""
        self.vs[8]["classtype"] = """ExpressionStatement"""
        self.vs[8]["mm__"] = """ExpressionStatement"""
        self.vs[8]["cardinality"] = """1"""
        self.vs[8]["GUID__"] = 7753734859488883436
        self.vs[9]["name"] = """layer5rule5class8"""
        self.vs[9]["classtype"] = """FunctionCall"""
        self.vs[9]["mm__"] = """FunctionCall"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 1571857363250931876
        self.vs[10]["name"] = """layer5rule5class9"""
        self.vs[10]["classtype"] = """FunctionPrototype"""
        self.vs[10]["mm__"] = """FunctionPrototype"""
        self.vs[10]["cardinality"] = """1"""
        self.vs[10]["GUID__"] = 198578805431785405
        self.vs[11]["mm__"] = """hasAttribute_S"""
        self.vs[11]["GUID__"] = 1941499065582881242
        self.vs[12]["name"] = """name"""
        self.vs[12]["Type"] = """'String'"""
        self.vs[12]["mm__"] = """Attribute"""
        self.vs[12]["GUID__"] = 6261909617746448138
        self.vs[13]["name"] = """eq_"""
        self.vs[13]["mm__"] = """Equation"""
        self.vs[13]["GUID__"] = 7992151651019580770
        self.vs[14]["mm__"] = """leftExpr"""
        self.vs[14]["GUID__"] = 854037207489565305
        self.vs[15]["mm__"] = """rightExpr"""
        self.vs[15]["GUID__"] = 6983341580979366517
        self.vs[16]["name"] = """main"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Constant"""
        self.vs[16]["GUID__"] = 5089919465811825624
        self.vs[17]["name"] = """layer5rule5class0"""
        self.vs[17]["classtype"] = """StatementList"""
        self.vs[17]["mm__"] = """StatementList"""
        self.vs[17]["cardinality"] = """+"""
        self.vs[17]["GUID__"] = 490136503311859855
        self.vs[18]["name"] = """layer5rule5class6"""
        self.vs[18]["classtype"] = """StatementList"""
        self.vs[18]["mm__"] = """StatementList"""
        self.vs[18]["cardinality"] = """1"""
        self.vs[18]["GUID__"] = 75221269659015065
        self.vs[19]["mm__"] = """backward_link"""
        self.vs[19]["type"] = """ruleDef"""
        self.vs[19]["GUID__"] = 3869624171291631148
        self.vs[20]["mm__"] = """backward_link"""
        self.vs[20]["type"] = """ruleDef"""
        self.vs[20]["GUID__"] = 7907415947053462786
        self.vs[21]["associationType"] = """statements"""
        self.vs[21]["mm__"] = """directLink_T"""
        self.vs[21]["GUID__"] = 8115364050007371057
        self.vs[22]["associationType"] = """expr"""
        self.vs[22]["mm__"] = """directLink_T"""
        self.vs[22]["GUID__"] = 5779843021669224081
        self.vs[23]["associationType"] = """function"""
        self.vs[23]["mm__"] = """directLink_T"""
        self.vs[23]["GUID__"] = 3760084984120839811
        self.vs[24]["mm__"] = """apply_contains"""
        self.vs[24]["GUID__"] = 8458791409168808489
        self.vs[25]["mm__"] = """apply_contains"""
        self.vs[25]["GUID__"] = 5264885225752288210
        self.vs[26]["mm__"] = """apply_contains"""
        self.vs[26]["GUID__"] = 6503498514981821974
        self.vs[27]["mm__"] = """apply_contains"""
        self.vs[27]["GUID__"] = 7277667308428532092
        self.vs[28]["associationType"] = """body"""
        self.vs[28]["mm__"] = """directLink_S"""
        self.vs[28]["GUID__"] = 7385553045433223686
        self.vs[29]["associationType"] = """statements"""
        self.vs[29]["mm__"] = """directLink_S"""
        self.vs[29]["GUID__"] = 5355417078143001992
        self.vs[30]["associationType"] = """expression"""
        self.vs[30]["mm__"] = """directLink_S"""
        self.vs[30]["GUID__"] = 1184113689356131020
        self.vs[31]["associationType"] = """tests"""
        self.vs[31]["mm__"] = """directLink_S"""
        self.vs[31]["GUID__"] = 2314231164376789232
        self.vs[32]["associationType"] = """testcase"""
        self.vs[32]["mm__"] = """directLink_S"""
        self.vs[32]["GUID__"] = 4869830686103610131
        self.vs[33]["mm__"] = """match_contains"""
        self.vs[33]["GUID__"] = 4454145366199609167
        self.vs[34]["mm__"] = """match_contains"""
        self.vs[34]["GUID__"] = 1483099857984716922
        self.vs[35]["mm__"] = """match_contains"""
        self.vs[35]["GUID__"] = 2831587135940643698
        self.vs[36]["mm__"] = """match_contains"""
        self.vs[36]["GUID__"] = 3905708171909959510
        self.vs[37]["mm__"] = """match_contains"""
        self.vs[37]["GUID__"] = 3746754048886155218
        self.vs[38]["mm__"] = """match_contains"""
        self.vs[38]["GUID__"] = 6168338643398228179

