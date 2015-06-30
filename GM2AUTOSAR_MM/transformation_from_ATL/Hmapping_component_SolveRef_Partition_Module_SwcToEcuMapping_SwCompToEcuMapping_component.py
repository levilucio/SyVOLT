

from core.himesis import Himesis

class Hmapping_component_SolveRef_Partition_Module_SwcToEcuMapping_SwCompToEcuMapping_component(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model Hmapping_component_SolveRef_Partition_Module_SwcToEcuMapping_SwCompToEcuMapping_component.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hmapping_component_SolveRef_Partition_Module_SwcToEcuMapping_SwCompToEcuMapping_component, self).__init__(name='Hmapping_component_SolveRef_Partition_Module_SwcToEcuMapping_SwCompToEcuMapping_component', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 9], [9, 3], [0, 10], [10, 4], [1, 11], [11, 5], [1, 12], [12, 6], [3, 7], [7, 4], [5, 8], [8, 6], [5, 13], [13, 3], [6, 14], [14, 4], [5, 15], [15, 16], [17, 18], [18, 16], [17, 19], [19, 20], [6, 21], [21, 22], [23, 24], [24, 22], [23, 25], [25, 26], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """mapping_component_SolveRef_Partition_Module_SwcToEcuMapping_SwCompToEcuMapping_component"""
        self["GUID__"] = 8041783360518296707
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 3557359669623608444
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 751195744760430780
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 1938269759847842538
        self.vs[3]["name"] = """"""
        self.vs[3]["classtype"] = """Partition"""
        self.vs[3]["mm__"] = """Partition"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 1291949723856710503
        self.vs[4]["name"] = """"""
        self.vs[4]["classtype"] = """Module"""
        self.vs[4]["mm__"] = """Module"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = 6586821227716312785
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """SwcToEcuMapping"""
        self.vs[5]["mm__"] = """SwcToEcuMapping"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = 7992399918846343509
        self.vs[6]["name"] = """"""
        self.vs[6]["classtype"] = """SwCompToEcuMapping_component"""
        self.vs[6]["mm__"] = """SwCompToEcuMapping_component"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = 8636813567206397539
        self.vs[7]["associationType"] = """module"""
        self.vs[7]["mm__"] = """directLink_S"""
        self.vs[7]["GUID__"] = 1767814555387699506
        self.vs[8]["associationType"] = """component"""
        self.vs[8]["mm__"] = """directLink_T"""
        self.vs[8]["GUID__"] = 1610150398828982745
        self.vs[9]["mm__"] = """match_contains"""
        self.vs[9]["GUID__"] = 3808658859622104787
        self.vs[10]["mm__"] = """match_contains"""
        self.vs[10]["GUID__"] = 5100041837672490595
        self.vs[11]["mm__"] = """apply_contains"""
        self.vs[11]["GUID__"] = 4618775689700222834
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 5167104951544611098
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 5301295195068487807
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 2907978912780063605
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 3429809488797205739
        self.vs[16]["name"] = """ApplyAttribute"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["GUID__"] = 8644218814136035381
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 8132727984906570154
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 4521579024057266309
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 9067671453684522903
        self.vs[20]["name"] = """solveRef"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 383202574687058388
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 3186561837967973575
        self.vs[22]["name"] = """ApplyAttribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["GUID__"] = 444839457765807686
        self.vs[23]["name"] = """eq_"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = 1219454992068908699
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = 2266504116641476668
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = 3582037872213941100
        self.vs[26]["name"] = """solveRef"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 6115017882173120960

