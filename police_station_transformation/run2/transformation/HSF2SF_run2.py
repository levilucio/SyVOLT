

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HSF2SF_run2(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HSF2SF_run2.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HSF2SF_run2, self).__init__(name='HSF2SF_run2', num_nodes=15, edges=[])
        
        # Add the edges
        self.add_edges([(1, 9), (9, 5), (1, 10), (10, 3), (5, 11), (11, 6), (3, 12), (12, 7), (5, 0), (0, 3), (8, 1), (2, 8), (2, 13), (2, 14), (6, 4), (4, 7), (13, 6), (14, 7)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'PoliceStationMM'
p2
a.""")
        self["name"] = """SF2SF_run2"""
        self["GUID__"] = UUID('56898367-452f-4f45-8755-49576c42c33c')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """t_"""
        self.vs[0]["mm__"] = """directLink_T"""
        self.vs[0]["GUID__"] = UUID('bec86076-a9b5-4517-9665-fdbd26ff5391')
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = UUID('6ef1ff73-c741-4e5f-bfab-60b8fa5f40bc')
        self.vs[2]["mm__"] = """MatchModel"""
        self.vs[2]["GUID__"] = UUID('7bb68093-d3d5-4296-a26a-5e837841e83a')
        self.vs[3]["name"] = """f"""
        self.vs[3]["classtype"] = """female2"""
        self.vs[3]["mm__"] = """Female_T"""
        self.vs[3]["GUID__"] = UUID('c7b31808-6be8-4610-a1c3-931e35345d12')
        self.vs[4]["mm__"] = """indirectLink_S"""
        self.vs[4]["GUID__"] = UUID('af7ee3ee-ea18-4bcd-a1a4-e92ed44c32af')
        self.vs[5]["name"] = """s"""
        self.vs[5]["classtype"] = """station2"""
        self.vs[5]["mm__"] = """Station_T"""
        self.vs[5]["GUID__"] = UUID('c7903999-e4ee-4bb5-84a1-91279267ce65')
        self.vs[6]["name"] = """s"""
        self.vs[6]["classtype"] = """station2"""
        self.vs[6]["mm__"] = """Station_S"""
        self.vs[6]["cardinality"] = """+"""
        self.vs[6]["GUID__"] = UUID('96ef37ab-b012-4a5a-abf8-d19e6c72e418')
        self.vs[7]["name"] = """f"""
        self.vs[7]["classtype"] = """female2"""
        self.vs[7]["mm__"] = """Female_S"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = UUID('8addb37a-3fd2-403f-be31-b7d3a05253be')
        self.vs[8]["mm__"] = """paired_with"""
        self.vs[8]["GUID__"] = UUID('89b80bf7-b5e1-4594-8bb1-d598f2f3e036')
        self.vs[9]["mm__"] = """apply_contains"""
        self.vs[9]["GUID__"] = UUID('80560c36-5f05-43e5-a12f-d2d9e5b620ce')
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = UUID('edf3b3e9-4218-4a21-b8b1-f11a6d46bb3e')
        self.vs[11]["mm__"] = """backward_link"""
        self.vs[11]["GUID__"] = UUID('62a15628-efce-4c13-84e8-f9e8a7ba9c88')
        self.vs[12]["mm__"] = """backward_link"""
        self.vs[12]["GUID__"] = UUID('07505edc-9db9-4349-b10c-05c167b103bd')
        self.vs[13]["mm__"] = """match_contains"""
        self.vs[13]["GUID__"] = UUID('85da815a-335e-4d03-bc4b-01705e7f0715')
        self.vs[14]["mm__"] = """match_contains"""
        self.vs[14]["GUID__"] = UUID('6dd59a19-8180-4ca2-9b0f-3ef64e4301a3')

