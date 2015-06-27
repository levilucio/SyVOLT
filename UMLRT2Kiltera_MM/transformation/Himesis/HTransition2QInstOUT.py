

from core.himesis import Himesis

class HTransition2QInstOUT(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HTransition2QInstOUT.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HTransition2QInstOUT, self).__init__(name='HTransition2QInstOUT', num_nodes=43, edges=[])
        
        # Add the edges
        self.add_edges([[9, 31], [31, 3], [9, 32], [32, 7], [7, 33], [33, 1], [9, 34], [34, 1], [8, 0], [0, 11], [22, 16], [16, 28], [23, 17], [17, 10], [24, 18], [18, 30], [11, 19], [19, 40], [8, 20], [20, 41], [8, 21], [21, 42], [38, 1], [1, 4], [5, 2], [2, 14], [2, 15], [10, 12], [12, 29], [10, 13], [13, 39], [6, 35], [35, 9], [6, 36], [36, 3], [6, 37], [37, 7], [6, 38], [4, 39], [6, 5], [22, 25], [23, 26], [24, 27], [14, 8], [15, 11], [25, 40], [26, 41], [27, 42]])
        # Set the graph attributes
        self["mm__"] = ['UMLRT2Kiltera_MM']
        self["name"] = """Transition2QInstOUT"""
        self["GUID__"] = 3749454627843449828
        
        # Set the node attributes
        self.vs[0]["associationType"] = """channelNames"""
        self.vs[0]["mm__"] = """directLink_T"""
        self.vs[0]["GUID__"] = 4133835868356222525
        self.vs[1]["name"] = """vertex1"""
        self.vs[1]["classtype"] = """Vertex"""
        self.vs[1]["mm__"] = """Vertex"""
        self.vs[1]["cardinality"] = """1"""
        self.vs[1]["GUID__"] = 830690598894214856
        self.vs[2]["mm__"] = """ApplyModel"""
        self.vs[2]["GUID__"] = 6555769018826237090
        self.vs[3]["name"] = """out2_1"""
        self.vs[3]["classtype"] = """OUT2"""
        self.vs[3]["mm__"] = """OUT2"""
        self.vs[3]["cardinality"] = """1"""
        self.vs[3]["GUID__"] = 987760982904136054
        self.vs[4]["mm__"] = """hasAttribute_S"""
        self.vs[4]["GUID__"] = 2669663642903523892
        self.vs[5]["mm__"] = """paired_with"""
        self.vs[5]["GUID__"] = 1675225061788622920
        self.vs[6]["mm__"] = """MatchModel"""
        self.vs[6]["GUID__"] = 3288714805506904284
        self.vs[7]["name"] = """statemachine1"""
        self.vs[7]["classtype"] = """StateMachine"""
        self.vs[7]["mm__"] = """StateMachine"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = 5091871555499115026
        self.vs[8]["name"] = """inst1"""
        self.vs[8]["classtype"] = """Inst"""
        self.vs[8]["mm__"] = """Inst"""
        self.vs[8]["cardinality"] = """1"""
        self.vs[8]["GUID__"] = 9156818687504006931
        self.vs[9]["name"] = """transition1"""
        self.vs[9]["classtype"] = """Transition"""
        self.vs[9]["mm__"] = """Transition"""
        self.vs[9]["cardinality"] = """+"""
        self.vs[9]["GUID__"] = 1082381076586641419
        self.vs[10]["name"] = """concat1"""
        self.vs[10]["mm__"] = """Concat"""
        self.vs[10]["Type"] = """'String'"""
        self.vs[10]["GUID__"] = 4026289071505715868
        self.vs[11]["name"] = """name1"""
        self.vs[11]["classtype"] = """Name"""
        self.vs[11]["mm__"] = """Name"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 2463415442832202971
        self.vs[12]["mm__"] = """hasArgs"""
        self.vs[12]["GUID__"] = 637997370850694023
        self.vs[13]["mm__"] = """hasArgs"""
        self.vs[13]["GUID__"] = 5943383644573326687
        self.vs[14]["mm__"] = """apply_contains"""
        self.vs[14]["GUID__"] = 6910186076723569668
        self.vs[15]["mm__"] = """apply_contains"""
        self.vs[15]["GUID__"] = 8191938240831239551
        self.vs[16]["mm__"] = """rightExpr"""
        self.vs[16]["GUID__"] = 8846518324520933562
        self.vs[17]["mm__"] = """rightExpr"""
        self.vs[17]["GUID__"] = 5975028753297810630
        self.vs[18]["mm__"] = """rightExpr"""
        self.vs[18]["GUID__"] = 6382299690944420526
        self.vs[19]["mm__"] = """hasAttribute_T"""
        self.vs[19]["GUID__"] = 2584098881073268375
        self.vs[20]["mm__"] = """hasAttribute_T"""
        self.vs[20]["GUID__"] = 3333163046885052286
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 1979864792606213438
        self.vs[22]["name"] = """eq2"""
        self.vs[22]["mm__"] = """Equation"""
        self.vs[22]["GUID__"] = 5054138952058187962
        self.vs[23]["name"] = """eq1"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = 1935623989523151589
        self.vs[24]["name"] = """eq3"""
        self.vs[24]["mm__"] = """Equation"""
        self.vs[24]["GUID__"] = 1793469059695857575
        self.vs[25]["mm__"] = """leftExpr"""
        self.vs[25]["GUID__"] = 1620924959513554532
        self.vs[26]["mm__"] = """leftExpr"""
        self.vs[26]["GUID__"] = 6414125878914994152
        self.vs[27]["mm__"] = """leftExpr"""
        self.vs[27]["GUID__"] = 94247992263620825
        self.vs[28]["name"] = """sh"""
        self.vs[28]["mm__"] = """Constant"""
        self.vs[28]["Type"] = """'String'"""
        self.vs[28]["GUID__"] = 6451835475649650377
        self.vs[29]["name"] = """B"""
        self.vs[29]["mm__"] = """Constant"""
        self.vs[29]["Type"] = """'String'"""
        self.vs[29]["GUID__"] = 2355334794228562686
        self.vs[30]["name"] = """instfortrans"""
        self.vs[30]["mm__"] = """Constant"""
        self.vs[30]["Type"] = """'String'"""
        self.vs[30]["GUID__"] = 8783203315367753823
        self.vs[31]["associationType"] = """type"""
        self.vs[31]["mm__"] = """directLink_S"""
        self.vs[31]["GUID__"] = 9130366634729388240
        self.vs[32]["associationType"] = """owningStateMachine"""
        self.vs[32]["mm__"] = """directLink_S"""
        self.vs[32]["GUID__"] = 8223440483315357673
        self.vs[33]["associationType"] = """exitPoints"""
        self.vs[33]["mm__"] = """directLink_S"""
        self.vs[33]["GUID__"] = 1555482224658854797
        self.vs[34]["associationType"] = """dest"""
        self.vs[34]["mm__"] = """directLink_S"""
        self.vs[34]["GUID__"] = 8804329862795873404
        self.vs[35]["mm__"] = """match_contains"""
        self.vs[35]["GUID__"] = 1409506646482166519
        self.vs[36]["mm__"] = """match_contains"""
        self.vs[36]["GUID__"] = 3881833158668810368
        self.vs[37]["mm__"] = """match_contains"""
        self.vs[37]["GUID__"] = 4739826574898541131
        self.vs[38]["mm__"] = """match_contains"""
        self.vs[38]["GUID__"] = 106684994450277845
        self.vs[39]["name"] = """name"""
        self.vs[39]["mm__"] = """Attribute"""
        self.vs[39]["Type"] = """'String'"""
        self.vs[39]["GUID__"] = 5420233937432395400
        self.vs[40]["name"] = """literal"""
        self.vs[40]["mm__"] = """Attribute"""
        self.vs[40]["Type"] = """'String'"""
        self.vs[40]["GUID__"] = 2859783921393937162
        self.vs[41]["name"] = """name"""
        self.vs[41]["mm__"] = """Attribute"""
        self.vs[41]["Type"] = """'String'"""
        self.vs[41]["GUID__"] = 7524533378077350307
        self.vs[42]["name"] = """pivot"""
        self.vs[42]["mm__"] = """Attribute"""
        self.vs[42]["Type"] = """'String'"""
        self.vs[42]["GUID__"] = 6264105839322857955

