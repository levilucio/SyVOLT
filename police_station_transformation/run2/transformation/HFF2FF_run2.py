

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HFF2FF_run2(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HFF2FF_run2.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HFF2FF_run2, self).__init__(name='HFF2FF_run2', num_nodes=15, edges=[])
        
        # Add the edges
        self.add_edges([(1, 5), (5, 9), (1, 6), (6, 10), (9, 7), (7, 13), (10, 8), (8, 14), (9, 0), (0, 10), (4, 1), (2, 4), (2, 11), (2, 12), (13, 3), (3, 14), (11, 13), (12, 14)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'PoliceStationMM'
p2
a.""")
        self["name"] = """FF2FF_run2"""
        self["GUID__"] = UUID('8d42aa12-ddbc-4dd6-afae-ca79b11038c7')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """t_"""
        self.vs[0]["mm__"] = """directLink_T"""
        self.vs[0]["GUID__"] = UUID('8b6f19eb-5761-4e68-8458-24fa947d09bf')
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = UUID('63db4d53-f691-405e-a7e1-625e4c13a0b7')
        self.vs[2]["mm__"] = """MatchModel"""
        self.vs[2]["GUID__"] = UUID('5cb73ba3-893b-4e23-9ba7-371955bf2bdf')
        self.vs[3]["mm__"] = """indirectLink_S"""
        self.vs[3]["GUID__"] = UUID('944c2f77-6ed5-4e2d-90ef-33265c19c8e1')
        self.vs[4]["mm__"] = """paired_with"""
        self.vs[4]["GUID__"] = UUID('53caa44b-ddeb-4f21-b28c-39ea5e7a1d19')
        self.vs[5]["mm__"] = """apply_contains"""
        self.vs[5]["GUID__"] = UUID('a1e66450-c65b-4af5-8354-fa5c7fcb71ac')
        self.vs[6]["mm__"] = """apply_contains"""
        self.vs[6]["GUID__"] = UUID('dede3a26-a914-4737-8cf5-7abbf9418bfb')
        self.vs[7]["mm__"] = """backward_link"""
        self.vs[7]["GUID__"] = UUID('227e8f25-6760-4a8d-8922-71931a8bf637')
        self.vs[8]["mm__"] = """backward_link"""
        self.vs[8]["GUID__"] = UUID('eaad9819-a8a0-4b75-bdd0-09b8c66c791a')
        self.vs[9]["name"] = """f1"""
        self.vs[9]["classtype"] = """female2"""
        self.vs[9]["mm__"] = """Female_T"""
        self.vs[9]["GUID__"] = UUID('6e798c79-835d-462b-9fe8-f52dfc92eda8')
        self.vs[10]["name"] = """f2"""
        self.vs[10]["classtype"] = """female2"""
        self.vs[10]["mm__"] = """Female_T"""
        self.vs[10]["GUID__"] = UUID('22dd8498-3f57-417e-a130-29cff6dc7f2c')
        self.vs[11]["mm__"] = """match_contains"""
        self.vs[11]["GUID__"] = UUID('c14d865a-a4bc-4967-aca5-ade79f4f9d3e')
        self.vs[12]["mm__"] = """match_contains"""
        self.vs[12]["GUID__"] = UUID('48af41c9-a15a-4ea8-8a74-9db7b011fc9c')
        self.vs[13]["name"] = """f1"""
        self.vs[13]["classtype"] = """female2"""
        self.vs[13]["mm__"] = """Female_S"""
        self.vs[13]["cardinality"] = """+"""
        self.vs[13]["GUID__"] = UUID('9dba44bd-0869-4b59-97dc-914ac34e7420')
        self.vs[14]["name"] = """f2"""
        self.vs[14]["classtype"] = """female2"""
        self.vs[14]["mm__"] = """Female_S"""
        self.vs[14]["cardinality"] = """+"""
        self.vs[14]["GUID__"] = UUID('92d840c5-4c27-495f-9a3d-1ebfc8bcdf07')

