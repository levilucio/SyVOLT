

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HF2F_run3(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HF2F_run3.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HF2F_run3, self).__init__(name='HF2F_run3', num_nodes=7, edges=[])
        
        # Add the edges
        self.add_edges([(1, 0), (0, 3), (6, 1), (2, 6), (2, 4), (4, 5)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'PoliceStationMM'
p2
a.""")
        self["name"] = """F2F_run3"""
        self["GUID__"] = UUID('1af2b3a7-a3ef-48a9-b331-cf0a76d04d6c')
        
        # Set the node attributes
        self.vs[0]["mm__"] = """apply_contains"""
        self.vs[0]["GUID__"] = UUID('58eb350f-5021-4f87-a5d7-5d4ea60b442c')
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = UUID('f6024ede-c5cf-425a-aa68-a1c99a32704f')
        self.vs[2]["mm__"] = """MatchModel"""
        self.vs[2]["GUID__"] = UUID('bea90665-55db-4fea-b81c-f1809d26acda')
        self.vs[3]["mm__"] = """Female_T"""
        self.vs[3]["classtype"] = """female3"""
        self.vs[3]["name"] = """f"""
        self.vs[3]["GUID__"] = UUID('c2ee62f4-d174-455b-aa26-25cfc96185a2')
        self.vs[4]["mm__"] = """match_contains"""
        self.vs[4]["GUID__"] = UUID('c7989c46-ae8f-4728-ad4c-c26ac5dec310')
        self.vs[5]["mm__"] = """Female_S"""
        self.vs[5]["classtype"] = """female3"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["name"] = """f"""
        self.vs[5]["GUID__"] = UUID('b7f42be6-261c-4a4c-afd2-05a7a2544795')
        self.vs[6]["mm__"] = """paired_with"""
        self.vs[6]["GUID__"] = UUID('f32075c0-2f90-4812-bdd4-3cc213326ef3')

