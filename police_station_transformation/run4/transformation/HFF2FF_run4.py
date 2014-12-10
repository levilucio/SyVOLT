

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HFF2FF_run4(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HFF2FF_run4.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HFF2FF_run4, self).__init__(name='HFF2FF_run4', num_nodes=15, edges=[])
        
        # Add the edges
        self.add_edges([(1, 5), (5, 9), (1, 6), (6, 10), (9, 7), (7, 13), (10, 8), (8, 14), (9, 0), (0, 10), (4, 1), (2, 4), (2, 11), (2, 12), (13, 3), (3, 14), (11, 13), (12, 14)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'PoliceStationMM'
p2
a.""")
        self["name"] = """FF2FF_run4"""
        self["GUID__"] = UUID('32113fc3-218d-4bb6-b811-d67aba1d61f5')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """t_"""
        self.vs[0]["mm__"] = """directLink_T"""
        self.vs[0]["GUID__"] = UUID('4a2bd36f-c25f-4770-945b-57e08758529f')
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = UUID('3c7c3c2c-eb1a-4cad-ba75-84e330561fe9')
        self.vs[2]["mm__"] = """MatchModel"""
        self.vs[2]["GUID__"] = UUID('77ca23d6-a316-4813-a689-0ba1ac18dd79')
        self.vs[3]["mm__"] = """indirectLink_S"""
        self.vs[3]["GUID__"] = UUID('63cbe20f-ff81-4465-b9db-1b8836541279')
        self.vs[4]["mm__"] = """paired_with"""
        self.vs[4]["GUID__"] = UUID('b13ff4e1-789c-4cca-ac9c-0605c7d4d50a')
        self.vs[5]["mm__"] = """apply_contains"""
        self.vs[5]["GUID__"] = UUID('f0eeb6c2-2a11-4afc-95ea-8bc2fb49d5ce')
        self.vs[6]["mm__"] = """apply_contains"""
        self.vs[6]["GUID__"] = UUID('26c1ee74-0756-47f6-837e-89fd7de5a984')
        self.vs[7]["mm__"] = """backward_link"""
        self.vs[7]["GUID__"] = UUID('37fc5367-97ac-4e93-8449-52a9572bf3c5')
        self.vs[8]["mm__"] = """backward_link"""
        self.vs[8]["GUID__"] = UUID('fa6c97d7-87ef-4a74-a879-bc77636815b8')
        self.vs[9]["name"] = """f1"""
        self.vs[9]["classtype"] = """female4"""
        self.vs[9]["mm__"] = """Female_T"""
        self.vs[9]["GUID__"] = UUID('926d5092-1b09-446e-bdd1-3e68e35a1a11')
        self.vs[10]["name"] = """f2"""
        self.vs[10]["classtype"] = """female4"""
        self.vs[10]["mm__"] = """Female_T"""
        self.vs[10]["GUID__"] = UUID('9023eac2-db1b-489d-a200-f4032f295e36')
        self.vs[11]["mm__"] = """match_contains"""
        self.vs[11]["GUID__"] = UUID('248acc76-ca5c-4d38-b8ca-50e53bd4aee7')
        self.vs[12]["mm__"] = """match_contains"""
        self.vs[12]["GUID__"] = UUID('c81330f1-e1d8-45dc-a749-c9f19bdcb1b2')
        self.vs[13]["name"] = """f1"""
        self.vs[13]["classtype"] = """female4"""
        self.vs[13]["mm__"] = """Female_S"""
        self.vs[13]["cardinality"] = """+"""
        self.vs[13]["GUID__"] = UUID('98698917-8219-4bb3-8d41-df7aef87b345')
        self.vs[14]["name"] = """f2"""
        self.vs[14]["classtype"] = """female4"""
        self.vs[14]["mm__"] = """Female_S"""
        self.vs[14]["cardinality"] = """+"""
        self.vs[14]["GUID__"] = UUID('bf1c80a5-bdbd-4da2-a1a5-c7984bcf6271')

