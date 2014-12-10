

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HRule1_1Exists(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HRule1_1Exists.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HRule1_1Exists, self).__init__(name='HRule1_1Exists', num_nodes=15, edges=[])
        
        # Add the edges
        self.add_edges([(5, 0), (0, 6), (4, 9), (9, 1), (4, 10), (10, 7), (1, 3), (1, 11), (8, 2), (2, 4), (11, 5), (7, 12), (12, 6), (3, 7), (13, 5), (14, 6), (8, 13), (8, 14)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'GM2AUTOSAR_MM'
p2
a.""")
        self["name"] = """rule1_1Exists"""
        self["GUID__"] = UUID('78d9ddc0-4f0d-4a27-ade2-62894498bb42')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """virtualDevice"""
        self.vs[0]["mm__"] = """directLink_S"""
        self.vs[0]["GUID__"] = UUID('7915190a-2920-4089-af85-ffd3848db741')
        self.vs[1]["name"] = """s1"""
        self.vs[1]["classtype"] = """System"""
        self.vs[1]["mm__"] = """System"""
        self.vs[1]["cardinality"] = """1"""
        self.vs[1]["GUID__"] = UUID('7f3957d8-dcfa-4a96-a98d-b08259783f77')
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = UUID('30c859df-f003-4e47-bc81-51b498fb7d17')
        self.vs[3]["associationType"] = """softwareComposition"""
        self.vs[3]["mm__"] = """directLink_T"""
        self.vs[3]["GUID__"] = UUID('12f9177e-4df7-444a-9a2e-2c7f6e2bace7')
        self.vs[4]["mm__"] = """ApplyModel"""
        self.vs[4]["GUID__"] = UUID('ddaf8fa4-7eb9-44df-8b4d-5eff8e2c8cd2')
        self.vs[5]["name"] = """ecu1"""
        self.vs[5]["classtype"] = """ECU"""
        self.vs[5]["mm__"] = """ECU"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = UUID('14e7773c-bc4f-4367-a09e-c237bcee8e1a')
        self.vs[6]["name"] = """vd1"""
        self.vs[6]["classtype"] = """VirtualDevice"""
        self.vs[6]["mm__"] = """VirtualDevice"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = UUID('e5179ffa-e963-4c06-b5bc-6f095e94d8d2')
        self.vs[7]["name"] = """sc1"""
        self.vs[7]["classtype"] = """SoftwareComposition"""
        self.vs[7]["mm__"] = """SoftwareComposition"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = UUID('d5559a7a-35a7-4b56-9b71-9610a5a04fc4')
        self.vs[8]["mm__"] = """MatchModel"""
        self.vs[8]["GUID__"] = UUID('d479bec9-ef32-4de4-9308-fd145c8af577')
        self.vs[9]["mm__"] = """apply_contains"""
        self.vs[9]["GUID__"] = UUID('c9d98f60-85a1-48d4-9b2b-a1c5d9c097e0')
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = UUID('2ac6fdc6-a048-40e9-9969-371d000012d5')
        self.vs[11]["mm__"] = """backward_link"""
        self.vs[11]["type"] = """ruleDef"""
        self.vs[11]["GUID__"] = UUID('e888f3bd-52d3-4708-9067-0eff5f2c6f3b')
        self.vs[12]["mm__"] = """backward_link"""
        self.vs[12]["type"] = """ruleDef"""
        self.vs[12]["GUID__"] = UUID('b6668e8b-b8a8-44f9-8dcb-03d30e7ee7c3')
        self.vs[13]["mm__"] = """match_contains"""
        self.vs[13]["GUID__"] = UUID('fcba2faf-c24e-424d-bb31-9d36eaafaa99')
        self.vs[14]["mm__"] = """match_contains"""
        self.vs[14]["GUID__"] = UUID('37616932-e806-43d5-9e4a-2bd475f1ec8f')

