

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HSF2SF_run1(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HSF2SF_run1.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HSF2SF_run1, self).__init__(name='HSF2SF_run1', num_nodes=15, edges=[])
        
        # Add the edges
        self.add_edges([(1, 9), (9, 5), (1, 10), (10, 3), (5, 11), (11, 6), (3, 12), (12, 7), (5, 0), (0, 3), (8, 1), (2, 8), (2, 13), (2, 14), (6, 4), (4, 7), (13, 6), (14, 7)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'PoliceStationMM'
p2
a.""")
        self["name"] = """SF2SF_run1"""
        self["GUID__"] = UUID('dfdb89b4-2249-4daf-aa9e-fcae67220aeb')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """s2f"""
        self.vs[0]["mm__"] = """directLink_T"""
        self.vs[0]["GUID__"] = UUID('e92b6f49-26af-487c-8538-2ab20def7212')
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = UUID('5ef5754a-dc2d-4e62-afc1-91b5cd41a091')
        self.vs[2]["mm__"] = """MatchModel"""
        self.vs[2]["GUID__"] = UUID('de02f486-9530-4289-8643-1fb2f8d4964d')
        self.vs[3]["name"] = """5.f"""
        self.vs[3]["classtype"] = """female1"""
        self.vs[3]["mm__"] = """Female_T"""
        self.vs[3]["GUID__"] = UUID('737b3568-0088-4145-943d-885aa6054c23')
        self.vs[4]["mm__"] = """indirectLink_S"""
        self.vs[4]["GUID__"] = UUID('047c7501-6a66-4462-9911-51b24b4d6566')
        self.vs[5]["name"] = """5.s"""
        self.vs[5]["classtype"] = """station1"""
        self.vs[5]["mm__"] = """Station_T"""
        self.vs[5]["GUID__"] = UUID('27ffc2bb-165b-467f-83c7-9cee0fed6376')
        self.vs[6]["name"] = """5.s"""
        self.vs[6]["classtype"] = """station1"""
        self.vs[6]["mm__"] = """Station_S"""
        self.vs[6]["cardinality"] = """+"""
        self.vs[6]["GUID__"] = UUID('423b25d2-e3b5-492e-8fff-9b1a7bcb5c83')
        self.vs[7]["name"] = """5.f"""
        self.vs[7]["classtype"] = """female1"""
        self.vs[7]["mm__"] = """Female_S"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = UUID('399152f9-8641-4bb4-9164-642e7ba272a4')
        self.vs[8]["mm__"] = """paired_with"""
        self.vs[8]["GUID__"] = UUID('68b13a3f-c72f-4cb8-a8ff-c8c80251e9a5')
        self.vs[9]["mm__"] = """apply_contains"""
        self.vs[9]["GUID__"] = UUID('60f486e6-837e-46d6-93b3-5dcae950e0ec')
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = UUID('e09712aa-4f5b-4e36-b8bd-c6f2aaa959a9')
        self.vs[11]["mm__"] = """backward_link"""
        self.vs[11]["GUID__"] = UUID('cac254da-dbc8-4a7d-918a-fc710dc44380')
        self.vs[12]["mm__"] = """backward_link"""
        self.vs[12]["GUID__"] = UUID('b5b931ad-f68c-4b72-9a29-72e15008c413')
        self.vs[13]["mm__"] = """match_contains"""
        self.vs[13]["GUID__"] = UUID('c4ae51e9-0a7c-4a4d-8942-459e97121693')
        self.vs[14]["mm__"] = """match_contains"""
        self.vs[14]["GUID__"] = UUID('e36125d5-2d11-47c0-a813-a723d93b9bab')

