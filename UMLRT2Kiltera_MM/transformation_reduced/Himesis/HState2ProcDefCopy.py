

from core.himesis import Himesis

class HState2ProcDefCopy(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HState2ProcDefCopy.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HState2ProcDefCopy, self).__init__(name='HState2ProcDefCopy', num_nodes=51, edges=[])
        
        # Add the edges
        self.add_edges([[6, 10], [10, 13], [6, 11], [11, 14], [6, 12], [12, 15], [30, 20], [20, 7], [31, 21], [21, 41], [32, 22], [22, 42], [33, 23], [23, 43], [34, 24], [24, 44], [6, 25], [25, 46], [13, 26], [26, 47], [14, 27], [27, 48], [15, 28], [28, 49], [6, 29], [29, 50], [4, 0], [0, 16], [0, 17], [0, 18], [0, 19], [7, 8], [8, 40], [7, 9], [9, 45], [5, 1], [1, 3], [3, 2], [2, 45], [5, 4], [30, 35], [31, 36], [32, 37], [33, 38], [34, 39], [16, 6], [17, 13], [18, 14], [19, 15], [35, 46], [36, 47], [37, 48], [38, 49], [39, 50]])
        # Set the graph attributes
        self["mm__"] = ['UMLRT2Kiltera_MM']
        self["name"] = """State2ProcDefCopy"""
        self["GUID__"] = 7152217143627811207
        
        # Set the node attributes
        self.vs[0]["mm__"] = """ApplyModel"""
        self.vs[0]["GUID__"] = 7627914396263650972
        self.vs[1]["mm__"] = """match_contains"""
        self.vs[1]["GUID__"] = 3939256222827564792
        self.vs[2]["mm__"] = """hasAttribute_S"""
        self.vs[2]["GUID__"] = 8533552382447949488
        self.vs[3]["name"] = """state1"""
        self.vs[3]["classtype"] = """State"""
        self.vs[3]["mm__"] = """State"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 995873152185397992
        self.vs[4]["mm__"] = """paired_with"""
        self.vs[4]["GUID__"] = 6494761049920864998
        self.vs[5]["mm__"] = """MatchModel"""
        self.vs[5]["GUID__"] = 4709983440512710925
        self.vs[6]["name"] = """procdef1"""
        self.vs[6]["classtype"] = """ProcDef"""
        self.vs[6]["mm__"] = """ProcDef"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = 4216615354843785191
        self.vs[7]["name"] = """concat1"""
        self.vs[7]["mm__"] = """Concat"""
        self.vs[7]["Type"] = """'String'"""
        self.vs[7]["GUID__"] = 1875263340744121208
        self.vs[8]["mm__"] = """hasArgs"""
        self.vs[8]["GUID__"] = 5034187439585834925
        self.vs[9]["mm__"] = """hasArgs"""
        self.vs[9]["GUID__"] = 5889062703002579863
        self.vs[10]["associationType"] = """channelNames"""
        self.vs[10]["mm__"] = """directLink_T"""
        self.vs[10]["GUID__"] = 2813387721368637776
        self.vs[11]["associationType"] = """channelNames"""
        self.vs[11]["mm__"] = """directLink_T"""
        self.vs[11]["GUID__"] = 253076960970561187
        self.vs[12]["associationType"] = """channelNames"""
        self.vs[12]["mm__"] = """directLink_T"""
        self.vs[12]["GUID__"] = 5019004895174290524
        self.vs[13]["name"] = """name1"""
        self.vs[13]["classtype"] = """Name"""
        self.vs[13]["mm__"] = """Name"""
        self.vs[13]["cardinality"] = """1"""
        self.vs[13]["GUID__"] = 1905686815802071908
        self.vs[14]["name"] = """name2"""
        self.vs[14]["classtype"] = """Name"""
        self.vs[14]["mm__"] = """Name"""
        self.vs[14]["cardinality"] = """1"""
        self.vs[14]["GUID__"] = 4935384543084388657
        self.vs[15]["name"] = """name3"""
        self.vs[15]["classtype"] = """Name"""
        self.vs[15]["mm__"] = """Name"""
        self.vs[15]["cardinality"] = """1"""
        self.vs[15]["GUID__"] = 2356643122903429573
        self.vs[16]["mm__"] = """apply_contains"""
        self.vs[16]["GUID__"] = 6020021328889196163
        self.vs[17]["mm__"] = """apply_contains"""
        self.vs[17]["GUID__"] = 2561661900522343632
        self.vs[18]["mm__"] = """apply_contains"""
        self.vs[18]["GUID__"] = 320146283344815915
        self.vs[19]["mm__"] = """apply_contains"""
        self.vs[19]["GUID__"] = 3388229757364993968
        self.vs[20]["mm__"] = """rightExpr"""
        self.vs[20]["GUID__"] = 3232530344857811827
        self.vs[21]["mm__"] = """rightExpr"""
        self.vs[21]["GUID__"] = 3633132881936682590
        self.vs[22]["mm__"] = """rightExpr"""
        self.vs[22]["GUID__"] = 8027330054768687009
        self.vs[23]["mm__"] = """rightExpr"""
        self.vs[23]["GUID__"] = 1291444534305192128
        self.vs[24]["mm__"] = """rightExpr"""
        self.vs[24]["GUID__"] = 7512896241622486050
        self.vs[25]["mm__"] = """hasAttribute_T"""
        self.vs[25]["GUID__"] = 2759300586942288682
        self.vs[26]["mm__"] = """hasAttribute_T"""
        self.vs[26]["GUID__"] = 6122457399449601078
        self.vs[27]["mm__"] = """hasAttribute_T"""
        self.vs[27]["GUID__"] = 2175284954839151113
        self.vs[28]["mm__"] = """hasAttribute_T"""
        self.vs[28]["GUID__"] = 6050638256706814248
        self.vs[29]["mm__"] = """hasAttribute_T"""
        self.vs[29]["GUID__"] = 5782565258669433404
        self.vs[30]["name"] = """eq1"""
        self.vs[30]["mm__"] = """Equation"""
        self.vs[30]["GUID__"] = 545004928613451973
        self.vs[31]["name"] = """eq2"""
        self.vs[31]["mm__"] = """Equation"""
        self.vs[31]["GUID__"] = 1101504434123582880
        self.vs[32]["name"] = """eq3"""
        self.vs[32]["mm__"] = """Equation"""
        self.vs[32]["GUID__"] = 2750078426749789093
        self.vs[33]["name"] = """eq4"""
        self.vs[33]["mm__"] = """Equation"""
        self.vs[33]["GUID__"] = 2688897664351002476
        self.vs[34]["name"] = """eq5"""
        self.vs[34]["mm__"] = """Equation"""
        self.vs[34]["GUID__"] = 7592732239401312233
        self.vs[35]["mm__"] = """leftExpr"""
        self.vs[35]["GUID__"] = 7192095847603916933
        self.vs[36]["mm__"] = """leftExpr"""
        self.vs[36]["GUID__"] = 2425339070984489349
        self.vs[37]["mm__"] = """leftExpr"""
        self.vs[37]["GUID__"] = 6881640054858651243
        self.vs[38]["mm__"] = """leftExpr"""
        self.vs[38]["GUID__"] = 265252833601019169
        self.vs[39]["mm__"] = """leftExpr"""
        self.vs[39]["GUID__"] = 4966349216589712856
        self.vs[40]["name"] = """S"""
        self.vs[40]["mm__"] = """Constant"""
        self.vs[40]["Type"] = """'String'"""
        self.vs[40]["GUID__"] = 6800389233499419872
        self.vs[41]["name"] = """enp"""
        self.vs[41]["mm__"] = """Constant"""
        self.vs[41]["Type"] = """'String'"""
        self.vs[41]["GUID__"] = 8837062126349173778
        self.vs[42]["name"] = """exit"""
        self.vs[42]["mm__"] = """Constant"""
        self.vs[42]["Type"] = """'String'"""
        self.vs[42]["GUID__"] = 3877697074430810766
        self.vs[43]["name"] = """exack"""
        self.vs[43]["mm__"] = """Constant"""
        self.vs[43]["Type"] = """'String'"""
        self.vs[43]["GUID__"] = 4083706923790208441
        self.vs[44]["name"] = """procdef"""
        self.vs[44]["mm__"] = """Constant"""
        self.vs[44]["Type"] = """'String'"""
        self.vs[44]["GUID__"] = 317866173660978366
        self.vs[45]["name"] = """name"""
        self.vs[45]["mm__"] = """Attribute"""
        self.vs[45]["Type"] = """'String'"""
        self.vs[45]["GUID__"] = 6573975616125460087
        self.vs[46]["name"] = """name"""
        self.vs[46]["mm__"] = """Attribute"""
        self.vs[46]["Type"] = """'String'"""
        self.vs[46]["GUID__"] = 8344939398038000732
        self.vs[47]["name"] = """literal"""
        self.vs[47]["mm__"] = """Attribute"""
        self.vs[47]["Type"] = """'String'"""
        self.vs[47]["GUID__"] = 8599079658211604296
        self.vs[48]["name"] = """literal"""
        self.vs[48]["mm__"] = """Attribute"""
        self.vs[48]["Type"] = """'String'"""
        self.vs[48]["GUID__"] = 6251861593471483775
        self.vs[49]["name"] = """literal"""
        self.vs[49]["mm__"] = """Attribute"""
        self.vs[49]["Type"] = """'String'"""
        self.vs[49]["GUID__"] = 3903386387351432024
        self.vs[50]["name"] = """pivot"""
        self.vs[50]["mm__"] = """Attribute"""
        self.vs[50]["Type"] = """'String'"""
        self.vs[50]["GUID__"] = 4079318190525166440

