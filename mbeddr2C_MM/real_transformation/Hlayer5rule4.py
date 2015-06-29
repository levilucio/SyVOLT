

from core.himesis import Himesis

class Hlayer5rule4(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model Hlayer5rule4.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer5rule4, self).__init__(name='Hlayer5rule4', num_nodes=59, edges=[])
        
        # Add the edges
        self.add_edges([[0, 37], [37, 3], [0, 38], [38, 17], [0, 39], [39, 18], [0, 40], [40, 4], [0, 41], [41, 5], [0, 42], [42, 6], [0, 43], [43, 7], [0, 44], [44, 8], [0, 45], [45, 9], [0, 46], [46, 10], [0, 47], [47, 11], [1, 30], [30, 19], [1, 31], [31, 20], [1, 32], [32, 12], [1, 33], [33, 13], [1, 34], [34, 14], [1, 35], [35, 15], [1, 36], [36, 16], [3, 48], [48, 17], [17, 49], [49, 18], [18, 50], [50, 4], [4, 51], [51, 5], [5, 52], [52, 6], [4, 53], [53, 7], [6, 54], [54, 8], [8, 55], [55, 9], [8, 56], [56, 10], [10, 57], [57, 11], [11, 58], [58, 7], [19, 24], [24, 20], [20, 25], [25, 12], [12, 26], [26, 13], [12, 27], [27, 14], [14, 28], [28, 15], [15, 29], [29, 16], [19, 21], [21, 3], [13, 22], [22, 10], [16, 23], [23, 9], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer5rule4"""
        self["GUID__"] = 7652774002010309550
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 3369894426290246996
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 2412211749117660759
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 7129456709445203312
        self.vs[3]["name"] = """layer5rule4class0"""
        self.vs[3]["classtype"] = """TestCase"""
        self.vs[3]["mm__"] = """TestCase"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 3578210111913953940
        self.vs[4]["name"] = """layer5rule4class3"""
        self.vs[4]["classtype"] = """PortAdapterOpCallExpr"""
        self.vs[4]["mm__"] = """PortAdapterOpCallExpr"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = 200014975355575052
        self.vs[5]["name"] = """layer5rule4class4"""
        self.vs[5]["classtype"] = """PortAdapterRefExpr"""
        self.vs[5]["mm__"] = """PortAdapterRefExpr"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 8623869387669997102
        self.vs[6]["name"] = """layer5rule4class5"""
        self.vs[6]["classtype"] = """PortAdapter"""
        self.vs[6]["mm__"] = """PortAdapter"""
        self.vs[6]["cardinality"] = """+"""
        self.vs[6]["GUID__"] = 1771373409346587920
        self.vs[7]["name"] = """layer5rule4class6"""
        self.vs[7]["classtype"] = """Operation"""
        self.vs[7]["mm__"] = """Operation"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 7439602118295569202
        self.vs[8]["name"] = """layer5rule4class7"""
        self.vs[8]["classtype"] = """AdapterInstancePortRef"""
        self.vs[8]["mm__"] = """AdapterInstancePortRef"""
        self.vs[8]["cardinality"] = """+"""
        self.vs[8]["GUID__"] = 3872583663723128399
        self.vs[9]["name"] = """layer5rule4class8"""
        self.vs[9]["classtype"] = """ComponentInstance"""
        self.vs[9]["mm__"] = """ComponentInstance"""
        self.vs[9]["cardinality"] = """+"""
        self.vs[9]["GUID__"] = 1758249909203467829
        self.vs[10]["name"] = """layer5rule4class9"""
        self.vs[10]["classtype"] = """ProvidedPort"""
        self.vs[10]["mm__"] = """ProvidedPort"""
        self.vs[10]["cardinality"] = """+"""
        self.vs[10]["GUID__"] = 2661943878872091018
        self.vs[11]["name"] = """layer5rule4class10"""
        self.vs[11]["classtype"] = """ClientServerInterface"""
        self.vs[11]["mm__"] = """ClientServerInterface"""
        self.vs[11]["cardinality"] = """+"""
        self.vs[11]["GUID__"] = 2613355876425137437
        self.vs[12]["name"] = """layer5rule4class13"""
        self.vs[12]["classtype"] = """FunctionCall"""
        self.vs[12]["mm__"] = """FunctionCall"""
        self.vs[12]["cardinality"] = """1"""
        self.vs[12]["GUID__"] = 8500593067850645416
        self.vs[13]["name"] = """layer5rule4class14"""
        self.vs[13]["classtype"] = """FunctionPrototype"""
        self.vs[13]["mm__"] = """FunctionPrototype"""
        self.vs[13]["cardinality"] = """1"""
        self.vs[13]["GUID__"] = 6107576475897913088
        self.vs[14]["name"] = """layer5rule4class15"""
        self.vs[14]["classtype"] = """ReferenceExpr"""
        self.vs[14]["mm__"] = """ReferenceExpr"""
        self.vs[14]["cardinality"] = """1"""
        self.vs[14]["GUID__"] = 3806509975213720766
        self.vs[15]["name"] = """layer5rule4class16"""
        self.vs[15]["classtype"] = """GlobalVarRef"""
        self.vs[15]["mm__"] = """GlobalVarRef"""
        self.vs[15]["cardinality"] = """1"""
        self.vs[15]["GUID__"] = 8305913537543110178
        self.vs[16]["name"] = """layer5rule4class17"""
        self.vs[16]["classtype"] = """GlobalVariableDeclaration"""
        self.vs[16]["mm__"] = """GlobalVariableDeclaration"""
        self.vs[16]["cardinality"] = """1"""
        self.vs[16]["GUID__"] = 4739570858794023854
        self.vs[17]["name"] = """layer5rule4class1"""
        self.vs[17]["classtype"] = """StatementList"""
        self.vs[17]["mm__"] = """StatementList"""
        self.vs[17]["cardinality"] = """+"""
        self.vs[17]["GUID__"] = 1094161512538877605
        self.vs[18]["name"] = """layer5rule4class2"""
        self.vs[18]["classtype"] = """ExpressionStatement"""
        self.vs[18]["mm__"] = """ExpressionStatement"""
        self.vs[18]["cardinality"] = """+"""
        self.vs[18]["GUID__"] = 6779574176277645264
        self.vs[19]["name"] = """layer5rule4class11"""
        self.vs[19]["classtype"] = """StatementList"""
        self.vs[19]["mm__"] = """StatementList"""
        self.vs[19]["cardinality"] = """1"""
        self.vs[19]["GUID__"] = 8426973606351620102
        self.vs[20]["name"] = """layer5rule4class12"""
        self.vs[20]["classtype"] = """ExpressionStatement"""
        self.vs[20]["mm__"] = """ExpressionStatement"""
        self.vs[20]["cardinality"] = """1"""
        self.vs[20]["GUID__"] = 8251977577716450310
        self.vs[21]["mm__"] = """backward_link"""
        self.vs[21]["type"] = """ruleDef"""
        self.vs[21]["GUID__"] = 6637904582899816635
        self.vs[22]["mm__"] = """backward_link"""
        self.vs[22]["type"] = """ruleDef"""
        self.vs[22]["GUID__"] = 4715861908337802051
        self.vs[23]["mm__"] = """backward_link"""
        self.vs[23]["type"] = """ruleDef"""
        self.vs[23]["GUID__"] = 2132950492449703618
        self.vs[24]["associationType"] = """statements"""
        self.vs[24]["mm__"] = """directLink_T"""
        self.vs[24]["GUID__"] = 2946221571539264750
        self.vs[25]["associationType"] = """expr"""
        self.vs[25]["mm__"] = """directLink_T"""
        self.vs[25]["GUID__"] = 6823444365671539266
        self.vs[26]["associationType"] = """function"""
        self.vs[26]["mm__"] = """directLink_T"""
        self.vs[26]["GUID__"] = 2855363175289281551
        self.vs[27]["associationType"] = """actuals"""
        self.vs[27]["mm__"] = """directLink_T"""
        self.vs[27]["GUID__"] = 7916486637775030364
        self.vs[28]["associationType"] = """expression"""
        self.vs[28]["mm__"] = """directLink_T"""
        self.vs[28]["GUID__"] = 5428604947837217691
        self.vs[29]["associationType"] = """var"""
        self.vs[29]["mm__"] = """directLink_T"""
        self.vs[29]["GUID__"] = 6369594514963863392
        self.vs[30]["mm__"] = """apply_contains"""
        self.vs[30]["GUID__"] = 1450894859004919280
        self.vs[31]["mm__"] = """apply_contains"""
        self.vs[31]["GUID__"] = 1588760896841281405
        self.vs[32]["mm__"] = """apply_contains"""
        self.vs[32]["GUID__"] = 5375195393361092228
        self.vs[33]["mm__"] = """apply_contains"""
        self.vs[33]["GUID__"] = 6922045048238403544
        self.vs[34]["mm__"] = """apply_contains"""
        self.vs[34]["GUID__"] = 5441860462227370957
        self.vs[35]["mm__"] = """apply_contains"""
        self.vs[35]["GUID__"] = 7964257588139032811
        self.vs[36]["mm__"] = """apply_contains"""
        self.vs[36]["GUID__"] = 975905573905948148
        self.vs[37]["mm__"] = """match_contains"""
        self.vs[37]["GUID__"] = 804524800659514520
        self.vs[38]["mm__"] = """match_contains"""
        self.vs[38]["GUID__"] = 1909952255423376831
        self.vs[39]["mm__"] = """match_contains"""
        self.vs[39]["GUID__"] = 5994444706977297450
        self.vs[40]["mm__"] = """match_contains"""
        self.vs[40]["GUID__"] = 6387888042878324688
        self.vs[41]["mm__"] = """match_contains"""
        self.vs[41]["GUID__"] = 1414259003206905701
        self.vs[42]["mm__"] = """match_contains"""
        self.vs[42]["GUID__"] = 1892829604400863097
        self.vs[43]["mm__"] = """match_contains"""
        self.vs[43]["GUID__"] = 3390769209860798325
        self.vs[44]["mm__"] = """match_contains"""
        self.vs[44]["GUID__"] = 2385523544246255871
        self.vs[45]["mm__"] = """match_contains"""
        self.vs[45]["GUID__"] = 8489664226841677554
        self.vs[46]["mm__"] = """match_contains"""
        self.vs[46]["GUID__"] = 7070554508272643451
        self.vs[47]["mm__"] = """match_contains"""
        self.vs[47]["GUID__"] = 524694952413846800
        self.vs[48]["associationType"] = """body"""
        self.vs[48]["mm__"] = """directLink_S"""
        self.vs[48]["GUID__"] = 7344488426713159292
        self.vs[49]["associationType"] = """statements"""
        self.vs[49]["mm__"] = """directLink_S"""
        self.vs[49]["GUID__"] = 2989075655098902576
        self.vs[50]["associationType"] = """expr"""
        self.vs[50]["mm__"] = """directLink_S"""
        self.vs[50]["GUID__"] = 352123888005362131
        self.vs[51]["associationType"] = """expression"""
        self.vs[51]["mm__"] = """directLink_S"""
        self.vs[51]["GUID__"] = 8587785018531419353
        self.vs[52]["associationType"] = """portAdater"""
        self.vs[52]["mm__"] = """directLink_S"""
        self.vs[52]["GUID__"] = 2508708240031525858
        self.vs[53]["associationType"] = """operation"""
        self.vs[53]["mm__"] = """directLink_S"""
        self.vs[53]["GUID__"] = 7842628301372633563
        self.vs[54]["associationType"] = """portRef"""
        self.vs[54]["mm__"] = """directLink_S"""
        self.vs[54]["GUID__"] = 6816984862372654794
        self.vs[55]["associationType"] = """instance"""
        self.vs[55]["mm__"] = """directLink_S"""
        self.vs[55]["GUID__"] = 428551165815331971
        self.vs[56]["associationType"] = """port"""
        self.vs[56]["mm__"] = """directLink_S"""
        self.vs[56]["GUID__"] = 7990524065804380861
        self.vs[57]["associationType"] = """intf"""
        self.vs[57]["mm__"] = """directLink_S"""
        self.vs[57]["GUID__"] = 1367745536530296504
        self.vs[58]["associationType"] = """contents"""
        self.vs[58]["mm__"] = """directLink_S"""
        self.vs[58]["GUID__"] = 3072124134301436094

