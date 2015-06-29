

from core.himesis import Himesis

class Hlayer3rule4(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model Hlayer3rule4.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer3rule4, self).__init__(name='Hlayer3rule4', num_nodes=56, edges=[])
        
        # Add the edges
        self.add_edges([[0, 29], [29, 13], [0, 30], [30, 3], [0, 31], [31, 4], [0, 32], [32, 5], [1, 33], [33, 14], [1, 34], [34, 6], [1, 35], [35, 7], [1, 36], [36, 8], [13, 17], [17, 3], [3, 18], [18, 4], [4, 19], [19, 5], [14, 20], [20, 6], [6, 21], [21, 8], [8, 22], [22, 7], [14, 15], [15, 13], [7, 16], [16, 5], [13, 23], [23, 37], [3, 24], [24, 38], [4, 25], [25, 39], [6, 9], [9, 40], [10, 11], [11, 40], [10, 12], [45, 54], [54, 39], [45, 55], [55, 28], [44, 52], [52, 27], [44, 53], [53, 45], [43, 50], [50, 38], [43, 51], [51, 44], [42, 48], [48, 26], [42, 49], [49, 43], [41, 46], [46, 37], [41, 47], [47, 42], [12, 41], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer3rule4"""
        self["GUID__"] = 766684514095489774
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 2855893759336241122
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 5554166662560629798
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 861877490726772978
        self.vs[3]["name"] = """layer3rule4class1"""
        self.vs[3]["classtype"] = """InstanceConfiguration"""
        self.vs[3]["mm__"] = """InstanceConfiguration"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 2892951853224639177
        self.vs[4]["name"] = """layer3rule4class2"""
        self.vs[4]["classtype"] = """ComponentInstance"""
        self.vs[4]["mm__"] = """ComponentInstance"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = 1254351532880989008
        self.vs[5]["name"] = """layer3rule4class3"""
        self.vs[5]["classtype"] = """AtomicComponent"""
        self.vs[5]["mm__"] = """AtomicComponent"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 1662334693066359797
        self.vs[6]["name"] = """layer3rule4class5"""
        self.vs[6]["classtype"] = """GlobalVariableDeclaration"""
        self.vs[6]["mm__"] = """GlobalVariableDeclaration"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = 7815867010767739046
        self.vs[7]["name"] = """layer3rule4class6"""
        self.vs[7]["classtype"] = """TypeDef"""
        self.vs[7]["mm__"] = """TypeDef"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = 1572226440564228267
        self.vs[8]["name"] = """layer3rule4class7"""
        self.vs[8]["classtype"] = """TypeDefType"""
        self.vs[8]["mm__"] = """TypeDefType"""
        self.vs[8]["cardinality"] = """1"""
        self.vs[8]["GUID__"] = 5559463802918952922
        self.vs[9]["mm__"] = """hasAttribute_T"""
        self.vs[9]["GUID__"] = 1093688966723297102
        self.vs[10]["name"] = """eq_"""
        self.vs[10]["mm__"] = """Equation"""
        self.vs[10]["GUID__"] = 6608295876924689783
        self.vs[11]["mm__"] = """leftExpr"""
        self.vs[11]["GUID__"] = 2948950787129015974
        self.vs[12]["mm__"] = """rightExpr"""
        self.vs[12]["GUID__"] = 9180637814226081599
        self.vs[13]["name"] = """layer3rule4class0"""
        self.vs[13]["classtype"] = """ImplementationModule"""
        self.vs[13]["mm__"] = """ImplementationModule"""
        self.vs[13]["cardinality"] = """+"""
        self.vs[13]["GUID__"] = 6693392221308582603
        self.vs[14]["name"] = """layer3rule4class4"""
        self.vs[14]["classtype"] = """ImplementationModule"""
        self.vs[14]["mm__"] = """ImplementationModule"""
        self.vs[14]["cardinality"] = """1"""
        self.vs[14]["GUID__"] = 2797137208999517740
        self.vs[15]["mm__"] = """backward_link"""
        self.vs[15]["type"] = """ruleDef"""
        self.vs[15]["GUID__"] = 8307236384032173448
        self.vs[16]["mm__"] = """backward_link"""
        self.vs[16]["type"] = """ruleDef"""
        self.vs[16]["GUID__"] = 2307731275428039866
        self.vs[17]["associationType"] = """contents"""
        self.vs[17]["mm__"] = """directLink_S"""
        self.vs[17]["GUID__"] = 8123717502780960098
        self.vs[18]["associationType"] = """contents"""
        self.vs[18]["mm__"] = """directLink_S"""
        self.vs[18]["GUID__"] = 919284578813644081
        self.vs[19]["associationType"] = """component"""
        self.vs[19]["mm__"] = """directLink_S"""
        self.vs[19]["GUID__"] = 5232738202612568355
        self.vs[20]["associationType"] = """contents"""
        self.vs[20]["mm__"] = """directLink_T"""
        self.vs[20]["GUID__"] = 7591762119852663607
        self.vs[21]["associationType"] = """type"""
        self.vs[21]["mm__"] = """directLink_T"""
        self.vs[21]["GUID__"] = 2970537261741923678
        self.vs[22]["associationType"] = """typeDef"""
        self.vs[22]["mm__"] = """directLink_T"""
        self.vs[22]["GUID__"] = 668774803909097705
        self.vs[23]["mm__"] = """hasAttribute_S"""
        self.vs[23]["GUID__"] = 7860163448696629426
        self.vs[24]["mm__"] = """hasAttribute_S"""
        self.vs[24]["GUID__"] = 4859009802049182246
        self.vs[25]["mm__"] = """hasAttribute_S"""
        self.vs[25]["GUID__"] = 8950049947615488763
        self.vs[26]["name"] = """_"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 5404405446692895251
        self.vs[27]["name"] = """_"""
        self.vs[27]["Type"] = """'String'"""
        self.vs[27]["mm__"] = """Constant"""
        self.vs[27]["GUID__"] = 4257709008574989236
        self.vs[28]["name"] = """__instance"""
        self.vs[28]["Type"] = """'String'"""
        self.vs[28]["mm__"] = """Constant"""
        self.vs[28]["GUID__"] = 5433921438511756836
        self.vs[29]["mm__"] = """match_contains"""
        self.vs[29]["GUID__"] = 2059652295495694982
        self.vs[30]["mm__"] = """match_contains"""
        self.vs[30]["GUID__"] = 3604985734756890020
        self.vs[31]["mm__"] = """match_contains"""
        self.vs[31]["GUID__"] = 977562034838074428
        self.vs[32]["mm__"] = """match_contains"""
        self.vs[32]["GUID__"] = 6399094226833921544
        self.vs[33]["mm__"] = """apply_contains"""
        self.vs[33]["GUID__"] = 3896308376356182299
        self.vs[34]["mm__"] = """apply_contains"""
        self.vs[34]["GUID__"] = 6105148381179700796
        self.vs[35]["mm__"] = """apply_contains"""
        self.vs[35]["GUID__"] = 7457311495627498849
        self.vs[36]["mm__"] = """apply_contains"""
        self.vs[36]["GUID__"] = 8373672824576406240
        self.vs[37]["name"] = """name"""
        self.vs[37]["Type"] = """'String'"""
        self.vs[37]["mm__"] = """Attribute"""
        self.vs[37]["GUID__"] = 5922442223328582141
        self.vs[38]["name"] = """name"""
        self.vs[38]["Type"] = """'String'"""
        self.vs[38]["mm__"] = """Attribute"""
        self.vs[38]["GUID__"] = 4209121619832552406
        self.vs[39]["name"] = """name"""
        self.vs[39]["Type"] = """'String'"""
        self.vs[39]["mm__"] = """Attribute"""
        self.vs[39]["GUID__"] = 811362553922350951
        self.vs[40]["name"] = """name"""
        self.vs[40]["Type"] = """'String'"""
        self.vs[40]["mm__"] = """Attribute"""
        self.vs[40]["GUID__"] = 5761920384933473610
        self.vs[41]["name"] = """Concatlayer3rule4class5attribute038"""
        self.vs[41]["Type"] = """'String'"""
        self.vs[41]["mm__"] = """Concat"""
        self.vs[41]["GUID__"] = 2183444858396997387
        self.vs[42]["name"] = """Concatlayer3rule4class5attribute041"""
        self.vs[42]["Type"] = """'String'"""
        self.vs[42]["mm__"] = """Concat"""
        self.vs[42]["GUID__"] = 2943453852148898613
        self.vs[43]["name"] = """Concatlayer3rule4class5attribute045"""
        self.vs[43]["Type"] = """'String'"""
        self.vs[43]["mm__"] = """Concat"""
        self.vs[43]["GUID__"] = 6578270659954981768
        self.vs[44]["name"] = """Concatlayer3rule4class5attribute048"""
        self.vs[44]["Type"] = """'String'"""
        self.vs[44]["mm__"] = """Concat"""
        self.vs[44]["GUID__"] = 4659764052448285288
        self.vs[45]["name"] = """Concatlayer3rule4class5attribute052"""
        self.vs[45]["Type"] = """'String'"""
        self.vs[45]["mm__"] = """Concat"""
        self.vs[45]["GUID__"] = 6672772346882571234
        self.vs[46]["mm__"] = """hasArgs"""
        self.vs[46]["GUID__"] = 7522934091316624929
        self.vs[47]["mm__"] = """hasArgs"""
        self.vs[47]["GUID__"] = 2996975096814463388
        self.vs[48]["mm__"] = """hasArgs"""
        self.vs[48]["GUID__"] = 9082293821264327451
        self.vs[49]["mm__"] = """hasArgs"""
        self.vs[49]["GUID__"] = 6490358640143443793
        self.vs[50]["mm__"] = """hasArgs"""
        self.vs[50]["GUID__"] = 737005090480625312
        self.vs[51]["mm__"] = """hasArgs"""
        self.vs[51]["GUID__"] = 8260850113699970739
        self.vs[52]["mm__"] = """hasArgs"""
        self.vs[52]["GUID__"] = 5115392028809831406
        self.vs[53]["mm__"] = """hasArgs"""
        self.vs[53]["GUID__"] = 3297211347727579051
        self.vs[54]["mm__"] = """hasArgs"""
        self.vs[54]["GUID__"] = 344698052749558211
        self.vs[55]["mm__"] = """hasArgs"""
        self.vs[55]["GUID__"] = 362357337736855508

