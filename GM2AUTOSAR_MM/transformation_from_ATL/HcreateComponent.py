

from core.himesis import Himesis

class HcreateComponent(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HcreateComponent.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HcreateComponent, self).__init__(name='HcreateComponent', num_nodes=35, edges=[])
        
        # Add the edges
        self.add_edges([[0, 16], [16, 3], [0, 17], [17, 4], [0, 18], [18, 5], [1, 10], [10, 6], [1, 11], [11, 7], [5, 12], [12, 4], [4, 13], [13, 3], [6, 8], [8, 7], [3, 9], [9, 31], [6, 19], [19, 32], [20, 21], [21, 32], [20, 22], [22, 14], [7, 23], [23, 33], [24, 25], [25, 33], [24, 26], [26, 31], [7, 27], [27, 34], [28, 29], [29, 34], [28, 30], [30, 15], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """createComponent"""
        self["GUID__"] = 4243952523379343679
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 6962525036682502439
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 3933271577476665341
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 3728460300626366433
        self.vs[3]["name"] = """"""
        self.vs[3]["classtype"] = """Module"""
        self.vs[3]["mm__"] = """Module"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 4600202935122677930
        self.vs[4]["name"] = """"""
        self.vs[4]["classtype"] = """Partition"""
        self.vs[4]["mm__"] = """Partition"""
        self.vs[4]["cardinality"] = """1"""
        self.vs[4]["GUID__"] = 4319262607733233065
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """PhysicalNode"""
        self.vs[5]["mm__"] = """PhysicalNode"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = 4348338880372414989
        self.vs[6]["name"] = """"""
        self.vs[6]["classtype"] = """SwCompToEcuMapping_component"""
        self.vs[6]["mm__"] = """SwCompToEcuMapping_component"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = 3235665656551213034
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """ComponentPrototype"""
        self.vs[7]["mm__"] = """ComponentPrototype"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = 7480676712255865617
        self.vs[8]["associationType"] = """componentPrototype"""
        self.vs[8]["mm__"] = """directLink_T"""
        self.vs[8]["GUID__"] = 233602438806654331
        self.vs[9]["mm__"] = """hasAttribute_S"""
        self.vs[9]["GUID__"] = 6835259583643173475
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 1150240012314136049
        self.vs[11]["mm__"] = """apply_contains"""
        self.vs[11]["GUID__"] = 8152349909688846137
        self.vs[12]["associationType"] = """partition"""
        self.vs[12]["mm__"] = """directLink_S"""
        self.vs[12]["GUID__"] = 4858592861157296738
        self.vs[13]["associationType"] = """module"""
        self.vs[13]["mm__"] = """directLink_S"""
        self.vs[13]["GUID__"] = 7534407875454612819
        self.vs[14]["name"] = """solveRef"""
        self.vs[14]["mm__"] = """Constant"""
        self.vs[14]["Type"] = """'String'"""
        self.vs[14]["GUID__"] = 3136476772695466157
        self.vs[15]["name"] = """solveRef"""
        self.vs[15]["mm__"] = """Constant"""
        self.vs[15]["Type"] = """'String'"""
        self.vs[15]["GUID__"] = 4734172355844618871
        self.vs[16]["mm__"] = """match_contains"""
        self.vs[16]["GUID__"] = 4605065421388908618
        self.vs[17]["mm__"] = """match_contains"""
        self.vs[17]["GUID__"] = 6006152695192667245
        self.vs[18]["mm__"] = """match_contains"""
        self.vs[18]["GUID__"] = 4226250298918616718
        self.vs[19]["mm__"] = """hasAttribute_T"""
        self.vs[19]["GUID__"] = 6658566897349226150
        self.vs[20]["name"] = """eq_"""
        self.vs[20]["mm__"] = """Equation"""
        self.vs[20]["GUID__"] = 1154571052428397939
        self.vs[21]["mm__"] = """leftExpr"""
        self.vs[21]["GUID__"] = 6409441821474248500
        self.vs[22]["mm__"] = """rightExpr"""
        self.vs[22]["GUID__"] = 3346152518563565779
        self.vs[23]["mm__"] = """hasAttribute_T"""
        self.vs[23]["GUID__"] = 2866844295505414680
        self.vs[24]["name"] = """eq_"""
        self.vs[24]["mm__"] = """Equation"""
        self.vs[24]["GUID__"] = 899557349751785795
        self.vs[25]["mm__"] = """leftExpr"""
        self.vs[25]["GUID__"] = 8983132429455642183
        self.vs[26]["mm__"] = """rightExpr"""
        self.vs[26]["GUID__"] = 906768180854356102
        self.vs[27]["mm__"] = """hasAttribute_T"""
        self.vs[27]["GUID__"] = 5578292599887505632
        self.vs[28]["name"] = """eq_"""
        self.vs[28]["mm__"] = """Equation"""
        self.vs[28]["GUID__"] = 1234059906603622847
        self.vs[29]["mm__"] = """leftExpr"""
        self.vs[29]["GUID__"] = 5639152254852000968
        self.vs[30]["mm__"] = """rightExpr"""
        self.vs[30]["GUID__"] = 6692579334642407607
        self.vs[31]["name"] = """name"""
        self.vs[31]["mm__"] = """Attribute"""
        self.vs[31]["Type"] = """'String'"""
        self.vs[31]["GUID__"] = 1041810393865281027
        self.vs[32]["name"] = """ApplyAttribute"""
        self.vs[32]["mm__"] = """Attribute"""
        self.vs[32]["Type"] = """'String'"""
        self.vs[32]["GUID__"] = 7382319104183536599
        self.vs[33]["name"] = """shortName"""
        self.vs[33]["mm__"] = """Attribute"""
        self.vs[33]["Type"] = """'String'"""
        self.vs[33]["GUID__"] = 461432551221245089
        self.vs[34]["name"] = """ApplyAttribute"""
        self.vs[34]["mm__"] = """Attribute"""
        self.vs[34]["Type"] = """'String'"""
        self.vs[34]["GUID__"] = 2658057431565614173

