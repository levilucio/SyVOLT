

from core.himesis import Himesis

class Hcompostype_component_SolveRef_PhysicalNode_Partition_Module_CompositionType_ComponentPrototype(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model Hcompostype_component_SolveRef_PhysicalNode_Partition_Module_CompositionType_ComponentPrototype.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hcompostype_component_SolveRef_PhysicalNode_Partition_Module_CompositionType_ComponentPrototype, self).__init__(name='Hcompostype_component_SolveRef_PhysicalNode_Partition_Module_CompositionType_ComponentPrototype', num_nodes=31, edges=[])
        
        # Add the edges
        self.add_edges([[0, 28], [28, 3], [0, 29], [29, 4], [0, 30], [30, 5], [1, 8], [8, 6], [1, 9], [9, 7], [3, 10], [10, 4], [4, 11], [11, 5], [6, 12], [12, 7], [7, 13], [13, 6], [6, 14], [14, 3], [7, 15], [15, 5], [6, 16], [16, 17], [18, 19], [19, 17], [18, 20], [20, 21], [7, 22], [22, 23], [24, 25], [25, 23], [24, 26], [26, 27], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """compostype_component_SolveRef_PhysicalNode_Partition_Module_CompositionType_ComponentPrototype"""
        self["GUID__"] = 3671788133972303474
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 7862315039454778239
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 6309980538208105011
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 8259557393800876920
        self.vs[3]["name"] = """"""
        self.vs[3]["classtype"] = """PhysicalNode"""
        self.vs[3]["mm__"] = """PhysicalNode"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 7440208197228033325
        self.vs[4]["name"] = """"""
        self.vs[4]["classtype"] = """Partition"""
        self.vs[4]["mm__"] = """Partition"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = 4575826903688898001
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """Module"""
        self.vs[5]["mm__"] = """Module"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 3557505733571763129
        self.vs[6]["name"] = """"""
        self.vs[6]["classtype"] = """CompositionType"""
        self.vs[6]["mm__"] = """CompositionType"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = 8590785366522609884
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """ComponentPrototype"""
        self.vs[7]["mm__"] = """ComponentPrototype"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = 6618454890108689317
        self.vs[8]["mm__"] = """apply_contains"""
        self.vs[8]["GUID__"] = 3963536465733386903
        self.vs[9]["mm__"] = """apply_contains"""
        self.vs[9]["GUID__"] = 6871495822502419225
        self.vs[10]["associationType"] = """partition"""
        self.vs[10]["mm__"] = """directLink_S"""
        self.vs[10]["GUID__"] = 4385493516469952231
        self.vs[11]["associationType"] = """module"""
        self.vs[11]["mm__"] = """directLink_S"""
        self.vs[11]["GUID__"] = 573461379563196035
        self.vs[12]["associationType"] = """component"""
        self.vs[12]["mm__"] = """directLink_T"""
        self.vs[12]["GUID__"] = 9009715784386671213
        self.vs[13]["associationType"] = """type"""
        self.vs[13]["mm__"] = """directLink_T"""
        self.vs[13]["GUID__"] = 7315886808596415271
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 4159519627235387946
        self.vs[15]["mm__"] = """backward_link"""
        self.vs[15]["type"] = """ruleDef"""
        self.vs[15]["GUID__"] = 7472810553122366514
        self.vs[16]["mm__"] = """hasAttribute_T"""
        self.vs[16]["GUID__"] = 4600815958956079730
        self.vs[17]["name"] = """ApplyAttribute"""
        self.vs[17]["Type"] = """'String'"""
        self.vs[17]["mm__"] = """Attribute"""
        self.vs[17]["GUID__"] = 6640457318794629906
        self.vs[18]["name"] = """eq_"""
        self.vs[18]["mm__"] = """Equation"""
        self.vs[18]["GUID__"] = 2171548106008382325
        self.vs[19]["mm__"] = """leftExpr"""
        self.vs[19]["GUID__"] = 7431179909321665201
        self.vs[20]["mm__"] = """rightExpr"""
        self.vs[20]["GUID__"] = 8518281069848172550
        self.vs[21]["name"] = """solveRef"""
        self.vs[21]["Type"] = """'String'"""
        self.vs[21]["mm__"] = """Constant"""
        self.vs[21]["GUID__"] = 4692158291825186139
        self.vs[22]["mm__"] = """hasAttribute_T"""
        self.vs[22]["GUID__"] = 6591849345686713684
        self.vs[23]["name"] = """ApplyAttribute"""
        self.vs[23]["Type"] = """'String'"""
        self.vs[23]["mm__"] = """Attribute"""
        self.vs[23]["GUID__"] = 7776144607807901326
        self.vs[24]["name"] = """eq_"""
        self.vs[24]["mm__"] = """Equation"""
        self.vs[24]["GUID__"] = 3853934979620933456
        self.vs[25]["mm__"] = """leftExpr"""
        self.vs[25]["GUID__"] = 4021762619325935662
        self.vs[26]["mm__"] = """rightExpr"""
        self.vs[26]["GUID__"] = 1066209295978088610
        self.vs[27]["name"] = """solveRef"""
        self.vs[27]["Type"] = """'String'"""
        self.vs[27]["mm__"] = """Constant"""
        self.vs[27]["GUID__"] = 3944217045298734753
        self.vs[28]["mm__"] = """match_contains"""
        self.vs[28]["GUID__"] = 8526824471164987492
        self.vs[29]["mm__"] = """match_contains"""
        self.vs[29]["GUID__"] = 4843076848138277205
        self.vs[30]["mm__"] = """match_contains"""
        self.vs[30]["GUID__"] = 1336742661662359560

