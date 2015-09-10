

from core.himesis import Himesis

class Hsysmapping_swMapping_SolveRef_PhysicalNode_Partition_SystemMapping_SwcToEcuMapping(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model Hsysmapping_swMapping_SolveRef_PhysicalNode_Partition_SystemMapping_SwcToEcuMapping.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hsysmapping_swMapping_SolveRef_PhysicalNode_Partition_SystemMapping_SwcToEcuMapping, self).__init__(name='Hsysmapping_swMapping_SolveRef_PhysicalNode_Partition_SystemMapping_SwcToEcuMapping', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 9], [9, 3], [0, 10], [10, 4], [1, 11], [11, 5], [1, 12], [12, 6], [3, 7], [7, 4], [5, 8], [8, 6], [5, 13], [13, 3], [6, 14], [14, 4], [5, 15], [15, 16], [17, 18], [18, 16], [17, 19], [19, 20], [6, 21], [21, 22], [23, 24], [24, 22], [23, 25], [25, 26], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """sysmapping_swMapping_SolveRef_PhysicalNode_Partition_SystemMapping_SwcToEcuMapping"""
        self["GUID__"] = 8192893704120951459
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 6977392703624477414
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 7828885443795326301
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 2625176960646331792
        self.vs[3]["name"] = """"""
        self.vs[3]["classtype"] = """PhysicalNode"""
        self.vs[3]["mm__"] = """PhysicalNode"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 4650715886733937626
        self.vs[4]["name"] = """"""
        self.vs[4]["classtype"] = """Partition"""
        self.vs[4]["mm__"] = """Partition"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = 4839637421785076182
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """SystemMapping"""
        self.vs[5]["mm__"] = """SystemMapping"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = 3478098931514129141
        self.vs[6]["name"] = """"""
        self.vs[6]["classtype"] = """SwcToEcuMapping"""
        self.vs[6]["mm__"] = """SwcToEcuMapping"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = 5483956647862923086
        self.vs[7]["associationType"] = """partition"""
        self.vs[7]["mm__"] = """directLink_S"""
        self.vs[7]["GUID__"] = 1631901294562668908
        self.vs[8]["associationType"] = """swMapping"""
        self.vs[8]["mm__"] = """directLink_T"""
        self.vs[8]["GUID__"] = 5267897680175772035
        self.vs[9]["mm__"] = """match_contains"""
        self.vs[9]["GUID__"] = 4054131902500580467
        self.vs[10]["mm__"] = """match_contains"""
        self.vs[10]["GUID__"] = 3124107003625621908
        self.vs[11]["mm__"] = """apply_contains"""
        self.vs[11]["GUID__"] = 9069573659422126953
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 7332952996356521255
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 2655768987390212019
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 5960159993670953561
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 1144879601067745074
        self.vs[16]["name"] = """ApplyAttribute"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["GUID__"] = 2103854269393252136
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 7264479307091387740
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 4863946828524105905
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 1587694871810551326
        self.vs[20]["name"] = """solveRef"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 2655494637118104140
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 7729633980811999078
        self.vs[22]["name"] = """ApplyAttribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["GUID__"] = 3779080394679039043
        self.vs[23]["name"] = """eq_"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = 7676894768217604924
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = 3852510855527722188
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = 1016823515176949975
        self.vs[26]["name"] = """solveRef"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 7274333601885029913

