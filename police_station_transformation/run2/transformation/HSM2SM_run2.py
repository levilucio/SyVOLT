

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HSM2SM_run2(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HSM2SM_run2.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HSM2SM_run2, self).__init__(name='HSM2SM_run2', num_nodes=15, edges=[])
        
        # Add the edges
        self.add_edges([(1, 9), (9, 5), (1, 10), (10, 7), (5, 11), (11, 6), (7, 12), (12, 4), (5, 0), (0, 7), (8, 1), (2, 8), (2, 13), (2, 14), (6, 3), (3, 4), (13, 6), (14, 4)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'PoliceStationMM'
p2
a.""")
        self["name"] = """SM2SM_run2"""
        self["GUID__"] = UUID('d2f2bfb1-dee8-4e19-ac6d-9ec4fc7ce2ed')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """t_"""
        self.vs[0]["mm__"] = """directLink_T"""
        self.vs[0]["GUID__"] = UUID('8fd73996-b102-4ee3-882e-47f8e7afbabf')
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = UUID('75f54268-8b73-444d-8d8e-f5fe68b3b55c')
        self.vs[2]["mm__"] = """MatchModel"""
        self.vs[2]["GUID__"] = UUID('9aad21ac-1b37-423f-ab11-8df8c5706f2f')
        self.vs[3]["mm__"] = """indirectLink_S"""
        self.vs[3]["GUID__"] = UUID('6b0b3529-8722-4889-a63f-27870bc965ef')
        self.vs[4]["name"] = """m"""
        self.vs[4]["classtype"] = """male2"""
        self.vs[4]["mm__"] = """Male_S"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = UUID('5be34ccc-92a7-477d-9437-3523877d6984')
        self.vs[5]["name"] = """s"""
        self.vs[5]["classtype"] = """station2"""
        self.vs[5]["mm__"] = """Station_T"""
        self.vs[5]["GUID__"] = UUID('cac34c91-a7c6-4b7f-a324-1d7e773b82e9')
        self.vs[6]["name"] = """s"""
        self.vs[6]["classtype"] = """station2"""
        self.vs[6]["mm__"] = """Station_S"""
        self.vs[6]["cardinality"] = """+"""
        self.vs[6]["GUID__"] = UUID('926c95e7-e2c2-439f-88f5-ec439de0b1d0')
        self.vs[7]["name"] = """m"""
        self.vs[7]["classtype"] = """male2"""
        self.vs[7]["mm__"] = """Male_T"""
        self.vs[7]["GUID__"] = UUID('91f9ee58-879f-42a1-a7cd-dda31d19af60')
        self.vs[8]["mm__"] = """paired_with"""
        self.vs[8]["GUID__"] = UUID('2bec9607-541a-4073-9180-3c4ed0420059')
        self.vs[9]["mm__"] = """apply_contains"""
        self.vs[9]["GUID__"] = UUID('7bef2304-0631-4ac2-9f91-5863a97d02a7')
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = UUID('62183fe8-ac51-4a18-9e55-5a5ad047f829')
        self.vs[11]["mm__"] = """backward_link"""
        self.vs[11]["GUID__"] = UUID('b3ccef80-ab6f-4089-88b4-f66549a74625')
        self.vs[12]["mm__"] = """backward_link"""
        self.vs[12]["GUID__"] = UUID('1fd248ec-a1e5-403a-9eae-a133d5bb317e')
        self.vs[13]["mm__"] = """match_contains"""
        self.vs[13]["GUID__"] = UUID('59b802cb-4a3e-4f18-878a-c6687eda7435')
        self.vs[14]["mm__"] = """match_contains"""
        self.vs[14]["GUID__"] = UUID('cdefc43a-4926-4d02-8f81-b6df97bb5af2')

