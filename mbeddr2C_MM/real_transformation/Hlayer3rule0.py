

from core.himesis import Himesis

class Hlayer3rule0(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model Hlayer3rule0.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer3rule0, self).__init__(name='Hlayer3rule0', num_nodes=37, edges=[])
        
        # Add the edges
        self.add_edges([[0, 28], [28, 10], [0, 29], [29, 3], [0, 30], [30, 4], [1, 31], [31, 11], [1, 32], [32, 5], [1, 33], [33, 6], [10, 12], [12, 3], [3, 13], [13, 4], [11, 14], [14, 5], [5, 15], [15, 6], [11, 7], [7, 10], [10, 16], [16, 34], [3, 17], [17, 35], [18, 19], [19, 35], [18, 20], [20, 21], [5, 8], [8, 36], [22, 23], [23, 36], [22, 24], [9, 25], [25, 34], [9, 26], [26, 27], [24, 9], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer3rule0"""
        self["GUID__"] = 3674717325156401178
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 8863403621159937389
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 8347296578088803802
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 2534056146806697903
        self.vs[3]["name"] = """layer3rule0class1"""
        self.vs[3]["classtype"] = """Function"""
        self.vs[3]["mm__"] = """Function"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 7156038492867291463
        self.vs[4]["name"] = """layer3rule0class2"""
        self.vs[4]["classtype"] = """Int32Type"""
        self.vs[4]["mm__"] = """Int32Type"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = 4857076417410840073
        self.vs[5]["name"] = """layer3rule0class4"""
        self.vs[5]["classtype"] = """FunctionPrototype"""
        self.vs[5]["mm__"] = """FunctionPrototype"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = 5286521347939831326
        self.vs[6]["name"] = """layer3rule0class5"""
        self.vs[6]["classtype"] = """VoidType"""
        self.vs[6]["mm__"] = """VoidType"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = 8367554622308105629
        self.vs[7]["mm__"] = """backward_link"""
        self.vs[7]["type"] = """ruleDef"""
        self.vs[7]["GUID__"] = 5415789609492674686
        self.vs[8]["mm__"] = """hasAttribute_T"""
        self.vs[8]["GUID__"] = 1615810425978492470
        self.vs[9]["name"] = """Concatlayer3rule0class4attribute033"""
        self.vs[9]["Type"] = """'String'"""
        self.vs[9]["mm__"] = """Concat"""
        self.vs[9]["GUID__"] = 7966276665064422715
        self.vs[10]["name"] = """layer3rule0class0"""
        self.vs[10]["classtype"] = """ImplementationModule"""
        self.vs[10]["mm__"] = """ImplementationModule"""
        self.vs[10]["cardinality"] = """+"""
        self.vs[10]["GUID__"] = 7890747462217777721
        self.vs[11]["name"] = """layer3rule0class3"""
        self.vs[11]["classtype"] = """ImplementationModule"""
        self.vs[11]["mm__"] = """ImplementationModule"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 5760613631334723844
        self.vs[12]["associationType"] = """contents"""
        self.vs[12]["mm__"] = """directLink_S"""
        self.vs[12]["GUID__"] = 2471344942558196628
        self.vs[13]["associationType"] = """type"""
        self.vs[13]["mm__"] = """directLink_S"""
        self.vs[13]["GUID__"] = 2740785288640416199
        self.vs[14]["associationType"] = """contents"""
        self.vs[14]["mm__"] = """directLink_T"""
        self.vs[14]["GUID__"] = 8887888475567830665
        self.vs[15]["associationType"] = """type"""
        self.vs[15]["mm__"] = """directLink_T"""
        self.vs[15]["GUID__"] = 8865501178517114157
        self.vs[16]["mm__"] = """hasAttribute_S"""
        self.vs[16]["GUID__"] = 4943386613296614662
        self.vs[17]["mm__"] = """hasAttribute_S"""
        self.vs[17]["GUID__"] = 7884432203485200773
        self.vs[18]["name"] = """eq_"""
        self.vs[18]["mm__"] = """Equation"""
        self.vs[18]["GUID__"] = 2646245257200660299
        self.vs[19]["mm__"] = """leftExpr"""
        self.vs[19]["GUID__"] = 8372676580318961436
        self.vs[20]["mm__"] = """rightExpr"""
        self.vs[20]["GUID__"] = 7722083879294223646
        self.vs[21]["name"] = """main"""
        self.vs[21]["Type"] = """'String'"""
        self.vs[21]["mm__"] = """Constant"""
        self.vs[21]["GUID__"] = 7551183475916470015
        self.vs[22]["name"] = """eq_"""
        self.vs[22]["mm__"] = """Equation"""
        self.vs[22]["GUID__"] = 7922089918538315006
        self.vs[23]["mm__"] = """leftExpr"""
        self.vs[23]["GUID__"] = 8074234325826374649
        self.vs[24]["mm__"] = """rightExpr"""
        self.vs[24]["GUID__"] = 7542532943220852209
        self.vs[25]["mm__"] = """hasArgs"""
        self.vs[25]["GUID__"] = 3082331710651312252
        self.vs[26]["mm__"] = """hasArgs"""
        self.vs[26]["GUID__"] = 8764466711128013260
        self.vs[27]["name"] = """_blockexpr_main_2"""
        self.vs[27]["Type"] = """'String'"""
        self.vs[27]["mm__"] = """Constant"""
        self.vs[27]["GUID__"] = 2827988255175350662
        self.vs[28]["mm__"] = """match_contains"""
        self.vs[28]["GUID__"] = 6502837430521861845
        self.vs[29]["mm__"] = """match_contains"""
        self.vs[29]["GUID__"] = 4323821556879948200
        self.vs[30]["mm__"] = """match_contains"""
        self.vs[30]["GUID__"] = 792261856844381452
        self.vs[31]["mm__"] = """apply_contains"""
        self.vs[31]["GUID__"] = 6436345070906481880
        self.vs[32]["mm__"] = """apply_contains"""
        self.vs[32]["GUID__"] = 3978375429695654423
        self.vs[33]["mm__"] = """apply_contains"""
        self.vs[33]["GUID__"] = 7578624994160003440
        self.vs[34]["name"] = """name"""
        self.vs[34]["Type"] = """'String'"""
        self.vs[34]["mm__"] = """Attribute"""
        self.vs[34]["GUID__"] = 7178852940305267544
        self.vs[35]["name"] = """name"""
        self.vs[35]["Type"] = """'String'"""
        self.vs[35]["mm__"] = """Attribute"""
        self.vs[35]["GUID__"] = 8116304855730557950
        self.vs[36]["name"] = """name"""
        self.vs[36]["Type"] = """'String'"""
        self.vs[36]["mm__"] = """Attribute"""
        self.vs[36]["GUID__"] = 4094362835381756173

