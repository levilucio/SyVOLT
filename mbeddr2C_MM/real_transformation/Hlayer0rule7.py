

from core.himesis import Himesis

class Hlayer0rule7(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model Hlayer0rule7.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer0rule7, self).__init__(name='Hlayer0rule7', num_nodes=46, edges=[])
        
        # Add the edges
        self.add_edges([[0, 9], [9, 3], [0, 10], [10, 4], [1, 23], [23, 5], [1, 24], [24, 6], [1, 25], [25, 7], [4, 8], [8, 3], [5, 11], [11, 6], [6, 12], [12, 7], [3, 13], [13, 26], [4, 14], [14, 27], [5, 15], [15, 28], [16, 17], [17, 28], [16, 18], [33, 44], [44, 34], [33, 45], [45, 35], [32, 42], [42, 26], [32, 43], [43, 33], [30, 40], [40, 31], [30, 41], [41, 32], [29, 38], [38, 27], [29, 39], [39, 30], [18, 29], [6, 19], [19, 36], [20, 21], [21, 36], [20, 22], [22, 37], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer0rule7"""
        self["GUID__"] = 6043978281190904608
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 5999183413730063715
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 3190680471944695990
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 3836804130670049956
        self.vs[3]["name"] = """layer0rule7class0"""
        self.vs[3]["classtype"] = """AtomicComponent"""
        self.vs[3]["mm__"] = """AtomicComponent"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 9180197533682291551
        self.vs[4]["name"] = """layer0rule7class1"""
        self.vs[4]["classtype"] = """ImplementationModule"""
        self.vs[4]["mm__"] = """ImplementationModule"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = 7130195943879831143
        self.vs[5]["name"] = """layer0rule7class2"""
        self.vs[5]["classtype"] = """StructDeclaration"""
        self.vs[5]["mm__"] = """StructDeclaration"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = 6324766667984600974
        self.vs[6]["name"] = """layer0rule7class3"""
        self.vs[6]["classtype"] = """Member"""
        self.vs[6]["mm__"] = """Member"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = 8277827831017651065
        self.vs[7]["name"] = """layer0rule7class4"""
        self.vs[7]["classtype"] = """Int32Type"""
        self.vs[7]["mm__"] = """Int32Type"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = 5351015819666620020
        self.vs[8]["associationType"] = """contents"""
        self.vs[8]["mm__"] = """directLink_S"""
        self.vs[8]["GUID__"] = 1927790339075514553
        self.vs[9]["mm__"] = """match_contains"""
        self.vs[9]["GUID__"] = 6472214394685509152
        self.vs[10]["mm__"] = """match_contains"""
        self.vs[10]["GUID__"] = 1177292768182515243
        self.vs[11]["associationType"] = """members"""
        self.vs[11]["mm__"] = """directLink_T"""
        self.vs[11]["GUID__"] = 5451065931048666301
        self.vs[12]["associationType"] = """type"""
        self.vs[12]["mm__"] = """directLink_T"""
        self.vs[12]["GUID__"] = 6701417081196416253
        self.vs[13]["mm__"] = """hasAttribute_S"""
        self.vs[13]["GUID__"] = 8166009011459975647
        self.vs[14]["mm__"] = """hasAttribute_S"""
        self.vs[14]["GUID__"] = 5746788480719811854
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 2857941990788544598
        self.vs[16]["name"] = """eq_"""
        self.vs[16]["mm__"] = """Equation"""
        self.vs[16]["GUID__"] = 9207472319898618760
        self.vs[17]["mm__"] = """leftExpr"""
        self.vs[17]["GUID__"] = 2235765348874382986
        self.vs[18]["mm__"] = """rightExpr"""
        self.vs[18]["GUID__"] = 3349247257413671769
        self.vs[19]["mm__"] = """hasAttribute_T"""
        self.vs[19]["GUID__"] = 3254406284413377870
        self.vs[20]["name"] = """eq_"""
        self.vs[20]["mm__"] = """Equation"""
        self.vs[20]["GUID__"] = 4542644803747760995
        self.vs[21]["mm__"] = """leftExpr"""
        self.vs[21]["GUID__"] = 7045297469365392421
        self.vs[22]["mm__"] = """rightExpr"""
        self.vs[22]["GUID__"] = 6933719295919734786
        self.vs[23]["mm__"] = """apply_contains"""
        self.vs[23]["GUID__"] = 1813265584724042527
        self.vs[24]["mm__"] = """apply_contains"""
        self.vs[24]["GUID__"] = 696741190221404480
        self.vs[25]["mm__"] = """apply_contains"""
        self.vs[25]["GUID__"] = 7481980765015423133
        self.vs[26]["name"] = """name"""
        self.vs[26]["mm__"] = """Attribute"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["GUID__"] = 7913966516286602529
        self.vs[27]["name"] = """name"""
        self.vs[27]["mm__"] = """Attribute"""
        self.vs[27]["Type"] = """'String'"""
        self.vs[27]["GUID__"] = 2879355108346105394
        self.vs[28]["name"] = """name"""
        self.vs[28]["mm__"] = """Attribute"""
        self.vs[28]["Type"] = """'String'"""
        self.vs[28]["GUID__"] = 1414887284141066062
        self.vs[29]["name"] = """Concatlayer0rule7class2attribute025"""
        self.vs[29]["mm__"] = """Concat"""
        self.vs[29]["Type"] = """'String'"""
        self.vs[29]["GUID__"] = 6380966635063620256
        self.vs[30]["name"] = """Concatlayer0rule7class2attribute028"""
        self.vs[30]["mm__"] = """Concat"""
        self.vs[30]["Type"] = """'String'"""
        self.vs[30]["GUID__"] = 2698767883335594690
        self.vs[31]["name"] = """_"""
        self.vs[31]["mm__"] = """Constant"""
        self.vs[31]["Type"] = """'String'"""
        self.vs[31]["GUID__"] = 346416986014412607
        self.vs[32]["name"] = """Concatlayer0rule7class2attribute032"""
        self.vs[32]["mm__"] = """Concat"""
        self.vs[32]["Type"] = """'String'"""
        self.vs[32]["GUID__"] = 2939380791487760507
        self.vs[33]["name"] = """Concatlayer0rule7class2attribute035"""
        self.vs[33]["mm__"] = """Concat"""
        self.vs[33]["Type"] = """'String'"""
        self.vs[33]["GUID__"] = 7913614270150489103
        self.vs[34]["name"] = """__"""
        self.vs[34]["mm__"] = """Constant"""
        self.vs[34]["Type"] = """'String'"""
        self.vs[34]["GUID__"] = 5622541824310483761
        self.vs[35]["name"] = """cdata"""
        self.vs[35]["mm__"] = """Constant"""
        self.vs[35]["Type"] = """'String'"""
        self.vs[35]["GUID__"] = 8155790412053758226
        self.vs[36]["name"] = """name"""
        self.vs[36]["mm__"] = """Attribute"""
        self.vs[36]["Type"] = """'String'"""
        self.vs[36]["GUID__"] = 3274052482987671740
        self.vs[37]["name"] = """aMemberSoTheStructIsNotEmpty"""
        self.vs[37]["mm__"] = """Constant"""
        self.vs[37]["Type"] = """'String'"""
        self.vs[37]["GUID__"] = 6658854943631990053
        self.vs[38]["mm__"] = """hasArgs"""
        self.vs[38]["GUID__"] = 2294282451434062057
        self.vs[39]["mm__"] = """hasArgs"""
        self.vs[39]["GUID__"] = 1334749313800948207
        self.vs[40]["mm__"] = """hasArgs"""
        self.vs[40]["GUID__"] = 1795076492664008283
        self.vs[41]["mm__"] = """hasArgs"""
        self.vs[41]["GUID__"] = 7464097489677120215
        self.vs[42]["mm__"] = """hasArgs"""
        self.vs[42]["GUID__"] = 3412118046806804106
        self.vs[43]["mm__"] = """hasArgs"""
        self.vs[43]["GUID__"] = 1761532714512374320
        self.vs[44]["mm__"] = """hasArgs"""
        self.vs[44]["GUID__"] = 3245680290631680434
        self.vs[45]["mm__"] = """hasArgs"""
        self.vs[45]["GUID__"] = 6637675097132479410

