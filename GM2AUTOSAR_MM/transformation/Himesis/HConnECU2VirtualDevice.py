

from core.himesis import Himesis

class HConnECU2VirtualDevice(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HConnECU2VirtualDevice.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HConnECU2VirtualDevice, self).__init__(name='HConnECU2VirtualDevice', num_nodes=19, edges=[])
        
        # Add the edges
        self.add_edges([[4, 0], [0, 6], [3, 13], [13, 1], [3, 14], [14, 5], [3, 15], [15, 8], [1, 9], [1, 17], [7, 2], [2, 3], [8, 16], [16, 4], [17, 4], [5, 18], [18, 6], [9, 5], [5, 10], [10, 8], [11, 4], [12, 6], [7, 11], [7, 12]])
        # Set the graph attributes
        self["mm__"] = ['GM2AUTOSAR_MM']
        self["name"] = """ConnECU2VirtualDevice"""
        self["GUID__"] = 8384027816084101013
        
        # Set the node attributes
        self.vs[0]["associationType"] = """virtualDevice"""
        self.vs[0]["mm__"] = """directLink_S"""
        self.vs[0]["GUID__"] = 7447166194716733943
        self.vs[1]["name"] = """sysmap1"""
        self.vs[1]["classtype"] = """SystemMapping"""
        self.vs[1]["mm__"] = """SystemMapping"""
        self.vs[1]["cardinality"] = """1"""
        self.vs[1]["GUID__"] = 3068704276520862489
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 6272858782103476813
        self.vs[3]["mm__"] = """ApplyModel"""
        self.vs[3]["GUID__"] = 2032317546483250281
        self.vs[4]["name"] = """ecu1"""
        self.vs[4]["classtype"] = """ECU"""
        self.vs[4]["mm__"] = """ECU"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = 2241667016390749860
        self.vs[5]["name"] = """stem1"""
        self.vs[5]["classtype"] = """SwcToEcuMapping"""
        self.vs[5]["mm__"] = """SwcToEcuMapping"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = 1953841625358388299
        self.vs[6]["name"] = """vd1"""
        self.vs[6]["classtype"] = """VirtualDevice"""
        self.vs[6]["mm__"] = """VirtualDevice"""
        self.vs[6]["cardinality"] = """+"""
        self.vs[6]["GUID__"] = 6578225633871544632
        self.vs[7]["mm__"] = """MatchModel"""
        self.vs[7]["GUID__"] = 231101012544465048
        self.vs[8]["name"] = """ecuinst1"""
        self.vs[8]["classtype"] = """EcuInstance"""
        self.vs[8]["mm__"] = """EcuInstance"""
        self.vs[8]["cardinality"] = """1"""
        self.vs[8]["GUID__"] = 5973759294232967806
        self.vs[9]["associationType"] = """swMapping"""
        self.vs[9]["mm__"] = """directLink_T"""
        self.vs[9]["GUID__"] = 136424888536057268
        self.vs[10]["associationType"] = """ecuInstance"""
        self.vs[10]["mm__"] = """directLink_T"""
        self.vs[10]["GUID__"] = 8152558230445937215
        self.vs[11]["mm__"] = """match_contains"""
        self.vs[11]["GUID__"] = 9187917811443664114
        self.vs[12]["mm__"] = """match_contains"""
        self.vs[12]["GUID__"] = 6359799782629894202
        self.vs[13]["mm__"] = """apply_contains"""
        self.vs[13]["GUID__"] = 1342238534146515369
        self.vs[14]["mm__"] = """apply_contains"""
        self.vs[14]["GUID__"] = 7499992844266129443
        self.vs[15]["mm__"] = """apply_contains"""
        self.vs[15]["GUID__"] = 4538902157719588033
        self.vs[16]["mm__"] = """backward_link"""
        self.vs[16]["type"] = """ruleDef"""
        self.vs[16]["GUID__"] = 4275812935161595061
        self.vs[17]["mm__"] = """backward_link"""
        self.vs[17]["type"] = """ruleDef"""
        self.vs[17]["GUID__"] = 6951876653462934862
        self.vs[18]["mm__"] = """backward_link"""
        self.vs[18]["type"] = """ruleDef"""
        self.vs[18]["GUID__"] = 4138911481510576153

