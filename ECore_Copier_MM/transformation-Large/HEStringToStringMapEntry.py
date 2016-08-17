

from core.himesis import Himesis

class HEStringToStringMapEntry(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HEStringToStringMapEntry.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HEStringToStringMapEntry, self).__init__(name='HEStringToStringMapEntry', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 3], [3, 6], [1, 4], [4, 7], [6, 8], [8, 22], [6, 9], [9, 23], [7, 10], [10, 24], [11, 12], [12, 24], [11, 13], [13, 22], [7, 14], [14, 25], [15, 16], [16, 25], [15, 17], [17, 23], [7, 18], [18, 26], [19, 20], [20, 26], [19, 21], [21, 5], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """EStringToStringMapEntry"""
        self["GUID__"] = 4634089967782331205
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 5767157123396954401
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 1802761838065258744
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 6185029176263327416
        self.vs[3]["mm__"] = """match_contains"""
        self.vs[3]["GUID__"] = 4920426410336854132
        self.vs[4]["mm__"] = """apply_contains"""
        self.vs[4]["GUID__"] = 9083745405555017509
        self.vs[5]["name"] = """solveRef"""
        self.vs[5]["mm__"] = """Constant"""
        self.vs[5]["Type"] = """'String'"""
        self.vs[5]["GUID__"] = 4417166335431353573
        self.vs[6]["name"] = """"""
        self.vs[6]["classtype"] = """EStringToStringMapEntry"""
        self.vs[6]["mm__"] = """EStringToStringMapEntry"""
        self.vs[6]["cardinality"] = """+"""
        self.vs[6]["GUID__"] = 4999628130002502929
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EStringToStringMapEntry"""
        self.vs[7]["mm__"] = """EStringToStringMapEntry"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = 5254374701123540708
        self.vs[8]["mm__"] = """hasAttribute_S"""
        self.vs[8]["GUID__"] = 98842191179507338
        self.vs[9]["mm__"] = """hasAttribute_S"""
        self.vs[9]["GUID__"] = 5727233244301733140
        self.vs[10]["mm__"] = """hasAttribute_T"""
        self.vs[10]["GUID__"] = 6058405372165000821
        self.vs[11]["name"] = """eq_"""
        self.vs[11]["mm__"] = """Equation"""
        self.vs[11]["GUID__"] = 2327648978409782716
        self.vs[12]["mm__"] = """leftExpr"""
        self.vs[12]["GUID__"] = 5395634497217842894
        self.vs[13]["mm__"] = """rightExpr"""
        self.vs[13]["GUID__"] = 397470113978665543
        self.vs[14]["mm__"] = """hasAttribute_T"""
        self.vs[14]["GUID__"] = 7498012780225567940
        self.vs[15]["name"] = """eq_"""
        self.vs[15]["mm__"] = """Equation"""
        self.vs[15]["GUID__"] = 5047015039538755382
        self.vs[16]["mm__"] = """leftExpr"""
        self.vs[16]["GUID__"] = 2447444071987196435
        self.vs[17]["mm__"] = """rightExpr"""
        self.vs[17]["GUID__"] = 4289097346207092349
        self.vs[18]["mm__"] = """hasAttribute_T"""
        self.vs[18]["GUID__"] = 8819798654255359161
        self.vs[19]["name"] = """eq_"""
        self.vs[19]["mm__"] = """Equation"""
        self.vs[19]["GUID__"] = 4504601851070629572
        self.vs[20]["mm__"] = """leftExpr"""
        self.vs[20]["GUID__"] = 1535342940883651354
        self.vs[21]["mm__"] = """rightExpr"""
        self.vs[21]["GUID__"] = 4460677478398366807
        self.vs[22]["name"] = """key"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["GUID__"] = 4992564708258750591
        self.vs[23]["name"] = """value"""
        self.vs[23]["mm__"] = """Attribute"""
        self.vs[23]["Type"] = """'String'"""
        self.vs[23]["GUID__"] = 3818887609102027894
        self.vs[24]["name"] = """key"""
        self.vs[24]["mm__"] = """Attribute"""
        self.vs[24]["Type"] = """'String'"""
        self.vs[24]["GUID__"] = 6780738832525991035
        self.vs[25]["name"] = """value"""
        self.vs[25]["mm__"] = """Attribute"""
        self.vs[25]["Type"] = """'String'"""
        self.vs[25]["GUID__"] = 6516981068807042253
        self.vs[26]["name"] = """ApplyAttribute"""
        self.vs[26]["mm__"] = """Attribute"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["GUID__"] = 6768649389232869619

