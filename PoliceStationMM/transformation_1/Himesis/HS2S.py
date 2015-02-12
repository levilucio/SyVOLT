

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HS2S(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HS2S.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HS2S, self).__init__(name='HS2S', num_nodes=14, edges=[])
        
        # Add the edges
        self.add_edges([(5, 0), (0, 7), (7, 1), (1, 13), (8, 2), (2, 12), (11, 3), (3, 5), (6, 4), (4, 12), (9, 6), (8, 10), (11, 9), (10, 13)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'PoliceStationMM'
p2
a.""")
        self["name"] = """S2S"""
        self["GUID__"] = UUID('3de8ef3c-05ae-4b3c-852c-c5981d99504f')
        
        # Set the node attributes
        self.vs[0]["mm__"] = """apply_contains"""
        self.vs[0]["GUID__"] = UUID('d57b1aa8-0fef-421b-b80a-1dec411cc1e7')
        self.vs[1]["mm__"] = """hasAttribute_T"""
        self.vs[1]["GUID__"] = UUID('ba7c8171-a56f-4ed1-8254-c5cc572371cc')
        self.vs[2]["mm__"] = """leftExpr"""
        self.vs[2]["GUID__"] = UUID('dccb63e0-3a24-4919-8f3d-ccd6821326cd')
        self.vs[3]["mm__"] = """paired_with"""
        self.vs[3]["GUID__"] = UUID('f4121763-dfb0-445f-bd33-82690726b0b8')
        self.vs[4]["mm__"] = """hasAttribute_S"""
        self.vs[4]["GUID__"] = UUID('756bae34-952e-400c-be0b-4f68fbbaa1fe')
        self.vs[5]["mm__"] = """ApplyModel"""
        self.vs[5]["GUID__"] = UUID('0a179e74-8b75-4dcc-ae9a-c454a3bb6b48')
        self.vs[6]["mm__"] = """Station_S"""
        self.vs[6]["classtype"] = """1"""
        self.vs[6]["cardinality"] = """s_"""
        self.vs[6]["name"] = """s_"""
        self.vs[6]["GUID__"] = UUID('a8600e37-d936-44ca-bc46-7a9d28cc631e')
        self.vs[7]["mm__"] = """Station_T"""
        self.vs[7]["classtype"] = """t_"""
        self.vs[7]["name"] = """s_"""
        self.vs[7]["GUID__"] = UUID('de25f120-1a74-43b8-955b-5bf633a322e5')
        self.vs[8]["mm__"] = """Equation"""
        self.vs[8]["GUID__"] = UUID('8aa21d7b-5535-4b0e-8744-f8c01b884d0c')
        self.vs[9]["mm__"] = """match_contains"""
        self.vs[9]["GUID__"] = UUID('9a7ebd7c-4c8b-42d9-ae55-79dd51aad897')
        self.vs[10]["mm__"] = """rightExpr"""
        self.vs[10]["GUID__"] = UUID('6425809e-5e0c-48ea-b11b-2eb0a8b1cd42')
        self.vs[11]["mm__"] = """MatchModel"""
        self.vs[11]["GUID__"] = UUID('59539d35-41a0-4cad-ac64-0fad3a792a42')
        self.vs[12]["mm__"] = """Attribute"""
        self.vs[12]["name"] = """name"""
        self.vs[12]["GUID__"] = UUID('e829868f-eda2-4a6d-bd26-afe37fb27c85')
        self.vs[13]["mm__"] = """Attribute"""
        self.vs[13]["name"] = """name"""
        self.vs[13]["GUID__"] = UUID('c51098cb-d901-46cb-95b4-c18ce1d9ea66')

