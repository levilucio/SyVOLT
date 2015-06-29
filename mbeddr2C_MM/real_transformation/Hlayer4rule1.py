

from core.himesis import Himesis

class Hlayer4rule1(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model Hlayer4rule1.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer4rule1, self).__init__(name='Hlayer4rule1', num_nodes=37, edges=[])
        
        # Add the edges
        self.add_edges([[0, 13], [13, 12], [0, 14], [14, 3], [1, 22], [22, 15], [1, 23], [23, 4], [1, 24], [24, 5], [12, 6], [6, 3], [15, 16], [16, 4], [4, 17], [17, 5], [15, 7], [7, 12], [12, 18], [18, 25], [3, 19], [19, 26], [4, 8], [8, 27], [9, 10], [10, 27], [9, 11], [30, 35], [35, 26], [30, 36], [36, 21], [29, 33], [33, 20], [29, 34], [34, 30], [28, 31], [31, 25], [28, 32], [32, 29], [11, 28], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer4rule1"""
        self["GUID__"] = 5920366288987423658
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 4336051676658282911
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 4695588112174078696
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 7992725105339284129
        self.vs[3]["name"] = """layer4rule1class1"""
        self.vs[3]["classtype"] = """InstanceConfiguration"""
        self.vs[3]["mm__"] = """InstanceConfiguration"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 5740745213730375552
        self.vs[4]["name"] = """layer4rule1class3"""
        self.vs[4]["classtype"] = """Function"""
        self.vs[4]["mm__"] = """Function"""
        self.vs[4]["cardinality"] = """1"""
        self.vs[4]["GUID__"] = 3350817510146986996
        self.vs[5]["name"] = """layer4rule1class4"""
        self.vs[5]["classtype"] = """StatementList"""
        self.vs[5]["mm__"] = """StatementList"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = 9131140756834045755
        self.vs[6]["associationType"] = """contents"""
        self.vs[6]["mm__"] = """directLink_S"""
        self.vs[6]["GUID__"] = 5834887104134017094
        self.vs[7]["mm__"] = """backward_link"""
        self.vs[7]["type"] = """ruleDef"""
        self.vs[7]["GUID__"] = 5543551529600103591
        self.vs[8]["mm__"] = """hasAttribute_T"""
        self.vs[8]["GUID__"] = 9035083535058275960
        self.vs[9]["name"] = """eq_"""
        self.vs[9]["mm__"] = """Equation"""
        self.vs[9]["GUID__"] = 7423193481459288102
        self.vs[10]["mm__"] = """leftExpr"""
        self.vs[10]["GUID__"] = 5744476417522220270
        self.vs[11]["mm__"] = """rightExpr"""
        self.vs[11]["GUID__"] = 3286396193686569048
        self.vs[12]["name"] = """layer4rule1class0"""
        self.vs[12]["classtype"] = """ImplementationModule"""
        self.vs[12]["mm__"] = """ImplementationModule"""
        self.vs[12]["cardinality"] = """+"""
        self.vs[12]["GUID__"] = 5126755952554633874
        self.vs[13]["mm__"] = """match_contains"""
        self.vs[13]["GUID__"] = 6777408630209869529
        self.vs[14]["mm__"] = """match_contains"""
        self.vs[14]["GUID__"] = 6589981443939046716
        self.vs[15]["name"] = """layer4rule1class2"""
        self.vs[15]["classtype"] = """ImplementationModule"""
        self.vs[15]["mm__"] = """ImplementationModule"""
        self.vs[15]["cardinality"] = """1"""
        self.vs[15]["GUID__"] = 3877981410537469747
        self.vs[16]["associationType"] = """contents"""
        self.vs[16]["mm__"] = """directLink_T"""
        self.vs[16]["GUID__"] = 5226679011661257482
        self.vs[17]["associationType"] = """body"""
        self.vs[17]["mm__"] = """directLink_T"""
        self.vs[17]["GUID__"] = 5730971223956523003
        self.vs[18]["mm__"] = """hasAttribute_S"""
        self.vs[18]["GUID__"] = 1311688257737904232
        self.vs[19]["mm__"] = """hasAttribute_S"""
        self.vs[19]["GUID__"] = 4038111057720046921
        self.vs[20]["name"] = """_"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 8629475333498514111
        self.vs[21]["name"] = """__init"""
        self.vs[21]["Type"] = """'String'"""
        self.vs[21]["mm__"] = """Constant"""
        self.vs[21]["GUID__"] = 1804013888703578799
        self.vs[22]["mm__"] = """apply_contains"""
        self.vs[22]["GUID__"] = 8838033606256235566
        self.vs[23]["mm__"] = """apply_contains"""
        self.vs[23]["GUID__"] = 2510772793742264687
        self.vs[24]["mm__"] = """apply_contains"""
        self.vs[24]["GUID__"] = 6300700583749266933
        self.vs[25]["name"] = """name"""
        self.vs[25]["Type"] = """'String'"""
        self.vs[25]["mm__"] = """Attribute"""
        self.vs[25]["GUID__"] = 8902279911047034617
        self.vs[26]["name"] = """name"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Attribute"""
        self.vs[26]["GUID__"] = 189034073559282788
        self.vs[27]["name"] = """name"""
        self.vs[27]["Type"] = """'String'"""
        self.vs[27]["mm__"] = """Attribute"""
        self.vs[27]["GUID__"] = 4632419300021245581
        self.vs[28]["name"] = """Concatlayer4rule1class3attribute026"""
        self.vs[28]["Type"] = """'String'"""
        self.vs[28]["mm__"] = """Concat"""
        self.vs[28]["GUID__"] = 8404711310539778166
        self.vs[29]["name"] = """Concatlayer4rule1class3attribute029"""
        self.vs[29]["Type"] = """'String'"""
        self.vs[29]["mm__"] = """Concat"""
        self.vs[29]["GUID__"] = 2067749236883927348
        self.vs[30]["name"] = """Concatlayer4rule1class3attribute033"""
        self.vs[30]["Type"] = """'String'"""
        self.vs[30]["mm__"] = """Concat"""
        self.vs[30]["GUID__"] = 4251966098571370094
        self.vs[31]["mm__"] = """hasArgs"""
        self.vs[31]["GUID__"] = 3305413220923856862
        self.vs[32]["mm__"] = """hasArgs"""
        self.vs[32]["GUID__"] = 6364900060861960135
        self.vs[33]["mm__"] = """hasArgs"""
        self.vs[33]["GUID__"] = 708911012853768538
        self.vs[34]["mm__"] = """hasArgs"""
        self.vs[34]["GUID__"] = 9062037447361207880
        self.vs[35]["mm__"] = """hasArgs"""
        self.vs[35]["GUID__"] = 4232562314154434897
        self.vs[36]["mm__"] = """hasArgs"""
        self.vs[36]["GUID__"] = 7176043051972592032

