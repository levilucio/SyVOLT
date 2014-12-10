

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HRule1_1(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HRule1_1.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HRule1_1, self).__init__(name='HRule1_1', num_nodes=15, edges=[])
        
        # Add the edges
        self.add_edges([(5, 0), (0, 6), (4, 9), (9, 1), (4, 10), (10, 7), (1, 3), (1, 11), (8, 2), (2, 4), (11, 5), (7, 12), (12, 6), (3, 7), (13, 5), (14, 6), (8, 13), (8, 14)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'GM2AUTOSAR_MM'
p2
a.""")
        self["name"] = """rule1_1"""
        self["GUID__"] = UUID('49c41f1f-b81e-41c2-89f6-a28469f1a4dc')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """virtualDevice"""
        self.vs[0]["mm__"] = """directLink_S"""
        self.vs[0]["GUID__"] = UUID('953af253-f6fe-47e6-8a61-04ef21dc3074')
        self.vs[1]["name"] = """s1"""
        self.vs[1]["classtype"] = """System"""
        self.vs[1]["mm__"] = """System"""
        self.vs[1]["cardinality"] = """+"""
        self.vs[1]["GUID__"] = UUID('67045dca-9483-44fb-9925-cc6527bfef28')
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = UUID('70c8195f-f3f7-4003-be6e-1cb334707b5e')
        self.vs[3]["associationType"] = """softwareComposition"""
        self.vs[3]["mm__"] = """directLink_T"""
        self.vs[3]["GUID__"] = UUID('f6fb5853-d88b-417e-b6c6-460c74017036')
        self.vs[4]["mm__"] = """ApplyModel"""
        self.vs[4]["GUID__"] = UUID('8ec9b788-5927-4166-8c33-b1be0de8bcc5')
        self.vs[5]["name"] = """ecu1"""
        self.vs[5]["classtype"] = """ECU"""
        self.vs[5]["mm__"] = """ECU"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = UUID('7d01461f-8c08-4c97-a3ee-2b23a18df643')
        self.vs[6]["name"] = """vd1"""
        self.vs[6]["classtype"] = """VirtualDevice"""
        self.vs[6]["mm__"] = """VirtualDevice"""
        self.vs[6]["cardinality"] = """+"""
        self.vs[6]["GUID__"] = UUID('8fbf84f5-5f4f-4c77-90ba-786dc988afa6')
        self.vs[7]["name"] = """sc1"""
        self.vs[7]["classtype"] = """SoftwareComposition"""
        self.vs[7]["mm__"] = """SoftwareComposition"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = UUID('a25e602f-2bd7-4ddf-af41-9099d436e3db')
        self.vs[8]["mm__"] = """MatchModel"""
        self.vs[8]["GUID__"] = UUID('b90b4300-e995-40f7-a2b6-e128f4376e90')
        self.vs[9]["mm__"] = """apply_contains"""
        self.vs[9]["GUID__"] = UUID('753d1a70-aafd-4baf-837c-594465f6a97c')
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = UUID('f4f77713-a127-49d0-bf8d-db65d85e934c')
        self.vs[11]["mm__"] = """backward_link"""
        self.vs[11]["type"] = """ruleDef"""
        self.vs[11]["GUID__"] = UUID('788bb9bb-e6b8-4a16-8901-d181c32a0755')
        self.vs[12]["mm__"] = """backward_link"""
        self.vs[12]["type"] = """ruleDef"""
        self.vs[12]["GUID__"] = UUID('3fa55cf1-5d3a-4ad5-9692-1cf1958e987a')
        self.vs[13]["mm__"] = """match_contains"""
        self.vs[13]["GUID__"] = UUID('563529d2-e463-408e-a1d7-35440b821d55')
        self.vs[14]["mm__"] = """match_contains"""
        self.vs[14]["GUID__"] = UUID('7485211a-2611-4ed8-b1a2-e98ce74c542a')

