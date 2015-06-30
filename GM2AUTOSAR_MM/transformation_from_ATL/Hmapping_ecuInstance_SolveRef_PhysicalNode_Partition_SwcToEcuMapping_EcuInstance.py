

from core.himesis import Himesis

class Hmapping_ecuInstance_SolveRef_PhysicalNode_Partition_SwcToEcuMapping_EcuInstance(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model Hmapping_ecuInstance_SolveRef_PhysicalNode_Partition_SwcToEcuMapping_EcuInstance.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hmapping_ecuInstance_SolveRef_PhysicalNode_Partition_SwcToEcuMapping_EcuInstance, self).__init__(name='Hmapping_ecuInstance_SolveRef_PhysicalNode_Partition_SwcToEcuMapping_EcuInstance', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 9], [9, 3], [0, 10], [10, 4], [1, 11], [11, 5], [1, 12], [12, 6], [3, 7], [7, 4], [5, 8], [8, 6], [6, 13], [13, 3], [5, 14], [14, 4], [5, 15], [15, 16], [17, 18], [18, 16], [17, 19], [19, 20], [6, 21], [21, 22], [23, 24], [24, 22], [23, 25], [25, 26], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """mapping_ecuInstance_SolveRef_PhysicalNode_Partition_SwcToEcuMapping_EcuInstance"""
        self["GUID__"] = 2154031390542943180
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 5102593288397674235
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 8001847859617743108
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 4479661505254589107
        self.vs[3]["name"] = """"""
        self.vs[3]["classtype"] = """PhysicalNode"""
        self.vs[3]["mm__"] = """PhysicalNode"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 2285267077133646457
        self.vs[4]["name"] = """"""
        self.vs[4]["classtype"] = """Partition"""
        self.vs[4]["mm__"] = """Partition"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = 1490969750177007973
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """SwcToEcuMapping"""
        self.vs[5]["mm__"] = """SwcToEcuMapping"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = 8488460680776613822
        self.vs[6]["name"] = """"""
        self.vs[6]["classtype"] = """EcuInstance"""
        self.vs[6]["mm__"] = """EcuInstance"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = 6920111414933667604
        self.vs[7]["associationType"] = """partition"""
        self.vs[7]["mm__"] = """directLink_S"""
        self.vs[7]["GUID__"] = 8205739282487786859
        self.vs[8]["associationType"] = """ecuInstance"""
        self.vs[8]["mm__"] = """directLink_T"""
        self.vs[8]["GUID__"] = 5367916582829304930
        self.vs[9]["mm__"] = """match_contains"""
        self.vs[9]["GUID__"] = 5203281314956123027
        self.vs[10]["mm__"] = """match_contains"""
        self.vs[10]["GUID__"] = 5125394446659756554
        self.vs[11]["mm__"] = """apply_contains"""
        self.vs[11]["GUID__"] = 2152334310171115671
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 5005445342535653919
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 5460843808286882683
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 4211036993067317764
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 2791475333410634732
        self.vs[16]["name"] = """ApplyAttribute"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["GUID__"] = 7706309371627002329
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 2071651777937485598
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 2056817141425851426
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 3389531964004316429
        self.vs[20]["name"] = """solveRef"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 2414314444814221872
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 6060858302463814497
        self.vs[22]["name"] = """ApplyAttribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["GUID__"] = 1138839522188377913
        self.vs[23]["name"] = """eq_"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = 3167066037718916686
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = 5132573809555330025
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = 6546175594961852512
        self.vs[26]["name"] = """solveRef"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 3002661233240966042

