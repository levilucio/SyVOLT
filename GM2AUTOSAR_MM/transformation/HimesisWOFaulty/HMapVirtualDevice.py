

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HMapVirtualDevice(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HMapVirtualDevice.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HMapVirtualDevice, self).__init__(name='HMapVirtualDevice', num_nodes=13, edges=[])
        
        # Add the edges
        self.add_edges([(4, 8), (8, 6), (6, 9), (9, 1), (3, 0), (0, 5), (12, 1), (7, 2), (2, 3), (10, 4), (11, 6), (7, 10), (7, 11), (7, 12)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'GM2AUTOSAR_MM'
p2
a.""")
        self["name"] = """MapVirtualDevice"""
        self["GUID__"] = UUID('03d2fb55-275f-47b5-932f-43b0f4668201')
        
        # Set the node attributes
        self.vs[0]["mm__"] = """apply_contains"""
        self.vs[0]["GUID__"] = UUID('18777d3b-08d3-4862-b6ea-a88ee8be0c3d')
        self.vs[1]["name"] = """dist1"""
        self.vs[1]["classtype"] = """Distributable"""
        self.vs[1]["mm__"] = """Distributable"""
        self.vs[1]["cardinality"] = """1"""
        self.vs[1]["GUID__"] = UUID('cf165c24-8a31-4566-b2c5-54d7e5ad1bf2')
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = UUID('b60d014a-9a76-4c4b-904c-5f01441e0987')
        self.vs[3]["mm__"] = """ApplyModel"""
        self.vs[3]["GUID__"] = UUID('bccc7383-7e7e-4f8e-ad89-9a9c17fdeb88')
        self.vs[4]["name"] = """ecu1"""
        self.vs[4]["classtype"] = """ECU"""
        self.vs[4]["mm__"] = """ECU"""
        self.vs[4]["cardinality"] = """1"""
        self.vs[4]["GUID__"] = UUID('806266d4-a980-400d-8a3e-dcab2a829f55')
        self.vs[5]["name"] = """stem1"""
        self.vs[5]["classtype"] = """SwcToEcuMapping"""
        self.vs[5]["mm__"] = """SwcToEcuMapping"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = UUID('026c9b42-933f-4b94-a473-a065405807f9')
        self.vs[6]["name"] = """vd1"""
        self.vs[6]["classtype"] = """VirtualDevice"""
        self.vs[6]["mm__"] = """VirtualDevice"""
        self.vs[6]["cardinality"] = """+"""
        self.vs[6]["GUID__"] = UUID('6b297345-cbb5-4174-8e36-f51a13e51deb')
        self.vs[7]["mm__"] = """MatchModel"""
        self.vs[7]["GUID__"] = UUID('437ce0cf-0932-47da-89a6-81d8d94a97dc')
        self.vs[8]["associationType"] = """virtualDevice"""
        self.vs[8]["mm__"] = """directLink_S"""
        self.vs[8]["GUID__"] = UUID('14d9aac0-9d83-499a-9ac7-d6c4a7080503')
        self.vs[9]["associationType"] = """distributable"""
        self.vs[9]["mm__"] = """directLink_S"""
        self.vs[9]["GUID__"] = UUID('10140353-153b-4bd8-b0dc-131bfa7f6d55')
        self.vs[10]["mm__"] = """match_contains"""
        self.vs[10]["GUID__"] = UUID('e65655a7-1e45-4062-9ce5-e4138332225e')
        self.vs[11]["mm__"] = """match_contains"""
        self.vs[11]["GUID__"] = UUID('e69d2ade-24cc-484c-8076-fa13d51503c4')
        self.vs[12]["mm__"] = """match_contains"""
        self.vs[12]["GUID__"] = UUID('ffa29afb-c14f-4837-874b-984ee71de67c')

