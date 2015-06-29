

from core.himesis import Himesis

class Hlayer1rule13(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model Hlayer1rule13.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer1rule13, self).__init__(name='Hlayer1rule13', num_nodes=14, edges=[])
        
        # Add the edges
        self.add_edges([[0, 8], [8, 3], [0, 10], [10, 9], [1, 11], [11, 4], [1, 13], [13, 12], [3, 5], [5, 9], [4, 6], [6, 12], [4, 7], [7, 3], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer1rule13"""
        self["GUID__"] = 2142322930580559100
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 8598562241201700010
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 3826635979545463412
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 7282244382907759916
        self.vs[3]["name"] = """layer1rule13class0"""
        self.vs[3]["classtype"] = """Operation"""
        self.vs[3]["mm__"] = """Operation"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 8548750461509382069
        self.vs[4]["name"] = """layer1rule13class2"""
        self.vs[4]["classtype"] = """FunctionPrototype"""
        self.vs[4]["mm__"] = """FunctionPrototype"""
        self.vs[4]["cardinality"] = """1"""
        self.vs[4]["GUID__"] = 3256607055038160331
        self.vs[5]["associationType"] = """type"""
        self.vs[5]["mm__"] = """directLink_S"""
        self.vs[5]["GUID__"] = 915830447240994933
        self.vs[6]["associationType"] = """type"""
        self.vs[6]["mm__"] = """directLink_T"""
        self.vs[6]["GUID__"] = 9024933990276671380
        self.vs[7]["mm__"] = """backward_link"""
        self.vs[7]["type"] = """ruleDef"""
        self.vs[7]["GUID__"] = 5308843554123140936
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 3113434174151966836
        self.vs[9]["name"] = """layer1rule13class1"""
        self.vs[9]["classtype"] = """VoidType"""
        self.vs[9]["mm__"] = """VoidType"""
        self.vs[9]["cardinality"] = """+"""
        self.vs[9]["GUID__"] = 2833634724628090435
        self.vs[10]["mm__"] = """match_contains"""
        self.vs[10]["GUID__"] = 7316075225689582999
        self.vs[11]["mm__"] = """apply_contains"""
        self.vs[11]["GUID__"] = 34972057941672210
        self.vs[12]["name"] = """layer1rule13class3"""
        self.vs[12]["classtype"] = """VoidType"""
        self.vs[12]["mm__"] = """VoidType"""
        self.vs[12]["cardinality"] = """1"""
        self.vs[12]["GUID__"] = 7375912335853313429
        self.vs[13]["mm__"] = """apply_contains"""
        self.vs[13]["GUID__"] = 7716372394149442226

