

from core.himesis import Himesis

class Hlayer0rule9(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model Hlayer0rule9.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer0rule9, self).__init__(name='Hlayer0rule9', num_nodes=24, edges=[])
        
        # Add the edges
        self.add_edges([[0, 4], [4, 3], [1, 21], [21, 5], [1, 22], [22, 6], [1, 23], [23, 7], [5, 15], [15, 7], [7, 16], [16, 6], [3, 8], [8, 17], [5, 9], [9, 18], [10, 11], [11, 18], [10, 12], [13, 19], [19, 17], [13, 20], [20, 14], [12, 13], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer0rule9"""
        self["GUID__"] = 3755196333074056110
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 4719342893076176200
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 5139121876555515518
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 1611774313642141313
        self.vs[3]["name"] = """layer0rule9class0"""
        self.vs[3]["classtype"] = """RequiredPort"""
        self.vs[3]["mm__"] = """RequiredPort"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 7488335639921937011
        self.vs[4]["mm__"] = """match_contains"""
        self.vs[4]["GUID__"] = 7459560290536044352
        self.vs[5]["name"] = """layer0rule9class1"""
        self.vs[5]["classtype"] = """Member"""
        self.vs[5]["mm__"] = """Member"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = 2694547402216592199
        self.vs[6]["name"] = """layer0rule9class2"""
        self.vs[6]["classtype"] = """VoidType"""
        self.vs[6]["mm__"] = """VoidType"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = 6416631915330772508
        self.vs[7]["name"] = """layer0rule9class3"""
        self.vs[7]["classtype"] = """PointerType"""
        self.vs[7]["mm__"] = """PointerType"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = 4853273412217772615
        self.vs[8]["mm__"] = """hasAttribute_S"""
        self.vs[8]["GUID__"] = 6883308479309757275
        self.vs[9]["mm__"] = """hasAttribute_T"""
        self.vs[9]["GUID__"] = 209631574350172942
        self.vs[10]["name"] = """eq_"""
        self.vs[10]["mm__"] = """Equation"""
        self.vs[10]["GUID__"] = 6901405308113944901
        self.vs[11]["mm__"] = """leftExpr"""
        self.vs[11]["GUID__"] = 263799425504130946
        self.vs[12]["mm__"] = """rightExpr"""
        self.vs[12]["GUID__"] = 1086559674651602500
        self.vs[13]["name"] = """Concatlayer0rule9class1attribute020"""
        self.vs[13]["mm__"] = """Concat"""
        self.vs[13]["Type"] = """'String'"""
        self.vs[13]["GUID__"] = 1962398464834573727
        self.vs[14]["name"] = """__port"""
        self.vs[14]["mm__"] = """Constant"""
        self.vs[14]["Type"] = """'String'"""
        self.vs[14]["GUID__"] = 8483931001260691336
        self.vs[15]["associationType"] = """type"""
        self.vs[15]["mm__"] = """directLink_T"""
        self.vs[15]["GUID__"] = 5147577614731773247
        self.vs[16]["associationType"] = """baseType"""
        self.vs[16]["mm__"] = """directLink_T"""
        self.vs[16]["GUID__"] = 3519009623117204259
        self.vs[17]["name"] = """name"""
        self.vs[17]["mm__"] = """Attribute"""
        self.vs[17]["Type"] = """'String'"""
        self.vs[17]["GUID__"] = 4811231498949856113
        self.vs[18]["name"] = """name"""
        self.vs[18]["mm__"] = """Attribute"""
        self.vs[18]["Type"] = """'String'"""
        self.vs[18]["GUID__"] = 3873584886877508375
        self.vs[19]["mm__"] = """hasArgs"""
        self.vs[19]["GUID__"] = 7950113997983902767
        self.vs[20]["mm__"] = """hasArgs"""
        self.vs[20]["GUID__"] = 6511697610704922988
        self.vs[21]["mm__"] = """apply_contains"""
        self.vs[21]["GUID__"] = 5505355265083971855
        self.vs[22]["mm__"] = """apply_contains"""
        self.vs[22]["GUID__"] = 5737463855078401713
        self.vs[23]["mm__"] = """apply_contains"""
        self.vs[23]["GUID__"] = 4597124248697207392

