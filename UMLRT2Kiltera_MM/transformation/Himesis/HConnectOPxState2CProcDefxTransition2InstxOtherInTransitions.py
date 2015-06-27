

from core.himesis import Himesis

class HConnectOPxState2CProcDefxTransition2InstxOtherInTransitions(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HConnectOPxState2CProcDefxTransition2InstxOtherInTransitions.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HConnectOPxState2CProcDefxTransition2InstxOtherInTransitions, self).__init__(name='HConnectOPxState2CProcDefxTransition2InstxOtherInTransitions', num_nodes=58, edges=[])
        
        # Add the edges
        self.add_edges([[4, 16], [16, 8], [8, 17], [17, 3], [8, 18], [18, 0], [11, 19], [19, 2], [2, 20], [20, 10], [2, 21], [21, 7], [36, 28], [28, 53], [37, 29], [29, 9], [38, 30], [30, 56], [39, 31], [31, 57], [10, 22], [22, 50], [7, 23], [23, 51], [11, 24], [24, 52], [34, 0], [0, 12], [5, 1], [1, 40], [1, 41], [1, 42], [1, 43], [9, 25], [25, 54], [9, 26], [26, 48], [9, 27], [27, 55], [6, 32], [32, 4], [6, 33], [33, 8], [6, 34], [6, 35], [35, 3], [41, 2], [12, 48], [4, 13], [13, 49], [15, 4], [6, 5], [36, 44], [37, 45], [38, 46], [39, 47], [40, 11], [42, 10], [43, 7], [7, 14], [14, 8], [44, 49], [45, 50], [46, 51], [47, 52], [11, 15]])
        # Set the graph attributes
        self["mm__"] = ['UMLRT2Kiltera_MM']
        self["name"] = """ConnectOPxState2CProcDefxTransition2InstxOtherInTransitions"""
        self["GUID__"] = 684206038362290013
        
        # Set the node attributes
        self.vs[0]["name"] = """vertex1"""
        self.vs[0]["classtype"] = """Vertex"""
        self.vs[0]["mm__"] = """Vertex"""
        self.vs[0]["cardinality"] = """+"""
        self.vs[0]["GUID__"] = 8192465963097736199
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 7845104656945202257
        self.vs[2]["name"] = """conditionbranch1"""
        self.vs[2]["classtype"] = """ConditionBranch"""
        self.vs[2]["mm__"] = """ConditionBranch"""
        self.vs[2]["cardinality"] = """1"""
        self.vs[2]["GUID__"] = 5271149482900157912
        self.vs[3]["name"] = """in1_1"""
        self.vs[3]["classtype"] = """IN1"""
        self.vs[3]["mm__"] = """IN1"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 9141132560708240564
        self.vs[4]["name"] = """state1"""
        self.vs[4]["classtype"] = """State"""
        self.vs[4]["mm__"] = """State"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = 5342028430417281353
        self.vs[5]["mm__"] = """paired_with"""
        self.vs[5]["GUID__"] = 2385469667441229442
        self.vs[6]["mm__"] = """MatchModel"""
        self.vs[6]["GUID__"] = 7708162180103254773
        self.vs[7]["name"] = """inst1"""
        self.vs[7]["classtype"] = """Inst"""
        self.vs[7]["mm__"] = """Inst"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = 1500468659050905618
        self.vs[8]["name"] = """transition1"""
        self.vs[8]["classtype"] = """Transition"""
        self.vs[8]["mm__"] = """Transition"""
        self.vs[8]["cardinality"] = """+"""
        self.vs[8]["GUID__"] = 1220329955639186315
        self.vs[9]["name"] = """concat1"""
        self.vs[9]["mm__"] = """Concat"""
        self.vs[9]["Type"] = """'String'"""
        self.vs[9]["GUID__"] = 6736500014236267814
        self.vs[10]["name"] = """expr1"""
        self.vs[10]["classtype"] = """Expr"""
        self.vs[10]["mm__"] = """Expr"""
        self.vs[10]["cardinality"] = """1"""
        self.vs[10]["GUID__"] = 2291522944722898728
        self.vs[11]["name"] = """conditionset1"""
        self.vs[11]["classtype"] = """ConditionSet"""
        self.vs[11]["mm__"] = """ConditionSet"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 1161097291328717226
        self.vs[12]["mm__"] = """hasAttribute_S"""
        self.vs[12]["GUID__"] = 4593959176011447115
        self.vs[13]["mm__"] = """hasAttribute_S"""
        self.vs[13]["GUID__"] = 4609943968772630305
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["GUID__"] = 8261004042304997785
        self.vs[15]["type"] = """ruleDef"""
        self.vs[15]["mm__"] = """backward_link"""
        self.vs[15]["GUID__"] = 7667031326702663045
        self.vs[16]["associationType"] = """transitions"""
        self.vs[16]["mm__"] = """directLink_S"""
        self.vs[16]["GUID__"] = 3056682304062613291
        self.vs[17]["associationType"] = """type"""
        self.vs[17]["mm__"] = """directLink_S"""
        self.vs[17]["GUID__"] = 2000191123637766980
        self.vs[18]["associationType"] = """src"""
        self.vs[18]["mm__"] = """directLink_S"""
        self.vs[18]["GUID__"] = 524030759011605662
        self.vs[19]["associationType"] = """branches"""
        self.vs[19]["mm__"] = """directLink_T"""
        self.vs[19]["GUID__"] = 2543116700183264105
        self.vs[20]["associationType"] = """if"""
        self.vs[20]["mm__"] = """directLink_T"""
        self.vs[20]["GUID__"] = 6289349442714143090
        self.vs[21]["associationType"] = """then"""
        self.vs[21]["mm__"] = """directLink_T"""
        self.vs[21]["GUID__"] = 407967512920506826
        self.vs[22]["mm__"] = """hasAttribute_T"""
        self.vs[22]["GUID__"] = 6084841465470505644
        self.vs[23]["mm__"] = """hasAttribute_T"""
        self.vs[23]["GUID__"] = 4602097186588058885
        self.vs[24]["mm__"] = """hasAttribute_T"""
        self.vs[24]["GUID__"] = 3337360490704735515
        self.vs[25]["mm__"] = """hasArgs"""
        self.vs[25]["GUID__"] = 8908195639179287062
        self.vs[26]["mm__"] = """hasArgs"""
        self.vs[26]["GUID__"] = 7428725400856253097
        self.vs[27]["mm__"] = """hasArgs"""
        self.vs[27]["GUID__"] = 2124879866551356947
        self.vs[28]["mm__"] = """rightExpr"""
        self.vs[28]["GUID__"] = 5930011774245234163
        self.vs[29]["mm__"] = """rightExpr"""
        self.vs[29]["GUID__"] = 5883281680554603433
        self.vs[30]["mm__"] = """rightExpr"""
        self.vs[30]["GUID__"] = 3460043433065947280
        self.vs[31]["mm__"] = """rightExpr"""
        self.vs[31]["GUID__"] = 8094238935890657323
        self.vs[32]["mm__"] = """match_contains"""
        self.vs[32]["GUID__"] = 6419529872873213758
        self.vs[33]["mm__"] = """match_contains"""
        self.vs[33]["GUID__"] = 1464782190379599630
        self.vs[34]["mm__"] = """match_contains"""
        self.vs[34]["GUID__"] = 6175795950750980713
        self.vs[35]["mm__"] = """match_contains"""
        self.vs[35]["GUID__"] = 5794399915948497569
        self.vs[36]["name"] = """eq1"""
        self.vs[36]["mm__"] = """Equation"""
        self.vs[36]["GUID__"] = 4240227647471241216
        self.vs[37]["name"] = """eq2"""
        self.vs[37]["mm__"] = """Equation"""
        self.vs[37]["GUID__"] = 623307138179533170
        self.vs[38]["name"] = """eq3"""
        self.vs[38]["mm__"] = """Equation"""
        self.vs[38]["GUID__"] = 7292611911510167098
        self.vs[39]["name"] = """eq4"""
        self.vs[39]["mm__"] = """Equation"""
        self.vs[39]["GUID__"] = 5852777871823252820
        self.vs[40]["mm__"] = """apply_contains"""
        self.vs[40]["GUID__"] = 1225915555605627800
        self.vs[41]["mm__"] = """apply_contains"""
        self.vs[41]["GUID__"] = 4103702996046381034
        self.vs[42]["mm__"] = """apply_contains"""
        self.vs[42]["GUID__"] = 5885415524902318738
        self.vs[43]["mm__"] = """apply_contains"""
        self.vs[43]["GUID__"] = 886075053227385595
        self.vs[44]["mm__"] = """leftExpr"""
        self.vs[44]["GUID__"] = 8543554512049401942
        self.vs[45]["mm__"] = """leftExpr"""
        self.vs[45]["GUID__"] = 6042475767550967388
        self.vs[46]["mm__"] = """leftExpr"""
        self.vs[46]["GUID__"] = 8611378992316746779
        self.vs[47]["mm__"] = """leftExpr"""
        self.vs[47]["GUID__"] = 8916980241579133254
        self.vs[48]["name"] = """name"""
        self.vs[48]["mm__"] = """Attribute"""
        self.vs[48]["Type"] = """'String'"""
        self.vs[48]["GUID__"] = 6227287310992906663
        self.vs[49]["name"] = """isComposite"""
        self.vs[49]["mm__"] = """Attribute"""
        self.vs[49]["Type"] = """'Bool'"""
        self.vs[49]["GUID__"] = 4688101724487997691
        self.vs[50]["name"] = """literal"""
        self.vs[50]["mm__"] = """Attribute"""
        self.vs[50]["Type"] = """'String'"""
        self.vs[50]["GUID__"] = 3756109162140509927
        self.vs[51]["name"] = """pivot"""
        self.vs[51]["mm__"] = """Attribute"""
        self.vs[51]["Type"] = """'String'"""
        self.vs[51]["GUID__"] = 1247930355168861155
        self.vs[52]["name"] = """pivot"""
        self.vs[52]["mm__"] = """Attribute"""
        self.vs[52]["Type"] = """'String'"""
        self.vs[52]["GUID__"] = 7449842356818439754
        self.vs[53]["name"] = """true"""
        self.vs[53]["mm__"] = """Constant"""
        self.vs[53]["Type"] = """'Bool'"""
        self.vs[53]["GUID__"] = 7297249909650550095
        self.vs[54]["name"] = """enp=xox"""
        self.vs[54]["mm__"] = """Constant"""
        self.vs[54]["Type"] = """'String'"""
        self.vs[54]["GUID__"] = 4939643517844376102
        self.vs[55]["name"] = """xox"""
        self.vs[55]["mm__"] = """Constant"""
        self.vs[55]["Type"] = """'String'"""
        self.vs[55]["GUID__"] = 4076802218673584801
        self.vs[56]["name"] = """instForInTrans"""
        self.vs[56]["mm__"] = """Constant"""
        self.vs[56]["Type"] = """'String'"""
        self.vs[56]["GUID__"] = 4584593899122311530
        self.vs[57]["name"] = """condsetcompstate"""
        self.vs[57]["mm__"] = """Constant"""
        self.vs[57]["Type"] = """'String'"""
        self.vs[57]["GUID__"] = 3258277028074118848

