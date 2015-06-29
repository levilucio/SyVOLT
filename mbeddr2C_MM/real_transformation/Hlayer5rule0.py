

from core.himesis import Himesis

class Hlayer5rule0(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model Hlayer5rule0.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer5rule0, self).__init__(name='Hlayer5rule0', num_nodes=53, edges=[])
        
        # Add the edges
        self.add_edges([[0, 27], [27, 3], [0, 28], [28, 4], [0, 29], [29, 5], [0, 30], [30, 6], [0, 31], [31, 7], [1, 42], [42, 8], [1, 43], [43, 9], [1, 44], [44, 10], [1, 45], [45, 11], [1, 46], [46, 12], [1, 47], [47, 13], [1, 48], [48, 14], [1, 49], [49, 15], [1, 50], [50, 16], [1, 51], [51, 17], [1, 52], [52, 18], [3, 19], [19, 4], [4, 20], [20, 5], [5, 21], [21, 6], [6, 22], [22, 7], [8, 32], [32, 10], [10, 33], [33, 11], [11, 34], [34, 12], [11, 35], [35, 13], [12, 36], [36, 14], [12, 37], [37, 15], [14, 38], [38, 9], [15, 39], [39, 16], [13, 40], [40, 18], [18, 41], [41, 17], [8, 23], [23, 3], [9, 24], [24, 5], [16, 25], [25, 7], [17, 26], [26, 5], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer5rule0"""
        self["GUID__"] = 4146776545960670117
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 5036006750601734948
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 4394575936389003184
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 8402029718365348926
        self.vs[3]["name"] = """layer5rule0class0"""
        self.vs[3]["classtype"] = """ComponentInstance"""
        self.vs[3]["mm__"] = """ComponentInstance"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 2315096559031200359
        self.vs[4]["name"] = """layer5rule0class1"""
        self.vs[4]["classtype"] = """AtomicComponent"""
        self.vs[4]["mm__"] = """AtomicComponent"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = 6705398133570898466
        self.vs[5]["name"] = """layer5rule0class2"""
        self.vs[5]["classtype"] = """ProvidedPort"""
        self.vs[5]["mm__"] = """ProvidedPort"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 3572744860123844885
        self.vs[6]["name"] = """layer5rule0class3"""
        self.vs[6]["classtype"] = """ClientServerInterface"""
        self.vs[6]["mm__"] = """ClientServerInterface"""
        self.vs[6]["cardinality"] = """+"""
        self.vs[6]["GUID__"] = 5645183129957766707
        self.vs[7]["name"] = """layer5rule0class4"""
        self.vs[7]["classtype"] = """Operation"""
        self.vs[7]["mm__"] = """Operation"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 2192362810798067604
        self.vs[8]["name"] = """layer5rule0class5"""
        self.vs[8]["classtype"] = """StatementList"""
        self.vs[8]["mm__"] = """StatementList"""
        self.vs[8]["cardinality"] = """1"""
        self.vs[8]["GUID__"] = 5544517008549638850
        self.vs[9]["name"] = """layer5rule0class6"""
        self.vs[9]["classtype"] = """GlobalVariableDeclaration"""
        self.vs[9]["mm__"] = """GlobalVariableDeclaration"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 3485835700440800937
        self.vs[10]["name"] = """layer5rule0class7"""
        self.vs[10]["classtype"] = """ExpressionStatement"""
        self.vs[10]["mm__"] = """ExpressionStatement"""
        self.vs[10]["cardinality"] = """1"""
        self.vs[10]["GUID__"] = 3109330529400774051
        self.vs[11]["name"] = """layer5rule0class8"""
        self.vs[11]["classtype"] = """AssignmentExpr"""
        self.vs[11]["mm__"] = """AssignmentExpr"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 2430780767401460476
        self.vs[12]["name"] = """layer5rule0class9"""
        self.vs[12]["classtype"] = """GenericDotExpression"""
        self.vs[12]["mm__"] = """GenericDotExpression"""
        self.vs[12]["cardinality"] = """1"""
        self.vs[12]["GUID__"] = 6646293423574752461
        self.vs[13]["name"] = """layer5rule0class10"""
        self.vs[13]["classtype"] = """ReferenceExpr"""
        self.vs[13]["mm__"] = """ReferenceExpr"""
        self.vs[13]["cardinality"] = """1"""
        self.vs[13]["GUID__"] = 8193936145218951719
        self.vs[14]["name"] = """layer5rule0class11"""
        self.vs[14]["classtype"] = """GlobalVarRef"""
        self.vs[14]["mm__"] = """GlobalVarRef"""
        self.vs[14]["cardinality"] = """1"""
        self.vs[14]["GUID__"] = 3520701128308088768
        self.vs[15]["name"] = """layer5rule0class12"""
        self.vs[15]["classtype"] = """GenericMemberRef"""
        self.vs[15]["mm__"] = """GenericMemberRef"""
        self.vs[15]["cardinality"] = """1"""
        self.vs[15]["GUID__"] = 5911127082519133
        self.vs[16]["name"] = """layer5rule0class13"""
        self.vs[16]["classtype"] = """CFunctionPointerStructMember"""
        self.vs[16]["mm__"] = """CFunctionPointerStructMember"""
        self.vs[16]["cardinality"] = """1"""
        self.vs[16]["GUID__"] = 5641193897425791366
        self.vs[17]["name"] = """layer5rule0class14"""
        self.vs[17]["classtype"] = """FunctionPrototype"""
        self.vs[17]["mm__"] = """FunctionPrototype"""
        self.vs[17]["cardinality"] = """1"""
        self.vs[17]["GUID__"] = 2454505263430379099
        self.vs[18]["name"] = """layer5rule0class15"""
        self.vs[18]["classtype"] = """FunctionRefExpr"""
        self.vs[18]["mm__"] = """FunctionRefExpr"""
        self.vs[18]["cardinality"] = """1"""
        self.vs[18]["GUID__"] = 1191548167121688209
        self.vs[19]["associationType"] = """component"""
        self.vs[19]["mm__"] = """directLink_S"""
        self.vs[19]["GUID__"] = 6773934298333545621
        self.vs[20]["associationType"] = """contents"""
        self.vs[20]["mm__"] = """directLink_S"""
        self.vs[20]["GUID__"] = 2647648007995450058
        self.vs[21]["associationType"] = """intf"""
        self.vs[21]["mm__"] = """directLink_S"""
        self.vs[21]["GUID__"] = 7020236564554950372
        self.vs[22]["associationType"] = """contents"""
        self.vs[22]["mm__"] = """directLink_S"""
        self.vs[22]["GUID__"] = 1529554696899346060
        self.vs[23]["mm__"] = """backward_link"""
        self.vs[23]["type"] = """ruleDef"""
        self.vs[23]["GUID__"] = 6990263032803429880
        self.vs[24]["mm__"] = """backward_link"""
        self.vs[24]["type"] = """ruleDef"""
        self.vs[24]["GUID__"] = 829462908918925367
        self.vs[25]["mm__"] = """backward_link"""
        self.vs[25]["type"] = """ruleDef"""
        self.vs[25]["GUID__"] = 1139503900803829041
        self.vs[26]["mm__"] = """backward_link"""
        self.vs[26]["type"] = """ruleDef"""
        self.vs[26]["GUID__"] = 6357984843976391319
        self.vs[27]["mm__"] = """match_contains"""
        self.vs[27]["GUID__"] = 6257965575539903274
        self.vs[28]["mm__"] = """match_contains"""
        self.vs[28]["GUID__"] = 5855131004338983756
        self.vs[29]["mm__"] = """match_contains"""
        self.vs[29]["GUID__"] = 5976264469711352894
        self.vs[30]["mm__"] = """match_contains"""
        self.vs[30]["GUID__"] = 7610130735714772728
        self.vs[31]["mm__"] = """match_contains"""
        self.vs[31]["GUID__"] = 542699724448917723
        self.vs[32]["associationType"] = """statements"""
        self.vs[32]["mm__"] = """directLink_T"""
        self.vs[32]["GUID__"] = 3096577725153672376
        self.vs[33]["associationType"] = """expr"""
        self.vs[33]["mm__"] = """directLink_T"""
        self.vs[33]["GUID__"] = 8495793800928910556
        self.vs[34]["associationType"] = """left"""
        self.vs[34]["mm__"] = """directLink_T"""
        self.vs[34]["GUID__"] = 7272952238891386371
        self.vs[35]["associationType"] = """right"""
        self.vs[35]["mm__"] = """directLink_T"""
        self.vs[35]["GUID__"] = 2252815132830917084
        self.vs[36]["associationType"] = """expression"""
        self.vs[36]["mm__"] = """directLink_T"""
        self.vs[36]["GUID__"] = 1813901418837108077
        self.vs[37]["associationType"] = """target"""
        self.vs[37]["mm__"] = """directLink_T"""
        self.vs[37]["GUID__"] = 674294250268988777
        self.vs[38]["associationType"] = """var"""
        self.vs[38]["mm__"] = """directLink_T"""
        self.vs[38]["GUID__"] = 5257258438714865728
        self.vs[39]["associationType"] = """member"""
        self.vs[39]["mm__"] = """directLink_T"""
        self.vs[39]["GUID__"] = 8568538150816063699
        self.vs[40]["associationType"] = """expression"""
        self.vs[40]["mm__"] = """directLink_T"""
        self.vs[40]["GUID__"] = 5260135453348724743
        self.vs[41]["associationType"] = """function"""
        self.vs[41]["mm__"] = """directLink_T"""
        self.vs[41]["GUID__"] = 8987257125660081192
        self.vs[42]["mm__"] = """apply_contains"""
        self.vs[42]["GUID__"] = 9034674312812547981
        self.vs[43]["mm__"] = """apply_contains"""
        self.vs[43]["GUID__"] = 2260704784613643417
        self.vs[44]["mm__"] = """apply_contains"""
        self.vs[44]["GUID__"] = 2566116379982343982
        self.vs[45]["mm__"] = """apply_contains"""
        self.vs[45]["GUID__"] = 4620309388314857836
        self.vs[46]["mm__"] = """apply_contains"""
        self.vs[46]["GUID__"] = 3686952545634679823
        self.vs[47]["mm__"] = """apply_contains"""
        self.vs[47]["GUID__"] = 3740338045216003039
        self.vs[48]["mm__"] = """apply_contains"""
        self.vs[48]["GUID__"] = 3425288149374468986
        self.vs[49]["mm__"] = """apply_contains"""
        self.vs[49]["GUID__"] = 6774773855012093712
        self.vs[50]["mm__"] = """apply_contains"""
        self.vs[50]["GUID__"] = 6197126052764984794
        self.vs[51]["mm__"] = """apply_contains"""
        self.vs[51]["GUID__"] = 1878780450612680177
        self.vs[52]["mm__"] = """apply_contains"""
        self.vs[52]["GUID__"] = 3246849035945731738

