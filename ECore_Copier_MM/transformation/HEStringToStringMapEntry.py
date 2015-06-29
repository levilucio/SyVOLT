

from core.himesis import Himesis

class HEStringToStringMapEntry(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HEStringToStringMapEntry.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HEStringToStringMapEntry, self).__init__(name='HEStringToStringMapEntry', num_nodes=21, edges=[])
        
        # Add the edges
        self.add_edges([[0, 3], [3, 5], [1, 4], [4, 6], [5, 7], [7, 17], [5, 8], [8, 18], [6, 9], [9, 19], [10, 11], [11, 19], [10, 12], [12, 17], [6, 13], [13, 20], [14, 15], [15, 20], [14, 16], [16, 18], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """EStringToStringMapEntry"""
        self["GUID__"] = 4634089967782331205
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 6339318944647469944
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 4923292584619328737
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 7417612584931150444
        self.vs[3]["mm__"] = """match_contains"""
        self.vs[3]["GUID__"] = 3448783001864234295
        self.vs[4]["mm__"] = """apply_contains"""
        self.vs[4]["GUID__"] = 8549108673803888330
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EStringToStringMapEntry"""
        self.vs[5]["mm__"] = """EStringToStringMapEntry"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 2655678174158550480
        self.vs[6]["name"] = """"""
        self.vs[6]["classtype"] = """EStringToStringMapEntry"""
        self.vs[6]["mm__"] = """EStringToStringMapEntry"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = 1064437281631316772
        self.vs[7]["mm__"] = """hasAttribute_S"""
        self.vs[7]["GUID__"] = 5181984345033982054
        self.vs[8]["mm__"] = """hasAttribute_S"""
        self.vs[8]["GUID__"] = 4390040158622719677
        self.vs[9]["mm__"] = """hasAttribute_T"""
        self.vs[9]["GUID__"] = 6896501783062636090
        self.vs[10]["name"] = """eq_"""
        self.vs[10]["mm__"] = """Equation"""
        self.vs[10]["GUID__"] = 2827551811756164503
        self.vs[11]["mm__"] = """leftExpr"""
        self.vs[11]["GUID__"] = 3627268082316215542
        self.vs[12]["mm__"] = """rightExpr"""
        self.vs[12]["GUID__"] = 7550675147995820437
        self.vs[13]["mm__"] = """hasAttribute_T"""
        self.vs[13]["GUID__"] = 2081611678774101290
        self.vs[14]["name"] = """eq_"""
        self.vs[14]["mm__"] = """Equation"""
        self.vs[14]["GUID__"] = 4256472892217557723
        self.vs[15]["mm__"] = """leftExpr"""
        self.vs[15]["GUID__"] = 8925728432772003667
        self.vs[16]["mm__"] = """rightExpr"""
        self.vs[16]["GUID__"] = 8673724033137838881
        self.vs[17]["name"] = """key"""
        self.vs[17]["mm__"] = """Attribute"""
        self.vs[17]["Type"] = """'String'"""
        self.vs[17]["GUID__"] = 2821857244522289763
        self.vs[18]["name"] = """value"""
        self.vs[18]["mm__"] = """Attribute"""
        self.vs[18]["Type"] = """'String'"""
        self.vs[18]["GUID__"] = 7147353299129977256
        self.vs[19]["name"] = """key"""
        self.vs[19]["mm__"] = """Attribute"""
        self.vs[19]["Type"] = """'String'"""
        self.vs[19]["GUID__"] = 1814941449420549045
        self.vs[20]["name"] = """value"""
        self.vs[20]["mm__"] = """Attribute"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["GUID__"] = 6748338583818228435

