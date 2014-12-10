

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HMapDistributable(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HMapDistributable.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HMapDistributable, self).__init__(name='HMapDistributable', num_nodes=16, edges=[])
        
        # Add the edges
        self.add_edges([(5, 9), (9, 6), (6, 10), (10, 0), (4, 11), (11, 8), (4, 12), (12, 2), (15, 0), (7, 1), (1, 4), (3, 2), (8, 3), (13, 5), (14, 6), (7, 13), (7, 14), (7, 15)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'GM2AUTOSAR_MM'
p2
a.""")
        self["name"] = """MapDistributable"""
        self["GUID__"] = UUID('c135978b-9906-4777-b3e8-040271ee2641')
        
        # Set the node attributes
        self.vs[0]["name"] = """dist1"""
        self.vs[0]["classtype"] = """Distributable"""
        self.vs[0]["mm__"] = """Distributable"""
        self.vs[0]["cardinality"] = """+"""
        self.vs[0]["GUID__"] = UUID('9ace6e52-49d0-4440-9943-1b36a97804a3')
        self.vs[1]["mm__"] = """paired_with"""
        self.vs[1]["GUID__"] = UUID('7bb06824-5d57-4598-8d68-1868a65318d0')
        self.vs[2]["name"] = """comp1"""
        self.vs[2]["classtype"] = """ComponentPrototype"""
        self.vs[2]["mm__"] = """ComponentPrototype"""
        self.vs[2]["cardinality"] = """1"""
        self.vs[2]["GUID__"] = UUID('4c3b6a9d-b790-457e-9139-42c7218b11fb')
        self.vs[3]["associationType"] = """componentPrototype"""
        self.vs[3]["mm__"] = """directLink_T"""
        self.vs[3]["GUID__"] = UUID('bef17871-daea-4ab8-8274-eed9cf184aaf')
        self.vs[4]["mm__"] = """ApplyModel"""
        self.vs[4]["GUID__"] = UUID('431e545b-c0aa-4c17-98de-526e1cab1ff4')
        self.vs[5]["name"] = """ecu1"""
        self.vs[5]["classtype"] = """ECU"""
        self.vs[5]["mm__"] = """ECU"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = UUID('15ef96ac-20f7-43b3-8ca7-72e64fdf1acb')
        self.vs[6]["name"] = """vd1"""
        self.vs[6]["classtype"] = """VirtualDevice"""
        self.vs[6]["mm__"] = """VirtualDevice"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = UUID('2c123012-24f0-4b23-8391-e4a898a9dbec')
        self.vs[7]["mm__"] = """MatchModel"""
        self.vs[7]["GUID__"] = UUID('19d3bec1-8294-4432-96f4-94fdad0d49a4')
        self.vs[8]["name"] = """sctemc1"""
        self.vs[8]["classtype"] = """SwCompToEcuMapping_component"""
        self.vs[8]["mm__"] = """SwCompToEcuMapping_component"""
        self.vs[8]["cardinality"] = """1"""
        self.vs[8]["GUID__"] = UUID('e8d64118-35b8-42f7-875a-123136cd7a83')
        self.vs[9]["associationType"] = """virtualDevice"""
        self.vs[9]["mm__"] = """directLink_S"""
        self.vs[9]["GUID__"] = UUID('aec63ce4-f95d-47c9-bd27-087fc8bd507a')
        self.vs[10]["associationType"] = """distributable"""
        self.vs[10]["mm__"] = """directLink_S"""
        self.vs[10]["GUID__"] = UUID('0566b110-af56-4a30-b6a7-a114ae1201da')
        self.vs[11]["mm__"] = """apply_contains"""
        self.vs[11]["GUID__"] = UUID('562ce050-a763-40bd-9ea4-136fbdd0e45a')
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = UUID('a90ef605-7d8f-4fd9-b47d-7a179ba009aa')
        self.vs[13]["mm__"] = """match_contains"""
        self.vs[13]["GUID__"] = UUID('9391bc3f-3efa-4390-847d-4fe5edef911b')
        self.vs[14]["mm__"] = """match_contains"""
        self.vs[14]["GUID__"] = UUID('05c165b2-5653-4ede-80ef-ba86817cc976')
        self.vs[15]["mm__"] = """match_contains"""
        self.vs[15]["GUID__"] = UUID('44d3d370-9321-4658-9bad-67ce26b08f21')

